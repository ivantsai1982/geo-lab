"""S2 pass B: merge pass-A outputs, select subset for double annotation, build input files.

Selection (fixed before seeing pass-B results):
  - pass A F1=1 (first-hand; covers every item with evidence level >= R-D), or
  - pass A F12 in {實測, 服務推銷, 工具討論}, plus
  - a 10% simple random sample (seed 20260930) of all remaining items, to estimate
    how many relevant items pass A missed.
Output: data/full/s2/passA_all.jsonl, passB_selection.json, in_B_NNN{a,b,c}.json
"""
import json, glob, os, random

D = "G:/學習雜亂/GEO學習/data/full/s2/"
MAX_ITEMS, MAX_CHARS, PER_TASK = 60, 60000, 3
TYPES = {"實測", "服務推銷", "工具討論"}


def level(F):
    if F["F1"] and F["F2"] and F["F3"] and F["F4"] and F["F5"] and F["F6"]: return "R-A"
    if F["F1"] and F["F2"] and F["F3"] and F["F6"]: return "R-B"
    if F["F1"] and F["F7"] and F["F6"]: return "R-C"
    if F["F1"]: return "R-D"
    return "R-E"


items = {}
for f in sorted(glob.glob(D + "in_A_*.json")):
    for x in json.load(open(f, encoding="utf-8")):
        items[x["id"]] = x

A = {}
for f in sorted(glob.glob(D + "out_A_*.jsonl")):
    for l in open(f, encoding="utf-8"):
        if l.strip():
            o = json.loads(l); o["level"] = level(o); A[o["id"]] = o

missing = [i for i in items if i not in A]
print("items", len(items), "annotated", len(A), "missing", len(missing))
with open(D + "passA_all.jsonl", "w", encoding="utf-8") as w:
    for i in items:
        if i in A: w.write(json.dumps(A[i], ensure_ascii=False) + "\n")

core = [i for i in items if i in A and (A[i]["F1"] == 1 or A[i]["F12"] in TYPES)]
rest = [i for i in items if i in A and i not in set(core)]
random.seed(20260930)
rand = random.sample(rest, round(len(rest) * 0.10))
sel = set(core) | set(rand)
order = [i for i in items if i in sel]  # keep thread order
json.dump({"core": core, "random": rand, "rule": __doc__}, open(D + "passB_selection.json", "w", encoding="utf-8"), ensure_ascii=False)
print("core", len(core), "random", len(rand), "total", len(order))

files, cur, size = [], [], 0
for i in order:
    x = items[i]; s = len(json.dumps(x, ensure_ascii=False))
    if cur and (len(cur) >= MAX_ITEMS or size + s > MAX_CHARS):
        files.append(cur); cur, size = [], 0
    cur.append(x); size += s
if cur: files.append(cur)
for k, chunk in enumerate(files):
    t, s = divmod(k, PER_TASK)
    json.dump(chunk, open(f"{D}in_B_{t:03d}{'abc'[s]}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("files", len(files), "tasks", (len(files) + PER_TASK - 1) // PER_TASK)
