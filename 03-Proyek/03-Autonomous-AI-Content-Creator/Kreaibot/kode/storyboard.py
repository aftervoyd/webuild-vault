#!/usr/bin/env python3
"""Mode CERITA (multi-shot) — solusi untuk skenario panjang yang "gak jelas".

Masalah: model i2v hanya sanggup SATU aksi menerus per render. Cerita seperti
"lari membelakangi kamera, kamera ngejar, sesekali noleh, hampir jatuh, lanjut
lari sambil ketawa" kalau dipaksa jadi 1 render → meleleh (latar berubah, wajah
drift, tangan blob).

Solusi: pecah cerita jadi N klip pendek (1 aksi per klip), LALU frame terakhir
dari klip sebelumnya dipakai sebagai frame awal klip berikutnya (frame chaining)
supaya karakter + latar nyambung, baru dijahit jadi 1 video.
"""
from __future__ import annotations

import asyncio
import logging
import os
import subprocess
import urllib.request
from pathlib import Path
from typing import Awaitable, Callable, List, Optional, Sequence

log = logging.getLogger("krea.story")

SHOT_SECONDS = 5          # 1 klip = 5 detik (paling stabil & paling murah)


def _ffmpeg() -> str:
    return os.getenv("FFMPEG_BIN", "") or os.getenv("KREAIBOT_FFMPEG", "") or "ffmpeg"


def last_frame(clip: Path, out: Path) -> Path:
    """Ambil frame TERAKHIR dari klip → dipakai jadi gambar awal klip berikutnya."""
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([_ffmpeg(), "-v", "error", "-y", "-sseof", "-0.2", "-i", str(clip),
                    "-frames:v", "1", "-q:v", "2", str(out)],
                   check=True, capture_output=True)
    return out


def stitch(clips: Sequence[Path], out: Path) -> Path:
    """Jahit klip-klip jadi satu video (re-encode supaya aman walau ukuran beda)."""
    out.parent.mkdir(parents=True, exist_ok=True)
    lst = out.parent / "concat_cerita.txt"
    lst.write_text("\n".join(f"file '{Path(c).resolve()}'" for c in clips), encoding="utf-8")
    subprocess.run([_ffmpeg(), "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", str(out)],
                   check=True, capture_output=True)
    return out


async def _download(url: str, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    await asyncio.to_thread(urllib.request.urlretrieve, url, dest)
    return dest


async def render_story(backend, *, photo: Path, shots: Sequence[str], ratio: str,
                       work: Path, dur_each: int = SHOT_SECONDS,
                       job_id: int = 0, poll_interval: float = 5.0,
                       timeout: int = 1800,
                       on_progress: Optional[Callable[[int, int, str], Awaitable[None]]] = None
                       ) -> Path:
    """Render `shots` klip berurutan dengan frame chaining, lalu jahit jadi 1 video.

    `backend` = instance RunningHubBackend (punya submit()/poll()).
    """
    from backends import GenRequest
    from backends.mediafix import unwrap_media

    clips: List[Path] = []
    src = Path(photo)
    total = len(shots)
    for i, prompt in enumerate(shots, start=1):
        raw_out = work / f"shot{i}.mp4"
        req = GenRequest(job_id=(job_id * 100 + i), feature_key="i2v", workflow="krea_i2v_ltx",
                         photos=[src], prompt=prompt, ratio=ratio,
                         duration=dur_each, out_path=raw_out)
        task_id = await backend.submit(req)
        t0 = asyncio.get_event_loop().time()
        while True:
            if asyncio.get_event_loop().time() - t0 > timeout:
                raise TimeoutError(f"shot {i} melebihi batas waktu")
            st = await backend.poll(task_id)
            if st.state == "failed":
                raise RuntimeError(f"shot {i} gagal: {st.error}")
            if st.state == "done":
                rp = str(st.result_path or "")
                if rp.startswith("http"):
                    await _download(rp, raw_out)
                elif rp and Path(rp).exists():
                    raw_out = Path(rp)
                break
            if on_progress:
                await on_progress(i, total, st.message or "diproses...")
            await asyncio.sleep(poll_interval)
        clip = await asyncio.to_thread(unwrap_media, raw_out)
        clips.append(Path(clip))
        log.info("shot %s/%s selesai: %s", i, total, clip)
        if i < total:                      # frame akhir → gambar awal shot berikutnya
            nxt = work / f"last{i}.jpg"
            try:
                await asyncio.to_thread(last_frame, Path(clip), nxt)
                if nxt.exists() and nxt.stat().st_size > 1000:
                    src = nxt
            except Exception as e:         # noqa: BLE001
                log.warning("gagal ambil frame terakhir shot %s: %s", i, e)
    return await asyncio.to_thread(stitch, clips, work / "hasil_cerita.mp4")


def plan_shots(total_seconds: int) -> tuple[int, int]:
    """Total durasi → (jumlah shot, detik per shot). 15s→3×5, 30s→6×5."""
    total = max(SHOT_SECONDS, int(total_seconds or 15))
    n = max(1, round(total / SHOT_SECONDS))
    return n, SHOT_SECONDS