"""Traditional (neutral) -> Simplified Chinese edition. Pure conversion, no rewriting:
1) a hand-checked table of Taiwan->mainland vocabulary that has the SAME meaning (longest first);
2) OpenCC t2s (character-level only, no phrase rewriting);
3) corner quotes 「」『』 -> “” ‘’.
OpenCC tw2sp is deliberately NOT used: it mistranslates (查詢->查找, 指標->指针, 核心->内核).
Writes a substitution log so every vocabulary change can be audited.
"""
import opencc, glob, re, os, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
SRC, DST = R + "book/zh-hant/", R + "book/zh-hans/"
VOCAB = [  # (traditional source, simplified target) — same meaning only
    ("AI 代理可讀性", "智能体可读性"), ("AI 代理", "AI 智能体"),
    ("應用程式介面", "应用程序接口"), ("應用程式", "应用程序"), ("程式介面", "程序接口"),
    ("開發者介面", "开发者接口"), ("資料介面", "数据接口"), ("原始碼", "源代码"), ("程式碼", "代码"), ("結構化資料", "结构化数据"), ("訓練資料", "训练数据"),
    ("資料庫", "数据库"), ("資料夾", "文件夹"), ("行動裝置", "移动设备"), ("部落格", "博客"), ("部落客", "博主"),
    ("伺服器", "服务器"), ("搜尋", "搜索"), ("網路", "网络"), ("軟體", "软件"), ("硬體", "硬件"),
    ("資訊", "信息"), ("訊息", "信息"), ("訊號", "信号"), ("機率", "概率"), ("透過", "通过"),
    ("預設", "默认"), ("設定", "设置"), ("登入", "登录"), ("使用者", "用户"), ("影片", "视频"),
    ("螢幕", "屏幕"), ("貼文", "帖子"), ("品質", "质量"), ("演算法", "算法"), ("數位", "数字"),
    ("介面", "界面"), ("檔案", "文件"), ("線上", "在线"), ("回饋", "反馈"), ("支援", "支持"),
    ("專案", "项目"), ("行銷", "营销"), ("點閱", "点击"), ("最佳化", "优化"), ("載入", "加载"),
    ("儲存", "存储"), ("帳號", "账号"), ("帳戶", "账户"), ("範例", "示例"), ("視窗", "窗口"),
    ("選單", "菜单"), ("簡訊", "短信"), ("回覆", "回复"), ("連結", "链接"),
]
PROG = re.compile(r"(?<!方)程式")  # 程式 -> 程序, but never 方程式
ZHE_KEEP = ("顯著", "著名", "著作", "著重", "卓著", "土著", "著稱", "原著", "論著", "專著", "名著", "編著")
t2s = opencc.OpenCC("t2s")
os.makedirs(DST, exist_ok=True)
log = collections.Counter()


def convert(t):
    for a, b in VOCAB:
        n = t.count(a)
        if n: log[(a, b)] += n; t = t.replace(a, b)
    n = len(PROG.findall(t))
    if n: log[("程式", "程序")] += n; t = PROG.sub("程序", t)
    # 著 as aspect particle -> 着 (keep compound words listed above)
    keep = {w: f"\x00{k}\x00" for k, w in enumerate(ZHE_KEEP)}
    for w, ph in keep.items(): t = t.replace(w, ph)
    n = t.count("著"); t = t.replace("著", "着")
    if n: log[("著(助詞)", "着")] += n
    for w, ph in keep.items(): t = t.replace(ph, w)
    t = t2s.convert(t)
    for a, b in (("「", "“"), ("」", "”"), ("『", "‘"), ("』", "’")): t = t.replace(a, b)
    return t


files = sorted(glob.glob(SRC + "第*章_*.md")) + [SRC + "_術語表.md", SRC + "00_先讀這一頁.md"]
for f in files:
    name = t2s.convert(os.path.basename(f))
    open(DST + name, "w", encoding="utf-8", newline="\n").write(convert(open(f, encoding="utf-8").read()))
with open(DST + "_转换记录.md", "w", encoding="utf-8", newline="\n") as w:
    w.write("# 繁→简转换记录\n\n只做字形转换（OpenCC t2s）和下表中两岸同义用词替换，未改写任何句子。\n\n| 繁体原词 | 简体用词 | 次数 |\n|---|---|---|\n")
    for (a, b), n in log.most_common(): w.write(f"| {a} | {b} | {n} |\n")
print(len(files), "files;", sum(log.values()), "vocabulary substitutions")
for (a, b), n in log.most_common(): print(n, a, "->", b)
