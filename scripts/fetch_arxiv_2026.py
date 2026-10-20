"""專抓 2026 年起的 GEO / AI 搜索papers，放到 ../papers/0_2026最新/，並把舊目錄裡的 2026 論文移過去"""
import os, re, csv, time, shutil, glob
from fetch_arxiv_common import api, parse, download, safe, OUT

DATE = 'submittedDate:[202601010000 TO 202612312359]'
TOPICS = [
    'abs:"generative engine optimization"',
    'abs:"generative engine"',
    'abs:"generative search"',
    'abs:"answer engine"',
    'abs:"AI search"',
    'abs:"AI overviews"',
    'abs:"search engine optimization"',
    'abs:GEO AND abs:LLM',
    'abs:visibility AND abs:LLM AND (abs:brand OR abs:product OR abs:content)',
    'abs:citation AND (abs:"search engine" OR abs:"web search") AND abs:LLM',
    'abs:"source selection" AND abs:LLM',
    'abs:"deep research" AND abs:citation',
    'abs:"agentic search"',
    'abs:"search agent" AND abs:web',
    'abs:"retrieval-augmented" AND (abs:manipulation OR abs:poisoning OR abs:"content injection")',
    'abs:"ranking manipulation"',
    'abs:"LLM" AND abs:"recommendation" AND abs:"brand"',
    'abs:"generative retrieval" AND abs:web',
    'abs:"query fan-out" OR abs:"query rewriting" AND abs:"search engine"',
]
MUST = re.compile(r'generative engine|generative search|answer engine|ai search|ai overview|search engine|web search|'
                  r'\bseo\b|\bgeo\b|search agent|agentic search|deep research|citation|visibility|retriev', re.I)
LLM = re.compile(r'\bllms?\b|language model|generative|chatgpt|gpt|gemini|perplexity|claude|agent', re.I)

idx_path = os.path.join(OUT, 'index.csv')
old = list(csv.DictReader(open(idx_path, encoding='utf-8-sig'))) if os.path.exists(idx_path) else []
have = {r['id']: r for r in old}

new = {}
for q in TOPICS:
    root = api({'search_query': f'({q}) AND {DATE}', 'max_results': 100,
                'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    time.sleep(3)
    if root is None: continue
    got = parse(root); kept = 0
    for p in got:
        t = p['title'] + ' ' + p['abstract']
        if p['published'] < '2026-01-01' or not (MUST.search(t) and LLM.search(t)): continue
        if p['id'] in new: continue
        p['tier'], p['note'], p['query'] = '0_2026最新', '', q
        new[p['id']] = p; kept += 1
    print(f'{q[:65]:65s} 返回{len(got):3d} 保留{kept:3d}', flush=True)

d = os.path.join(OUT, '0_2026最新'); os.makedirs(d, exist_ok=True)
for p in sorted(new.values(), key=lambda x: x['published'], reverse=True):
    fn = f"{p['published'][:7]}_{p['id']}_{safe(p['title'])}.pdf"
    p['file'] = os.path.join('0_2026最新', fn)
    dst = os.path.join(d, fn)
    prev = have.get(p['id'])
    if prev and prev.get('file') and os.path.exists(os.path.join(OUT, prev['file'])):
        if prev['tier'] in ('1_GEO核心', '2_檢索基礎'):   # 核心論文保留原位
            new.pop(p['id']); continue
        shutil.move(os.path.join(OUT, prev['file']), dst); print('MOVE', fn, flush=True)
    elif not os.path.exists(dst):
        print('OK ' if download(p['id'], dst) else 'ERR', fn, flush=True); time.sleep(3)

rows = [r for r in old if r['id'] not in new] + list(new.values())
fields = ['tier', 'id', 'published', 'title', 'note', 'authors', 'categories', 'query', 'file', 'abstract']
rows.sort(key=lambda x: (x['tier'], x['published']))
with open(idx_path, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('2026 論文數:', len(new), ' 索引總數:', len(rows))
