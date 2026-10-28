#!/usr/bin/env python3
"""Helper GUI Telegram Desktop headless: ocr + aksi xdotool."""
import csv, subprocess, sys, time
from PIL import Image, ImageOps

DISP = ":99"
WIN = "4194326"


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


def key(k, delay=0.06):
    sh(f'DISPLAY={DISP} xdotool windowfocus --sync {WIN}')
    sh(f'DISPLAY={DISP} xdotool key --delay {int(delay*1000)} {k}')


def typ(text, delay=90):
    sh(f'DISPLAY={DISP} xdotool windowfocus --sync {WIN}')
    sh(f'DISPLAY={DISP} xdotool type --delay {delay} -- {text!r}'.replace("'", "'\\''"))


def click(x, y):
    sh(f'DISPLAY={DISP} xdotool windowfocus --sync {WIN}')
    sh(f'DISPLAY={DISP} xdotool mousemove {x} {y} click 1')


def shot(path="/tmp/tg.png"):
    sh(f'DISPLAY={DISP} scrot -o {path}')
    return path


def ocr(png, box, scale=2, psm=11, thr=None):
    """box = (x0,y0,x1,y1) pada pixel SCREEN. Kembalikan [(teks, screen_x, screen_y, conf)]"""
    im = Image.open(png).convert("L").crop(box)
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    px = list(im.getdata())
    dark_text = (sum(px) / len(px)) >= 115
    if not dark_text:
        im = ImageOps.invert(im)
    t = thr if thr is not None else (145 if dark_text else 130)
    im = im.point(lambda p: 0 if p < t else 255)
    im.save("/tmp/ocr_in.png")
    out = subprocess.run(["tesseract", "/tmp/ocr_in.png", "stdout", "--psm", str(psm), "tsv"],
                         capture_output=True, text=True).stdout
    res = []
    for r in csv.DictReader(out.splitlines(), delimiter="\t"):
        txt = (r.get("text") or "").strip()
        try:
            conf = float(r.get("conf") or -1)
        except ValueError:
            conf = -1
        if not txt or conf < 30:
            continue
        x = box[0] + int(r["left"]) / scale
        y = box[1] + int(r["top"]) / scale
        w = int(r["width"]) / scale
        h = int(r["height"]) / scale
        res.append((txt, round(x + w / 2), round(y + h / 2), round(conf)))
    return res