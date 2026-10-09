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
    kind: str = "generic"    # generic | ugc
    need_style: bool = False # wajib pilih gaya (UGC)
    char_first: bool = False # foto ke-1 = character sheet
    product_slot: bool = False  # ada slot foto produk
    duration: int = 5         # durasi default render (detik) — batas workflow 4..15
    durations: tuple[int, ...] = (5,)   # pilihan durasi yang dijual
    hint: str = ""            # petunjuk langkah saat minta foto


FEATURES: dict[str, Feature] = {
    "ugc": Feature(
        key="ugc",
        label="🛍️ UGC Video Iklan",
        cost=2.5,
        min_photos=2, max_photos=2,
        need_prompt=True, need_ratio=True,
        duration=15,
        desc=("Video iklan gaya kreator (UGC) untuk jualan produk.\n"
              "· Character sheet (foto wajah/tubuh kamu) + foto produk\n"
              "· Tulis brief: nama produk, harga, keunggulan, atau maunya video seperti apa\n"
              "· Pilih gaya (Review / Unboxing / Problem-Solution / Testimoni / Promo / Sinematik)\n"
              "· Prompt video dirakit otomatis jadi lebih rapi & natural"),
        backend_workflow="krea_ugc_h3",
        kind="ugc", need_style=True, char_first=True, product_slot=True,
        durations=(15,),
        hint="Kirim foto karakter, lalu foto produk, terus langsung ketik brief-nya.",
    ),
    "allinone": Feature(
        key="allinone",
        label="🌌 Video All-in-One",
        cost=2.5,
        min_photos=1, max_photos=6,
        need_prompt=True, need_ratio=True,
        duration=15, durations=(5, 15),
        desc=("Video sinematik dari 1–6 foto referensi.\n"
              "· Foto 1 = frame awal · Foto 2 = frame akhir\n"
              "· Foto 3–6 = elemen tambahan (outfit/properti/scene)\n"
              "· 5 detik = 1 Token · 15 detik = 2,5 Token"),
        backend_workflow="krea_allinone_h3",
        hint="Kirim 1–6 foto (foto 1 = frame awal, foto 2 = frame akhir).",
    ),
    "i2v": Feature(
        key="i2v",
        label="🎬 Image to Video",
        cost=0.5,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=True,
        duration=5, durations=(5, 10, 15),
        desc=("Foto → video pendek.\n"
              "· 5 detik = 0,5 Token · 10 detik = 1 Token · 15 detik = 1,5 Token\n"
              "· Ada suara ambient otomatis, gerak halus 24 fps\n"
              "· Cocok buat teaser, loop, dan bikin cepat"),
        backend_workflow="krea_i2v_ltx",
        hint="Kirim 1 foto (wajah, produk, atau scene apa saja).",
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
    "long": Feature(
        key="long",
        label="🎥 Video 30 Detik",
        cost=1.0,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=True,
        duration=30, durations=(30,),
        desc=("Satu foto → video 30 detik sekali jalan (bukan sambung-sambungan).\n"
              "· 1 Token (Rp1.000) — sama dengan pasaran\n"
              "· Ada suara ambient, 24 fps, 768×1280\n"
              "· Cocok buat cerita/iklan panjang"),
        backend_workflow="krea_i2v_ltx",
        hint="Kirim 1 foto + ketik mau videonya seperti apa (boleh cerita panjang).",
    ),
    "editor": Feature(
        key="editor",
        label="🖌️ AI Image Editor",
        cost=0.3,
        min_photos=1, max_photos=1,
        need_prompt=True, need_ratio=False,
        desc=("Edit foto dari instruksi teks (ganti latar, gaya, pakaian).\n"
              "· Contoh: \"make it cyberpunk style, neon lighting, 8k\"\n"
              "· Contoh: \"anime style, detailed background\"\n"
              "· Hasil = gambar (bukan video)"),
        backend_workflow="krea_imgedit",
        hint="Kirim 1 foto yang mau diedit — habis itu langsung ketik instruksi edit-nya.",
    ),
}

RATIOS = {"9:16": "📱 9:16 (TikTok/Reels/Shorts)", "16:9": "🎬 16:9 (YouTube)", "1:1": "🔲 1:1 (Feed IG)"}

# Harga token per (fitur, durasi) — acuan pasar @KuzushiGenBot, margin kita 40–70%.
# Ubah di sini kalau mau naik/turunin harga; kode lain ngikut otomatis.
DURATION_COST: dict[tuple[str, int], float] = {
    # i2v 15s AKTIF sejak 9 Okt 11:20 (app LTX-2.3: 89 koin / 465 s, terbukti).
    # Catatan lama "15s dimatikan" itu untuk app Wan2.2 yang memang gagal.
    ("i2v", 5): 0.5, ("i2v", 10): 1.0, ("i2v", 15): 1.5,
    ("long", 30): 1.0,          # 30 s sekali render: app LTX-2.3, terbukti 9 Okt 11:50 (135 koin)
    ("allinone", 5): 1.0, ("allinone", 15): 2.5,
    ("ugc", 15): 2.5,
}


def cost_for(key: str, duration: int) -> float:
    """Biaya token untuk fitur + durasi tertentu (fallback: harga default fitur)."""
    if (key, duration) in DURATION_COST:
        return DURATION_COST[(key, duration)]
    f = FEATURES.get(key)
    return f.cost if f else 0.0


# Fitur yang SUDAH tersambung ke mesin render nyata (RunningHub workflow FL2VA).
# Fitur lain tetap ada di katalog tapi belum tampil ke user sampai workflow-nya siap.
SIAP_JUAL: tuple[str, ...] = ("ugc", "allinone", "i2v", "long", "editor")


def enabled_features() -> list[Feature]:
    return [f for f in FEATURES.values() if f.key in SIAP_JUAL]


def get(key: str) -> Feature | None:
    return FEATURES.get(key)


def price_rp(feature: Feature, tokens_per_10k: int, harga_10k: int) -> int:
    """Konversi biaya token → rupiah."""
    return int(feature.cost / tokens_per_10k * harga_10k)