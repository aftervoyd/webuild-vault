#!/usr/bin/env python3
"""Bangun workflow orisinal RH: 'Food & Product Photo Studio' (Qwen-Image text-to-image).

Output: workflows/food-photo-studio.json

Dasar keputusan (dari 4 uji-jalan nyata, lihat RUNNINGHUB-GAP-SCAN.md):
  * Model SELALU menyisipkan teks sampah bila prompt mengarah ke "poster/menu"  -> poster berteks TIDAK layak.
  * Foto makanan/produk + headline yang diminta justru render BAGUS.
  Karena itu produk ini diposisikan sebagai STUDIO FOTO (bebas teks), bukan pembuat poster berteks.

Desain app:
  * Semua node = node STANDAR  -> RunningHub BISA mengekspose widget-nya sebagai input user.
  * Input yang di-expose: CLIPTextEncode(node 6).text  ("Describe the dish / product").
  * Node 5 = preset gaya fotografi komersial, anti-teks (di-bake) -> digabung ConditioningCombine.
  * Tanpa LoRA Lightning: uji 8-step menghasilkan teks/artefak buruk; 30 step penuh jauh lebih bersih
    dan tetap murah (13-22 koin/run, 60-110 dtk).
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "workflows" / "food-photo-studio.json"

nodes, links = [], []
_link = {"n": 0}


def node(nid, ntype, pos, size, widgets, inputs, outputs, props=None, mode=0, order=0, title=None):
    d = {
        "id": nid, "type": ntype, "pos": list(pos), "size": list(size),
        "flags": {}, "order": order, "mode": mode,
        "inputs": inputs, "outputs": outputs, "widgets_values": list(widgets),
        "properties": props or {"cnr_id": "comfy-core", "ver": "0.3.48",
                                "widget_ue_connectable": {}, "Node name for S&R": ntype},
    }
    if title:
        d["title"] = title
    nodes.append(d)
    return d


def in_sock(name, wtype, link=None):
    e = {"name": name, "type": wtype, "label": name, "localized_name": name}
    if link is not None:
        e["link"] = link
    return e


def in_widget(name, wtype, shape=None):
    e = {"widget": {"name": name}, "name": name, "label": name,
         "type": wtype, "localized_name": name}
    if shape:
        e["shape"] = shape
    return e


def out_sock(name, wtype, slot=0):
    return {"name": name, "type": wtype, "links": [], "label": name,
            "localized_name": name, "slot_index": slot}


def link(oid, oslot, tid, tslot, ltype):
    _link["n"] += 1
    lid = _link["n"]
    links.append([lid, oid, oslot, tid, tslot, ltype])
    return lid


# ------------------------------------------------------------------ prompt
STYLE = ("Photorealistic professional food photography, natural daylight, realistic textures, "
         "appetizing true-to-life colors, shallow depth of field, clean minimal background, "
         "shot on a full-frame camera. No text, no words, no letters, no numbers, no watermark, "
         "no logo, no signage, no captions, no menu lists. "
         "Absolutely text-free image.")

USER_DEFAULT = ("A plate of Indonesian nasi goreng topped with a sunny-side-up fried egg, a few cucumber "
                "slices and a red chili on the side, served on a rustic wooden table, warm inviting light, "
                "steam rising from the rice.")

# ------------------------------------------------------------------ 1 UNETLoader
node(1, "UNETLoader", (40, 40), (330, 82),
     ["qwen_image_fp8_e4m3fn.safetensors", "default"],
     [in_widget("unet_name", "COMBO"), in_widget("weight_dtype", "COMBO")],
     [out_sock("MODEL", "MODEL")], order=0)

# ------------------------------------------------------------------ 2 ModelSamplingAuraFlow
node(2, "ModelSamplingAuraFlow", (400, 40), (250, 82),
     [3.5],
     [in_sock("model", "MODEL"), in_widget("shift", "FLOAT")],
     [out_sock("MODEL", "MODEL")], order=1)

# ------------------------------------------------------------------ 3 CLIPLoader
node(3, "CLIPLoader", (40, 160), (330, 106),
     ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"],
     [in_widget("clip_name", "COMBO"), in_widget("type", "COMBO"),
      in_widget("device", "COMBO", shape=7)],
     [out_sock("CLIP", "CLIP")], order=2)

# ------------------------------------------------------------------ 4 VAELoader
node(4, "VAELoader", (40, 300), (330, 58),
     ["qwen_image_vae.safetensors"],
     [in_widget("vae_name", "COMBO")],
     [out_sock("VAE", "VAE")], order=3)

# ------------------------------------------------------------------ 5 CLIPTextEncode (preset gaya, dibake)
node(5, "CLIPTextEncode", (400, 160), (430, 170),
     [STYLE],
     [in_sock("clip", "CLIP"), in_widget("text", "STRING")],
     [out_sock("CONDITIONING", "CONDITIONING")], order=4,
     title="Style preset (baked)")

# ------------------------------------------------------------------ 6 CLIPTextEncode (USER, diekspos)
node(6, "CLIPTextEncode", (400, 370), (430, 200),
     [USER_DEFAULT],
     [in_sock("clip", "CLIP"), in_widget("text", "STRING")],
     [out_sock("CONDITIONING", "CONDITIONING")], order=5,
     title="Describe your dish / product")

# ------------------------------------------------------------------ 7 ConditioningCombine
node(7, "ConditioningCombine", (870, 300), (250, 66),
     [],
     [in_sock("conditioning_1", "CONDITIONING"), in_sock("conditioning_2", "CONDITIONING")],
     [out_sock("CONDITIONING", "CONDITIONING")], order=6)

# ------------------------------------------------------------------ 8 ConditioningZeroOut
node(8, "ConditioningZeroOut", (870, 400), (250, 46),
     [],
     [in_sock("conditioning", "CONDITIONING")],
     [out_sock("CONDITIONING", "CONDITIONING")], order=7)

# ------------------------------------------------------------------ 9 EmptySD3LatentImage
node(9, "EmptySD3LatentImage", (40, 420), (250, 106),
     [832, 1216, 1],
     [in_widget("width", "INT"), in_widget("height", "INT"), in_widget("batch_size", "INT")],
     [out_sock("LATENT", "LATENT")], order=8)

# ------------------------------------------------------------------ 10 KSampler
node(10, "KSampler", (1160, 40), (300, 262),
     [1234567890, "randomize", 30, 4, "euler", "simple", 1],
     [in_sock("model", "MODEL"), in_sock("positive", "CONDITIONING"),
      in_sock("negative", "CONDITIONING"), in_sock("latent_image", "LATENT"),
      in_widget("seed", "INT"), in_widget("steps", "INT"), in_widget("cfg", "FLOAT"),
      in_widget("sampler_name", "COMBO"), in_widget("scheduler", "COMBO"),
      in_widget("denoise", "FLOAT")],
     [out_sock("LATENT", "LATENT")], order=9)

# ------------------------------------------------------------------ 11 VAEDecode
node(11, "VAEDecode", (1510, 40), (240, 46),
     [],
     [in_sock("samples", "LATENT"), in_sock("vae", "VAE")],
     [out_sock("IMAGE", "IMAGE")], order=10)

# ------------------------------------------------------------------ 12 SaveImage
node(12, "SaveImage", (1510, 140), (400, 450),
     ["FoodPhotoStudio"],
     [in_sock("images", "IMAGE"), in_widget("filename_prefix", "STRING")],
     [out_sock("image_urls", "STRING", slot=0), out_sock("images", "IMAGE", slot=1)],
     order=11)

# ------------------------------------------------------------------ 13 MarkdownNote
GUIDE = ("## Food & Product Photo Studio (Qwen-Image)\n\n"
         "**What it does** — turns one written description into a studio-quality food or product photo.\n"
         "Made for menu photos, delivery-app listings, social posts and UMKM product catalogues.\n\n"
         "**How to use**\n"
         "1. Describe the dish or product in `Describe your dish / product`:\n"
         "   what it is, the plate/packaging, the surface, the light and the mood.\n"
         "2. Run. Output is 832x1216 portrait.\n\n"
         "**Example**\n"
         "`A bowl of beef noodle soup on a dark slate table, fresh herbs and chili on the side, "
         "warm side light, steam rising, clean background.`\n\n"
         "**Note** — this app is intentionally TEXT-FREE. Generated lettering is unreliable, so the "
         "style preset suppresses all words; add the real title/price in Canva or Photoshop afterwards.\n\n"
         "**Models** — Qwen-Image fp8, 30 steps, cfg 4, euler/simple + Qwen 2.5-VL text encoder\n"
         "+ Qwen Image VAE. Prompts can be Indonesian, English or Chinese.")
node(13, "MarkdownNote", (1160, 360), (620, 340), [GUIDE], [], [], order=12,
     props={"widget_ue_connectable": {}, "Node name for S&R": "MarkdownNote"})

# ------------------------------------------------------------------ wiring
def wire(olid, oslot, tid, tslot, ltype):
    l = link(olid, oslot, tid, tslot, ltype)
    tnode = next(n for n in nodes if n["id"] == tid)
    tnode["inputs"][tslot]["link"] = l


wire(1, 0, 2, 0, "MODEL")            # unet -> auraflow
wire(2, 0, 10, 0, "MODEL")           # auraflow -> ksampler
wire(3, 0, 5, 0, "CLIP")             # clip -> style
wire(3, 0, 6, 0, "CLIP")             # clip -> user
wire(4, 0, 11, 1, "VAE")             # vae -> decode
wire(5, 0, 7, 0, "CONDITIONING")     # style -> combine(0)
wire(6, 0, 7, 1, "CONDITIONING")     # user  -> combine(1)
wire(5, 0, 8, 0, "CONDITIONING")     # style -> zeroout
wire(7, 0, 10, 1, "CONDITIONING")    # positive
wire(8, 0, 10, 2, "CONDITIONING")    # negative
wire(9, 0, 10, 3, "LATENT")          # latent
wire(10, 0, 11, 0, "LATENT")         # sampler -> decode
wire(11, 0, 12, 0, "IMAGE")          # decode -> save

wf = {
    "last_node_id": 13,
    "last_link_id": _link["n"],
    "nodes": nodes,
    "links": links,
    "groups": [],
    "config": {},
    "extra": {"ds": {"scale": 0.65, "offset": [0, 0]}},
    "version": 0.4,
}

# ------------------------------------------------------------------ validasi
ids = {n["id"]: n for n in nodes}
for n in nodes:
    for o in n["outputs"]:
        o["links"] = []
for lid, oid, oslot, tid, tslot, ltype in links:
    ids[oid]["outputs"][oslot]["links"].append(lid)

errs = []
for lid, oid, oslot, tid, tslot, ltype in links:
    o, t = ids.get(oid), ids.get(tid)
    if not o or not t:
        errs.append(f"link {lid}: node hilang {oid}->{tid}")
        continue
    if oslot >= len(o["outputs"]):
        errs.append(f"link {lid}: slot keluar {oid}:{oslot} invalid")
    elif lid not in (o["outputs"][oslot].get("links") or []):
        errs.append(f"link {lid}: tidak tercatat di output {oid}:{oslot}")
    if tslot >= len(t["inputs"]):
        errs.append(f"link {lid}: slot masuk {tid}:{tslot} invalid")
    elif t["inputs"][tslot].get("link") != lid:
        errs.append(f"link {lid}: tidak tercatat di input {tid}:{tslot}")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(wf, indent=2))
print("ditulis:", OUT, "| nodes:", len(nodes), "links:", len(links))
print("ERRORS:", errs if errs else "none OK")