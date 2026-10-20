"""S4 soft-ad detection by statistics (no hand-set cut-offs).
1) Author-brand concentration: for every author with >=3 brand-mentioning items, and every
   brand they mention >=2 times, one-sided binomial test of their mention count against the
   brand's share among all OTHER authors' brand-mentioning items. Benjamini-Hochberg over
   all tests, q<0.05, and the mentions must span >=2 threads -> the pair is flagged.
2) Near-duplicate templates: word 5-shingle Jaccard between items in DIFFERENT threads.
   Threshold = 99.9th percentile of Jaccard over 50,000 random item pairs (seed fixed).
3) Coded signals (reliable fields): F12=服務推銷, F10=1 (call to action).
An item is excluded from the citation list if any of 1-3 applies; reasons are kept.
Output: data/full/s4/softad_flags.json, data/full/s4/軟廣告檢驗報告.md
"""
import json, re, sqlite3, random, collections, os, sys
from scipy.stats import binomtest
import numpy as np
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
S2 = R + "data/full/s2/"; OUT = R + "data/full/s4/"; os.makedirs(OUT, exist_ok=True)

items = {}
import glob
for f in sorted(glob.glob(S2 + "in_A_*.json")):
    for x in json.load(open(f, encoding="utf-8")): items[x["id"]] = x
final = {o["id"]: o for o in map(json.loads, open(S2 + "final_items.jsonl", encoding="utf-8"))}

db = sqlite3.connect(R + "data/reddit.db")
author, thread = {}, {}
for pid, a in db.execute("select id, author from posts"):
    author["p_" + pid] = a; thread["p_" + pid] = pid
for cid, a, pid in db.execute("select id, author, post_id from comments"):
    author["c_" + cid] = a; thread["c_" + cid] = pid
miss = [i for i in final if i not in author]
print("items", len(final), "without author", len(miss))

norm = lambda b: re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", str(b).lower())
BAD = {"", "deleted", "[deleted]", "automoderator", "none"}

# ---- 1) author-brand concentration
by_author = collections.defaultdict(list)
for i, o in final.items():
    a = author.get(i)
    brands = {norm(b) for b in (o.get("F9") or []) if norm(b)}
    if a and a.lower() not in BAD and brands:
        by_author[a].append((i, brands))
brand_items = [(author.get(i), {norm(b) for b in (o.get("F9") or []) if norm(b)})
               for i, o in final.items() if o.get("F9")]
tot = len(brand_items)
brand_cnt = collections.Counter(b for _, bs in brand_items for b in bs)
author_brand_cnt = collections.defaultdict(collections.Counter)
for a, bs in brand_items:
    for b in bs: author_brand_cnt[a][b] += 1
tests = []
for a, lst in by_author.items():
    n = len(lst)
    if n < 3: continue
    c = collections.Counter(b for _, bs in lst for b in bs)
    for b, k in c.items():
        if k < 2: continue
        other_tot = tot - n
        other_b = brand_cnt[b] - author_brand_cnt[a][b]
        p0 = max(other_b, 0.5) / max(other_tot, 1)
        p = binomtest(k, n, p0, alternative="greater").pvalue
        ths = {thread[i] for i, bs in lst if b in bs}
        tests.append((p, a, b, k, n, len(ths)))
tests.sort()
m = len(tests); flagged_pairs = []
# BH step-up
cut = 0
for r, t in enumerate(tests, 1):
    if t[0] <= 0.05 * r / m: cut = r
def commercial(o):
    return int(o.get("F10") or 0) == 1 or int(o.get("F11") or 0) == 1 or o.get("F12") == "服務推銷"
for t in tests[:cut]:
    _, a, b = t[:3]
    link = any(commercial(final[i]) for i, bs in by_author[a] if b in bs)
    if t[5] >= 2 and link: flagged_pairs.append(t)
fp = {(a, b) for _, a, b, *_ in flagged_pairs}
print("author-brand tests", m, "BH-significant", cut, "flagged (>=2 threads)", len(flagged_pairs))

# ---- 2) near-duplicate templates
def shingles(t):
    w = re.findall(r"\w+", (t or "").lower())
    return {" ".join(w[j:j + 5]) for j in range(len(w) - 4)} if len(w) >= 30 else set()
sh = {i: shingles(items[i].get("text")) for i in final}
sh = {i: s for i, s in sh.items() if s}
ids = list(sh)
jac = lambda x, y: len(x & y) / len(x | y)
rng = random.Random(20260930)
null = [jac(sh[a], sh[b]) for a, b in (rng.sample(ids, 2) for _ in range(50000))]
thr_null = float(np.percentile(null, 99.9))
inv = collections.defaultdict(list)
for i, s in sh.items():
    for g in s: inv[g].append(i)
pair_hits = collections.Counter()
for g, lst in inv.items():
    if 2 <= len(lst) <= 50:
        for x in range(len(lst)):
            for y in range(x + 1, len(lst)):
                pair_hits[(lst[x], lst[y])] += 1
cand = []
for (x, y), h in pair_hits.items():
    if h >= 3 and thread.get(x) != thread.get(y):
        j = jac(sh[x], sh[y])
        if j > thr_null: cand.append((x, y, round(j, 3)))
# candidate-pair Jaccard is bimodal (incidental overlap vs copies); threshold = density
# minimum between the two modes (histogram, 20 bins, search 0.2-0.8)
hist, edges = np.histogram([c[2] for c in cand], bins=20, range=(0, 1))
lo, hi = 4, 16
k = lo + int(np.argmin(hist[lo:hi])); thr = float(edges[k])
dups = [c for c in cand if c[2] >= thr]
same_author = [c for c in dups if author.get(c[0]) == author.get(c[1])]
templ = [c for c in dups if author.get(c[0]) != author.get(c[1])]
dup_items = {i for x, y, _ in templ for i in (x, y)}
# same-author reposts: keep the earliest, mark others as duplicates (not ads)
repost = set()
for x, y, _ in same_author:
    later = max((x, y), key=lambda i: items[i].get("date") or "")
    repost.add(later)
print("null p99.9", round(thr_null, 4), "valley threshold", thr, "dup pairs", len(dups), "same-author", len(same_author), "template pairs", len(templ), "template items", len(dup_items), "reposts", len(repost))

# ---- combine
flags = {}
for i, o in final.items():
    r = []
    if o.get("F12") == "服務推銷": r.append("服務推銷")
    if int(o.get("F10") or 0) == 1: r.append("引導動作")
    a = author.get(i)
    if any((a, norm(b)) in fp for b in (o.get("F9") or [])): r.append("作者品牌集中")
    if i in dup_items: r.append("不同作者模板")
    if r: flags[i] = r
json.dump({"flags": flags, "reposts": sorted(repost), "author_brand": flagged_pairs, "near_dup_pairs": dups, "near_dup_threshold": thr},
          open(OUT + "softad_flags.json", "w", encoding="utf-8"), ensure_ascii=False)

lv = collections.Counter(); lv_ex = collections.Counter()
for i, o in final.items():
    lv[o["level"]] += 1
    if i in flags: lv_ex[o["level"]] += 1
reason = collections.Counter(x for r in flags.values() for x in r)
rep = ["# S4 軟廣告統計檢驗報告", "",
       f"- 條目 {len(final)}；被標為軟廣告或推銷的 {len(flags)} 條",
       f"- 原因分佈：{dict(reason)}",
       f"- 作者－品牌集中度：共檢驗 {m} 組，BH 校正後顯著 {cut} 組，其中跨 ≥2 串 {len(flagged_pairs)} 組",
       f"- 近重複：隨機配對 Jaccard 第 99.9 百分位為 {thr_null:.4f}（幾乎為 0，不能單獨作門檻）；候選配對的相似度呈雙峰，取兩峰之間密度最低點 {thr:.2f} 為門檻",
       f"- 跨串近重複 {len(dups)} 對：同一作者重複貼文 {len(same_author)} 對（去重，保留最早一份，共 {len(repost)} 條標為重複），不同作者模板 {len(templ)} 對（涉及 {len(dup_items)} 條，標為軟廣告）",
       "- 作者－品牌集中：在 BH 顯著且跨 ≥2 串之外，還要求該作者提及該品牌的內容中至少一條帶引導動作、利益披露或被判為服務推銷（有商業關係的證據）", "",
       "| 證據等級 | 總數 | 被排除 | 保留 |", "|---|---|---|---|"]
for k in ["R-A", "R-B", "R-C", "R-D", "R-E"]:
    rep.append(f"| {k} | {lv[k]} | {lv_ex[k]} | {lv[k]-lv_ex[k]} |")
rep += ["", "## 顯著的作者－品牌組合（前 30）", "", "| 品牌 | 提及次數/該作者品牌帖數 | 串數 | p |", "|---|---|---|---|"]
for p, a, b, k, n, t in flagged_pairs[:30]:
    rep.append(f"| {b} | {k}/{n} | {t} | {p:.2e} |")
open(OUT + "軟廣告檢驗報告.md", "w", encoding="utf-8").write("\n".join(rep))
print("\n".join(rep[:12]))
