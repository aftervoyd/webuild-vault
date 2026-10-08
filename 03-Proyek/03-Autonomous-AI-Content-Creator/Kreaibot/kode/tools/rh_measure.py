#!/usr/bin/env python3
"""Ukur BIAYA (consumeCoins) render RunningHub untuk rasio & durasi tertentu.

Pakai: .venv/bin/python tools/rh_measure.py --ratio 9:16 --duration 15 --photo depan.png --photo belakang.png
Mencetak: taskId, consumeCoins, taskCostTime, url output, dan estimasi Rp.
Tidak menyimpan video (kecuali --out diberikan).
"""
from __future__ import annotations
import argparse, asyncio, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
import aiohttp
from backends import GenRequest
from backends.runninghub import RunningHubBackend

KURS = float(os.getenv("KURS_USD_IDR", "16200"))
RUPIAH_PER_KOIN = float(os.getenv("RUPIAH_PER_KOIN", "4.46"))   # dari paket Dasar $9,9/36.000

PROMPT = ("0-3s: handheld medium shot, the creator lifts the product toward the camera, warm light. "
          "3-7s: gentle push-in, product label becomes sharp and readable, natural movement, consistent person.")


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ratio", default="9:16")
    ap.add_argument("--duration", type=int, default=5)
    ap.add_argument("--feature", default="allinone")
    ap.add_argument("--photo", action="append", required=True)
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    be = RunningHubBackend(api_key=os.getenv("RUNNINGHUB_API_KEY"),
                           base=os.getenv("RUNNINGHUB_BASE", "https://www.runninghub.ai"),
                           work_dir=str(ROOT / "work"))
    req = GenRequest(job_id=0, feature_key=a.feature, workflow=a.feature,
                     photos=[Path(p) for p in a.photo], prompt=PROMPT,
                     ratio=a.ratio, duration=a.duration)

    print(f"→ rasio={a.ratio} durasi={a.duration}s fitur={a.feature} foto={len(a.photo)}")
    uploaded = [await be.upload(Path(p)) for p in a.photo]
    print("  upload:", uploaded)
    payload = {"apiKey": be.api_key, "workflowId": be._workflow_id(a.feature),
               "nodeInfoList": be._bind(be._node_bindings(a.feature), req, uploaded)}
    print("  nodeInfoList:", payload["nodeInfoList"])
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as s:
        async with s.post(f"{be.base}/task/openapi/create", json=payload,
                          headers={"Authorization": f"Bearer {be.api_key}"}) as r:
            js = await r.json(content_type=None)
    tid = str((js.get("data") or {}).get("taskId") or "")
    if not tid:
        print("❌ gagal create:", js); return 1
    print("  taskId:", tid, "— menunggu render…")
    t0 = time.time()
    while time.time() - t0 < 1500:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
            async with s.post(f"{be.base}/task/openapi/status", json={"apiKey": be.api_key, "taskId": tid},
                              headers={"Authorization": f"Bearer {be.api_key}"}) as r:
                st = (await r.json(content_type=None)).get("data")
        if st == "SUCCESS":
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
                async with s.post(f"{be.base}/task/openapi/outputs", json={"apiKey": be.api_key, "taskId": tid},
                                  headers={"Authorization": f"Bearer {be.api_key}"}) as r:
                    out = (await r.json(content_type=None)).get("data") or []
            for it in out:
                koin = it.get("consumeCoins")
                print(f"\n✅ SELESAI dalam {int(time.time()-t0)}s")
                print(f"   💰 consumeCoins = {koin}  (≈ Rp{float(koin or 0)*RUPIAH_PER_KOIN:,.0f} @ Rp{RUPIAH_PER_KOIN}/koin)")
                print(f"   ⏱  taskCostTime = {it.get('taskCostTime')}s")
                print(f"   🔗 {it.get('fileUrl')}")
                if a.out:
                    from bot import fetch_url
                    d = await fetch_url(str(it.get("fileUrl")), Path(a.out))
                    print("   ⬇ tersimpan:", d, d.stat().st_size, "bytes")
            return 0
        if st in ("FAILED", "CANCEL"):
            print("❌ task", st); return 1
        await asyncio.sleep(10)
    print("⏰ timeout"); return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
