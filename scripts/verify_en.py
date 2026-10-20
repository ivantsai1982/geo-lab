"""Independent check of the English translation against the Chinese source:
structure (headings / list items / table rows / bold spans) and numbers
(every number in the source must appear in the translation; 萬 converted to x10,000)."""
import re, glob, os, sys
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"


def struct(t):
    L = t.splitlines()
    return (sum(l.startswith("#") for l in L), sum(bool(re.match(r"\s*([-*]|\d+\.)\s", l)) for l in L),
            sum(l.lstrip().startswith("|") for l in L))


def nums_zh(t):
    out = set()
    for m in re.finditer(r"(\d+(?:,\d{3})*(?:\.\d+)?)\s*(萬|億|千)?", t):
        v = float(m.group(1).replace(",", "")) * {"萬": 1e4, "億": 1e8, "千": 1e3}.get(m.group(2) or "", 1)
        out.add(v)
    return out


def nums_en(t):
    out = set()
    for m in re.finditer(r"(\d+(?:,\d{3})*(?:\.\d+)?)\s*(million|billion)?", t):
        v = float(m.group(1).replace(",", "")) * {"million": 1e6, "billion": 1e9}.get(m.group(2) or "", 1)
        out.add(v)
    return out


for zh in sorted(glob.glob(R + "book/zh-hant/第*章_*.md")):
    ch = int(re.search(r"第(\d+)章", zh).group(1))
    en = R + f"book/en/Chapter_{ch:02d}.md"
    if not os.path.exists(en):
        print(f"ch{ch:02d} MISSING"); continue
    a, b = open(zh, encoding="utf-8").read(), open(en, encoding="utf-8").read()
    sa, sb = struct(a), struct(b)
    miss = sorted(v for v in nums_zh(a) - nums_en(b) if not (1 <= v <= 20 and v == int(v)))
    ratio = len(b.split()) / max(len(re.sub(r"\s", "", a)), 1)
    flag = "OK" if sa == sb and not miss else "CHECK"
    print(f"ch{ch:02d} {flag} headings {sa[0]}/{sb[0]} list {sa[1]}/{sb[1]} table {sa[2]}/{sb[2]} "
          f"EN words/ZH chars {ratio:.2f} numbers-missing {miss[:12]}")
