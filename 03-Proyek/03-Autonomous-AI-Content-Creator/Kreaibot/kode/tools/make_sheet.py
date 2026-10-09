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

from PIL import Image, ImageDraw, ImageFont

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
    items = []
    for spec in sys.argv[3:]:
        label, _, path = spec.partition(":")
        p = Path(path)
        if p.exists():
            items.append((label.strip().upper(), p))
        else:
            print("⚠️  lewat (tidak ada):", path)
    if not items:
        print("tidak ada panel")
        return 1

    panels = [(lab, fit(Image.open(p), PH)) for lab, p in items]
    pw = max(im.width for _, im in panels)
    cols = 2
    rows = (len(panels) + cols - 1) // cols
    head = 120 if len(panels) > 1 else 0
    W = MARGIN * 2 + cols * pw + (cols - 1) * GUTTER
    H = MARGIN * 2 + head + rows * (LABEL_H + PH) + (rows - 1) * GUTTER
    sheet = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(sheet)

    if head:
        d.text((MARGIN, MARGIN + 10), f"{name.upper()} — CHARACTER SHEET", font=_font(46), fill=INK)
        d.text((MARGIN, MARGIN + 66),
               "Reference sheet for the bot · face close-up is the real photo; "
               "full-body panels are AI views generated FROM that photo",
               font=_font(24), fill=SUB)

    for i, (lab, im) in enumerate(panels):
        r, c = divmod(i, cols)
        x = MARGIN + c * (pw + GUTTER)
        y = MARGIN + head + r * (LABEL_H + PH + GUTTER)
        d.text((x, y + 12), lab, font=_font(32), fill=INK)
        sheet.paste(im, (x, y + LABEL_H))

    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=96)
    print(f"✅ sheet: {out} ({sheet.size[0]}×{sheet.size[1]}, {len(panels)} panel) "
          f"{out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())