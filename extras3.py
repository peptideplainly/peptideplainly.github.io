"""Oct 18 2026: trending research-peptide guides (batch 1: Melanotan II). Every claim tied to a fetched PubMed abstract or official page."""
def pm(i,label): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{label}</a>'
SCEN="https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019/210797Orig1s000Approv.pdf"
MHRA_FOI="https://assets.publishing.service.gov.uk/media/669fbd3aa3c2a28abb50d55a/Final_Redaction_FOI_24_274.pdf"
LEGIT="../how-to-tell-if-a-peptide-source-is-legit.html"
def safety(items,legal):
    li="".join(f"<li>{x}</li>" for x in items)
    return f'<aside class="safety" aria-label="Safety and legal"><h2>Safety &amp; legal, in 20 seconds</h2><ul><li><strong>Legal status:</strong> {legal}</li>{li}<li><strong>Quality:</strong> research vials are unregulated. Here\'s <a href="{LEGIT}">how to tell if a source is legit</a>.</li></ul></aside>'
MT2_SAFE=safety([
 f'<strong>Moles:</strong> case reports describe new and darkening moles, including within 24 hours of a single injection ({pm(24334249,"Eur J Dermatol, 2014")}), and a melanoma diagnosed in a 20-year-old user who also used sunbeds ({pm(24355990,"Dermatology, 2014, single case")}). A 2017 review counted four such melanoma reports and said conclusive evidence of a link is lacking ({pm(28266027,"Int J Dermatol, 2017")}).',
 f'<strong>Rare but serious:</strong> priapism needing surgery ({pm(33460908,"Sex Med, 2021")}), and a renal infarction case, with rhabdomyolysis and kidney failure described before ({pm(31953620,"CEN Case Rep, 2020")}).'],
 f'not FDA-approved, and not approved as a tanning product. The UK regulator (MHRA) tells people using MT2 injections or nasal sprays to stop (<a href="{MHRA_FOI}" rel="noopener">MHRA, 2024</a>).')
PEP3={
"melanotan-2":("Melanotan II (MT2)","What is Melanotan II (MT2)? The 'tan jab' peptide behind the TikTok buzz: the tanning and libido studies, appetite research, risks and status.",
f"Melanotan II (MT2, MT-II) is a lab-made, ring-shaped version of alpha-melanocyte-stimulating hormone (α-MSH), the hormone that tells your skin to make pigment. It was first tested in people at the University of Arizona in the 1990s. It's a non-selective melanocortin-receptor agonist ({pm(31953620,'Peters et al., 2020')}), which is why it touches tanning, libido and appetite all at once.",
f'<strong>Not FDA-approved.</strong> MT2 isn\'t approved as a medicine or tanning product ({pm(28266027,"Int J Dermatol, 2017")}). Its cousin afamelanotide (also known as Melanotan I, {pm(41547183,"J Pharm Biomed Anal, 2026")}) <em>is</em> FDA-approved, as Scenesse (<a href="{SCEN}" rel="noopener">FDA approval, Oct 8, 2019</a>), an implant that increases pain-free light exposure in adults with the rare light-sensitivity condition EPP. In the UK, the MHRA says it has removed melanotan products from the market for over 10 years (<a href="{MHRA_FOI}" rel="noopener">MHRA FOI response, 2024</a>).',
f'''<li><strong>The original tanning study</strong> ({pm(8637402,"Dorr et al., Life Sci, 1996")}): a pilot Phase 1 trial in 3 healthy men. After only 5 low-dose injections, 2 of the 3 had measurably darker skin on the face, upper body and buttocks a week later. Side effects: mild nausea, yawning and stretching, fatigue and spontaneous erections.</li>
<li><strong>Erections in men with psychogenic ED</strong> ({pm(9679884,"Wessells et al., J Urol, 1998")}): double-blind, placebo-controlled crossover, 10 men. 8 of 10 had clinically apparent erections. Strong rigidity lasted 38.0 minutes on MT2 vs 3.0 on placebo. Nausea, yawning and <strong>decreased appetite</strong> were more common on MT2.</li>
<li><strong>Erections and desire with organic ED</strong> ({pm(11018622,"Wessells et al., Urology, 2000")}): 10 men, placebo-controlled. Erections after 12 of 19 MT2 injections vs 1 of 21 placebo, and <strong>sexual desire was significantly higher</strong>. Severe nausea followed 4 of 19 injections.</li>
<li><strong>Appetite, in animal studies</strong> ({pm(36155088,"Neuropeptides, 2022")}): in one mouse study, MT2 injected directly into a brain reward area cut food intake and the motivation to work for food, without signs of an aversive state.</li>
<li><strong>The buzz is documented:</strong> dermatologists have analyzed melanotan content on TikTok ({pm(39148422,"JEADV, 2025")}) and its "Barbie drug" marketing ({pm(38808957,"JEADV, 2025")}). A study of 205 forum users found people mainly used it for a tan before sun holidays and fitness competitions ({pm(34464955,"Dermatology, 2021")}).</li>''',
[]),
}
X3={
"melanotan-2":dict(badge=("research","Research purposes only"),
 h1="Melanotan II (MT2): the tanning peptide, the research & the risks",
 quick=["<strong>What it is:</strong> a lab-made version of α-MSH, the hormone that switches on skin pigment.","<strong>Status:</strong> research purposes only. Not FDA-approved.","<strong>Human evidence:</strong> small 1990s trials: darker skin in a 3-man pilot, erections in two 10-man ED studies.","<strong>Side effects in studies:</strong> nausea, yawning, fatigue, lower appetite, spontaneous erections.","<strong>Watch out for:</strong> mole changes in case reports. See the safety box."],
 dosing=f'''{MT2_SAFE}<h2 id="dosing">Melanotan II dosage: what we know</h2><p>There is <strong>no approved or established human dose</strong>, so we don't list one. The 1990s studies dosed by body weight under medical supervision, and they were tiny.</p>''',
 faq=[("Does Melanotan II really tan you?","It darkened skin in a tiny 1996 pilot: 2 of 3 men had measurably darker skin a week after 5 low-dose injections."),
 ("Does Melanotan II increase libido?","In two small 1990s trials in men with erectile dysfunction, it triggered erections, and the 2000 study found sexual desire was significantly higher than on placebo."),
 ("Does Melanotan II suppress appetite?","Decreased appetite was reported more often on MT2 than placebo in one small 1998 trial (10 men), and it cut food intake in one mouse study (injected directly into the brain)."),
 ("Is Melanotan II legal?","It's not FDA-approved. Its cousin afamelanotide is approved as Scenesse for the rare condition EPP. The UK regulator tells people to stop using MT2 injections and nasal sprays."),
 ("What are the side effects of Melanotan II?","In studies: nausea, yawning and stretching, fatigue, lower appetite and spontaneous erections. Case reports describe new or darkening moles, melanomas in users, priapism and kidney problems."),
 ("What's the difference between Melanotan I and II?","Melanotan I is afamelanotide, the FDA-approved drug in Scenesse. Melanotan II is a different, ring-shaped molecule that also acts on the receptors involved in libido and appetite.")]),
}
META3={"melanotan-2":("skin","Tanning, libido (in studies)","Injection or nasal spray (unregulated)",None)}
EXCITE3={"melanotan-2":("The \"tan jab\" peptide all over TikTok.",["In the first human pilot, <strong>2 of 3 men tanned</strong> after just 5 low-dose injections.","Triggered erections in <strong>8 of 10</strong> men with psychogenic ED in a small placebo-controlled trial.","Less appetite was a reported side effect in one small trial, and a mouse study backs it up."],"The viral tanning peptide. Pigment, libido and appetite effects in studies.")}
TITLES3={"peptides/melanotan-2.html":"Melanotan II (MT2): tanning peptide research, effects & risks"}
LILLY_MAY21="https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-powerful-weight-loss"
LILLY_KNOW="https://www.lilly.com/news/stories/what-to-know-about-retatrutide"
RETA_BADGE_T="Investigational: not approved; only available in Lilly clinical trials"
RETA_HERO=(f'<div class="hero-reta"><span class="hot-tag">🔥 Hot right now</span>'
 '<strong><a href="peptides/retatrutide.html" data-goatcounter-click="hero-retatrutide">Retatrutide: up to −25.0% average weight in Phase 3</a></strong>'
 f'<span>TRIUMPH-1, 80 weeks, 12 mg arm, counting dropouts (<a href="{LILLY_MAY21}" rel="noopener">Lilly, May 21, 2026</a>). Investigational: Lilly plans to submit to the FDA in Q1 2027.</span>'
 '<a class="hero-reta-go" href="peptides/retatrutide.html" data-goatcounter-click="hero-retatrutide-go">Read the retatrutide guide →</a></div>')
LABEL_LINE="Label doses are there so you can follow along with your prescriber. "
RESEARCH_PAGES={"peptides/retatrutide-side-effects.html","peptides/retatrutide-fda-approval-status.html"}
def wire3(pages):
    k="index.html"; v=list(pages[k]); a='<div class="hero-cta">'
    assert a in v[2]; v[2]=v[2].replace(a,RETA_HERO+a,1); pages[k]=tuple(v)
    # research-only pages: no 'label doses' line in the footer disclaimer
    for k in list(pages):
        v=list(pages[k])
        if LABEL_LINE in v[2] and ('class="badge research"' in v[2].split('<h2',1)[0] or k in RESEARCH_PAGES):
            v[2]=v[2].replace(LABEL_LINE,""); pages[k]=tuple(v)
    for s in PEP3:
        k=f"peptides/{s}.html"; v=list(pages[k]); v[2]=v[2].replace("Checked against official sources Oct 16, 2026","Checked against PubMed and official sources Oct 18, 2026",1)
        v[3]=[{**o,"lastReviewed":"2026-10-18"} if o.get("@type")=="MedicalWebPage" else ({**o,"datePublished":"2026-10-18","dateModified":"2026-10-18"} if o.get("@type")=="Article" else o) for o in v[3]]
        pages[k]=tuple(v)
