#!/usr/bin/env python3
"""Uji jalur PRODUKSI fitur MOTION (Wan2.2 Animate) — foto karakter + video gerakan → video.

App: 2039639280896708610 "New Wan2.2 Animate Motion Transfer"
Node: 484=主图(foto) · 488=video sumber gerak · 476=秒数(durasi) · 482=resolusi(3=vertikal 720p)
      478=姿势(1=vitpose) · 475=帧率(16)

Pakai: .venv/bin/python tools/motion_test.py [durasi] [foto] [video]
"""
from __future__ import annotations

import asyncio
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv      # noqa: E402

load_dotenv(ROOT / ".env")


async def main() -> int:
    from backends import GenRequest
    from backends.runninghub import RunningHubBackend

    dur = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    foto = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "work/tests/ref1.jpg"
    vid = Path(sys.argv[3]) if len(sys.argv) > 3 else \
        ROOT / "work/tests/backend_i2v_10s__ComfyUI_ZIP_video_00000.mp4"
    out = ROOT / f"work/tests/motion_{dur}s.mp4"

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=558, feature_key="motion", workflow="",
                     photos=[foto], video_in=vid, prompt="", ratio="9:16",
                     duration=dur, out_path=out)
    t0 = time.time()
    print(f"▶️ MOTION {dur}s · foto={foto.name} · video={vid.name}", flush=True)
    tid = await be.submit(req)
    print("task:", tid, flush=True)
    while True:
        st = await be.poll(tid)
        print(f"t+{int(time.time()-t0)}s {st.state} {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(6)
    print("state:", st.state, "err:", st.error, "t:", int(time.time()-t0), "s", flush=True)
    if st.result_path:
        print("URL:", st.result_path, flush=True)
        urllib.request.urlretrieve(st.result_path, out)
        print("saved:", out, out.stat().st_size, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))