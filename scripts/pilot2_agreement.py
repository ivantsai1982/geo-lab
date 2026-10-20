"""第二輪試標一致性（手冊 v0.3）。Krippendorff α（名義）+ bootstrap 95% CI，並按抽樣層（隨機/富集）分列。"""
import json, glob, os, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
from pilot_agreement import alpha, boot, verdict, level
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'data', 'pilot2')
def load(pat):
    d = {}
    for f in sorted(glob.glob(os.path.join(P, pat))):
        for l in open(f, encoding='utf-8'):
            l = l.strip()
            if l:
                try: o = json.loads(l); d[o['id']] = o
                except Exception: print('BAD', f, l[:60])
    return d
A, B = load('out_items_A_*.jsonl'), load('out_items_B_*.jsonl')
items = {x['id']: x for x in json.load(open(os.path.join(P, 'items_all.json'), encoding='utf-8'))}
ids = sorted(set(A) & set(B))
print(f'條目 A={len(A)} B={len(B)} 共同={len(ids)}/{len(items)}')
b01 = lambda v: 1 if v in (1, '1', True, 'true') else 0
def f13(v):
    if isinstance(v, str) and v.startswith('新主題'): return '新'
    try: return int(v)
    except Exception: return str(v)
def f15(v): return (v or '無').split(':')[0]
def fields(o):
    r = {k: b01(o.get(k)) for k in ['F1','F2','F3','F4','F5','F6','F7','F8','F10','F11']}
    r['F9有無'] = int(bool(o.get('F9'))); r['F12'] = o.get('F12'); r['F13主'] = f13(o.get('F13'))
    r['F15'] = f15(o.get('F15')); r['F16有無'] = int(bool((o.get('F16') or '').strip()))
    r['F14有無'] = int((o.get('F14') or '無') != '無'); r['等級'] = level(o)
    return r
FA = {i: fields(A[i]) for i in ids}; FB = {i: fields(B[i]) for i in ids}
def secondary(o): return {f13(v) for v in (o.get('F13b') or [])} | {f13(o.get('F13'))}
names = list(FA[ids[0]].keys())
rows = []
for strat in ('全部', '隨機', '富集'):
    sid = [i for i in ids if strat == '全部' or items[i]['stratum'] == strat]
    for k in names:
        pr = [(FA[i][k], FB[i][k]) for i in sid]
        a = alpha(pr); lo, hi = boot(pr, B=1000) if strat == '全部' else (float('nan'),) * 2
        pos = (sum(1 for x, _ in pr if x == 1), sum(1 for _, y in pr if y == 1))
        rows.append((strat, k, a, lo, hi, sum(x == y for x, y in pr) / len(pr), pos))
    if strat == '全部':
        for t in list(range(1, 15)):
            pr = [(int(t in secondary(A[i])), int(t in secondary(B[i]))) for i in sid]
            a = alpha(pr); lo, hi = boot(pr, B=1000)
            rows.append((strat, f'議題{t}(主+次)', a, lo, hi, sum(x == y for x, y in pr) / len(pr),
                         (sum(x for x, _ in pr), sum(y for _, y in pr))))
print(f"\n{'層':4s} {'字段':12s} {'α':>6s} {'95%CI':>15s} {'一致':>6s} 陽性A/B 判定")
for s, k, a, lo, hi, ag, pos in rows:
    ci = f'[{lo:5.3f},{hi:5.3f}]' if lo == lo else ' ' * 15
    print(f'{s:4s} {k:12s} {a:6.3f} {ci} {ag:6.1%} {str(pos):>9s} {verdict(a, lo if lo == lo else a) if s == "全部" else ""}')
TA, TB = load('out_threads_A_*.jsonl'), load('out_threads_B_*.jsonl')
th = {x['id']: x for x in json.load(open(os.path.join(P, 'threads_all.json'), encoding='utf-8'))}
tids = sorted(set(TA) & set(TB))
pr = [(TA[i]['label'], TB[i]['label']) for i in tids]
a = alpha(pr); lo, hi = boot(pr)
print(f'\n討論串 {len(tids)}/{len(th)}  S1 α={a:.3f} [{lo:.3f},{hi:.3f}] {verdict(a, lo)}')
st = collections.defaultdict(collections.Counter)
for i in tids: st[th[i]['stratum']][TA[i]['label'] if TA[i]['label'] == TB[i]['label'] else '不一致'] += 1
for s, c in st.items(): print(' ', s, dict(c))
print('\n證據等級 A:', collections.Counter(FA[i]['等級'] for i in ids), '\n         B:', collections.Counter(FB[i]['等級'] for i in ids))
print('F13主 分佈 A:', sorted(collections.Counter(FA[i]['F13主'] for i in ids).items(), key=str))
json.dump([dict(id=i, stratum=items[i]['stratum'], diff={k: (FA[i][k], FB[i][k]) for k in names if FA[i][k] != FB[i][k]},
                text=items[i]['text'][:500]) for i in ids if any(FA[i][k] != FB[i][k] for k in names)],
          open(os.path.join(P, 'disagreements.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
