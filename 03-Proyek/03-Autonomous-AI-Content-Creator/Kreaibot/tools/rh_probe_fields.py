#!/usr/bin/env python3
"""Cari nama field yang benar untuk sebuah node (dipakai saat API bilang field_not_found)."""
from __future__ import annotations
import asyncio, json, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
import aiohttp

KEY = os.getenv("RUNNINGHUB_API_KEY", "")
BASE = os.getenv("RUNNINGHUB_BASE", "https://www.runninghub.ai").rstrip("/")
WF = os.getenv("RUNNINGHUB_WF_ALLINONE", "2084116925483151361")
PROMPT = ("0-2s: handheld medium shot, the creator smiles to camera and lifts the product "
          "into frame, warm natural light. "
          "2-5s: gentle push-in to a close-up as the product label becomes clearly readable, "
          "same person and outfit throughout, subtle natural motion.")

async def create(s, node_list):
    async with s.post(f"{BASE}/task/openapi/create",
                      json={"apiKey": KEY, "workflowId": WF, "nodeInfoList": node_list},
                      headers={"Authorization": f"Bearer {KEY}"}) as r:
        return await r.json(content_type=None)

async def main():
    photos = sys.argv[1:3] or ["api/db5b58716c013e69ec439b68ab3383fef85f701d01ebe9d8c57563015d2d159d.png",
                               "api/5c9401cf9baed1423b9956c08b6641633a9b2673865db852359c3ac1ddd6dff3.png"]
    base_nodes = [{"nodeId": "4", "fieldName": "image", "fieldValue": photos[0]},
                  {"nodeId": "6", "fieldName": "image", "fieldValue": photos[1]}]
    cands = ["text", "prompt", "positive", "prompt_text", "text_prompt", "caption", "content",
             "string", "value", "instruction", "description", "texts", "text_input", "encode_text",
             "mini_max_text", "t2v_prompt", "clip_text", "text_1", "prompt1", "note"]
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
        for f in cands:
            nl = base_nodes + [{"nodeId": "8", "fieldName": f, "fieldValue": PROMPT}]
            js = await create(s, nl)
            code = js.get("code")
            if code == 0:
                tid = (js.get("data") or {}).get("taskId")
                print(f"✅ FIELD BENAR: '{f}'  → taskId={tid}")
                print("   (render dimulai! kita berhenti di sini biar gak boros coin)")
                return 0
            msg = str(js.get("msg", ""))
            print(f"   ✗ {f:14s} → {code} {msg[:80]}")
    print("❌ gak ada kandidat yang cocok — perlu liat panel API di web (klik tombol 'API')")
    return 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
