#!/usr/bin/env python3
"""Bangun workflow orisinal RH: 'Menu & Poster Studio' (Qwen-Image text-to-image).

Output: workflows/menu-poster-studio.json  (format ComfyUI UI, siap di-import ke RunningHub)

Semua tipe node + nama model diambil dari workflow publik RH yang sudah terbukti jalan
(pq_1954567812612288513 = Qwen-Image t2i, pq_2074679846487289857 = menu, pq_1967918185590718466).

Desain app (penting untuk publish):
  * SELURUH node = node STANDAR  -> RunningHub BISA mengekspose widget-nya sebagai input user.
  * Input yang di-expose ke user: CLIPTextEncode(node 7).text  ("Describe your menu / poster").
  * Node 6 = prompt gaya (di-bake, tidak di-expose) -> digabung via ConditioningCombine.
    Jadi user cukup menulis isi/ide, hasilnya tetap konsisten bergaya poster profesional.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "workflows" / "menu-poster-studio.json"

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


def in_sock(name, wtype, link=None, shape=None):
    e = {"name": name, "type": wtype, "label": name, "localized_name": name}
    if link is not None:
        e["link"] = link
    if shape:
        e["shape"] = shape
    return e


def in_widget(name, wtype, shape=None):
    e = {"widget": {"name": name}, "name": name, "label": name,
         "type": wtype, "localized_name": name}
    if shape:
        e["shape"] = shape
    return e


def out_sock(name, wtype, links, slot=0):
    return {"name": name, "type": wtype, "links": links, "label": name,
            "localized_name": name, "slot_index": slot}


def link(oid, oslot, tid, tslot, ltype):
    _link["n"] += 1
    lid = _link["n"]
    links.append([lid, oid, oslot, tid, tslot, ltype])
    return lid


# ---------------------------------------------------------------- prompt
STYLE = ("Professional restaurant menu and promotional poster design. Clean modern layout, "
         "appetizing food photography, elegant typography, strong visual hierarchy, "
         "high-end commercial print quality, balanced composition, soft studio lighting, "
         "rich vibrant colors, sharp details, 4k advertising quality.")

USER_DEFAULT = ("A steaming bowl of beef noodle soup on a rustic wooden table, fresh herbs and "
                "chili on the side, warm inviting light. Large elegant title text \"MENU SPESIAL\" "
                "at the top and a smaller line \"Mulai Rp 25.000\" below it. Modern restaurant "
                "poster style.")

# ---------------------------------------------------------------- 1 UNETLoader
node(1, "UNETLoader", (40, 40), (330, 82),
     ["qwen_image_fp8_e4m3fn.safetensors", "default"],
     [in_widget("unet_name", "COMBO"), in_widget("weight_dtype", "COMBO")],
     [out_sock("MODEL", "MODEL", [1])], order=0)

# ---------------------------------------------------------------- 2 LoRA Lightning 8-step
node(2, "LoraLoaderModelOnly", (400, 40), (330, 82),
     ["Qwen-Image-Lightning-8steps-V2.0 bf16.safetensors", 1.0],
     [in_sock("model", "MODEL"), in_widget("lora_name", "COMBO"),
      in_widget("strength_model", "FLOAT")],
     [out_sock("MODEL", "MODEL", [2])], order=1)

# ---------------------------------------------------------------- 3 ModelSamplingAuraFlow
node(3, "ModelSamplingAuraFlow", (760, 40), (250, 82),
     [3.5],
     [in_sock("model", "MODEL"), in_widget("shift", "FLOAT")],
     [out_sock("MODEL", "MODEL", [3])], order=2)

# ---------------------------------------------------------------- 4 CLIPLoader
node(4, "CLIPLoader", (40, 160), (330, 106),
     ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"],
     [in_widget("clip_name", "COMBO"), in_widget("type", "COMBO"),
      in_widget("device", "COMBO", shape=7)],
     [out_sock("CLIP", "CLIP", [4, 5])], order=3)

# ---------------------------------------------------------------- 5 VAELoader
node(5, "VAELoader", (40, 300), (330, 58),
     ["qwen_image_vae.safetensors"],
     [in_widget("vae_name", "COMBO")],
     [out_sock("VAE", "VAE", [6])], order=4)

# ---------------------------------------------------------------- 6 CLIPTextEncode (gaya, dibake)
node(6, "CLIPTextEncode", (400, 160), (420, 160),
     [STYLE],
     [in_sock("clip", "CLIP"), in_widget("text", "STRING")],
     [out_sock("CONDITIONING", "CONDITIONING", [7, 8])], order=5,
     title="Style preset (baked)")

# ---------------------------------------------------------------- 7 CLIPTextEncode (USER, diekspos)
node(7, "CLIPTextEncode", (400, 360), (420, 220),
     [USER_DEFAULT],
     [in_sock("clip", "CLIP"), in_widget("text", "STRING")],
     [out_sock("CONDITIONING", "CONDITIONING", [9])], order=6,
     title="Your menu / poster idea")

# ---------------------------------------------------------------- 8 ConditioningCombine
node(8, "ConditioningCombine", (860, 300), (250, 66),
     [],
     [in_sock("conditioning_1", "CONDITIONING"), in_sock("conditioning_2", "CONDITIONING")],
     [out_sock("CONDITIONING", "CONDITIONING", [10])], order=7)

# ---------------------------------------------------------------- 9 ConditioningZeroOut (negatif)
node(9, "ConditioningZeroOut", (860, 400), (250, 46),
     [],
     [in_sock("conditioning", "CONDITIONING")],
     [out_sock("CONDITIONING", "CONDITIONING", [11])], order=8)

# ---------------------------------------------------------------- 10 EmptySD3LatentImage
node(10, "EmptySD3LatentImage", (40, 420), (250, 106),
     [832, 1216, 1],
     [in_widget("width", "INT"), in_widget("height", "INT"), in_widget("batch_size", "INT")],
     [out_sock("LATENT", "LATENT", [12])], order=9)

# ---------------------------------------------------------------- 11 KSampler
node(11, "KSampler", (1150, 40), (300, 262),
     [1234567890, "randomize", 8, 1, "euler", "simple", 1],
     [in_sock("model", "MODEL"), in_sock("positive", "CONDITIONING"),
      in_sock("negative", "CONDITIONING"), in_sock("latent_image", "LATENT"),
      in_widget("seed", "INT"), in_widget("steps", "INT"), in_widget("cfg", "FLOAT"),
      in_widget("sampler_name", "COMBO"), in_widget("scheduler", "COMBO"),
      in_widget("denoise", "FLOAT")],
     [out_sock("LATENT", "LATENT", [13])], order=10)

# ---------------------------------------------------------------- 12 VAEDecode
node(12, "VAEDecode", (1500, 40), (240, 46),
     [],
     [in_sock("samples", "LATENT"), in_sock("vae", "VAE")],
     [out_sock("IMAGE", "IMAGE", [14])], order=11)

# ---------------------------------------------------------------- 13 SaveImage
node(13, "SaveImage", (1500, 140), (400, 450),
     ["MenuPosterStudio"],
     [in_sock("images", "IMAGE"), in_widget("filename_prefix", "STRING")],
     [out_sock("image_urls", "STRING", [], slot=0), out_sock("images", "IMAGE", [], slot=1)],
     order=12)

# ---------------------------------------------------------------- 14 MarkdownNote
GUIDE = ("## Menu & Poster Studio (Qwen-Image)\n\n"
         "**What it does** — turn one written idea into a finished restaurant menu / promo poster.\n"
         "Qwen-Image renders on-image text (titles, prices) better than most models.\n\n"
         "**How to use**\n"
         "1. Write your idea in `Your menu / poster idea` — describe the dish, the mood,\n"
         "   and the words that must appear on the poster (put them in quotes).\n"
         "2. Run. Output is 832x1216 portrait.\n\n"
         "**Tips** — always quote the exact text you want printed:\n"
         "`Large title text \"NASI GORENG SPESIAL\" and below it \"Rp 25.000\".`\n\n"
         "**Models** — Qwen-Image fp8 + Qwen-Image-Lightning 8-step LoRA (fast & cheap)\n"
         "+ Qwen 2.5-VL text encoder + Qwen Image VAE. Style preset is baked in and\n"
         "combined with your prompt, so every result keeps a consistent poster look.\n\n"
         "Prompts can be in Indonesian, English or Chinese.")
node(14, "MarkdownNote", (1150, 360), (620, 340), [GUIDE], [], [], order=13,
     props={"widget_ue_connectable": {}, "Node name for S&R": "MarkdownNote"})

# ---------------------------------------------------------------- wiring
def wire(olid, oslot, tid, tslot, ltype):
    l = link(olid, oslot, tid, tslot, ltype)
    tnode = next(n for n in nodes if n["id"] == tid)
    tnode["inputs"][tslot]["link"] = l
    return l

# model: 1 -> 2 -> 3 -> 11
wire(1, 0, 2, 0, "MODEL")
wire(2, 0, 3, 0, "MODEL")
wire(3, 0, 11, 0, "MODEL")
# clip: 4 -> 6, 4 -> 7
wire(4, 0, 6, 0, "CLIP")
wire(4, 0, 7, 0, "CLIP")
# vae: 5 -> 12
wire(5, 0, 12, 1, "VAE")
# conditioning: 6 -> 8 (slot0), 7 -> 8 (slot1), 6 -> 9
wire(6, 0, 8, 0, "CONDITIONING")
wire(7, 0, 8, 1, "CONDITIONING")
wire(6, 0, 9, 0, "CONDITIONING")
# positive/negative -> 11
wire(8, 0, 11, 1, "CONDITIONING")
wire(9, 0, 11, 2, "CONDITIONING")
# latent: 10 -> 11
wire(10, 0, 11, 3, "LATENT")
# sampler -> decode -> save
wire(11, 0, 12, 0, "LATENT")
wire(12, 0, 13, 0, "IMAGE")

wf = {
    "last_node_id": 14,
    "last_link_id": _link["n"],
    "nodes": nodes,
    "links": links,
    "groups": [],
    "config": {},
    "extra": {"ds": {"scale": 0.65, "offset": [0, 0]}},
    "version": 0.4,
}

# ---------------------------------------------------------------- validasi
ids = {n["id"]: n for n in nodes}
# hitung ulang daftar link di setiap output dari tabel `links` (sumber kebenaran)
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