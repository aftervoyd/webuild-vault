"""Tata letak CHARACTER SHEET machine-readable — SATU sumber kebenaran.

Dipakai bareng oleh:
 - `tools/make_sheet.py` (bikin sheet manual dari panel),
 - `chargen.py` (Character Creator: sheet master dari foto + pilihan user),
 - `sheetfix.py` (bot MEMBACA sheet → harus tahu geometri yang sama persis).

Kenapa dipisah: kalau angka tata letak ditulis di banyak tempat, sekali berubah → bot salah potong
panel (persis bug 9 Okt: bot nyomot judul + potongan wajah sebagai "panel referensi").
"""
from __future__ import annotations

from pathlib import Path

# Angka tetap — JANGAN diubah tanpa mengubah sheetfix.GRID.
GRID = {"cols": 2, "margin": 24, "gutter": 24, "label_h": 64, "ph": 1280, "head": 120}

BG = (245, 245, 246)
INK = (28, 28, 32)
SUB = (95, 95, 105)
SUB_DEFAULT = ("Reference sheet for the bot · every panel is a REAL reference photo of her "
               "(no AI-generated body)")


def _font(size: int):
    from PIL import ImageFont
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:                                # noqa: BLE001
                pass
    return ImageFont.load_default()


def fit(im, h: int):
    """Skala panel ke tinggi `h` (rasio dipertahankan) lalu center-crop ke rasio 2:3."""
    from PIL import Image
    w = max(1, int(im.width * h / im.height))
    im = im.convert("RGB").resize((w, h), Image.LANCZOS)
    tw = int(h * 2 / 3)
    if w > tw:
        x = (w - tw) // 2
        im = im.crop((x, 0, x + tw, h))
    return im


def layout_panels(size: tuple[int, int]) -> list[tuple[int, int, int, int]] | None:
    """Kotak semua panel untuk sheet buatan kita (kiri→kanan, atas→bawah). None kalau bukan sheet kita."""
    try:
        W, H = int(size[0]), int(size[1])
    except Exception:                                        # noqa: BLE001
        return None
    g = GRID
    pw = (W - 2 * g["margin"] - (g["cols"] - 1) * g["gutter"]) // g["cols"]
    if pw < 100:
        return None
    for head in (g["head"], 0):
        for rows in range(1, 9):
            if 2 * g["margin"] + head + rows * (g["label_h"] + g["ph"]) \
               + (rows - 1) * g["gutter"] != H:
                continue
            out = []
            for i in range(rows * g["cols"]):
                r, c = divmod(i, g["cols"])
                x = g["margin"] + c * (pw + g["gutter"])
                y = g["margin"] + head + r * (g["label_h"] + g["ph"] + g["gutter"]) + g["label_h"]
                out.append((x, y, pw, g["ph"]))
            return out
    return None


def build(name: str, out_path: Path, panels: list[tuple[str, Path]],
          subtitle: str = SUB_DEFAULT) -> Path | None:
    """Susun sheet dari panel [(label, path)] → simpan ke out_path."""
    from PIL import Image, ImageDraw
    items = []
    for lab, p in panels:
        p = Path(p)
        if p.exists():
            items.append((lab.strip().upper(), fit(Image.open(p), GRID["ph"])))
    if not items:
        return None
    pw = max(im.width for _, im in items)
    cols = GRID["cols"]
    rows = (len(items) + cols - 1) // cols
    head = GRID["head"] if len(items) > 1 else 0
    W = GRID["margin"] * 2 + cols * pw + (cols - 1) * GRID["gutter"]
    H = (GRID["margin"] * 2 + head + rows * (GRID["label_h"] + GRID["ph"])
         + (rows - 1) * GRID["gutter"])
    sheet = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(sheet)
    if head:
        d.text((GRID["margin"], GRID["margin"] + 10), f"{name.upper()} — CHARACTER SHEET",
               font=_font(46), fill=INK)
        d.text((GRID["margin"], GRID["margin"] + 66), subtitle, font=_font(24), fill=SUB)
    for i, (lab, im) in enumerate(items):
        r, c = divmod(i, cols)
        x = GRID["margin"] + c * (pw + GRID["gutter"])
        y = GRID["margin"] + head + r * (GRID["label_h"] + GRID["ph"] + GRID["gutter"])
        d.text((x, y + 12), lab, font=_font(32), fill=INK)
        sheet.paste(im, (x, y + GRID["label_h"]))
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, quality=96)
    return out_path