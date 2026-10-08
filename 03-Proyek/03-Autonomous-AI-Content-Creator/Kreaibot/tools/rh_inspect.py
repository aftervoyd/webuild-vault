#!/usr/bin/env python3
"""Inspeksi workflow RunningHub: tarik definisi node + NAMA FIELD yang valid.

Dipakai SETELAH API key masuk. Tujuannya: dapat nama field persis buat
nodeInfoList (biar binding image/prompt/rasio gak nebak-nebak).

  .venv/bin/python tools/rh_inspect.py 2084116925483151361
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

import aiohttp  # noqa: E402

CANDIDATES = ("/task/openapi/getWorkflowJson", "/task/openapi/workflowJson",
              "/task/openapi/getWorkflow", "/uc/openapi/workflowJson")


async def main() -> int:
    wf = sys.argv[1] if len(sys.argv) > 1 else os.getenv("RUNNINGHUB_WF_ALLINONE", "")
    key = os.getenv("RUNNINGHUB_API_KEY", "")
    base = os.getenv("RUNNINGHUB_BASE", "https://www.runninghub.ai").rstrip("/")
    if not wf or not key:
        print("❌ butuh workflowId (argumen / RUNNINGHUB_WF_ALLINONE) + RUNNINGHUB_API_KEY di .env")
        return 1

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
        for path in CANDIDATES:
            try:
                async with s.post(f"{base}{path}",
                                  json={"apiKey": key, "workflowId": wf},
                                  headers={"Authorization": f"Bearer {key}"}) as r:
                    txt = await r.text()
                    print(f"═══ {path} → HTTP {r.status} ({len(txt)} bytes)")
                    if r.status == 200:
                        try:
                            js = json.loads(txt)
                        except json.JSONDecodeError:
                            print(txt[:800]); continue
                        dumped = json.dumps(js, ensure_ascii=False)
                        open(ROOT / "workflows" / f"rhjson_{wf}.json", "w").write(dumped)
                        print("   tersimpan →", ROOT / f"workflows/rhjson_{wf}.json")
                        # ringkas: node + field
                        data = js.get("data", js)
                        nodes = data.get("nodes") if isinstance(data, dict) else None
                        if nodes:
                            for n in nodes:
                                print(f"   node {n.get('id') or n.get('nodeId')} "
                                      f"{n.get('type') or n.get('nodeName') or ''} "
                                      f"fields={list((n.get('inputs') or {}).keys()) or n.get('fieldNames')}")
                        else:
                            print("   struktur:", dumped[:600])
                        return 0
                    print("   ", txt[:200])
            except Exception as e:      # noqa: BLE001
                print(f"═══ {path} → error: {e}")
    print("\n⚠️  semua kandidat gagal — kirim output ini ke gue, kita cari endpoint yang benar.")
    return 2


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))