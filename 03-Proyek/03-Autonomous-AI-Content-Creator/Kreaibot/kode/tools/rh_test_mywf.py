#!/usr/bin/env python3
"""Uji-jalan workflow orisinal 'qwen-consistency-edit' via OpenAPI RunningHub.

Upload foto -> create task (isi node LoadImage id=6) -> poll hasil.
Pakai:  .venv/bin/python tools/rh_test_mywf.py --photo work/inventory_fix/1_Arunika.jpg \
            --wf 2108636907092680705 --node 6 --prompt "..."
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


async def upload(p: Path) -> str:
    data = aiohttp.FormData()
    data.add_field("apiKey", API_KEY)
    data.add_field("fileType", "image")
    data.add_field("file", p.read_bytes(), filename=p.name,
                   content_type="application/octet-stream")
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300)) as s:
        async with s.post(f"{BASE}/task/openapi/upload", data=data, headers=H) as r:
            js = await r.json(content_type=None)
    d = js.get("data")
    if isinstance(d, dict):
        for k in ("fileName", "file", "name"):
            v = d.get(k)
            if isinstance(v, str) and v:
                return v
    raise RuntimeError(f"upload gagal: {js}")


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--photo", required=True)
    ap.add_argument("--wf", required=True)
    ap.add_argument("--node", default="6", help="nodeId LoadImage")
    ap.add_argument("--prompt", default="")
    a = ap.parse_args()

    if not API_KEY:
        print("API_KEY kosong"); return 1

    print("1) upload:", a.photo)
    name = await upload(Path(a.photo))
    print("   ->", name)

    node_list = [{"nodeId": a.node, "fieldName": "image", "fieldValue": name}]
    print("2) create task untuk workflow", a.wf)
    js = await post("/task/openapi/create",
                    {"apiKey": API_KEY, "workflowId": a.wf, "nodeInfoList": node_list})
    print("   resp:", js)
    if js.get("code") not in (0, 200) and not js.get("data"):
        print("❌ create gagal"); return 2
    tid = (js.get("data") or {}).get("taskId")
    if not tid:
        print("❌ tidak ada taskId"); return 2
    print("   taskId:", tid)

    print("3) polling...")
    t0 = time.time()
    while time.time() - t0 < 900:
        o = await post("/task/openapi/outputs", {"apiKey": API_KEY, "taskId": tid})
        code = o.get("code")
        if code == 0 and o.get("data"):
            print("✅ SELESAI", round(time.time() - t0, 1), "s")
            for f in o["data"]:
                print("   ", f.get("fileType"), f.get("fileUrl"))
            return 0
        if code == 805:
            print("❌ TASK GAGAL:", o.get("msg"), str(o.get("data"))[:600])
            return 3
        print("   ...", o.get("msg"), "code", code)
        await asyncio.sleep(8)
    print("⏰ timeout"); return 4


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))