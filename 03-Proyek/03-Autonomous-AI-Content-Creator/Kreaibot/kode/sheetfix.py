"""Character sheet → ambil panel orangnya (fix "hasil aneh" 9 Okt).

MASALAH NYATA: user mengirim **character sheet** (satu file berisi 15 panel: MAIN VIEW, SIDE VIEW,
EYES/NOSE/LIPS DETAIL, color swatch, dst) ke fitur image-to-video. Model lalu "menggerakkan"
lembaran panel itu → hasilnya jadi video berisi kotak-kotak panel, bukan orang. (job 13, 9 Okt.)

SOLUSI: sebelum render, foto diperiksa pakai model VISION (PromptSmith, teks saja — bukan model
generator): kalau terdeteksi sheet, bot mengambil SATU panel orang (paling cocok buat portrait)
dari koordinat yang dikasih model, lalu panel itulah yang dipakai render.

Semua opsional: kalau API tak ada / gagal / ragu → foto asli dipakai apa adanya (bot tetap jalan).
"""
from __future__ import annotations

import base64
import json
import logging
import urllib.request
from pathlib import Path

log = logging.getLogger("kreaibot.sheetfix")

PROMPT = (
    "Lihat gambar ini. Jawab HANYA JSON tanpa penjelasan: "
    '{"sheet": true/false, "box": [x, y, w, h]}.\n'
    "sheet=true kalau ini LEMBAR/KOLASE berisi BANYAK panel (beberapa gambar dalam satu file, "
    "biasanya ada label tulisan seperti MAIN VIEW / SIDE VIEW / DETAIL / color swatch). "
    "Jika ini foto satu orang biasa, sheet=false dan box=null.\n"
    "Kalau sheet=true: box = kotak panel yang PALING BAGUS dijadikan foto portrait, yaitu panel "
    "berisi SATU orang (setengah badan atau seluruh badan), menghadap kamera, tanpa tulisan, "
    "tanpa color swatch. Koordinat dalam PIXEL gambar asli (bukan persen), format [x, y, w, h]."
)


def _ask_vision(img_bytes: bytes, mime: str, base_url: str, api_key: str,
                model: str, timeout: int = 150) -> str:
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url": {"url": f"data:{mime};base64,"
                                                      + base64.b64encode(img_bytes).decode()}},
        ]}],
        "max_tokens": 300, "temperature": 0,
    }).encode()
    req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {api_key}"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        j = json.load(r)
    return str((j.get("choices") or [{}])[0].get("message", {}).get("content") or "")


def _parse(text: str) -> dict:
    """Ambil JSON dari balasan model (tahan banting: ada ```json ... ``` atau teks tambahan)."""
    s = text.strip()
    if "```" in s:
        parts = s.split("```")
        for p in parts:
            p = p.strip()
            if p.startswith("{") or p.startswith("json"):
                s = p[4:].strip() if p.startswith("json") else p
                break
    a, b = s.find("{"), s.rfind("}")
    if a < 0 or b < 0:
        return {"sheet": False, "box": None, "err": "tak ada JSON"}
    try:
        j = json.loads(s[a:b + 1])
    except Exception as e:                              # noqa: BLE001
        return {"sheet": False, "box": None, "err": str(e)[:80]}
    box = j.get("box")
    if not (isinstance(box, (list, tuple)) and len(box) == 4):
        box = None
    else:
        try:
            box = [int(float(v)) for v in box]
        except Exception:                               # noqa: BLE001
            box = None
    return {"sheet": bool(j.get("sheet")), "box": box}


def analyze_sync(path: Path, base_url: str, api_key: str, model: str) -> dict:
    """Deteksi sheet (blocking — panggil lewat asyncio.to_thread)."""
    if not (base_url and api_key and model):
        return {"sheet": False, "box": None, "skip": "vision tak dikonfigurasi"}
    try:
        raw = Path(path).read_bytes()
    except Exception as e:                              # noqa: BLE001
        return {"sheet": False, "box": None, "err": f"baca gagal: {e}"}
    mime = "image/png" if raw[:4] == b"\x89PNG" else "image/jpeg"
    try:
        return _parse(_ask_vision(raw, mime, base_url, api_key, model))
    except Exception as e:                              # noqa: BLE001
        log.warning("vision sheet-check gagal: %s", e)
        return {"sheet": False, "box": None, "err": str(e)[:120]}


def crop_panel(path: Path, box: list[int], out_path: Path,
               min_side: int = 220) -> Path | None:
    """Potong panel dari sheet. None kalau kotak tak masuk akal (biar foto asli tetap dipakai)."""
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        im = Image.open(path).convert("RGB")
    except Exception:                                   # noqa: BLE001
        return None
    W, H = im.size
    x, y, w, h = box
    x, y = max(0, min(x, W - 1)), max(0, min(y, H - 1))
    w, h = min(w, W - x), min(h, H - y)
    if w < min_side or h < min_side:                    # kotak kekecilan → jangan dipakai
        return None
    # buang margin 2% biar garis panel/gutter tidak ikut
    mx, my = int(w * 0.02), int(h * 0.02)
    box2 = (x + mx, y + my, x + w - mx, y + h - my)
    try:
        im.crop(box2).save(out_path, quality=95)
        return out_path
    except Exception:                                   # noqa: BLE001
        return None


def reason_text() -> str:
    return ("🔍 Sepertinya ini <b>character sheet</b> (satu gambar berisi banyak panel).\n"
            "Kalau sheet dipakai apa adanya, hasilnya jadi video berisi kotak-kotak panel.\n"
            "Bot sudah <b>mengambil panel orangnya</b> untuk dipakai render.")