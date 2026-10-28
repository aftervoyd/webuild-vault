#!/usr/bin/env python3
"""Uji-jalan workflow TEXT-TO-IMAGE via OpenAPI RunningHub (tanpa upload gambar).

Contoh:
  .venv/bin/python tools/rh_test_txt2img.py --wf 2108766028850372610 \
      --prompt "menu poster: nasi goreng ... judul \"MENU SPESIAL\""
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
import time
from pathlib import Path

import aiohttp
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("RUNNINGHUB_API_KEY", "")
BASE = (os.getenv("RUNNINGHUB_BASE") or "https://www.runninghub.ai").rstrip("/")
H = {"Authorization": f"Bearer {API_KEY}"}


async def post(path: str, payload: dict) -> dict:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=180)) as s:
        async with s.post(f"{BASE}{path}", json=payload, headers=H) as r:
            return await r.json(content_type=None)


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wf", required=True)
    ap.add_argument("--node", default="7", help="nodeId CLIPTextEncode yang diisi user")
    ap.add_argument("--field", default="text")
    ap.add_argument("--prompt", default="", help="kosongkan untuk pakai default workflow")
    a = ap.parse_args()

    if not API_KEY:
        print("API_KEY kosong")
        return 1

    node_list = []
    if a.prompt:
        node_list.append({"nodeId": a.node, "fieldName": a.field, "fieldValue": a.prompt})

    print(f"1) create task | wf={a.wf} | override={len(node_list)} node")
    js = await post("/task/openapi/create",
                    {"apiKey": API_KEY, "workflowId": a.wf, "nodeInfoList": node_list})
    print("   resp:", str(js)[:300])
    tid = (js.get("data") or {}).get("taskId") if isinstance(js.get("data"), dict) else None
    if not tid:
        print("GAGAL create:", js)
        return 2
    print("   taskId:", tid)

    print("2) polling...")
    t0 = time.time()
    while time.time() - t0 < 900:
        o = await post("/task/openapi/outputs", {"apiKey": API_KEY, "taskId": tid})
        code = o.get("code")
        if code == 0 and o.get("data"):
            print("SELESAI", round(time.time() - t0, 1), "s")
            for f in o["data"]:
                print("   ", f.get("fileType"), f.get("fileUrl"))
            return 0
        print("   ...", o.get("msg"), "code", code, str(o.get("data"))[:200])
        if code in (805, 804):
            return 3
        await asyncio.sleep(8)
    print("timeout")
    return 4


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))