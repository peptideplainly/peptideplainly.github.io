# Oct 20 2026: NSW peptide ED surge + FDA interim peptide compounding policy explainer
from urllib.parse import quote
from newpages import faqld,faqh,crumbs,signup,SUB
import newpages2
def a(u,t): return f'<a href="{u}" rel="noopener">{t}</a>'
NSWP="nsw-peptide-emergency-department-surge.html"
BPCP="bpc-157-compounding-fda-interim-policy.html"
REP="https://www.health.nsw.gov.au/epidemiology/Publications/unapproved-peptide-use.pdf"
REPPG="https://www.health.nsw.gov.au/epidemiology/Pages/unapproved-peptide-use.aspx"
MR="https://www.nsw.gov.au/ministerial-releases/nsw-health-warns-of-surge-hospital-presentations-linked-to-peptide-use"
AUSDOC="https://www.ausdoc.com.au/news/almost-1200-ed-presentations-linked-to-unapproved-peptide-use-in-figures-showing-steep-rise/"
NH="https://www.newcastleherald.com.au/story/9370838/nsw-health-warning-as-unapproved-peptide-hospital-visits-soar/"
ABC="https://www.abc.net.au/news/2026-10-19/nsw-peptide-emergency-department-surge-prompts-warning/107281674"
RIN="https://www.reginfo.gov/public/do/eoDetails?rrid=1568964"
DFA="https://www.doctorsforamerica.org/news/statement-release-doctors-for-america-urges-white-house-to-reject-fdas-interim-access-policy-for-unapproved-peptides"
REU="https://www.yahoo.com/news/politics/articles/us-fda-takes-step-change-213124893.html"
CAT="https://www.fda.gov/media/94155/download"
SAFE="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks"
from extras3 import PCAC_VOTES,PCAC_JUL26
FRPI="https://www.federalregister.gov/public-inspection/2026-22192/enforcement-discretion-policy-regarding-503a-compounding-using-certain-peptide-bulk-drug-substances"
HHSPDF="https://www.hhs.gov/sites/default/files/hhs-503a-peptide-enforcement-discretion-policy-appendix-b.pdf"
FRDOC="https://www.federalregister.gov/documents/2026/10/30/2026-22192/enforcement-discretion-policy-regarding-503a-compounding-using-certain-peptide-bulk-drug-substances"
REGDOC="https://www.regulations.gov/document/HHS-OASH-2026-0496-0002"
NBC="https://www.nbcnews.com/health/health-news/rfk-jr-takes-shortcut-make-peptides-widely-available-rcna606133"
DOCKET="https://www.regulations.gov/docket/HHS-OASH-2026-0496"
LEGIT="how-to-tell-if-a-peptide-source-is-legit.html"
FDAL="fda-approved-peptides-list.html"
def share(url,txt,slug,label,pitch):
    s=newpages2.SHARE.replace(quote(newpages2.SHARE_URL,safe=''),quote(url,safe='')).replace(newpages2.SHARE_URL,url)
    T=newpages2.SHARE_TXT; s=s.replace(quote(T),quote(txt)).replace(T,txt)
    return s.replace("Share this calculator",label).replace("Know someone mixing up mg, mL and units? Send them the math.",pitch).replace("share-calc-",f"share-{slug}-")
def nav(items,sig):
    li="".join(f'<li><a href="{h}" data-goatcounter-click="next-{sig}-{k}"><strong>{t}</strong><span>{d}</span></a></li>' for h,k,t,d in items)
    return f'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>{li}<li><a href="{SUB}" data-goatcounter-click="next-{sig}-signup" rel="noopener"><strong>Get the Friday email</strong><span>The week\'s biggest peptide news, free, in five minutes.</span></a></li></ul></nav>'
NSW_FAQ=[
("How many people went to hospital after using peptides in NSW?",f'NSW Health counted 1,180 emergency department presentations that mentioned unapproved peptide use between 1 July 2025 and 30 September 2026, in people aged 16 and over ({a(REP,"NSW Health report")}). That counts visits, not unique people, and doesn\'t prove the peptide caused the visit.'),
("Which peptide showed up most?",f'Retatrutide. It was mentioned in 833 of the 1,180 presentations (71%) ({a(REP,"NSW Health")}). Retatrutide is an investigational drug that isn\'t approved in Australia or the US.'),
("Is retatrutide approved anywhere?",f'No. NSW Health says none of BPC-157, GHK-Cu, TB-500, retatrutide or CJC-1295 is approved in Australia for any purpose ({a(MR,"NSW Government")}). In the US it\'s still in phase 3; see our <a href="peptides/retatrutide-fda-approval-status.html">retatrutide FDA status tracker</a>.'),
]
def nsw(BASE,ORG,DISC):
    url=f"{BASE}/{NSWP}"
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / NSW peptide ER surge</p>
<h1>Peptide ER visits exploded in NSW: 5 a month to 217</h1>
<p class="lead"><strong>Australia's biggest state just put hard numbers on the gray-market peptide boom</strong>, and retatrutide is all over them.</p>
<p>New NSW Health surveillance data counts <strong>1,180 emergency department presentations</strong> that mentioned unapproved peptide use between 1 July 2025 and 30 September 2026. Monthly visits went from <strong>5 in July 2025 to 217 in September 2026</strong> ({a(REP,"NSW Health report")}; {a(MR,"NSW Government release")}).</p>
<h2 id="numbers">The numbers, plainly</h2>
<div class="table-wrap"><table class="compare"><caption class="sr">NSW emergency department presentations mentioning unapproved peptide use, July 2025 to September 2026</caption><thead><tr><th scope="col">Measure</th><th scope="col">Figure</th></tr></thead><tbody>
<tr><th scope="row">Total ED presentations (age 16+)</th><td>1,180</td></tr>
<tr><th scope="row">Monthly, July 2025 → September 2026</th><td>5 → 217</td></tr>
<tr><th scope="row">Mentioned retatrutide</th><td>833 (71%)</td></tr>
<tr><th scope="row">Mentioned "peptide" or another unapproved peptide (BPC-157, TB-500, CJC-1295, GHK-Cu, ipamorelin, melanotan)</th><td>445 (38%)</td></tr>
<tr><th scope="row">Mentioned both</th><td>98 (8%)</td></tr>
<tr><th scope="row">Admitted to hospital from the ED</th><td>18%</td></tr>
<tr><th scope="row">Biggest age groups</th><td>25–34: 32%; 35–44: 26%; 16–24: 25%</td></tr>
<tr><th scope="row">Men / women</th><td>51% / 49%</td></tr></tbody></table></div>
<p class="fine">All figures from the {a(REP,"NSW Health surveillance report")} (Centre for Epidemiology and Evidence, October 2026; {a(REPPG,"report page")}). The groups overlap, so 833 + 445 − 98 = 1,180.</p>
<h2 id="why">What sent people to the ER</h2>
<p>The most common primary diagnoses were <strong>gut problems</strong> (abdominal pain, nausea, vomiting), <strong>heart-related</strong> issues including chest pain, and <strong>anaphylaxis, allergic reactions and medication reactions</strong> ({a(REP,"NSW Health")}). NSW Health says clinicians are also reporting serious illness including <strong>kidney damage and liver injury</strong> ({a(MR,"NSW Government")}).</p>
<p>NSW Chief Health Officer Dr Kerry Chant: "A professional looking website, a label, purity claim, reviews, or influencer endorsement is not proof of what is inside the product." ({a(MR,"NSW Government")})</p>
<h2 id="read-carefully">How to read these numbers</h2>
<ul><li><strong>It's visits, not people.</strong> A repeat visit counts again.</li>
<li><strong>It's a mention, not proof of cause.</strong> The report says it "cannot conclude that peptide use caused the presentation" ({a(REP,"NSW Health")}).</li>
<li><strong>It's probably an undercount.</strong> Peptide use only counts if it was mentioned at triage and written down; the report says the level of under-capture couldn't be estimated.</li>
<li><strong>"Retatrutide" means the label, not a lab test.</strong> Nobody verified what was in the vials.</li></ul>
<h2 id="us">What it means if you're in the US</h2>
<p>Retatrutide isn't approved in Australia or the US. Lilly plans to submit it to the FDA in Q1 2027 (<a href="peptides/retatrutide-fda-approval-status.html">our tracker</a>). What's sold online as "retatrutide" is a research chemical with no FDA quality checks. Wondering what is approved? See our <a href="{FDAL}">FDA-approved peptides list</a>.</p>
<p class="safety-line"><strong>Not FDA-approved; sold for research only.</strong> Known risks: GI effects, chest pain, allergic reactions and reported kidney and liver injury in the NSW data ({a(REP,"NSW Health")}; {a(MR,"NSW Government")}). <a href="{LEGIT}">How to check a lab report</a>.</p>
<p class="fine">Also covered by {a(AUSDOC,"AusDoc")}, the {a(NH,"Newcastle Herald")} and {a(ABC,"ABC News")}.</p>
{nav([("peptides/retatrutide-side-effects.html","se","Retatrutide side effects","What the trials found, plainly."),("peptides/retatrutide-fda-approval-status.html","status","Retatrutide release date","FDA status and every phase 3 readout."),(LEGIT,"legit","How to check a lab report","How to read a COA and spot the red flags."),(BPCP,"bpc","BPC-157 and the HHS peptide policy","Where the FDA's interim peptide policy stands.")],"nsw")}
{signup("signup-nsw")}
{share(BASE+"/"+NSWP,"Peptide ER visits in NSW went from 5 a month to 217. Retatrutide was mentioned in 833 of 1,180. The numbers, plainly","nsw","Share this story","Know someone buying retatrutide online? Send them the numbers.")}
<h2 id="faq">NSW peptide surge FAQ</h2>{faqh(NSW_FAQ)}{DISC}</article>'''
    t="NSW peptide ER surge: 1,180 visits, retatrutide in 833"
    d="NSW Health data: peptide-linked ER visits rose from 5 a month to 217, with retatrutide mentioned in 833 of 1,180. What it means and the risks."
    schema=[ORG,{"@type":"NewsArticle","headline":"Peptide ER visits exploded in NSW: 5 a month to 217","description":d,"url":url,"inLanguage":"en","datePublished":"2026-10-20","dateModified":"2026-10-20","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"},"image":BASE+"/og/nsw-peptide-surge.png",
        "citation":[{"@type":"Report","name":"Emergency department presentations mentioning unapproved peptide use, NSW, July 2025 to September 2026","url":REP},{"@type":"WebPage","name":"NSW Health warns of surge in hospital presentations linked to peptide use","url":MR}]},
        faqld(NSW_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("NSW peptide ER surge",url)])]
    return (t,d,body,schema)
BPC_FAQ=[
("Is BPC-157 now legal to compound?",f'Only in a narrow way. HHS\'s enforcement-discretion policy was published in the Federal Register on Oct 30, 2026 (91 FR 68526; {a(FRDOC,"Federal Register")}). HHS says it does not intend to take enforcement action against "a State-licensed pharmacy, Federal facility, or licensed physician" compounding with a peptide listed in Appendix A, when the policy\'s conditions are met. It is interim, non-binding and can be revisited. BPC-157 is still not FDA-approved.'),
("Does this make \"research use only\" BPC-157 legal?",'No. The policy only covers compounding by state-licensed pharmacies, federal facilities and licensed physicians. It says nothing that makes "research use only" vials sold online legal for people to use, and it doesn\'t approve any product.'),
("Which peptides are covered?",f'Six, listed in Appendix A of the HHS policy document: BPC-157, epitalon, KPV, MOTS-c, semax and TB-500 ({a(HHSPDF,"HHS policy PDF")}). We checked the list against the HHS document on Oct 31, 2026; it matches what NBC News reported ({a(NBC,"NBC News")}). Appendix B limits each one to specific forms and routes.'),
("Can I comment on it?",f'Yes. The notice says written comments can be submitted until 2 weeks after publication, on regulations.gov docket {a(DOCKET,"HHS-OASH-2026-0496")}. Regulations.gov lists the comment period as closing Nov 13, 2026 at 11:59 p.m. ET ({a(REGDOC,"regulations.gov")}).'),
("Is BPC-157 FDA-approved?",f'No. It isn\'t an approved drug for any use, and the notice itself says "Compounded drugs are not FDA-approved" ({a(FRPI,"Federal Register")}). See our <a href="{FDAL}">FDA-approved peptides list</a>.'),
]
def bpc(BASE,ORG,DISC):
    url=f"{BASE}/{BPCP}"
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / BPC-157 and the FDA interim policy</p>
<p class="kicker">Updated Oct 31, 2026 · published Oct 30 · list verified</p><h1>BPC-157 and the HHS peptide compounding policy</h1>
<p class="lead"><strong>The HHS peptide policy was published in the Federal Register on Fri, Oct 30, after clearing White House review on Oct 27.</strong> Here's what it does, what it doesn't, and where BPC-157 stands.</p>
<p><strong>The short version:</strong> it's an interim, non-binding promise not to enforce, for state-licensed 503A pharmacies, federal facilities and licensed physicians compounding certain peptides. It is not an FDA approval, and it does not make "research use only" vials legal.</p>
<h2 id="policy">What the notice says</h2>
<ul><li><strong>Title:</strong> "Enforcement Discretion Policy Regarding 503A Compounding Using Certain Peptide Bulk Drug Substances," Federal Register doc 2026-22192, Docket No. HHS-OASH-2026-0496, RIN 0910-ZD94, from the HHS Office of the Secretary ({a(FRPI,"Federal Register public inspection")}).</li>
<li><strong>Review:</strong> OIRA concluded its review on <strong>Oct 27, 2026</strong>: "Consistent with Change" ({a(RIN,"reginfo.gov")}). It was received Oct 14 under the working title "Interim Access Policy for Compounding Using Certain Peptides."</li>
<li><strong>Publication:</strong> published <strong>Oct 30, 2026</strong>, 91 FR 68526 ({a(FRDOC,"Federal Register")}).</li>
<li><strong>Who it covers:</strong> HHS "does not intend to take enforcement action against a State-licensed pharmacy, Federal facility, or licensed physician compounding a drug product using a peptide bulk drug substance found in Appendix A" ({a(FRPI,"Federal Register")}).</li>
<li><strong>Interim and non-binding:</strong> HHS "may revisit application of this interim policy (in whole or in part) if, among other things, a safety signal or product quality issue arises," and the policy "is not binding on HHS or the public" ({a(FRPI,"Federal Register")}).</li>
<li><strong>Not an approval:</strong> "Compounded drugs are not FDA-approved," the notice says ({a(FRPI,"Federal Register")}).</li>
<li><strong>Comments:</strong> the notice says "until 2 weeks after date of publication"; regulations.gov lists the deadline as <strong>Nov 13, 2026, 11:59 p.m. ET</strong>, docket {a(DOCKET,"HHS-OASH-2026-0496")} ({a(REGDOC,"regulations.gov")}).</li></ul>
<h2 id="list">Which peptides?</h2>
<p><strong>Six</strong>, listed in Appendix A of the HHS policy document ({a(HHSPDF,"HHS policy PDF")}; the file name says "appendix-b"): <strong>BPC-157, epitalon, KPV, MOTS-c, semax and TB-500</strong>. We checked the list against the HHS document on Oct 31, 2026, and it matches what NBC News reported ({a(NBC,"NBC News")}). Appendix B limits each peptide to specific forms and routes.</p>
<p>The policy only applies when a set of conditions is met, including a patient-specific prescription, a bulk substance from an FDA-registered facility with a valid certificate of analysis, a single active ingredient per product, the label statement "This is a compounded drug product. Not for resale.", and reporting of serious adverse events and quality problems to FDA's MedWatch ({a(HHSPDF,"HHS policy")}).</p>
<h2 id="doesnt">What it doesn't do</h2>
<ul><li><strong>It doesn't approve BPC-157.</strong> None of the six peptides is FDA-approved.</li>
<li><strong>It doesn't make "research use only" vials legal.</strong> It covers compounding by pharmacies, federal facilities and physicians, not research-chemical sellers. HHS says the policy is meant to "discourage the continued, widespread use of certain research-use-only peptides supplied by foreign manufacturers that pose a safety risk to US patients" ({a(HHSPDF,"HHS policy")}).</li>
<li><strong>It doesn't add anything to the 503A bulks list.</strong> The notice says FDA's future rulemakings "may propose" adding some or all of these peptides.</li>
<li><strong>It doesn't change the evidence.</strong> BPC-157's research is still mostly animal studies (<a href="peptides/bpc-157.html">our guide</a>).</li></ul>
<h2 id="today">Where BPC-157 stands today</h2>
<ul><li><strong>Not FDA-approved</strong> for any use (<a href="{FDAL}">our FDA list</a>).</li>
<li><strong>Not on category 1</strong> of FDA's 503A bulk substance categories ({a(CAT,"FDA 503A categories")}).</li>
<li><strong>The July 2026 advisory vote was non-binding.</strong> FDA's Pharmacy Compounding Advisory Committee voted to recommend BPC-157 and five others ({a(PCAC_JUL26,"FDA meeting page")}; {a(PCAC_VOTES,"vote report")}).</li></ul>
<h2 id="against">The pushback: Doctors for America</h2>
<p>On Oct 16, Doctors for America urged OMB to <strong>return the policy to FDA</strong> ({a(DFA,"DFA statement")}). Their main points, in their words:</p>
<ul><li>The policy "would let compounding pharmacies sell injectable peptides that have never been shown to be safe … or even reliably identified."</li>
<li>"In July, FDA's own scientists recommended that none of the seven peptides reviewed be added to the compounding list," and the committee "overrode them on narrow 8–6 votes."</li>
<li>On BPC-157 evidence, they cite a 2025 <em>HSS Journal</em> systematic review that found 35 animal studies and one small retrospective human report (12 patients with knee pain, 7 reporting relief).</li>
<li>They want any addition to go through proposed rule, public comment and final rule, with FDA's evidence reviews published.</li></ul>
<h2 id="for">Who wants it: telehealth</h2>
<p>Telehealth company <strong>Hims &amp; Hers</strong> has said it plans to offer peptides if regulations permit ({a(REU,"Reuters")}). Peptides have also been promoted by HHS Secretary Robert F. Kennedy Jr. ({a(REU,"Reuters")}).</p>
<h2 id="next">What happens next</h2>
<p>Comments close Nov 13, 2026. HHS can revisit the policy at any time, and FDA's future rulemakings "may propose" adding some or all of the six to the 503A bulks list. We track changes on our <a href="peptide-fda-status-tracker.html">FDA status tracker</a>.</p>
<p class="safety-line"><strong>Not FDA-approved; sold for research only.</strong> Known risks: not well studied in people (mostly animal studies); FDA cites immunogenicity, impurity and limited-safety-data concerns ({a(SAFE,"FDA")}). <a href="{LEGIT}">How to check a lab report</a>.</p>
{nav([("peptides/bpc-157.html","bpc","BPC-157 guide","The research, plainly."),("peptides/bpc-157-tb-500-stack.html","stack","BPC-157 + TB-500 stack","What the 'Wolverine' stack research says."),(FDAL,"fda","FDA-approved peptides list","Approved, compoundable or research-only?"),(NSWP,"nsw","NSW peptide ER surge","5 visits a month to 217.")],"bpcpol")}
{signup("signup-bpcpol")}
{share(BASE+"/"+BPCP,"BPC-157 and the HHS peptide compounding policy: what it does and doesn\'t do, with sources","bpcpol","Share this explainer","Know someone who thinks BPC-157 is already legal to compound? Send them this.")}
<h2 id="faq">BPC-157 policy FAQ</h2>{faqh(BPC_FAQ)}{DISC}</article>'''
    t="BPC-157 and the HHS peptide compounding policy, explained"
    d="HHS's peptide compounding policy published Oct 30 and covers six peptides, including BPC-157. Who it covers, what it doesn't do, and comment deadline."
    schema=[ORG,{"@type":"NewsArticle","headline":"BPC-157 and the HHS peptide compounding policy","description":d,"url":url,"inLanguage":"en","datePublished":"2026-10-20","dateModified":"2026-10-31","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"},"image":BASE+"/og/bpc-157-policy.png",
        "citation":[{"@type":"WebPage","name":"Federal Register 2026-22192 (91 FR 68526)","url":FRDOC},{"@type":"WebPage","name":"HHS Enforcement Discretion Policy (Appendices A and B)","url":HHSPDF},{"@type":"WebPage","name":"RIN 0910-ZD94 EO 12866 review","url":RIN},{"@type":"WebPage","name":"Doctors for America statement","url":DFA},{"@type":"NewsArticle","name":"US FDA takes step to change peptide compounding policy (Reuters)","url":REU},{"@type":"WebPage","name":"503A bulk drug substance categories","url":CAT}]},
        faqld(BPC_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("BPC-157 and the FDA interim policy",url)])]
    return (t,d,body,schema)
def add(pages,BASE,ORG,DISC):
    pages[NSWP]=nsw(BASE,ORG,DISC); pages[BPCP]=bpc(BASE,ORG,DISC)
def wire(pages):
    from newpages2 import sub
    tile=lambda R:f'<section class="wide two" aria-label="Peptide news"><a class="tile" href="{R}{NSWP}"><h3>NSW peptide ER surge</h3><p>5 visits a month to 217. Retatrutide in 833.</p></a><a class="tile" href="{R}{BPCP}"><h3>BPC-157 and the HHS peptide policy</h3><p>Published Oct 30: six peptides.</p></a></section>'
    h='<section class="wide"><div class="sec-head"><h2>Trending tools &amp; guides</h2></div></section>'
    sub(pages,"index.html",h,h+tile(""))
    h2='<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'
    sub(pages,"peptides/index.html",h2,h2+tile("../"))
    N='<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>'
    li=lambda R,p,k,t,d:f'<li><a href="{R}{p}" data-goatcounter-click="next-{k}"><strong>{t}</strong><span>{d}</span></a></li>'
    nswli=lambda R,k:li(R,NSWP,k+"-nsw","NSW peptide ER surge","1,180 visits; retatrutide mentioned in 833.")
    bpcli=lambda R,k:li(R,BPCP,k+"-bpcpol","BPC-157 and the HHS peptide policy","Published Oct 30: what it does and doesn\'t do.")
    sub(pages,"peptides/retatrutide.html",N,N+nswli("../","reta"))
    sub(pages,"peptides/bpc-157.html",N,N+bpcli("../","bpc"))
    sub(pages,"peptides/bpc-157-tb-500-stack.html",N,N+bpcli("../","stack"))
    sub(pages,FDAL,N,N+bpcli("","fda")+nswli("","fda"))
    D='<p class="disclaimer">'
    co=lambda html:f'<p class="calc-callout">{html}</p>'+D
    for s in ("retatrutide-side-effects","retatrutide-fda-approval-status"):
        sub(pages,f"peptides/{s}.html",D,co(f'<strong>New:</strong> NSW Health counted 1,180 peptide-linked ER visits, with retatrutide mentioned in 833. <a href="../{NSWP}" data-goatcounter-click="{s}-to-nsw">See the numbers</a>.'))
    sub(pages,LEGIT,D,co(f'<strong>Why it matters:</strong> <a href="{NSWP}" data-goatcounter-click="legit-to-nsw">peptide ER visits in NSW went from 5 a month to 217</a>. And <a href="{BPCP}" data-goatcounter-click="legit-to-bpcpol">BPC-157 and the HHS peptide policy</a>'))
LLMS=[("NSW peptide ER surge",NSWP,"NSW Health surveillance: 1,180 ED presentations mentioning unapproved peptides (Jul 2025–Sep 2026), retatrutide in 833, with caveats and sources."),
      ("BPC-157 and the HHS peptide policy",BPCP,"HHS's 503A peptide enforcement-discretion policy (FR doc 2026-22192, docket HHS-OASH-2026-0496): cleared OIRA Oct 27, published Oct 30, 2026 (91 FR 68526); covers BPC-157, epitalon, KPV, MOTS-c, semax, TB-500 (Appendix A); comments close Nov 13, 2026; who it covers, what it doesn't do.")]
CARDS={NSWP:dict(card="nsw-peptide-surge",kicker="News · Australia",title="Peptide ER visits: 5 a month to 217",sub="NSW Health data: retatrutide mentioned in 833 of 1,180.",badge="",badge_t="",hot=True),
       BPCP:dict(card="bpc-157-policy",kicker="News · FDA",title="BPC-157 and the HHS peptide policy",sub="Published Oct 30: six peptides. What it does and doesn't do.",badge="",badge_t="",hot=True)}
