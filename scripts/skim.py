"""快速瀏覽論文：打印摘要 + 結論段。用法: python skim.py <arxiv_id> [...]"""
import sys, re, glob, os
from fetch_arxiv_common import OUT
sys.stdout.reconfigure(encoding='utf-8')
for aid in sys.argv[1:]:
    fs = glob.glob(os.path.join(OUT, '_txt', '*', f'*_{aid}_*.txt'))
    if not fs: print('NOT FOUND', aid); continue
    t = open(fs[0], encoding='utf-8').read()
    print('=' * 20, os.path.basename(fs[0]))
    a = max(t.find('Abstract'), t.find('ABSTRACT'), 0)
    print(t[a:a + 2000])
    m = [x.start() for x in re.finditer(r'\n\s*(\d+\.?\s*)?(Conclusions?|CONCLUSIONS?|Discussion|DISCUSSION)\b', t)]
    if m: print('\n...CONCLUSION...\n' + t[m[-1]:m[-1] + 2500])
