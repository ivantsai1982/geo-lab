import json, glob, os, sys
D = "G:/學習雜亂/GEO學習/data/full/s2/"
p = sys.argv[1] if len(sys.argv) > 1 else "A"
done, partial, bad = [], [], []
for t in range(176):
    ok = True; any_ = False
    for s in "abc":
        fi = f"{D}in_{p}_{t:03d}{s}.json"
        if not os.path.exists(fi): continue
        fo = f"{D}out_{p}_{t:03d}{s}.jsonl"
        if not os.path.exists(fo): ok = False; continue
        any_ = True
        ids_in = [x["id"] for x in json.load(open(fi, encoding="utf-8"))["items"]] if isinstance(json.load(open(fi, encoding="utf-8")), dict) else [x["id"] for x in json.load(open(fi, encoding="utf-8"))]
        try:
            ids_out = [json.loads(l)["id"] for l in open(fo, encoding="utf-8") if l.strip()]
        except Exception as e:
            bad.append(f"{t:03d}{s}:json"); ok = False; continue
        if set(ids_out) != set(ids_in): bad.append(f"{t:03d}{s}:{len(ids_out)}/{len(ids_in)}"); ok = False
    (done if ok else partial if any_ else []).append(t)
print("done", len(done)); print("partial", partial); print("bad", bad)
print("missing", [t for t in range(176) if t not in done and t not in partial])
