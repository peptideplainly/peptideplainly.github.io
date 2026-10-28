# Oct 27 2026: newsletter Status watch (from tracker LOG) + sitemap-indexed archive /newsletter/issue-NNN.html
import re, markdown as _md
import tracker, html as _h
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
# Sponsor rules (template-level, enforced at build): sponsor copy for research-only compounds must not
# encourage human use or give dosing. Copy containing dosing/human-use terms fails the build.
_BANNED=re.compile(r"\b(\d+\s?(mg|mcg|µg|iu|units?|ml)\b|dos(e|es|ing|age)|inject\w*|stack(s|ing)?|cycle|protocol|for human use|take it|subq|subcutaneous)",re.I)
def sponsor(i):
    fm=i.get("fm",{}); keys=("sponsor_name","sponsor_copy","sponsor_url","sponsor_cta")
    if not any(fm.get(k) for k in keys): return ""
    miss=[k for k in keys if not fm.get(k)]
    if miss: raise SystemExit(f"issue-{i['n']:03d}: sponsor block missing {miss}")
    bad=_BANNED.search(fm["sponsor_copy"]+" "+fm["sponsor_cta"])
    if bad: raise SystemExit(f"issue-{i['n']:03d}: sponsor copy contains disallowed dosing/human-use term {bad.group(0)!r}")
    camp=f"issue-{i['n']:03d}"; u=urlsplit(fm["sponsor_url"])
    if u.scheme!="https": raise SystemExit("sponsor_url must be https")
    q=[(k,v) for k,v in parse_qsl(u.query) if not k.startswith("utm_")]+[("utm_source","peptideplainly"),("utm_medium","newsletter"),("utm_campaign",camp)]
    url=urlunsplit(u._replace(query=urlencode(q)))
    slug=re.sub(r"[^a-z0-9]+","-",fm["sponsor_name"].lower()).strip("-")
    e=_h.escape; n=e(fm["sponsor_name"])
    return (f'<aside class="sponsor" aria-label="Sponsored by {n}"><p class="sp-label">Sponsored</p><h2>{n}</h2><p>{e(fm["sponsor_copy"])}</p>'
        f'<p><a class="btn sp-btn" href="{e(url)}" rel="sponsored noopener" target="_blank" data-goatcounter-click="sponsor-{slug}-{camp}">{e(fm["sponsor_cta"])}</a></p>'
        f'<p class="fine sp-disc">Paid sponsorship. {n} paid to appear in this issue. Sponsors don\'t review or influence our editorial content, and a sponsorship is not an endorsement. Not medical advice; research-only compounds are not approved for human use.</p></aside>')
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
        pages[path]=(t[:70],d,f'<article class="issue"><p class="crumbs"><a href="../index.html">Home</a> / <a href="../newsletter.html">Newsletter</a> / Issue #{i["n"]}</p><p class="eyebrow">{eb}</p><h1>{i["headline"]}</h1>{body}{sponsor(i)}{watch(i["iso"],"../")}<p class="fine">Archived issue, published as sent.{cur}</p></article>',
            [ORG,{"@type":"Article","headline":t,"url":f"{BASE}/{path}","datePublished":i["iso"],"author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}}])
