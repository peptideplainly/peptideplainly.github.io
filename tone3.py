"""Batch 3 sitewide tone pass (Oct 18, 2026): bold headlines, general-audience framing, one-line safety notes,
trimmed regulatory copy. Facts only from sources already cited on each page (or linked here)."""
from extras import pm
LEGIT="../how-to-tell-if-a-peptide-source-is-legit.html"
FDA_RISK="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks"
WADA='<a href="https://www.wada-ama.org/en/prohibited-list" rel="noopener">WADA</a>'
JUL26="https://www.fda.gov/advisory-committees/advisory-committee-calendar/july-23-24-2026-meeting-pharmacy-compounding-advisory-committee-07232026"
VOTES="https://www.peptides.media/updates/pcac-july-2026-vote-results"
COSM="https://www.fda.gov/cosmetics/cosmetics-laws-regulations/fda-authority-over-cosmetics-how-cosmetics-are-not-fda-approved-are-fda-regulated"
DSUP="https://www.fda.gov/food/information-consumers-using-dietary-supplements/questions-and-answers-dietary-supplements"
def line(risks,status="Not FDA-approved; sold for research only."):
    return f'<p class="safety-line"><strong>{status}</strong> Known risks: {risks}. <a href="{LEGIT}">Choose a tested source.</a></p>'
def nodose(extra=""):
    return f'<h2 id="dosing">Dosage</h2><p>There\'s <strong>no established human dose</strong>, so we don\'t list one.{(" "+extra) if extra else ""}</p>'
VOTE=f'In July 2026 an FDA advisory committee voted to recommend allowing it in pharmacy compounding (<a href="{JUL26}" rel="noopener">FDA meeting page</a>; <a href="{VOTES}" rel="noopener">vote report</a>). The vote is non-binding.'
REG={
"bpc-157":f'<strong>Not FDA-approved.</strong> {VOTE} Banned in sport ({WADA}).',
"tb-500":f'<strong>Neither TB-500 nor thymosin beta-4 is FDA-approved.</strong> {VOTE.replace("allowing it","allowing TB-500")} Banned in sport ({WADA}).',
"mots-c":f'<strong>Not FDA-approved.</strong> {VOTE} Banned in sport ({WADA}).',
"semax":f'<strong>Not FDA-approved.</strong> {VOTE}',
"cjc-1295-ipamorelin":f'<strong>Neither is FDA-approved.</strong> Both are banned in sport ({WADA}).',
"ghk-cu":f'A staple skincare ingredient (often listed as "copper tripeptide-1"); cosmetics <a href="{COSM}" rel="noopener">don\'t need FDA premarket approval</a>. Injectable GHK-Cu isn\'t an FDA-approved drug.',
"collagen-peptides":f'Sold as a dietary supplement. The FDA <a href="{DSUP}" rel="noopener">doesn\'t approve supplements</a> before they\'re sold.',
}
ONE={
"bpc-157":line(f'not well studied; there\'s no clinical safety data in people yet; the review also flags risks from unregulated manufacturing and contamination ({pm(40756949,"Vasireddi et al., HSS Journal 2025")})'),
"tb-500":line(f'not well studied; FDA found no human exposure data for the TB-500 fragment (<a href="{FDA_RISK}" rel="noopener">FDA</a>)'),
"mots-c":line('not well studied; there are no published human treatment trials yet'),
"semax":line(f'not well studied; for the routes people use, FDA says it has little or no safety information (<a href="{FDA_RISK}" rel="noopener">FDA</a>)'),
"cjc-1295-ipamorelin":line(f'FDA has identified serious adverse events with CJC-1295, including increased heart rate and a whole-body flushing reaction (<a href="{FDA_RISK}" rel="noopener">FDA</a>)'),
"ghk-cu":line(f'for injectable use, possible immune reactions and limited human data (<a href="{FDA_RISK}" rel="noopener">FDA</a>). On the skin, use products as directed',status="Injectable GHK-Cu isn't FDA-approved; sold for research only."),
}
DOSE={
"bpc-157":nodose("Most numbers online trace back to rat and mouse studies dosed by body weight."),
"tb-500":nodose("Online numbers mostly come from animal studies."),
"mots-c":nodose("A registered Phase 2a trial (NCT07505745) may give the first real human data."),
"semax":nodose("The main human study used it in hospital stroke rehab."),
"cjc-1295-ipamorelin":nodose("The human studies dosed by body weight in research settings."),
"ghk-cu":'<h2 id="dosing">How it\'s used</h2><p><strong>Skincare:</strong> serums and creams, used as directed on the label. <strong>Injectable:</strong> there\'s no established human dose, so we don\'t list one.</p>',
}
H1={
"semaglutide":"Semaglutide (Ozempic, Wegovy): the GLP-1 that started the weight-loss revolution",
"tirzepatide":"Tirzepatide (Mounjaro, Zepbound): the shot that beat semaglutide head-to-head",
"orforglipron":"Orforglipron (Foundayo): the no-needle GLP-1 pill, results & how to take it",
"bpc-157":"BPC-157: the cult recovery peptide, and what the research shows",
"tb-500":"TB-500 (thymosin beta-4): the repair peptide athletes swear by",
"ghk-cu":"GHK-Cu: the copper peptide behind glowing-skin routines",
"collagen-peptides":"Collagen peptides: the skin supplement with 26 trials behind it",
"cjc-1295-ipamorelin":"CJC-1295 & ipamorelin: the famous GH stack, and what studies show",
"mots-c":"MOTS-c: the 'exercise in a vial' mitochondrial peptide",
"semax":"Semax: the nasal brain peptide that raised BDNF in a clinical study",
"pt-141":"PT-141 (bremelanotide): the desire drug that works on the brain, not blood flow",
"tesamorelin":"Tesamorelin (Egrifta): the GH-boosting peptide that cut deep belly fat in trials",
}
# General-audience framing: benefits first, approved indication as one short line, populations kept accurate.
EXCITE={
"tesamorelin":("Your own growth hormone, turned up. Deep belly fat, down.",["<strong>Visceral belly fat fell 15.2%</strong> in 26 weeks, while it rose 5.0% on placebo (412-person clinical trial in adults with HIV-associated fat gain).","<strong>IGF-1 rose 81%</strong> and triglycerides improved in the same trial.","FDA-approved (as Egrifta) for excess belly fat in adults with HIV lipodystrophy."],"The GH-boosting peptide that cut deep belly fat 15% in a trial."),
"pt-141":("Works on desire in the brain, not blood flow.",["Improved desire and cut distress vs placebo in two Phase 3 trials (<strong>1,267</strong> premenopausal women with low desire).","Taken only when needed, at least 45 minutes before sex.","FDA-approved (as Vyleesi) for low sexual desire (HSDD) in premenopausal women."],"The desire drug that acts in the brain. As-needed, FDA-approved."),
"semax":("The nasal-spray peptide for brain and focus.",["<strong>Higher BDNF</strong>, a brain growth factor, and better daily-function scores in a 110-patient clinical study (stroke rehab).","Lots of lab work on brain gene activity.","Used for decades in Russian research."],"The nasal brain peptide. Raised BDNF in a clinical study."),
}
QUICK={
"tesamorelin":{"Status":"<strong>Status:</strong> FDA-approved (as Egrifta) for excess belly fat in adults with HIV lipodystrophy.","For athletes":"<strong>For athletes:</strong> banned in sport (WADA)."},
"pt-141":{"Status":"<strong>Status:</strong> FDA-approved (as Vyleesi) for low sexual desire (HSDD) in premenopausal women."},
"collagen-peptides":{"Status":"<strong>Status:</strong> a dietary supplement."},
"ghk-cu":{"Status":"<strong>Status:</strong> a familiar skincare ingredient. Injectable use is research-only."},
}
PEPREG={
"tesamorelin":lambda r: r,  # placeholder, replaced below
}
def apply(PEP,X,EX,INTRO):
    for k,t in REG.items(): p=list(PEP[k]); p[3]=t; PEP[k]=tuple(p)
    for k,v in ONE.items(): X[k]["dosing"]=v+DOSE[k]
    for k,h in H1.items(): X[k]["h1"]=h
    for k,e in EXCITE.items(): EX[k]=e
    for k,fx in QUICK.items():
        X[k]["quick"]=[next((v for lab,v in fx.items() if q.startswith(f"<strong>{lab}:")),q) for q in X[k]["quick"]]
    for k in X:
        X[k]["quick"]=[q.replace(" Everything else is off-label.","").replace(" Not for men or postmenopausal women.","") for q in X[k]["quick"]]
        X[k]["dosing"]=X[k]["dosing"].replace("<strong>Your prescriber sets your dose.</strong> This is a summary of the official FDA label to help you follow along, not a plan to start, change, or stop anything.","<strong>From the official FDA label.</strong> Your prescriber sets your dose.")
    # Shorter approved-drug status lines, indication kept exact
    for k,old,new in [
     ("tesamorelin",None,'<strong>FDA-approved</strong> (as Egrifta, first in 2010) for excess belly fat in adults with HIV lipodystrophy (<a href="{EGR}" rel="noopener">Egrifta WR label</a>). Other uses are off-label. Banned in sport ({WADA}).'),
     ("pt-141",None,'<strong>FDA-approved</strong> (2019, as Vyleesi) for acquired, generalized low sexual desire (HSDD) that causes distress in premenopausal women (<a href="{VYL}" rel="noopener">Vyleesi label</a>). The label doesn\'t cover men or postmenopausal women. "PT-141" research vials aren\'t Vyleesi.')]:
        import re
        r=PEP[k][3]; links=re.findall(r'href="([^"]+)"',r)
        lab=next((u for u in links if "dailymed" in u or "accessdata" in u or "label" in u.lower()),links[0] if links else "")
        p=list(PEP[k]); p[3]=new.replace("{EGR}",lab).replace("{VYL}",lab).replace("{WADA}",WADA); PEP[k]=tuple(p)
