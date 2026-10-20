"""S3 一致性檢驗：兩次獨立標註 (A=Sonnet/手冊A, B=Opus/手冊B) 的 Krippendorff's α（名義尺度）+ bootstrap 95% CI。
門檻（Krippendorff 2004）：α≥0.800 可靠；0.667–0.800 僅試探性；<0.667 定義不合格須重寫。"""
import json, glob, os, re, random, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'data', 'pilot')

def load(pat):
    d = {}
    for f in sorted(glob.glob(os.path.join(P, pat))):
        for line in open(f, encoding='utf-8'):
            line = line.strip()
            if not line: continue
            try: o = json.loads(line)
            except Exception: print('BAD JSON', f, line[:80]); continue
            d[o['id']] = o
    return d

def alpha(pairs):
    """pairs: list of (a,b) 名義值，兩個編碼者、無缺失"""
    pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
    n = 2 * len(pairs)
    if n == 0: return float('nan')
    cnt = collections.Counter(); o = collections.Counter()
    for a, b in pairs:
        cnt[a] += 1; cnt[b] += 1; o[(a, b)] += 1; o[(b, a)] += 1
    Do = sum(v for (a, b), v in o.items() if a != b) / n
    De = sum(cnt[a] * cnt[b] for a in cnt for b in cnt if a != b) / (n * (n - 1))
    return 1.0 if De == 0 else 1 - Do / De

def boot(pairs, B=2000, seed=0):
    r = random.Random(seed); vals = []
    for _ in range(B):
        s = [pairs[r.randrange(len(pairs))] for _ in pairs]
        v = alpha(s)
        if v == v: vals.append(v)
    vals.sort()
    return (vals[int(.025 * len(vals))], vals[int(.975 * len(vals))]) if vals else (float('nan'),) * 2

def verdict(a, lo):
    if a != a: return '無法計算'
    if lo >= 0.800: return '可靠'
    if a >= 0.800: return '可靠(CI下界<0.8)'
    if a >= 0.667: return '試探性'
    return '不合格→重寫定義'

def level(o):
    F = {k: int(o.get(k) or 0) for k in ['F1','F2','F3','F4','F5','F6','F7','F8']}
    if F['F1'] and F['F2'] and F['F3'] and F['F4'] and F['F5'] and F['F6']: return 'R-A'
    if F['F1'] and F['F2'] and F['F3'] and F['F6']: return 'R-B'
    if F['F1'] and (F['F7'] or F['F8']) and F['F6']: return 'R-C'
    if F['F1']: return 'R-D'
    return 'R-E'

A, B = load('out_items_A_*.jsonl'), load('out_items_B_*.jsonl')
ids = sorted(set(A) & set(B))
items = {x['id']: x for x in json.load(open(os.path.join(P, 'items_all.json'), encoding='utf-8'))}
print(f'條目：A={len(A)} B={len(B)} 共同={len(ids)} / 應有 {len(items)}')
rows = []
def report(name, pairs):
    a = alpha(pairs); lo, hi = boot(pairs)
    pos = sum(1 for x, y in pairs if x in (1, '1', True)) , sum(1 for x, y in pairs if y in (1, '1', True))
    agree = sum(x == y for x, y in pairs) / len(pairs)
    rows.append((name, a, lo, hi, agree, pos, verdict(a, lo)))
b01 = lambda v: 1 if v in (1, '1', True, 'true') else 0
for k in ['F1','F2','F3','F4','F5','F6','F7','F8','F10','F11']:
    report(k, [(b01(A[i].get(k)), b01(B[i].get(k))) for i in ids])
report('F9有無品牌', [(int(bool(A[i].get('F9'))), int(bool(B[i].get('F9')))) for i in ids])
report('F12類型', [(A[i].get('F12'), B[i].get('F12')) for i in ids])
def f13(o):
    s = set()
    for v in o.get('F13') or []:
        s.add('新主題' if isinstance(v, str) and v.startswith('新主題') else str(v).strip())
    return s
for lab in [str(x) for x in range(1, 11)] + ['新主題']:
    report(f'F13-{lab}', [(int(lab in f13(A[i])), int(lab in f13(B[i]))) for i in ids])
norm15 = lambda v: (v or '').split(':')[0]
report('F15案例', [(norm15(A[i].get('F15')), norm15(B[i].get('F15'))) for i in ids])
report('F14有無主張', [(int((A[i].get('F14') or '無') != '無'), int((B[i].get('F14') or '無') != '無')) for i in ids])
report('證據等級(推導)', [(level(A[i]), level(B[i])) for i in ids])

TA, TB = load('out_threads_A_*.jsonl'), load('out_threads_B_*.jsonl')
th = {x['id']: x for x in json.load(open(os.path.join(P, 'threads_all.json'), encoding='utf-8'))}
tids = sorted(set(TA) & set(TB))
print(f'討論串：A={len(TA)} B={len(TB)} 共同={len(tids)} / 應有 {len(th)}')
report('S1討論串分類', [(TA[i]['label'], TB[i]['label']) for i in tids])

print(f"\n{'字段':14s} {'α':>6s}  {'95%CI':>15s}  {'一致率':>6s}  {'陽性數A/B':>10s}  判定")
for name, a, lo, hi, ag, pos, v in rows:
    print(f'{name:14s} {a:6.3f}  [{lo:5.3f},{hi:5.3f}]  {ag:6.1%}  {str(pos):>10s}  {v}')

# F9 品牌集合一致性（Jaccard）
js = []
for i in ids:
    a = {x.lower().strip() for x in A[i].get('F9') or []}; b = {x.lower().strip() for x in B[i].get('F9') or []}
    if a or b: js.append(len(a & b) / len(a | b))
print(f'\nF9 品牌列表 Jaccard 平均（至少一方非空，n={len(js)}）: {sum(js)/max(1,len(js)):.3f}')

# S1：各層分佈 + 雙方都判 GEO 的比例；詞表召回參考
print('\nS1 各層標註分佈（A/B 一致時的標籤）：')
st = collections.defaultdict(collections.Counter)
for i in tids:
    st[th[i]['stratum']][TA[i]['label'] if TA[i]['label'] == TB[i]['label'] else '不一致'] += 1
for s, c in st.items(): print(' ', s, dict(c))

# 等級分佈 & 不一致明細輸出供審閱
dis = []
for i in ids:
    diff = {k: (A[i].get(k), B[i].get(k)) for k in ['F1','F2','F3','F4','F5','F6','F7','F8','F10','F11','F12']
            if (b01(A[i].get(k)), b01(B[i].get(k))) != (b01(B[i].get(k)), b01(A[i].get(k))) or A[i].get(k) != B[i].get(k)}
    if diff: dis.append(dict(id=i, diff=diff, text=items[i]['text'][:600], A14=A[i].get('F14'), B14=B[i].get('F14')))
json.dump(dis, open(os.path.join(P, 'disagreements.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n證據等級分佈 A:', collections.Counter(level(A[i]) for i in ids), ' B:', collections.Counter(level(B[i]) for i in ids))
print('不一致條目數', len(dis), '→ data/pilot/disagreements.json')
