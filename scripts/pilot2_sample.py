"""第二輪試標抽樣（手冊 v0.2）：與第一輪不重疊。
條目 400 = 200 簡單隨機 + 200 富集層（含第一人稱 + 數字，用來增加 F4/F5/F8 等稀有陽性，使 α 的 CI 收窄）。
α 是衡量「標註工具」本身的信度，富集抽樣不影響其有效性，但報告時兩層分開列出。
討論串 100 = 新詞表下 r/seo·TechSEO 命中層 60 + GEO 版塊 40。"""
import sqlite3, random, json, os, re, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'pilot2'); os.makedirs(OUT, exist_ok=True)
con = sqlite3.connect(os.path.join(ROOT, 'data', 'reddit.db'))
rng = random.Random(20261001)
GEO_SUBS = ['aeo', 'GenerativeSEOstrategy', 'SEO_LLM', 'LLMTraffic']
used = {x['id'] for x in json.load(open(os.path.join(ROOT, 'data', 'pilot', 'items_all.json'), encoding='utf-8'))}
used_t = {x['id'] for x in json.load(open(os.path.join(ROOT, 'data', 'pilot', 'threads_all.json'), encoding='utf-8'))}
RICH = re.compile(r"\b(we|i|our|my)\b.{0,80}\b(tested|tracked|ran|measured|analy[sz]ed|saw|noticed|found|built|checked)\b", re.I)
NUM = re.compile(r'\d')
day = lambda t: datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
cut = lambda s, n: (s or '')[:n] + ('…[截斷]' if s and len(s) > n else '')

pool = []
for sub in GEO_SUBS:
    for pid, t, b, n, c in con.execute("SELECT id,title,body,noise,created FROM posts WHERE sub=? AND noise IN ('','title_only')", (sub,)):
        txt = (t or '') + ' ' + (b if n == '' else '')
        pool.append(('p_' + pid, sub, txt))
    for cid, b, c in con.execute("SELECT id,body,created FROM comments WHERE sub=? AND noise=''", (sub,)):
        pool.append(('c_' + cid, sub, b))
pool = [p for p in pool if p[0] not in used]
rich = [p for p in pool if RICH.search(p[2]) and NUM.search(p[2])]
print('可抽總體', len(pool), ' 富集層', len(rich))
rand = rng.sample(pool, 200)
rset = {p[0] for p in rand}
rich_s = rng.sample([p for p in rich if p[0] not in rset], 200)

def mk(pid, sub, stratum):
    if pid.startswith('p_'):
        t, b, n, c = con.execute('SELECT title,body,noise,created FROM posts WHERE id=?', (pid[2:],)).fetchone()
        return dict(id=pid, kind='帖子', sub=sub, stratum=stratum, date=day(c), title=t,
                    text=cut(b if n == '' else '[正文已被刪除，只剩標題]', 4000))
    post, par, c, body = con.execute('SELECT post_id,parent_id,created,body FROM comments WHERE id=?', (pid[2:],)).fetchone()
    pt = con.execute('SELECT title,body FROM posts WHERE id=?', (post,)).fetchone() or ('[帖子不在數據集中]', '')
    if par and par.startswith('t1_'):
        r = con.execute('SELECT body FROM comments WHERE id=?', (par[3:],)).fetchone()
        ctx = '上級評論：' + cut(r[0] if r else '[不在數據集中]', 700)
    else:
        ctx = '帖子正文：' + cut(pt[1], 700)
    return dict(id=pid, kind='評論', sub=sub, stratum=stratum, date=day(c), title=pt[0], context=ctx, text=cut(body, 4000))
items = [mk(p, s, '隨機') for p, s, _ in rand] + [mk(p, s, '富集') for p, s, _ in rich_s]

from pilot_sample_lex import AI_LEX
def thread(pid, maxc=6000):
    t, b, n = con.execute('SELECT title,body,noise FROM posts WHERE id=?', (pid,)).fetchone()
    s = f'【標題】{t}\n【正文】{cut(b, 2500) if n == "" else "[已刪除]"}\n【評論】\n'
    k = 0
    for (body,) in con.execute("SELECT body FROM comments WHERE post_id=? AND noise='' ORDER BY score DESC", (pid,)):
        if len(s) > maxc: s += '…[其餘評論省略]'; break
        s += '- ' + cut(body, 600).replace('\n', ' ') + '\n'; k += 1
    if k == 0: s += '（無評論）\n'
    return s
hit = []
for pid, t, b in con.execute("SELECT id,title,body FROM posts WHERE sub IN ('SEO','TechSEO') AND noise IN ('','title_only')"):
    if 't_' + pid in used_t: continue
    blob = (t or '') + ' ' + (b or '') + ' ' + ' '.join(x for (x,) in con.execute("SELECT body FROM comments WHERE post_id=? AND noise=''", (pid,)))
    if AI_LEX.search(blob): hit.append(pid)
print('新詞表命中 r/seo+TechSEO 討論串', len(hit))
geo = [r[0] for r in con.execute(f"SELECT id FROM posts WHERE sub IN ({','.join('?'*4)}) AND noise IN ('','title_only')", GEO_SUBS) if 't_' + r[0] not in used_t]
threads = [dict(id='t_' + p, stratum='SEO命中', text=thread(p)) for p in rng.sample(hit, 60)] + \
          [dict(id='t_' + p, stratum='GEO版塊', text=thread(p)) for p in rng.sample(geo, 40)]
json.dump(items, open(os.path.join(OUT, 'items_all.json'), 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(threads, open(os.path.join(OUT, 'threads_all.json'), 'w', encoding='utf-8'), ensure_ascii=False)
for ps, seed in (('A', 3), ('B', 4)):
    for lst, n, pre in ((items, 40, 'in_items'), (threads, 10, 'in_threads')):
        l = [{k: v for k, v in x.items() if k not in ('stratum', 'sub')} for x in lst]
        random.Random(seed).shuffle(l)
        for i in range(0, len(l), n):
            json.dump(l[i:i + n], open(os.path.join(OUT, f'{pre}_{ps}_{i // n:02d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('items', len(items), 'threads', len(threads))
