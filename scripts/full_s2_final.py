"""S2 final labels per item.
- Item coded only in pass A: A's labels.
- Coded in A and B: fields where A==B take that value; for items sent to pass C,
  each triage field takes the majority of A/B/C. If all three differ (possible only
  for F12), the item is flagged 未決 and excluded from the citation list.
- Non-triage fields (F9, F13, F13b, F14, F15, F16): take B when B exists (Opus), else A;
  these fields only organise content and never decide inclusion.
- Evidence level is recomputed from the final F-fields by the fixed rule.
Output: data/full/s2/final_items.jsonl, summary printed.
"""
import json, glob, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
D = "G:/學習雜亂/GEO學習/data/full/s2/"
TRIAGE = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F10", "F11", "F12"]


def level(F):
    g = lambda k: int(F.get(k) or 0)
    if g("F1") and g("F2") and g("F3") and g("F4") and g("F5") and g("F6"): return "R-A"
    if g("F1") and g("F2") and g("F3") and g("F6"): return "R-B"
    if g("F1") and g("F7") and g("F6"): return "R-C"
    if g("F1"): return "R-D"
    return "R-E"


def load(p):
    d = {}
    for f in sorted(glob.glob(D + p)):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                o = json.loads(l); d[o["id"]] = o
    return d


A, B, C = load("out_A_*.jsonl"), load("out_B_*.jsonl"), load("out_C_*.jsonl")
sent_c = {d["id"] for d in json.load(open(D + "disagreements_triage.json", encoding="utf-8"))}
missing_c = sorted(sent_c - set(C))
print("A", len(A), "B", len(B), "C", len(C), "sent_to_C", len(sent_c), "missing_C", len(missing_c))

stats = collections.Counter(); final = []
for i, a in A.items():
    b, c = B.get(i), C.get(i)
    coders = [x for x in (a, b, c) if x is not None]
    o = dict(b or a); o["id"] = i; o["coders"] = "A" + ("B" if b else "") + ("C" if c else "")
    for k in TRIAGE:  # descriptive fields: majority if 3 coders, else B (Opus) if present
        vals = [x.get(k) for x in coders]
        v, n = collections.Counter(vals).most_common(1)[0]
        o[k] = v if n >= 2 else (b or a).get(k)
    # evidence level: majority of the coders' own derived levels (fixed rule per coder)
    lv = [level(x) for x in coders]
    v, n = collections.Counter(lv).most_common(1)[0]
    unresolved = []
    if len(coders) == 1 or n >= 2 or (len(coders) == 2 and lv[0] == lv[1]):
        o["level"] = v if len(coders) != 2 or lv[0] == lv[1] else level(o)
    else:
        o["level"] = level(o); unresolved.append("level")
    f12 = collections.Counter(x.get("F12") for x in coders).most_common(1)[0]
    if len(coders) == 3 and f12[1] < 2: unresolved.append("F12")
    o["未決"] = unresolved
    stats[o["level"]] += 1
    if unresolved: stats["未決"] += 1
    final.append(o)

with open(D + "final_items.jsonl", "w", encoding="utf-8") as w:
    for o in final: w.write(json.dumps(o, ensure_ascii=False) + "\n")
print(dict(stats))
print("F12", collections.Counter(o["F12"] for o in final).most_common())
print("R-A/B/C non-ad candidates:",
      sum(1 for o in final if o["level"] in ("R-A", "R-B", "R-C") and not o["未決"]))
