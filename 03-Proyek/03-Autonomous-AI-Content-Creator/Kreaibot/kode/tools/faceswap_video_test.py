#!/usr/bin/env python3
"""Uji: apakah app FACE SWAP kita menerima VIDEO sebagai node '模特/Model' (145)?

Kalau YA → kita otomatis punya fitur "Face Swap & Motion" (andalan Kuzushi, 2 Token):
gerak diambil dari footage nyata + wajah user ditransfer.

Pakai: .venv/bin/python tools/faceswap_video_test.py [video_sumber]
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

    face = ROOT / "work/tests/ref1.jpg"
    vid = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        ROOT / "work/tests/backend_i2v_10s__ComfyUI_ZIP_video_00000.mp4"
    out = ROOT / "work/tests/faceswap_video_probe.mp4"
    if not vid.exists():
        print("video sumber tidak ada:", vid)
        return 2
    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=556, feature_key="faceswap", workflow="",
                     photos=[face], video_in=vid, prompt="", ratio="9:16",
                     duration=10, out_path=out)
    t0 = time.time()
    print(f"▶️ faceswap dengan VIDEO: face={face.name} video={vid.name} ({vid.stat().st_size} B)", flush=True)
    tid = await be.submit(req)
    print("task:", tid, flush=True)
    while True:
        st = await be.poll(tid)
        print(f"t+{int(time.time()-t0)}s {st.state} {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(5)
    print("state:", st.state, "err:", st.error, flush=True)
    if st.result_path:
        print("URL:", st.result_path, flush=True)
        urllib.request.urlretrieve(st.result_path, out)
        print("saved:", out, out.stat().st_size, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))