#!/usr/bin/env python3
"""Uji jalur ZOOM-VARIANT backend RunningHub TANPA membuat task (0 koin).

Yang diverifikasi:
  1. `_zoom_variant()` menghasilkan gambar dengan ukuran sesuai rasio (dan beda dari aslinya)
  2. upload gambar zoom ke RunningHub berhasil (upload gratis)
  3. `_bind()` memetakan binding i2v ke file yang benar:
       node 6 (frame PERTAMA) ← foto asli
       node 4 (frame TERAKHIR) ← foto hasil zoom
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv                                  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

from backends import GenRequest                                  # noqa: E402
from backends.runninghub import RATIO_SIZES, RunningHubBackend    # noqa: E402

FOTO = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/job_3/ref1.bin"


def main() -> int:
    be = RunningHubBackend(api_key=os.getenv("RUNNINGHUB_API_KEY", ""),
                           base=os.getenv("RUNNINGHUB_BASE", ""),
                           work_dir=str(ROOT / "work" / "tests"))
    f = {"ok": True}

    # 1) zoom variant
    zv = be._zoom_variant(FOTO, "9:16", "zoomcheck")
    if not zv or not zv.exists():
        print("❌ _zoom_variant gagal")
        return 1
    from PIL import Image, ImageChops
    a = Image.open(FOTO).convert("RGB")
    z = Image.open(zv).convert("RGB")
    w, h = RATIO_SIZES["9:16"]
    beda = ImageChops.difference(z.resize(a.size), a).getbbox() is not None
    ok_size = (z.width, z.height) == (w, h)
    print(f"  {'✅' if ok_size else '❌'} ukuran zoom {z.size} == {w}x{h} (rasio 9:16)")
    print(f"  {'✅' if beda else '❌'} gambar zoom beda dari foto asli ({zv.name}, {zv.stat().st_size//1024} KB)")
    f["ok"] &= ok_size and beda

    # 2) upload (gratis)
    up = asyncio.run(be.upload(zv))
    print(f"  {'✅' if up else '❌'} upload zoom → {up[:46]}…")
    f["ok"] &= bool(up)

    # 3) resolusi binding i2v
    req = GenRequest(job_id=0, feature_key="i2v", workflow="", photos=[str(FOTO)],
                     video_in=None, prompt="uji", ratio="9:16", duration=5,
                     out_path=ROOT / "work" / "tests" / "x.mp4")
    bindings = be._node_bindings("i2v")
    out = be._bind(bindings, req, ["FOTO_ASLI.bin"], {"@photo1_zoom": up})
    node = {b["nodeId"]: (b["fieldName"], b["fieldValue"]) for b in out}
    first_ok = node.get("6", ("", ""))[1] == "FOTO_ASLI.bin"
    last_ok = node.get("4", ("", ""))[1] == up
    print(f"  {'✅' if first_ok else '❌'} node 6 (frame PERTAMA) ← foto asli")
    print(f"  {'✅' if last_ok else '❌'} node 4 (frame TERAKHIR) ← foto zoom")
    print(f"  📋 binding i2v: {json.dumps(out)[:220]}…")
    f["ok"] &= first_ok and last_ok

    print(f"\n  hasil: {'✅ jalur zoom siap (tanpa task / 0 koin)' if f['ok'] else '❌ ada masalah'}")
    return 0 if f["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())