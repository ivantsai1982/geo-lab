"""Build one evidence pack per textbook chapter (no model calls).
Each pack: framework section + full notes of papers cited there + practitioner evidence
(R-A/B/C non-ad full text, R-D sample with numbers/artifacts), community consensus clusters,
and commercial leads (marked, not usable as evidence). Split into files <= 55k chars.
Output: book/research-zh-hant/_證據包/chNN_partK.md
"""
import json, re, glob, collections, os, sys
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
OUT = R + "book/research-zh-hant/_證據包/"; os.makedirs(OUT, exist_ok=True)
fw = open(R + "framework/03_geo-textbook-framework_v1.md", encoding="utf-8").read()
notes = {n["id"]: n for n in json.load(open(R + "papers/_notes/all_notes.json", encoding="utf-8"))}
items = {}
for f in glob.glob(R + "data/full/s2/in_A_*.json"):
    for x in json.load(open(f, encoding="utf-8")): items[x["id"]] = x
F = {o["id"]: o for o in map(json.loads, open(R + "data/full/s2/final_items.jsonl", encoding="utf-8"))}
sd = json.load(open(R + "data/full/s4/softad_flags.json", encoding="utf-8"))
flags, rep = sd["flags"], set(sd["reposts"])
cons = json.load(open(R + "data/full/s5/consensus.json", encoding="utf-8"))

# chapter -> (framework heading, F13 topics, F15 case filter)
CH = {
    0: ("第 0 章", [], None), 1: ("第 1 章", [13], None), 2: ("第 2 章", [1], None),
    3: ("第 3 章", [2], None), 4: ("第 4 章", [3], None), 5: ("第 5 章", [4], None),
    6: ("第 6 章", [5], None), 7: ("第 7 章", [6], None), 8: ("第 8 章", [7], None),
    9: ("第 9 章", [8, 14], None), 10: ("第 10 章", [9], None), 11: ("第 11 章", [10], None),
    12: ("第 12 章", [11], None), 13: ("第 13 章", [], "品牌推薦"), 14: ("第 14 章", [], "內容網站"),
    15: ("第 15 章", [12], None), 99: ("附錄 A", [], None),
}
secs = re.split(r"\n(?=## )", fw)
def section(h): return next((s for s in secs if s.startswith("## " + h)), "")
LV = ("R-A", "R-B", "R-C")
ok = lambda i, o: not o["未決"] and i not in flags and i not in rep
topic_of = lambda o: o["F13"] if isinstance(o["F13"], int) else None
case_of = lambda o: (o.get("F15") or "無").split(":")[0]


def item_block(i, n=1500):
    o, x = F[i], items[i]
    head = f"[{i}] 等級 {o['level']}｜類型 {o['F12']}｜日期 {x.get('date')}｜主張：{o.get('F14')}"
    ctx = f"\n上下文：{x['context'][:300]}" if x.get("context") else ""
    title = f"\n標題：{x['title']}" if x.get("title") else ""
    return f"{head}{title}{ctx}\n原文：{(x.get('text') or '')[:n]}\n"


def build(ch):
    h, topics, case = CH[ch]
    sec = section(h)
    ids = sorted(set(re.findall(r"\d{4}\.\d{4,5}", sec)))
    if ch == 99: ids = sorted(set(re.findall(r"\d{4}\.\d{4,5}", section("附錄 A"))))
    KW = {0: ["證據", "方法", "評估", "測量", "LLM 評判", "重複"], 13: ["品牌", "推薦", "產品", "電商", "購物"],
          14: ["出版", "新聞", "內容網站", "流量", "點擊", "publisher"]}
    if ch in KW and len(ids) < 8:
        rank = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        extra = [n["id"] for n in notes.values() if n["id"] not in ids
                 and any(k in json.dumps(n, ensure_ascii=False) for k in KW[ch])]
        extra.sort(key=lambda i: rank.get(notes[i]["evidence"], 5))
        ids = ids + extra[:15]
    paper = "\n".join(json.dumps(notes[p], ensure_ascii=False) for p in ids if p in notes)
    sel = lambda o: (topic_of(o) in topics) if topics else (case and case_of(o) == case)
    hi = [i for i, o in F.items() if ok(i, o) and o["level"] in LV and sel(o)]
    rd = [i for i, o in F.items() if ok(i, o) and o["level"] == "R-D" and sel(o)
          and (int(o.get("F2") or 0) or int(o.get("F7") or 0))]
    rd = sorted(rd, key=lambda i: -len(items[i].get("text") or ""))[:60]
    leads = [i for i, o in F.items() if o["level"] in LV and i in flags and sel(o)][:25]
    cc = [c for c in cons if (c["topic"] in topics if topics else False) and c["verdict"] != "樣本不足"]
    if ch in (0, 1, 99): cc = [c for c in cons if c["verdict"] == "共識支持"][:40] if ch == 1 else []
    parts = [f"# 第 {ch} 章證據包\n\n## A. 框架中本章的內容\n\n{sec}\n\n## B. 本章引用論文的精讀筆記（JSON，每行一篇）\n\n{paper}\n"]
    body = [f"\n## C. 從業者高證據內容（R-A/R-B/R-C，已排除推銷），共 {len(hi)} 條\n\n"] + [item_block(i) for i in hi]
    body += [f"\n## D. 一手觀察（R-D，含數字或證據物件），{len(rd)} 條，只能作為線索或例子\n\n"] + [item_block(i, 700) for i in rd]
    body += [f"\n## E. 社群主張與共識（每位作者一票；共識≠正確）\n\n"]
    for c in cc:
        hi_ids = [x["id"] for x in c["items"] if x["level"] in LV and x["stance"] in ("支持", "反對")][:5]
        body.append(f"- [群{c['cluster']}] {c['verdict']}｜支持 {c['support_authors']} / 反對 {c['oppose_authors']} 位作者｜{c['canonical']}｜高證據條目：{hi_ids}\n")
    body += [f"\n## F. 待查線索（作者與提及品牌有商業關係，不可作為證據或案例）\n\n"] + [item_block(i, 400) for i in leads]
    text = parts[0] + "".join(body)
    chunks, cur = [], ""
    for line in text.split("\n"):
        if len(cur) + len(line) > 55000: chunks.append(cur); cur = ""
        cur += line + "\n"
    chunks.append(cur)
    for k, c in enumerate(chunks, 1):
        open(f"{OUT}ch{ch:02d}_part{k}.md", "w", encoding="utf-8").write(c)
    return len(ids), len(hi), len(rd), len(cc), len(leads), len(chunks)


for ch in CH:
    print(ch, "papers/hi/rd/consensus/leads/files", build(ch))
