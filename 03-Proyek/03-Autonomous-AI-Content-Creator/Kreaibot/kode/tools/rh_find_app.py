#!/usr/bin/env python3
"""Coba beberapa app RunningHub berturut-turut sampai ada yang jalan (app kembar sering beda nasib).

Pakai: ./.venv/bin/python tools/rh_find_app.py <foto> '<prompt>' <out_dir> <appId> [<appId> ...]
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from dotenv import load_dotenv                       # noqa: E402

load_dotenv(ROOT / ".env")

NODES = [{"nodeId": "9", "fieldName": "image", "value": "@photo1"},
         {"nodeId": "4", "fieldName": "text", "value": "@prompt"},
         {"nodeId": "8", "fieldName": "resolution", "value": "2k"}]


def koin() -> int:
    key = os.getenv("RUNNINGHUB_API_KEY", "")
    req = urllib.request.Request("https://www.runninghub.cn/uc/openapi/accountStatus",
                                 data=json.dumps({"apikey": key}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    return int((json.load(urllib.request.urlopen(req, timeout=40)).get("data") or {}).get("remainCoins") or 0)


async def coba(app_id: str, photo: Path, prompt: str, out: Path) -> bool:
    from backends import GenRequest
    from backends.runninghub import RunningHubBackend
    os.environ["RUNNINGHUB_APP_EDITOR"] = app_id
    os.environ["RUNNINGHUB_APP_NODES_EDITOR"] = json.dumps(NODES)
    be = RunningHubBackend(os.getenv("RUNNINGHUB_API_KEY", ""), os.getenv("RUNNINGHUB_BASE", ""),
                           upload_key=os.getenv("RUNNINGHUB_UPLOAD_KEY", ""))
    t0, before = time.time(), koin()
    try:
        task = await be.submit(GenRequest(job_id=996, feature_key="editor", workflow="", photos=[photo],
                                          prompt=prompt, ratio="9:16", duration=0, out_path=out))
        while time.time() - t0 < 420:
            st = await be.poll(task)
            el = int(time.time() - t0)
            if st.state == "done":
                rp = str(st.result_path or "")
                if rp.startswith("http"):
                    r = urllib.request.Request(rp, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(r, timeout=240) as resp, open(out, "wb") as f:
                        f.write(resp.read())
                try:
                    from PIL import Image
                    im = Image.open(out)
                    sz = f"{im.size[0]}×{im.size[1]} rasio {im.size[0] / im.size[1]:.3f}"
                except Exception:
                    sz = "?"
                print(f"✅ APP {app_id} JALAN · {el}s · {before - koin()} koin · {sz} → {out}")
                return True
            if st.state == "failed":
                print(f"❌ app {app_id} gagal ({el}s): {str(st.error)[:70]}")
                return False
            await asyncio.sleep(5)
        print(f"❌ app {app_id} timeout")
    except Exception as e:                                # noqa: BLE001
        print(f"❌ app {app_id} error: {type(e).__name__}: {str(e)[:80]}")
    return False


async def main() -> int:
    photo, prompt, out_dir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    apps = sys.argv[4:]
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, app in enumerate(apps):
        if await coba(app, photo, prompt, out_dir / f"coba_{app}.png"):
            return 0
        await asyncio.sleep(3)
    print("semua app gagal — coba lain waktu / app lain")
    return 1


if __name__ == "__main__":
    os.chdir(ROOT)
    raise SystemExit(asyncio.run(main()))