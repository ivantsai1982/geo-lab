"""把 ../papers/ 下所有 PDF 轉成純文本，存到 ../papers/_txt/（同目錄結構），方便檢索與閱讀"""
import fitz, os, glob, sys
from fetch_arxiv_common import OUT
for pdf in glob.glob(os.path.join(OUT, '*', '*.pdf')):
    rel = os.path.relpath(pdf, OUT)
    txt = os.path.join(OUT, '_txt', rel[:-4] + '.txt')
    if os.path.exists(txt): continue
    os.makedirs(os.path.dirname(txt), exist_ok=True)
    try:
        with fitz.open(pdf) as doc:
            open(txt, 'w', encoding='utf-8').write('\n'.join(p.get_text() for p in doc))
    except Exception as e:
        print('ERR', rel, e)
print('done')
