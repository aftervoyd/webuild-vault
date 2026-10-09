#!/usr/bin/env python3
"""Susun CHARACTER SHEET machine-readable dari beberapa panel.

Kenapa: model (editor/i2v) membaca satu gambar. Kalau panel ditata dengan geometri TETAP dan setiap
panel berisi SATU tampilan (wajah close-up, badan depan, samping, belakang), maka:
 - `sheetfix.crop_panel()` bisa menemukan orangnya dengan andal (panel bersih, tidak tumpang tindih),
 - identitas & proporsi terjaga karena tiap panel dirender dari foto referensi yang SAMA,
 - user bisa lihat & verifikasi sendiri.

Aturan tata letak (supaya "mudah dibaca sistem"):
 - latar seragam, tanpa teks DI DALAM panel (label ditaruh di strip tipis di atas panel),
 - panel portrait rasio sama, tinggi sama, jarak (gutter) tetap,
 - urutan tetap: FACE → FRONT → SIDE → BACK.

Pakai:
  ./.venv/bin/python tools/make_sheet.py <nama> <keluar.png> \
      "FACE CLOSE UP:<file>" "FRONT FULL BODY:<file>" "SIDE FULL BODY:<file>" "BACK FULL BODY:<file>"
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sheetbuild

GUTTER = 24          # jarak antar panel (px)
LABEL_H = 64         # tinggi strip label (px)
MARGIN = 24
BG = (245, 245, 246)
INK = (28, 28, 32)
SUB = (95, 95, 105)
PH = 1280            # tinggi tiap panel


def _font(size: int) -> ImageFont.ImageFont:
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:                        # noqa: BLE001
                pass
    return ImageFont.load_default()


def fit(im: Image.Image, h: int) -> Image.Image:
    """Skala panel ke tinggi `h` (rasio dipertahankan) lalu center-crop ke rasio 2:3."""
    w = max(1, int(im.width * h / im.height))
    im = im.convert("RGB").resize((w, h), Image.LANCZOS)
    tw = int(h * 2 / 3)
    if w > tw:
        x = (w - tw) // 2
        im = im.crop((x, 0, x + tw, h))
    return im


def main() -> int:
    name, out = sys.argv[1], Path(sys.argv[2])
    panels = []
    for spec in sys.argv[3:]:
        label, _, path = spec.partition(":")
        if Path(path).exists():
            panels.append((label.strip(), Path(path)))
        else:
            print("⚠️  lewat (tidak ada):", path)
    res = sheetbuild.build(name, Path(out), panels)
    if not res:
        print("tidak ada panel"); return 1
    from PIL import Image
    im = Image.open(res)
    print(f"✅ sheet: {res} ({im.size[0]}×{im.size[1]}, {len(panels)} panel) {res.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())