"""Character Creator — bikin MASTER CHARACTER SHEET otomatis dari 1 foto wajah.

Alur (nol-prompt, semua pencet tombol):
  1. user kirim 1 foto wajah (referensi identitas),
  2. pilih: gender → penampilan/ras → vibe wajah → bentuk dada (1-3) → langsing (1-3) → pinggul (1-3)
     → outfit,
  3. mesin menggambar: 1 panel WAJAH close-up + 3 panel BADAN (depan/samping/belakang) yang identitasnya
     dijaga dari foto user,
  4. disusun jadi sheet machine-readable (tata letak `sheetbuild.py`) → disimpan jadi karakter user.

Semua render tetap mesin RunningHub original (env `RUNNINGHUB_APP_CHARGEN`).
"""
from __future__ import annotations

import asyncio
import logging
import urllib.request
from pathlib import Path

import sheetbuild

log = logging.getLogger("kreaibot.chargen")

DISCLAIMER = "Setiap panel yang digambar AI adalah orang DEWASA (18+)."

# HARGA fitur Character Creator (token). Diukur NYATA 9 Okt (selisih koin sebelum/sesudah):
#   4 render (1 wajah + 3 badan) ≈ 200–220 koin ≈ Rp700–760 (harga koin RunningHub ≈ Rp3,4)
#   dijual 3 Token = Rp3.000  →  margin ± 75%
# Kalau biaya mesin naik/turun, cuma angka ini yang diubah.
COST = 3.0

# ---------------------------------------------------------------- pilihan user (label UI + frasa prompt)
GENDER: dict[str, tuple[str, str]] = {
    "wanita": ("👩 Wanita", "woman"),
    "pria": ("👨 Pria", "man"),
}

RACE: dict[str, tuple[str, str]] = {
    "asia_timur": ("🌸 Asia Timur", "East Asian (Chinese/Korean) facial features"),
    "asia_tenggara": ("🌺 Asia Tenggara", "Southeast Asian (Indonesian) facial features"),
    "asia_selatan": ("🪷 Asia Selatan", "South Asian (Indian) facial features"),
    "eropa": ("🌹 Eropa", "European Caucasian facial features"),
    "timur_tengah": ("🌻 Timur Tengah", "Middle Eastern facial features"),
    "latin": ("💃 Latin", "Latin American facial features"),
    "afrika": ("🌍 Afrika", "Black African facial features"),
    "campuran": ("🌈 Blasteran", "mixed-race (Eurasian) facial features"),
}

VIBE: dict[str, tuple[str, str]] = {
    "imut": ("🥰 Imut", "cute, youthful, soft rounded features, sweet friendly look"),
    "manis": ("🍬 Manis", "sweet, warm and gentle features, kind natural smile"),
    "elegan": ("💼 Elegan", "elegant, mature, refined and confident features"),
    "tegas": ("😎 Tegas", "bold, sharp and strongly defined features, intense gaze"),
    "sporty": ("🏃 Sporty", "sporty, fresh, healthy glowing skin, energetic look"),
    "misterius": ("🌙 Misterius", "mysterious and sultry look, subtle smoky eyes"),
    "natural": ("🌿 Natural", "natural and plain, minimal makeup, girl/boy-next-door look"),
}

BUST: dict[str, tuple[str, str]] = {
    "1": ("1 — Kecil", "small, flat chest"),
    "2": ("2 — Sedang", "medium, average bust"),
    "3": ("3 — Penuh", "full, large bust with visible cleavage"),
}
SLIM: dict[str, tuple[str, str]] = {
    "1": ("1 — Langsing", "slim and slender figure with a thin waist"),
    "2": ("2 — Sedang", "average, balanced body shape"),
    "3": ("3 — Berisi", "curvier, fuller body with soft curves"),
}
HIPS: dict[str, tuple[str, str]] = {
    "1": ("1 — Sempit", "narrow hips and slim legs"),
    "2": ("2 — Sedang", "average hips and normal leg proportions"),
    "3": ("3 — Lebar", "wide hips with fuller thighs and legs"),
}

OUTFIT: dict[str, tuple[str, str]] = {
    "netral": ("⚪ Netral", "simple neutral fitted top and straight pants"),
    "kasual": ("👕 Kasual", "casual t-shirt, jeans and sneakers"),
    "dress": ("👗 Dress", "elegant fitted knee-length dress"),
    "formal": ("🧥 Formal", "formal office shirt and blazer"),
    "sporty": ("🩳 Sporty", "sporty athletic top and leggings"),
    "seksi": ("🖤 Seksi", "sexy fitted outfit with a low neckline"),
    "tradisional": ("🧣 Tradisional", "traditional Indonesian kebaya"),
}

LABELS = {"gender": GENDER, "race": RACE, "vibe": VIBE, "bust": BUST, "slim": SLIM,
          "hips": HIPS, "outfit": OUTFIT}


def label(kind: str, key: str) -> str:
    row = LABELS.get(kind, {}).get(key)
    return row[0] if row else key


def _ascii(text: str) -> str:
    """Buang karakter non-ASCII (emoji) — font sheet tidak punya glyph-nya → jadi kotak tofu di judul."""
    out = text.replace("·", "-").replace("—", "-")
    out = "".join(ch for ch in out if ord(ch) < 128)
    while "  " in out:
        out = out.replace("  ", " ")
    return out.strip(" -")


def _word(kind: str, key: str, default: str = "") -> str:
    row = LABELS.get(kind, {}).get(key)
    return row[1] if row else default


# ---------------------------------------------------------------- prompt
def face_prompt(opts: dict) -> str:
    g = _word("gender", opts.get("gender", "wanita"), "woman")
    r = _word("race", opts.get("race", "asia_tenggara"), "Southeast Asian facial features")
    v = _word("vibe", opts.get("vibe", "natural"), "natural look")
    return (f"Studio portrait photograph of the SAME person as the reference photo — keep the facial "
            f"identity, face shape and features recognizable and consistent. She/he is a {g} with {r}, "
            f"{v}. Adult (18+). Head-and-shoulders close-up, facing the camera and looking straight at "
            f"the lens, calm neutral expression, plain light gray studio background, soft even studio "
            f"lighting, photorealistic, sharp focus, no text, no watermark")


# Sepatu ikut outfit supaya konsisten di semua panel (temuan uji 9 Okt: sepatu beda-beda antar panel).
SHOES: dict[str, str] = {
    "netral": "black flat shoes", "kasual": "white sneakers", "dress": "black high heels",
    "formal": "black leather shoes", "sporty": "white running shoes",
    "seksi": "black high heels", "tradisional": "black flat sandals",
}


def body_prompt(opts: dict, view: str) -> str:
    g = _word("gender", opts.get("gender", "wanita"), "woman")
    r = _word("race", opts.get("race", "asia_tenggara"), "Southeast Asian facial features")
    b = _word("bust", opts.get("bust", "2"), "medium, average bust")
    s = _word("slim", opts.get("slim", "2"), "average, balanced body shape")
    h = _word("hips", opts.get("hips", "2"), "average hips and normal leg proportions")
    o = _word("outfit", opts.get("outfit", "netral"), "simple neutral fitted top and straight pants")
    sh = SHOES.get(opts.get("outfit", "netral"), "black flat shoes")
    pose = {"front": "Standing straight facing the camera",
            "side": "Standing straight in full side profile facing right",
            "back": "Standing straight with her/his back turned to the camera"}.get(view, "Standing straight")
    return (f"Full body photograph of the SAME person as the reference photo — keep the face, hair, "
            f"glasses and identity EXACTLY the same as the reference. A {g} with {r}. Adult (18+). "
            f"Body: {b}, {s}, {h}. Wearing EXACTLY this outfit and nothing else: {o}, with {sh}. "
            f"Same outfit and same shoes as the reference image — do not change the clothes. "
            f"{pose}, full body visible from head to toe including shoes, arms relaxed at the sides, "
            f"plain light gray studio background, soft even studio lighting, photorealistic, "
            f"sharp focus, no text, no watermark")


# ---------------------------------------------------------------- backend helper
def _download(url: str, dest: Path) -> Path:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=240) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    return dest


async def _gen(backend, feature: str, photos: list[Path], prompt: str, out_path: Path,
               timeout: int = 900) -> Path:
    """Render 1 gambar lewat backend RunningHub (submit → poll → unduh → rapikan ekstensi)."""
    from backends import GenRequest
    from backends.mediafix import fix_ext, unwrap_media
    out_path = Path(out_path)
    req = GenRequest(job_id=0, feature_key=feature, workflow="", photos=photos, prompt=prompt,
                     ratio="", duration=0, out_path=out_path)
    task = await backend.submit(req)
    t = 0
    while True:
        st = await backend.poll(task)
        if st.state == "failed":
            raise RuntimeError(f"render gagal: {st.error}")
        if st.state == "done":
            rp = str(st.result_path or "")
            if rp.startswith("http"):
                p = await asyncio.to_thread(_download, rp, out_path)
                p = await asyncio.to_thread(unwrap_media, p)
                p = await asyncio.to_thread(fix_ext, p)
                return Path(p)
            if rp and Path(rp).exists():
                return Path(rp)
            if out_path.exists():
                return out_path
            raise RuntimeError("render selesai tapi berkas tidak ketemu")
        await asyncio.sleep(5)
        t += 5
        if t > timeout:
            raise RuntimeError("render timeout")


# ---------------------------------------------------------------- alur utama
async def run(backend, face_photo: Path, opts: dict, out_dir: Path, on_step=None) -> dict:
    """Bikin sheet master. Balikin {"sheet": Path, "panels": [(label, Path)]}.

    `on_step(teks)` dipanggil tiap tahap (buat update pesan progress di bot).
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    name = (opts.get("name") or "Karakter").strip()

    async def step(msg: str) -> None:
        log.info("chargen: %s", msg)
        if on_step:
            try:
                await on_step(msg)
            except Exception as e:                           # noqa: BLE001
                log.warning("on_step gagal: %s", e)

    panels: list[tuple[str, Path]] = []
    await step("🎨 Menggambar wajah master…")
    face_out = out_dir / "cc_face.png"
    face_out = await _gen(backend, "chargen", [Path(face_photo)], face_prompt(opts), face_out)
    panels.append(("FACE CLOSE UP", face_out))

    # PENTING: panel depan digambar dari WAJAH, lalu samping & belakang digambar dari PANEL DEPAN.
    # Temuan uji 9 Okt: kalau semua digambar dari wajah, outfit/sepatu beda-beda antar panel.
    # Rantai begini bikin baju, sepatu, rambut & proporsi ikut konsisten.
    await step("🧍 Menggambar badan (depan)…")
    front_out = out_dir / "cc_front.png"
    front_out = await _gen(backend, "chargen", [face_out], body_prompt(opts, "front"), front_out)
    panels.append(("FULL BODY FRONT", front_out))

    for view, label_id in (("side", "FULL BODY SIDE"), ("back", "FULL BODY BACK")):
        await step(f"🧍 Menggambar badan ({view})…")
        p = out_dir / f"cc_{view}.png"
        p = await _gen(backend, "chargen", [front_out], body_prompt(opts, view), p)
        panels.append((label_id, p))

    await step("📋 Menyusun sheet…")
    sheet = sheetbuild.build(
        name, out_dir / "cc_sheet.png", panels,
        subtitle=_ascii(f"Character Creator · master sheet from your face reference · "
                        f"{label('gender', opts.get('gender'))} · {label('race', opts.get('race'))} · "
                        f"{label('vibe', opts.get('vibe'))}"))
    if not sheet:
        raise RuntimeError("gagal menyusun sheet")
    return {"sheet": Path(sheet), "panels": panels}


def summary(opts: dict) -> str:
    """Ringkasan pilihan user (buat konfirmasi sebelum bayar)."""
    return ("\n".join([
        f"  · Gender: {label('gender', opts.get('gender'))}",
        f"  · Penampilan: {label('race', opts.get('race'))}",
        f"  · Vibe wajah: {label('vibe', opts.get('vibe'))}",
        f"  · Bentuk dada: {label('bust', opts.get('bust'))}",
        f"  · Langsing: {label('slim', opts.get('slim'))}",
        f"  · Pinggul–bawah: {label('hips', opts.get('hips'))}",
        f"  · Outfit: {label('outfit', opts.get('outfit'))}",
    ]))