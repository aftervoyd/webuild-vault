#!/usr/bin/env python3
"""Papan bukti: lebar layout di ukuran layar laptop/komputer umum."""
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/dejavu/"
def f(sz,b=True):
    try: return ImageFont.truetype(F+("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"),sz)
    except Exception: return ImageFont.load_default()
rows=[("layar-1920.png","1920 \u00d7 1080  \u2014  monitor Full HD (paling umum)"),
      ("layar-1366.png","1366 \u00d7 768  \u2014  laptop paling umum")]
TW=1360; gap,pad,lb=24,44,36
ims=[]
for fn,lb2 in rows:
    im=Image.open("/root/"+fn).convert("RGB"); s=TW/im.width
    ims.append((im.resize((TW,int(im.height*s)),Image.LANCZOS),lb2))
H=86+sum(i.height+lb+gap for i,_ in ims)+pad
board=Image.new("RGB",(TW+pad*2,H),(11,18,32)); d=ImageDraw.Draw(board)
for y in range(H):
    t=y/max(H-1,1); d.line([(0,y),(TW+pad*2,y)],fill=(int(11+26*t),int(18+34*t),int(32+52*t)))
d.text((pad,24),"Desa Digital Pamekaran  \u2014  versi website desktop",font=f(25),fill=(233,242,255))
d.text((pad,56),"sidebar permanen kiri  \u00b7  kolom Agenda Desa + kalender di kanan  \u00b7  TANPA navbar bawah",font=f(14,False),fill=(150,178,214))
yy=86
for im,lb2 in ims:
    d.text((pad,yy),lb2,font=f(15),fill=(198,219,245)); yy+=lb
    board.paste(im,(pad,yy)); d.rectangle([pad,yy,pad+im.width-1,yy+im.height-1],outline=(90,128,178),width=1)
    yy+=im.height+gap
board.save("/root/projects/desa-mobile/papan-lebar.png")
print("papan-lebar.png",board.size)
