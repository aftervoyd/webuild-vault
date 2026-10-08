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
import os
from pathlib import Path

import aiohttp

from . import GenRequest, GenStatus

DEFAULT_BASE = "https://www.runninghub.ai"


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
            async with s.post(url, json=payload) as r:
                return await r.json(content_type=None)

    async def upload(self, file_path: Path) -> str:
        """Upload aset ke RunningHub, balikin nama file di server mereka."""
        url = f"{self.base}/task/openapi/upload"
        data = aiohttp.FormData()
        data.add_field("apiKey", self.api_key)
        data.add_field("file", Path(file_path).read_bytes(),
                       filename=Path(file_path).name, content_type="application/octet-stream")
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300)) as s:
            async with s.post(url, data=data) as r:
                js = await r.json(content_type=None)
        # struktur umum: {"code":0,"data":{"fileName":"..."}}
        if isinstance(js, dict) and isinstance(js.get("data"), dict):
            return str(js["data"].get("fileName") or js["data"].get("file") or "")
        return ""

    def _bind(self, bindings: list[dict], req: GenRequest, uploaded: list[str]) -> list[dict]:
        out: list[dict] = []
        for b in bindings:
            val = str(b.get("value", ""))
            if val.startswith("@photo"):
                idx = int(val.replace("@photo", "") or "1") - 1
                val = uploaded[idx] if idx < len(uploaded) else ""
            elif val == "@prompt":
                val = req.prompt
            elif val == "@ratio":
                val = req.ratio
            elif val == "@video":
                val = uploaded[-1] if uploaded else ""
            if val == "":
                continue
            out.append({"nodeId": str(b.get("nodeId", "")),
                        "fieldName": str(b.get("fieldName", "text")),
                        "fieldValue": val})
        return out

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

        payload = {"apiKey": self.api_key, "workflowId": wf,
                   "nodeInfoList": self._bind(self._node_bindings(req.feature_key), req, uploaded)}
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
    def _output_url(js: dict) -> Path | None:
        """Ambil URL hasil pertama (dipakai worker untuk download)."""
        try:
            d = js.get("data")
            items = d if isinstance(d, list) else [d]
            for it in items:
                if isinstance(it, dict):
                    url = it.get("fileUrl") or it.get("url")
                    if url:
                        return Path(str(url))          # URL disimpan sebagai "path"
        except Exception:
            pass
        return None