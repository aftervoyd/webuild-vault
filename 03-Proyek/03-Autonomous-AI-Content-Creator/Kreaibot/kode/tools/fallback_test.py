#!/usr/bin/env python3
"""Uji FALLBACK otomatis: paksa app utama RUSAK → backend harus pindah sendiri ke app cadangan.

Bukti nyata (9 Okt): app "低价渠道版" gagal dengan "Your API balance is insufficient"
(saldo $ kosong, koin masih banyak) → user melihat "gagal terus". Setelah fallback:
user tidak perlu tahu, render tetap jalan.
"""
from __future__ import annotations

import asyncio
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv                     # noqa: E402

load_dotenv(ROOT / ".env")

# app RUSAK (butuh saldo $) sebagai "utama", CADANGAN tetap dari .env (Kontext/Qwen)
os.environ["RUNNINGHUB_APP_EDITOR"] = "2061699451919618049"
os.environ["RUNNINGHUB_APP_NODES_EDITOR"] = (
    '[{"nodeId":"2","fieldName":"image","value":"@photo1"},'
    '{"nodeId":"1","fieldName":"prompt","value":"@prompt"}]')


async def main() -> int:
    from backends import GenRequest
    from backends.runninghub import RunningHubBackend

    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    tid = await be.submit(GenRequest(job_id=995, feature_key="editor", workflow="",
                                     photos=[ROOT / "work/inventory_fix/1_Arunika_panel.jpg"],
                                     prompt="she wears a white towel mirror selfie, keep the same face",
                                     ratio="9:16", duration=0, out_path=ROOT / "work/tests/fallback_uji.png"))
    print("task awal (pakai app rusak):", tid)
    t0 = time.time()
    while time.time() - t0 < 420:
        st = await be.poll(tid)
        el = int(time.time() - t0)
        if st.state == "done":
            print(f"✅ FALLBACK BERHASIL · {el}s → {st.result_path}")
            return 0
        if st.state == "failed":
            print("❌ fallback GAGAL:", str(st.error)[:160])
            return 1
        if el % 15 < 6:
            print(f"  t+{el}s · {st.state} · {st.message}")
        await asyncio.sleep(5)
    print("timeout")
    return 1


if __name__ == "__main__":
    os.chdir(ROOT)
    raise SystemExit(asyncio.run(main()))