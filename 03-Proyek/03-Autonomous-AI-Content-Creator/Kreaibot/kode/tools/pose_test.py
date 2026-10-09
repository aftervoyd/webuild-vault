#!/usr/bin/env python3
"""Uji jalur PRODUKSI fitur POSE (Pose Transfer & Style) — FOTO orang + FOTO pose → gambar.

App: 2038158176293494785 "姿势迁移！动作姿势迁移，超强人物一致性"
Node: 24=人物图(orang) · 31=姿势图(pose) · 51=人脸相似度(index, default app)

Pakai: .venv/bin/python tools/pose_test.py [foto_orang] [foto_pose]
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

    orang = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/tests/ref1.jpg"
    pose = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "work/tests/motion_frames/m2.jpg"
    out = ROOT / "work/tests/pose_hasil.png"

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=601, feature_key="pose", workflow="",
                     photos=[orang, pose], prompt="", ratio="9:16",
                     duration=5, out_path=out)
    t0 = time.time()
    print(f"▶️ POSE · orang={orang.name} · pose={pose.name}", flush=True)
    tid = await be.submit(req)
    print("task:", tid, flush=True)
    while True:
        st = await be.poll(tid)
        print(f"t+{int(time.time()-t0)}s {st.state} {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(6)
    print("state:", st.state, "err:", st.error, "t:", int(time.time() - t0), "s", flush=True)
    if st.result_path:
        print("URL:", st.result_path, flush=True)
        urllib.request.urlretrieve(st.result_path, out)
        print("saved:", out, out.stat().st_size, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))