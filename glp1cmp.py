"""GLP-1 comparison page: semaglutide vs tirzepatide vs retatrutide vs orforglipron.
Every number comes from a cited PubMed abstract or the FDA label on DailyMed (checked Oct 16, 2026)."""
import html,re
from extras import DM,OZ,RYB,WEG,MOU,ZEP
from extras2 import FOU
def pmid(i): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">PMID {i}</a>'
def lab(s,t): return f'<a href="{DM(s)}" rel="noopener">{t}</a>'
ROWS=[
("semaglutide","Semaglutide",("approved","FDA-approved"),
 "Weekly shot (Ozempic, Wegovy) or daily pill (Rybelsus, Ozempic tablets, Wegovy tablets)",
 "GLP-1 receptor (1 hormone target). A peptide.",
 f'<strong>−14.9%</strong> average body weight at 68 weeks on 2.4 mg weekly vs −2.4% on placebo (STEP 1, {pmid(33567185)}). The Wegovy pill hit <strong>−13.6%</strong> at 64 weeks vs −2.2% (OASIS 4, {pmid(40934115)}).',
 f'{lab(OZ,"Ozempic")}, {lab(WEG,"Wegovy")} (shot &amp; pill), {lab(RYB,"Rybelsus / Ozempic tablets")}',
 "Wegovy label: shot steps up from 0.25 mg to a usual 2.4 mg weekly; pill steps up from 1.5 mg to 25 mg daily."),
("tirzepatide","Tirzepatide",("approved","FDA-approved"),
 "Weekly shot",
 "GIP + GLP-1 receptors (2 hormone targets). A peptide.",
 f'<strong>−20.9%</strong> average body weight at 72 weeks on 15 mg vs −3.1% on placebo (SURMOUNT-1, {pmid(35658024)}). Head-to-head, <strong>−20.2% vs −13.7%</strong> for semaglutide (SURMOUNT-5, {pmid(40353578)}).',
 f'{lab(MOU,"Mounjaro")}, {lab(ZEP,"Zepbound")}',
 "Zepbound label: starts at 2.5 mg weekly, steps up by 2.5 mg at least every 4 weeks, maintenance 5, 10 or 15 mg."),
("retatrutide","Retatrutide",("research","Investigational (research only)"),
 "Weekly shot (clinical trials only)",
 "GIP + GLP-1 + glucagon receptors (3 hormone targets). A peptide.",
 f'<strong>−25.0%</strong> average body weight at 80 weeks on 12 mg vs −3.9% on placebo (TRIUMPH-1, {pmid(42814954)}). The biggest average number of the four.',
 "None yet. Lilly plans to file with the FDA in early 2027.",
 "No approved human dose. Trials used 4, 9 or 12 mg weekly, stepped up under medical supervision."),
("orforglipron","Orforglipron",("approved","FDA-approved"),
 "Daily pill, with or without food",
 "GLP-1 receptor (1 hormone target). A small molecule, not a peptide.",
 f'<strong>−11.2%</strong> average body weight at 72 weeks on the top dose vs −2.1% on placebo (ATTAIN-1, {pmid(40960239)}).',
 f'{lab(FOU,"Foundayo")} (approved April 1, 2026)',
 "Foundayo label: starts at 0.8 mg daily, steps up at least every 30 days, maximum 17.2 mg daily."),
]
FAQ=[
("Which GLP-1 causes the most weight loss?","On average, retatrutide posted the biggest number: −25.0% at 80 weeks on 12 mg in TRIUMPH-1. But it's still investigational. Among approved drugs, tirzepatide leads: −20.9% at 72 weeks on 15 mg in SURMOUNT-1, and it beat semaglutide head-to-head in SURMOUNT-5 (−20.2% vs −13.7%)."),
("Is there a GLP-1 weight-loss pill?","Yes, two. The Wegovy pill (semaglutide 25 mg, approved December 2025) averaged −13.6% at 64 weeks in OASIS 4. Foundayo (orforglipron, approved April 2026) averaged up to −11.2% at 72 weeks in ATTAIN-1, and its label says it can be taken with or without food."),
("Is retatrutide FDA-approved?","Not yet. As of October 2026 it's investigational. Lilly reported positive Phase 3 results and plans to submit it to the FDA in early 2027. There's no approved human dose."),
("What's the difference between semaglutide and tirzepatide?","Semaglutide acts on one hormone receptor (GLP-1). Tirzepatide acts on two (GIP and GLP-1). In the SURMOUNT-5 head-to-head trial, tirzepatide produced more average weight loss at 72 weeks."),
("What's the difference between Ozempic and Wegovy?","Both are semaglutide from Novo Nordisk. Ozempic (shot or tablet) is approved for type 2 diabetes. Wegovy (shot or pill) is approved for weight management and heart-risk reduction, with its own doses."),
("Is orforglipron a peptide?","No. Orforglipron is a small-molecule drug that hits the same GLP-1 receptor as semaglutide. That's part of why it can be a simple daily pill."),
("Can you compare these trial numbers directly?","Only loosely. Each trial had different people, doses and lengths (64 to 80 weeks). The only head-to-head trial among these four is SURMOUNT-5, tirzepatide vs semaglutide."),
]
TITLE="GLP-1s: semaglutide vs tirzepatide vs retatrutide vs orforglipron"
DESC="Semaglutide, tirzepatide, retatrutide and orforglipron side by side: weight-loss results, pills vs shots, receptors and FDA status."
def build(BASE,ORG,DISC):
    trs="".join(f'<tr><th scope="row"><a href="peptides/{s}.html">{n}</a></th><td><span class="badge {bk}">{bt}</span></td><td>{how}</td><td>{mech}</td><td>{res}</td><td>{brands}</td><td>{dose}</td></tr>' for s,n,(bk,bt),how,mech,res,brands,dose in ROWS)
    faqh="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)
    url=BASE+"/glp1-comparison.html"
    body=f'''<section class="wide"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / GLP-1 comparison</p>
<p class="kicker">Spotlight · weight loss</p><h1>Semaglutide vs tirzepatide vs retatrutide vs orforglipron</h1>
<p class="lead">These four are rewriting weight loss. Trials have shown average drops of 11% to 25% of body weight, and you can now pick a weekly shot or a daily pill. Here's how the big four stack up, with every number linked to its source.</p>
<ul class="glp1-top"><li><strong>Biggest average result:</strong> retatrutide, −25.0% in TRIUMPH-1 (still in trials).</li><li><strong>Strongest approved drug:</strong> tirzepatide (Zepbound), −20.9% in SURMOUNT-1, and it beat semaglutide head-to-head.</li><li><strong>The original:</strong> semaglutide (Ozempic, Wegovy), now as a shot or a pill, with heart protection shown in SELECT.</li><li><strong>Easiest pill:</strong> orforglipron (Foundayo), once a day with or without food.</li></ul>
<div class="table-wrap"><table class="compare glp1-table"><caption class="sr">GLP-1 comparison table</caption><thead><tr><th scope="col">Drug</th><th scope="col">Status (U.S.)</th><th scope="col">How it's taken</th><th scope="col">How it works</th><th scope="col">Headline weight-loss result</th><th scope="col">Approved brands</th><th scope="col">Dosing</th></tr></thead><tbody>{trs}</tbody></table></div>
<p class="fine">Trial results are average changes in body weight in adults with obesity and without diabetes. The trials differ in people, doses and length, so compare loosely. The only head-to-head trial here is SURMOUNT-5. Dosing summaries come from the FDA labels on DailyMed. Your prescriber sets your dose. Checked against official sources Oct 16, 2026.</p>
<h2>Read the full guides</h2><ul>{"".join(f'<li><a href="peptides/{s}.html">{n}</a>: results, label dosing, side effects and FAQs</li>' for s,n,*_ in ROWS)}</ul>
<h2 id="faq">GLP-1 comparison FAQ</h2>{faqh}{DISC}</section>'''
    strip=lambda a:html.unescape(re.sub('<[^>]+>','',a))
    schema=[ORG,{"@type":"MedicalWebPage","name":TITLE,"description":DESC,"url":url,"inLanguage":"en","lastReviewed":"2026-10-16","publisher":{"@id":BASE+"/#org"},"about":[{"@type":"Drug","name":n} for _,n,*_ in ROWS]},
     {"@type":"Article","headline":TITLE,"description":DESC,"url":url,"datePublished":"2026-10-16","dateModified":"2026-10-16","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
     {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in FAQ]},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Peptide guides","item":BASE+"/peptides/"},{"@type":"ListItem","position":3,"name":"GLP-1 comparison","item":url}]}]
    return (TITLE,DESC,body,schema)
