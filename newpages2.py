"""Traffic push 2 (Oct 17, 2026): semaglutide vs tirzepatide, retatrutide release date / FDA status,
calculator share block, calculator callouts, above-the-fold signup strip. Figures copied from the linked sources, checked Oct 17, 2026."""
import html,re
from newpages import SUB,CALC,SE,LEGIT,faqld,faqh,crumbs,signup
def pm(i,label): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{label}</a>'
VS="semaglutide-vs-tirzepatide.html"; REL="peptides/retatrutide-fda-approval-status.html"
LILLY_T4="https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-weight-loss-average"
LILLY_T1="https://www.prnewswire.com/news-releases/lillys-triple-agonist-retatrutide-delivered-powerful-weight-loss-in-pivotal-phase-3-obesity-trial-302778859.html"
LILLY_T23="https://www.prnewswire.com/news-releases/lillys-triple-agonist-retatrutide-successful-in-two-additional-phase-3-obesity-trials-delivering-significant-improvements-in-weight-and-a1c-302832674.html"
FDA_LTR="https://storage.courtlistener.com/recap/gov.uscourts.ca7.55916/gov.uscourts.ca7.55916.46.2.pdf"
def ct(n,label): return f'<a href="https://clinicaltrials.gov/study/{n}" rel="noopener">{label}</a>'

# ---- a) Semaglutide vs tirzepatide ----
VS_FAQ=[("Which is better for weight loss, semaglutide or tirzepatide?","In the only head-to-head trial, SURMOUNT-5, tirzepatide won: −20.2% average weight change at 72 weeks vs −13.7% for semaglutide, in 751 adults with obesity and no type 2 diabetes."),
("How much weight do people lose on semaglutide?","In STEP 1, adults on semaglutide 2.4 mg weekly averaged −14.9% at 68 weeks (−15.3 kg) vs −2.4% on placebo, alongside lifestyle intervention."),
("How much weight do people lose on tirzepatide?","In SURMOUNT-1, average weight change at 72 weeks was −15.0% on 5 mg, −19.5% on 10 mg and −20.9% on 15 mg, vs −3.1% on placebo."),
("What's the difference between how they work?","Semaglutide activates one hormone receptor, GLP-1. Tirzepatide activates two, GIP and GLP-1."),
("Are the side effects different?","In all three trials the most common side effects were gastrointestinal, mostly mild to moderate and mainly during dose escalation (SURMOUNT) or transient (STEP 1)."),
("Is retatrutide better than tirzepatide?","Nobody knows yet. Retatrutide's published trials (TRIUMPH-1: −25.0% on 12 mg at 80 weeks, counting dropouts) posted bigger average numbers than tirzepatide's SURMOUNT-1 (−20.9% on 15 mg at 72 weeks), but they were different trials and there's no head-to-head. Retatrutide is still investigational, with no approval date announced."),
("What about orforglipron?","See our four-way GLP-1 comparison for all the big names side by side, including the orforglipron pill.")]
RETA_SEC=f'''<h2 id="retatrutide">Where does retatrutide fit?</h2>
<p><span class="badge research">Investigational: not approved; only available in Lilly clinical trials</span> (<a href="https://www.lilly.com/news/stories/what-to-know-about-retatrutide" rel="noopener">Lilly</a>) Retatrutide is Lilly's triple agonist and the name everyone's searching next to these two. It has posted the biggest average weight-loss numbers of the three in its own trials. But it has <strong>never been tested head-to-head</strong> against semaglutide or tirzepatide, so the numbers below come from different trials with different people, lengths and dose arms. Compare loosely.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">Retatrutide published trial results</caption><thead><tr><th scope="col">Retatrutide trial</th><th scope="col">Who &amp; how long</th><th scope="col">Average weight change</th><th scope="col">Counts dropouts?</th></tr></thead><tbody>
<tr><th scope="row">Phase 2<br>{pm(37366315,"NEJM 2023")}</th><td>338 adults with obesity (or overweight plus a weight-related condition), 48 weeks</td><td><strong>−24.2%</strong> (12 mg arm) vs −2.1% on placebo</td><td>Not stated in the abstract (least-squares means)</td></tr>
<tr><th scope="row">TRIUMPH-1<br>{pm(42814954,"NEJM 2026")}</th><td>2,339 adults with obesity, no diabetes, 80 weeks</td><td>−17.6% (4 mg), −23.7% (9 mg), <strong>−25.0%</strong> (12 mg) vs −3.9% on placebo</td><td>Yes (treatment-regimen estimand, intention-to-treat)</td></tr>
<tr><th scope="row">TRIUMPH-2<br>{pm(42810372,"Lancet 2026")}</th><td>1,152 adults with obesity and type 2 diabetes, 80 weeks</td><td>−11.9% (4 mg), −16.8% (9 mg), <strong>−18.8%</strong> (12 mg) vs −5.1% on placebo</td><td>Yes (treatment-regimen estimand)</td></tr></tbody></table></div>
<p class="fine">Dose labels are the trial arm names, not dosing advice. There is no approved human dose of retatrutide.</p>
<ul><li><strong>Status:</strong> retatrutide is still investigational and not FDA-approved, and no approval date has been announced.</li><li><strong>Filing:</strong> in July 2026, Lilly said it plans to submit retatrutide to the FDA in Q1 2027 (<a href="{LILLY_T23}" rel="noopener">Lilly, July 23, 2026</a>).</li><li><strong>Side effects:</strong> in TRIUMPH-1 the most common adverse events were gastrointestinal.</li></ul>
<p>Track it: <a href="peptides/retatrutide-fda-approval-status.html">retatrutide release date &amp; FDA status</a> · <a href="peptides/retatrutide-side-effects.html">what users report online</a> · <a href="peptides/retatrutide.html">full retatrutide guide</a>. Want orforglipron too? <a href="glp1-comparison.html">All four GLP-1s side by side</a>.</p>'''
def vs(BASE,ORG,DISC,ROWS):
    RETA=RETA_SEC
    url=f"{BASE}/{VS}"; wl=ROWS[0][7]; zl=ROWS[1][7]
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / Semaglutide vs tirzepatide vs retatrutide</p>
<p class="kicker">Head-to-head · weight loss</p><h1>Semaglutide vs tirzepatide: who won the head-to-head, and where retatrutide fits</h1>
<p><span class="badge approved">Semaglutide: FDA-approved</span> <span class="badge approved">Tirzepatide: FDA-approved</span> <span class="badge research">Retatrutide: investigational, not approved</span> <span class="fine">Checked against the published trials Oct 18, 2026</span></p>
<p class="lead">Wegovy or Zepbound? Ozempic or Mounjaro? These two are the biggest names in weight loss, and they've actually gone toe to toe in a randomized trial. Here's who won, by how much, what the landmark trials showed for each, and where the triple-agonist retatrutide fits in.</p>
<aside class="excite" aria-label="The verdict"><p class="kicker">The verdict</p><p class="sa">Tirzepatide won the head-to-head.</p><ul>
<li><strong>−20.2% vs −13.7%</strong> average weight change at 72 weeks, tirzepatide vs semaglutide (SURMOUNT-5, 751 adults).</li>
<li><strong>−18.4 cm vs −13.0 cm</strong> off the waist.</li>
<li>Tirzepatide users were more likely to hit every big target: at least 10%, 15%, 20% and 25% weight loss.</li></ul></aside>
<h2>SURMOUNT-5: the head-to-head trial</h2>
<p>Published in the <em>New England Journal of Medicine</em> in 2025 ({pm(40353578,"Aronne et al., NEJM 2025, PMID 40353578")}). 751 adults with obesity and without type 2 diabetes were randomized 1:1 to the maximum tolerated weekly dose of tirzepatide (10 or 15 mg) or semaglutide (1.7 or 2.4 mg) for 72 weeks. It was an open-label phase 3b trial funded by Eli Lilly, the maker of tirzepatide.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">SURMOUNT-5 results at 72 weeks</caption><thead><tr><th scope="col">At 72 weeks</th><th scope="col">Tirzepatide</th><th scope="col">Semaglutide</th></tr></thead><tbody>
<tr><th scope="row">Average weight change</th><td><strong>−20.2%</strong></td><td>−13.7%</td></tr>
<tr><th scope="row">Average waist change</th><td><strong>−18.4 cm</strong></td><td>−13.0 cm</td></tr>
<tr><th scope="row">Counts dropouts?</th><td colspan="2">Not stated in the abstract (least-squares means)</td></tr>
<tr><th scope="row">Most common side effects</th><td colspan="2">Gastrointestinal in both groups, mostly mild to moderate, mainly during dose escalation</td></tr></tbody></table></div>
<h2>The landmark trial for each drug</h2>
<p>Each drug also has its own big placebo-controlled trial. These weren't head-to-head, and the people, doses and lengths differ, so compare them loosely.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">STEP 1 vs SURMOUNT-1</caption><thead><tr><th scope="col"></th><th scope="col">Semaglutide: STEP 1</th><th scope="col">Tirzepatide: SURMOUNT-1</th></tr></thead><tbody>
<tr><th scope="row">Source</th><td>{pm(33567185,"Wilding et al., NEJM 2021")}</td><td>{pm(35658024,"Jastreboff et al., NEJM 2022")}</td></tr>
<tr><th scope="row">Who</th><td>1,961 adults with obesity (or overweight plus a weight-related condition), no diabetes</td><td>2,539 adults with obesity (or overweight plus a weight-related complication), no diabetes</td></tr>
<tr><th scope="row">Length &amp; doses</th><td>68 weeks, 2.4 mg weekly vs placebo, plus lifestyle intervention</td><td>72 weeks, 5, 10 or 15 mg weekly vs placebo</td></tr>
<tr><th scope="row">Average weight change</th><td><strong>−14.9%</strong> (−15.3 kg) vs −2.4% on placebo</td><td><strong>−15.0%</strong> (5 mg), <strong>−19.5%</strong> (10 mg), <strong>−20.9%</strong> (15 mg) vs −3.1% on placebo</td></tr>
<tr><th scope="row">Big-loss club</th><td>50.5% lost 15% or more (vs 4.9% on placebo)</td><td>50% (10 mg) and 57% (15 mg) lost 20% or more (vs 3% on placebo)</td></tr>
<tr><th scope="row">Counts dropouts?</th><td>Yes (primary estimand: effect regardless of stopping treatment)</td><td>Yes (treatment-regimen estimand, intention-to-treat)</td></tr>
<tr><th scope="row">Stopped for side effects</th><td>4.5% stopped for GI events (vs 0.8% on placebo)</td><td>4.3%, 7.1% and 6.2% stopped for adverse events (vs 2.6% on placebo)</td></tr>
<tr><th scope="row">Most common side effects</th><td>Nausea and diarrhea, typically transient and mild to moderate</td><td>Gastrointestinal, mostly mild to moderate, mainly during dose escalation</td></tr></tbody></table></div>
{RETA}<h2>How they work</h2><ul><li><strong>Semaglutide</strong> (Ozempic, Wegovy, Rybelsus) activates <strong>one</strong> hormone receptor: GLP-1.</li><li><strong>Tirzepatide</strong> (Mounjaro, Zepbound) activates <strong>two</strong>: GIP and GLP-1.</li><li><strong>Retatrutide</strong> (investigational, Lilly) activates <strong>three</strong>: GIP, GLP-1 and glucagon.</li></ul>
<h2>Label dosing for weight management</h2><ul><li><strong>{wl}</strong></li><li><strong>{zl}</strong></li></ul><p class="fine">Copied from the FDA labels on DailyMed via our <a href="glp1-comparison.html">GLP-1 comparison</a>. Your prescriber sets your dose.</p>
<div class="calc-callout"><p><strong>Got a vial and a dose in mg?</strong> Our free <a href="{CALC}" data-goatcounter-click="calc-callout-vs">peptide reconstitution calculator</a> shows the math from your own vial label.</p></div>
<h2>Go deeper</h2><ul><li><a href="peptides/semaglutide.html">Semaglutide guide</a>: STEP 1, SELECT heart results, label dosing, FAQs.</li><li><a href="peptides/tirzepatide.html">Tirzepatide guide</a>: SURMOUNT trials, label dosing, FAQs.</li><li><a href="peptides/retatrutide.html">Retatrutide guide</a>, its <a href="peptides/retatrutide-fda-approval-status.html">release date &amp; FDA status</a> and <a href="peptides/retatrutide-side-effects.html">what users report online</a>.</li><li><a href="glp1-comparison.html">All four GLP-1s side by side</a>, including orforglipron, the daily pill.</li><li><a href="{LEGIT}">How to tell if a source is legit</a>.</li></ul>
{signup("signup-vs")}
<h2 id="faq">Semaglutide vs tirzepatide FAQ</h2>{faqh(VS_FAQ).replace("our four-way GLP-1 comparison",'our <a href="glp1-comparison.html">four-way GLP-1 comparison</a>')}{DISC}</article>'''
    t="Semaglutide vs tirzepatide vs retatrutide: weight-loss results"
    d="Semaglutide vs tirzepatide head-to-head (SURMOUNT-5: −20.2% vs −13.7%), plus where retatrutide fits from its NEJM and Lancet trials. Label dosing only."
    schema=[ORG,{"@type":"MedicalWebPage","name":"Semaglutide vs tirzepatide vs retatrutide: the numbers","description":d,"url":url,"inLanguage":"en","lastReviewed":"2026-10-18","publisher":{"@id":BASE+"/#org"},"about":[{"@type":"Drug","name":"Semaglutide"},{"@type":"Drug","name":"Tirzepatide"},{"@type":"Drug","name":"Retatrutide"}],
        "citation":[{"@type":"ScholarlyArticle","name":"Tirzepatide as Compared with Semaglutide for the Treatment of Obesity","sameAs":"https://doi.org/10.1056/NEJMoa2416394"},{"@type":"ScholarlyArticle","name":"Once-Weekly Semaglutide in Adults with Overweight or Obesity","sameAs":"https://doi.org/10.1056/NEJMoa2032183"},{"@type":"ScholarlyArticle","name":"Tirzepatide Once Weekly for the Treatment of Obesity","sameAs":"https://doi.org/10.1056/NEJMoa2206038"},{"@type":"ScholarlyArticle","name":"Retatrutide, a Triple Hormone Receptor Agonist, for Treatment of Obesity","sameAs":"https://doi.org/10.1056/NEJMoa2604169"},{"@type":"ScholarlyArticle","name":"Triple-Hormone-Receptor Agonist Retatrutide for Obesity - A Phase 2 Trial","sameAs":"https://doi.org/10.1056/NEJMoa2301972"},{"@type":"ScholarlyArticle","name":"Retatrutide in adults with obesity and type 2 diabetes (TRIUMPH-2): a double-blind, parallel-group, randomised, placebo-controlled, phase 3 trial","sameAs":"https://doi.org/10.1016/S0140-6736(26)01861-1"}]},
        {"@type":"Article","headline":"Semaglutide vs tirzepatide vs retatrutide: the numbers","description":d,"url":url,"datePublished":"2026-10-17","dateModified":"2026-10-18","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(VS_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Semaglutide vs tirzepatide vs retatrutide",url)])]
    return (t,d,body,schema)

# ---- b) Retatrutide release date & FDA approval status ----
REL_FAQ=[("When will retatrutide be released?","There's no release date yet. Lilly has said it plans to submit retatrutide to the FDA for U.S. approval in the first quarter of 2027. Lilly hasn't announced an approval or launch date, and we don't guess one."),
("Is retatrutide FDA-approved?","No. Retatrutide is investigational. Lilly says it cannot be legally sold or marketed for human use."),
("Has Lilly filed retatrutide with the FDA?","Not as of Lilly's latest update we found (July 23, 2026). Lilly said it was completing the manufacturing and quality (CMC) data package and planned to submit in Q1 2027."),
("Will retatrutide be reviewed as a drug or a biologic?","That's in dispute. Lilly plans a Biologics License Application (BLA). In an October 2, 2026 letter, FDA again concluded retatrutide is not a biological product and that an application would need to go under section 505 of the Federal Food, Drug, and Cosmetic Act. Lilly's legal challenge is ongoing."),
("How much weight did people lose in the retatrutide trials?","In TRIUMPH-1, published in NEJM, average weight change at 80 weeks was −17.6% (4 mg), −23.7% (9 mg) and −25.0% (12 mg) vs −3.9% on placebo.")]
def release(BASE,ORG,DISC,NOTE,badge):
    bk,bt=badge; url=f"{BASE}/{REL}"
    rows=[("2023","Phase 2 published",f'Retatrutide 12 mg averaged −24.2% at 48 weeks vs −2.1% on placebo in 338 adults ({pm(37366315,"NEJM 2023, PMID 37366315")}).'),
      ("May–Aug 2023","TRIUMPH phase 3 trials start",f'ClinicalTrials.gov start dates: TRIUMPH-3 May 30, TRIUMPH-1 July 10, TRIUMPH-2 July 11, TRIUMPH-4 Aug 1, 2023 ({ct("NCT05882045","NCT05882045")}, {ct("NCT05929066","NCT05929066")}, {ct("NCT05929079","NCT05929079")}, {ct("NCT05931367","NCT05931367")}). Lilly says the initial program enrolled more than 5,800 people.'),
      ("Dec 11, 2025","TRIUMPH-4: first phase 3 win",f'Obesity plus knee osteoarthritis, 68 weeks. 12 mg: <strong>−28.7%</strong> average weight (efficacy estimand; −23.7% treatment-regimen) and knee pain down 4.5 points on WOMAC at 9 mg (<a href="{LILLY_T4}" rel="noopener">Lilly</a>).'),
      ("May 21, 2026","TRIUMPH-1 topline",f'Obesity without diabetes, 80 weeks. 12 mg: <strong>−28.3%</strong> (efficacy estimand; −25.0% treatment-regimen), and 45.3% lost at least 30% of body weight (<a href="{LILLY_T1}" rel="noopener">Lilly</a>).'),
      ("July 23, 2026","TRIUMPH-2 &amp; TRIUMPH-3 topline, filing plan",f'Type 2 diabetes: up to <strong>−20.8%</strong>. Severe obesity with heart disease: up to <strong>−22.6%</strong> (efficacy estimand, 80 weeks). Lilly said it plans to submit a BLA to FDA in <strong>Q1 2027</strong> (<a href="{LILLY_T23}" rel="noopener">Lilly</a>).'),
      ("Sept 29, 2026","Full results published",f'TRIUMPH-1 in NEJM: −17.6%, −23.7% and −25.0% vs −3.9% on placebo ({pm(42814954,"PMID 42814954")}). TRIUMPH-2 in The Lancet: −11.9%, −16.8% and −18.8% vs −5.1% ({pm(42810372,"PMID 42810372")}). Both treatment-regimen estimand, online Sept 29.'),
      ("Oct 2, 2026","FDA: not a biologic",f'On remand from a federal court, FDA again concluded retatrutide is not a biological product, so an application would need to be submitted under section 505 of the FD&amp;C Act rather than as a BLA (<a href="{FDA_LTR}" rel="noopener">FDA letter, filed in the Seventh Circuit Oct 8, 2026</a>).')]
    tl="".join(f'<li><span class="tl-date">{d}</span><strong>{h}</strong><p>{x}</p></li>' for d,h,x in rows)
    body=f'''<article class="guide cat-weight"><p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Peptide guides</a> / <a href="retatrutide.html">Retatrutide</a> / FDA status</p>
<p class="kicker">Status tracker · updated Oct 17, 2026</p><h1>Retatrutide release date &amp; FDA approval status</h1>
<p><span class="badge {bk}">{bt}</span> <span class="fine">Not FDA-approved</span></p>
<p class="lead">Retatrutide has racked up phase 3 win after phase 3 win, with average weight loss up to −25.0% in its published TRIUMPH-1 results. So when can you actually get it? Here's exactly where it stands, with every date sourced.</p>
<aside class="excite" aria-label="Where it stands"><p class="kicker">Where it stands right now</p><ul>
<li><strong>Not FDA-approved.</strong> Lilly says retatrutide is investigational and can't be legally sold or marketed for human use.</li>
<li><strong>Filing:</strong> Lilly says it plans to submit to the FDA for U.S. approval in <strong>Q1 2027</strong>.</li>
<li><strong>Release date:</strong> none announced. Lilly hasn't given an approval or launch date, so we don't predict one.</li>
<li><strong>Five positive phase 3 studies</strong>, according to Lilly, and it says it has the clinical data to support global submissions for obesity, knee osteoarthritis pain and sleep apnea.</li></ul></aside>
<h2>The TRIUMPH timeline</h2><ol class="timeline">{tl}</ol>
<p class="fine">"Efficacy estimand" estimates the effect if everyone stayed on treatment; "treatment-regimen estimand" counts everyone randomized, including people who stopped. That's why Lilly's press-release numbers run higher than the published ones.</p>
<h2>What happens next</h2><ul>
<li><strong>Submission:</strong> Lilly says it is finishing the chemistry, manufacturing and controls (CMC) package and then plans to submit in Q1 2027.</li>
<li><strong>Pathway fight:</strong> Lilly wants retatrutide reviewed as a biologic (BLA). FDA's October 2 letter says it's a drug that needs a section 505 application. Lilly's legal challenge is ongoing in the U.S. Court of Appeals for the Seventh Circuit.</li>
<li><strong>More trials:</strong> Lilly is also studying retatrutide in type 2 diabetes, chronic low back pain, cardiovascular and kidney outcomes, and fatty liver disease (MASLD).</li></ul>
<h2>Can you get it now?</h2><p>Not legitimately. The only real retatrutide is Lilly's product in clinical trials. Products sold online are labeled for research purposes only, and their content isn't checked. If you're reading about people using it anyway, see <a href="retatrutide-side-effects.html">what 13,589 users reported online</a> and <a href="../{LEGIT}">how to tell if a source is legit</a>.</p>
<div class="calc-callout"><p><strong>On semaglutide or tirzepatide?</strong> Our <a href="../{CALC}" data-goatcounter-click="calc-callout-reta-status">units calculator</a> is the converter for semaglutide and tirzepatide vials.</p></div>
<p>Full trial results, myths and FAQs: our <a href="retatrutide.html">retatrutide guide</a>. Comparing options: <a href="../glp1-comparison.html">all four GLP-1s side by side</a>.</p>
{signup("signup-reta-status")}
<h2 id="faq">Retatrutide release date FAQ</h2>{faqh(REL_FAQ)}{NOTE}{DISC}</article>'''
    t="Retatrutide release date & FDA approval status (Oct 2026)"
    d="When will retatrutide be approved? Lilly plans to submit to FDA in Q1 2027. Every TRIUMPH phase 3 readout so far, the biologic dispute and what's next."
    schema=[ORG,{"@type":"MedicalWebPage","name":"Retatrutide release date & FDA approval status","description":d,"url":url,"inLanguage":"en","lastReviewed":"2026-10-17","publisher":{"@id":BASE+"/#org"},"about":{"@type":"Drug","name":"Retatrutide"}},
        {"@type":"Article","headline":"Retatrutide release date & FDA approval status","description":d,"url":url,"datePublished":"2026-10-17","dateModified":"2026-10-17","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(REL_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Retatrutide",BASE+"/peptides/retatrutide.html"),("FDA status",url)])]
    return (t,d,body,schema)

# ---- 2) Calculator share block ----
SHARE_URL="https://peptideplainly.com/peptide-reconstitution-calculator.html"
SHARE_TXT="Free peptide reconstitution calculator: vial mg + water mL to concentration, mL and syringe units, with the math shown"
from urllib.parse import quote
SHARE=f'''<section class="share" aria-label="Share this calculator"><h2>Share this calculator</h2><p>Know someone mixing up mg, mL and units? Send them the math.</p>
<div class="share-row"><button type="button" class="btn" id="share-copy" data-goatcounter-click="share-calc-copy">Copy link</button>
<a class="btn ghost" href="https://x.com/intent/post?text={quote(SHARE_TXT)}&amp;url={quote(SHARE_URL,safe='')}" target="_blank" rel="noopener" data-goatcounter-click="share-calc-x">Share on X</a>
<a class="btn ghost" href="https://www.reddit.com/submit?url={quote(SHARE_URL,safe='')}&amp;title={quote(SHARE_TXT)}" target="_blank" rel="noopener" data-goatcounter-click="share-calc-reddit">Share on Reddit</a></div>
<p class="fine" id="share-msg" aria-live="polite"></p></section>
<script>(function(){{var b=document.getElementById("share-copy"),m=document.getElementById("share-msg"),u="{SHARE_URL}",t="{SHARE_TXT}";
function copied(){{m.textContent="Link copied. Paste it anywhere."}}
function fallback(){{if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(u).then(copied,manual)}}else manual()}}
function manual(){{var i=document.createElement("input");i.value=u;document.body.appendChild(i);i.select();try{{document.execCommand("copy");copied()}}catch(e){{m.textContent="Copy this link: "+u}}i.remove()}}
b.addEventListener("click",function(){{if(navigator.share){{navigator.share({{title:document.title,text:t,url:u}}).catch(function(e){{if(e&&e.name!=="AbortError")fallback()}})}}else fallback()}})}})();</script>'''

# ---- callouts + signup strip ----
def calc_callout(kind,R,tag):
    txt="turns any vial's mg + water into mg/mL, mL and U-100 units. Plug in your own numbers. Math only."
    return f'<div class="calc-callout"><p><strong>🧮 Free tool:</strong> our <a href="{R}{CALC}" data-goatcounter-click="calc-callout-{tag}">peptide reconstitution calculator</a> {txt}</p></div>'
def strip(tag):
    return f'<div class="atf-signup"><p><strong>The Friday email.</strong> The week\'s biggest peptide news in five minutes. Free.</p><a class="btn" href="{SUB}" data-goatcounter-click="signup-atf-{tag}" rel="noopener">Get it free</a></div>'

def add(pages,BASE,ORG,DISC,NOTE,X,ROWS):
    pages[VS]=vs(BASE,ORG,DISC,ROWS)
    pages[REL]=release(BASE,ORG,DISC,NOTE,X["retatrutide"]["badge"])
def sub(pages,k,a,b):
    v=list(pages[k]); assert a in v[2],(k,a[:60]); v[2]=v[2].replace(a,b,1); pages[k]=tuple(v)
def wire(pages):
    # calculator share block, before the FAQ
    sub(pages,CALC,'<h2>The math, plainly</h2>',SHARE+'<h2>The math, plainly</h2>')
    # calculator callouts on GLP-1 guides (after Quick facts block)
    for s,kind in (("semaglutide","dose"),("tirzepatide","dose"),("retatrutide","vial"),("orforglipron","vial")):
        sub(pages,f"peptides/{s}.html",'<nav class="related glp1-compare"',calc_callout(kind,"../",s)+'<nav class="related glp1-compare"')
    sub(pages,"glp1-comparison.html",'<div class="table-wrap">',calc_callout("dose","","glp1-comparison")+'<div class="table-wrap">')
    sub(pages,SE,'<h2>The most reported retatrutide side effects</h2>',calc_callout("vial","../","reta-side-effects")+'<h2>The most reported retatrutide side effects</h2>')
    # cross-links: comparison <-> vs page; guides -> new pages
    sub(pages,"glp1-comparison.html",'<h2>Read the full guides</h2>','<p class="calc-callout"><strong>Just choosing between two?</strong> See <a href="semaglutide-vs-tirzepatide.html" data-goatcounter-click="cmp-to-vs">semaglutide vs tirzepatide: the head-to-head numbers</a>.</p><h2>Read the full guides</h2>')
    for s in ("semaglutide","tirzepatide"):
        sub(pages,f"peptides/{s}.html",'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>',f'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul><li><a href="../{VS}" data-goatcounter-click="next-{s}-vs"><strong>Semaglutide vs tirzepatide</strong><span>The head-to-head numbers from SURMOUNT-5.</span></a></li>')
    for s in ("retatrutide","orforglipron"):
        sub(pages,f"peptides/{s}.html",'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>',f'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul><li><a href="retatrutide-fda-approval-status.html" data-goatcounter-click="next-{s}-reta-status"><strong>Retatrutide release date</strong><span>FDA status and every phase 3 readout so far.</span></a></li>')
    sub(pages,SE,'Want the trial data? Our','Wondering when it will be approved? See the <a href="retatrutide-fda-approval-status.html">retatrutide release date &amp; FDA status tracker</a>. Want the trial data? Our')
    # home + guides index tiles
    T=lambda R:f'<section class="wide two" aria-label="GLP-1 deep dives"><a class="tile" href="{R}{VS}"><h3>Semaglutide vs tirzepatide</h3><p>Who won the head-to-head: −20.2% vs −13.7%.</p></a><a class="tile" href="{R}{REL}"><h3>Retatrutide release date</h3><p>FDA status and every phase 3 readout so far.</p></a></section>'
    sub(pages,"index.html",'<section class="wide"><div class="sec-head"><h2>Trending tools &amp; guides</h2></div></section>','<section class="wide"><div class="sec-head"><h2>Trending tools &amp; guides</h2></div></section>'+T(""))
    sub(pages,"peptides/index.html",'<section class="wide"><h2>Tools &amp; buyer guides</h2></section>','<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'+T("../").replace(f'../{REL}',REL.split("/")[1]))
    # home: calculator callout right under the hero
    sub(pages,"index.html",'</section>\n<section class="wide glp1"','</section>\n<div class="wide">'+calc_callout("dose","","home")+'</div>\n<section class="wide glp1"')
def signup_atf(pages,targets):
    for k,tag in targets:
        v=list(pages[k]); v[2]=strip(tag)+v[2]; pages[k]=tuple(v)
LLMS=[("Semaglutide vs tirzepatide vs retatrutide: the numbers",VS,"SURMOUNT-5 head-to-head (−20.2% vs −13.7% at 72 weeks), STEP 1 and SURMOUNT-1, plus retatrutide's published phase 2, TRIUMPH-1 and TRIUMPH-2 results (not head-to-head; retatrutide is investigational)."),
      ("Retatrutide release date & FDA approval status",REL,"Not FDA-approved. Lilly plans to submit in Q1 2027. TRIUMPH phase 3 timeline and the biologic classification dispute.")]
CARDS={VS:dict(card="semaglutide-vs-tirzepatide",kicker="Head-to-head · weight loss",title="Semaglutide vs tirzepatide vs retatrutide",sub="SURMOUNT-5: −20.2% vs −13.7%. Plus where retatrutide fits.",badge="",badge_t="",hot=True),
 REL:dict(card="retatrutide-fda-status",kicker="Status tracker · Oct 2026",title="Retatrutide release date & FDA status",sub="Lilly plans to submit in Q1 2027. Every readout so far.",badge="research",badge_t="Investigational · not approved",hot=True)}
