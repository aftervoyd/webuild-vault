#!/usr/bin/env python3
"""Pasang gate channel referral Kreaibot (Kreativ Community).

Pakai:
    .venv/bin/python tools/channel_setup.py @username          # cek saja (aman)
    .venv/bin/python tools/channel_setup.py @username --set    # tulis .env + restart
    .venv/bin/python tools/channel_setup.py @username --post   # kirim pesan sambutan ke channel

Yang diperiksa: channel ada? bot sudah ADMIN? jumlah member? gate-nya jalan?
"""
from __future__ import annotations

import asyncio
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from aiogram import Bot                                          # noqa: E402
from aiogram.client.default import DefaultBotProperties          # noqa: E402
from aiogram.enums import ParseMode                              # noqa: E402
from aiogram.exceptions import TelegramBadRequest                # noqa: E402
from config import settings                                      # noqa: E402

WELCOME = """🎬 <b>Selamat datang di Kreativ Community!</b>

Komunitas resmi <b>Kreea.ai</b> — studio konten AI di Telegram.

<b>Yang bisa kamu bikin di @kreeaibot:</b>
🎬 Video UGC / iklan produk (15 detik)
🌌 Video All-in-One (foto produk → video iklan lengkap)
🖼️ Image to Video (1 foto → video bergerak)

<b>Cara mulai:</b>
1️⃣ Buka @kreeaibot → tekan /start
2️⃣ Pilih fitur → kirim foto produk + brief
3️⃣ Tunggu beberapa menit → video siap 🚀

<b>Aturan grup:</b>
• Saling bantu & jangan spam
• Dilarang konten judi/ilegal
• Promo produk sendiri boleh, jangan tiap menit 😄

<b>Bonus komunitas:</b> ngajak teman pakai link referral kamu → dapat <b>1,5 token</b> per teman yang gabung, dan temanmu dapat <b>2,5 token</b>! (menu 🎁 Referral di bot)

Selamat berkarya! 💚"""


def patch_env(username: str) -> str:
    env = ROOT / ".env"
    txt = env.read_text()
    new, n = re.subn(r"(?m)^KREAIBOT_CHANNEL=.*$", f"KREAIBOT_CHANNEL={username}", txt)
    if n == 0:
        new = txt.rstrip("\n") + f"\nKREAIBOT_CHANNEL={username}\n"
    env.write_text(new)
    env.chmod(0o600)
    return f"{n} baris diganti" if n else "baris ditambah"


async def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 1
    uname = args[0].lstrip("@").strip()
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    me = await bot.get_me()
    ok = True
    try:
        chat = await bot.get_chat(f"@{uname}")
        print(f"1️⃣  channel ketemu : <{chat.title}> · @{chat.username} · id={chat.id} · tipe={chat.type}")
        if chat.type != "channel":
            print("   ⚠️ ini bukan CHANNEL (mungkin grup) — gate referral pakai getChatMember, tetap bisa tapi sebaiknya channel")
        try:
            cnt = await bot.get_chat_member_count(chat.id)
            print(f"2️⃣  jumlah member : {cnt}")
        except TelegramBadRequest as e:
            print(f"2️⃣  jumlah member : tidak terbaca ({str(e)[:80]})")
        m = await bot.get_chat_member(chat.id, me.id)
        st = m.status if isinstance(m.status, str) else m.status.value
        print(f"3️⃣  status bot    : {st} {'✅' if st in ('administrator', 'creator') else '❌ (harus ADMIN!)'}")
        if st not in ("administrator", "creator"):
            ok = False
            print("   → Tambahkan @%s sebagai ADMIN di channel (Channel → Kelola → Administrator → Tambah)." % me.username)
        # uji gate: id acak yang pasti belum gabung
        try:
            rm = await bot.get_chat_member(chat.id, 7777777777)
            print(f"4️⃣  uji non-member: status={rm.status} (harus 'left'/'kicked')")
        except TelegramBadRequest as e:
            print(f"4️⃣  uji non-member: ditolak ({str(e)[:70]}) — anggap belum gabung ✓")
        # uji gate untuk user asli (owner)
        for uid in settings.admin_ids:
            try:
                om = await bot.get_chat_member(chat.id, int(uid))
                print(f"   owner {uid}: status={om.status}")
            except TelegramBadRequest as e:
                print(f"   owner {uid}: error {str(e)[:60]}")
    except TelegramBadRequest as e:
        print(f"❌ channel @{uname} tidak ketemu / bot belum di-add: {str(e)[:120]}")
        ok = False
    if "--set" in flags and ok:
        print(f"\n⚙️  tulis .env : KREAIBOT_CHANNEL={uname} → {patch_env(uname)}")
        print("   (setelah ini: systemctl restart kreaibot)")
    if "--post" in flags and ok:
        await bot.send_message(chat.id, WELCOME)
        print("\n📣 pesan sambutan terkirim ke channel ✓")
    await bot.session.close()
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))