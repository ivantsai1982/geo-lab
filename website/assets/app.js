
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
