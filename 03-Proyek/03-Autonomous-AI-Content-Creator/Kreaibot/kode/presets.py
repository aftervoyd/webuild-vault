#!/usr/bin/env python3
"""Preset 1-TAP — user cukup tap tombol setelah kirim foto, TANPA ngetik prompt.

Filosofi (lihat RANCANGAN-UX-PRESET-9OKT.md di vault):
- Prompt tidak wajib diketik: preset = prompt siap pakai yang sudah patuh aturan
  "1 aksi per klip" (akar masalah video meleleh).
- Kerumitan (multi-scene + frame chaining) disembunyikan DI DALAM preset:
  preset `larikejar` pakai mesin `story`, tapi user tetap cuma 1 tap.
- Harga selalu tampil di tombol (contek kebiasaan Kuzushi).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

IDENTITY = ("The person's face, hair, glasses and outfit stay exactly as in the reference photo, "
            "photoreal skin texture, no morphing, no identity drift.")


@dataclass(frozen=True)
class Preset:
    key: str
    emoji: str
    label: str
    feature: str = ""            # fitur katalog: i2v | story | editor | "" (biarkan apa adanya)
    duration: int = 0            # durasi default (0 = ikut fitur)
    prompt: str = ""             # prompt inti (English) — wajib 1 aksi
    story: str = ""              # brief cerita (dipakai mesin story; boleh bahasa Indonesia)
    hint: str = ""
    beta: bool = False           # True = belum terbukti → JANGAN tampil di grid
    tags: tuple = field(default_factory=tuple)

    def text(self) -> str:
        """Teks yang dikirim sebagai prompt ke job (prompt tunggal atau brief cerita)."""
        return self.story or self.prompt


# --- preset VIDEO (grid utama setelah user kirim foto) -----------------------
VIDEO_PRESETS: List[Preset] = [
    Preset("ketawa", "😄", "Tertawa & melambai",
           feature="i2v", duration=5,
           prompt="The person from the photo laughs warmly and waves at the camera with a bright smile. "
                  "Gentle slow push-in camera. " + IDENTITY),
    Preset("menari", "💃", "Menari",
           feature="i2v", duration=10,
           prompt="The person from the photo dances gracefully with smooth, flowing body movement and a "
                  "joyful expression. Static camera, soft cinematic lighting. " + IDENTITY),
    Preset("vlog", "🚶", "Vlog selfie jalan",
           feature="i2v", duration=10,
           prompt="The person from the photo walks slowly toward the camera like a casual selfie vlog, "
                  "smiling and talking to the lens. Gentle handheld-style camera. " + IDENTITY),
    Preset("kaget", "😮", "Kaget / terkejut",
           feature="i2v", duration=5,
           prompt="The person from the photo suddenly looks surprised, eyes widening and head pulling "
                  "back slightly, then relaxing into a small smile. Static camera. " + IDENTITY),
    Preset("pose", "💪", "Pose model / fashion",
           feature="i2v", duration=5,
           prompt="The person from the photo holds an elegant fashion pose, slowly turning their head and "
                  "shifting weight with quiet confidence. Slow gentle orbit camera. " + IDENTITY),
    Preset("angin", "🌬️", "Angin & rambut natural",
           feature="i2v", duration=10,
           prompt="The person from the photo stands calmly while a light breeze moves their hair and "
                  "clothes softly, gentle blinking and subtle breathing. Static camera. " + IDENTITY),
    Preset("larikejar", "🏃", "Lari dikejar kamera",
           feature="story", duration=15, beta=True,
           story="wanita/pria di foto berlari membelakangi kamera dan kamera mengejar pelan, "
                 "sesekali menoleh ke belakang, hampir tersandung tapi tetap berlari sambil tertawa"),
    Preset("cerita", "📖", "Cerita panjang (30s)",
           feature="story", duration=30, beta=True,
           story=""),
]

# --- preset EDITOR FOTO (prompt siap pakai) ----------------------------------
EDITOR_PRESETS: List[Preset] = [
    Preset("ed_baju", "👕", "Ganti baju/outfit",
           feature="editor", prompt="change the person's outfit into a stylish modern outfit, "
                                    "keep the same face, pose and background"),
    Preset("ed_latar", "🏝️", "Ganti latar belakang",
           feature="editor", prompt="replace the background with a beautiful tropical beach at golden "
                                    "hour, keep the person exactly the same"),
    Preset("ed_cyber", "🌆", "Gaya cyberpunk",
           feature="editor", prompt="make it cyberpunk style with neon lighting and a futuristic city "
                                    "background, keep the face identical, 8k detail"),
    Preset("ed_hapus", "🧽", "Hapus objek",
           feature="editor", prompt="remove unwanted objects from the photo and cleanly fill the area, "
                                    "keep the person unchanged"),
    Preset("ed_studio", "📸", "Foto studio profesional",
           feature="editor", prompt="turn this into a professional studio portrait with softbox "
                                    "lighting and a clean gray backdrop, keep the face identical"),
]

SPECIALS: List[Preset] = [
    Preset("sendiri", "✍️", "Tulis sendiri", hint="Ketik prompt bebas kamu sendiri."),
    Preset("kejutan", "🎲", "Kejutan", hint="Bot pilih situasi acak buat kamu."),
]

ALL: Dict[str, Preset] = {p.key: p for p in VIDEO_PRESETS + EDITOR_PRESETS + SPECIALS}


def resolve(key: str, twist: int = 0) -> Optional[Preset]:
    """Ambil preset; `kejutan` → pilih acak dari preset video (deterministik dari twist)."""
    if key == "kejutan":
        pool = VIDEO_PRESETS or []
        return pool[twist % len(pool)] if pool else None
    return ALL.get(key)


def for_feature(feature_key: str) -> List[Preset]:
    """Preset yang relevan untuk sebuah fitur (untuk grid setelah foto)."""
    if feature_key == "editor":
        return EDITOR_PRESETS + [ALL["sendiri"]]
    if feature_key in ("i2v", "long", "story"):
        return ([p for p in VIDEO_PRESETS if not p.beta] + [ALL["sendiri"], ALL["kejutan"]])
    return []


def kb_rows(feature_key: str, cost_for) -> list:
    """Baris tombol siap pakai untuk aiogram (2 kolom) — lengkap dengan HARGA.

    `cost_for(feature, durasi)` = fungsi catalog.cost_for supaya harga pasti sinkron.
    """
    from aiogram.types import InlineKeyboardButton

    rows: list = []
    pair: list = []
    for p in for_feature(feature_key):
        if p.key == "sendiri":
            pair.append(InlineKeyboardButton(text=f"{p.emoji} {p.label}", callback_data="p:sendiri"))
            continue
        if p.key == "kejutan":
            pair.append(InlineKeyboardButton(text=f"{p.emoji} {p.label}", callback_data="p:kejutan"))
            continue
        feat = p.feature or feature_key
        dur = p.duration
        harga = ""
        try:
            harga = f" · {cost_for(feat, dur):g}T"
        except Exception:                      # noqa: BLE001
            harga = ""
        pair.append(InlineKeyboardButton(text=f"{p.emoji} {p.label}{harga}",
                                         callback_data=f"p:{p.key}"))
        if len(pair) == 2:
            rows.append(pair)
            pair = []
    if pair:
        rows.append(pair)
    return rows