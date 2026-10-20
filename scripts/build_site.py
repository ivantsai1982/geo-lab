"""Build a static documentation-style website (left chapter nav, right on-page TOC,
search, dark mode, language switch) for the popular edition in 繁中 / 简中 / English.
Output: website/ (open website/index.html in a browser; no server needed)."""
import glob, json, os, re, shutil, sys, html
import markdown
from markdown.extensions.toc import slugify_unicode
sys.stdout.reconfigure(encoding="utf-8")
R = "G:/學習雜亂/GEO學習/"
OUT = R + "website/"


def _svg(path):
    return ('<svg class="ic" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + path + '</svg>')
ICON = {
    "menu": _svg('<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>'),
    "search": _svg('<circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'),
    "theme": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 0 0 18z" fill="currentColor"/>'),
    "globe": _svg('<circle cx="12" cy="12" r="9"/><line x1="3" y1="12" x2="21" y2="12"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18z"/>'),
    "down": _svg('<polyline points="6 9 12 15 18 9"/>'),
    "check": _svg('<polyline points="20 6 9 17 4 12"/>'),
    "right": _svg('<polyline points="9 6 15 12 9 18"/>'),
    "left_arrow": _svg('<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>'),
    "right_arrow": _svg('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>'),
    "copy": _svg('<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>'),
}

SHORT = {"zh-Hant": "繁", "zh-Hans": "简", "en": "EN"}
LANGS = {
    "zh-Hant": dict(src=R + "book/zh-hant/", pat=r"第(\d+)章_.*\.md$", gloss="_術語表.md", label="繁體中文",
                    book="AI 為什麼不推薦你？", sub="寫給所有人的 GEO 入門", toc="本頁目錄", search="搜尋",
                    contents="目錄", prev="上一章", next="下一章", gl="術語表", noresult="沒有找到結果", copy="複製本頁 Markdown", copied="已複製",
                    parts={0: "開場：先學會不被騙", 1: "第一部：AI 回答你之前的七道關", 8: "第二部：做什麼有用、怎麼知道有沒有用", 13: "第三部：真實案例", 16: "結語"}),
    "zh-Hans": dict(src=R + "book/zh-hans/", pat=r"第(\d+)章_.*\.md$", gloss="_术语表.md", label="简体中文",
                    book="AI 为什么不推荐你？", sub="写给所有人的 GEO 入门", toc="本页目录", search="搜索",
                    contents="目录", prev="上一章", next="下一章", gl="术语表", noresult="没有找到结果", copy="复制本页 Markdown", copied="已复制",
                    parts={0: "开场：先学会不被骗", 1: "第一部：AI 回答你之前的七道关", 8: "第二部：做什么有用、怎么知道有没有用", 13: "第三部：真实案例", 16: "结语"}),
    "en": dict(src=R + "book/en/", pat=r"Chapter_(\d+)\.md$", gloss="../zh-hant/_術語表.md", label="English",
               book="Why Doesn't AI Recommend You?", sub="A plain-language guide to GEO", toc="On this page", search="Search",
               contents="Contents", prev="Previous", next="Next", gl="Glossary", noresult="No results", copy="Copy page as Markdown", copied="Copied",
               parts={0: "Opening: Learn Not to Be Fooled", 1: "Part One: The Seven Gates", 8: "Part Two: What Works and How to Know",
                      13: "Part Three: Real Cases", 16: "Conclusion"}),
}

CSS = r"""
:root{--bg:#fff;--fg:#1f2328;--muted:#5f6368;--line:#e4e6ea;--bar:#1b1b1f;--barfg:#f2f2f2;--link:#1a55c9;--accent:#b31b1b;
--side:#fafafa;--hl:#eef3ff;--code:#f5f6f8;--th:#f3f4f6}
:root[data-theme=dark]{--bg:#16171b;--fg:#e6e6e6;--muted:#a0a4ab;--line:#2c2f36;--bar:#0e0f12;--barfg:#e6e6e6;--link:#7fa8ff;
--accent:#ff6b6b;--side:#1b1c21;--hl:#22273a;--code:#202228;--th:#202228}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#16171b;--fg:#e6e6e6;--muted:#a0a4ab;--line:#2c2f36;--bar:#0e0f12;
--barfg:#e6e6e6;--link:#7fa8ff;--accent:#ff6b6b;--side:#1b1c21;--hl:#22273a;--code:#202228;--th:#202228}}
*{box-sizing:border-box}html{scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 -apple-system,"Segoe UI","PingFang SC","PingFang TC","Microsoft YaHei","Microsoft JhengHei","Noto Sans CJK SC",Roboto,sans-serif}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:20;height:56px;background:var(--bar);color:var(--barfg);display:flex;align-items:center;gap:16px;padding:0 20px}
.brand{font-weight:700;letter-spacing:.5px;color:var(--barfg);white-space:nowrap}.brand b{color:var(--accent)}
.menu-btn{display:none;align-items:center;background:none;border:0;color:var(--barfg);cursor:pointer;padding:4px}.menu-btn .ic{width:22px;height:22px}
.search{position:relative;flex:0 1 420px}
.search input{width:100%;padding:8px 12px 8px 34px;border-radius:6px;border:0;background:#2c2d33;color:#fff;font-size:15px}
.search .sic{position:absolute;left:10px;top:9px;color:#aaa;display:flex}
#results{position:absolute;top:44px;left:0;right:0;max-height:70vh;overflow:auto;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.2);display:none}
#results a{display:block;padding:10px 14px;border-bottom:1px solid var(--line);color:var(--fg)}#results a:hover{background:var(--hl);text-decoration:none}
#results small{display:block;color:var(--muted)}#results mark{background:#ffe58a;color:#000}
.spacer{flex:1}.lang{position:relative}
.lang-btn{display:flex;align-items:center;gap:6px;background:none;border:1px solid #555;color:var(--barfg);border-radius:6px;padding:5px 10px;font-size:14px;cursor:pointer;white-space:nowrap}
.lang-btn:hover{border-color:#999}.lang-menu{display:none;position:absolute;right:0;top:42px;min-width:170px;background:var(--bg);border:1px solid var(--line);
border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.25);padding:6px;z-index:30}.lang.open .lang-menu{display:block}
.lang-menu a{display:block;padding:8px 12px;border-radius:6px;color:var(--fg);font-size:14px}.lang-menu a:hover{background:var(--hl);text-decoration:none}
.lang-menu a{display:flex;justify-content:space-between;align-items:center}.lang-menu a .ic{visibility:hidden}.lang-menu a.on{font-weight:700;color:var(--link)}.lang-menu a.on .ic{visibility:visible}
.ls{display:none}.theme{display:flex;align-items:center;justify-content:center;background:none;border:1px solid #555;color:var(--barfg);border-radius:50%;width:32px;height:32px;cursor:pointer}.ic{flex:none;vertical-align:-3px}.crumbs{position:sticky;top:56px;z-index:10;display:flex;align-items:center;gap:12px;margin:-36px -48px 24px;padding:10px 48px;background:var(--bg);border-bottom:1px solid var(--line);font-size:13.5px;color:var(--muted)}.trail{flex:1;min-width:0;display:flex;align-items:center;flex-wrap:nowrap;overflow:hidden;white-space:nowrap}.trail>a,.trail>span,#crumb-sec{overflow:hidden;text-overflow:ellipsis}.trail a{color:var(--fg);font-weight:600}.trail a:hover{color:var(--link)}.trail .sep{display:inline-flex;margin:0 4px;opacity:.6}.trail .sep .ic{width:14px;height:14px}.cur-wrap{display:none;align-items:center;min-width:0}.cur-wrap.on{display:inline-flex}#crumb-sec{color:var(--fg);font-weight:600}.copy-md{flex:none;display:flex;align-items:center;gap:6px;background:none;border:1px solid var(--line);color:var(--fg);border-radius:6px;padding:5px 10px;font-size:13px;cursor:pointer}.copy-md:hover{border-color:var(--link);color:var(--link)}.copy-md .i-done{display:none}.copy-md.done{color:#1a7f37;border-color:#1a7f37}.copy-md.done .i-done{display:flex}.copy-md.done .i-copy{display:none}.copy-md span{display:flex}.pager small .ic{width:14px;height:14px}
.wrap{display:flex;max-width:1440px;margin:0 auto}
nav.side{width:280px;flex:none;position:sticky;top:56px;height:calc(100vh - 56px);overflow:auto;padding:28px 12px 40px 28px;font-size:14.5px}
nav.side .part{margin:18px 0 6px;font-size:12px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.4px}
nav.side a{display:block;padding:5px 10px;border-radius:6px;color:var(--fg)}nav.side a:hover{background:var(--hl);text-decoration:none}
nav.side a.on{background:var(--hl);color:var(--link);font-weight:600}
main{flex:1;min-width:0;padding:36px 48px 80px;max-width:860px}
main h1{font-size:2.1em;font-weight:500;line-height:1.3;margin:.2em 0 .8em;color:var(--fg)}
main h2{font-size:1.45em;font-weight:600;margin:2em 0 .6em;padding-top:.3em;border-top:1px solid var(--line)}
main h3{font-size:1.15em;margin:1.6em 0 .4em}main h4{margin:1.3em 0 .3em}
main table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.94em;display:block;overflow-x:auto}
main th,main td{border:1px solid var(--line);padding:8px 10px;vertical-align:top}main th{background:var(--th);text-align:left}
main blockquote{margin:1em 0;padding:.6em 1em;border-left:4px solid var(--link);background:var(--hl);border-radius:0 6px 6px 0}
main code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.9em}
main pre{background:var(--code);padding:14px;border-radius:8px;overflow:auto}main pre code{background:none;padding:0}
main hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:56px;border-top:1px solid var(--line);padding-top:20px}
.pager a{flex:1;padding:12px 16px;border:1px solid var(--line);border-radius:8px}.pager a.nx{text-align:right}.pager small{display:block;color:var(--muted)}
aside.toc{width:260px;flex:none;position:sticky;top:56px;height:calc(100vh - 56px);overflow:auto;padding:36px 20px 40px 8px;font-size:13.5px}
nav.side,aside.toc{scrollbar-width:thin;scrollbar-color:transparent transparent}nav.side:hover,aside.toc:hover{scrollbar-color:var(--line) transparent}nav.side::-webkit-scrollbar,aside.toc::-webkit-scrollbar{width:6px}nav.side::-webkit-scrollbar-thumb,aside.toc::-webkit-scrollbar-thumb{background:transparent;border-radius:3px}nav.side:hover::-webkit-scrollbar-thumb,aside.toc:hover::-webkit-scrollbar-thumb{background:var(--line)}aside.toc{overscroll-behavior:contain}nav.side{overscroll-behavior:contain}aside.toc .t{font-weight:700;margin-bottom:8px;position:sticky;top:-36px;background:var(--bg);padding:6px 0}aside.toc a{display:block;color:var(--muted);padding:3px 0 3px 10px;border-left:2px solid var(--line)}
aside.toc a.l3{padding-left:22px;font-size:12.5px}aside.toc a.on{color:var(--link);border-left-color:var(--link)}
.home{max-width:760px;margin:60px auto;padding:0 20px}.home h1{font-weight:500}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-top:28px}
.cards a{display:block;padding:22px;border:1px solid var(--line);border-radius:10px;color:var(--fg)}.cards a:hover{border-color:var(--link);text-decoration:none}
.cards b{display:block;font-size:1.15em;margin-bottom:4px}
@media (max-width:1200px){aside.toc{display:none}}
@media (max-width:860px){.menu-btn{display:flex}.crumbs{margin:-24px -16px 16px;padding:8px 16px}.copy-md .lbl{display:none}nav.side{position:fixed;left:0;top:56px;background:var(--side);z-index:15;transform:translateX(-100%);transition:.2s;box-shadow:2px 0 12px rgba(0,0,0,.2)}
nav.side.open{transform:none}main{padding:24px 16px 60px}.search{flex:1;min-width:0}.lf{display:none}.ls{display:inline}header{gap:10px;padding:0 12px}.brand span{display:none}}
"""

JS = r"""
(function(){
 const root=document.documentElement,key='geo-theme';
 try{const t=localStorage.getItem(key);if(t)root.dataset.theme=t;}catch(e){}
 const tb=document.querySelector('.theme');if(tb)tb.onclick=()=>{const d=(root.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark'?'light':'dark';root.dataset.theme=d;try{localStorage.setItem(key,d)}catch(e){}};
 const lg=document.querySelector('.lang');
 if(lg){const btn=lg.querySelector('.lang-btn');btn.onclick=e=>{e.stopPropagation();const o=lg.classList.toggle('open');btn.setAttribute('aria-expanded',o)};
  document.addEventListener('click',e=>{if(!e.target.closest('.lang'))lg.classList.remove('open')});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')lg.classList.remove('open')});
  const blocks=()=>[...document.querySelectorAll('main > *:not(.pager):not(.crumbs)')];
  lg.querySelectorAll('.lang-menu a').forEach(a=>a.onclick=e=>{
   if(a.classList.contains('on')){e.preventDefault();lg.classList.remove('open');return}
   const b=blocks(),top=64;if(!b.length||scrollY<10)return;
   let i=b.findIndex(x=>x.getBoundingClientRect().bottom>top);if(i<0)i=b.length-1;
   const r=b[i].getBoundingClientRect(),f=Math.min(1,Math.max(0,(top-r.top)/Math.max(r.height,1)));
   e.preventDefault();location.href=a.href.split('#')[0]+'#pos='+i+','+f.toFixed(3)+','+b.length;});}
 if(location.hash.startsWith('#pos=')){const [i,f,n]=location.hash.slice(5).split(',').map(Number),b=[...document.querySelectorAll('main > *:not(.pager):not(.crumbs)')];
  const go=()=>{let k=b.length===n?i:Math.round(i*b.length/Math.max(n,1));k=Math.min(Math.max(k,0),b.length-1);const el=b[k];if(!el)return;
   const y=el.getBoundingClientRect().top+scrollY+f*el.offsetHeight-64;scrollTo(0,Math.max(0,y));history.replaceState(null,'',location.pathname)};
  go();addEventListener('load',go);}
 const sec=document.getElementById('crumb-sec');
 if(sec){const h2=[...document.querySelectorAll('main h2')],wrap=sec.parentElement;const g=()=>{let c=null;for(const h of h2){if(h.getBoundingClientRect().top<110)c=h;else break}
  if(c){sec.textContent=c.textContent;wrap.classList.add('on')}else wrap.classList.remove('on')};addEventListener('scroll',g,{passive:true});g();}
 const cb=document.querySelector('.copy-md'),src=document.getElementById('md-src');
 if(cb&&src){const md=JSON.parse(src.textContent),lbl=cb.querySelector('.lbl');
  const fallback=()=>{const t=document.createElement('textarea');t.value=md;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();
   let ok=false;try{ok=document.execCommand('copy')}catch(e){}t.remove();return ok};
  const done=()=>{cb.classList.add('done');lbl.textContent=cb.dataset.copied;setTimeout(()=>{cb.classList.remove('done');lbl.textContent=cb.dataset.copy},1600)};
  cb.onclick=()=>{if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(md).then(done,()=>{if(fallback())done()})}else if(fallback())done()};}
 const sideOn=document.querySelector('nav.side a.on'),sideBox=document.querySelector('nav.side');if(sideOn&&sideBox){const t=sideOn.offsetTop;if(t>sideBox.clientHeight-80)sideBox.scrollTop=t-sideBox.clientHeight/3}
 const mb=document.querySelector('.menu-btn'),side=document.querySelector('nav.side');if(mb&&side)mb.onclick=()=>side.classList.toggle('open');
 const links=[...document.querySelectorAll('aside.toc a')],heads=links.map(a=>document.getElementById(decodeURIComponent(a.hash.slice(1)))).filter(Boolean);
 if(heads.length){const f=()=>{let i=0;heads.forEach((h,k)=>{if(h.getBoundingClientRect().top<90)i=k});links.forEach(a=>a.classList.remove('on'));const a=links.find(x=>decodeURIComponent(x.hash.slice(1))===heads[i].id);if(a){a.classList.add('on');const box=document.querySelector('aside.toc');if(box){const t=a.offsetTop,b=t+a.offsetHeight,v0=box.scrollTop+40,v1=box.scrollTop+box.clientHeight-40;if(t<v0||b>v1)box.scrollTo({top:Math.max(0,t-box.clientHeight/2),behavior:document.hidden?'auto':'smooth'})}}};addEventListener('scroll',f,{passive:true});f();}
 const inp=document.querySelector('.search input'),box=document.getElementById('results');
 if(inp&&window.SEARCH){const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  inp.oninput=()=>{const q=inp.value.trim().toLowerCase();if(q.length<1){box.style.display='none';return}
   const out=[];for(const d of SEARCH){const i=d.x.toLowerCase().indexOf(q);const j=d.h.toLowerCase().indexOf(q);if(i<0&&j<0)continue;
    const s=Math.max(0,i-40),snip=i<0?d.x.slice(0,90):d.x.slice(s,i+q.length+60);
    const re=new RegExp(q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'ig');
    out.push(`<a href="${d.u}"><b>${esc(d.h)}</b><small>${esc(d.c)}</small><small>${esc(snip).replace(re,m=>'<mark>'+m+'</mark>')}</small></a>`);if(out.length>=30)break}
   box.innerHTML=out.join('')||`<a>${NORES}</a>`;box.style.display='block'};
  document.addEventListener('click',e=>{if(!e.target.closest('.search'))box.style.display='none'});}
 if(document.querySelector('code.language-mermaid')){const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
  s.onload=()=>{document.querySelectorAll('code.language-mermaid').forEach(c=>{const d=document.createElement('div');d.className='mermaid';d.textContent=c.textContent;c.parentNode.replaceWith(d)});mermaid.initialize({startOnLoad:false,theme:root.dataset.theme==='dark'?'dark':'default'});mermaid.run()};document.head.appendChild(s);}
})();
"""


def page(lang, L, title, nav, body, toc, pager, depth=1, crumbs=None, mdtext=None):
    up = "../" * depth
    items = "".join(f'<a class="{"on" if k == lang else ""}" data-lang="{k}" href="{up}{k}/{{PAGE}}"><span>{v["label"]}</span>{ICON["check"]}</a>'
                    for k, v in LANGS.items())
    langs = (f'<button class="lang-btn" aria-haspopup="true" aria-expanded="false" aria-label="language">{ICON["globe"]}'
             f'<span class="lf">{L["label"]}</span><span class="ls">{SHORT[lang]}</span>{ICON["down"]}</button>'
             f'<div class="lang-menu" role="menu">{items}</div>')
    tochtml = (f'<aside class="toc"><div class="t">{L["toc"]}</div>{toc}</aside>' if toc else '<aside class="toc"></aside>')
    bar = ""
    if crumbs:
        sep = f'<span class="sep">{ICON["right"]}</span>'
        trail = sep.join((f'<a href="{h}">{html.escape(t)}</a>' if h else f'<span>{html.escape(t)}</span>') for t, h in crumbs)
        btn = ''
        if mdtext:
            btn = (f'<button class="copy-md" data-copy="{html.escape(L["copy"])}" data-copied="{html.escape(L["copied"])}" title="{html.escape(L["copy"])}">'
                   f'<span class="i-copy">{ICON["copy"]}</span><span class="i-done">{ICON["check"]}</span><span class="lbl">{html.escape(L["copy"])}</span></button>')
        bar = f'<div class="crumbs"><nav class="trail" aria-label="breadcrumb">{trail}</nav>{btn}</div>'
    mdjs = ''
    if mdtext:
        mdjs = '<script type="application/json" id="md-src">' + json.dumps(mdtext, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · {html.escape(L["book"])}</title><link rel="stylesheet" href="{up}assets/style.css"></head><body>
<header><button class="menu-btn" aria-label="menu">{ICON["menu"]}</button><a class="brand" href="index.html"><b>GEO</b> <span>{html.escape(L["book"])}</span></a>
<div class="search"><span class="sic">{ICON["search"]}</span><input placeholder="{L['search']}…" aria-label="{L['search']}"><div id="results"></div></div><div class="spacer"></div>
<div class="lang">{langs}</div><button class="theme" title="theme" aria-label="theme">{ICON["theme"]}</button></header>
<div class="wrap"><nav class="side">{nav}</nav><main>{bar}{body}{pager}</main>{tochtml}</div>{mdjs}
<script>const NORES={json.dumps(L["noresult"])};</script><script src="search.js"></script><script src="{up}assets/app.js"></script></body></html>"""


def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + "assets")
    open(OUT + "assets/style.css", "w", encoding="utf-8").write(CSS)
    open(OUT + "assets/app.js", "w", encoding="utf-8").write(JS)
    for lang, L in LANGS.items():
        d = OUT + lang + "/"; os.makedirs(d)
        chs = sorted((int(re.search(L["pat"], os.path.basename(f)).group(1)), f)
                     for f in glob.glob(L["src"] + "*.md") if re.search(L["pat"], os.path.basename(f)))
        docs = []
        for n, f in chs:
            md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list",
                                               markdown.extensions.toc.TocExtension(slugify=slugify_unicode, toc_depth="2-3")])
            text = open(f, encoding="utf-8").read()
            body = md.convert(text)
            title = next((l.lstrip("# ").strip() for l in text.splitlines() if l.startswith("# ")), f"{n}")
            docs.append(dict(n=n, title=title, body=body, toks=md.toc_tokens, file=f"ch{n:02d}.html", md=text))
        if L["gloss"]:
            md = markdown.Markdown(extensions=["tables", markdown.extensions.toc.TocExtension(slugify=slugify_unicode)])
            gt = open(L["src"] + L["gloss"], encoding="utf-8").read()
            docs.append(dict(n=99, title=L["gl"], body=md.convert(gt), toks=[], file="glossary.html", md=gt))

        def nav(cur):
            s = f'<a class="{"on" if cur == "index.html" else ""}" href="index.html">{L["contents"]}</a>'
            for dd in docs:
                if dd["n"] in L["parts"]: s += f'<div class="part">{L["parts"][dd["n"]]}</div>'
                if dd["n"] == 99: s += '<div class="part"></div>'
                s += f'<a class="{"on" if dd["file"] == cur else ""}" href="{dd["file"]}">{html.escape(dd["title"])}</a>'
            return s

        search = []
        for k, dd in enumerate(docs):
            toc = ""
            for t in dd["toks"]:
                if t["level"] == 1:
                    for c in t["children"]:
                        toc += f'<a class="l2" href="#{c["id"]}">{html.escape(c["name"])}</a>'
                        for c3 in c["children"]: toc += f'<a class="l3" href="#{c3["id"]}">{html.escape(c3["name"])}</a>'
                else:
                    toc += f'<a class="l{t["level"]}" href="#{t["id"]}">{html.escape(t["name"])}</a>'
                    for c3 in t["children"]: toc += f'<a class="l3" href="#{c3["id"]}">{html.escape(c3["name"])}</a>'
            pv = docs[k - 1] if k > 0 else None
            nx = docs[k + 1] if k + 1 < len(docs) else None
            pager = '<div class="pager">' + (f'<a href="{pv["file"]}"><small>{ICON["left_arrow"]} {L["prev"]}</small>{html.escape(pv["title"])}</a>' if pv else "<span></span>") \
                    + (f'<a class="nx" href="{nx["file"]}"><small>{L["next"]} {ICON["right_arrow"]}</small>{html.escape(nx["title"])}</a>' if nx else "<span></span>") + "</div>"
            part = next((L["parts"][q] for q in sorted(L["parts"], reverse=True) if q <= dd["n"]), None) if dd["n"] != 99 else None
            crumbs = [(dd["title"], "#")]
            out = page(lang, L, dd["title"], nav(dd["file"]), dd["body"], toc, pager, crumbs=crumbs, mdtext=dd["md"]).replace("{PAGE}", dd["file"])
            open(d + dd["file"], "w", encoding="utf-8").write(out)
            # search index: split body by h2/h3
            parts = re.split(r'(<h[23] id="[^"]*">.*?</h[23]>)', dd["body"])
            head, hid = dd["title"], ""
            for p in parts:
                m = re.match(r'<h[23] id="([^"]*)">(.*?)</h[23]>', p)
                if m: hid, head = m.group(1), re.sub("<[^>]+>", "", m.group(2)); continue
                txt = re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", " ", p))).strip()
                if txt: search.append(dict(u=dd["file"] + (f"#{hid}" if hid else ""), h=head, c=dd["title"], x=txt))
        open(d + "search.js", "w", encoding="utf-8").write("window.SEARCH=" + json.dumps(search, ensure_ascii=False) + ";")
        # contents page
        lst = ""
        for dd in docs:
            if dd["n"] in L["parts"]: lst += f"<h2>{L['parts'][dd['n']]}</h2>"
            lst += f'<p><a href="{dd["file"]}">{html.escape(dd["title"])}</a></p>'
        body = f'<h1>{html.escape(L["book"])}</h1><p>{html.escape(L["sub"])}</p>{lst}'
        open(d + "index.html", "w", encoding="utf-8").write(page(lang, L, L["contents"], nav("index.html"), body, "", "").replace("{PAGE}", "index.html"))
        print(lang, len(docs), "pages,", len(search), "search entries")
    cards = "".join(f'<a href="{k}/index.html"><b>{v["label"]}</b>{html.escape(v["book"])}<br><small>{html.escape(v["sub"])}</small></a>' for k, v in sorted(LANGS.items(), key=lambda kv: kv[0] != "en"))
    open(OUT + "index.html", "w", encoding="utf-8").write(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GEO Lab</title><link rel="stylesheet" href="assets/style.css"></head><body><header><span class="brand"><b>GEO</b> <span>Generative Engine Optimization</span></span>
<div class="spacer"></div><button class="theme" aria-label="theme">{ICON["theme"]}</button></header><div class="home"><h1>Why Doesn't AI Recommend You? · AI 為什麼不推薦你？ · AI 为什么不推荐你？</h1>
<div class="cards">{cards}</div></div><script src="assets/app.js"></script></body></html>""")


build()
