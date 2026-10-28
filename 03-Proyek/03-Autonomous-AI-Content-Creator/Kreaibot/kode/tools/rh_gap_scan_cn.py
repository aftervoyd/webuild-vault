#!/usr/bin/env python3
"""Pindai celah pasokan RunningHub — versi istilah Mandarin (RH dominan China)."""
from __future__ import annotations

import json
import time
import urllib.request

URL = "https://www.runninghub.ai/api/search/workflow"
H = {"Content-Type": "application/json", "client": "web",
     "X-RH-Lang": "en", "User-Language": "en"}

KW = {
    "证件照 ID photo": "证件照", "一寸照 passport": "一寸照片", "写真 portrait": "写真",
    "头像 avatar": "头像", "商品图 product": "商品图", "电商 ecommerce": "电商",
    "抠图 matting": "抠图", "白底 white bg": "白底", "换装 outfit": "换装",
    "老照片修复 restore": "老照片修复", "修复 repair": "修复", "上色 colorize": "上色",
    "换脸 faceswap": "换脸", "保持一致性 consistency": "一致性", "模特换人": "模特换人",
    "放大 upscale": "放大", "超分": "超分", "去水印 watermark": "去水印",
    "室内设计 interior": "室内设计", "户型图 floorplan": "户型图", "建筑 render": "建筑表现",
    "美食 food": "美食", "菜单 menu": "菜单", "纹身 tattoo": "纹身",
    "服装 clothing": "服装", "珠宝 jewelry": "珠宝", "logo": "logo",
    "表情包 emoji": "表情包", "图标 icon": "图标", "漫画 comic": "漫画",
    "分镜 storyboard": "分镜", "字幕 subtitle": "字幕", "配音 dubbing": "配音",
    "印花 pattern": "印花", "无缝 seamless": "无缝", "像素 pixel": "像素",
    "海报 poster": "海报", "简历 resume": "简历", "PPT": "PPT",
    "宠物 pet": "宠物", "婚纱 wedding": "婚纱", "汽车 car": "汽车",
    "鞋 sneaker": "鞋子", "海报生成": "海报生成", "贴纸 sticker": "贴纸",
}


def count(kw: str) -> int | None:
    body = json.dumps({"search": kw, "current": 1, "size": 1}).encode()
    req = urllib.request.Request(URL, data=body, headers=H)
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            js = json.loads(r.read().decode())
        return int((js.get("data") or {}).get("total", 0))
    except Exception:  # noqa: BLE001
        return None


rows = []
for label, kw in KW.items():
    n = count(kw)
    rows.append((label, kw, n))
    print(f"{str(n):>6}  {kw:<8} {label}")
    time.sleep(0.35)

print("\n=== PALING KOSONG (celah nyata) ===")
for label, kw, n in sorted([r for r in rows if r[2] is not None], key=lambda x: x[2])[:18]:
    print(f"{n:>6}  {kw:<8} {label}")