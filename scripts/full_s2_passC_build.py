"""S2 pass C: blind third annotation of items where pass A and B disagree on
evidence level, F1, F10, F11 or F12. Opus + codebook A wording (A used Sonnet+A,
B used Opus+B), so every coder/codebook combination differs. Final value per field
= majority of the three codings."""
import json
D = "G:/學習雜亂/GEO學習/data/full/s2/"
items = {}
import glob
for f in sorted(glob.glob(D + "in_A_*.json")):
    for x in json.load(open(f, encoding="utf-8")): items[x["id"]] = x
dis = [d["id"] for d in json.load(open(D + "disagreements_triage.json", encoding="utf-8"))]
order = [i for i in items if i in set(dis)]
files, cur, size = [], [], 0
for i in order:
    x = items[i]; s = len(json.dumps(x, ensure_ascii=False))
    if cur and (len(cur) >= 60 or size + s > 60000): files.append(cur); cur, size = [], 0
    cur.append(x); size += s
if cur: files.append(cur)
for k, ch in enumerate(files):
    t, s = divmod(k, 3)
    json.dump(ch, open(f"{D}in_C_{t:03d}{'abc'[s]}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("items", len(order), "files", len(files), "tasks", (len(files) + 2) // 3)
