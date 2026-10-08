#!/usr/bin/env python3
"""Verifikasi jalur PRODUKSI (backend yang dipakai bot): i2v frame-akhir kosong.

Beda dari tools/rh_test_bind.py (menyusun nodeInfoList sendiri), skrip ini memakai
backends/runninghub.py yang sama dengan bot → membuktikan konfigurasi .env benar.

Pakai: .venv/bin/python tools/backend_i2v_test.py [foto]
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

    photo = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/job_3/ref1.bin"
    prompt = (ROOT / "work/tests/prompt_h3.txt").read_text(encoding="utf-8").strip()
    out = ROOT / "work/tests/backend_i2v.mp4"
    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""))
    req = GenRequest(job_id=999, feature_key="i2v", workflow="", photos=[photo],
                     prompt=prompt, ratio="9:16", duration=5, out_path=out)
    t0 = time.time()
    print(f"▶️ submit lewat backend PRODUKSI · {time.strftime('%H:%M:%S')}", flush=True)
    task = await be.submit(req)
    print(f"   taskId: {task}", flush=True)
    st = None
    while True:
        st = await be.poll(task)
        el = int(time.time() - t0)
        print(f"   t+{el:4d}s {st.state} · {(st.message or st.error)[:110]}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(20)
    if st.state == "done" and st.result_path:
        urllib.request.urlretrieve(str(st.result_path), out)
        print(f"   ⬇️ {out} ({out.stat().st_size} byte)", flush=True)
    print(f"   SELESAI: {st.state} · {int(time.time() - t0)}s", flush=True)
    return 0 if st.state == "done" else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))