#!/usr/bin/env python3
"""E2E sandbox Aulaa — bikin 1 transaksi QRIS pakai jalur kode yang sama seperti bot.

PENGAMAN: kalau respons ternyata `is_test: false` (= transaksi LIVE beneran),
transaksi langsung DIBATALKAN dan skrip berhenti dengan error. Sandbox only!
"""
from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db as dbmod                                 # noqa: E402
from aulaa import Aulaa, make_client               # noqa: E402
from config import settings                        # noqa: E402

UID = 8886993492          # telegram id owner (biar bot DM buktinya ke dia)
RP = 10_000


async def main() -> int:
    gw = make_client(settings)
    if gw is None:
        print("❌ AULAA_API_KEY kosong")
        return 1
    db = dbmod.Database(settings.db_path)
    order_id = f"SBX-{UID}-{int(time.time())}"
    tok = RP // max(1, settings.harga_per_10k // max(1, settings.tokens_per_10k))
    db.pay_create(order_id, UID, RP, tok)
    print(f"1️⃣  order dibuat lokal : {order_id}  (Rp{RP:,} → {tok:g} token)".replace(",", "."))

    p = await gw.create(order_id, RP, method=settings.aulaa_method or "qris",
                        redirect_url=settings.aulaa_redirect or None)
    print(f"2️⃣  gateway balas     : id={p.id}\n    status={p.status} · metode={p.method} · is_test={p.is_test}")
    print(f"    kode bayar (payment_number) = {p.number!r}")
    print(f"    expired_at={p.expired_at}")

    if not p.is_test:
        print("\n🚨 BAHAYA: ini transaksi LIVE (is_test=false), bukan sandbox!")
        print("   → gue batalkan sekarang. Balikkan switch project ke SANDBOX di dashboard dulu.")
        try:
            await gw.cancel(p.id)
            print("   ✅ transaksi LIVE sudah dibatalkan (cancel).")
        except Exception as e:                      # noqa: BLE001
            print(f"   ⚠️ gagal batal otomatis: {e} — BATALKAN MANUAL di dashboard!")
        db.pay_set(order_id, status="error", note="LIVE (bukan sandbox) → dibatalkan")
        return 2

    db.pay_set(order_id, payment_id=p.id, invoice=p.number, is_test=1)
    qp = Aulaa.qr_png(p.number, Path(settings.work_dir) / f"qr-{order_id}.png")
    print(f"3️⃣  QR dirender       : {qp} ({qp.stat().st_size} bytes)")
    print(f"\n👉 Halaman simulasi   : https://api.aulaa.co/payment-simulation")
    print(f"👉 Kode untuk dibayar  : {p.number}")
    print(f"👉 Poller bot (12s) akan otomatis kredit {tok:g} token begitu lunas.\n")
    print(f"ORDER_ID={order_id}\nPAYMENT_ID={p.id}\nKODE={p.number}\nQR={qp}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))