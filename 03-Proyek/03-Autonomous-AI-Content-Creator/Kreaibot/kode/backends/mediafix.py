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
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
MEDIA_EXT = VIDEO_EXT | IMAGE_EXT


def unwrap_media(path: Path | str) -> Path:
    """Beberapa AI App mengemas hasil jadi ZIP (mis. app LTX-2.3 "…zip").

    Deteksi header PK lalu ambil file media pertama di dalamnya.
    """
    p = Path(path)
    try:
        if not p.exists() or p.is_dir() or p.read_bytes()[:4] != b"PK\x03\x04":
            return p
    except Exception:                                        # noqa: BLE001
        return p
    import zipfile
    try:
        with zipfile.ZipFile(p) as z:
            names = sorted(n for n in z.namelist()
                           if Path(n).suffix.lower() in MEDIA_EXT and not n.startswith("__MACOSX"))
            if not names:
                return p
            target = names[0]
            out = p.with_name(f"{p.stem}__{Path(target).name}")
            with z.open(target) as src, open(out, "wb") as dst:
                dst.write(src.read())
        if out.exists() and out.stat().st_size > 0:
            return out
    except Exception:                                        # noqa: BLE001
        pass
    return p


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
    # KEPUTUSAN USER (9 Okt): "kalau ngerusak kualitas, pakai hasil ORIGINAL RunningHub saja."
    # minterpolate bikin FRAME SINTETIS → bisa memunculkan artefak. Jadi DEFAULT: JANGAN diinterpolasi;
    # hasil keluar apa adanya dari model RunningHub. Nyalakan hanya kalau memang diminta:
    #   KREAIBOT_SMOOTH_FPS=1
    if os.getenv("KREAIBOT_SMOOTH_FPS", "0").strip().lower() not in ("1", "true", "yes", "on"):
        return p
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