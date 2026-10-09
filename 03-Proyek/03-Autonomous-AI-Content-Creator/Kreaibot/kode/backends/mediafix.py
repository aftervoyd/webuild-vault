"""Perbaikan hasil video: fps rendah (16 fps) → halus (30 fps).

Model jalur koin (Wan2.2 dll) keluar di **16 fps**; di layar 60 Hz hasilnya terlihat
patah-patah / seperti gerak lambat. Interpolasi frame menaikkan ke 30 fps TANPA
mengubah durasi atau kecepatan gerak — cuma lebih halus.

Saklar: `KREAIBOT_FPS` (default 30; isi 0 untuk mematikan).
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

from .mock import ffmpeg_bin

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm"}


def ffprobe_bin() -> str:
    fb = ffmpeg_bin()
    cand = (os.environ.get("FFPROBE_BIN"),
            str(Path(fb).with_name("ffprobe")) if fb else None,
            "/usr/local/bin/ffprobe", "/usr/bin/ffprobe")
    for c in cand:
        if c and Path(c).exists():
            return c
    return "ffprobe"


def probe_fps(path: Path) -> float:
    try:
        out = subprocess.run([ffprobe_bin(), "-v", "error", "-select_streams", "v:0",
                              "-show_entries", "stream=r_frame_rate",
                              "-of", "default=nw=1:nk=1", str(path)],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if "/" in out:
            num, den = out.split("/")
            return float(num) / float(den or 1)
        return float(out or 0)
    except Exception:                                        # noqa: BLE001
        return 0.0


def target_fps() -> float:
    try:
        return float(os.getenv("KREAIBOT_FPS", "30") or 0)
    except ValueError:
        return 30.0


def smooth_fps(path: Path | str, target: float | None = None, timeout: int = 1200) -> Path:
    """Ubah jadi versi `target` fps (interpolasi gerak). Balikin path asli kalau tak perlu/gagal."""
    p = Path(path)
    tgt = target or target_fps()
    if not tgt or p.suffix.lower() not in VIDEO_EXT or not p.exists():
        return p
    src = probe_fps(p)
    if not src or src >= tgt - 0.5:
        return p
    out = p.with_name(f"{p.stem}_{int(tgt)}fps{p.suffix}")
    cmd = [ffmpeg_bin(), "-v", "error", "-y", "-i", str(p),
           "-filter:v",
           f"minterpolate=fps={tgt:g}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
           "-c:a", "copy", "-movflags", "+faststart", str(out)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return p
    if r.returncode == 0 and out.exists() and out.stat().st_size > 0:
        return out
    return p