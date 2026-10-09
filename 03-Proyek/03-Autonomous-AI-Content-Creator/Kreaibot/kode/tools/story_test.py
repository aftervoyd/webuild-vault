#!/usr/bin/env python3
"""Uji jalur PRODUKSI mode CERITA: N klip pendek + frame chaining → 1 video jahitan.

Pakai: .venv/bin/python tools/story_test.py [jumlah_scene] [foto]
"""
from __future__ import annotations

import asyncio
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv                       # noqa: E402

load_dotenv(ROOT / ".env")

STORY = ("wanita itu berlari membelakangi kamera lalu kamera mengejar, wanita itu sesekali menoleh "
         "dan hampir terjatuh tapi lanjut berlari dan tertawa")


async def main() -> int:
    import promptsmith
    import storyboard
    from backends.runninghub import RunningHubBackend

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    photo = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "work/tests/ref1.jpg"
    work = ROOT / "work/tests/story_run"
    work.mkdir(parents=True, exist_ok=True)

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    shots = await promptsmith.split_story(STORY, shots=n, seconds_each=5,
                                          base_url=os.getenv("PROMPTSMITH_BASE_URL", ""),
                                          api_key=os.getenv("PROMPTSMITH_API_KEY", ""),
                                          model=os.getenv("PROMPTSMITH_MODEL", ""))
    for i, s in enumerate(shots, 1):
        print(f"scene {i}: {s}", flush=True)

    async def prog(i, total, msg):
        print(f"   ⏳ scene {i}/{total}: {msg} (t+{int(time.time()-t0)}s)", flush=True)

    t0 = time.time()
    out = await storyboard.render_story(be, photo=photo, shots=shots, ratio="9:16",
                                        work=work, dur_each=5, job_id=777,
                                        on_progress=prog)
    print(f"✅ hasil: {out} ({out.stat().st_size} byte) dalam {int(time.time()-t0)}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))