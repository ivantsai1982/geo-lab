"""Lint the popular edition: forbidden attribution, vendor names, and every number must
exist in the matching research-edition chapter (popular edition may not add numbers)."""
import re, glob, os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
REGIONAL = ["台北", "台灣", "新台幣", "便利商店", "超商", "CP值", "CP 值", "踩雷", "打臉", "佛系", "超夯", "母湯", "很頂", "芭樂", "傻眼", "揪團", "阿嬤", "夜市", "捷運", "機車", "粉專", "臉書", "Line 群", "蝦皮", "PChome", "momo"]
BAD = [r"貼文", r"帖子", r"網友", r"arXiv", r"\bDOI\b", r"\d{4}\.\d{4,5}", r"\b[cp]_[a-z0-9]{6,8}\b"]
sd = json.load(open(R + "data/full/s4/softad_flags.json", encoding="utf-8"))
PLATFORMS = {"youtube", "linkedin", "wikipedia", "wordpress", "google", "chatgpt", "openai", "reddit", "gemini",
             "perplexity", "claude", "bing", "amazon", "quora", "medium", "g2", "cloudflare", "shopify", "forbes"}
vendors = sorted({b for _, a, b, *_ in sd["author_brand"]} - PLATFORMS)
core = lambda n: re.sub(r"[^\d.]", "", n)
for f in sorted(glob.glob(R + "book/zh-hant/第*章_*.md")):
    ch = int(re.search(r"第(\d+)章", os.path.basename(f)).group(1))
    src = glob.glob(R + (f"book/research-zh-hant/第{ch:02d}章_*.md" if ch < 16 else "book/research-zh-hant/附錄A_*.md"))
    ref = open(src[0], encoding="utf-8").read().replace(",", "") if src else ""
    t = open(f, encoding="utf-8").read()
    issues = []
    for b in BAD + ([] if ch == 15 else [r"Reddit"]):
        for m in re.finditer(b, t, flags=re.I):
            issues.append(f"禁詞 {m.group(0)!r}: …{t[max(0, m.start()-20):m.end()+20]}…".replace("\n", " "))
    for w in REGIONAL:
        for m in re.finditer(re.escape(w), t):
            issues.append(f"地區用語 {w!r}: …{t[max(0, m.start()-15):m.end()+15]}…".replace("\n", " "))
    flat = re.sub(r"[^a-z0-9]", "", t.lower())
    for v in vendors:
        if len(v) >= 5 and v in flat: issues.append(f"業者名? {v}")
    nums = set(re.findall(r"\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*倍|\d{2,}(?:,\d{3})*(?:\.\d+)?", t))
    miss = sorted(n for n in nums if core(n) and core(n) not in ref and not re.fullmatch(r"20[12]\d", core(n)))
    wc = len(re.sub(r"\s", "", t))
    print(f"== {os.path.basename(f)}  字數 {wc}  問題 {len(issues)}  研究版無此數字 {len(miss)}")
    for x in issues[:10]: print("   ", x)
    if miss: print("    數字待查:", miss[:30])
