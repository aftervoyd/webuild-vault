"""Katalog fitur + harga token (mengikuti/ melebihi pasar — acuan @KuzushiGenBot)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Feature:
    key: str
    label: str
    cost: float              # biaya token
    min_photos: int
    max_photos: int
    need_prompt: bool
    need_ratio: bool
    desc: str
    backend_workflow: str    # nama workflow di backend (ComfyUI/RunningHub)


FEATURES: dict[str, Feature] = {
    "allinone": Feature(
        key="allinone",
        label="🌌 Video All-in-One (30s)",
        cost=1.0,
        min_photos=1, max_photos=6,
        need_prompt=True, need_ratio=True,
        desc=("Video 30 detik dari 1–6 foto referensi.\n"
              "· Foto 1 = frame awal · Foto 2 = frame akhir (opsional)\n"
              "· Foto 3–6 = elemen tambahan (outfit/properti/scene)"),
        backend_workflow="krea_allinone_h3",
    ),
    "i2v": Feature(
        key="i2v",
        label="🎬 Image to Video",
        cost=0.5,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=True,
        desc="Foto → video pendek (5 detik). Cocok buat teaser & loop.",
        backend_workflow="krea_i2v_ltx",
    ),
    "faceswap": Feature(
        key="faceswap",
        label="🎭 Face Swap & Motion",
        cost=2.0,
        min_photos=2, max_photos=2,
        need_prompt=False, need_ratio=False,
        desc=("Foto wajah bersih + video gerakan sumber (.mp4) → wajah ditukar.\n"
              "Disarankan video 15 dtk, maks 30 dtk."),
        backend_workflow="krea_faceswap",
    ),
    "pose": Feature(
        key="pose",
        label="🕺 Pose Transfer & Style",
        cost=0.5,
        min_photos=2, max_photos=2,
        need_prompt=True, need_ratio=False,
        desc="Foto karakter + foto pose referensi → karakter mengikuti pose.",
        backend_workflow="krea_pose",
    ),
    "lipsync": Feature(
        key="lipsync",
        label="🎤 Video Lip Sync",
        cost=0.5,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=False,
        desc="Foto wajah + teks/audio → video berbicara/bernyanyi.",
        backend_workflow="krea_lipsync_h3",
    ),
    "editor": Feature(
        key="editor",
        label="🖌️ AI Image Editor",
        cost=0.3,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=False,
        desc="Edit foto dari prompt (ganti latar, gaya, pakaian).",
        backend_workflow="krea_imgedit",
    ),
}

RATIOS = {"9:16": "📱 9:16 (TikTok/Reels/Shorts)", "16:9": "🎬 16:9 (YouTube)", "1:1": "🔲 1:1 (Feed IG)"}


def get(key: str) -> Feature | None:
    return FEATURES.get(key)


def price_rp(feature: Feature, tokens_per_10k: int, harga_10k: int) -> int:
    """Konversi biaya token → rupiah."""
    return int(feature.cost / tokens_per_10k * harga_10k)