import json, urllib.request, collections, time
H={"Content-Type":"application/json","client":"web","X-RH-Lang":"en","User-Language":"en"}
def post(url, body):
    r=urllib.request.Request(url, data=json.dumps(body).encode(), headers=H)
    return json.load(urllib.request.urlopen(r, timeout=30))
def search(kw, n=6):
    try:
        d=post("https://www.runninghub.ai/api/search/workflow", {"search":kw,"current":1,"size":n})
        return [x.get("id") for x in d["data"]["records"] if x.get("id")]
    except Exception as e:
        return []
def export(wid):
    try:
        r=urllib.request.Request("https://www.runninghub.ai/api/workflow/export",
            data=json.dumps({"workflowId":wid}).encode(), headers=H)
        return json.load(urllib.request.urlopen(r, timeout=40))
    except Exception:
        return None

for kw in ["抠图","证件照","菜单","商品图","模特换人"]:
    ids=search(kw, 5)
    print(f"\n### {kw}  -> {len(ids)} diprobe")
    nodes=collections.Counter(); models=set()
    for wid in ids[:4]:
        d=export(wid)
        if not d: continue
        w=d.get("data") or d
        w=w.get("workflow") if isinstance(w.get("workflow"), dict) else w
        for n in (w.get("nodes") or []):
            ct=n.get("type") or n.get("class_type") or ""
            nodes[ct]+=1
            for v in (n.get("widgets_values") or []):
                if isinstance(v,str) and (v.endswith(".safetensors") or v.endswith(".pth") or v.endswith(".ckpt")):
                    models.add(v)
        time.sleep(0.3)
    print("  node:", ", ".join(f"{k}x{v}" for k,v in nodes.most_common(9)))
    if models: print("  model:", ", ".join(sorted(models)[:8]))
