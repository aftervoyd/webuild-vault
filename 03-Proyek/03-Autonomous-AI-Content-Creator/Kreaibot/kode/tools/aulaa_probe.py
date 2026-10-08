#!/usr/bin/env python3
"""Probe API Aulaa (Kreea.ai) — metodenya saja, aman.

Cek: (1) API key valid? (2) metode apa yang aktif di project ini + batas nominalnya?
Tidak membuat transaksi apa pun.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aulaa import AulaaError, make_client          # noqa: E402
from config import settings                        # noqa: E402


async def main() -> int:
    gw = make_client(settings)
    if gw is None:
        print("❌ AULAA_API_KEY belum diisi di .env")
        return 1
    print(f"🔑 key: {settings.aulaa_api_key[:12]}…{settings.aulaa_api_key[-4:]}  (project {settings.aulaa_project_id})")
    print(f"🌐 base: {gw.base}\n")
    try:
        ms = await gw.methods()
    except AulaaError as e:
        print(f"❌ GAGAL — HTTP {e.status}: {e}\n   payload: {str(e.payload)[:300]}")
        if e.status == 401:
            print("   → API key salah/tidak aktif. Ambil ulang dari Dashboard → Projects → API Keys.")
        elif e.status == 403:
            print("   → Project belum Live / disuspend (cek switch Sandbox↔Live di Dashboard → Projects).")
        return 1

    print(f"✅ API key VALID — {len(ms)} metode aktif untuk project ini:\n")
    print(f"   {'kode':<16}{'nama':<26}{'tipe':<16}{'min':>10}{'max':>14}")
    print("   " + "-" * 84)
    for m in sorted(ms, key=lambda x: str(x.get("code"))):
        code, name, typ = str(m.get("code", "")), str(m.get("name", ""))[:24], str(m.get("type", ""))
        mn, mx = int(m.get("min_amount") or 0), int(m.get("max_amount") or 0)
        if m.get("is_available"):
            print(f"   {code:<16}{name:<26}{typ:<16}{mn:>10,}{mx:>14,}".replace(",", "."))
    kode = {str(m.get("code")) for m in ms if m.get("is_available")}
    print(f"\n   QRIS aktif? {'✅ YA' if 'qris' in kode else '❌ TIDAK — harus diaktifkan di Dashboard → detail project'}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))