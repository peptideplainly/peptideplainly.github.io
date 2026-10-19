# Oct 19 2026: FDA-approved peptides list (approved vs compoundable vs research-only)
from urllib.parse import quote
from newpages import faqld,faqh,crumbs,signup,SUB
import newpages2
from extras3 import FORZ,PCAC_VOTES,PCAC_OCT24,PCAC_JUL26
P="fda-approved-peptides-list.html"
URL="https://peptideplainly.com/"+P
def DAF(n): return f"https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo={n}"
def DM(s): return f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={s}"
def a(u,t): return f'<a href="{u}" rel="noopener">{t}</a>'
CAT="https://www.fda.gov/media/94155/download"
SAFE="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks"
BIO="https://www.fda.gov/drugs/human-drug-compounding/notice-compounders-changes-affect-compounding-march-23-2020"
BLA="https://www.fda.gov/media/119229/download"
FDA_C="https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-concerns-unapproved-glp-1-drugs-used-weight-loss"
FDA_SHORT="https://www.fda.gov/drugs/drug-alerts-and-statements/fda-clarifies-policies-compounders-national-glp-1-supply-begins-stabilize"
FDA_POL="https://www.fda.gov/drugs/human-drug-compounding/human-drug-compounding-policies-and-rules"
RIN="https://www.reginfo.gov/public/do/eoDetails?rrid=1568964"
AP='<span class="badge approved">FDA-approved</span>'
RO='<span class="badge research">Research purposes only</span>'
IV='<span class="badge research">Investigational</span>'
NOCOMP=f'Generally no: it\'s a biological product, and biologics aren\'t eligible for the compounding exemptions ({a(BIO,"FDA")}).'
BADC=f'Not on FDA\'s category 1 list ({a(CAT,"FDA 503A list")}). FDA lists it as nominated, then withdrawn, with safety concerns ({a(SAFE,"FDA")}).'
# (name, link, badge, what it is / brand, compounding, source)
APPROVED=[
("Semaglutide","peptides/semaglutide.html",AP,"Ozempic, Wegovy (injections), Rybelsus (pill)",f'Not anymore for copies of the brand: the shortage is over and FDA\'s grace periods ended in 2025 ({a(FDA_SHORT,"FDA")}). In April 2026 FDA proposed excluding it from the 503B bulk list ({a(FDA_POL,"FDA")}).',f'{a(DAF(209637),"Ozempic")}, {a(DAF(215256),"Wegovy")}, {a(DAF(213051),"Rybelsus")} (Drugs@FDA)'),
("Tirzepatide","peptides/tirzepatide.html",AP,"Mounjaro, Zepbound",f'Same as semaglutide: shortage resolved, grace periods over ({a(FDA_SHORT,"FDA")}); proposed 503B exclusion in April 2026 ({a(FDA_POL,"FDA")}).',f'{a(DAF(215866),"Mounjaro")}, {a(DAF(217806),"Zepbound")} (Drugs@FDA)'),
("Liraglutide",None,AP,"Victoza, Saxenda, plus approved generics","Not covered on this page.",f'{a(DAF("022341"),"Victoza")}, {a(DAF(206321),"Saxenda")} (Drugs@FDA)'),
("Dulaglutide",None,AP,"Trulicity (type 2 diabetes)",NOCOMP.replace("it's a biological product","it's approved as a biologic (BLA)"),f'{a(DAF(125469),"Trulicity")} (Drugs@FDA)'),
("Tesamorelin","peptides/tesamorelin.html",AP,"Egrifta WR (HIV-associated belly fat)",NOCOMP+f' Egrifta was deemed a biologic in 2020 ({a(BLA,"FDA list")}).',f'{a(DM("839334d3-8c1d-4c26-9036-2ab524a6ea75"),"Egrifta WR label")} (DailyMed)'),
("Bremelanotide (PT-141)","peptides/pt-141.html",AP,"Vyleesi (low desire in premenopausal women)","Not covered on this page.",f'{a(DM("f1d0c1b5-2f39-4bad-a6a4-0066e3ad5dcf"),"Vyleesi label")} (DailyMed); {a(DAF(210557),"Drugs@FDA")}'),
("Elamipretide (SS-31)","peptides/elamipretide.html",AP,"Forzinity (Barth syndrome), approved Sept 2025","Not covered on this page.",f'{a(FORZ,"Forzinity label")} (DailyMed); {a(DAF(215244),"Drugs@FDA")}'),
("Oxytocin",None,AP,"Pitocin and generics (used in labor and delivery, in hospital)","Not covered on this page.",f'{a(DAF("018261"),"Pitocin")} (Drugs@FDA)'),
("hCG (chorionic gonadotropin)",None,AP,"Pregnyl, Novarel and generic chorionic gonadotropin (fertility)",NOCOMP+f' FDA names hCG specifically.',f'{a(DAF("017692"),"Pregnyl")}, {a(DAF("017016"),"Novarel")} (Drugs@FDA); {a(BLA,"FDA biologics list")}'),
]
OTHER=[
("Orforglipron","peptides/orforglipron.html",AP,"Foundayo, approved April 1, 2026. A GLP-1 pill, but a small molecule, not a peptide","Not covered on this page.",f'{a(DAF(220934),"Drugs@FDA")}'),
("Retatrutide","peptides/retatrutide.html",IV,"Lilly's triple agonist, still in phase 3. Not approved; Lilly plans to file in Q1 2027",f'No. FDA says it can\'t be used in compounding under federal law ({a(FDA_C,"FDA")}).',f'{a(FDA_C,"FDA")}; <a href="peptides/retatrutide-fda-approval-status.html">our FDA status tracker</a>'),
]
RESEARCH=[
("BPC-157","peptides/bpc-157.html",f'{BADC} PCAC voted in favor in July 2026 (non-binding).'),
("TB-500","peptides/tb-500.html",f'{BADC} PCAC voted 8–6–1 in favor in July 2026 (non-binding).'),
("GHK-Cu","peptides/ghk-cu.html",f'Topical and other non-injectable forms are on FDA\'s category 1 list; <strong>injectable</strong> GHK-Cu is not ({a(CAT,"FDA 503A list")}).'),
("Ipamorelin","peptides/cjc-1295-ipamorelin.html",f'No. Placed in category 2 (safety concerns) ({a(SAFE,"FDA")}); PCAC voted 0–12–1 against in Oct 2024 ({a(PCAC_OCT24,"FDA minutes")}).'),
("CJC-1295","peptides/cjc-1295-ipamorelin.html",BADC),
("MOTS-c","peptides/mots-c.html",f'{BADC} PCAC voted 7–5–2 in favor in July 2026 (non-binding).'),
("Semax","peptides/semax.html",f'{BADC} PCAC voted 8–5–1 in favor in July 2026 (non-binding).'),
("Selank","peptides/selank.html",BADC),
]
def nm(n,l,R=""): return f'<a href="{R}{l}">{n}</a>' if l else n
def rows(L):
    return "".join(f'<tr><th scope="row">{nm(n,l)}</th><td>{b}</td><td>{w}</td><td>{c}</td><td>{s}</td></tr>' for n,l,b,w,c,s in L)
HEAD='<thead><tr><th scope="col">Compound</th><th scope="col">Status</th><th scope="col">Brand / what it\'s for</th><th scope="col">Can it be compounded?</th><th scope="col">Primary source</th></tr></thead>'
FAQ=[
("Is BPC-157 FDA-approved?",f'No. BPC-157 is not an approved drug and is sold for research only. It\'s also not on FDA\'s list of bulk substances compounders can use while under review ({a(CAT,"FDA")}). A July 2026 advisory committee vote in its favor is a recommendation, not an approval.'),
("Which GLP-1s are FDA-approved?",f'Semaglutide (Ozempic, Wegovy, Rybelsus), tirzepatide (Mounjaro, Zepbound), liraglutide (Victoza, Saxenda) and dulaglutide (Trulicity), per Drugs@FDA. Orforglipron (Foundayo) is approved too, but it\'s a small molecule, not a peptide. Retatrutide is still investigational.'),
("Can a pharmacy compound peptides like BPC-157 or TB-500?",f'Not under current FDA policy. Neither is on FDA\'s category 1 list, and FDA lists both as nominated, then withdrawn, with safety concerns ({a(SAFE,"FDA")}). The PCAC voted for them in July 2026, but FDA hasn\'t acted on that vote.'),
("What is the FDA's interim peptide compounding policy?",f'A notice titled "Interim Access Policy for Compounding Using Certain Peptides" (RIN 0910-ZD94) reached White House review on Oct 14, 2026 ({a(RIN,"reginfo.gov")}). It isn\'t published or in effect, and its details aren\'t public yet.'),
]
def share():
    s=newpages2.SHARE.replace(newpages2.SHARE_URL,URL)
    s=s.replace(quote(newpages2.SHARE_URL,safe=''),quote(URL,safe=''))
    T=newpages2.SHARE_TXT; NT="Which peptides are actually FDA-approved? The plain list, with a source for every row"
    s=s.replace(quote(T),quote(NT)).replace(T,NT)
    return s.replace("Share this calculator","Share this list").replace("Know someone mixing up mg, mL and units? Send them the math.","Know someone who thinks BPC-157 is FDA-approved? Send them the list.").replace("share-calc-","share-fda-")
def page(BASE,ORG,DISC):
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / FDA-approved peptides list</p>
<h1>FDA-approved peptides: the real list</h1>
<p class="lead"><strong>Approved, compoundable or research-only?</strong> Here's where every popular peptide actually stands, with a primary FDA source on every row.</p>
<p><strong>The short version:</strong> nine of the peptides people ask about are real FDA-approved drugs. Retatrutide is close but still investigational. The trendy ones, BPC-157, TB-500, ipamorelin, CJC-1295, MOTS-c, Semax and Selank, are not approved, and compounders can't currently use them either.</p>
<h2 id="approved">FDA-approved peptide drugs</h2>
<div class="table-wrap"><table class="compare"><caption class="sr">FDA-approved peptide drugs, brands and compounding status</caption>{HEAD}<tbody>{rows(APPROVED)}</tbody></table></div>
<p class="fine">"Not covered on this page" means we haven't verified a compounding status for that drug, so we don't state one. Approval is for the brand and use on its label only.</p>
<h2 id="close">Close, but not peptides or not approved</h2>
<div class="table-wrap"><table class="compare"><caption class="sr">Orforglipron and retatrutide status</caption>{HEAD}<tbody>{rows(OTHER)}</tbody></table></div>
<h2 id="research">Research-only peptides</h2>
<p>None of these is an FDA-approved drug. The column on the right is what FDA's compounding lists say.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">Research-only peptides and their FDA compounding status</caption><thead><tr><th scope="col">Compound</th><th scope="col">Status</th><th scope="col">Can it be compounded? (FDA source)</th></tr></thead><tbody>{"".join(f'<tr><th scope="row">{nm(n,l)}</th><td>{RO}</td><td>{c}</td></tr>' for n,l,c in RESEARCH)}</tbody></table></div>
<p class="safety-line"><strong>Not FDA-approved; sold for research only.</strong> Known risks: not well studied in people; FDA cites immunogenicity, impurity and limited-safety-data concerns for several of these ({a(SAFE,"FDA")}). <a href="how-to-tell-if-a-peptide-source-is-legit.html">Choose a tested source</a>.</p>
<h2 id="whats-next">What could change next</h2>
<ul><li><strong>The July 2026 PCAC votes.</strong> FDA's compounding advisory committee voted to recommend BPC-157, KPV, TB-500, MOTS-c, Semax and epitalon for the 503A list ({a(PCAC_JUL26,"FDA meeting page")}; {a(PCAC_VOTES,"vote report")}). The votes are advice. FDA hasn't added any of them yet.</li>
<li><strong>An interim access policy.</strong> FDA sent "Interim Access Policy for Compounding Using Certain Peptides" (RIN 0910-ZD94) to White House review on Oct 14, 2026 ({a(RIN,"reginfo.gov")}). It isn't published or in effect, and which peptides it covers isn't public.</li>
<li><strong>Injectable GHK-Cu.</strong> FDA says it plans to take GHK-Cu to the PCAC by the end of February 2027 ({a(CAT,"FDA 503A list")}).</li>
<li><strong>Retatrutide.</strong> Lilly plans to submit to FDA in Q1 2027. Track it on our <a href="peptides/retatrutide-fda-approval-status.html">retatrutide FDA status page</a>.</li></ul>
<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>
<li><a href="compounded-vs-brand-semaglutide-tirzepatide.html" data-goatcounter-click="next-fda-cb"><strong>Compounded or brand-name?</strong><span>How to tell what's in your box in two minutes.</span></a></li>
<li><a href="how-to-tell-if-a-peptide-source-is-legit.html" data-goatcounter-click="next-fda-legit"><strong>Is your source legit?</strong><span>How to read a COA and spot the red flags.</span></a></li>
<li><a href="semaglutide-vs-tirzepatide.html" data-goatcounter-click="next-fda-vs"><strong>Semaglutide vs tirzepatide</strong><span>Who won the head-to-head.</span></a></li>
<li><a href="{SUB}" data-goatcounter-click="next-fda-signup" rel="noopener"><strong>Get the Friday email</strong><span>We'll tell you the moment FDA moves on any of these.</span></a></li></ul></nav>
{signup("signup-fda")}
{share()}
<h2 id="faq">FDA status FAQ</h2>{faqh(FAQ)}{DISC}</article>'''
    t="FDA-approved peptides list: approved, compounded or research-only?"
    d="Which peptides are FDA-approved, which can be compounded and which are research-only? Semaglutide to BPC-157, with an FDA source for every row."
    schema=[ORG,{"@type":"MedicalWebPage","name":t,"description":d,"url":URL,"inLanguage":"en","lastReviewed":"2026-10-19","publisher":{"@id":BASE+"/#org"},
        "citation":[{"@type":"WebPage","name":"503A bulk drug substance categories","url":CAT},{"@type":"WebPage","name":"Certain bulk drug substances for use in compounding that may present significant safety risks","url":SAFE},{"@type":"WebPage","name":"Notice to Compounders: Changes that affect compounding as of March 23, 2020","url":BIO},{"@type":"WebPage","name":"RIN 0910-ZD94 at OIRA","url":RIN}]},
        {"@type":"Article","headline":"FDA-approved peptides: the real list","description":d,"url":URL,"inLanguage":"en","datePublished":"2026-10-19","dateModified":"2026-10-19","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("FDA-approved peptides list",URL)])]
    return (t,d,body,schema)
def add(pages,BASE,ORG,DISC): pages[P]=page(BASE,ORG,DISC)
def wire(pages):
    from newpages2 import sub
    tile=lambda R:f'<section class="wide two" aria-label="FDA status"><a class="tile" href="{R}{P}"><h3>FDA-approved peptides list</h3><p>Approved, compoundable or research-only? Every row sourced.</p></a></section>'
    h='<section class="wide"><div class="sec-head"><h2>Trending tools &amp; guides</h2></div></section>'
    sub(pages,"index.html",h,h+tile(""))
    h2='<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'
    sub(pages,"peptides/index.html",h2,h2+tile("../"))
LLMS=[("FDA-approved peptides list",P,"Which peptides are FDA-approved (semaglutide, tirzepatide, tesamorelin, bremelanotide, elamipretide, oxytocin, hCG...), which can be compounded, and which are research-only (BPC-157, TB-500, GHK-Cu...), with FDA sources.")]
CARDS={P:dict(card="fda-approved-peptides",kicker="Status check · FDA",title="FDA-approved peptides: the real list",sub="Approved, compoundable or research-only? Every row sourced.",badge="",badge_t="",hot=True)}
