#!/usr/bin/env python3
"""Papan versi website desktop (final). Semua sumber dirender dgn &nofx=1."""
from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/truetype/dejavu/"
def f(sz, b=True):
    try: return ImageFont.truetype(F + ("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), sz)
    except Exception: return ImageFont.load_default()
TW, gap, pad, lb = 1360, 24, 44, 36
def board(rows, judul, sub, out):
    ims = []
    for fn, l in rows:
        im = Image.open("/root/" + fn).convert("RGB"); s = TW / im.width
        ims.append((im.resize((TW, int(im.height * s)), Image.LANCZOS), l))
    H = 86 + sum(i.height + lb + gap for i, _ in ims) + pad
    b = Image.new("RGB", (TW + pad * 2, H), (11, 18, 32)); d = ImageDraw.Draw(b)
    for y in range(H):
        t = y / max(H - 1, 1)
        d.line([(0, y), (TW + pad * 2, y)], fill=(int(11 + 26 * t), int(18 + 34 * t), int(32 + 52 * t)))
    d.text((pad, 24), judul, font=f(25), fill=(233, 242, 255))
    d.text((pad, 56), sub, font=f(14, False), fill=(150, 178, 214))
    yy = 86
    for im, l in ims:
        d.text((pad, yy), l, font=f(15), fill=(198, 219, 245)); yy += lb
        b.paste(im, (pad, yy))
        d.rectangle([pad, yy, pad + im.width - 1, yy + im.height - 1], outline=(90, 128, 178), width=1)
        yy += im.height + gap
    b.save(out); print(out, b.size)
board([("layar-1920.png", "1920 \u00d7 1080  \u2014  monitor Full HD (paling umum)"),
       ("layar-1366.png", "1366 \u00d7 768  \u2014  laptop paling umum")],
      "Desa Digital Pamekaran  \u2014  versi website desktop (final)",
      "sidebar permanen kiri \u00b7 lonceng di sidebar (Pemberitahuan) \u00b7 TANPA bar judul & navbar bawah \u00b7 kolom Agenda Desa + kalender",
      "/root/papan-desktop-1.png")
board([("layar-1920-pasar.png", "1920 \u00d7 1080  \u2014  Pasar UMKM (pencarian + grid produk mengisi penuh)"),
       ("layar-1920-login.png", "1920 \u00d7 1080  \u2014  Login (tanpa sidebar, kartu di tengah)")],
      "Desa Digital Pamekaran  \u2014  versi website desktop (lanjutan)",
      "halaman lain di versi desktop",
      "/root/papan-desktop-2.png")
