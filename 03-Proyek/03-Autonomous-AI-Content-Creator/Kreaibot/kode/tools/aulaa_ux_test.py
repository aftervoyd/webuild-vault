#!/usr/bin/env python3
"""Uji UX penuh: QR terkirim ke chat → bayar di simulator → ukur latensi auto-kredit
TANPA menekan tombol apa pun. Sekaligus membuktikan pesan QR berubah sendiri jadi LUNAS.
"""
from __future__ import annotations

import asyncio
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db as dbmod                                             # noqa: E402
from aiogram import Bot                                        # noqa: E402
from aiogram.client.default import DefaultBotProperties        # noqa: E402
from aiogram.enums import ParseMode                            # noqa: E402
from aiogram.types import (FSInputFile, InlineKeyboardButton,  # noqa: E402
                           InlineKeyboardMarkup)
from aulaa import Aulaa, make_client                            # noqa: E402
from config import settings                                     # noqa: E402

SIM = "https://api.aulaa.co/payment-simulation"
UID = 8886993492
UA = {"User-Agent": "Mozilla/5.0 Chrome/126", "Referer": SIM, "Origin": "https://api.aulaa.co"}


def http(url: str, data: dict | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url, data=urllib.parse.urlencode(data).encode() if data else None,
        method="POST" if data else "GET",
        headers={**UA, **({"Content-Type": "application/x-www-form-urlencoded"} if data else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "ignore")


async def main() -> int:
    db = dbmod.Database(settings.db_path)
    gw = make_client(settings)
    if gw is None:
        print("❌ AULAA_API_KEY kosong")
        return 1
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    order_id = f"UX-{UID}-{int(time.time())}"
    db.pay_create(order_id, UID, 10_000, 10.0)
    p = await gw.create(order_id, 10_000, method="qris", redirect_url=settings.aulaa_redirect)
    if not p.is_test:
        await gw.cancel(p.id)
        print("🚨 is_test=false → LIVE! transaksi dibatalkan.")
        return 2
    db.pay_set(order_id, payment_id=p.id, invoice=p.number, is_test=1)

    qp = Aulaa.qr_png(p.number, Path(settings.work_dir) / f"qr-{order_id}.png")
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Sudah Bayar — Cek Sekarang", callback_data=f"t:cek:{order_id}")],
        [InlineKeyboardButton(text="📄 Buka Halaman Bayar", url=gw.pay_url(p.id))]])
    m = await bot.send_photo(UID, FSInputFile(qp),
                             caption=(f"💳 <b>Rp10.000</b> → <b>10 Token</b>\n\n"
                                      f"uji auto-kredit: bayar di simulator, JANGAN tekan tombol apa pun\n"
                                      f"<code>{p.number}</code>"), reply_markup=kb)
    db.pay_set(order_id, msg_id=m.message_id, chat_id=m.chat.id)
    print(f"1️⃣  QR terkirim ke chat (msg_id={m.message_id}) · order={order_id}")

    st, _ = http(SIM, {"code": p.number, "action": "paid"})
    t0 = time.time()
    print(f"2️⃣  pembayaran disimulasikan (HTTP {st}) pada t=0 · poller TIDAK disentuh")

    lat = None
    while time.time() - t0 < 45:
        await asyncio.sleep(1)
        r = db.pay_get(order_id)
        if r and r["status"] == "paid":
            lat = time.time() - t0
            break
    r = db.pay_get(order_id)
    print(f"3️⃣  status di DB   : {r['status']}" + (f"  ← auto-kredit dalam {lat:.1f}s (tanpa tombol!)" if lat else "  ⚠️ TIMEOUT"))
    print(f"4️⃣  saldo owner    : {db.balance(UID):g} token")
    await bot.session.close()
    return 0 if lat else 3


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))