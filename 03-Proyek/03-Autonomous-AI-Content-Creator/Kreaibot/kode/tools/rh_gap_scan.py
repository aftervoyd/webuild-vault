#!/usr/bin/env python3
"""Pindai celah pasokan di RunningHub: hitung jumlah workflow publik per niche.

Pakai: .venv/bin/python tools/rh_gap_scan.py
"""
from __future__ import annotations

import json
import time
import urllib.request

URL = "https://www.runninghub.ai/api/search/workflow"
H = {"Content-Type": "application/json", "client": "web",
     "X-RH-Lang": "en", "User-Language": "en"}

KEYWORDS = [
    "passport photo", "id photo", "visa photo", "证件照", "photo booth",
    "product photo", "ecommerce photo", "product shot", "catalog photo",
    "headshot", "professional headshot", "linkedin photo",
    "old photo restore", "colorize", "photo restoration", "denoise old photo",
    "face swap", "character consistency", "identity", "portrait",
    "upscale", "enhance", "image matting", "background remove",
    "interior design", "real estate", "floor plan", "architectural render",
    "food photo", "menu design", "restaurant",
    "tattoo design", "tshirt mockup", "merch", "jewelry design",
    "logo", "sticker", "emoji", "icon set",
    "comic", "manga", "storyboard", "anime",
    "subtitle", "video caption", "translate", "voice clone", "dubbing",
    "seamless texture", "pattern", "3d isometric", "pixel art",
    "poster", "flyer", "banner", "social media post",
    "resume", "cv template", "presentation slide",
    "pet portrait", "wedding photo", "car photo", "sneaker design",
]


def count(kw: str) -> int | None:
    body = json.dumps({"search": kw, "current": 1, "size": 1}).encode()
    req = urllib.request.Request(URL, data=body, headers=H)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            js = json.loads(r.read().decode())
        return int((js.get("data") or {}).get("total", 0))
    except Exception as e:  # noqa: BLE001
        print("  err", kw, e)
        return None


rows = []
for kw in KEYWORDS:
    n = count(kw)
    rows.append((kw, n))
    print(f"{str(n):>6}  {kw}")
    time.sleep(0.4)

print("\n=== PALING KOSONG (celah) ===")
for kw, n in sorted([r for r in rows if r[1] is not None], key=lambda x: x[1])[:20]:
    print(f"{n:>6}  {kw}")