from pathlib import Path
import html,re,mistune
base=Path(__file__).parent
md=(base/'CONTENT.md').read_text(encoding='utf-8')

class AnchorRenderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__()
        self.ids={}
        self.h2=[]
    def heading(self,text,level,**attrs):
        stripped=re.sub(r'<[^>]+>','',text).strip()
        slug=re.sub(r'[^a-z0-9-]','',re.sub(r'\s+','-',stripped.lower())).strip('-') or 'section'
        count=self.ids.get(slug,0);self.ids[slug]=count+1
        if count:slug+=f'-{count+1}'
        if level==2:self.h2.append((slug,stripped))
        return f'<h{level} id="{html.escape(slug)}">{text}</h{level}>\n'

r=AnchorRenderer()
renderer=mistune.create_markdown(renderer=r,plugins=['table','strikethrough','url'])
content_html=renderer(md)
# Separate title and meta lead intro - keep original content complete
nav='\n'.join(f'<a href="#{a}">{html.escape(title)}</a>' for a,title in r.h2)
html_code='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Momentum: engineering, evidence, FAQ and context behind a supervised AI manufacturing production-preparation prototype for AI Builder Cup 2026.">
<meta name="theme-color" content="#f8f7f4">
<title>Momentum | Behind the Build</title>
<style>
:root{--bg:#f8f7f4;--paper:#fffefa;--ink:#18202b;--muted:#596573;--teal:#145c54;--teal-dark:#104740;--teal-pale:#e8efeb;--gold:#c8a96b;--line:#e1e2dd;--soft:#f3f3ef;--shadow:0 20px 70px rgba(20,31,31,.055)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:104px}body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}a{color:var(--teal);text-underline-offset:3px}a:hover{color:#0c3f38}a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #92beb4;outline-offset:3px}
.top{height:72px;background:#fffefa;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:0 max(24px,calc((100% - 1520px)/2));gap:20px;box-shadow:0 4px 25px rgba(0,0,0,.024)}
.brand{display:flex;align-items:center;gap:14px;text-decoration:none;color:var(--ink);font-size:20px;font-weight:800;letter-spacing:-.6px;white-space:nowrap}.brand svg{width:32px;height:32px}.brand small{font-size:10px;color:var(--teal);letter-spacing:1.3px;font-weight:800;margin-left:6px}.top-right{display:flex;gap:14px;align-items:center}.top-right a{font-size:12px;font-weight:750;text-decoration:none;border:1px solid #d8e3de;border-radius:12px;padding:8px 12px;white-space:nowrap}.top-right a.primary{background:var(--teal);color:white;border-color:var(--teal)}
.layout{display:grid;grid-template-columns:minmax(225px,285px) minmax(0,980px);gap:50px;max-width:1510px;margin:0 auto;padding:35px 28px 90px}.sidebar{position:sticky;top:107px;align-self:start;height:calc(100vh - 120px);overflow:auto;border-right:1px solid var(--line);padding-right:18px;scrollbar-width:thin}.sidebar strong{font-size:12px;color:var(--teal);text-transform:uppercase;letter-spacing:1.2px}.nav{margin-top:12px;display:flex;flex-direction:column;gap:1px}.nav a{display:block;padding:8px 12px;border-radius:9px;color:#4e5b65;text-decoration:none;font-size:13px;line-height:1.35}.nav a:hover,.nav a.active{color:var(--teal);background:var(--teal-pale)}
.search-wrap{margin:18px 0 8px}.search-wrap input{width:100%;border:1px solid #d1ded8;background:white;border-radius:11px;padding:12px 14px;color:var(--ink);font:inherit;font-size:13px;outline:none}.results{font-size:12px;max-height:220px;overflow:auto}.results a{display:block;padding:7px 10px;text-decoration:none;border-bottom:1px solid var(--line)}
.main{min-width:0}.intro{padding:0 0 33px;border-bottom:1px solid var(--line);margin-bottom:42px}.eyebrow{font-size:11px;font-weight:800;color:var(--teal);letter-spacing:1.7px;text-transform:uppercase;margin-bottom:20px}.cover{background:linear-gradient(125deg,#e7ede8,#f9f8f4 58%);padding:36px 46px;border:1px solid #dee5df;border-radius:24px;margin-bottom:26px}.cover h1{font-size:clamp(36px,5vw,65px);letter-spacing:-2.2px;line-height:1.06;margin:0;color:var(--ink)}.cover p{font-size:16px;color:#4b5c61;margin:14px 0 0;max-width:760px}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0 4px}.chip{background:var(--teal-pale);color:var(--teal-dark);border-radius:999px;padding:6px 13px;font-size:11px;font-weight:760}.chip:last-child{background:#f2eada;color:#78602f}
.doc{background:transparent;max-width:940px}.doc h1{display:none}.doc>p:first-of-type{display:none}.doc>p:nth-of-type(2){display:none}.doc h2{font-size:clamp(25px,3.2vw,39px);line-height:1.18;letter-spacing:-1px;margin:78px 0 25px;border-top:1px solid var(--line);padding-top:38px}.doc h3{font-size:21px;line-height:1.4;letter-spacing:-.35px;margin:35px 0 12px;color:#28313c}.doc h4{margin:27px 0 8px;font-size:17px}.doc p,.doc li{font-size:15px;color:#46535f}.doc ul,.doc ol{padding-left:23px}.doc li{padding:4px 0}.doc li::marker{color:var(--teal)}.doc strong{color:var(--ink)}.doc blockquote{padding:17px 21px;border-left:4px solid var(--teal);background:#eaf1ec;border-radius:0 12px 12px 0;margin:22px 0}.doc blockquote p{margin:0;color:#294c46}.doc hr{border:0;border-top:1px solid var(--line);margin:28px 0}.doc img{display:block;max-width:100%;height:auto;object-fit:contain;border:1px solid #d6dcd8;border-radius:13px;background:white;box-shadow:var(--shadow);margin:18px 0}.doc img[src*="production"],.doc img[src*="recommendation"],.doc img[src*="five-risk"]{max-height:580px}.doc em{font-size:13px;color:#667480}.doc table{width:100%;border-collapse:separate;border-spacing:0;border:1px solid #dbe1dc;border-radius:12px;overflow:hidden;background:white;font-size:13px;margin:19px 0 30px}.doc th{text-align:left;background:#e8efeb;color:var(--teal-dark);font-size:12px}.doc th,.doc td{border-bottom:1px solid #e8eae6;padding:12px 13px;vertical-align:top}.doc tr:last-child td{border-bottom:none}.doc tbody tr:nth-child(even){background:#fcfcfa}.doc td{color:#43545e}.doc table a{word-break:break-word}.doc code{background:#e7ebe8;border-radius:4px;padding:1px 4px}.doc pre{overflow:auto;background:#1b2426;color:white;padding:15px;border-radius:12px}
.foot{border-top:1px solid var(--line);font-size:12px;color:var(--muted);padding:30px 0;margin-top:70px}.status{font-size:12px;color:var(--teal);font-weight:750}.back{display:none}.faq-filter{display:none}
@media(max-width:1050px){.layout{grid-template-columns:minmax(200px,230px) minmax(0,1fr);gap:26px;padding:26px 20px}.cover{padding:28px}.top-right a:not(.primary){display:none}}
@media(max-width:760px){.layout{display:block;padding:12px 18px 60px}.sidebar{position:relative;top:auto;overflow:visible;height:auto;border:0;padding:8px 0 22px}.nav{max-height:140px;overflow:auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}.nav a{font-size:12px;padding:8px 9px}.top{height:65px;padding:0 17px}.brand{font-size:18px}.brand small{display:none}.top-right{gap:8px}.top-right a.primary{font-size:11px;padding:7px 10px}.intro{margin-bottom:0}.cover{border-radius:17px;padding:26px}.cover h1{letter-spacing:-1.2px}.doc h2{margin-top:45px;padding-top:26px}.doc p,.doc li{font-size:14.5px}.doc table{display:block;overflow-x:auto}.doc th,.doc td{min-width:125px}.doc blockquote{margin:15px 0}.back{display:inline-block;position:fixed;right:14px;bottom:16px;z-index:40;background:var(--teal);color:white;text-decoration:none;border-radius:999px;padding:10px 15px;font-size:12px;box-shadow:var(--shadow)}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style>
</head>
<body>
<header class="top"><a class="brand" href="#top"><svg viewBox="0 0 32 32" fill="none" stroke="#c8a96b" stroke-width="1.8"><path d="M16 2 29 9v14L16 30 3 23V9zM3 9l13 7 13-7M16 16v14M10 5l13 7"/></svg>Momentum <small>BEHIND THE BUILD</small></a><div class="top-right"><a href="https://github.com/SiddhantOswal/Momentum" target="_blank" rel="noopener noreferrer">Source code</a><a href="https://momentum-ai.cloud.run/" class="primary" target="_blank" rel="noopener noreferrer">Open application ↗</a></div></header>
<div class="layout" id="top">
<aside class="sidebar"><strong>Explore Momentum</strong><div class="search-wrap"><input type="search" id="kbsearch" autocomplete="off" placeholder="Search the knowledge bank" aria-label="Search the knowledge bank"></div><div class="results" id="searchresults" aria-live="polite"></div><nav class="nav" aria-label="Document sections">__NAV__</nav><p class="status">Supervised prototype · Evidence-led</p></aside>
<main class="main">
<div class="intro"><div class="cover"><div class="eyebrow">Team Nucleas &nbsp; / &nbsp; AI Builder Cup 2026</div><h1>Momentum.<br>Behind the Build.</h1><p>The complete technical companion to the industrial production intelligence prototype.</p><p style="margin:12px 0 18px;font-size:14px;line-height:1.55;color:#516460"><strong>Siddhant Oswal</strong> · Team Lead &nbsp; / &nbsp; <strong>Om Jain</strong> · Team Member</p><div class="meta"><span class="chip">Manufacturing · Intelligent operations</span><span class="chip">Google Cloud + Gemini</span><span class="chip">Sustainability category</span></div></div></div>
<article class="doc" id="document">__CONTENT__</article>
<footer class="foot">Prepared by Team Nucleas. Source-grounded project reference, not an independently audited factory study. <a href="CONTENT.md" download>Download Markdown source</a>. Last reviewed 17 October 2026.</footer>
</main></div><a href="#top" class="back" aria-label="Back to top">↑ Top</a>
<script>
(function(){
 const input=document.getElementById('kbsearch'), res=document.getElementById('searchresults'),doc=document.getElementById('document');
 const sections=[...doc.querySelectorAll('h2,h3,h4')];
 input.addEventListener('input',()=>{
  const q=input.value.trim().toLowerCase(); res.replaceChildren();if(q.length<2)return;
  let matches=[];
  for(const h of sections){ if(h.textContent.toLowerCase().includes(q))matches.push(h); }
  if(matches.length<5){
    const textNodes=[...doc.querySelectorAll('p,li')].filter(e=>e.textContent.toLowerCase().includes(q));
    for(const t of textNodes){if(matches.length>=12)break;const h=t.closest('section')?.querySelector('h2')||t.previousElementSibling||t; if(!matches.includes(t))matches.push(t);}
  }
  for(const m of matches.slice(0,12)){
    const a=document.createElement('a');a.href='#'+(m.id||'document');a.textContent=(m.textContent||'Match').trim().slice(0,105);
    a.addEventListener('click',()=>{if(!m.id){m.scrollIntoView({behavior:'smooth',block:'center'});}input.value='';res.replaceChildren()});res.append(a);
  }
  if(!matches.length)res.textContent='No matching headings or text.';
 });
 const links=[...document.querySelectorAll('.nav a')];
 const obs=new IntersectionObserver(entries=>{for(const entry of entries){if(!entry.isIntersecting)continue;links.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+entry.target.id));}}, {rootMargin:'-100px 0px -72% 0px',threshold:0});
 for(const h of doc.querySelectorAll('h2'))obs.observe(h);
})();
</script>
</body></html>'''
html_code=html_code.replace('__NAV__',nav).replace('__CONTENT__',content_html)
(base/'index.html').write_text(html_code,encoding='utf-8')
print('WROTE',base/'index.html','bytes',len(html_code),'sections',len(r.h2))
