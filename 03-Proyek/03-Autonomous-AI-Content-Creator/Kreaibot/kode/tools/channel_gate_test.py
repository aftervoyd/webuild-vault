#!/usr/bin/env python3
"""Tes gate channel komunitas (Kreativ Community) lewat Bot API.

Memverifikasi guru logika `_channel_ok` di bot.py:
  - owner        → creator       → LOLOS
  - bot sendiri   → administrator → LOLOS
  - non-member    → error "member not found" → DITOLAK (gate aktif)
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Bot                        # noqa: E402
from config import settings                    # noqa: E402

GATE_OK = ("creator", "administrator", "member", "restricted")   # sama seperti _channel_ok()
NON_MEMBER = 7777777777


async def main() -> int:
    if not settings.channel:
        print("❌ KREAIBOT_CHANNEL belum diisi — gate nonaktif")
        return 1
    bot = Bot(settings.bot_token)
    me = await bot.get_me()
    ch = await bot.get_chat(f"@{settings.channel}")
    print(f"📢 channel: {ch.title} · @{ch.username} · id={ch.id}")
    member_count = await bot.get_chat_member_count(ch.id)
    print(f"👥 member : {member_count}\n")
    ok_all = True
    for label, uid, expect in (("owner", settings.admin_ids[0], True),
                               ("bot sendiri", me.id, True),
                               ("non-member", NON_MEMBER, False)):
        try:
            m = await bot.get_chat_member(ch.id, int(uid))
            st = m.status if isinstance(m.status, str) else m.status.value
            gate = st in GATE_OK
        except Exception as e:                     # noqa: BLE001
            st, gate = f"error ({str(e)[:38]})", False
        mark = "✅" if gate == expect else "❌"
        ok_all &= gate == expect
        print(f"  {mark} {label:<12} status={st:<28} gate={'LOLOS' if gate else 'DITOLAK'}")
    print(f"\n  hasil: {'✅ gate channel benar' if ok_all else '❌ ada yang tidak sesuai'}")
    await bot.session.close()
    return 0 if ok_all else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))