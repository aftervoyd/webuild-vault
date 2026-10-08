#!/usr/bin/env python3
"""Uji BINDING node workflow RunningHub langsung (tanpa lewat bot).

Untuk eksperimen: node mana yang jadi "first frame", mana "last frame", dan
apakah frame default workflow bocor ke hasil.

Pakai:
  .venv/bin/python tools/rh_test_bind.py --name t1 --photo <foto> --duration 5 \
        --ratio 9:16 --first 6 --last 4 --last-mode same|zoom|none --prompt "..."

  --first/--last = nodeId LoadImage untuk frame pertama/terakhir
  --last-mode same → frame terakhir = foto yang sama
  --last-mode zoom → frame terakhir = foto sama di-zoom 1.12x (biar ada gerakan)
  --last-mode none → node terakhir TIDAK diisi → bakal pakai default workflow (bug)

Hasil: work/tests/<name>.mp4 + <name>-sheet.jpg (6 frame) + biaya/waktu task.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import aiohttp                                                    # noqa: E402
from dotenv import load_dotenv                                     # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("RUNNINGHUB_API_KEY", "")
BASE = (os.getenv("RUNNINGHUB_BASE") or "https://www.runninghub.ai").rstrip("/")
WF = os.getenv("RUNNINGHUB_WF_UGC", "")
OUT_DIR = ROOT / "work" / "tests"
RATIO_SIZES = {"9:16": (480, 832), "16:9": (832, 480), "1:1": (640, 640),
               "4:3": (832, 480), "3:4": (480, 640)}


async def _post(path: str, payload: dict) -> dict:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as s:
        async with s.post(f"{BASE}{path}", json=payload,
                          headers={"Authorization": f"Bearer {API_KEY}"}) as r:
            return await r.json(content_type=None)


async def upload(p: Path) -> str:
    data = aiohttp.FormData()
    data.add_field("apiKey", API_KEY)
    data.add_field("fileType", "image")
    data.add_field("file", p.read_bytes(), filename=p.name,
                   content_type="application/octet-stream")
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300)) as s:
        async with s.post(f"{BASE}/task/openapi/upload", data=data,
                          headers={"Authorization": f"Bearer {API_KEY}"}) as r:
            js = await r.json(content_type=None)
    d = js.get("data") if isinstance(js, dict) else None
    name = ""
    if isinstance(d, dict):
        for k in ("fileName", "file", "name"):
            v = d.get(k)
            if isinstance(v, str) and v:
                name = v
                break
            if isinstance(v, list) and v:
                name = str(v[0])
                break
    if not name:
        raise RuntimeError(f"upload gagal: {js}")
    return name


def make_zoom_variant(src: Path, dst: Path, ratio: str) -> Path:
    """Buat 'frame terakhir' = foto yang sama tapi di-zoom & digeser dikit."""
    from PIL import Image
    w, h = RATIO_SIZES.get(ratio, (480, 832))
    im = Image.open(src).convert("RGB")
    # cover ke ukuran target dulu
    sw, sh = im.size
    sc = max(w / sw, h / sh)
    im = im.resize((int(sw * sc), int(sh * sc)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    im = im.crop((x, y, x + w, y + h))
    # zoom 1.12x (push-in) → gerakan halus buat model
    zw, zh = int(w / 1.12), int(h / 1.12)
    zx, zy = (w - zw) // 2, (h - zh) // 2
    im.crop((zx, zy, zx + zw, zy + zh)).resize((w, h), Image.LANCZOS).save(dst, quality=92)
    return dst


def frames_sheet(mp4: Path, name: str) -> Path | None:
    from PIL import Image, ImageDraw
    dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
        capture_output=True, text=True).stdout.strip() or 0)
    ts = [0, dur * 0.1, dur * 0.25, dur * 0.5, dur * 0.75, max(dur - 0.3, 0)]
    tmp = OUT_DIR / f"_{name}_frames"
    tmp.mkdir(parents=True, exist_ok=True)
    ims, labels = [], []
    for i, t in enumerate(ts):
        f = tmp / f"f{i}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(mp4),
                        "-frames:v", "1", "-q:v", "4", "-vf", "scale=200:-1", str(f), "-y"],
                       capture_output=True)
        if f.exists():
            ims.append(Image.open(f))
            labels.append(f"t={t:.1f}s")
    if not ims:
        return None
    W = sum(i.width for i in ims)
    H = max(i.height for i in ims)
    sheet = Image.new("RGB", (W, H + 20), "white")
    d = ImageDraw.Draw(sheet)
    x = 0
    for i, lab in zip(ims, labels):
        sheet.paste(i, (x, 20))
        d.text((x + 3, 5), lab, fill="black")
        x += i.width
    out = OUT_DIR / f"{name}-sheet.jpg"
    sheet.save(out, quality=86)
    return out


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--photo", required=True)
    ap.add_argument("--prompt", default="Subtle natural motion, the subject moves slightly, "
                                        "soft handheld camera push-in, cinematic.")
    ap.add_argument("--ratio", default="9:16")
    ap.add_argument("--duration", type=int, default=5)
    ap.add_argument("--first", dest="first", default="6")
    ap.add_argument("--last", dest="last", default="4")
    ap.add_argument("--last-mode", choices=["same", "zoom", "none", "empty"], default="same")
    ap.add_argument("--poll", type=int, default=900)
    a = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    src = Path(a.photo)
    w, h = RATIO_SIZES.get(a.ratio, (480, 832))
    print(f"▶ {a.name}: wf={WF} ratio={a.ratio} ({w}x{h}) dur={a.duration}s "
          f"first=node{a.first} last=node{a.last}({a.last_mode})")

    up_main = await upload(src)
    print(f"  upload ✔ {src.name} → {up_main[:40]}…")

    nodes = [{"nodeId": str(a.first), "fieldName": "image", "fieldValue": up_main}]
    if a.last_mode == "same":
        nodes.append({"nodeId": str(a.last), "fieldName": "image", "fieldValue": up_main})
    elif a.last_mode == "zoom":
        zv = make_zoom_variant(src, OUT_DIR / f"{a.name}-last.jpg", a.ratio)
        nodes.append({"nodeId": str(a.last), "fieldName": "image",
                      "fieldValue": await upload(zv)})
    # last_mode == none → sengaja kosong (untuk membuktikan bocornya default)
    if a.last_mode == "empty":
        # node terakhir dikirim dengan NILAI KOSONG → harapan: workflow menganggap
        # "tidak ada frame terakhir" (i2v bebas beranimasi) tanpa pakai sampel default.
        nodes.append({"nodeId": str(a.last), "fieldName": "image", "fieldValue": ""})
    nodes += [{"nodeId": "8", "fieldName": "prompt", "fieldValue": a.prompt},
              {"nodeId": "7", "fieldName": "aspect_ratio", "fieldValue": a.ratio},
              {"nodeId": "7", "fieldName": "duration_seconds", "fieldValue": str(a.duration)},
              {"nodeId": "7", "fieldName": "width", "fieldValue": str(w)},
              {"nodeId": "7", "fieldName": "height", "fieldValue": str(h)}]

    js = await _post("/task/openapi/create", {"apiKey": API_KEY, "workflowId": WF,
                                              "nodeInfoList": nodes})
    tid = str((js.get("data") or {}).get("taskId") if isinstance(js.get("data"), dict)
              else js.get("data") or "")
    if not tid:
        print(f"  ❌ create gagal: {json.dumps(js)[:300]}")
        return 1
    print(f"  task: {tid}")

    t0 = time.time()
    out_url = None
    while time.time() - t0 < a.poll:
        await asyncio.sleep(8)
        st = await _post("/task/openapi/status", {"apiKey": API_KEY, "taskId": tid})
        state = str(st.get("data") or "").upper()
        el = time.time() - t0
        print(f"     t+{el:5.0f}s  {state}")
        if state in ("SUCCESS", "SUCCEEDED", "DONE", "COMPLETED"):
            o = await _post("/task/openapi/outputs", {"apiKey": API_KEY, "taskId": tid})
            item = (o.get("data") or [{}])[0] if isinstance(o.get("data"), list) else (o.get("data") or {})
            out_url = item.get("fileUrl") or item.get("url")
            cost = item.get("consumeCoins")
            ctime = item.get("taskCostTime")
            print(f"  ✅ selesai dalam {el:.0f}s · biaya={cost} koin · taskCostTime={ctime}s")
            break
        if state in ("FAILED", "ERROR"):
            print(f"  ❌ gagal: {json.dumps(st)[:300]}")
            return 2

    if not out_url:
        print("  ⚠️ timeout tanpa output")
        return 3

    mp4 = OUT_DIR / f"{a.name}.mp4"
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300)) as s:
        async with s.get(out_url) as r:
            mp4.write_bytes(await r.read())
    print(f"  ⬇️  {mp4} ({mp4.stat().st_size/1e6:.2f} MB)")

    sheet = frames_sheet(mp4, a.name)
    if sheet:
        print(f"  🖼️  {sheet}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))