"""步驟1：把 reddit 原始 jsonl 整理成 SQLite（posts / comments 兩表），只保留分析需要的字段，並標記客觀噪音。
客觀噪音 = 正文已刪除且無標題外內容、機器人帳號、純鏈接/極短無信息。不做任何主觀判斷。"""
import json, glob, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'reddit相關貼文')
DB = os.path.join(ROOT, 'data', 'reddit.db')
BOTS = {'AutoModerator', 'sneakpeekbot', 'RemindMeBot', 'B0tRank', 'GoodBot_BadBot', 'WikiSummarizerBot', 'SaveVideo', 'savevideo', 'RepostSleuthBot'}
DEL = {'[removed]', '[deleted]', '', None}
URL = re.compile(r'https?://\S+')

def noise(text, author):
    if author in BOTS or (author or '').lower().endswith('bot') and author not in (None, '[deleted]'):
        return 'bot'
    if text in DEL: return 'deleted'
    stripped = URL.sub('', text).strip()
    if len(re.findall(r'\w+', stripped)) < 4: return 'too_short'
    return ''

if os.path.exists(DB): os.remove(DB)
con = sqlite3.connect(DB)
con.executescript('''
CREATE TABLE posts(id TEXT PRIMARY KEY, sub TEXT, author TEXT, created INTEGER, score INTEGER, num_comments INTEGER,
  title TEXT, body TEXT, url TEXT, domain TEXT, flair TEXT, permalink TEXT, noise TEXT);
CREATE TABLE comments(id TEXT PRIMARY KEY, sub TEXT, post_id TEXT, parent_id TEXT, author TEXT, created INTEGER,
  score INTEGER, body TEXT, noise TEXT);
''')
for f in sorted(glob.glob(os.path.join(SRC, '*.jsonl'))):
    kind = 'posts' if f.endswith('_posts.jsonl') else 'comments'
    rows = []
    for line in open(f, encoding='utf-8'):
        try: d = json.loads(line)
        except Exception: continue
        a = d.get('author')
        if kind == 'posts':
            body = d.get('selftext') or ''
            # 帖子：正文刪了但標題還在，只要標題有內容就不算噪音（評論區可能有價值）
            n = noise(body, a)
            if n in ('deleted', 'too_short') and len(re.findall(r'\w+', d.get('title') or '')) >= 4: n = 'title_only'
            rows.append((d['id'], d.get('subreddit'), a, int(float(d.get('created_utc') or 0)), d.get('score'),
                         d.get('num_comments'), d.get('title'), body, d.get('url'), d.get('domain'),
                         d.get('link_flair_text'), d.get('permalink'), n))
        else:
            body = d.get('body') or ''
            rows.append((d['id'], d.get('subreddit'), (d.get('link_id') or '')[3:], d.get('parent_id'), a,
                         int(float(d.get('created_utc') or 0)), d.get('score'), body, noise(body, a)))
    q = '?,' * (13 if kind == 'posts' else 9)
    con.executemany(f'INSERT OR IGNORE INTO {kind} VALUES ({q[:-1]})', rows)
    print(f'{os.path.basename(f):45s} {len(rows):7d}')
con.commit()
for t in ('posts', 'comments'):
    print(f'\n== {t} 噪音分佈 ==')
    for r in con.execute(f"SELECT sub, noise, COUNT(*) FROM {t} GROUP BY sub, noise ORDER BY sub, noise"):
        print(f'  {r[0]:22s} {r[1] or "OK":12s} {r[2]:7d}')
con.execute('CREATE INDEX ic ON comments(post_id)'); con.commit()
