"""用 arXiv API 檢索 GEO / 生成式搜索 / 信息檢索papers，下載 PDF 到 ../papers/"""
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, time, os, re, csv, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'papers')
API = 'http://export.arxiv.org/api/query?'
NS = {'a': 'http://www.w3.org/2005/Atom'}

# 核心必讀：按 arXiv ID 指定（tier 決定閱讀順序）
CORE = {
    '2311.09735': ('1_GEO核心', 'GEO: Generative Engine Optimization（開山論文）'),
    '2304.09848': ('1_GEO核心', '生成式搜索引擎的可驗證性/引用評估'),
    '2404.07981': ('1_GEO核心', '操縱 LLM 提升產品曝光'),
    '2406.18382': ('1_GEO核心', 'Adversarial SEO for LLMs'),
    '2406.03589': ('1_GEO核心', '對話式搜索引擎的排序操縱'),
    '2005.11401': ('2_檢索基礎', 'RAG 原始論文'),
    '2004.04906': ('2_檢索基礎', 'DPR 稠密檢索'),
    '2004.12832': ('2_檢索基礎', 'ColBERT'),
    '2307.03172': ('2_檢索基礎', 'Lost in the Middle：上下文位置效應'),
    '2112.09332': ('2_檢索基礎', 'WebGPT：帶引用的網頁問答'),
    '2308.07107': ('2_檢索基礎', 'LLM for IR 綜述'),
    '2312.10997': ('2_檢索基礎', 'RAG 綜述'),
    '2310.11511': ('2_檢索基礎', 'Self-RAG'),
}

QUERIES = [
    'all:"generative engine optimization"',
    'abs:"generative engine" AND abs:optimization',
    'abs:"generative search engine"',
    'abs:"answer engine"',
    'abs:"AI search" AND (abs:citation OR abs:visibility OR abs:source)',
    'abs:"AI overviews"',
    'abs:"search engine optimization" AND (abs:LLM OR abs:"large language model")',
    'abs:"product visibility" AND abs:"language model"',
    'abs:"ranking manipulation" AND abs:"language model"',
    'abs:"brand" AND abs:"LLM" AND abs:recommendation AND abs:visibility',
    'abs:"source attribution" AND abs:"generative search"',
    'abs:"citation" AND abs:"search-augmented"',
    'abs:"retrieval-augmented generation" AND abs:"poisoning"',
    'abs:"conversational search" AND abs:citation',
    'abs:"LLM-based search" AND (abs:bias OR abs:source)',
]
RELEVANT = re.compile(r'generative engine|generative search|answer engine|ai search|ai overview|search engine optimi|'
                      r'\bseo\b|\bgeo\b|visibility|citation|cited|ranking manipulat|source|retriev', re.I)

def api(params):
    url = API + urllib.parse.urlencode(params)
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return ET.fromstring(r.read())
        except Exception as e:
            print('  retry', e); time.sleep(5 * (i + 1))
    return None

def parse(root):
    out = []
    for e in root.findall('a:entry', NS):
        aid = e.find('a:id', NS).text.rsplit('/abs/', 1)[-1]
        base = re.sub(r'v\d+$', '', aid)
        out.append(dict(
            id=base,
            title=' '.join(e.find('a:title', NS).text.split()),
            authors='; '.join(a.find('a:name', NS).text for a in e.findall('a:author', NS))[:300],
            published=e.find('a:published', NS).text[:10],
            abstract=' '.join(e.find('a:summary', NS).text.split()),
            categories=' '.join(c.get('term') for c in e.findall('a:category', NS)),
        ))
    return out

papers = {}
print('== 核心論文 ==')
root = api({'id_list': ','.join(CORE), 'max_results': len(CORE)})
for p in parse(root):
    p['tier'], p['note'], p['query'] = *CORE[p['id']], 'core'
    papers[p['id']] = p
time.sleep(3)

for q in QUERIES:
    root = api({'search_query': q, 'max_results': 50, 'sortBy': 'relevance'})
    time.sleep(3)
    if root is None: continue
    got = parse(root); kept = 0
    for p in got:
        if p['id'] in papers: continue
        if not RELEVANT.search(p['title'] + ' ' + p['abstract']): continue
        p['tier'], p['note'], p['query'] = '3_延伸檢索', '', q
        papers[p['id']] = p; kept += 1
    print(f'{q[:70]:70s} 返回{len(got):3d} 新增{kept:3d}')

# 延伸檢索只保留 2023 年後（生成式搜索時代）
papers = {k: v for k, v in papers.items() if v['tier'] != '3_延伸檢索' or v['published'] >= '2023-01-01'}
print('總計', len(papers))

def safe(s): return re.sub(r'[\/:*?"<>|]', '', s)[:90].strip()
for p in sorted(papers.values(), key=lambda x: (x['tier'], x['published'])):
    d = os.path.join(OUT, p['tier']); os.makedirs(d, exist_ok=True)
    fn = f"{p['published'][:7]}_{p['id']}_{safe(p['title'])}.pdf"
    p['file'] = os.path.join(p['tier'], fn)
    path = os.path.join(d, fn)
    if os.path.exists(path) and os.path.getsize(path) > 10000: continue
    try:
        req = urllib.request.Request(f"https://arxiv.org/pdf/{p['id']}", headers={'User-Agent': 'geo-study/0.1'})
        with urllib.request.urlopen(req, timeout=120) as r, open(path, 'wb') as f: f.write(r.read())
        print('OK ', fn)
    except Exception as e:
        print('ERR', p['id'], e); p['file'] = ''
    time.sleep(3)

fields = ['tier', 'id', 'published', 'title', 'note', 'authors', 'categories', 'query', 'file', 'abstract']
rows = sorted(papers.values(), key=lambda x: (x['tier'], x['published']), reverse=False)
with open(os.path.join(OUT, 'index.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('done')
