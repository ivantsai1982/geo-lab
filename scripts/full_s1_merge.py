"""合併 S1 全量兩次標註，計算 α，確定 GEO 討論串集合（兩次都判 GEO 才保留）。"""
import json, glob, os, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
from pilot_agreement import alpha, boot
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data', 'full', 's1')
man = json.load(open(os.path.join(D, 'manifest.json'), encoding='utf-8'))
GEO = {'aeo', 'GenerativeSEOstrategy', 'SEO_LLM', 'LLMTraffic'}
lab = {'A': {}, 'B': {}}
for p in 'AB':
    for f in glob.glob(os.path.join(D, f'out_{p}_*.jsonl')):
        for l in open(f, encoding='utf-8'):
            l = l.strip()
            if l:
                try: o = json.loads(l); lab[p][o['id']] = o['label'].strip()
                except Exception as e: print('BAD', f, l[:60])
for p in 'AB':
    miss = set(man) - set(lab[p]); extra = set(lab[p]) - set(man)
    print(p, '已標', len(lab[p]), '缺', len(miss), '多餘', len(extra), '標籤', collections.Counter(lab[p].values()))
ids = sorted(set(lab['A']) & set(lab['B']) & set(man))
pairs = [(lab['A'][i], lab['B'][i]) for i in ids]
a = alpha(pairs); lo, hi = boot(pairs, B=1000)
print(f'\nS1 全量 α={a:.3f} 95%CI[{lo:.3f},{hi:.3f}]  n={len(ids)}  一致率={sum(x==y for x,y in pairs)/len(pairs):.1%}')
for grp, cond in (('GEO版塊', lambda i: man[i] in GEO), ('SEO/TechSEO', lambda i: man[i] not in GEO)):
    sid = [i for i in ids if cond(i)]; pr = [(lab['A'][i], lab['B'][i]) for i in sid]
    both = collections.Counter(x if x == y else '不一致' for x, y in pr)
    print(f'{grp}: n={len(sid)} α={alpha(pr):.3f}', dict(both))
keep = [i for i in ids if lab['A'][i] == 'GEO' and lab['B'][i] == 'GEO']
json.dump(keep, open(os.path.join(D, 'geo_threads.json'), 'w'), indent=0)
print('\n最終 GEO 討論串（兩次一致）:', len(keep), ' 其中 GEO版塊', sum(man[i] in GEO for i in keep), ' SEO/TechSEO', sum(man[i] not in GEO for i in keep))
