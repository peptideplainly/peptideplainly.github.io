"""Traffic pages (Oct 17, 2026): retatrutide side effects (JAMA Netw Open), GLP-1 units calculator, legit-source guide.
Every figure is copied from the source linked next to it. Checked Oct 17, 2026."""
import html,re
SUB="https://peptideplainly.beehiiv.com/subscribe"
JAMA="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2855285"
PENN="https://www.engineering.upenn.edu/stories/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1/"
FDA_ERR="https://www.fda.gov/drugs/human-drug-compounding/fda-alerts-health-care-providers-compounders-and-patients-dosing-errors-associated-compounded"
FDA_GLP1="https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-concerns-unapproved-glp-1-drugs-used-weight-loss"
BESAFE="https://www.fda.gov/consumers/consumer-updates/how-buy-medicines-safely-online-pharmacy"
ISO="https://www.iso.org/ISO-IEC-17025-testing-and-calibration-laboratories.html"
def pm(i,label): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{label}</a>, PMID {i}'
SE="peptides/retatrutide-side-effects.html"; CALC="glp1-units-calculator.html"; LEGIT="how-to-tell-if-a-peptide-source-is-legit.html"
def strip(a): return html.unescape(re.sub('<[^>]+>','',a))
def faqld(F): return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in F]}
def faqh(F): return "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in F)
def crumbs(BASE,items): return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate([("Home",BASE+"/")]+items)]}
def signup(tag): return f'<div class="nl-cta"><h2>Get the next big peptide study first</h2><p>New results like this, explained plainly in five minutes, every Friday. Free.</p><p><a class="btn" href="{SUB}" data-goatcounter-click="{tag}" rel="noopener">Get the Friday email</a></p></div>'

# ---- a) Retatrutide side effects (JAMA Network Open, Oct 14 2026) ----
TOP=[("Increased appetite",1336,"17.1"),("Fatigue",1188,"15.2"),("Increased energy",970,"12.4"),("Nausea",907,"11.6"),("Food cravings",571,"7.3"),("Insomnia",475,"6.1"),("Raised heart rate",374,"4.8"),
     ("Hunger",366,"4.7"),("Constipation",354,"4.5"),("Diarrhea",345,"4.4"),("Bloating (abdominal distension)",331,"4.2"),("Malaise",318,"4.1"),("Muscle growth (muscle hypertrophy)",317,"4.1"),("Weight increased",305,"3.9"),("Anxiety",301,"3.8"),("Fast heartbeat (tachycardia)",294,"3.8")]
SE_FAQ=[("What are the most common retatrutide side effects people report online?",f'In the Penn team\'s JAMA Network Open study of Reddit posts, the most common self-reported symptoms were increased appetite (17.1% of 7,823 users), fatigue (15.2%), increased energy (12.4%), nausea (11.6%), food cravings (7.3%), insomnia (6.1%) and a raised heart rate (4.8%).'),
("Is this study a clinical trial?","No. It's a cross-sectional analysis of public Reddit posts, where people described their own experiences. Nobody's product, dose or health history could be verified. The authors call the findings hypothesis-generating."),
("How is this different from the retatrutide trials?","In the phase 2 obesity trial, gastrointestinal events (nausea, diarrhea, vomiting and constipation) were most common. In the Reddit posts, gut symptoms were common but not dominant. Appetite, energy, sleep, heart-rate and muscle-related reports stood out more."),
("Why would people report increased appetite on a weight-loss drug?","The authors call it unexpected and don't have an answer yet. They list possible explanations, including product or dose differences, stacking several peptides, reconstitution practices, who posts on Reddit, or symptoms blamed on the drug that came from something else."),
("Is retatrutide FDA-approved?","No. It's investigational and in phase 3 trials. The study notes the FDA has warned that nonapproved retatrutide products are being sold directly to consumers, including ones labeled for research or not for human consumption.")]
def side_effects(BASE,ORG,DISC,NOTE,badge):
    bk,bt=badge; url=f"{BASE}/{SE}"
    rows="".join(f'<tr><th scope="row">{n}</th><td>{c:,}</td><td>{p}%</td></tr>' for n,c,p in TOP)
    cite=f'<a href="{JAMA}" rel="noopener">Sehgal et al., JAMA Network Open, Oct 14, 2026</a>'
    body=f'''<article class="guide cat-weight"><p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Peptide guides</a> / <a href="retatrutide.html">Retatrutide</a> / Side effects</p>
<p class="kicker">New study · Oct 14, 2026</p><h1>Retatrutide side effects: what 13,589 people said online</h1>
<p><span class="badge {bk}">{bt}</span> <span class="fine">Checked against the published paper Oct 17, 2026</span></p>
<p class="lead">Retatrutide is the triple-agonist shot everyone's watching, and thousands of people are already posting about it. A University of Pennsylvania team just ran those posts through AI and published the first systematic look at what users say they feel. Here's what they found.</p>
<aside class="excite" aria-label="The headline numbers"><p class="kicker">The headline numbers</p><ul>
<li><strong>148,640</strong> retatrutide posts and comments from <strong>38,936</strong> Reddit users across 27 communities were analyzed.</li>
<li><strong>13,589</strong> users described currently taking retatrutide.</li>
<li><strong>7,823</strong> of them (57.6%) reported at least one symptom, after the researchers set aside expected effects like weight loss and appetite suppression.</li>
<li>Top reports: <strong>increased appetite, fatigue, increased energy, nausea, food cravings, insomnia and a raised heart rate.</strong></li></ul></aside>
<div class="quick"><h2>Quick facts</h2><ul>
<li><strong>Study:</strong> "Self-Reported Adverse Effects Among Social Media Users Taking Nonapproved Retatrutide," {cite}. A University of Pennsylvania team, with Boston Children's Hospital and Harvard Medical School.</li>
<li><strong>Type:</strong> a cross-sectional analysis of public Reddit posts. Self-reported, not a trial.</li>
<li><strong>Method:</strong> large language models flagged posts about personal use and matched each symptom to standard medical terms (MedDRA). A manual check of 100 posts showed high precision and recall.</li>
<li><strong>Window:</strong> posts from May 2021 to December 2025. Reports of current use dated March 10, 2023 to December 31, 2025.</li>
<li><strong>What the authors say:</strong> the findings are <em>hypothesis-generating</em> and flag signals worth formal drug-safety follow-up.</li></ul></div>
<h2>The most reported retatrutide side effects</h2>
<p>Share of the 7,823 users who described at least one symptom. One person can report several.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">Most common self-reported retatrutide symptoms</caption><thead><tr><th scope="col">Symptom (as reported)</th><th scope="col">Users</th><th scope="col">Share</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="fine">Source: Table in {cite}. Plain-English labels; the paper uses MedDRA terms such as "Energy increased," "Food craving" and "Heart rate increased."</p>
<h2>By body system</h2><ul>
<li><strong>Gut:</strong> 32.5% of users reported a gastrointestinal symptom. Nausea led (11.6%), then constipation (4.5%), diarrhea (4.4%) and bloating (4.2%).</li>
<li><strong>Mood and sleep:</strong> 30.3% reported a psychiatric-category symptom, led by insomnia (6.1%) and anxiety (3.8%).</li>
<li><strong>Heart:</strong> "heart rate increased" came up for 4.8% of users, and 5.9% reported a cardiac-category symptom such as a fast heartbeat (3.8%) or palpitations (1.9%).</li>
<li><strong>Muscle:</strong> 14.4% reported a musculoskeletal symptom. Muscle growth (4.1%) was the most common, ahead of muscle loss (2.0%).</li></ul>
<h2>The surprise: it doesn't look like the trials</h2>
<p>In the phase 2 obesity trial, gut effects (nausea, diarrhea, vomiting and constipation) were the most common side effects. On Reddit, gut symptoms were common but not dominant. Appetite, general (fatigue, energy), muscle, sleep and heart-rate reports stood out instead. The pattern also differed from the same team's earlier Reddit study of semaglutide and tirzepatide, where reports were more concentrated in nausea, vomiting and gut-motility categories. The authors suggest the difference <em>may</em> come from retatrutide's extra target, the glucagon receptor, since it's the only triple agonist in its class. They also flag the appetite finding as unexpected, given the big weight losses in trials.</p>
<h2>Read this before you quote it</h2>
<p>These are things people wrote online about products they bought outside the trials. The researchers point out that product identity, purity, dose and medical history couldn't be verified, and that the results may reflect dose or product differences, stacking several peptides, reconstitution practices, who posts on Reddit, or symptoms blamed on the drug that came from something else. So the study can't tell you how often a side effect happens, whether retatrutide caused it, or how it compares to approved GLP-1s. It's a map of what to test next, and prospective studies are the next step.</p>
<p>Want the trial data? Our <a href="retatrutide.html">retatrutide guide</a> covers the phase 3 TRIUMPH results, status and FAQs. Comparing options? See <a href="../glp1-comparison.html">all four GLP-1s side by side</a>. Thinking about where a vial came from? Read <a href="../{LEGIT}">how to tell if a peptide source is legit</a>.</p>
{signup("signup-reta-side-effects")}
<h2 id="faq">Retatrutide side effects FAQ</h2>{faqh(SE_FAQ)}
<p class="fine">Sources: {cite} (doi:10.1001/jamanetworkopen.2026.38929); <a href="{PENN}" rel="noopener">Penn Engineering news release</a>.</p>{NOTE}{DISC}</article>'''
    t="Retatrutide side effects: what 13,589 users reported (JAMA 2026)"
    d="Retatrutide side effects people report online: increased appetite, fatigue, energy, nausea, cravings, insomnia, raised heart rate. Penn's JAMA study."
    schema=[ORG,{"@type":"MedicalWebPage","name":"Retatrutide side effects: what 13,589 people said online","description":d,"url":url,"inLanguage":"en","lastReviewed":"2026-10-17","publisher":{"@id":BASE+"/#org"},"about":{"@type":"Drug","name":"Retatrutide"},
        "citation":{"@type":"ScholarlyArticle","name":"Self-Reported Adverse Effects Among Social Media Users Taking Nonapproved Retatrutide","url":JAMA,"datePublished":"2026-10-14","isPartOf":{"@type":"Periodical","name":"JAMA Network Open"},"sameAs":"https://doi.org/10.1001/jamanetworkopen.2026.38929"}},
        {"@type":"Article","headline":"Retatrutide side effects: what 13,589 people said online","description":d,"url":url,"datePublished":"2026-10-17","dateModified":"2026-10-17","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(SE_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Retatrutide",BASE+"/peptides/retatrutide.html"),("Side effects",url)])]
    return (t,d,body,schema)

# ---- b) Semaglutide / tirzepatide mg -> mL -> units calculator ----
CALC_FAQ=[("How many units is 1 mL on an insulin syringe?","On a U-100 insulin syringe, 1 mL is 100 units, so 0.1 mL is 10 units and 0.01 mL is 1 unit. 'Units' on the syringe are a measure of volume, not of drug."),
("How do I convert mg to units?","Divide your prescribed dose in mg by your vial's concentration in mg per mL to get mL. Multiply mL by 100 to get units on a U-100 syringe. The concentration is the number that changes everything, so take it from your own vial label or pharmacy."),
("Why does the same dose come out to different units?","Because concentrations vary. FDA notes that compounded semaglutide can come in different concentrations, even from the same compounder, so the same mg dose can be a different number of units."),
("Does this calculator tell me what dose to take?","No. It only converts the dose your prescriber gave you. It never suggests a dose. Always follow your prescriber and pharmacist and double-check with them.")]
CALCJS=r'''<script>(function(){var f=document.getElementById("calc"),o=document.getElementById("calc-out"),mode=f.querySelectorAll("input[name=mode]");
function num(id){var v=document.getElementById(id).value.trim().replace(",",".");if(v==="")return NaN;var n=Number(v);return n>0&&isFinite(n)?n:NaN}
function r(x,d){return Number(x.toFixed(d)).toString()}
function sync(){var m=f.querySelector("input[name=mode]:checked").value;document.getElementById("m-conc").hidden=m!=="conc";document.getElementById("m-mix").hidden=m!=="mix";}
function go(e){if(e)e.preventDefault();var m=f.querySelector("input[name=mode]:checked").value,c,steps=[],dose=num("dose");
if(m==="conc"){c=num("conc");if(isNaN(c)){return say("Enter your vial's concentration in mg per mL (it's on the vial or pharmacy label).")}steps.push("Concentration = <b>"+r(c,4)+" mg/mL</b> (from your vial label)")}
else{var t=num("total"),w=num("water");if(isNaN(t)||isNaN(w)){return say("Enter the total mg in the vial and the mL of liquid added.")}c=t/w;steps.push("Concentration = "+r(t,4)+" mg ÷ "+r(w,4)+" mL = <b>"+r(c,4)+" mg/mL</b>")}
if(isNaN(dose)){return say("Enter the dose in mg that your prescriber gave you.",steps)}
var ml=dose/c,u=ml*100;steps.push("Volume = "+r(dose,4)+" mg ÷ "+r(c,4)+" mg/mL = <b>"+r(ml,4)+" mL</b>");steps.push("U-100 units = "+r(ml,4)+" mL × 100 = <b>"+r(u,2)+" units</b>");
var warn="";if(u>100)warn='<p class="calc-warn">That\'s more than one full U-100 syringe (100 units = 1 mL). Stop and check the numbers with your pharmacist.</p>';else if(u<1)warn='<p class="calc-warn">That\'s under 1 unit, too small to measure accurately on a U-100 syringe. Check with your pharmacist.</p>';
o.innerHTML='<p class="calc-big"><span>'+r(ml,4)+' mL</span><span>'+r(u,2)+' units</span></p><p class="fine">on a U-100 insulin syringe</p><ol class="calc-steps"><li>'+steps.join("</li><li>")+"</li></ol>"+warn+'<p class="calc-check"><strong>Always follow your prescriber and pharmacist; double-check with them</strong> before you draw anything up.</p>'}
function say(t,s){o.innerHTML=(s&&s.length?'<ol class="calc-steps"><li>'+s.join("</li><li>")+"</li></ol>":"")+'<p>'+t+"</p>"}
mode.forEach(function(x){x.addEventListener("change",function(){sync();go()})});f.addEventListener("input",function(){go()});f.addEventListener("submit",go);sync()})();</script>'''
def calculator(BASE,ORG,DISC):
    url=f"{BASE}/{CALC}"
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / Units calculator</p>
<p class="kicker">Free tool · math only</p><h1>Semaglutide &amp; tirzepatide calculator: mg to mL to units</h1>
<p class="lead">Got a vial and a dose in mg, but your syringe says "units"? Plug in your own numbers and see the exact math, step by step. No guessing, no mix-ups.</p>
<form id="calc" class="calc" novalidate><fieldset><legend>1. Your vial's strength</legend>
<label class="calc-opt"><input type="radio" name="mode" value="conc" checked> My label shows mg per mL</label>
<label class="calc-opt"><input type="radio" name="mode" value="mix"> I know the total mg and how much liquid was added</label>
<div id="m-conc"><label for="conc">Concentration (mg per mL)</label><input id="conc" inputmode="decimal" autocomplete="off" placeholder="from your vial label"></div>
<div id="m-mix" hidden><label for="total">Total mg in the vial</label><input id="total" inputmode="decimal" autocomplete="off" placeholder="from your vial label"><label for="water">mL of liquid added</label><input id="water" inputmode="decimal" autocomplete="off" placeholder="from your pharmacy instructions"></div></fieldset>
<fieldset><legend>2. Your prescribed dose</legend><label for="dose">Dose in mg (from your prescriber)</label><input id="dose" inputmode="decimal" autocomplete="off" placeholder="from your prescription"></fieldset>
<button class="btn" type="submit" data-goatcounter-click="calc-convert">Show my math</button></form>
<div id="calc-out" class="calc-out" aria-live="polite"><p>Your result and the full math will show here.</p></div>
<p class="calc-check"><strong>Always follow your prescriber and pharmacist; double-check with them.</strong> This tool does math only. It never suggests a dose, and it's for <strong>U-100 insulin syringes only</strong> (100 units = 1 mL).</p>
<h2>The math, plainly</h2><ol><li><strong>Concentration</strong> (mg/mL) = total mg in the vial ÷ mL of liquid in it. If your label already says mg/mL, use that.</li><li><strong>mL to draw</strong> = your prescribed dose in mg ÷ concentration in mg/mL.</li><li><strong>Units on a U-100 syringe</strong> = mL × 100.</li></ol>
<p>That's it. Three steps, and the concentration is the one that matters most: the same mg dose is a different number of units in a different-strength vial.</p>
<h2>Why people mix these up</h2><p>Milligrams (mg) measure the drug. Milliliters (mL) and syringe "units" measure liquid. The FDA has <a href="{FDA_ERR}" rel="noopener">received reports of dosing errors</a> with compounded semaglutide where people confused mg, mL and units, including patients told to draw 5 units (0.05 mL) on a U-100 syringe who drew 50 units instead. FDA says compounded concentrations can vary, even from one compounder, and that patients should talk with their prescriber or compounder about how to measure their dose. The FDA-approved pens (Ozempic, Wegovy) are dosed in mg and come prefilled.</p>
<p>New to these drugs? Read the <a href="peptides/semaglutide.html">semaglutide guide</a> and the <a href="peptides/tirzepatide.html">tirzepatide guide</a> for label dosing straight from the FDA, or <a href="glp1-comparison.html">compare all four GLP-1s</a>. Buying from a pharmacy you don't know? See <a href="{LEGIT}">how to tell if a source is legit</a>.</p>
{signup("signup-calc")}
<h2 id="faq">Units calculator FAQ</h2>{faqh(CALC_FAQ)}
<p class="fine">Sources: <a href="{FDA_ERR}" rel="noopener">FDA alert on compounded semaglutide dosing errors</a>; <a href="{FDA_GLP1}" rel="noopener">FDA's concerns with unapproved GLP-1 drugs</a>.</p>{DISC}</article>{CALCJS}'''
    t="Semaglutide & tirzepatide units calculator: mg to mL to units"
    d="Convert your semaglutide or tirzepatide dose from mg to mL to U-100 syringe units, using your own vial's strength. Math shown. Follow your prescriber."
    schema=[ORG,{"@type":"WebApplication","name":"Semaglutide & tirzepatide mg to mL to units calculator","url":url,"description":d,"applicationCategory":"HealthApplication","operatingSystem":"Any","isAccessibleForFree":True,"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"publisher":{"@id":BASE+"/#org"}},
        faqld(CALC_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Units calculator",url)])]
    return (t,d,body,schema)

# ---- c) How to tell if a peptide source is legit ----
LEGIT_FAQ=[("What is a COA for peptides?","A certificate of analysis: a lab report for one specific batch. A useful one names the compound, the batch or lot number, the testing lab, the test date, and results like HPLC purity and a mass-spec identity check."),
("Is HPLC purity enough?","No. HPLC purity tells you how much of the sample is one main compound. A mass spec identity check tells you that compound is the right molecule. You want both, plus how much is actually in the vial."),
("How do I verify a COA?","Match the lot number to your vial, then contact the testing lab named on the report (or use its online lookup, if it has one) and confirm the report number and results are real."),
("What are the biggest red flags?","No COA, a COA with no lot number or lab name, the same report used for every batch, prices that seem too good to be true, and prescription drugs sold without a prescription.")]
def legit(BASE,ORG,DISC):
    url=f"{BASE}/{LEGIT}"
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / Is your source legit?</p>
<p class="kicker">Buyer's guide</p><h1>How to tell if a peptide source is legit</h1>
<p class="lead">Great sources love showing their receipts. Here's how to read a COA in two minutes, check it's real, and spot the red flags, so you know exactly what's in the vial.</p>
<aside class="excite" aria-label="The 30-second version"><p class="kicker">The 30-second version</p><ul><li><strong>COA for your exact batch:</strong> the lot number on the report matches your vial.</li><li><strong>Purity and identity:</strong> HPLC purity <em>and</em> a mass spec check.</li><li><strong>Independent lab you can contact:</strong> named, dated, and verifiable.</li><li><strong>Prescription drug?</strong> A licensed pharmacy that asks for your prescription.</li></ul></aside>
<h2>Why it matters</h2><p>Testing is the whole game, and the research shows why:</p><ul>
<li>Researchers bought semaglutide vials from illegal online pharmacies with no prescription and tested them. Every vial contained endotoxin (a bacterial contaminant), measured purity was 7.7% to 14.37% against the 99% claimed on the labels, and the semaglutide content was 28.56% to 38.69% <em>above</em> the labeled amount ({pm(39509151,"Ashraf et al., J Med Internet Res, 2024")}).</li>
<li>Melanotan II vials from three online shops each claimed 10 mg. Testing found 4.32 to 8.84 mg, and vials from two shops held 4.1% to 5.9% unknown impurities ({pm(24771717,"Breindahl et al., Drug Test Anal, 2015")}).</li>
<li>Obestatin bought from five manufacturers by research groups: one product was a totally different peptide, and two-thirds of the rest fell short of research quality (under 95% purity and/or single impurities over 1%). The authors recommend quality-control testing before using any peptide in research ({pm(18342612,"De Spiegeleer et al., Anal Biochem, 2008")}).</li></ul>
<h2>What's on a good COA</h2><p>A certificate of analysis (COA) is the lab report for one batch. Look for:</p><ul>
<li><strong>Compound name</strong> and the amount the vial is supposed to hold.</li>
<li><strong>Batch or lot number</strong> that matches the number printed on <em>your</em> vial. A report for a different batch tells you nothing about yours.</li>
<li><strong>HPLC purity:</strong> high-performance liquid chromatography separates the sample and shows what share of it is the main compound, ideally with the chromatogram (the peak chart) attached.</li>
<li><strong>Mass spec identity:</strong> mass spectrometry checks that the main compound has the expected molecular mass, which means it's the right molecule. Purity alone can't tell you that. In the melanotan II study, identity was confirmed by mass spec, while LC-UV measured amount and impurities ({pm(24771717,"Breindahl 2015")}).</li>
<li><strong>Amount per vial:</strong> measured content, so you know the vial holds what the label says.</li>
<li><strong>Endotoxin result</strong> for anything injectable, since endotoxin turned up in every vial in the semaglutide study above.</li>
<li><strong>The lab's name, the test date</strong> and a report number.</li></ul>
<h2>Third-party testing: what "independent" should mean</h2><ul>
<li><strong>A separate lab</strong> from the seller, named on the report, with real contact details.</li>
<li><strong>Accreditation is a plus.</strong> <a href="{ISO}" rel="noopener">ISO/IEC 17025</a> is the international standard that lets testing labs show they work competently and produce valid results.</li>
<li><strong>Verify the report with the lab.</strong> Contact the lab named on the COA, or use its online lookup if it has one, and confirm the report number, compound, lot and results match.</li>
<li><strong>Fresh, batch-specific results.</strong> A new batch should come with its own report.</li></ul>
<h2>Red flags</h2><ul>
<li>No COA, or "available on request" that never arrives.</li>
<li>A COA with no lot number, no lab name, no date, or a lot number that doesn't match your vial.</li>
<li>The same report reused across batches or products.</li>
<li>Purity listed with no method, or HPLC purity with no identity check.</li>
<li>A lab that can't be found or won't confirm the report.</li>
<li>Prescription drugs sold without a prescription, prices that seem too good to be true, or no U.S. address and licensed pharmacist. These are the FDA's <a href="{BESAFE}" rel="noopener">warning signs of an unsafe online pharmacy</a>.</li></ul>
<h2>Approved drug? Use the pharmacy route</h2><p>For FDA-approved medicines like semaglutide and tirzepatide, the FDA's checklist for a <a href="{BESAFE}" rel="noopener">safe online pharmacy</a> is simple. It requires a prescription, lists a U.S. address and phone number, has a licensed pharmacist to answer questions, and is licensed by a state board of pharmacy, which you can check through FDA's BeSafeRx tool. Getting dosed from a vial? Our <a href="{CALC}">mg-to-units calculator</a> shows the math from your own label.</p>
<p>Next up: <a href="peptides/index.html">all our peptide guides</a>, <a href="peptides/retatrutide-side-effects.html">what retatrutide users report online</a>, or <a href="peptides-101.html">Peptides 101</a>.</p>
{signup("signup-legit")}
<h2 id="faq">Peptide source FAQ</h2>{faqh(LEGIT_FAQ)}{DISC}</article>'''
    t="How to tell if a peptide source is legit: COAs, testing, red flags"
    d="How to check a peptide source: what a real COA shows (lot match, HPLC purity, mass spec identity), how to verify third-party testing, and the red flags."
    schema=[ORG,{"@type":"Article","headline":"How to tell if a peptide source is legit","description":d,"url":url,"inLanguage":"en","datePublished":"2026-10-17","dateModified":"2026-10-17","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(LEGIT_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Is your source legit?",url)])]
    return (t,d,body,schema)

def add(pages,BASE,ORG,DISC,NOTE,X):
    pages[SE]=side_effects(BASE,ORG,DISC,NOTE,X["retatrutide"]["badge"])
    pages[CALC]=calculator(BASE,ORG,DISC)
    pages[LEGIT]=legit(BASE,ORG,DISC)
LLMS=[("Retatrutide side effects: what 13,589 users reported online",SE,"Penn's JAMA Network Open study (Oct 14, 2026) of self-reported symptoms in Reddit posts. Research purposes only."),
      ("Semaglutide & tirzepatide units calculator",CALC,"Math-only mg to mL to U-100 syringe units converter from your own vial concentration. No dose suggestions."),
      ("How to tell if a peptide source is legit",LEGIT,"COAs, HPLC purity, mass spec identity, third-party testing and red flags.")]
TILES=f'<section class="wide two" aria-label="Tools and buyer guides"><a class="tile" href="{{R}}{SE}"><h3>🔥 Retatrutide side effects</h3><p>What 13,589 users reported online, from the new JAMA study.</p></a><a class="tile" href="{{R}}{CALC}"><h3>mg → mL → units calculator</h3><p>Semaglutide &amp; tirzepatide math from your own vial label.</p></a><a class="tile" href="{{R}}{LEGIT}"><h3>Is your source legit?</h3><p>Read a COA in two minutes and spot the red flags.</p></a></section>'
def link_in(pages):
    def sub(k,a,b):
        v=list(pages[k]); assert a in v[2],(k,a); v[2]=v[2].replace(a,b,1); pages[k]=tuple(v)
    sub("peptides/index.html",'<section class="wide">\n<div class="chips"','<section class="wide"><h2>Tools &amp; buyer guides</h2></section>'+TILES.replace("{R}","../").replace(f'../{SE}',SE.split("/")[1])+'<section class="wide">\n<div class="chips"')
    sub("index.html",'<section id="this-week">','<section class="wide"><div class="sec-head"><h2>Trending tools &amp; guides</h2></div></section>'+TILES.replace("{R}","")+'<section id="this-week">')
CARDS={SE:dict(card="retatrutide-side-effects",kicker="New JAMA study · Oct 2026",title="Retatrutide side effects: what 13,589 users reported",sub="Appetite, fatigue, energy, nausea, insomnia, heart rate.",badge="research",badge_t="Research purposes only",hot=True),
 CALC:dict(card="glp1-units-calculator",kicker="Free tool · math only",title="Semaglutide & tirzepatide: mg → mL → units",sub="Your vial, your prescribed dose, the exact math.",badge="",badge_t="",hot=False),
 LEGIT:dict(card="legit-source",kicker="Buyer's guide",title="How to tell if a peptide source is legit",sub="COAs, HPLC purity, mass spec and red flags.",badge="",badge_t="",hot=False)}
def next_links(slug):
    L=[]
    if slug in ("semaglutide","tirzepatide"): L.append((CALC,"mg → mL → units calculator","Convert your prescribed dose using your own vial's strength.","calc"))
    if slug in ("semaglutide","tirzepatide","retatrutide","orforglipron"): L.append((SE,"Retatrutide side effects","What 13,589 users reported online, from the new JAMA study.","reta-se"))
    L.append((LEGIT,"Is your source legit?","Read a COA, verify third-party testing, spot the red flags.","legit"))
    li="".join(f'<li><a href="{"" if u.startswith("peptides/") else "../"}{u.split("/")[-1] if u.startswith("peptides/") else u}" data-goatcounter-click="next-{slug}-{tag}"><strong>{t}</strong><span>{d}</span></a></li>' for u,t,d,tag in L)
    return f'<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>{li}<li><a href="{SUB}" data-goatcounter-click="next-{slug}-signup" rel="noopener"><strong>Get the Friday email</strong><span>The week\'s biggest peptide news, free, in five minutes.</span></a></li></ul></nav>'
def link_guides(pages,slugs):
    for s in slugs:
        k=f"peptides/{s}.html"; v=list(pages[k]); a='<h2 id="faq">'; assert a in v[2]; v[2]=v[2].replace(a,next_links(s)+a,1); pages[k]=tuple(v)
