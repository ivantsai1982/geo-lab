"""試標抽樣：
 (1) 條目級：4 個 GEO 版塊 × (帖子 50 + 評論 50) = 400 條，分層簡單隨機抽樣
 (2) 討論串級（S1 相關性）：GEO 版塊 100 串 + r/seo·r/TechSEO 命中 AI 詞表 100 串 + 未命中 50 串
每個 pass 使用不同隨機順序、不同分批，減少順序/上下文效應。"""
import sqlite3, random, json, os, re, datetime, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'pilot')
con = sqlite3.connect(os.path.join(ROOT, 'data', 'reddit.db'))
rng = random.Random(20260930)
GEO_SUBS = ['aeo', 'GenerativeSEOstrategy', 'SEO_LLM', 'LLMTraffic']
AI_LEX = re.compile(r'\b(geo|aeo|llmo|gpt\w*|chatgpt|openai|perplexity|gemini|claude|copilot|llms?|ai overviews?|aio|ai mode|'
                    r'sge|generative|answer engines?|ai search|ai visibility|llms\.txt|oai-searchbot|gptbot|'
                    r'perplexitybot|claudebot|google-extended|searchgpt|cited|citations?|grok|deepseek|ai crawlers?|'
                    r'ai (?:answers?|tools?|bots?|agents?|traffic|citations?|mentions?))\b', re.I)
day = lambda t: datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
cut = lambda s, n: (s or '')[:n] + ('…[截斷]' if s and len(s) > n else '')

def post_text(pid):
    return con.execute('SELECT title, body, noise FROM posts WHERE id=?', (pid,)).fetchone()

items = []
for sub in GEO_SUBS:
    ps = con.execute("SELECT id FROM posts WHERE sub=? AND noise IN ('','title_only')", (sub,)).fetchall()
    for (pid,) in rng.sample(ps, 50):
        t, b, n = post_text(pid)
        c = con.execute('SELECT created FROM posts WHERE id=?', (pid,)).fetchone()[0]
        items.append(dict(id='p_' + pid, kind='帖子', sub=sub, date=day(c), title=t,
                          text=cut(b if n == '' else '[正文已被刪除，只剩標題]', 4000)))
    cs = con.execute("SELECT id FROM comments WHERE sub=? AND noise=''", (sub,)).fetchall()
    for (cid,) in rng.sample(cs, 50):
        pid, par, c, body = con.execute('SELECT post_id,parent_id,created,body FROM comments WHERE id=?', (cid,)).fetchone()
        pt = post_text(pid) or ('[帖子不在數據集中]', '', '')
        if par and par.startswith('t1_'):
            r = con.execute('SELECT body FROM comments WHERE id=?', (par[3:],)).fetchone()
            parent = '上級評論：' + cut(r[0] if r else '[不在數據集中]', 700)
        else:
            parent = '帖子正文：' + cut(pt[1], 700)
        items.append(dict(id='c_' + cid, kind='評論', sub=sub, date=day(c), title=pt[0], context=parent,
                          text=cut(body, 4000)))

def thread(pid, maxc=6000):
    t, b, n = post_text(pid)
    s = f'【標題】{t}\n【正文】{cut(b, 2500) if n == "" else "[已刪除]"}\n【評論】\n'
    for (body,) in con.execute("SELECT body FROM comments WHERE post_id=? AND noise='' ORDER BY score DESC", (pid,)):
        if len(s) > maxc: s += '…[其餘評論省略]'; break
        s += '- ' + cut(body, 600).replace('\n', ' ') + '\n'
    return s

threads = []
geo_threads = con.execute(f"SELECT id,sub FROM posts WHERE sub IN ({','.join('?'*4)}) AND noise IN ('','title_only')", GEO_SUBS).fetchall()
for pid, sub in rng.sample(geo_threads, 100): threads.append(dict(id='t_' + pid, sub=sub, stratum='GEO版塊', text=thread(pid)))
hit, miss = [], []
for pid, sub, t, b in con.execute("SELECT id,sub,title,body FROM posts WHERE sub IN ('SEO','TechSEO') AND noise IN ('','title_only')"):
    blob = (t or '') + ' ' + (b or '') + ' ' + ' '.join(x for (x,) in con.execute("SELECT body FROM comments WHERE post_id=? AND noise=''", (pid,)))
    (hit if AI_LEX.search(blob) else miss).append((pid, sub))
print('r/seo+TechSEO 討論串: 命中AI詞表', len(hit), ' 未命中', len(miss))
for pid, sub in rng.sample(hit, 100): threads.append(dict(id='t_' + pid, sub=sub, stratum='SEO命中詞表', text=thread(pid)))
for pid, sub in rng.sample(miss, 50): threads.append(dict(id='t_' + pid, sub=sub, stratum='SEO未命中詞表', text=thread(pid)))

json.dump(items, open(os.path.join(OUT, 'items_all.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(threads, open(os.path.join(OUT, 'threads_all.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

def split(lst, n, seed, prefix, strip=()):
    l = [{k: v for k, v in x.items() if k not in strip} for x in lst]
    random.Random(seed).shuffle(l)
    for i in range(0, len(l), n):
        p = os.path.join(OUT, f'{prefix}_{i // n:02d}.json')
        json.dump(l[i:i + n], open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for ps, seed in (('A', 1), ('B', 2)):
    split(items, 40, seed, f'in_items_{ps}')
    split(threads, 25, seed + 10, f'in_threads_{ps}', strip=('stratum', 'sub'))  # 隱藏來源版塊，避免標註者按版塊猜
print('items', len(items), 'threads', len(threads))
