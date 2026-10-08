#!/usr/bin/env python3
"""Uji E2E alur referral TANPA Telegram — panggil handler asli pakai objek Message palsu.

Menguji:
  1. user baru klik link referral  → bonus invitee masuk, bonus pengundang masuk
  2. klik link yang sama 2x        → TIDAK dobel (1 akun = 1 bonus)
  3. self-referral                 → ditolak
  4. gate "wajib join channel"     → aktif saat KREAIBOT_CHANNEL diisi

DB terisolasi (tidak menyentuh kreaibot.sqlite3 produksi).
Jalankan: .venv/bin/python tools/ref_e2e.py
"""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import bot as B                                            # noqa: E402
from aiogram.filters import CommandObject                  # noqa: E402
from aiogram.fsm.context import FSMContext                 # noqa: E402
from aiogram.fsm.storage.base import StorageKey            # noqa: E402
from aiogram.fsm.storage.memory import MemoryStorage       # noqa: E402
from db import Database                                    # noqa: E402

TMP = Path("/tmp/reftest.sqlite3")
ok_all: list[bool] = []


def ok(label: str, cond: bool, extra: str = "") -> None:
    ok_all.append(bool(cond))
    print(f"{'✅' if cond else '❌'} {label}" + (f" — {extra}" if extra else ""))


class U:
    def __init__(self, uid: int, username: str = "", name: str = ""):
        self.id, self.username, self.full_name = uid, username, name


class C:
    def __init__(self, uid: int):
        self.id = uid


class M:                     # Message palsu: cukup untuk handler start
    def __init__(self, uid: int, username: str = "", name: str = "Tester"):
        self.from_user, self.chat, self.sent = U(uid, username, name), C(uid), []

    async def answer(self, text, **kw):
        self.sent.append(text)
        return self


def ctx(uid: int) -> FSMContext:
    return FSMContext(storage=MemoryStorage(),
                      key=StorageKey(bot_id=1, chat_id=uid, user_id=uid))


async def start_with_ref(uid: int, ref_uid: int, username: str = "") -> M:
    m = M(uid, username)
    cmd = CommandObject(prefix="/", command="start", args=f"ref_{ref_uid}")
    await B.cmd_start_ref(m, cmd, ctx(uid))
    return m


async def main() -> int:
    if TMP.exists():
        TMP.unlink()
    B.db = Database(TMP)                                   # ← isolasi dari DB produksi
    B.settings.channel = ""                                # gate channel OFF dulu
    B.db.ensure_user(900, "inviter", "Inviter", signup_bonus=1.0)

    # 1) user BARU klik link referral  (saldo = 2,5 bonus referral + 1,0 bonus daftar)
    m = await start_with_ref(987654321, 900, "temanbaru")
    ok("user baru dapat bonus invitee 2,5 token (+1 bonus daftar)",
       B.db.balance(987654321) == 3.5, f"saldo={B.db.balance(987654321)}")
    ok("pengundang dapat bonus 1,5 token",
       B.db.balance(900) == 2.5, f"saldo={B.db.balance(900)}")
    ok("balasan ke invitee menyebut bonus", any("2.5" in s or "bonus" in s.lower() for s in m.sent),
       m.sent[0][:48].replace("\n", " ") if m.sent else "(kosong)")

    # 2) klik ulang link yang sama → tidak dobel
    await B.cmd_start_ref(M(987654321, "temanbaru"),
                          CommandObject(prefix="/", command="start", args="ref_900"), ctx(987654321))
    ok("klik link 2x TIDAK menambah bonus", B.db.balance(987654321) == 3.5 and B.db.balance(900) == 2.5,
       f"invitee={B.db.balance(987654321)} inviter={B.db.balance(900)}")

    # 3) self-referral
    a = B.db.ref_register(555, 555)
    ok("self-referral ditolak", not a)

    # 4) invitee kedua dari pengundang sama (cap belum kena)
    await start_with_ref(987654322, 900, "teman2")
    ok("invitee kedua dibayar (pengundang 2,5→4,0)",
       B.db.balance(900) == 4.0 and B.db.balance(987654322) == 3.5,
       f"inviter={B.db.balance(900)} invitee2={B.db.balance(987654322)}")

    # 5) gate channel AKTIF (bot belum admin → dianggap belum join, tidak crash)
    B.settings.channel = "kreativcommunity_test"
    m3 = await start_with_ref(987654323, 900, "teman3")
    ok("gate channel aktif → bonus referral DITAHAN (cuma bonus daftar)",
       B.db.balance(987654323) == 1.0 and any("Join" in s for s in m3.sent),
       f"saldo={B.db.balance(987654323)}")
    r = B.db.ref_get(987654323)
    ok("status tetap 'pending' (belum dibayar)", r is not None and r["status"] == "pending")

    # 6) rekap + statistik
    st = B.db.ref_summary(900)
    ok("rekap: 3 undangan, 2 cair, 3 token", st["total"] == 3 and st["paid"] == 2 and st["earned"] == 3.0, str(st))
    top = B.db.ref_top(5)
    ok("ref_top mengembalikan pengundang teratas", len(top) >= 1 and int(top[0]["inviter_id"]) == 900)

    print(f"\nHASIL: {sum(ok_all)}/{len(ok_all)} tes referral E2E lulus")
    TMP.unlink(missing_ok=True)
    return 0 if all(ok_all) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))