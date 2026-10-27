# Oct 18 2026: compounded vs brand-name semaglutide/tirzepatide beginner guide
from newpages import faqld,faqh,crumbs,signup,SUB,CALC,LEGIT,BESAFE,FDA_ERR
from extras import DM,WEG,ZEP
CB="compounded-vs-brand-semaglutide-tirzepatide.html"
OZI="adec4fd2-6858-4c99-91d4-531f5f2a2d79"; MJI="d2d7da5d-ad07-4228-955f-cf7e355c8cc0"
FDA_C="https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-concerns-unapproved-glp-1-drugs-used-weight-loss"
FDA_QA="https://www.fda.gov/drugs/human-drug-compounding/compounding-and-fda-questions-and-answers"
FDA_NDC="https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory"
FDA_SHORT="https://www.fda.gov/drugs/drug-alerts-and-statements/fda-clarifies-policies-compounders-national-glp-1-supply-begins-stabilize"
FDA_POL="https://www.fda.gov/drugs/human-drug-compounding/human-drug-compounding-policies-and-rules"
OSP="https://doi.org/10.1002/osp4.70200"
NDCQ="https://www.accessdata.fda.gov/scripts/cder/ndc/"
CB_FAQ=[
("How do I know if my semaglutide is compounded?",'Check the label. Brand-name semaglutide injections are Ozempic and Wegovy, made by Novo Nordisk and sold as prefilled pens. If your label names a compounding pharmacy or outsourcing facility instead, or your semaglutide came in a vial, it\'s compounded.'),
("Does Zepbound come in a vial?",f'Yes. Lilly sells Zepbound and Mounjaro in single-dose and multi-dose vials as well as pens, per their <a href="{DM(ZEP)}" rel="noopener">DailyMed listings</a>. So a vial alone doesn\'t mean tirzepatide is compounded. Check that the label says Zepbound or Mounjaro and Eli Lilly.'),
("Is compounded semaglutide the same as Ozempic?",f'No. The FDA says compounded drugs are not FDA-approved and don\'t go through its review for safety, effectiveness or quality before they\'re sold. It also flags any company claiming its compounded drug is "the same as" an FDA-approved one as a red flag (<a href="{FDA_C}" rel="noopener">FDA</a>).'),
("Does an NDC number mean my drug is FDA-approved?",f'No. The FDA says an NDC number "does not in any way denote FDA approval." Outsourcing facilities can choose to assign NDCs to compounded drugs too (<a href="{FDA_NDC}" rel="noopener">FDA NDC Directory</a>). Look the number up and check the brand name and maker it belongs to.'),
("What's the difference between a 503A and a 503B pharmacy?",f'503A is a state-licensed pharmacy (or a physician) compounding mainly under state board of pharmacy oversight. 503B is an FDA-registered outsourcing facility, inspected by the FDA on a risk-based schedule and held to current good manufacturing practice (CGMP) standards (<a href="{FDA_QA}" rel="noopener">FDA</a>). Neither one makes the product FDA-approved.'),
]
def guide(BASE,ORG,DISC):
    url=f"{BASE}/{CB}"
    body=f'''<article class="issue"><p class="crumbs"><a href="index.html">Home</a> / <a href="peptides/index.html">Peptide guides</a> / Compounded or brand-name?</p>
<p class="kicker">Beginner's guide · GLP-1s</p><h1>Compounded or brand-name semaglutide or tirzepatide? How to tell in two minutes</h1>
<p><span class="badge approved">Semaglutide: FDA-approved</span> <span class="badge approved">Tirzepatide: FDA-approved</span> <span class="fine">The brand-name versions. Compounded versions are not FDA-approved. Checked against FDA and DailyMed Oct 18, 2026</span></p>
<p class="lead">Grab your box, your vial or your pen. Two minutes from now you'll know exactly what you've got: Ozempic, Wegovy, Mounjaro or Zepbound, or a compounded version made by a pharmacy. Here's the label check, the NDC trick and what the FDA actually says.</p>
<aside class="excite" aria-label="The 30-second version"><p class="kicker">The 30-second version</p><ul>
<li><strong>Brand name and maker on the label:</strong> Ozempic or Wegovy from <strong>Novo Nordisk</strong>, Mounjaro or Zepbound from <strong>Eli Lilly</strong>. A pharmacy's name as the maker means compounded.</li>
<li><strong>Semaglutide in a vial?</strong> Compounded. Brand semaglutide injections come as prefilled pens.</li>
<li><strong>Tirzepatide in a vial?</strong> Could be either. Lilly sells Zepbound and Mounjaro vials too, so read the label.</li>
<li><strong>Look up the NDC</strong> in the FDA's NDC Directory and check which product and company it belongs to.</li></ul></aside>
<h2>You're not the only one who isn't sure</h2>
<p>A University of Michigan study in <em>Obesity Science &amp; Practice</em> (Sept 2026) asked 322 U.S. adults on weekly semaglutide or tirzepatide injections to upload a photo of their medication. Blinded reviewers classified 83 of them (25.78%) as using a compounded product. Of those 83, <strong>54 (65.06%) had self-reported using one of the four brand-name products</strong> (<a href="{OSP}" rel="noopener">Katz, Gearhardt &amp; Griauzde, Obes Sci Pract, 2026</a>).</p>
<p class="fine">An online study recruited through the Prolific research platform, with a small compounded group. The authors call for larger, more diverse samples.</p>
<h2>The brand-name lineup</h2>
<p>These are the FDA-approved injections. If your product isn't one of these, it's not the brand drug.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">Brand-name semaglutide and tirzepatide injections</caption><thead><tr><th scope="col">Brand</th><th scope="col">Drug</th><th scope="col">Maker</th><th scope="col">How it comes</th><th scope="col">NDC starts with</th></tr></thead><tbody>
<tr><th scope="row"><a href="{DM(OZI)}" rel="noopener">Ozempic</a></th><td>Semaglutide</td><td>Novo Nordisk</td><td>Prefilled pen</td><td>0169</td></tr>
<tr><th scope="row"><a href="{DM(WEG)}" rel="noopener">Wegovy</a></th><td>Semaglutide</td><td>Novo Nordisk</td><td>Prefilled pen</td><td>0169</td></tr>
<tr><th scope="row"><a href="{DM(MJI)}" rel="noopener">Mounjaro</a></th><td>Tirzepatide</td><td>Eli Lilly</td><td>Pen, KwikPen, single-dose or multi-dose vial</td><td>0002</td></tr>
<tr><th scope="row"><a href="{DM(ZEP)}" rel="noopener">Zepbound</a></th><td>Tirzepatide</td><td>Eli Lilly</td><td>Pen, KwikPen, single-dose or multi-dose vial</td><td>0002</td></tr></tbody></table></div>
<p class="fine">Package types and NDC labeler codes from the manufacturers' DailyMed listings, checked Oct 18, 2026. A licensed repackager can relabel genuine brand product under its own NDC prefix, so look up any other prefix. Semaglutide also comes as tablets (Rybelsus and Wegovy tablets), which this guide doesn't cover.</p>
<h2>Step 1: read the label and packaging</h2><ul>
<li><strong>Brand name and company.</strong> Brand products print the brand name and the drug company. Compounded products are labeled by the compounder: the FDA's own warnings describe "the compounding pharmacies identified on the labels" of compounded semaglutide and tirzepatide (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>Pen or vial.</strong> The FDA says compounders sell semaglutide in "multiple-dose vials and prefilled syringes," often in different concentrations (<a href="{FDA_ERR}" rel="noopener">FDA</a>). Brand semaglutide injections are pens only. For tirzepatide, Lilly-made vials exist, so the label is what counts.</li>
<li><strong>Extra ingredients.</strong> Vitamin B12, B6, L-carnitine or NAD on the label? The FDA says some compounders add these to semaglutide, and the safety and effectiveness of those combinations "has not been established" (<a href="{FDA_ERR}" rel="noopener">FDA</a>). The brand drugs don't contain them.</li>
<li><strong>"Semaglutide sodium" or "semaglutide acetate."</strong> These salt forms are different active ingredients from the approved drugs, and the FDA says it isn't aware of any lawful basis for compounding with them (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>Doses in units or mL instead of a preset pen dose?</strong> That's the vial life. Use our <a href="{CALC}">peptide reconstitution calculator</a> to check the math on your prescribed dose.</li></ul>
<h2>Step 2: check the NDC number</h2>
<p>The National Drug Code (NDC) is the FDA's three-segment ID number for a drug product, printed on the box or label (<a href="{FDA_NDC}" rel="noopener">FDA</a>).</p><ul>
<li><strong>Look it up</strong> in the FDA's <a href="{NDCQ}" rel="noopener">NDC Directory</a> and check that the product name and company match what's on your box.</li>
<li><strong>An NDC doesn't mean approved.</strong> In the FDA's words, assigning an NDC "does not in any way denote FDA approval of the product." Outsourcing facilities can choose to assign NDCs to compounded drugs too, so what matters is <em>which</em> product the number belongs to.</li></ul>
<h2>Step 3: check the prescription and the pharmacy</h2><ul>
<li><strong>Read your prescription or order.</strong> Does it say Ozempic, Wegovy, Mounjaro or Zepbound, or just "semaglutide" or "tirzepatide" from a compounding pharmacy? Ask the prescriber or telehealth service which one you're getting. The FDA tells patients to contact the compounder or telehealth platform with any questions about the label (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>503A or 503B?</strong> A 503A compounder is a state-licensed pharmacy (or physician), mainly overseen by the state board of pharmacy. A 503B outsourcing facility is registered with the FDA, inspected on a risk-based schedule and held to CGMP manufacturing standards. Either way, the product is not FDA-approved (<a href="{FDA_QA}" rel="noopener">FDA</a>).</li>
<li><strong>Use a state-licensed pharmacy.</strong> The FDA's <a href="{BESAFE}" rel="noopener">BeSafeRx</a> checklist: a valid prescription required, a U.S. address and phone number, and a licensed pharmacist to answer questions.</li></ul>
<h2>What the FDA says about compounded GLP-1s</h2><ul>
<li><strong>Not FDA-approved.</strong> The FDA does not review compounded drugs for safety, effectiveness or quality before they're sold, and says they should only be used when a patient's needs can't be met by an FDA-approved drug (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>The shortages are over.</strong> The FDA declared the semaglutide shortage resolved on Feb 21, 2025. Its grace periods for compounders making essentially copies of the approved drugs ended in 2025: for outsourcing facilities, March 19 for tirzepatide and May 22 for semaglutide (<a href="{FDA_SHORT}" rel="noopener">FDA</a>). In April 2026 the FDA proposed excluding semaglutide and tirzepatide from the 503B bulk substances list (<a href="{FDA_POL}" rel="noopener">FDA</a>).</li>
<li><strong>Adverse event reports.</strong> As of May 31, 2026, the FDA had received 990 reports linked to compounded semaglutide and more than 730 linked to compounded tirzepatide, and says these are likely underreported (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>Fakes exist.</strong> The FDA has found fraudulent compounded semaglutide and tirzepatide naming pharmacies that don't exist or didn't make the product, and counterfeit Ozempic (<a href="{FDA_C}" rel="noopener">FDA</a>).</li>
<li><strong>Vial rules.</strong> Throw a multiple-dose vial away 28 days after first use, even if some is left. Use a new sterile needle and syringe every time. Don't use an injectable GLP-1 that arrives warm (<a href="{FDA_C}" rel="noopener">FDA</a>).</li></ul>
<h2>The FDA's red flags</h2><p>The FDA says to watch for a company that (<a href="{FDA_C}" rel="noopener">FDA</a>):</p><ul>
<li>claims its compounded drug is the same as an FDA-approved drug</li>
<li>offers prices that seem too good to be true</li>
<li>sends medicine that looks different from before, or arrives broken, damaged or without instructions</li>
<li>doesn't require a screening and a prescription from a licensed doctor</li>
<li>has spelling errors on the label, a wrong pharmacy address, or a pharmacy name you suspect is fake</li></ul>
<p>Looking at a lab report for something other than a prescription drug? Our <a href="{LEGIT}">guide to checking a lab report</a> shows how to read a COA.</p>
<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>
<li><a href="peptides/semaglutide.html" data-goatcounter-click="next-cb-sema"><strong>Semaglutide guide</strong><span>Ozempic, Wegovy and Rybelsus: the trials, plainly.</span></a></li>
<li><a href="peptides/tirzepatide.html" data-goatcounter-click="next-cb-tirz"><strong>Tirzepatide guide</strong><span>Mounjaro and Zepbound: the dual agonist explained.</span></a></li>
<li><a href="{CALC}" data-goatcounter-click="next-cb-calc"><strong>Peptide reconstitution calculator</strong><span>The vial math for your prescribed dose.</span></a></li>
<li><a href="semaglutide-vs-tirzepatide.html" data-goatcounter-click="next-cb-vs"><strong>Semaglutide vs tirzepatide</strong><span>Who won the head-to-head, and where retatrutide fits.</span></a></li>
<li><a href="{SUB}" data-goatcounter-click="next-cb-signup" rel="noopener"><strong>Get the Friday email</strong><span>The week's biggest peptide news, free, in five minutes.</span></a></li></ul></nav>
{signup("signup-cb")}
<h2 id="faq">Compounded vs brand FAQ</h2>{faqh(CB_FAQ)}{DISC}</article>'''
    t="Compounded or brand-name semaglutide & tirzepatide? How to tell"
    d="Is your semaglutide or tirzepatide compounded or Ozempic, Wegovy, Mounjaro or Zepbound? Check the label, pen vs vial and the NDC, plus what the FDA says."
    cites=[{"@type":"WebPage","name":"FDA's Concerns with Unapproved GLP-1 Drugs Used for Weight Loss","url":FDA_C},
           {"@type":"WebPage","name":"Compounding and the FDA: Questions and Answers","url":FDA_QA},
           {"@type":"WebPage","name":"National Drug Code Directory","url":FDA_NDC},
           {"@type":"WebPage","name":"FDA clarifies policies for compounders as national GLP-1 supply begins to stabilize","url":FDA_SHORT},
           {"@type":"ScholarlyArticle","name":"Improving Medication Classification in GLP-1RA Research: Feasibility of a Photo-Review Protocol","sameAs":OSP}]
    schema=[ORG,{"@type":"MedicalWebPage","name":"Compounded or brand-name semaglutide or tirzepatide? How to tell","description":d,"url":url,"inLanguage":"en","lastReviewed":"2026-10-18","publisher":{"@id":BASE+"/#org"},
           "about":[{"@type":"Drug","name":"Semaglutide"},{"@type":"Drug","name":"Tirzepatide"}],"citation":cites},
        {"@type":"Article","headline":"Compounded or brand-name semaglutide or tirzepatide? How to tell in two minutes","description":d,"url":url,"inLanguage":"en","datePublished":"2026-10-18","dateModified":"2026-10-18","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
        faqld(CB_FAQ),crumbs(BASE,[("Peptide guides",BASE+"/peptides/"),("Compounded or brand-name?",url)])]
    return (t,d,body,schema)
def add(pages,BASE,ORG,DISC):
    pages[CB]=guide(BASE,ORG,DISC)
def wire(pages):
    from newpages2 import sub
    for s in ("semaglutide","tirzepatide"):
        a='<nav class="next-up" aria-label="Keep going"><h2>Keep going</h2><ul>'
        sub(pages,f"peptides/{s}.html",a,a+f'<li><a href="../{CB}" data-goatcounter-click="next-{s}-cb"><strong>Compounded or brand-name?</strong><span>How to tell what\'s in your box in two minutes.</span></a></li>')
    sub(pages,CALC,'<h2>The math, plainly</h2>',f'<p class="calc-callout"><strong>Not sure if your vial is compounded or brand-name?</strong> <a href="{CB}" data-goatcounter-click="calc-to-cb">Here\'s how to tell in two minutes</a>.</p><h2>The math, plainly</h2>')
LLMS=[("Compounded or brand-name semaglutide & tirzepatide? How to tell",CB,"Beginner guide: label and packaging checks (pens vs vials), NDC lookup, 503A vs 503B, and what the FDA says about compounded GLP-1s.")]
CARDS={CB:dict(card="compounded-vs-brand",kicker="Beginner's guide · GLP-1s",title="Compounded or brand-name? How to tell",sub="Label, pen vs vial, NDC. Two minutes, total clarity.",badge="",badge_t="",hot=True)}
