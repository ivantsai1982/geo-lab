"""全量 S1：討論串 GEO 相關性分類的輸入。
範圍 = 4 個 GEO 版塊全部討論串 + r/seo·r/TechSEO 中命中 AI 詞表（v0.2）的討論串；
排除「無內容」（正文已刪且無任何有效評論）——客觀規則，試標中兩組標註員對此類一致判為無內容。
兩個 pass 用不同隨機種子分批（每批 60 串），並隱藏來源版塊。"""
import sqlite3, json, os, random, sys
sys.stdout.reconfigure(encoding='utf-8')
from pilot_sample_lex import AI_LEX
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'full', 's1')
con = sqlite3.connect(os.path.join(ROOT, 'data', 'reddit.db'))
GEO = ('aeo', 'GenerativeSEOstrategy', 'SEO_LLM', 'LLMTraffic')
cut = lambda s, n: (s or '')[:n] + ('…[截斷]' if s and len(s) > n else '')
threads, excluded = [], 0
for pid, sub, t, b, n in con.execute("SELECT id,sub,title,body,noise FROM posts WHERE noise IN ('','title_only')"):
    com = [x for (x,) in con.execute("SELECT body FROM comments WHERE post_id=? AND noise='' ORDER BY score DESC", (pid,))]
    if n == 'title_only' and not com: excluded += 1; continue
    if sub not in GEO and not AI_LEX.search((t or '') + ' ' + (b or '') + ' ' + ' '.join(com)): continue
    s = f'【標題】{t}\n【正文】{cut(b, 2500) if n == "" else "[已刪除]"}\n【評論】\n'
    for body in com:
        if len(s) > 6000: s += '…[其餘評論省略]'; break
        s += '- ' + cut(body, 600).replace('\n', ' ') + '\n'
    if not com: s += '（無評論）\n'
    threads.append(dict(id='t_' + pid, text=s, _sub=sub))
json.dump({x['id']: x['_sub'] for x in threads}, open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8'))
print('納入', len(threads), '（GEO版塊', sum(x['_sub'] in GEO for x in threads), '）  無內容排除', excluded)
for ps, seed in (('A', 101), ('B', 202)):
    l = [{k: v for k, v in x.items() if k != '_sub'} for x in threads]
    random.Random(seed).shuffle(l)
    for i in range(0, len(l), 60):
        json.dump(l[i:i + 60], open(os.path.join(OUT, f'in_{ps}_{i // 60:03d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(ps, (len(l) + 59) // 60, '批')
