"""RunningHub adapter — backend ComfyUI-cloud (sama seperti yang dipakai kompetitor).

Alur: upload aset -> create task (workflowId + node bindings) -> poll status -> ambil output.

Konfigurasi (di .env):
  RUNNINGHUB_API_KEY=...
  RUNNINGHUB_BASE=https://www.runninghub.ai
  RUNNINGHUB_WF_ALLINONE=1234567890          # workflowId di akun kamu
  RUNNINGHUB_NODES_ALLINONE=[{"nodeId":"12","fieldName":"image","value":"@photo1"},
                             {"nodeId":"13","fieldName":"image","value":"@photo2"},
                             {"nodeId":"20","fieldName":"text","value":"@prompt"},
                             {"nodeId":"21","fieldName":"text","value":"@ratio"}]

Placeholder yang dikenali di "value": @photo1..@photo6, @prompt, @ratio, @video
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
from pathlib import Path

import aiohttp

from . import GenRequest, GenStatus

log = logging.getLogger("kreaibot")
DEFAULT_BASE = "https://www.runninghub.ai"


RATIO_SIZES: dict[str, tuple[int, int]] = {
    "9:16": (480, 832),
    "16:9": (832, 480),
    "1:1": (640, 640),
    "4:3": (832, 480),      # default workflow FL2VA
    "3:4": (480, 640),
}


class RunningHubBackend:
    name = "runninghub"

    def __init__(self, api_key: str = "", base: str = DEFAULT_BASE,
                 work_dir: str = ".", **_: object):
        self.api_key = api_key or os.getenv("RUNNINGHUB_API_KEY", "")
        self.base = (base or DEFAULT_BASE).rstrip("/")
        self.work_dir = Path(work_dir)

    # ---------- helpers ----------
    def _workflow_id(self, feature_key: str) -> str:
        return os.getenv(f"RUNNINGHUB_WF_{feature_key.upper()}", "")

    def _node_bindings(self, feature_key: str) -> list[dict]:
        raw = os.getenv(f"RUNNINGHUB_NODES_{feature_key.upper()}", "[]")
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return []

    async def _post(self, path: str, payload: dict) -> dict:
        url = f"{self.base}{path}"
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as s:
            async with s.post(url, json=payload,
                              headers={"Authorization": f"Bearer {self.api_key}"}) as r:
                return await r.json(content_type=None)

    async def upload(self, file_path: Path) -> str:
        """Upload aset ke RunningHub, balikin nama file di server mereka.

        Kirim juga `fileType` (image/video/audio) + header Bearer, dan coba
        endpoint baru lalu lama — beberapa versi API minta kombinasi berbeda.
        """
        p = Path(file_path)
        ext = p.suffix.lower().lstrip(".")
        if ext in ("mp4", "mov", "webm", "mkv", "avi"):
            kind = "video"
        elif ext in ("mp3", "wav", "m4a", "aac", "flac", "ogg"):
            kind = "audio"
        else:
            kind = "image"

        last_err: object = None
        for path in ("/task/openapi/upload", "/task/openapi/fileUpload"):
            try:
                data = aiohttp.FormData()
                data.add_field("apiKey", self.api_key)
                data.add_field("fileType", kind)
                data.add_field("file", p.read_bytes(), filename=p.name,
                               content_type="application/octet-stream")
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300)) as s:
                    async with s.post(f"{self.base}{path}", data=data,
                                      headers={"Authorization": f"Bearer {self.api_key}"}) as r:
                        js = await r.json(content_type=None)
            except Exception as e:                      # noqa: BLE001
                last_err = e
                continue
            name = self._pick_name(js)
            if name:
                return name
            last_err = js
        raise RuntimeError(f"upload ke RunningHub gagal ({p.name}): {last_err}")

    @staticmethod
    def _pick_name(js: object) -> str:
        """Ambil nama file dari berbagai bentuk respons upload."""
        d = js.get("data") if isinstance(js, dict) else None
        if isinstance(d, dict):
            for k in ("fileName", "file", "name", "fileNameList"):
                v = d.get(k)
                if isinstance(v, list) and v:
                    return str(v[0])
                if isinstance(v, str) and v:
                    return v
        if isinstance(d, list) and d:
            return str(d[0])
        return ""

    def _bind(self, bindings: list[dict], req: GenRequest, uploaded: list[str],
              extra: dict[str, str] | None = None) -> list[dict]:
        out: list[dict] = []
        extra = extra or {}
        for b in bindings:
            val = str(b.get("value", ""))
            if val in extra:                        # mis. @photo1_zoom (sudah diunggah terpisah)
                val = extra[val]
            elif val.startswith("@photo"):
                idx = int(val.replace("@photo", "") or "1") - 1
                val = uploaded[idx] if idx < len(uploaded) else ""
            elif val == "@prompt":
                val = req.prompt
            elif val == "@ratio":
                val = req.ratio
            elif val == "@duration":
                d = getattr(req, "duration", 0) or 0
                if not d:
                    d = int(os.getenv(f"RUNNINGHUB_DURATION_{req.feature_key.upper()}",
                                      os.getenv("RUNNINGHUB_DEFAULT_DURATION", "5")) or 5)
                val = str(d)
            elif val in ("@width", "@height"):
                w, h = RATIO_SIZES.get(req.ratio.replace(" ", ""), (480, 832))
                val = str(w if val == "@width" else h)
            elif val == "@video":
                val = uploaded[-1] if uploaded else ""
            if val == "":
                continue
            out.append({"nodeId": str(b.get("nodeId", "")),
                        "fieldName": str(b.get("fieldName", "text")),
                        "fieldValue": val})
        return out

    ZOOM_FACTOR = 1.12          # push-in halus untuk "frame akhir" i2v

    def _zoom_variant(self, src: Path, ratio: str, tag: str) -> Path | None:
        """Foto yang sama di-zoom ~1.12x (ke arah tengah) → dipakai sebagai frame akhir.

        Hasil tes nyata: dengan frame awal = frame akhir = foto identik, model cuma
        me-morph ekspresi (nyaris statis); kalau frame akhir di-zoom, gerakannya jadi
        push-in kamera yang natural. Foto ASLI tetap dipakai di frame awal.
        """
        try:
            from PIL import Image
        except ImportError:                     # Pillow tak ada → lewati (pakai foto asli)
            return None
        w, h = RATIO_SIZES.get((ratio or "").replace(" ", ""), (480, 832))
        try:
            im = Image.open(src).convert("RGB")
            sw, sh = im.size
            sc = max(w / sw, h / sh)
            im = im.resize((max(int(sw * sc), w), max(int(sh * sc), h)), Image.LANCZOS)
            x, y = (im.width - w) // 2, (im.height - h) // 2
            im = im.crop((x, y, x + w, y + h))
            zw, zh = int(w / self.ZOOM_FACTOR), int(h / self.ZOOM_FACTOR)
            zx, zy = (w - zw) // 2, (h - zh) // 2
            out = self.work_dir / f"{tag}.jpg"
            im.crop((zx, zy, zx + zw, zy + zh)).resize((w, h), Image.LANCZOS).save(out, quality=92)
            return out
        except Exception:                       # noqa: BLE001
            return None

    # ---------- kontrak Backend ----------
    async def submit(self, req: GenRequest) -> str:
        wf = self._workflow_id(req.feature_key)
        if not wf:
            raise RuntimeError(f"workflowId untuk '{req.feature_key}' belum diisi "
                               f"(RUNNINGHUB_WF_{req.feature_key.upper()})")
        assets = list(req.photos) + ([req.video_in] if req.video_in else [])
        uploaded: list[str] = []
        for p in assets:
            uploaded.append(await self.upload(Path(p)))

        # Placeholder @photoN_zoom → foto ke-N di-zoom (bukti: "frame akhir" ber-zoom
        # bikin gerakan push-in; kalau identik, video jadi nyaris statis).
        extra: dict[str, str] = {}
        for b in self._node_bindings(req.feature_key):
            val = str(b.get("value", ""))
            if val.startswith("@photo") and val.endswith("_zoom"):
                idx = int(val[len("@photo"):-len("_zoom")] or "1") - 1
                if 0 <= idx < len(req.photos):
                    zv = self._zoom_variant(Path(req.photos[idx]), req.ratio,
                                            f"{Path(req.photos[idx]).stem}-zoom")
                    if zv:
                        try:
                            extra[val] = await self.upload(zv)
                        except Exception as e:          # noqa: BLE001
                            log.warning("upload zoom-variant gagal (%s) → pakai foto asli", e)

        payload = {"apiKey": self.api_key, "workflowId": wf,
                   "nodeInfoList": self._bind(self._node_bindings(req.feature_key), req, uploaded, extra)}
        js = await self._post("/task/openapi/create", payload)
        task_id = ""
        if isinstance(js, dict):
            d = js.get("data")
            task_id = str(d.get("taskId") if isinstance(d, dict) else d or "")
        if not task_id:
            raise RuntimeError(f"gagal membuat task RunningHub: {js}")
        return task_id

    async def poll(self, task_id: str) -> GenStatus:
        st = await self._post("/task/openapi/status", {"apiKey": self.api_key, "taskId": task_id})
        data = st.get("data") if isinstance(st, dict) else None
        state_raw = ""
        if isinstance(data, dict):
            state_raw = str(data.get("status") or data.get("taskStatus") or "")
        elif isinstance(data, str):
            state_raw = data
        state_raw = state_raw.upper()

        if state_raw in ("SUCCESS", "SUCCEEDED", "COMPLETED", "DONE"):
            out = await self._post("/task/openapi/outputs", {"apiKey": self.api_key, "taskId": task_id})
            return GenStatus(state="done", progress=100, message="selesai",
                             result_path=self._output_url(out))
        if state_raw in ("FAILED", "ERROR"):
            return GenStatus(state="failed", error=json.dumps(st)[:400])
        if state_raw in ("QUEUED", "PENDING", ""):
            return GenStatus(state="queued", progress=5, message="dalam antrean cloud")
        return GenStatus(state="running", progress=60, message="merender di cloud")

    @staticmethod
    def _output_url(js: dict) -> str | None:
        """Ambil URL hasil pertama.

        ⚠️ JANGAN dibungkus Path(): Path("https://x/y") menormalisasi jadi
        "https:/x/y" → urllib gagal dengan 'no host given'.
        """
        try:
            d = js.get("data")
            items = d if isinstance(d, list) else [d]
            for it in items:
                if isinstance(it, dict):
                    url = it.get("fileUrl") or it.get("url")
                    if url:
                        return str(url)
        except Exception:
            pass
        return None