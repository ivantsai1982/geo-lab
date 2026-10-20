import json, glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r'G:/學習雜亂/GEO學習/papers')
t = json.load(open('_notes/triage/triage_all.json', encoding='utf-8'))
A = [i for i, o in t.items() if o['tier'] == 'A'] + ['2307.03172']
txt = {}
for f in glob.glob('_txt/*/*.txt'):
    aid = os.path.basename(f).split('_')[1]
    txt[aid] = os.path.abspath(f).replace(os.sep, '/')
print('缺文本', [i for i in A if i not in txt])
key = lambda i: (min(t[i]['a_type']) if t.get(i, {}).get('a_type') else 3, i)
A = sorted([i for i in A if i in txt], key=key)
B = [A[k:k + 5] for k in range(0, len(A), 5)]
for n, b in enumerate(B):
    json.dump([{'id': i, 'txt': txt[i]} for i in b], open(f'_notes/batches/b{n:02d}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(A), '篇', len(B), '批')
