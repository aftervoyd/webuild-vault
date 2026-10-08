#!/usr/bin/env python3
"""VIDEO PANJANG dengan menyambung klip (workflow FL2VA maks 15 detik/render).

Cara kerja:
  1. Klip ke-1  : frame awal = foto-1, frame akhir = foto-2 (kalau ada).
  2. Klip ke-2+ : ambil FRAME TERAKHIR klip sebelumnya → jadi frame awal klip berikutnya
                  (mode first-frame-to-video, terbukti jalan), prompt = segmen cerita berikutnya.
  3. Semua klip disambung jadi satu file dengan ffmpeg (stream copy).

Pakai:
  .venv/bin/python tools/rh_long.py --dry --duration 30 --photo a.png --photo b.png
  .venv/bin/python tools/rh_long.py --duration 30 --photo a.png --photo b.png --style promo \
      --brief "serum wajah, promo diskon" --out work/hasil-30s.mp4
"""
from __future__ import annotations

import argparse
import asyncio
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

import aiohttp  # noqa: E402
from backends import GenRequest  # noqa: E402
from backends.runninghub import RunningHubBackend  # noqa: E402
import promptsmith as ps  # noqa: E402

MAX_CLIP = 15          # batas workflow FL2VA (terverifikasi dari validasi API)
MIN_CLIP = 4
KURS = float(os.getenv("KURS_USD_IDR", "16200"))
RUPIAH_PER_KOIN = float(os.getenv("RUPIAH_PER_KOIN", "4.46"))
FFMPEG = os.getenv("FFMPEG_BIN") or "ffmpeg"
FFPROBE = os.getenv("FFPROBE_BIN") or "ffprobe"


def ffmpeg(work: Path, args: list[str]) -> None:
    r = subprocess.run([FFMPEG, "-v", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg gagal: {r.stderr[:300]}")


def durasi_file(p: Path) -> float:
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(p)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


async def poll_task(be: RunningHubBackend, tid: str, maks: int = 1500) -> dict:
    t0 = time.time()
    while time.time() - t0 < maks:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
            async with s.post(f"{be.base}/task/openapi/status",
                              json={"apiKey": be.api_key, "taskId": tid},
                              headers={"Authorization": f"Bearer {be.api_key}"}) as r:
                st = (await r.json(content_type=None)).get("data")
        if st == "SUCCESS":
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
                async with s.post(f"{be.base}/task/openapi/outputs",
                                  json={"apiKey": be.api_key, "taskId": tid},
                                  headers={"Authorization": f"Bearer {be.api_key}"}) as r:
                    js = await r.json(content_type=None)
            return (js.get("data") or [{}])[0]
        if st in ("FAILED", "CANCEL"):
            raise RuntimeError(f"task {tid} → {st}")
        await asyncio.sleep(10)
    raise RuntimeError(f"task {tid} timeout")


async def render_clip(be: RunningHubBackend, frame: str, prompt: str, ratio: str,
                      durasi: int, with_last: str | None) -> tuple[str, str, int]:
    """Render 1 klip. frame/with_last = nama file hasil upload. Balikin (taskId, url, koin)."""
    req = GenRequest(job_id=0, feature_key="allinone", workflow="allinone",
                     photos=[Path("x")], prompt=prompt, ratio=ratio, duration=durasi)
    bindings = be._node_bindings("allinone")          # dari .env
    # node 4 = frame awal; node 6 hanya kalau ada frame akhir
    fixed = []
    for b in bindings:
        if str(b.get("nodeId")) == "4":
            fixed.append({"nodeId": "4", "fieldName": "image", "value": frame})
        elif str(b.get("nodeId")) == "6":
            if with_last:
                fixed.append({"nodeId": "6", "fieldName": "image", "value": with_last})
        else:
            fixed.append(b)
    payload = {"apiKey": be.api_key, "workflowId": be._workflow_id("allinone"),
               "nodeInfoList": be._bind(fixed, req, [frame, with_last or frame])}
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as s:
        async with s.post(f"{be.base}/task/openapi/create", json=payload,
                          headers={"Authorization": f"Bearer {be.api_key}"}) as r:
            js = await r.json(content_type=None)
    tid = str((js.get("data") or {}).get("taskId") or "")
    if not tid:
        raise RuntimeError(f"create klip gagal: {js}")
    out = await poll_task(be, tid)
    return tid, str(out.get("fileUrl") or ""), int(out.get("consumeCoins") or 0)


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--photo", action="append", required=True, help="1-2 foto (awal[, akhir])")
    ap.add_argument("--duration", type=int, default=30, help="total durasi video (detik)")
    ap.add_argument("--ratio", default="9:16")
    ap.add_argument("--style", default="promo")
    ap.add_argument("--brief", default="produk berkualitas, tampilkan manfaatnya")
    ap.add_argument("--out", default="work/hasil-panjang.mp4")
    ap.add_argument("--dry", action="store_true", help="cuma tampilkan rencana klip")
    a = ap.parse_args()

    total = a.duration
    if total < MIN_CLIP:
        print(f"⚠️  durasi minimum {MIN_CLIP}s (batas workflow) — dinaikkan dari {total}s")
        total = MIN_CLIP
    # bagi rata jadi N klip, masing-masing ≤ MAX_CLIP dan ≥ MIN_CLIP
    n = max(1, -(-total // MAX_CLIP))
    dasar, lebih = divmod(total, n)
    klips = [dasar + (1 if i < lebih else 0) for i in range(n)]

    st = ps.STYLES.get(a.style) or ps.STYLES["promo"]
    print(f"▶ total {total}s → {len(klips)} klip: {klips}")
    print(f"  rasio={a.ratio} gaya={st.key} ({st.label}) foto={a.photo}")
    for i, d in enumerate(klips, 1):
        mode = "FL2VA (awal+akhir)" if (i == 1 and len(a.photo) > 1) else "i2v (frame awal saja)"
        print(f"    klip {i}: {d}s  {mode}")
    if a.dry:
        print("(dry-run — tidak memanggil API, tidak memakai koin)")
        return 0

    work = ROOT / "work"
    work.mkdir(exist_ok=True)
    be = RunningHubBackend(api_key=os.getenv("RUNNINGHUB_API_KEY"),
                           base=os.getenv("RUNNINGHUB_BASE", "https://www.runninghub.ai"),
                           work_dir=str(work))

    frame = await be.upload(Path(a.photo[0]))
    last = await be.upload(Path(a.photo[1])) if len(a.photo) > 1 else None
    print("⬆️  frame di-upload:", frame)

    files: list[Path] = []
    total_koin = 0
    for i, d in enumerate(klips, 1):
        prompt = ps.h3_timeline(ps.STYLES.get(a.style) or ps.STYLES["promo"], d)
        print(f"\n── klip {i}/{len(klips)} ({d}s) mulai…")
        t0 = time.time()
        tid, url, koin = await render_clip(be, frame, prompt, a.ratio, d, last)
        total_koin += koin
        print(f"   ✅ {int(time.time()-t0)}s · {koin} koin · {tid}")
        dest = work / f"klip{i}.mp4"
        from bot import fetch_url
        await fetch_url(url, dest)
        files.append(dest)
        # frame terakhir klip ini → frame awal klip berikutnya
        if i < len(klips):
            last_png = work / f"frame{i}-akhir.png"
            ffmpeg(work, ["-ss", str(max(0.0, durasi_file(dest) - 0.15)), "-i", str(dest),
                          "-frames:v", "1", str(last_png)])
            frame, last = await be.upload(last_png), None     # klip berikut pakai mode i2v
            print(f"   ↳ frame akhir diekstrak & di-upload untuk klip {i+1}")

    # sambung semua klip
    daftar = work / "concat.txt"
    daftar.write_text("".join(f"file '{f.resolve()}'\n" for f in files))
    out = Path(a.out)
    ffmpeg(work, ["-f", "concat", "-safe", "0", "-i", str(daftar), "-c", "copy", str(out)])
    print(f"\n🎬 SELESAI: {out} ({out.stat().st_size:,} bytes · {durasi_file(out):.2f}s)")
    print(f"💰 total koin: {total_koin} ≈ Rp{total_koin*RUPIAH_PER_KOIN:,.0f}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))