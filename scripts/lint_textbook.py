"""Lint textbook chapters for forbidden attribution and unverifiable numbers.
- Forbidden in prose: Reddit/貼文/帖子/網友/論壇/r/xxx (ch15 may name Reddit as a platform), arXiv, DOI,
  paper-ID patterns, item ids (c_xxx/p_xxx), cluster ids, vendor names flagged as commercial leads.
- Numbers: every number with % or a unit-like context in the chapter is checked against the chapter's
  evidence pack text; numbers not found anywhere in the pack are listed for review.
"""
import re, glob, os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
BAD = [r"貼文", r"帖子", r"網友", r"論壇", r"\br/\w+", r"arXiv", r"\bDOI\b", r"\d{4}\.\d{4,5}", r"\b[cp]_[a-z0-9]{6,8}\b", r"群\d+"]
sd = json.load(open(R + "data/full/s4/softad_flags.json", encoding="utf-8"))
vendors = sorted({b for _, a, b, *_ in sd["author_brand"]})
EXTRA = open(R + "papers/_notes/all_notes_compact.txt", encoding="utf-8").read() + open(R + "data/full/s5/主張共識報告.md", encoding="utf-8").read()
files = sorted(glob.glob(R + "book/research-zh-hant/第*章_*.md")) + sorted(glob.glob(R + "book/research-zh-hant/附錄*.md"))
for f in files:
    t = open(f, encoding="utf-8").read()
    m = re.search(r"第(\d+)章", os.path.basename(f))
    ch = int(m.group(1)) if m else 99
    pack = "".join(open(p, encoding="utf-8").read() for p in glob.glob(R + f"book/research-zh-hant/_證據包/ch{ch:02d}_part*.md"))
    issues = []
    for b in BAD + ([] if ch == 15 else [r"Reddit"]):
        for mm in re.finditer(b, t, flags=re.I):
            issues.append(f"禁詞 {mm.group(0)!r}: …{t[max(0, mm.start()-20):mm.end()+20]}…".replace("\n", " "))
    low = t.lower()
    for v in vendors:
        if len(v) >= 5 and re.search(r"(?<![a-z0-9])" + re.escape(v) + r"(?![a-z0-9])", re.sub(r"[^a-z0-9\u4e00-\u9fff ]", "", low)):
            issues.append(f"商業關係品牌名 {v!r}")
    nums = set(re.findall(r"\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*倍|\d{2,}(?:,\d{3})*(?:\.\d+)?", t))
    core = lambda n: re.sub(r"[^\d.]", "", n)
    hay = pack.replace(",", "") + EXTRA
    miss = [n for n in nums if core(n) and core(n) not in hay and not re.fullmatch(r"20[12]\d", core(n))]
    wc = len(re.sub(r"\s", "", t))
    print(f"== {os.path.basename(f)}  字數 {wc}  禁詞/品牌 {len(issues)}  證據包中找不到的數字 {len(miss)}")
    for x in issues[:15]: print("   ", x)
    if miss: print("    數字待查:", sorted(miss)[:40])
