"""Rebuild contents pages (titles, word counts, totals) and full-book files for every edition,
and the Simplified Chinese contents page and full book (converted from Traditional Chinese).
Run after editing chapters, and after scripts/to_simplified.py."""
import re, sys, glob, opencc
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
B = R + "book/"


def w(path, text):
    open(path, "w", encoding="utf-8", newline="\n").write(text.replace("\r\n", "\n").rstrip("\n") + "\n")


zh_count = lambda t: len(re.sub(r"\s", "", t))
en_count = lambda t: len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.,%-]*", t))
LINK = re.compile(r"^- \[(?P<title>[^\]]+)\]\((?P<file>[^)]+\.md)\)(?P<tail>.*)$")


def rebuild(d, toc, full, count, fmt, total_re, total_fmt):
    lines = open(d + toc, encoding="utf-8").read().split("\n")
    files, total = [], 0
    for i, l in enumerate(lines):
        m = LINK.match(l)
        if not m or not m.group("file").startswith(("第", "Chapter", "附錄", "Appendix")):
            continue
        body = open(d + m.group("file"), encoding="utf-8").read()
        title = body.split("\n", 1)[0].lstrip("# ").strip()
        c = count(body); total += c
        lines[i] = f"- [{title}]({m.group('file')}){fmt(c)}"
        files.append(m.group("file"))
    t = re.sub(total_re, total_fmt(total), "\n".join(lines))
    w(d + toc, t)
    w(d + full, "\n\n".join([t.rstrip()] + [open(d + f, encoding="utf-8").read().rstrip() for f in files]))
    print(d.split("book/")[1], len(files), "files, total", total)


zh = (lambda c: f"（約 {c:,} 字）", r"全書約 [\d,]+ 字", lambda n: f"全書約 {n:,} 字")
en = (lambda c: f" (about {c:,} words)", r"About [\d,]+ words in total", lambda n: f"About {n:,} words in total")
rebuild(B + "zh-hant/", "00_目錄.md", "AI為什麼不推薦你_全書.md", zh_count, *zh)
rebuild(B + "en/", "00_Contents.md", "Why_Doesnt_AI_Recommend_You_Full.md", en_count, *en)
rebuild(B + "research-zh-hant/", "00_目錄.md", "GEO教材_全書.md", zh_count, *zh)
rebuild(B + "research-en/", "00_Contents.md", "GEO_Lab_Research_Edition_Full.md", en_count, *en)

# Simplified Chinese contents page and full book, converted from the Traditional ones
sys.argv = ["x"]
sys.path.insert(0, R + "scripts")
import to_simplified as ts  # noqa: E402  (re-runs the chapter conversion, which is idempotent)
t2s = opencc.OpenCC("t2s")
S, D = B + "zh-hant/", B + "zh-hans/"
for name in ["00_目錄.md", "AI為什麼不推薦你_全書.md"]:
    t = ts.convert(open(S + name, encoding="utf-8").read())
    for f in glob.glob(S + "第*章_*.md") + [S + "00_先讀這一頁.md"]:
        b = f.replace("\\", "/").split("/")[-1]
        t = t.replace(ts.convert(b), t2s.convert(b))  # link targets must match converted file names
    w(D + t2s.convert(name), t)
print("zh-hans contents and full book rebuilt")
