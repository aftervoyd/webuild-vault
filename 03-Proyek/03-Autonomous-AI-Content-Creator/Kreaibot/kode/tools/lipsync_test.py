#!/usr/bin/env python3
"""Uji jalur PRODUKSI fitur LIPSYNC (LTX 2.3 Digital Human) — FOTO + AUDIO → video orang ngomong.

App: 2031016553440878594 "LTX2.3数字人说话唱歌对口型" (1280p, 25-30fps, ~5 menit/10 detik)
Node: 444=人物图(foto) · 1755=音频(audio) · 1583=秒数 · 1776=audio offset
      1624=动作提示词 · 1606=最大分辨率(1280) · 1586=帧率(25)

Pakai: .venv/bin/python tools/lipsync_test.py [durasi] [foto] [audio]
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

    dur = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    foto = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "work/tests/ref1.jpg"
    audio = Path(sys.argv[3]) if len(sys.argv) > 3 else ROOT / "work/motions/vo_test_id.mp3"
    out = ROOT / f"work/tests/lipsync_{dur}s.mp4"

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=599, feature_key="lipsync", workflow="",
                     photos=[foto], video_in=audio, prompt="", ratio="9:16",
                     duration=dur, out_path=out)
    t0 = time.time()
    print(f"▶️ LIPSYNC {dur}s · foto={foto.name} · audio={audio.name}", flush=True)
    tid = await be.submit(req)
    print("task:", tid, flush=True)
    while True:
        st = await be.poll(tid)
        print(f"t+{int(time.time()-t0)}s {st.state} {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(8)
    print("state:", st.state, "err:", st.error, "t:", int(time.time() - t0), "s", flush=True)
    if st.result_path:
        print("URL:", st.result_path, flush=True)
        urllib.request.urlretrieve(st.result_path, out)
        print("saved:", out, out.stat().st_size, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))