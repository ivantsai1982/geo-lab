"""S2 條目級：GEO 討論串（S1 兩次一致判 GEO）中的全部帖子與有效評論。
每個 sub-file ≤ 約 60k 字元（單次 Read 可讀完）；3 個 sub-file 為一個代理任務。"""
import sqlite3, json, os, datetime, random, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'full', 's2')
con = sqlite3.connect(os.path.join(ROOT, 'data', 'reddit.db'))
geo = [t[2:] for t in json.load(open(os.path.join(ROOT, 'data', 'full', 's1', 'geo_threads.json')))]
day = lambda t: datetime.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d')
cut = lambda s, n: (s or '')[:n] + ('…[截斷]' if s and len(s) > n else '')
items = []
for pid in geo:
    t, b, n, c = con.execute('SELECT title,body,noise,created FROM posts WHERE id=?', (pid,)).fetchone()
    items.append(dict(id='p_' + pid, kind='帖子', date=day(c), title=t, text=cut(b if n == '' else '[正文已被刪除，只剩標題]', 4000)))
    for cid, par, cc, body in con.execute("SELECT id,parent_id,created,body FROM comments WHERE post_id=? AND noise=''", (pid,)):
        if par and par.startswith('t1_'):
            r = con.execute('SELECT body FROM comments WHERE id=?', (par[3:],)).fetchone()
            ctx = '上級評論：' + cut(r[0] if r else '[不在數據集中]', 500)
        else:
            ctx = '帖子正文：' + cut(b if n == '' else '[已刪除]', 500)
        items.append(dict(id='c_' + cid, kind='評論', date=day(cc), title=t, context=ctx, text=cut(body, 3000)))
print('條目總數', len(items), ' 帖子', sum(i['kind'] == '帖子' for i in items))
json.dump({i['id']: i for i in items}, open(os.path.join(OUT, 'items_all.json'), 'w', encoding='utf-8'), ensure_ascii=False)
random.Random(303).shuffle(items)
files, cur, size = [], [], 0
for it in items:
    s = len(json.dumps(it, ensure_ascii=False))
    if cur and (size + s > 60000 or len(cur) >= 60):
        files.append(cur); cur, size = [], 0
    cur.append(it); size += s
files.append(cur)
for k, f in enumerate(files):
    json.dump(f, open(os.path.join(OUT, f'in_A_{k // 3:03d}{"abc"[k % 3]}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('sub-files', len(files), ' 代理任務', (len(files) + 2) // 3, ' 平均每檔條目', len(items) // len(files))
