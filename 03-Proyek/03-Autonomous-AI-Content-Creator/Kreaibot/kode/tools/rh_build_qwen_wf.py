#!/usr/bin/env python3
"""Bangun workflow orisinal RH: 'Qwen-Image-Edit 2511 · Consistency Edit'.

Output: workflows/qwen-consistency-edit.json (format ComfyUI UI, siap di-import ke RunningHub).
Semua tipe node + nama model diambil dari workflow publik RH yang sudah terbukti jalan.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "workflows" / "qwen-consistency-edit.json"

nodes = []
links = []
_link = {"n": 0}


def node(nid, ntype, pos, size, widgets, inputs, outputs, props=None, mode=0, order=0, title=None):
    d = {
        "id": nid, "type": ntype, "pos": list(pos), "size": list(size),
        "flags": {}, "order": order, "mode": mode,
        "inputs": inputs, "outputs": outputs, "widgets_values": list(widgets),
        "properties": props or {"Node name for S&R": ntype, "widget_ue_connectable": {}},
    }
    if title:
        d["title"] = title
    nodes.append(d)
    return d


def in_widget(name, wtype, link=None, shape=None, extra=None):
    e = {"name": name, "type": wtype, "widget": {"name": name},
         "label": name, "localized_name": name}
    if link is not None:
        e["link"] = link
    if shape:
        e["shape"] = shape
    if extra:
        e.update(extra)
    return e


def in_sock(name, wtype, link=None, shape=None):
    e = {"name": name, "type": wtype, "label": name, "localized_name": name}
    if link is not None:
        e["link"] = link
    if shape:
        e["shape"] = shape
    return e


def out_sock(name, wtype, links, shape=None):
    e = {"name": name, "type": wtype, "links": links, "label": name,
         "localized_name": name, "slot_index": 0}
    if shape:
        e["shape"] = shape
    return e


def link(origin_id, origin_slot, target_id, target_slot, ltype):
    _link["n"] += 1
    lid = _link["n"]
    links.append([lid, origin_id, origin_slot, target_id, target_slot, ltype])
    return lid


SYS = ("Describe the key features of the input image (color, shape, size, texture, objects, "
       "background), then explain how the user's text instruction should alter or modify the image. "
       "Generate a new image that meets the user's requirements while maintaining consistency "
       "with the original input where appropriate.")
INSTR = "Change the background to a soft studio gradient, keep the subject's face and identity exactly the same, professional lighting."

# ---- 1 UNETLoader -----------------------------------------------------------
node(1, "UNETLoader", (40, 40), (340, 82),
     ["qwen_image_edit_2511_bf16.safetensors", "default"],
     [in_widget("unet_name", "COMBO"), in_widget("weight_dtype", "COMBO")],
     [out_sock("MODEL", "MODEL", [1])], order=0)

# ---- 2 LoraLoaderModelOnly (consistency) -----------------------------------
node(2, "LoraLoaderModelOnly", (420, 40), (340, 82),
     ["consistence_edit_v2.safetensors", 0.7],
     [in_sock("model", "MODEL", None), in_widget("lora_name", "COMBO"), in_widget("strength_model", "FLOAT")],
     [out_sock("MODEL", "MODEL", [2])], order=1)

# ---- 3 LoraLoaderModelOnly (lightning 4-step) ------------------------------
node(3, "LoraLoaderModelOnly", (800, 40), (340, 82),
     ["Qwen-Image-Edit-2511-Lightning-4steps-V1-fp32.safetensors", 1],
     [in_sock("model", "MODEL", None), in_widget("lora_name", "COMBO"), in_widget("strength_model", "FLOAT")],
     [out_sock("MODEL", "MODEL", [3])], order=2)

# ---- 4 CLIPLoader ----------------------------------------------------------
node(4, "CLIPLoader", (40, 180), (340, 106),
     ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"],
     [in_widget("clip_name", "COMBO"), in_widget("type", "COMBO"), in_widget("device", "COMBO")],
     [out_sock("CLIP", "CLIP", [4])], order=3)

# ---- 5 VAELoader -----------------------------------------------------------
node(5, "VAELoader", (40, 340), (340, 58),
     ["qwen_image_vae.safetensors"],
     [in_widget("vae_name", "COMBO")],
     [out_sock("VAE", "VAE", [5, 6])], order=4)

# ---- 6 LoadImage -----------------------------------------------------------
node(6, "LoadImage", (40, 450), (340, 314),
     ["example.png", "image"],
     [in_widget("image", "COMBO"), in_widget("upload", "IMAGEUPLOAD")],
     [out_sock("IMAGE", "IMAGE", [7, 8]), out_sock("MASK", "MASK", [])], order=5)

# ---- 7 Easy_QwenEdit2509 ---------------------------------------------------
node(7, "Easy_QwenEdit2509", (430, 420), (420, 300),
     ["crop", 384, INSTR, SYS],
     [in_sock("clip", "CLIP", None), in_sock("vae", "VAE", None),
      in_sock("image1", "IMAGE", None, shape=7), in_sock("image2", "IMAGE", None, shape=7),
      in_sock("image3", "IMAGE", None, shape=7), in_sock("latent_image", "IMAGE", None, shape=7),
      in_sock("latent_mask", "MASK", None, shape=7),
      in_widget("auto_resize", "COMBO"), in_widget("vl_size", "INT"),
      in_widget("prompt", "STRING"), in_widget("system_prompt", "STRING")],
     [out_sock("positive", "CONDITIONING", [9]), out_sock("zero_negative", "CONDITIONING", [10]),
      out_sock("latent", "LATENT", [11])], order=6)

# ---- 8 KSampler ------------------------------------------------------------
node(8, "KSampler", (900, 180), (320, 262),
     [1234567890, "randomize", 4, 1, "euler", "beta57", 1],
     [in_sock("model", "MODEL", None), in_sock("positive", "CONDITIONING", None),
      in_sock("negative", "CONDITIONING", None), in_sock("latent_image", "LATENT", None),
      in_widget("seed", "INT"), in_widget("steps", "INT"), in_widget("cfg", "FLOAT"),
      in_widget("sampler_name", "COMBO"), in_widget("scheduler", "COMBO"), in_widget("denoise", "FLOAT")],
     [out_sock("LATENT", "LATENT", [12])], order=7)

# ---- 9 VAEDecode -----------------------------------------------------------
node(9, "VAEDecode", (1270, 180), (240, 46),
     [],
     [in_sock("samples", "LATENT", None), in_sock("vae", "VAE", None)],
     [out_sock("IMAGE", "IMAGE", [13])], order=8)

# ---- 10 SaveImage ----------------------------------------------------------
node(10, "SaveImage", (1270, 280), (400, 450),
     ["QwenConsistencyEdit"],
     [in_sock("images", "IMAGE", None), in_widget("filename_prefix", "STRING")],
     [out_sock("image_urls", "STRING", []), out_sock("images", "IMAGE", [])], order=9)

# ---- 11 MarkdownNote (panduan) --------------------------------------------
GUIDE = ("## Qwen-Image-Edit 2511 · Consistency Edit\n\n"
         "**What it does**: edit any photo with a plain-English instruction while "
         "keeping the person/subject identity consistent.\n\n"
         "**How to use**\n"
         "1. Upload an image (LoadImage).\n"
         "2. Write your edit instruction in the `prompt` field of "
         "`Easy_QwenEdit2509` (e.g. *change the background to a beach, keep the face the same*).\n"
         "3. Run. 4-step Lightning sampler keeps it fast and cheap.\n\n"
         "**Models**: Qwen-Image-Edit-2511 (bf16) · Lightning 4-step LoRA · "
         "consistency-edit LoRA (0.7) · Qwen 2.5-VL text encoder · Qwen Image VAE.\n\n"
         "Built for consistent character / product editing.")
node(11, "MarkdownNote", (430, 760), (600, 320), [GUIDE], [], [], order=10)

# ---- wiring -----------------------------------------------------------------
# model chain 1 -> 2 -> 3 -> 8
l = link(1, 0, 2, 0, "MODEL"); nodes[1]["inputs"][0]["link"] = l
l = link(2, 0, 3, 0, "MODEL"); nodes[2]["inputs"][0]["link"] = l
l = link(3, 0, 8, 0, "MODEL"); nodes[7]["inputs"][0]["link"] = l
# clip 4 -> 7
l = link(4, 0, 7, 0, "CLIP"); nodes[6]["inputs"][0]["link"] = l
# vae 5 -> 7 and 5 -> 9
l = link(5, 0, 7, 1, "VAE"); nodes[6]["inputs"][1]["link"] = l
l = link(5, 0, 9, 1, "VAE"); nodes[8]["inputs"][1]["link"] = l
# image 6 -> 7 (image1 + latent_image)
l = link(6, 0, 7, 2, "IMAGE"); nodes[6]["inputs"][2]["link"] = l
l = link(6, 0, 7, 5, "IMAGE"); nodes[6]["inputs"][5]["link"] = l
# easy outputs -> ksampler
l = link(7, 0, 8, 1, "CONDITIONING"); nodes[7]["inputs"][1]["link"] = l
l = link(7, 1, 8, 2, "CONDITIONING"); nodes[7]["inputs"][2]["link"] = l
l = link(7, 2, 8, 3, "LATENT"); nodes[7]["inputs"][3]["link"] = l
# ksampler -> vaedecode -> saveimage
l = link(8, 0, 9, 0, "LATENT"); nodes[8]["inputs"][0]["link"] = l
l = link(9, 0, 10, 0, "IMAGE"); nodes[9]["inputs"][0]["link"] = l

wf = {
    "last_node_id": 11,
    "last_link_id": _link["n"],
    "nodes": nodes,
    "links": links,
    "groups": [],
    "config": {},
    "extra": {"ds": {"scale": 0.65, "offset": [0, 0]}},
    "version": 0.4,
}

# ---- validasi ---------------------------------------------------------------
ids = {n["id"]: n for n in nodes}
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
print("ERRORS:", errs if errs else "none ✓")