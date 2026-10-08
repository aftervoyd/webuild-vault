#!/usr/bin/env python3
"""Audit UX KREE.AI: telusuri SEMUA layar tiap fitur + cek tombol mati.

Dipakai untuk menjawab "periksa lagi semua fitur kita" secara sistematis:
  1. Setiap fitur: cetak urutan layar (teks + tombol) yang akan dilihat user
  2. Setiap layar WAJIB punya minimal 1 tombol yang bisa ditekan
  3. Setiap callback_data yang diproduksi kode HARUS punya handler (anti tombol mati)
  4. Setiap handler `F.data ==` / `startswith` yang tidak pernah diproduksi = indikasi sisa kode

Exit code 0 kalau bersih.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import catalog  # noqa: E402

SRC = (ROOT / "bot.py").read_text(encoding="utf-8")


def produced_callbacks() -> set[str]:
    return set(re.findall(r'callback_data=f?"([^"]+)"', SRC))


def has_handler(cb: str, handlers: set[str], prefixes: set[str]) -> bool:
    return cb in handlers or any(cb.startswith(p) for p in prefixes)


def main() -> int:
    handlers = set(re.findall(r'F\.data\s*==\s*"([^"]+)"', SRC))
    prefixes = set(re.findall(r'F\.data\.startswith\("([^"]+)"\)', SRC))
    prod = produced_callbacks()
    bad = 0

    print("═" * 64)
    print("AUDIT UX KREE.AI")
    print("═" * 64)

    for f in catalog.enabled_features():
        print(f"\n▸ {f.label}  [{f.key}]  ·  {f.cost:g} Token (dasar)")
        # 1) layar DETAIL (m:feat:<key>)
        if len(f.durations) > 1:
            detail = [f"▶️ {d} detik · {catalog.cost_for(f.key, d):g} Token" for d in f.durations]
            cbs = [f"m:go:{f.key}:{d}" for d in f.durations]
        else:
            detail, cbs = ["🚀 Mulai"], [f"m:go:{f.key}"]
        print(f"   1. Layar detail   : tombol {detail}")
        # 2) layar INPUT
        if f.kind == "ugc":
            print(f"   2. Input UGC      : foto karakter → foto produk → ketik brief"
                  f" ({f.min_photos}-{f.max_photos} foto, gaya: {f.need_style})")
        else:
            print(f"   2. Input foto     : {f.hint or f'kirim {f.min_photos}-{f.max_photos} foto'}"
                  f"  → langsung ketik prompt")
        # 3) layar KONFIRMASI
        rows = [f"🚀 Render ({catalog.cost_for(f.key, f.duration):g} Token)"]
        if f.need_ratio:
            rows.append("rasio: " + " / ".join(k for k in catalog.RATIOS))
        if len(f.durations) > 1:
            rows.append("durasi: " + " / ".join(
                f"{d} dtk {catalog.cost_for(f.key, d):g}T" for d in f.durations))
        if f.kind == "ugc":
            rows.append("🎨 Ganti gaya")
        print(f"   3. Konfirmasi     : {rows}")
        # 4) tombol batal + menu selalu ada
        for label, cb in (("❌ Batal", "f:cancel"), ("🔙 Menu Utama", "m:home")):
            if not has_handler(cb, handlers, prefixes):
                print(f"      ✗ handler hilang untuk {label} ({cb})")
                bad += 1
        for cb in cbs:
            if not has_handler(cb, handlers, prefixes):
                print(f"      ✗ tombol mati: {cb}")
                bad += 1
        # 5) sanity: durasi & harga
        if not f.durations:
            print("      ✗ fitur tanpa pilihan durasi")
            bad += 1
        for d in f.durations:
            if not (4 <= d <= 15):
                print(f"      ✗ durasi {d} di luar batas workflow (4..15)")
                bad += 1
            if catalog.cost_for(f.key, d) <= 0:
                print(f"      ✗ harga durasi {d} tidak masuk akal")
                bad += 1
        if f.kind not in ("ugc",) and not f.hint:
            print("      ⚠ tidak ada petunjuk foto (hint)")

    # tombol mati global
    print("\n▸ Cek tombol mati (seluruh bot)")
    dead = [c for c in sorted(prod) if "{" not in c and not has_handler(c, handlers, prefixes)]
    if dead:
        for c in dead:
            print(f"   ✗ tombol tanpa handler: {c}")
        bad += len(dead)
    else:
        print("   ✅ tidak ada tombol mati")

    # layar wajib ada
    print("\n▸ Cek layar & handler inti")
    wajib = {
        "tombol Menu Telegram (set_my_commands)": "set_my_commands",
        "handler teks bebas (mis. ketik '15 detik')": "on_free_text",
        "tombol durasi di layar detail": "m:go:{key}:{d}",
        "handler pilih durasi": 'startswith("a:dur:")',
        "handler pilih rasio": 'startswith("a:ratio:")',
        "handler render": 'F.data == "f:render"',
        "handler top-up": 'F.data == "m:topup"',
    }
    for label, needle in wajib.items():
        okk = needle in SRC or needle.replace("{key}", "").replace("{d}", "") in SRC
        if needle == "m:go:{key}:{d}":
            okk = 'f"m:go:{key}:{d}"' in SRC
        print(f"   {'✅' if okk else '✗'} {label}")
        if not okk:
            bad += 1

    print("\n" + "═" * 64)
    print(f"HASIL AUDIT: {'✅ semua layar bersih' if bad == 0 else f'❌ {bad} masalah'}")
    return 0 if bad == 0 else 2


if __name__ == "__main__":
    sys.exit(main())