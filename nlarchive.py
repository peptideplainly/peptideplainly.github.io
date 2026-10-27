# Oct 27 2026: newsletter Status watch (from tracker LOG) + sitemap-indexed archive /newsletter/issue-NNN.html
import re, markdown as _md
import tracker
def watch(upto_iso=None, root=""):
    items=[x for x in tracker.LOG if not upto_iso or x[0]<=upto_iso][:3]
    if not items: return ""
    li="".join(f'<li><strong>{tracker.fmt(d)}</strong>: {t} ({s})</li>' for d,t,s in items)
    li=li.replace('href="peptides/',f'href="{root}peptides/')
    return f'<section class="status-watch" aria-label="Status watch"><h2>Status watch</h2><ul>{li}</ul><p class="fine">From our <a href="{root}peptide-fda-status-tracker.html">FDA status tracker</a>.</p></section>'
def add(pages,SENT,CUR,BASE,ORG):
    if not SENT: return
    v=list(pages["newsletter.html"])
    links="".join(f'<li><a href="newsletter/issue-{i["n"]:03d}.html">Issue #{i["n"]}{" · "+i["date"] if i["date"] else ""}: {i["headline"]}</a></li>' for i in reversed(SENT))
    v[2]=v[2].replace('<div class="nl-cta">',watch()+f'<h2 id="archive">Past issues</h2><ul>{links}</ul><div class="nl-cta">',1)
    pages["newsletter.html"]=tuple(v)
    for i in SENT:
        body=_md.markdown(i["md"],extensions=["extra","nl2br"])
        body=re.sub(r"<h1>.*?</h1>","",body,count=1,flags=re.S)
        path=f"newsletter/issue-{i['n']:03d}.html"
        t=f"Peptide Plainly newsletter Issue #{i['n']}"+(f" ({i['date']})" if i['date'] else "")
        d=(f"Issue #{i['n']}: {i['headline']}")[:155]
        eb=f"Issue #{i['n']}"+(f" · {i['date']}" if i['date'] else "")
        cur=' <a href="../newsletter.html">Read this week\'s issue</a>.' if i is not CUR else ""
        pages[path]=(t[:70],d,f'<article class="issue"><p class="crumbs"><a href="../index.html">Home</a> / <a href="../newsletter.html">Newsletter</a> / Issue #{i["n"]}</p><p class="eyebrow">{eb}</p><h1>{i["headline"]}</h1>{body}{watch(i["iso"],"../")}<p class="fine">Archived issue, published as sent.{cur}</p></article>',
            [ORG,{"@type":"Article","headline":t,"url":f"{BASE}/{path}","datePublished":i["iso"],"author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}}])
