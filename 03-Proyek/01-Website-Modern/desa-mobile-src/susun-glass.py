#!/usr/bin/env python3
"""Susun papan presentasi: 4 layar mobile + 2 tampilan website."""
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def fnt(sz, bold=True):
    try:
        return ImageFont.truetype(FONT_DIR + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)
    except Exception:
        return ImageFont.load_default()

# ---------- papan MOBILE ----------
layar = [("m-login.png", "Login"), ("m-dash.png", "Dashboard"),
         ("m-drawer.png", "Menu Samping"), ("m-pasar.png", "Pasar UMKM")]
skala = 0.82
w, h = int(390 * skala), int(844 * skala)
gap, pad_top, pad_side, pad_bot = 26, 78, 44, 46
judul_h = 0
W = pad_side * 2 + w * 4 + gap * 3
H = pad_top + judul_h + h + 34 + pad_bot
papan = Image.new("RGB", (W, H), (11, 18, 32))
d = ImageDraw.Draw(papan)
# gradien halus
for y in range(H):
    t = y / max(H - 1, 1)
    d.line([(0, y), (W, y)], fill=(int(11 + 26 * t), int(18 + 34 * t), int(32 + 52 * t)))
d.text((pad_side, 26), "Desa Digital Pamekaran  \u2014  Glassmorphism", font=fnt(25), fill=(233, 242, 255))
d.text((pad_side, 54), "fokus mobile device  \u00b7  nav pil melayang, beranda di tengah",
       font=fnt(14, False), fill=(150, 178, 214))
for i, (fn, label) in enumerate(layar):
    x = pad_side + i * (w + gap)
    im = Image.open(fn).convert("RGB").resize((w, h), Image.LANCZOS)
    # bayangan
    sh = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([10, 10, w + 10, h + 10], 20, fill=(0, 0, 0, 120))
    papan.paste(Image.new("RGB", (w + 20, h + 20), (0, 0, 0)), (x - 10, pad_top + judul_h - 10), sh)
    papan.paste(im, (x, pad_top + judul_h))
    d.rectangle([x, pad_top + judul_h, x + w - 1, pad_top + judul_h + h - 1], outline=(90, 128, 178), width=1)
    tw = d.textlength(label, font=fnt(15))
    d.text((x + (w - tw) / 2, pad_top + judul_h + h + 12), label, font=fnt(15), fill=(198, 219, 245))
papan.save("presentasi-glass.png")
print("presentasi-glass.png", papan.size)

# ---------- papan WEBSITE ----------
web = [("w-dash.png", "Versi website \u2014 dashboard (6 tile sebaris, berita susun ke bawah)"),
       ("w-pasar.png", "Versi website \u2014 pasar UMKM (kotak pencarian + 4 kolom)"),
       ("w-login.png", "Versi website \u2014 login")]
s2 = 0.55
imgs = [(Image.open(fn).convert("RGB"), lb) for fn, lb in web]
scaled = [(im.resize((int(im.width * s2), int(im.height * s2)), Image.LANCZOS), lb) for im, lb in imgs]
gap2, pad2 = 22, 40
W2 = pad2 * 2 + max(s.width for s, _ in scaled)
lbl_h = 34
H2 = 76 + sum(s.height + lbl_h + gap2 for s, _ in scaled) + pad2
papan2 = Image.new("RGB", (W2, H2), (11, 18, 32))
d2 = ImageDraw.Draw(papan2)
for y in range(H2):
    t = y / max(H2 - 1, 1)
    d2.line([(0, y), (W2, y)], fill=(int(11 + 26 * t), int(18 + 34 * t), int(32 + 52 * t)))
d2.text((pad2, 22), "Desa Digital Pamekaran  \u2014  versi website", font=fnt(24), fill=(233, 242, 255))
yy = 66
for sim, lb in scaled:
    d2.text((pad2, yy), lb, font=fnt(14, False), fill=(160, 188, 222))
    yy += lbl_h
    papan2.paste(sim, (pad2, yy))
    d2.rectangle([pad2, yy, pad2 + sim.width - 1, yy + sim.height - 1], outline=(90, 128, 178), width=1)
    yy += sim.height + gap2
papan2.save("presentasi-web.png")
print("presentasi-web.png", papan2.size)