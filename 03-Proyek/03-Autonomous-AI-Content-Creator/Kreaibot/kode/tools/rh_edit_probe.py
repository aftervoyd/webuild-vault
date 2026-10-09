#!/usr/bin/env python3
"""Probe app editan RunningHub apa pun: jalankan 1 gambar + prompt, laporkan ukuran/waktu/koin.

Dipakai untuk memilih mesin terbaik (identitas kuat, rasio bisa diatur) SEBELUM masuk katalog jual.

Pakai:
  ./.venv/bin/python tools/rh_edit_probe.py <appId> '<nodes json>' <foto> '<prompt>' [keluar.png]
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv                     # noqa: E402

load_dotenv(ROOT / ".env")


def saldo() -> int:
    key = os.getenv("RUNNINGHUB_API_KEY", "")
    req = urllib.request.Request("https://www.runninghub.cn/uc/openapi/accountStatus",
                                 data=json.dumps({"apikey": key}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    return int((json.load(urllib.request.urlopen(req, timeout=40)).get("data") or {}).get("remainCoins") or 0)


async def main() -> int:
    from backends import GenRequest
    from backends.runninghub import RunningHubBackend

    app_id, nodes, photo = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    prompt = sys.argv[4] if len(sys.argv) > 4 else ""
    out = Path(sys.argv[5]) if len(sys.argv) > 5 else ROOT / "work/tests/probe_edit.png"
    # foto tambahan (buat app 2-gambar: face swap dll) → @photo2, @photo3, ...
    # pakai: RH_PROBE_PHOTOS="/path/wajah.jpg,/path/lain.jpg"
    extra = [Path(p) for p in os.getenv("RH_PROBE_PHOTOS", "").split(",") if p.strip()]
    photos = [photo] + extra

    os.environ["RUNNINGHUB_APP_EDITOR"] = app_id
    os.environ["RUNNINGHUB_APP_NODES_EDITOR"] = nodes

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    t0, before = time.time(), saldo()
    req = GenRequest(job_id=997, feature_key="editor", workflow="", photos=photos,
                     prompt=prompt, ratio="9:16", duration=0, out_path=out)
    task = await be.submit(req)
    print("taskId:", task)
    while True:
        st = await be.poll(task)
        el = int(time.time() - t0)
        if st.state == "failed":
            print(f"❌ GAGAL ({el}s): {st.error}")
            return 1
        if st.state == "done":
            rp = str(st.result_path or "")
            if rp.startswith("http"):
                r = urllib.request.Request(rp, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(r, timeout=240) as resp, open(out, "wb") as f:
                    f.write(resp.read())
            try:
                from PIL import Image
                im = Image.open(out)
                print(f"✅ SELESAI {el}s | koin terpakai: {before - saldo()} | ukuran: {im.size} "
                      f"| rasio: {im.size[0] / im.size[1]:.3f}")
            except Exception:
                print(f"✅ SELESAI {el}s | koin: {before - saldo()} | file: {out}")
            return 0
        if el % 20 < 6:
            print(f"  t+{el}s running…")
        if el > 900:
            print("❌ timeout")
            return 1
        await asyncio.sleep(5)


if __name__ == "__main__":
    os.chdir(ROOT)
    raise SystemExit(asyncio.run(main()))