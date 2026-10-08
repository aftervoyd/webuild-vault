#!/usr/bin/env python3
"""Uji bayar NYATA (mode LIVE) — bikin order Rp10.000 asli, kirim QR ke chat owner,
lalu ukur latensi auto-kredit oleh poller bot (tanpa menekan tombol apa pun).

Berbeda dengan aulaa_ux_test.py (yang MEMBATALKAN kalau is_test=false),
tool ini memang untuk LIVE: QR-nya bisa dibayar beneran pakai m-banking/e-wallet.

Pakai:  .venv/bin/python tools/aulaa_live_test.py [nominal]
        .venv/bin/python tools/aulaa_live_test.py status     # cek order LIVE terakhir
"""
from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import db as dbmod                                            # noqa: E402
from aiogram import Bot                                      # noqa: E402
from aiogram.client.default import DefaultBotProperties      # noqa: E402
from aiogram.enums import ParseMode                          # noqa: E402
from aiogram.types import (FSInputFile, InlineKeyboardButton,  # noqa: E402
                           InlineKeyboardMarkup)
from aulaa import Aulaa, make_client                         # noqa: E402
from config import settings                                  # noqa: E402

UID = 8886993492
POLL_MAX = 300.0          # detik maksimal memantau auto-kredit


async def cek_status(db) -> int:
    rows = list(db.conn.execute(
        "SELECT order_id, amount, tokens, status, is_test, paid_at FROM payments "
        "WHERE is_test=0 ORDER BY created_at DESC LIMIT 5"))
    if not rows:
        print("belum ada order LIVE (is_test=0) di database")
        return 1
    for r in rows:
        print(f"  {r['order_id']:<28} Rp{r['amount']:<7,} {r['tokens']:>4g} token  "
              f"{r['status']:<8} paid_at={r['paid_at'] or '-'}")
    return 0


async def main() -> int:
    db = dbmod.Database(settings.db_path)
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        return await cek_status(db)

    rp = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000
    tok = rp / 1000.0

    gw = make_client(settings)
    if gw is None:
        print("❌ AULAA_API_KEY kosong di .env")
        return 1
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    order_id = f"LIVE-{UID}-{int(time.time())}"
    db.pay_create(order_id, UID, rp, tok)
    p = await gw.create(order_id, rp, method=settings.aulaa_method,
                        redirect_url=settings.aulaa_redirect)

    if p.is_test:
        await gw.cancel(p.id)
        db.pay_set(order_id, status="error", note="live test tapi is_test=true")
        print("🚨 is_test = TRUE → project MASIH SANDBOX di dashboard Aulaa. Order dibatalkan.")
        print("   Flip switch Live dulu, baru jalanin tool ini lagi.")
        await bot.session.close()
        return 2

    db.pay_set(order_id, payment_id=p.id, invoice=p.number, is_test=0)
    print(f"🟢 LIVE order: {order_id} · payment_id={p.id}")
    print(f"   nominal Rp{rp:,} → {tok:g} token · status={p.status} · expired={p.expired_at}")

    exp = f"\n⏳ Berlaku sampai: {p.expired_at}" if p.expired_at else ""
    cap = ((f"💳 <b>Rp{rp:,}</b> → <b>{tok:g} Token</b>\n\n"
            f"Scan QR ini pakai <b>m-banking / e-wallet apa saja</b> (QRIS).\n"
            f"Token masuk <b>otomatis</b> begitu pembayaran berhasil — gak perlu kirim bukti.{exp}\n\n"
            f"ID kamu: <code>{UID}</code>").replace(",", "."))
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Sudah Bayar — Cek Sekarang", callback_data=f"t:cek:{order_id}")],
        [InlineKeyboardButton(text="📄 Buka Halaman Bayar", url=gw.pay_url(p.id))],
        [InlineKeyboardButton(text="⬅️ Menu Utama", callback_data="m:home")]])

    qp = Aulaa.qr_png(p.number, Path(settings.work_dir) / f"qr-{order_id}.png")
    m = await bot.send_photo(UID, FSInputFile(qp), caption=cap, reply_markup=kb)
    db.pay_set(order_id, msg_id=m.message_id, chat_id=m.chat.id)
    print(f"1️⃣  QR terkirim ke chat (msg_id={m.message_id}) — SILAKAN SCAN & BAYAR")

    t0 = time.time()
    lat = None
    print(f"2️⃣  memantau auto-kredit (maks {POLL_MAX:.0f}s, JANGAN tekan tombol)…")
    while time.time() - t0 < POLL_MAX:
        await asyncio.sleep(2)
        r = db.pay_get(order_id)
        st = (r["status"] if r else "?")
        el = time.time() - t0
        print(f"     t+{el:5.1f}s  status={st}")
        if st == "paid":
            lat = el
            break
        if st in ("expired", "error", "canceled"):
            break
    r = db.pay_get(order_id)
    if lat:
        print(f"\n✅ AUTO-KREDIT dalam {lat:.1f}s — saldo owner: {db.balance(UID):g} token")
        print("   (pesan QR di chat seharusnya sudah berubah jadi '✅ LUNAS')")
    else:
        print(f"\n⚠️  status akhir: {r['status'] if r else '?'} — belum lunas dalam {POLL_MAX:.0f}s.")
        print("   Kalau kamu bayar nanti, poller bot tetap mengkredit otomatis (cek: tools/aulaa_live_test.py status)")
    await bot.session.close()
    return 0 if lat else 3


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))