#!/usr/bin/env python3
"""Verifikasi jalur PRODUKSI untuk Face Swap (gambar): foto wajah + foto model → gambar.

Pakai: .venv/bin/python tools/backend_faceswap_test.py [foto_wajah] [foto_model]
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

from dotenv import load_dotenv                       # noqa: E402

load_dotenv(ROOT / ".env")


async def main() -> int:
    from backends import GenRequest                  # noqa: E402
    from backends.runninghub import RunningHubBackend  # noqa: E402

    face = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/tests/ref1.jpg"
    model = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "work/tests/nobalon-sheet.jpg"
    out = ROOT / "work/tests/backend_faceswap.png"

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=999, feature_key="faceswap", workflow="",
                     photos=[face, model], prompt="", ratio="9:16", duration=5, out_path=out)
    t0 = time.time()
    print(f"▶️ submit Face Swap · wajah={face.name} · model={model.name} · {time.strftime('%H:%M:%S')}", flush=True)
    task = await be.submit(req)
    print("task:", task, flush=True)
    while True:
        st = await be.poll(task)
        print(f"   t+{int(time.time()-t0)}s {st.state} · {st.message}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(5)
    if st.state != "done":
        print("GAGAL:", st.error, flush=True)
        return 1
    url = st.result_path or ""
    print("url:", url, flush=True)
    if url:
        urllib.request.urlretrieve(url, out)
        print(f"⬇️ {out} ({out.stat().st_size} byte)", flush=True)
    print(f"SELESAI: {st.state} · {int(time.time()-t0)}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))