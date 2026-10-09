#!/usr/bin/env python3
"""Diagnostik: apakah PROMPT benar-benar sampai ke model?

Pakai satu prompt yang mustahil terlewat (wig badut merah + topi pelangi + bendera kuning +
latar gunung salju). Kalau hasil render TIDAK memuat itu → binding node prompt kita salah.
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

PROMPT = ("The person from the photo is now wearing a bright RED clown wig and a tall RAINBOW TOP HAT, "
          "holding a bright YELLOW flag. The background becomes a snowy mountain at noon. "
          "Keep the face and identity identical.")


async def main() -> int:
    from backends import GenRequest
    from backends.runninghub import RunningHubBackend

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    out = ROOT / "work/tests/prompt_probe.mp4"
    req = GenRequest(job_id=555, feature_key="i2v", workflow="",
                     photos=[ROOT / "work/tests/ref1.jpg"], prompt=PROMPT,
                     ratio="9:16", duration=5, out_path=out)
    t0 = time.time()
    tid = await be.submit(req)
    print("task:", tid, flush=True)
    while True:
        st = await be.poll(tid)
        print(f"t+{int(time.time()-t0)}s {st.state} {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(6)
    print("URL:", st.result_path, flush=True)
    if st.result_path:
        urllib.request.urlretrieve(st.result_path, out)
        print("saved", out, out.stat().st_size, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))