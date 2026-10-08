#!/usr/bin/env python3
"""Simulasikan pembayaran sandbox Aulaa untuk order pending terakhir, lalu buktikan
bahwa poller bot mengkredit token otomatis.

Dipakai untuk uji sandbox: GET /payment-simulation/check?code=… lalu POST /payment-simulation
dengan action=paid (persis seperti tombol "Bayar (Sukses)" di halaman simulator).
"""
from __future__ import annotations

import asyncio
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db as dbmod                                 # noqa: E402
from aulaa import make_client                      # noqa: E402
from config import settings                        # noqa: E402

SIM = "https://api.aulaa.co/payment-simulation"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126 Safari/537.36",
      "Referer": SIM, "Origin": "https://api.aulaa.co"}


def http(url: str, data: dict | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url, data=urllib.parse.urlencode(data).encode() if data else None,
        method="POST" if data else "GET",
        headers={**UA, **({"Content-Type": "application/x-www-form-urlencoded"} if data else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "ignore")


async def main() -> int:
    db = dbmod.Database(settings.db_path)
    pend = db.pay_pending(20)
    if not pend:
        print("ℹ️  tidak ada order pending di DB — bikin dulu: python tools/aulaa_e2e.py")
        return 1
    want = sys.argv[1] if len(sys.argv) > 1 else ""
    row = next((r for r in pend if str(r["order_id"]) == want), None) if want else None
    row = row or pend[-1]
    order_id, code = str(row["order_id"]), str(row["invoice"] or "")
    print(f"📄 order   : {order_id}\n🔑 kode    : {code[:40]}… ({len(code)} char)\n")

    print("1️⃣  GET /payment-simulation/check")
    st, body = http(f"{SIM}/check?{urllib.parse.urlencode({'code': code})}")
    print(f"   HTTP {st} → {body[:300]}\n")

    print("2️⃣  POST /payment-simulation  action=paid  (tombol 'Bayar (Sukses)')")
    st, body = http(SIM, {"code": code, "action": "paid"})
    print(f"   HTTP {st} → {body[:300]}\n")

    print("3️⃣  tunggu poller bot (12s interval, maks 40s)…")
    for i in range(20):
        time.sleep(2)
        r = db.pay_get(order_id)
        if r and r["status"] == "paid":
            print(f"   ✅ setelah ~{(i + 1) * 2}s → status={r['status']} paid_at={r['paid_at']}")
            break
    else:
        print("   ⚠️ belum ke-credit — cek journalctl -u kreaibot | grep -i poll")

    gw = make_client(settings)
    if gw:
        p = await gw.get(str(row["payment_id"]))
        print(f"\n4️⃣  status di gateway : {p.status}  (paid_at={p.raw.get('paid_at')})")
    r = db.pay_get(order_id)
    bal = db.balance(int(row["telegram_id"]))
    print(f"5️⃣  di DB kita        : status={r['status']} · token={r['tokens']:g} · saldo user={bal:g}")
    led = [dict(e) for e in db.ledger(int(row["telegram_id"]), 8) if str(e["ref"]) == order_id]
    print(f"    ledger           : {led if led else '❌ tidak ada'}")
    return 0 if r["status"] == "paid" else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))