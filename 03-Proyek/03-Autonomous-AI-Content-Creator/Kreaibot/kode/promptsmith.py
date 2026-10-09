"""PromptSmith — mesin perakit prompt untuk KREE.AI.

Tugasnya: ubah brief user (teks berantakan, campur bahasa) + gaya pilihan
menjadi SATU prompt rapi & natural (bahasa Inggris, standar model video).

ATURAN: prompt hasil rakitan TIDAK PERNAH ditampilkan ke user.
Hanya dipakai internal (dikirim ke backend) dan disimpan untuk admin/debug.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field


# ---------------------------------------------------------------- gaya UGC
@dataclass(frozen=True)
class Style:
    key: str
    label: str
    hook: str
    body: str
    cta: str
    tone: str
    camera: str
    duration: int = 15
    talk: bool = True


STYLES: dict[str, Style] = {
    "review": Style(
        key="review", label="🗣️ Review Jujur",
        hook="opens with a candid face-to-camera hook saying this is a real, honest opinion",
        body="talks naturally about the experience of using the product while holding it up to the lens",
        cta="ends with a soft, friendly recommendation and a small hand gesture toward the camera",
        tone="casual, warm, trustworthy creator voice",
        camera="handheld selfie-style medium close-up, subtle natural shake",
    ),
    "unboxing": Style(
        key="unboxing", label="📦 Unboxing",
        hook="reveals the unopened packaging to the camera with visible excitement",
        body="opens the package and shows the product clearly, rotating it slowly so the label and details are readable",
        cta="holds the product up next to their face and smiles to close",
        tone="energetic, curious, first-time-reaction",
        camera="handheld, slight top-down angle over a table, natural daylight",
    ),
    "problem": Style(
        key="problem", label="😤 Problem → Solusi",
        hook="describes a relatable everyday frustration directly to the camera with a slight frown",
        body="reveals the product as the fix and demonstrates it working with a relieved expression",
        cta="says the problem is finally solved and points to the product",
        tone="conversational, empathetic, relieved at the end",
        camera="handheld medium shot indoors, warm natural light",
    ),
    "testimoni": Style(
        key="testimoni", label="⭐ Testimoni / Before–After",
        hook="speaks as a happy customer describing how things changed after using the product",
        body="shows the product and demonstrates the visible result, natural and convincing",
        cta="gives a short confident endorsement while holding the product",
        tone="sincere, upbeat customer testimonial",
        camera="handheld close-up, clean bright indoor background",
    ),
    "promo": Style(
        key="promo", label="🔥 Promo Hard-Sell",
        hook="starts with a high-energy hook about a limited-time deal",
        body="highlights the price and key selling points with quick hand gestures, product held prominently",
        cta="urges viewers to order now before the promo ends, pointing down toward the link",
        tone="fast, persuasive, urgent, marketable",
        camera="dynamic handheld with small punch-in moves, punchy lighting",
    ),
    "cinematic": Style(
        key="cinematic", label="🎬 Iklan Sinematik",
        hook="opens on an elegant, aesthetic shot of the product in a styled setting",
        body="the creator uses the product gracefully with soft, purposeful movements; shallow depth of field",
        cta="final hero shot of the product with the creator smiling off-camera",
        tone="calm, premium, no talking — visuals and gentle music carry it",
        camera="smooth slow push-in and subtle dolly moves, soft cinematic light",
        talk=False,
    ),
}

NEGATIVE = ("no extra people, no warped hands or fingers, no distorted face, no duplicate limbs, "
            "no on-screen typos, no watermark, no logo overlay, no jitter or morphing")


def style_list_kb_rows():
    """Baris tombol gaya untuk bot: [(key, label), ...]."""
    return [(s.key, s.label) for s in STYLES.values()]


# ------------------------------------------------------- template (offline)
def h3_timeline(st: "Style", duration: int) -> str:
    """Timeline gaya H3 (MiniMax/Hailuo FL2VA): prompt dipecah per segmen waktu.

    Ini format yang dipakai workflow H3 (contoh resmi komunitas):
        0-2s: <aksi + kamera>
        2-5s: <aksi + kamera lanjutan>
    Model membacanya sebagai SATU shot kontinu dengan perubahan bertahap.
    """
    d = max(4, min(30, int(duration or 15)))
    hook = max(1, round(d * 0.25))
    body = max(1, round(d * 0.45))
    cta = max(1, d - hook - body)
    rows, t = [], 0
    for length, text in ((hook, st.hook), (body, st.body), (cta, st.cta)):
        rows.append(f"{t}-{t + length}s: {text}, {st.camera}")
        t += length
    return ("TIMELINE (ONE continuous shot; the model must read it as consecutive beats — "
            "same person, same outfit, same product, same location throughout, "
            "only action/camera/framing change):\n" + "\n".join(rows))


def build_ugc_prompt(brief: str, style_key: str, product_hint: str = "",
                     ratio: str = "9:16", char_desc: str = "",
                     duration: int | None = None, fmt: str = "h3") -> str:
    """Rakit prompt UGC dari brief user + gaya. Tanpa perlu API apa pun.

    fmt='h3' → sertakan timeline per-segmen (format MiniMax H3 / Hailuo),
    fmt='plain' → prompt deskriptif saja.
    """
    st = STYLES.get(style_key) or STYLES["review"]
    dur = int(duration or st.duration)
    parts: list[str] = []

    head = f"Create a {dur}-second vertical {ratio} UGC-style advertisement video"
    if not st.talk:
        head += " (no dialogue; ambient music mood only)"
    parts.append(head + ".")

    parts.append(
        "CHARACTER: use the uploaded character sheet photo as the exact person — "
        "keep the same face, hair, skin tone, body shape and outfit consistent across every frame"
        + (f" ({char_desc})" if char_desc else "") + ".")

    prod_desc = product_hint or "the product shown in the uploaded product photo"
    parts.append(
        f"PRODUCT: use the uploaded product photo as the real product — {prod_desc}. "
        "The product must stay visually faithful: same shape, colours and label text, "
        "held in realistic hands, never warped or duplicated.")

    parts.append(f"STORY BEATS: the video {st.hook}; then {st.body}; finally {st.cta}.")

    if fmt == "h3":
        parts.append(h3_timeline(st, dur))

    if st.talk:
        parts.append(
            "SPEECH: natural Indonesian creator delivery, casual and unrehearsed, "
            "mouth movements matching the words, with subtle natural facial expressions.")

    brief_clean = " ".join(str(brief or "").split())[:700]
    if brief_clean:
        parts.append(f"DETAILS FROM THE CREATOR (follow these facts exactly, in a natural way): {brief_clean}.")

    parts.append(f"CAMERA & LIGHTING: {st.camera}; realistic natural lighting, photoreal skin texture.")
    parts.append(f"MOOD: {st.tone}.")
    parts.append(f"AVOID: {NEGATIVE}.")
    return " ".join(parts)


# --------------------------------------------------- penyempurnaan via LLM
REFINE_SYSTEM = (
    "You are a senior prompt engineer for AI video models (MiniMax H3 / Hailuo, Kling, Veo, LTX). "
    "Take the creator's messy brief and the target style, then output ONE single, natural, "
    "well-structured English prompt that will produce a high-quality UGC advertisement video "
    "with a consistent character and a faithful product. "
    "Keep every factual detail (product name, price, claims). Never invent facts. "
    "Structure it as: overall description, CHARACTER, PRODUCT, STORY BEATS, "
    "TIMELINE as ONE continuous shot broken into time segments (MiniMax H3 format, e.g. "
    "'0-3s: ...' / '3-9s: ...' / '9-15s: ...', covering action + camera + lighting per segment, "
    "keeping the same person, outfit, product and location throughout), "
    "SPEECH (if any), CAMERA & LIGHT, MOOD, AVOID. "
    "Reply with the prompt text ONLY - no preamble, no quotes, no markdown."
)


# --------------------------------------------------- penyempurnaan prompt VIDEO (i2v/all-in-one)
# Pelajaran penting (8 Okt): menempel klausa "seluruh frame harus bergerak" membuat model
# ikut me-warp wajah & badan → hasilnya lebih rusak. Aturan di bawah sengaja KETAT:
# identitas & latar dipertahankan, gerakan kecil & natural, dilarang menambah objek baru.
VIDEO_REFINE_SYSTEM = (
    "You are a senior prompt engineer for IMAGE-TO-VIDEO models (MiniMax H3/Hailuo, Kling, LTX, Veo). "
    "You get the user's raw prompt (may be Indonesian, messy, or very short) and rewrite it into ONE "
    "single, natural, high-quality English prompt that animates the user's uploaded photo.\n"
    "HARD RULES:\n"
    "1. Keep the user's intent exactly: same person, same scene, same action. NEVER invent new "
    "objects, people, places, brands or events the user did not ask for.\n"
    "2. ONE ACTION ONLY (most important): if the user lists MANY actions in sequence, do NOT keep "
    "them all. Pick ONE main action and write it as ONE continuous movement. Never chain "
    "'then / after that / begins to ... and then'. Stacked actions (laugh, turn, run, stumble, look "
    "back) make the video warp and look broken.\n"
    "3. Camera: slow simple moves only (slow push-in, gentle pan, static). NEVER write chase-cam, "
    "handheld running, whip pan or fast camera motion - that is the main source of warping.\n"
    "4. Identity must stay stable: say the person's face, hair, glasses, skin and outfit stay exactly "
    "as in the photo, photoreal skin texture, no morphing, no identity drift.\n"
    "5. Keep the background faithful to the photo. You may describe only the motion that naturally "
    "belongs to what the user described (e.g. sea waves moving gently, hair and fabric in a light "
    "breeze). NEVER say the whole frame moves, never ask for constant motion everywhere.\n"
    "6. Motion must be smooth, calm and believable (small natural movement), not chaotic.\n"
    "7. Include: subject + action, subtle camera movement, lighting/mood, realism cues.\n"
    "8. ONE paragraph, max 70 words. No bullet points, no quotes, no markdown, no preamble.\n"
    "9. Never mention text, watermark, logo, subtitles, or any duration/timeline.\n"
    "Reply with the rewritten prompt text ONLY."
)


async def refine_with_llm(base_prompt: str, brief: str, style_key: str,
                          base_url: str = "", api_key: str = "", model: str = "") -> str:
    """Coba rapikan prompt pakai LLM (opsional). Gagal → kembalikan base_prompt."""
    base_url = (base_url or os.getenv("PROMPTSMITH_BASE_URL", "")).rstrip("/")
    api_key = api_key or os.getenv("PROMPTSMITH_API_KEY", "")
    model = model or os.getenv("PROMPTSMITH_MODEL", "")
    if not (base_url and api_key and model):
        return base_prompt
    try:
        import aiohttp
        st = STYLES.get(style_key) or STYLES["review"]
        user = (f"CREATOR BRIEF (messy, may be Indonesian):\n{brief}\n\n"
                f"TARGET STYLE: {st.label} — hook: {st.hook}; body: {st.body}; cta: {st.cta}; "
                f"tone: {st.tone}; camera: {st.camera}; duration {st.duration}s.\n\n"
                f"DRAFT PROMPT (improve this, keep all facts):\n{base_prompt}")
        payload = {"model": model, "temperature": 0.7, "max_tokens": 900,
                   "messages": [{"role": "system", "content": REFINE_SYSTEM},
                                {"role": "user", "content": user}]}
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as s:
            async with s.post(f"{base_url}/chat/completions", json=payload,
                              headers={"Authorization": f"Bearer {api_key}",
                                       "Content-Type": "application/json"}) as r:
                js = await r.json(content_type=None)
        txt = (js.get("choices") or [{}])[0].get("message", {}).get("content", "").strip()
        return txt or base_prompt
    except Exception:
        return base_prompt


async def refine_video_prompt(raw: str, ratio: str = "9:16", duration: int = 5,
                              base_url: str = "", api_key: str = "", model: str = "",
                              timeout: int = 30) -> str:
    """Rapikan prompt user untuk fitur video (i2v / all-in-one).

    Aman: gagal / kosong / hasilnya aneh → kembalikan prompt ASLI. Render tidak boleh
    gagal cuma karena perapian prompt.
    """
    raw = " ".join(str(raw or "").split())
    if len(raw) < 3:
        return raw
    base_url = (base_url or os.getenv("PROMPTSMITH_BASE_URL", "")).rstrip("/")
    api_key = api_key or os.getenv("PROMPTSMITH_API_KEY", "")
    model = model or os.getenv("PROMPTSMITH_MODEL", "")
    if not (base_url and api_key and model):
        return raw
    try:
        import aiohttp
        user = (f"USER PROMPT (may be Indonesian, may be messy):\n{raw}\n\n"
                f"CONTEXT: image-to-video from the user's uploaded photo, aspect ratio {ratio}, "
                f"about {duration} seconds.\nREWRITTEN PROMPT:")
        payload = {"model": model, "temperature": 0.4, "max_tokens": 400,
                   "messages": [{"role": "system", "content": VIDEO_REFINE_SYSTEM},
                                {"role": "user", "content": user}]}
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as s:
            async with s.post(f"{base_url}/chat/completions", json=payload,
                              headers={"Authorization": f"Bearer {api_key}",
                                       "Content-Type": "application/json"}) as r:
                js = await r.json(content_type=None)
        txt = ((js.get("choices") or [{}])[0].get("message", {}) or {}).get("content", "") or ""
        txt = " ".join(txt.strip().strip('"').strip("`").split())[:1200]
        # Jaring pengaman: jawaban ngawur / kependekan → pakai prompt ASLI.
        if len(txt) < 20 or txt.lower().startswith(("i ", "here", "sure", "prompt:", "asal")):
            return raw
        return txt
    except Exception:                       # noqa: BLE001
        return raw


def summary_for_user(style_key: str, brief: str = "") -> str:
    """Ringkasan untuk user — TIDAK memuat prompt rakitan."""
    st = STYLES.get(style_key) or STYLES["review"]
    return f"🎨 Gaya: <b>{st.label}</b>\n⏱ Durasi: <b>{st.duration} detik</b>"