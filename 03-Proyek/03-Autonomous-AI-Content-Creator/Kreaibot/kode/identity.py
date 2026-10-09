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

# Prompt bawaan app (sudah teruji): ganti kepala+wajah gambar 1 dengan gambar 2, jaga komposisi/cahaya.
IDLOCK_PROMPT = ("参照图像1和图像2，把图像1人物的头和脸换成图像2人物的头和脸，"
                 "保持图像1的构图、场景和光线不变，融合真实自然，不能有PS痕迹")


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

        # 9 Okt malam: app "极速换脸" TERBUKTI no-op (wajah tidak berubah sama sekali). Diganti app
        # "换头换脸提高相似度优化版 (Flux2-Klein, 4K)" = 93% mirip (uji A/B/C berlabel).
        # Urutan foto app ini: node 6 = GAMBAR UTAMA (hasil render), node 26 = FOTO REFERENSI WAJAH.
        req = GenRequest(job_id=job_id, feature_key="idlock", workflow="",
                         photos=[result, face_photo], prompt=IDLOCK_PROMPT, ratio="", duration=0,
                         out_path=out_path)
        # CATATAN 9 Okt: dulu di sini dipanggil backend.generate() — metode itu TIDAK ADA di
        # RunningHubBackend, jadi kunci identitas GAGAL SENYAP (tertangkap except, cuma warning),
        # dan user selalu dapat hasil render yang wajahnya karangan model. API yang benar: submit/poll.
        task = await backend.submit(req)
        import asyncio
        import time as _t
        t0 = _t.time()
        while True:
            st = await backend.poll(task)
            if st.state == "failed":
                log.error("identity-lock GAGAL (wajah asli tidak terpasang): %s", st.error)
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
                log.error("identity-lock timeout (>600s)")
                return None
            await asyncio.sleep(4)
    except Exception as e:                                     # noqa: BLE001
        log.error("identity-lock error: %s", e)
        return None
    finally:
        if costs is not None:
            costs.append(("faceswap-lock", 10))