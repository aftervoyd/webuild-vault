"""Kunci identitas: face swap BALIK ke hasil render.

MASALAH NYATA (9 Okt 16:4x): user render AI Image Editor pakai karakter tersimpan "Arunika".
Model editor (All-in-One Image V2 / RhinatImageNG31Flash img2img) **menggambar ulang wajah** →
user: "tetep gak mirip sama sekali". Model img2img tidak bisa dijaga lewat prompt saja.

SOLUSI: setelah render, wajah asli karakter di-swap kembali ke hasil render memakai app
Face Swap (极速换脸) yang sama dengan fitur Face Swap Karakter — hasil akhirnya memakai
**pixel wajah asli** (bukan karangan model).

Dipakai otomatis kalau foto referensi = karakter/produk tersimpan user (niatnya jelas: identitas sama).
"""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("kreaibot.identity")


def _download(url: str, dest: Path) -> Path:
    """Unduh hasil dari cloud RunningHub (hindari impor bot → tidak ada impor melingkar)."""
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=240) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    return Path(dest)


async def lock_identity(backend, result: Path, face_photo: Path, job_id: int,
                        out_path: Path, costs: list | None = None) -> Path | None:
    """Face swap wajah `face_photo` ke gambar `result`. None kalau gagal (hasil asli tetap dipakai)."""
    try:
        from backends import GenRequest

        req = GenRequest(job_id=job_id, feature_key="faceswap", workflow="",
                         photos=[face_photo, result], prompt="", ratio="", duration=0,
                         out_path=out_path)
        task = await backend.generate(req)
        import asyncio
        import time as _t
        t0 = _t.time()
        while True:
            st = await backend.poll(task)
            if st.state == "failed":
                log.warning("identity-lock gagal: %s", st.error)
                return None
            if st.state == "done":
                rp = str(st.result_path or "")
                if rp.startswith("http"):
                    from backends.mediafix import fix_ext, unwrap_media
                    p = await asyncio.to_thread(_download, rp, out_path)
                    p = await asyncio.to_thread(unwrap_media, p)
                    p = await asyncio.to_thread(fix_ext, p)
                    return Path(p)
                if rp and Path(rp).exists():
                    return Path(rp)
                return out_path if out_path.exists() else None
            if _t.time() - t0 > 600:
                log.warning("identity-lock timeout")
                return None
            await asyncio.sleep(4)
    except Exception as e:                                     # noqa: BLE001
        log.warning("identity-lock dilewati: %s", e)
        return None
    finally:
        if costs is not None:
            costs.append(("faceswap-lock", 10))