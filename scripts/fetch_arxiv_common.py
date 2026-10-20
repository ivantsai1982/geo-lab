import urllib.request, urllib.parse, xml.etree.ElementTree as ET, time, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'papers')
API = 'http://export.arxiv.org/api/query?'
NS = {'a': 'http://www.w3.org/2005/Atom'}

def api(params):
    url = API + urllib.parse.urlencode(params)
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return ET.fromstring(r.read())
        except Exception as e:
            print('  retry', e, flush=True); time.sleep(5 * (i + 1))
    return None

def parse(root):
    out = []
    for e in root.findall('a:entry', NS):
        aid = e.find('a:id', NS).text.rsplit('/abs/', 1)[-1]
        out.append(dict(
            id=re.sub(r'v\d+$', '', aid),
            title=' '.join(e.find('a:title', NS).text.split()),
            authors='; '.join(a.find('a:name', NS).text for a in e.findall('a:author', NS))[:300],
            published=e.find('a:published', NS).text[:10],
            abstract=' '.join(e.find('a:summary', NS).text.split()),
            categories=' '.join(c.get('term') for c in e.findall('a:category', NS)),
        ))
    return out

def safe(s): return re.sub(r'[\/:*?"<>|]', '', s)[:90].strip()

def download(aid, path):
    try:
        req = urllib.request.Request(f'https://arxiv.org/pdf/{aid}', headers={'User-Agent': 'geo-study/0.1'})
        with urllib.request.urlopen(req, timeout=120) as r, open(path, 'wb') as f: f.write(r.read())
        return True
    except Exception as e:
        print('  ', e); return False
