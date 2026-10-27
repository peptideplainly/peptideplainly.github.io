# Oct 27 2026: FDA warning letters & safety alerts on peptide sellers (fda.gov-verified entries only)
from newpages import faqld,faqh,crumbs,signup
import fdalist as F
a=F.a; P="peptide-recalls-and-fda-warning-letters.html"; URL="https://peptideplainly.com/"+P
WL="https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/"
# (iso date, recipient, products named, exact FDA quote, slug)  -- each verified on fda.gov Oct 27, 2026
E=[
("2026-08-24","TXP Innovations LLC dba Tex Peptides","Semaglutide, tirzepatide, retatrutide, SS-31, tesamorelin, PT-141, bacteriostatic water","These products are especially concerning from a public health perspective because injectable drug products can pose risks of serious harm to users.","txp-innovations-llc-dba-tex-peptides-735067-08242026"),
("2026-08-24","Royal Peptides LLC","Tirzepatide, semaglutide, retatrutide, SS-31, PT-141, tesamorelin, \"BIMORELIN\"","…are unapproved new drugs under section 505(a) of the Federal Food, Drug, and Cosmetic Act (FD&C Act)","royal-peptides-llc-734884-08242026"),
("2026-03-31","Gram Peptides","Retatrutide, tirzepatide, bacteriostatic water","Despite statements on your product labeling marketing your products for \u201cResearch Use Only,\u201d and \u201cnot intended for human consumption, medical use, or veterinary use,\u201d evidence obtained from your website establishes that your products are intended to be drugs for human use.","gram-peptides-721806-03312026"),
("2025-09-09","GLP-1 Solution","Retatrutide, compounded semaglutide and tirzepatide","your retatrutide drug products are unapproved new drugs and misbranded drugs","glp-1-solution-715883-09092025"),
("2025-02-26","USApeptide.com","Semaglutide, tirzepatide","Unapproved new drugs do not carry the same assurances of safety and effectiveness as those drugs subject to FDA oversight.","usapeptidecom-696885-02262025"),
]
def fmt(d):
    import datetime as dt; return dt.date.fromisoformat(d).strftime("%b %-d, %Y")
FAQ=[("Does \"research use only\" make a peptide legal to sell for people?",f'Not according to these letters. FDA says labels like "research use only" don\'t override evidence from a seller\'s website that products are intended for human use (see the {a(WL+E[2][4],"Gram Peptides letter")}).'),
("Why are there no recalls listed?","We only list items we've verified on fda.gov with a direct link. We haven't yet found an FDA recall notice specific to the peptides we cover. When we do, it goes here with its date and link.")]
def page(BASE,ORG,DISC):
    rows="".join(f'<li><p><strong><time datetime="{d}">{fmt(d)}</time> · {r}</strong><br><span class="fine">Products named: {prod}</span></p><blockquote class="pull"><p>"{q}"</p><p class="fine">{a(WL+s,"FDA warning letter")}</p></blockquote></li>' for d,r,prod,q,s in E)
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / FDA warning letters</p>
<p class="kicker">Enforcement watch · checked Oct 27, 2026</p><h1>Peptide recalls and FDA warning letters</h1>
<p class="lead"><strong>What the FDA has actually said about peptide sellers</strong>, quoted word for word and linked to fda.gov. No rumors, no screenshots.</p>
<h2 id="letters">FDA warning letters</h2><p>Letters FDA sent to online sellers of peptide products. A warning letter is FDA's notice of violations it observed; it isn't a court finding.</p>
<ol class="wl">{rows}</ol>
<h2 id="recalls">Recalls</h2><p>None listed yet. We only add recalls we can link on fda.gov, and we haven't found one specific to the peptides we cover. FDA's full list is at {a("https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts","Recalls, Market Withdrawals, & Safety Alerts")}.</p>
<h2 id="fda-resources">FDA resources on fake and unapproved GLP-1s</h2><ul>
<li>{a(F.FDA_C,"FDA's Concerns with Unapproved GLP-1 Drugs Used for Weight Loss")}: counterfeit and fraudulent products, and why retatrutide and cagrilintide can't be compounded.</li>
<li>{a("https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters","FDA Warning Letters database")}: search any company by name.</li>
<li>Checking a product's paperwork? See <a href="how-to-tell-if-a-peptide-source-is-legit.html">how to check a lab report</a>.</li></ul>
<p>Status changes live on our <a href="peptide-fda-status-tracker.html">FDA status tracker</a>.</p>
{signup("signup-warnings")}
<h2 id="faq">FAQ</h2>{faqh(FAQ)}{DISC}</article>'''
    t="Peptide recalls and FDA warning letters, quoted and linked"
    d="FDA warning letters to online peptide sellers (semaglutide, tirzepatide, retatrutide and more), quoted word for word with fda.gov links."
    schema=[ORG,{"@type":"WebPage","name":t,"description":d,"url":URL,"inLanguage":"en","dateModified":"2026-10-27","publisher":{"@id":BASE+"/#org"},"citation":[{"@type":"WebPage","url":WL+s} for *_,s in E]},faqld(FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("FDA warning letters",URL)])]
    return (t,d,body,schema)
def add(pages,BASE,ORG,DISC):
    pages[P]=page(BASE,ORG,DISC)
    from newpages2 import sub
    sub(pages,"peptide-fda-status-tracker.html",'<h2 id="status">',f'<p class="calc-callout"><strong>Enforcement:</strong> <a href="{P}">FDA warning letters to peptide sellers</a>, quoted and linked.</p><h2 id="status">')
    sub(pages,"how-to-tell-if-a-peptide-source-is-legit.html",'<h2 id="fda-tools">',f'<p class="calc-callout"><strong>What FDA has said:</strong> <a href="{P}">warning letters to "research use only" peptide sellers</a>.</p><h2 id="fda-tools">')
    h2='<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'
    sub(pages,"peptides/index.html",h2,h2+f'<section class="wide two" aria-label="FDA warning letters"><a class="tile" href="../{P}"><h3>FDA warning letters</h3><p>What FDA told peptide sellers, quoted and linked.</p></a></section>')
LLMS=[("Peptide recalls and FDA warning letters",P,"FDA warning letters to online peptide sellers, quoted exactly with fda.gov links; recalls section lists only fda.gov-verified items.")]
CARDS={P:dict(card="fda-warning-letters",kicker="Enforcement watch · FDA",title="Peptide FDA warning letters",sub="What FDA told sellers, quoted and linked.",badge="",badge_t="",hot=False)}
