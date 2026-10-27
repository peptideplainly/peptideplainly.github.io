# Oct 27 2026: FDA status tracker + What-changed log + per-guide "Status last checked"
import fdalist as F
from newpages import faqld,faqh,crumbs,signup,SUB
from extras3 import PCAC_VOTES,PCAC_OCT24,PCAC_JUL26
a=F.a; P="peptide-fda-status-tracker.html"; URL="https://peptideplainly.com/"+P
AP=F.AP; RO=F.RO; IV=F.IV
# slug -> (name, badge, status line, latest event, source html, checked)
CHK19="Oct 19, 2026"
ROWS=[
("semaglutide","Semaglutide",AP,"FDA-approved (Ozempic, Wegovy, Rybelsus)",f'April 2026: FDA proposed excluding it from the 503B bulk list ({a(F.FDA_POL,"FDA")})',f'{a(F.DAF(209637),"Drugs@FDA")}',CHK19),
("tirzepatide","Tirzepatide",AP,"FDA-approved (Mounjaro, Zepbound)",f'April 2026: FDA proposed excluding it from the 503B bulk list ({a(F.FDA_POL,"FDA")})',f'{a(F.DAF(215866),"Drugs@FDA")}',CHK19),
("orforglipron","Orforglipron",AP,"FDA-approved (Foundayo); small molecule",f'Apr 1, 2026: approved',f'{a(F.DAF(220934),"Drugs@FDA")}',CHK19),
("retatrutide","Retatrutide",IV,"Investigational, not FDA-approved",f'Lilly plans to submit in Q1 2027; FDA says it can\'t be used in compounding',f'{a(F.FDA_C,"FDA")}; <a href="peptides/retatrutide-fda-approval-status.html">our tracker</a>',CHK19),
("cagrilintide","Cagrilintide (CagriSema)",IV,"Investigational, not FDA-approved",f'Dec 2025: Novo submitted CagriSema to FDA; FDA says cagrilintide can\'t be used in compounding',f'{a(F.FDA_C,"FDA")}; <a href="peptides/cagrilintide.html">our guide</a>',CHK19),
("tesamorelin","Tesamorelin",AP,"FDA-approved (Egrifta WR); biologic",f'Mar 23, 2020: deemed a biologic ({a(F.BLA,"FDA list")})',f'{a(F.DM("839334d3-8c1d-4c26-9036-2ab524a6ea75"),"DailyMed")}',CHK19),
("pt-141","Bremelanotide (PT-141)",AP,"FDA-approved (Vyleesi)",'Jun 21, 2019: approved',f'{a(F.DAF(210557),"Drugs@FDA")}',CHK19),
("elamipretide","Elamipretide (SS-31)",AP,"FDA-approved (Forzinity), accelerated approval",'Sept 19, 2025: approved',f'{a(F.DAF(215244),"Drugs@FDA")}',CHK19),
("bpc-157","BPC-157",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted to recommend (non-binding)',f'{a(PCAC_JUL26,"FDA meeting")}; {a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK19),
("tb-500","TB-500",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted 8–6–1 to recommend (non-binding)',f'{a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK19),
("mots-c","MOTS-c",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted 7–5–2 to recommend (non-binding)',f'{a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK19),
("semax","Semax",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted 8–5–1 to recommend (non-binding)',f'{a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK19),
("epitalon","Epitalon",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted 7–4–1 to recommend (non-binding)',f'{a(PCAC_VOTES,"vote report")}; {a(F.SAFE,"FDA")}',CHK19),
("kpv","KPV",RO,"Not approved; not on 503A category 1",'Jul 2026: PCAC voted to recommend (non-binding)',f'{a(PCAC_VOTES,"vote report")}; {a(F.SAFE,"FDA")}',CHK19),
("ghk-cu","GHK-Cu",RO,"Not approved; non-injectable forms on 503A category 1",'FDA plans to consult PCAC on injectable GHK-Cu by end of Feb 2027',f'{a(F.CAT,"503A list")}',CHK19),
("cjc-1295-ipamorelin","Ipamorelin",RO,"Not approved; FDA category 2 (503B, safety concerns)",'Oct 2024: PCAC voted 0–12–1 against',f'{a(PCAC_OCT24,"FDA minutes")}; {a(F.SAFE,"FDA")}',CHK19),
("cjc-1295-ipamorelin","CJC-1295",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
("selank","Selank",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
("kisspeptin","Kisspeptin-10",RO,"Not approved; 503A category 2",'Oct 2024: PCAC voted 0–11–0 against',f'{a(PCAC_OCT24,"FDA minutes")}; {a(F.SAFE,"FDA")}',CHK19),
("melanotan-2","Melanotan II",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
]
LOG=[
("2026-10-27","RIN 0910-ZD94 still shows Pending EO 12866 Regulatory Review",f'{a(F.RIN,"reginfo.gov")}'),
("2026-10-14","FDA's \"Interim Access Policy for Compounding Using Certain Peptides\" (RIN 0910-ZD94) received for White House review. Text not public; not in effect.",f'{a(F.RIN,"reginfo.gov")}'),
("2026-07-23","PCAC (July 23–24 meeting) voted to recommend BPC-157, KPV, TB-500, MOTS-c, Semax and epitalon for the 503A list. Non-binding.",f'{a(PCAC_JUL26,"FDA meeting page")}; {a(PCAC_VOTES,"vote report")}'),
("2026-05-14","FDA updated its 503A bulk substance categories. Non-injectable GHK-Cu is on category 1.",f'{a(F.CAT,"FDA 503A list")}'),
("2026-04-01","Orforglipron approved as Foundayo.",f'{a(F.DAF(220934),"Drugs@FDA")}'),
("2025-09-19","Elamipretide approved as Forzinity (accelerated approval).",f'{a(F.DAF(215244),"Drugs@FDA")}'),
]
def fmt(d):
    import datetime as dt; return dt.date.fromisoformat(d).strftime("%b %-d, %Y")
FAQ=[("How often is this tracker updated?","We re-check each status against FDA's own pages and add any change to the What-changed log with its date and source. Each guide shows when its status was last checked."),
("Does a PCAC vote mean a peptide is approved or compoundable?",f'No. Advisory committee votes are recommendations. FDA hasn\'t added any of the July 2026 peptides to the 503A list ({a(F.CAT,"FDA 503A list")}).')]
def page(BASE,ORG,DISC):
    rows="".join(f'<tr id="{s}-{i}"><th scope="row"><a href="peptides/{s}.html">{n}</a></th><td>{b}<br><span class="fine">{st}</span></td><td>{ev}</td><td>{src}</td><td>{c}</td></tr>' for i,(s,n,b,st,ev,src,c) in enumerate(ROWS))
    log="".join(f'<li><strong><time datetime="{d}">{fmt(d)}</time></strong>: {t} ({s})</li>' for d,t,s in LOG)
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / FDA status tracker</p>
<p class="kicker">Status tracker · checked Oct 27, 2026</p><h1>Peptide FDA status tracker</h1>
<p class="lead"><strong>Approved, investigational or research-only, and what changed last.</strong> Every row links the FDA page or primary source behind it, with the date we last checked.</p>
<h2 id="changes">What changed</h2><ul class="log">{log}</ul>
<h2 id="status">Status by compound</h2>
<div class="table-wrap"><table class="compare"><caption class="sr">FDA status by peptide, latest event and source</caption><thead><tr><th scope="col">Compound</th><th scope="col">Status</th><th scope="col">Latest event</th><th scope="col">Source</th><th scope="col">Last checked</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="fine">"503A category 1" is FDA's list of bulk substances compounders may use while under review; category 2 means FDA has identified safety concerns. See our <a href="fda-approved-peptides-list.html">FDA-approved peptides list</a> for brands and compounding details.</p>
{signup("signup-tracker")}
<h2 id="faq">Tracker FAQ</h2>{faqh(FAQ)}{DISC}</article>'''
    t="Peptide FDA status tracker: approvals, PCAC votes, policy changes"
    d="Every popular peptide's FDA status in one table, with a dated log of approvals, PCAC votes and compounding policy changes. Every row sourced."
    schema=[ORG,{"@type":"WebPage","name":t,"description":d,"url":URL,"inLanguage":"en","dateModified":"2026-10-27","publisher":{"@id":BASE+"/#org"}},faqld(FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("FDA status tracker",URL)])]
    return (t,d,body,schema)
CHECKED={}
for i,(s,n,b,st,ev,src,c) in enumerate(ROWS): CHECKED.setdefault(s,(c,i))
CHECKED["bpc-157-tb-500-stack"]=(CHK19,ROWS.index(next(r for r in ROWS if r[0]=="bpc-157")))
def add(pages,BASE,ORG,DISC):
    pages[P]=page(BASE,ORG,DISC)
    import re
    for s,(c,i) in CHECKED.items():
        k=f"peptides/{s}.html"; v=list(pages[k])
        m=re.search(r'(<span class="fine">Checked against[^<]*</span>)',v[2])
        if not m: continue
        v[2]=v[2].replace(m.group(1),m.group(1)+f'<br><span class="fine">Status last checked {c} · <a href="../{P}#{s}-{i}" data-goatcounter-click="status-{s}">FDA status tracker</a></span>',1); pages[k]=tuple(v)
    from newpages2 import sub
    sub(pages,"fda-approved-peptides-list.html",'<h2 id="approved">',f'<p class="calc-callout"><strong>What changed lately?</strong> <a href="{P}">See the FDA status tracker</a>.</p><h2 id="approved">')
    h2='<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'
    sub(pages,"peptides/index.html",h2,h2+f'<section class="wide two" aria-label="Status tracker"><a class="tile" href="../{P}"><h3>FDA status tracker</h3><p>Approvals, PCAC votes and policy changes, dated and sourced.</p></a></section>')
LLMS=[("Peptide FDA status tracker",P,"Status by compound with latest FDA event, source and last-checked date, plus a dated What-changed log (approvals, PCAC votes, RIN 0910-ZD94).")]
CARDS={P:dict(card="fda-status-tracker",kicker="Status tracker · FDA",title="Peptide FDA status tracker",sub="What changed, dated and sourced.",badge="",badge_t="",hot=True)}
