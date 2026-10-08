#!/usr/bin/env python3
"""Smoke-test RunningHub: upload 1 foto → create task → poll → unduh hasil.

Dipakai buat verifikasi cepat begitu API key + workflowId masuk ke .env.

Contoh:
  .venv/bin/python tools/rh_smoketest.py --feature ugc \
      --photo /root/projects/kreaibot/work/selftest/ref1.png \
      --photo /root/projects/kreaibot/work/selftest/ref2.png

Node binding dibaca dari .env (RUNNINGHUB_NODES_<FEATURE>) kalau ada;
kalau tidak, pakai --nodes '[{"nodeId":"12","fieldName":"image","value":"@photo1"}]'.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from backends import GenRequest  # noqa: E402
from backends.runninghub import RunningHubBackend  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature", default="ugc")
    ap.add_argument("--photo", action="append", default=[])
    ap.add_argument("--prompt", default="A 15-second vertical 9:16 UGC video ad: "
                                        "creator holds the product and reviews it naturally, "
                                        "consistent face, product label faithful.")
    ap.add_argument("--ratio", default="9:16")
    ap.add_argument("--nodes", default="")
    ap.add_argument("--timeout", type=int, default=1800)
    a = ap.parse_args()

    key = os.getenv("RUNNINGHUB_API_KEY", "")
    base = os.getenv("RUNNINGHUB_BASE", "https://www.runninghub.ai")
    wf = os.getenv(f"RUNNINGHUB_WF_{a.feature.upper()}", "")
    nodes_raw = a.nodes or os.getenv(f"RUNNINGHUB_NODES_{a.feature.upper()}", "[]")

    print("=== RunningHub smoke-test ===")
    print(f"base      : {base}")
    print(f"api key   : {'ada (' + key[:6] + '…' + key[-4:] + ')' if key else 'KOSONG'}")
    print(f"workflow  : {wf or 'KOSONG (RUNNINGHUB_WF_' + a.feature.upper() + ')'}")
    print(f"foto      : {a.photo or '(kosong)'}")
    if not key or not wf:
        print("\n❌ isi RUNNINGHUB_API_KEY & RUNNINGHUB_WF_<FEATURE> di .env dulu.")
        return 1

    be = RunningHubBackend(api_key=key, base=base, work_dir=str(ROOT / "work"))
    photos = [Path(p) for p in a.photo]

    # 0) upload (verifikasi endpoint + fileType)
    names: list[str] = []
    for p in photos:
        t0 = time.time()
        try:
            n = await be.upload(p)
            print(f"⬆️  upload {p.name} → {n}  ({time.time()-t0:.1f}s)")
            names.append(n)
        except Exception as e:
            print(f"❌ upload gagal: {e}")
            return 2

    # 1) create task
    req = GenRequest(job_id=0, feature_key=a.feature, workflow="", photos=photos,
                     prompt=a.prompt, ratio=a.ratio, out_path=ROOT / "work" / "smoketest.mp4")
    # paksa binding dari argumen kalau ada
    if a.nodes:
        os.environ[f"RUNNINGHUB_NODES_{a.feature.upper()}"] = nodes_raw
    try:
        tid = await be.submit(req)
        print(f"🚀 task dibuat: {tid}")
    except Exception as e:
        print(f"❌ create task gagal: {e}")
        return 3

    # 2) poll
    t0 = time.time()
    last = ""
    while time.time() - t0 < a.timeout:
        st = await be.poll(tid)
        if st.message != last:
            print(f"   [{int(time.time()-t0):4d}s] {st.state:8s} {st.message or ''}")
            last = st.message or ""
        if st.state == "done":
            print(f"\n✅ SELESAI dalam {time.time()-t0:.0f}s")
            print(f"   hasil: {st.result_path}")
            if str(st.result_path).startswith("http"):
                try:
                    from bot import fetch_url
                    dest = await fetch_url(str(st.result_path), ROOT / "work" / "smoketest.mp4")
                    print(f"   terunduh → {dest} ({dest.stat().st_size} bytes)")
                except Exception as e:
                    print(f"   ⚠️ gagal unduh: {e}")
            return 0
        if st.state == "failed":
            print(f"\n❌ GAGAL: {st.error}")
            return 4
        await asyncio.sleep(5)
    print("\n⏰ timeout")
    return 5


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))