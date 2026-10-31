# Oct 27 2026: FDA status tracker + What-changed log + per-guide "Status last checked"
import fdalist as F
from newpages import faqld,faqh,crumbs,signup,SUB
from extras3 import PCAC_VOTES,PCAC_OCT24,PCAC_JUL26
a=F.a; P="peptide-fda-status-tracker.html"; URL="https://peptideplainly.com/"+P
AP=F.AP; RO=F.RO; IV=F.IV
# slug -> (name, badge, status line, latest event, source html, checked)
CHK19="Oct 19, 2026"
CHK28="Oct 28, 2026"
FRPI="https://www.federalregister.gov/public-inspection/2026-22192/enforcement-discretion-policy-regarding-503a-compounding-using-certain-peptide-bulk-drug-substances"
HHSPDF="https://www.hhs.gov/sites/default/files/hhs-503a-peptide-enforcement-discretion-policy-appendix-b.pdf"
FRDOC="https://www.federalregister.gov/documents/2026/10/30/2026-22192/enforcement-discretion-policy-regarding-503a-compounding-using-certain-peptide-bulk-drug-substances"
CHK31="Oct 31, 2026"
NBC="https://www.nbcnews.com/health/health-news/rfk-jr-takes-shortcut-make-peptides-widely-available-rcna606133"
ROWS=[
("semaglutide","Semaglutide",AP,"FDA-approved (Ozempic, Wegovy, Rybelsus)",f'April 2026: FDA proposed excluding it from the 503B bulk list ({a(F.FDA_POL,"FDA")})',f'{a(F.DAF(209637),"Drugs@FDA")}',CHK19),
("tirzepatide","Tirzepatide",AP,"FDA-approved (Mounjaro, Zepbound)",f'April 2026: FDA proposed excluding it from the 503B bulk list ({a(F.FDA_POL,"FDA")})',f'{a(F.DAF(215866),"Drugs@FDA")}',CHK19),
("orforglipron","Orforglipron",AP,"FDA-approved (Foundayo); small molecule",f'Apr 1, 2026: approved',f'{a(F.DAF(220934),"Drugs@FDA")}',CHK19),
("retatrutide","Retatrutide",IV,"Investigational, not FDA-approved",f'Lilly plans to submit in Q1 2027; FDA says it can\'t be used in compounding',f'{a(F.FDA_C,"FDA")}; <a href="peptides/retatrutide-fda-approval-status.html">our tracker</a>',CHK19),
("cagrilintide","Cagrilintide (CagriSema)",IV,"Investigational, not FDA-approved",f'Dec 2025: Novo submitted CagriSema to FDA; FDA says cagrilintide can\'t be used in compounding',f'{a(F.FDA_C,"FDA")}; <a href="peptides/cagrilintide.html">our guide</a>',CHK19),
("tesamorelin","Tesamorelin",AP,"FDA-approved (Egrifta WR); biologic",f'Mar 23, 2020: deemed a biologic ({a(F.BLA,"FDA list")})',f'{a(F.DM("839334d3-8c1d-4c26-9036-2ab524a6ea75"),"DailyMed")}',CHK19),
("pt-141","Bremelanotide (PT-141)",AP,"FDA-approved (Vyleesi)",'Jun 21, 2019: approved',f'{a(F.DAF(210557),"Drugs@FDA")}',CHK19),
("elamipretide","Elamipretide (SS-31)",AP,"FDA-approved (Forzinity), accelerated approval",'Sept 19, 2025: approved',f'{a(F.DAF(215244),"Drugs@FDA")}',CHK19),
("bpc-157","BPC-157",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_JUL26,"FDA meeting")}; {a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK31),
("tb-500","TB-500",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK31),
("mots-c","MOTS-c",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK31),
("semax","Semax",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_VOTES,"vote report")}; {a(F.CAT,"503A list")}',CHK31),
("epitalon","Epitalon",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_VOTES,"vote report")}; {a(F.SAFE,"FDA")}',CHK31),
("kpv","KPV",RO,"Not approved; not on 503A category 1",'Oct 30, 2026: listed in Appendix A of HHS\'s interim 503A enforcement-discretion policy (published Oct 30). Interim, non-binding; not an approval; doesn\'t cover "research use only" sellers.',f'{a(HHSPDF,"HHS policy")}; {a(FRDOC,"Federal Register")}; {a(PCAC_VOTES,"vote report")}; {a(F.SAFE,"FDA")}',CHK31),
("ghk-cu","GHK-Cu",RO,"Not approved; non-injectable forms on 503A category 1",'FDA plans to consult PCAC on injectable GHK-Cu by end of Feb 2027',f'{a(F.CAT,"503A list")}',CHK19),
("cjc-1295-ipamorelin","Ipamorelin",RO,"Not approved; FDA category 2 (503B, safety concerns)",'Oct 2024: PCAC voted 0–12–1 against',f'{a(PCAC_OCT24,"FDA minutes")}; {a(F.SAFE,"FDA")}',CHK19),
("cjc-1295-ipamorelin","CJC-1295",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
("selank","Selank",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
("kisspeptin","Kisspeptin-10",RO,"Not approved; 503A category 2",'Oct 2024: PCAC voted 0–11–0 against',f'{a(PCAC_OCT24,"FDA minutes")}; {a(F.SAFE,"FDA")}',CHK19),
("melanotan-2","Melanotan II",RO,"Not approved; not on 503A category 1",'Listed by FDA as nominated, then withdrawn',f'{a(F.SAFE,"FDA")}',CHK19),
]
LOG=[
("2026-10-30","HHS's peptide enforcement-discretion policy published in the Federal Register (91 FR 68526, doc 2026-22192). Appendix A lists six peptides: BPC-157, epitalon, KPV, MOTS-c, semax and TB-500 (we verified the list against the HHS document; it matches NBC's report). Covers state-licensed pharmacies, federal facilities and licensed physicians, under conditions. Interim, non-binding; not an FDA approval; doesn't cover \"research use only\" sellers. Comments close Nov 13, 2026 (regulations.gov).",f'{a(FRDOC,"Federal Register")}; {a(HHSPDF,"HHS policy")}; <a href="https://www.regulations.gov/document/HHS-OASH-2026-0496-0002" rel="noopener">regulations.gov</a>'),
("2026-10-28","HHS's \"Enforcement Discretion Policy Regarding 503A Compounding Using Certain Peptide Bulk Drug Substances\" (RIN 0910-ZD94, docket HHS-OASH-2026-0496) cleared OIRA review on Oct 27 (\"Consistent with Change\") and is scheduled to publish in the Federal Register Oct 30. Covers state-licensed pharmacies, federal facilities and licensed physicians; interim and non-binding; not an FDA approval; doesn't cover \"research use only\" sellers. Peptide list (Appendix A) not yet verified by us; NBC reports BPC-157, epitalon, KPV, MOTS-c, semax, TB-500. Comments: 2 weeks after publication.",f'{a(FRPI,"Federal Register")}; {a(F.RIN,"reginfo.gov")}; {a(NBC,"NBC News")}'),
("2026-10-27","RIN 0910-ZD94 still shows Pending EO 12866 Regulatory Review",f'{a(F.RIN,"reginfo.gov")}'),
("2026-10-14","FDA's \"Interim Access Policy for Compounding Using Certain Peptides\" (RIN 0910-ZD94) received for White House review. Text not public at the time.",f'{a(F.RIN,"reginfo.gov")}'),
("2026-07-23","PCAC (July 23–24 meeting) voted to recommend BPC-157, KPV, TB-500, MOTS-c, Semax and epitalon for the 503A list. Non-binding.",f'{a(PCAC_JUL26,"FDA meeting page")}; {a(PCAC_VOTES,"vote report")}'),
("2026-05-14","FDA updated its 503A bulk substance categories. Non-injectable GHK-Cu is on category 1.",f'{a(F.CAT,"FDA 503A list")}'),
("2026-04-01","Orforglipron approved as Foundayo.",f'{a(F.DAF(220934),"Drugs@FDA")}'),
("2025-09-19","Elamipretide approved as Forzinity (accelerated approval).",f'{a(F.DAF(215244),"Drugs@FDA")}'),
]
def fmt(d):
    import datetime as dt; return dt.date.fromisoformat(d).strftime("%b %-d, %Y")
FAQ=[("How often is this tracker updated?","We re-check each status against FDA's own pages and add any change to the What-changed log with its date and source. Each guide shows when its status was last checked."),
("Does a PCAC vote mean a peptide is approved or compoundable?",f'No. Advisory committee votes are recommendations. FDA hasn\'t added any of the July 2026 peptides to the 503A list. A separate HHS enforcement-discretion policy (published Oct 30, 2026) is interim and non-binding, and isn\'t an approval ({a(F.CAT,"FDA 503A list")}).')]
def page(BASE,ORG,DISC):
    rows="".join(f'<tr id="{s}-{i}"><th scope="row"><a href="peptides/{s}.html">{n}</a></th><td>{b}<br><span class="fine">{st}</span></td><td>{ev}</td><td>{src}</td><td>{c}</td></tr>' for i,(s,n,b,st,ev,src,c) in enumerate(ROWS))
    log="".join(f'<li><strong><time datetime="{d}">{fmt(d)}</time></strong>: {t} ({s})</li>' for d,t,s in LOG)
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / FDA status tracker</p>
<p class="kicker">Status tracker · checked Oct 31, 2026</p><h1>Peptide FDA status tracker</h1>
<p class="lead"><strong>Approved, investigational or research-only, and what changed last.</strong> Every row links the FDA page or primary source behind it, with the date we last checked.</p>
<h2 id="changes">What changed</h2><ul class="log">{log}</ul>
<h2 id="status">Status by compound</h2>
<div class="table-wrap"><table class="compare"><caption class="sr">FDA status by peptide, latest event and source</caption><thead><tr><th scope="col">Compound</th><th scope="col">Status</th><th scope="col">Latest event</th><th scope="col">Source</th><th scope="col">Last checked</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="fine">"503A category 1" is FDA's list of bulk substances compounders may use while under review; category 2 means FDA has identified safety concerns. See our <a href="fda-approved-peptides-list.html">FDA-approved peptides list</a> for brands and compounding details.</p>
{signup("signup-tracker")}
<h2 id="faq">Tracker FAQ</h2>{faqh(FAQ)}{DISC}</article>'''
    t="Peptide FDA status tracker: approvals, PCAC votes, policy changes"
    d="Every popular peptide's FDA status in one table, with a dated log of approvals, PCAC votes and compounding policy changes. Every row sourced."
    schema=[ORG,{"@type":"WebPage","name":t,"description":d,"url":URL,"inLanguage":"en","dateModified":"2026-10-31","publisher":{"@id":BASE+"/#org"}},faqld(FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("FDA status tracker",URL)])]
    return (t,d,body,schema)
CHECKED={}
for i,(s,n,b,st,ev,src,c) in enumerate(ROWS): CHECKED.setdefault(s,(c,i))
CHECKED["bpc-157-tb-500-stack"]=(CHK31,ROWS.index(next(r for r in ROWS if r[0]=="bpc-157")))
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
