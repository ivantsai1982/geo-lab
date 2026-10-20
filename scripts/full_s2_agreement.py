"""S2 full run: agreement between pass A (Sonnet/codebook A) and pass B (Opus/codebook B).
Krippendorff's alpha (nominal), bootstrap 95% CI by multinomial resampling of the
coincidence cells (equivalent to resampling item pairs). Thresholds as in the pilot
(Krippendorff 2004): >=0.800 reliable, 0.667-0.800 tentative, <0.667 not usable.
Reported separately for the rule-selected subset ("core") and the 10% random subset,
plus the pass-A miss rate estimated from the random subset.
Outputs: data/full/s2/一致性報告_S2.md, disagreements_triage.json (items for a 3rd annotation).
"""
import json, glob, collections, sys
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
D = "G:/學習雜亂/GEO學習/data/full/s2/"
TYPES = {"實測", "服務推銷", "工具討論"}
TRIAGE = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F10", "F11", "F12", "level"]


def level(F):
    g = lambda k: int(F.get(k) or 0)
    if g("F1") and g("F2") and g("F3") and g("F4") and g("F5") and g("F6"): return "R-A"
    if g("F1") and g("F2") and g("F3") and g("F6"): return "R-B"
    if g("F1") and g("F7") and g("F6"): return "R-C"
    if g("F1"): return "R-D"
    return "R-E"


def load(pat):
    d = {}
    for f in sorted(glob.glob(D + pat)):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                o = json.loads(l); o["level"] = level(o); d[o["id"]] = o
    return d


def alpha_from(labels, pairs):
    idx = {v: i for i, v in enumerate(labels)}
    M = np.zeros((len(labels), len(labels)))
    for a, b in pairs:
        M[idx[a], idx[b]] += 1; M[idx[b], idx[a]] += 1
    return M


def alpha_M(M):
    n = M.sum()
    if n <= 1: return float("nan")
    nc = M.sum(1)
    Do = (n - np.trace(M)) / n
    De = (n * n - (nc ** 2).sum()) / (n * (n - 1))
    return 1.0 if De == 0 else 1 - Do / De


def stat(pairs, B=2000, seed=0):
    labels = sorted({x for p in pairs for x in p}, key=str)
    M = alpha_from(labels, pairs)
    a = alpha_M(M)
    # resample item pairs: multinomial over ordered pair cells
    cells = collections.Counter(pairs)
    keys = list(cells); p = np.array([cells[k] for k in keys], float); p /= p.sum()
    rng = np.random.default_rng(seed); vals = []
    for draw in rng.multinomial(len(pairs), p, size=B):
        M2 = alpha_from(labels, [])
        for k, c in zip(keys, draw):
            if c:
                i, j = labels.index(k[0]), labels.index(k[1])
                M2[i, j] += c; M2[j, i] += c
        v = alpha_M(M2)
        if v == v: vals.append(v)
    vals.sort()
    lo, hi = (vals[int(.025 * len(vals))], vals[int(.975 * len(vals))]) if vals else (float("nan"),) * 2
    agree = sum(x == y for x, y in pairs) / len(pairs)
    return a, lo, hi, agree


def verdict(a, lo):
    if a != a: return "無法計算"
    if lo >= 0.8: return "可靠"
    if a >= 0.8: return "可靠(CI下界<0.8)"
    if a >= 0.667: return "試探性"
    return "不合格"


A, Bp = load("out_A_*.jsonl"), load("out_B_*.jsonl")
sel = json.load(open(D + "passB_selection.json", encoding="utf-8"))
core, rand = set(sel["core"]), set(sel["random"])
common = set(A) & set(Bp)
print(f"A={len(A)} B={len(Bp)} common={len(common)} core={len(core)} random={len(rand)}")

b01 = lambda v: 1 if v in (1, "1", True) else 0
fields = {k: (lambda o, k=k: b01(o.get(k))) for k in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F10", "F11"]}
fields["F9有無品牌"] = lambda o: int(bool(o.get("F9")))
fields["F12類型"] = lambda o: o.get("F12")
fields["F13主議題"] = lambda o: "新主題" if isinstance(o.get("F13"), str) else o.get("F13")
fields["F14有無主張"] = lambda o: int((o.get("F14") or "無") != "無")
fields["F15案例"] = lambda o: (o.get("F15") or "無").split(":")[0]
fields["F16第三方"] = lambda o: int(bool((o.get("F16") or "").strip()))
fields["證據等級"] = lambda o: o["level"]
fields["收錄候選(R-A/B/C)"] = lambda o: int(o["level"] in ("R-A", "R-B", "R-C"))

out = ["# S2 全量逐條標註：一致性報告", "",
       f"- 第一遍（Sonnet，手冊 A）：{len(A)} 條；第二遍（Opus，手冊 B）：{len(Bp)} 條；兩遍都有：{len(common)} 條",
       f"- 第二遍樣本 = 規則選中 {len(core)} 條 + 隨機 {len(rand)} 條", "",
       "判定：α≥0.800 可靠；0.667–0.800 試探性；<0.667 不合格（Krippendorff 2004）。", ""]
def weighted_stat(pc, pr, w, B=1000, seed=1):
    """Population estimate: core stratum weight 1, random stratum weight w (inverse sampling prob).
    Stratified bootstrap (resample each stratum separately)."""
    labels = sorted({x for p in pc + pr for x in p}, key=str)
    li = {v: i for i, v in enumerate(labels)}

    def mat(cc, cr):
        M = np.zeros((len(labels),) * 2)
        for cnt, wt in ((cc, 1.0), (cr, w)):
            for (a, b), c in cnt.items():
                M[li[a], li[b]] += c * wt; M[li[b], li[a]] += c * wt
        return M
    Cc, Cr = collections.Counter(pc), collections.Counter(pr)
    a = alpha_M(mat(Cc, Cr))
    rng = np.random.default_rng(seed); vals = []
    kc, kr = list(Cc), list(Cr)
    pcv = np.array([Cc[k] for k in kc], float) / len(pc)
    prv = np.array([Cr[k] for k in kr], float) / len(pr)
    for _ in range(B):
        dc = rng.multinomial(len(pc), pcv); dr = rng.multinomial(len(pr), prv)
        v = alpha_M(mat(dict(zip(kc, dc)), dict(zip(kr, dr))))
        if v == v: vals.append(v)
    vals.sort()
    return a, vals[int(.025 * len(vals))], vals[int(.975 * len(vals))]


n_rest = len(A) - len(core)
w = n_rest / max(len(common & rand), 1)
ic, ir = sorted(common & core), sorted(common & rand)
out += [f"## 全體估計（按抽樣機率加權：規則選中權重 1，隨機樣本權重 {w:.2f}）", "",
        "這一節代表全部 31,007 條內容上兩遍標註的一致程度，是判定字段可靠性的主要依據。", "",
        "| 字段 | α | 95% CI | 判定 |", "|---|---|---|---|"]
for k, f in fields.items():
    a, lo, hi = weighted_stat([(f(A[i]), f(Bp[i])) for i in ic], [(f(A[i]), f(Bp[i])) for i in ir], w)
    out.append(f"| {k} | {a:.3f} | [{lo:.3f}, {hi:.3f}] | {verdict(a, lo)} |")
out.append("")

ids = ic
out += [f"## 規則選中子集（n={len(ids)}，未加權）", "",
        "此子集由第一遍結果篩選而來，值域受限，α 僅供參考。", "",
        "| 字段 | α | 95% CI | 原始一致率 | 判定 |", "|---|---|---|---|---|"]
for k, f in fields.items():
    a, lo, hi, ag = stat([(f(A[i]), f(Bp[i])) for i in ids])
    out.append(f"| {k} | {a:.3f} | [{lo:.3f}, {hi:.3f}] | {ag:.3f} | {verdict(a, lo)} |")
out.append("")

# pass-A miss rate from the random subset
ids = sorted(common & rand)
relB = [i for i in ids if Bp[i]["F1"] == 1 or Bp[i]["F12"] in TYPES]
hiB = [i for i in ids if Bp[i]["level"] in ("R-A", "R-B", "R-C")]
n = len(ids)
out += ["## 第一遍漏判估計（隨機子集）", "",
        f"- 隨機子集 {n} 條本來都是第一遍判為「非一手、非實測/推銷/工具」的內容。",
        f"- 其中第二遍判為一手或實測/推銷/工具的：{len(relB)} 條（{len(relB)/max(n,1):.1%}）",
        f"- 其中第二遍判為 R-A/B/C 的：{len(hiB)} 條（{len(hiB)/max(n,1):.1%}）",
        f"- 推算到全部未入選的 {len(A)-len(core)} 條：約 {len(hiB)/max(n,1)*(len(A)-len(core)):.0f} 條高證據內容可能被第一遍漏掉", ""]

# disagreements on triage fields -> third annotation
dis = []
for i in sorted(common):
    diff = [k for k in TRIAGE if (A[i].get(k) != Bp[i].get(k))]
    if any(k in ("level", "F10", "F11", "F12") for k in diff) or ("F1" in diff):
        dis.append({"id": i, "diff": diff})
json.dump(dis, open(D + "disagreements_triage.json", "w", encoding="utf-8"), ensure_ascii=False)
out += ["## 需第三次標註的分歧", "",
        f"- 證據等級、F1、F10、F11 或 F12 任一不一致的條目：{len(dis)} 條（見 disagreements_triage.json）", ""]
open(D + "一致性報告_S2.md", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
