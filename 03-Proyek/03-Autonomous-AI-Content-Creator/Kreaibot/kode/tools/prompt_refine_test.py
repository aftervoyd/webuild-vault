#!/usr/bin/env python3
"""Uji perapian prompt video (i2v/all-in-one) — pakai LLM saja, 0 koin render.

Menampilkan prompt ASLI user → hasil rapian, supaya kelihatan apakah aman:
tidak menambah objek baru, tidak menyuruh seluruh frame bergerak, identitas dijaga.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv                       # noqa: E402

load_dotenv(ROOT / ".env")

import promptsmith                                   # noqa: E402
from config import settings                          # noqa: E402

SAMPLE = [
    "wanita tersenyum di pantai",
    "viral tiktok, orangnya noleh pelan, rambut kena angin, ombak gerak, kamera push in halus",
    "bikin dia ngomong sambil ketawa, background kafe, sinematik",
    "produk skincare di tangan, diangkat ke kamera, natural light",
]

# frasa yang DILARANG muncul (penyebab wajah/badan ikut warp — pelajaran 8 Okt)
BAD = ("whole frame", "everything in frame", "entire frame", "constant motion",
       "everything moves", "all elements move")


async def main() -> int:
    print("═" * 72)
    print("UJI PERAPIAN PROMPT VIDEO (LLM saja · 0 koin)")
    print("═" * 72)
    print(f"  refine aktif: {settings.refine_video} · model: {settings.promptsmith_model}")
    ok = True
    for i, raw in enumerate(SAMPLE, 1):
        out = await promptsmith.refine_video_prompt(
            raw, ratio="9:16", duration=5,
            base_url=settings.promptsmith_base, api_key=settings.promptsmith_key,
            model=settings.promptsmith_model)
        same = out.strip() == raw.strip()
        kata = len(out.split())
        langgar = [b for b in BAD if b in out.lower()]
        print(f"\n  #{i} ASLI   : {raw}")
        print(f"      RAPIAN : {out}")
        print(f"      · {kata} kata · " + ("⏭ pakai asli (fallback)" if same else "✅ dirapikan")
              + (f" · ⚠️ PELANGGARAN: {', '.join(langgar)}" if langgar else ""))
        if langgar or kata > 130:
            ok = False
    empty = await promptsmith.refine_video_prompt("", base_url="x", api_key="x", model="x")
    print(f"\n  fallback input kosong → {'✅ aman (tetap kosong, tak error)' if empty == '' else '❌ ' + repr(empty)}")
    ok = ok and empty == ""
    print("\n" + "═" * 72)
    print("HASIL: " + ("✅ semua rapian aman dipakai" if ok else "⚠️ ada yang perlu dicek dulu"))
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))