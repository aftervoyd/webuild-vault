#!/usr/bin/env python3
"""Verifikasi jalur PRODUKSI untuk fitur EDITOR (AI Image Editor).

Pakai backend yang sama dengan bot (backends/runninghub.py) → membuktikan
konfigurasi .env (RUNNINGHUB_APP_EDITOR + RUNNINGHUB_APP_NODES_EDITOR) benar.

Hasil editor = GAMBAR, bukan video.

Pakai: .venv/bin/python tools/backend_editor_test.py [foto] ["prompt"]
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

DEFAULT_PROMPT = "make it cyberpunk style, neon lighting, highly detailed, 8k"


async def main() -> int:
    from backends import GenRequest                  # noqa: E402
    from backends.runninghub import RunningHubBackend  # noqa: E402

    photo = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/job_6/ref1.bin"
    prompt = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_PROMPT
    out = ROOT / "work/tests/backend_editor.png"
    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    req = GenRequest(job_id=998, feature_key="editor", workflow="", photos=[photo],
                     prompt=prompt, ratio="9:16", duration=0, out_path=out)
    t0 = time.time()
    print(f"▶️ submit EDITOR · app={os.getenv('RUNNINGHUB_APP_EDITOR')} · {time.strftime('%H:%M:%S')}", flush=True)
    print(f"   prompt: {prompt}", flush=True)
    task = await be.submit(req)
    print(f"   taskId: {task}", flush=True)
    st = None
    while True:
        st = await be.poll(task)
        el = int(time.time() - t0)
        print(f"   t+{el:4d}s {st.state} · {(st.message or st.error or '')[:110]}", flush=True)
        if st.state in ("done", "failed"):
            break
        await asyncio.sleep(10)
    if st.state == "done" and st.result_path:
        url = str(st.result_path)
        if url.startswith("http"):
            urllib.request.urlretrieve(url, out)
        print(f"   ⬇️ {out} ({out.stat().st_size} byte) dari {url[:110]}", flush=True)
    print(f"   SELESAI: {st.state} · {int(time.time() - t0)}s", flush=True)
    return 0 if st.state == "done" else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))