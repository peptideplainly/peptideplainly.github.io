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

# ===================== Batch 2 (Oct 18 2026) =====================
FDA_PCAC="https://www.fda.gov/media/193342/download"
PCAC_VOTES="https://www.peptides.media/updates/pcac-july-2026-vote-results"
FDA_GLP1C="https://www.fda.gov/drugs/drug-alerts-and-statements/fdas-concerns-unapproved-glp-1-drugs-used-weight-loss"
NOVO_NDA="https://www.novonordisk-us.com/media/press-releases/novo-nordisk-cagrisema-fda-nda-submission.html"
FORZ="https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=146bf34c-76f2-48db-ac07-fb29cce2cd75"
DRUGSFDA_FORZ="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=215244"
NOAPP="We found no FDA approval for it in Drugs@FDA (checked Oct 18, 2026)."
def pcac(name): return (f'Ahead of FDA\'s July 2026 compounding advisory committee meeting, FDA staff proposed <em>not</em> adding {name} to the 503A bulks list (<a href="{FDA_PCAC}" rel="noopener">FDA meeting materials</a>). '
    f'The committee voted to recommend it anyway (<a href="{PCAC_VOTES}" rel="noopener">vote report</a>). That vote is non-binding and is not a drug approval.')
B2_PEP={
"epitalon":("Epitalon (epithalon)","What is Epitalon? The longevity peptide behind the telomere buzz: the cell, mouse and small human studies, FDA status and FAQs.",
 f"Epitalon (also spelled epithalon) is a tiny lab-made peptide of four amino acids (Ala-Glu-Asp-Gly). It was modeled on epithalamin, an extract from the pineal gland, and it's one of the most talked-about longevity peptides online ({pm(42884164,'Int J Mol Sci review, 2026')}).",
 f'<strong>Not FDA-approved.</strong> {NOAPP} {pcac("epitalon")}',
 f'''<li><strong>Telomeres, in human cells</strong> ({pm(40908429,"Biogerontology, 2025")}): in lab-grown human cell lines, epitalon produced dose-dependent increases in telomere length, through telomerase in some cells and an alternative pathway (ALT) in others. Cells in a dish, not people.</li>
<li><strong>Lifespan, in mice</strong> ({pm(14501183,"Biogerontology, 2003")}): 54 mice per group, treated monthly for life. Mean lifespan didn't change, but maximum lifespan was 12.3% longer, chromosome damage in bone marrow fell 17.1%, and leukemia was less common than in controls.</li>
<li><strong>The big-picture review</strong> ({pm(42884164,"Int J Mol Sci, 2026")}): human evidence is limited to small physiological and biomarker studies plus an older controlled study in retinitis pigmentosa. No adequately powered randomized trial has proven a benefit, and long-term safety data are inadequate.</li>''',[]),
"selank":("Selank","What is Selank? The calming nasal peptide from Russia: the anxiety studies, animal research on memory and stress, status and FAQs.",
 f"Selank is a lab-made analogue of tuftsin, a natural immune peptide, developed and studied mainly in Russia ({pm(31625062,'Bull Exp Biol Med, 2019')}). Online it's sold as powder for injection or as nasal sprays ({pm(31667971,'Drug Test Anal, 2020')}), riding the \"peptides for the mind\" wave next to Semax.",
 f'<strong>Not FDA-approved.</strong> {NOAPP} A 2021 pharmacology review called Selank a "poorly studied" Russian drug with a GABA-related mechanism that is being sold to U.S. consumers as a dietary supplement ({pm(34396551,"J Clin Pharmacol, 2021")}).',
 f'''<li><strong>Anxiety, head to head with a tranquilizer</strong> ({pm(25176261,"Russian study, 2014")}): 60 patients with anxiety and related disorders. The authors report a pronounced anti-anxiety effect plus mild "nootropic" (thinking) effects, lasting about a week after the last dose, and better quality of life. Published in Russian.</li>
<li><strong>As an add-on</strong> ({pm(26356395,"Russian study, 2015")}): 70 patients. Adding Selank to the benzodiazepine phenazepam (40 patients, vs 30 on phenazepam alone) was linked to a faster response and fewer tranquilizer side effects such as attention and memory problems and sedation.</li>
<li><strong>Memory and stress, in animal studies</strong>: Selank protected memory against alcohol-induced impairment in rats, linked to brain BDNF levels ({pm(31625062,"Bull Exp Biol Med, 2019")}), and boosted diazepam's anti-anxiety effect in stressed rats ({pm(28280289,"Behav Neurol, 2017")}).</li>''',[]),
"kpv":("KPV","What is KPV? The anti-inflammatory tripeptide fans use for gut and skin: the colitis and cell studies, FDA status and FAQs.",
 f"KPV is a naturally occurring tripeptide (lysine-proline-valine), just three amino acids long, derived from the hormone alpha-MSH ({pm(40073467,'Tissue Cell, 2025')}). It's getting buzz for gut health and inflammation, and it gets into gut cells through PepT1, a transporter that's turned up in inflamed colons ({pm(18061177,'Gastroenterology, 2008')}).",
 f'<strong>Not FDA-approved.</strong> {NOAPP} {pcac("KPV")}',
 f'''<li><strong>Colitis, in mice</strong> ({pm(18061177,"Dalmasso et al., Gastroenterology, 2008")}): KPV in drinking water reduced colitis in two mouse models, with lower inflammatory signals. In human gut and immune cells in the lab, tiny (nanomolar) amounts blocked key inflammation pathways.</li>
<li><strong>Targeted delivery, in mice</strong> ({pm(28143741,"Mol Ther, 2017")}): KPV packed into gut-targeting nanoparticles sped mucosal healing and cut inflammation in a mouse colitis model.</li>
<li><strong>Skin cells</strong> ({pm(40073467,"Tissue Cell, 2025")}): in lab-grown human skin cells (and a 3D skin model), KPV reduced cell death and inflammation caused by fine-dust air pollution.</li>
<li>We found <strong>no published human trials</strong> of KPV.</li>''',[]),
"kisspeptin":("Kisspeptin","What is kisspeptin? The hormone peptide behind the libido buzz: randomized brain-scan trials in men and women, FDA status and FAQs.",
 "Kisspeptin is a natural hormone made in the brain that switches on the reproductive hormone system. Researchers at Imperial College London have been testing whether giving it changes how the brain responds to sexual and emotional cues, which is why it's trending as a libido peptide.",
 f'<strong>Not FDA-approved.</strong> {NOAPP} In the human studies below it was given as a timed infusion in a research clinic.',
 f'''<li><strong>Men with low sexual desire</strong> ({pm(36735255,"JAMA Netw Open, 2023")}): randomized, placebo-controlled crossover, 32 men completed. Kisspeptin changed activity in the brain's sexual-processing network while watching erotic videos, raised penile tumescence by up to 56% vs placebo, and increased "happiness about sex."</li>
<li><strong>Women with low sexual desire</strong> ({pm(36287566,"JAMA Netw Open, 2022")}): randomized crossover, 32 premenopausal women completed. Kisspeptin shifted sexual and attraction brain processing, and was well tolerated with no reported side effects.</li>
<li><strong>Healthy young men</strong> ({pm(28112678,"J Clin Invest, 2017")}): 29 men. Kisspeptin boosted limbic brain activity in response to sexual and couple-bonding images.</li>
<li><strong>Not an anxiety fix</strong> ({pm(40036336,"J Clin Endocrinol Metab, 2025")}): it raised reproductive hormones but didn't affect anxiety.</li>''',[]),
"cagrilintide":("Cagrilintide & CagriSema","What is cagrilintide (CagriSema)? Novo's amylin + semaglutide shot: −20.4% in REDEFINE 1, side effects, FDA status and FAQs.",
 f"Cagrilintide is a long-acting version of amylin, a hormone released with insulin that helps you feel full. CagriSema is Novo Nordisk's once-weekly combination of cagrilintide 2.4 mg and semaglutide 2.4 mg, and if approved it would be the first injectable GLP-1 plus amylin combination (<a href=\"{NOVO_NDA}\" rel=\"noopener\">Novo Nordisk</a>).",
 f'<strong>Investigational, not FDA-approved.</strong> Novo Nordisk submitted CagriSema to the FDA on Dec 18, 2025 (<a href="{NOVO_NDA}" rel="noopener">Novo Nordisk</a>), and no FDA decision has been announced as of Oct 18, 2026. The FDA says cagrilintide cannot be used in compounding under federal law (<a href="{FDA_GLP1C}" rel="noopener">FDA</a>).',
 f'''<li><strong>REDEFINE 1</strong> ({pm(40544433,"NEJM, 2025")}): 3,417 adults with obesity or overweight and no diabetes, 68 weeks. CagriSema: <strong>−20.4%</strong> average weight change vs −3.0% on placebo (treatment-policy estimand, which counts dropouts). Gastrointestinal side effects hit 79.6% vs 39.9% on placebo, mostly mild to moderate and temporary.</li>
<li><strong>REDEFINE 2</strong> ({pm(40544432,"NEJM, 2025")}): 1,206 adults with type 2 diabetes, 68 weeks. −13.7% vs −3.4% on placebo (counts dropouts), and 73.5% reached an HbA1c of 6.5% or less vs 15.9%.</li>
<li>Different trials from tirzepatide's and retatrutide's, so compare loosely. See <a href="../glp1-comparison.html">the GLP-1 comparison</a>.</li>''',[]),
"elamipretide":("SS-31 (elamipretide, Forzinity)","What is SS-31 (elamipretide)? The mitochondria peptide, now FDA-approved as Forzinity: label use, dosing, the aging-mouse data and FAQs.",
 f"SS-31, now named elamipretide, is a small peptide that targets mitochondria, your cells' energy factories. The FDA label calls it a \"mitochondrial cardiolipin binder\" (cardiolipin is a key fat in mitochondrial membranes), which is why it's a favorite in longevity and energy circles (<a href=\"{FORZ}\" rel=\"noopener\">FDA label</a>).",
 f'<strong>FDA-approved</strong> as Forzinity (Sept 19, 2025, <a href="{DRUGSFDA_FORZ}" rel="noopener">Drugs@FDA</a>) under accelerated approval, to improve muscle strength in adults and children with Barth syndrome, a rare mitochondrial disease, who weigh at least 30 kg. Continued approval may depend on a confirmatory trial (<a href="{FORZ}" rel="noopener">FDA label</a>). "SS-31" vials sold online are not Forzinity.',
 f'''<li><strong>The approval data</strong> (<a href="{FORZ}" rel="noopener">FDA label</a>): in a 12-patient crossover trial in Barth syndrome, it didn't beat placebo on walking distance or fatigue. In the open-label extension, knee-extensor muscle strength rose (median +63 newtons at week 168 in the 8 patients still enrolled), which supported accelerated approval.</li>
<li><strong>Aging, in mice</strong> ({pm(40080911,"Aging Cell, 2025")}): 8 weeks of treatment in old mice slowed frailty and partly reversed declines in heart function and muscle fatigue resistance, without measurable changes in epigenetic "biological age."</li>
<li><strong>Exercise tolerance, in aged mice</strong> ({pm(36840897,"Geroscience, 2023")}): intermittent treatment preserved exercise tolerance in aged female mice.</li>
<li><strong>A miss in adults</strong> ({pm(37268435,"Neurology, 2023")}): in MMPOWER-3, 218 adults with primary mitochondrial myopathy, it didn't improve walking or fatigue vs placebo. It was well tolerated.</li>''',[]),
"bpc-157-tb-500-stack":("BPC-157 + TB-500 stack","BPC-157 + TB-500, the 'Wolverine stack': what each peptide's research shows, the first study testing them together, status and risks.",
 "The BPC-157 + TB-500 stack (nicknamed the \"Wolverine stack\" online) pairs the two most popular recovery peptides. BPC-157 is a 15-amino-acid peptide based on a stomach-juice protein. TB-500 is a synthetic product based on part of thymosin beta-4, a natural repair protein. Full details live in our <a href=\"bpc-157.html\">BPC-157</a> and <a href=\"tb-500.html\">TB-500</a> guides.",
 f'<strong>Neither is FDA-approved</strong>, and both are banned at all times in sport under the <a href="https://www.wada-ama.org/en/prohibited-list" rel="noopener">2026 WADA Prohibited List</a>. FDA staff proposed not adding either to the 503A compounding list before the July 2026 advisory committee meeting (<a href="{FDA_PCAC}" rel="noopener">FDA meeting materials</a>); the committee voted to recommend both anyway (<a href="{PCAC_VOTES}" rel="noopener">vote report</a>). That vote is non-binding.',
 f'''<li><strong>The first head-to-head stack study, in rats</strong> ({pm(42542926,"Jt Dis Relat Surg, 2026")}): 32 rats after Achilles tendon repair, 8 per group. TB-500 alone made the strongest tendons; both peptides improved tendon structure. The <strong>combination did not add any benefit</strong> over either peptide alone.</li>
<li><strong>BPC-157 in people</strong> ({pm(42885452,"Acta Orthop Belg, 2026")}): a 2026 systematic review found 3 small human studies, 30 people in total, with no control groups. Certainty of evidence: very low.</li>
<li><strong>BPC-157 in animals</strong> ({pm(40756949,"HSS Journal, 2025")}): 36 studies, almost all animal, showing better healing of muscle, tendon, ligament and bone.</li>
<li><strong>Thymosin beta-4 in people</strong> ({pm(41229390,"Cardiovasc Res, 2025")}): in a 96-patient heart-attack trial, the overall result wasn't significant; a subgroup dosed early did better. No controlled human trials have tested products sold as "TB-500."</li>''',[]),
}
B2_SAFE={
"epitalon":safety([f'<strong>Unknowns:</strong> a 2026 review says dose-ranging and long-term safety data are inadequate, and cancer-related, immune and product-quality questions remain open ({pm(42884164,"Int J Mol Sci, 2026")}).'],"not FDA-approved. A July 2026 advisory vote to allow compounding is non-binding."),
"selank":safety([f'<strong>Unknowns:</strong> Selank and Semax have turned up in seized products, and the researchers who analyzed them wrote that, to their knowledge, these peptides "have not completed any clinical trials" ({pm(31667971,"Drug Test Anal, 2020")}). A pharmacology review flagged its GABA-related mechanism and called it poorly studied ({pm(34396551,"J Clin Pharmacol, 2021")}).'],"not FDA-approved."),
"kpv":safety(['<strong>Unknowns:</strong> no published human trials, so human side effects and safety are unknown.'],"not FDA-approved. A July 2026 advisory vote to allow compounding is non-binding."),
"kisspeptin":safety([f'<strong>Side effects:</strong> none reported in the 2022 women\'s trial ({pm(36287566,"JAMA Netw Open")}), but trials were short, single-visit research infusions. It switches on reproductive hormones, so long-term effects outside research are unknown.'],"not FDA-approved. Research products online are not the trial material."),
"cagrilintide":safety([f'<strong>Side effects in trials:</strong> mostly gastrointestinal (nausea, vomiting, diarrhea, constipation, abdominal pain) in 79.6% vs 39.9% on placebo in REDEFINE 1 ({pm(40544433,"NEJM, 2025")}).',f'<strong>Online "cagrilintide":</strong> the FDA has warned companies selling semaglutide, tirzepatide, retatrutide and similar drugs falsely labeled "for research purposes" (<a href="{FDA_GLP1C}" rel="noopener">FDA</a>).'],"investigational, not FDA-approved; the FDA says cagrilintide can't be used in compounding."),
"bpc-157-tb-500-stack":safety(['<strong>Unknowns:</strong> there is no human safety data on combining them, and BPC-157 has no clinical safety data in people yet, per the 2025 HSS Journal review.',f'<strong>Banned in sport:</strong> both are prohibited at all times by WADA.'],"neither is FDA-approved."),
}
B2_X={
"epitalon":dict(badge=("research","Research purposes only"),h1="Epitalon: the telomere longevity peptide, the research & the unknowns",
 quick=["<strong>What it is:</strong> a 4-amino-acid peptide modeled on a pineal gland extract.","<strong>Status:</strong> research purposes only. Not FDA-approved.","<strong>Evidence:</strong> longer telomeres in human cell lines; longer maximum lifespan in one mouse study.","<strong>Human evidence:</strong> small biomarker studies only. No large randomized trials.","<strong>Watch out for:</strong> unknown long-term safety. See the safety box."],
 faq=[("Does Epitalon lengthen telomeres?","In lab-grown human cell lines, yes: a 2025 study found dose-dependent telomere lengthening. That hasn't been shown in a proper human trial."),("Does Epitalon extend lifespan?","In one 2003 mouse study, mean lifespan didn't change, but maximum lifespan was 12.3% longer than in controls."),("Is Epitalon FDA-approved?","No. FDA staff proposed against allowing it in compounding; a July 2026 advisory committee recommended it anyway, but that vote is non-binding."),("What's the Epitalon dosage?","There's no established human dose, so we don't list one.")]),
"selank":dict(badge=("research","Research purposes only"),h1="Selank: the calming nasal peptide, the research & the unknowns",
 quick=["<strong>What it is:</strong> a lab-made analogue of the immune peptide tuftsin.","<strong>Status:</strong> research purposes only. Not FDA-approved.","<strong>Human evidence:</strong> two small Russian studies in anxiety disorders (60 and 70 patients).","<strong>Animal studies:</strong> protected memory and boosted anti-anxiety drug effects in rats.","<strong>Watch out for:</strong> poorly studied in the West. See the safety box."],
 faq=[("Does Selank work for anxiety?","Two small Russian studies (60 and 70 patients) reported anti-anxiety effects, one compared with and one added to the tranquilizer phenazepam. There are no large Western trials."),("Is Selank the same as Semax?","No. They're different peptides that often get sold side by side. Selank is a tuftsin analogue studied mainly for anxiety; see our <a href=\"semax.html\">Semax guide</a> for the other one."),("Is Selank FDA-approved?","No."),("What's the Selank dosage?","There's no established human dose, so we don't list one.")]),
"kpv":dict(badge=("research","Research purposes only"),h1="KPV: the anti-inflammatory gut peptide, the research & the unknowns",
 quick=["<strong>What it is:</strong> a naturally occurring 3-amino-acid peptide (Lys-Pro-Val).","<strong>Status:</strong> research purposes only. Not FDA-approved.","<strong>Evidence:</strong> reduced colitis in mouse studies; calmed inflammation in human cells in the lab.","<strong>Human evidence:</strong> no published human trials.","<strong>Watch out for:</strong> unknown human safety. See the safety box."],
 faq=[("What is KPV used for?","Online, mostly gut health and inflammation. The research behind that is in mice and lab-grown cells, where it reduced colitis and inflammatory signaling."),("Does KPV work in humans?","We found no published human trials."),("Is KPV FDA-approved?","No. FDA staff proposed against allowing it in compounding; a July 2026 advisory committee recommended it anyway, but that vote is non-binding."),("What's the KPV dosage?","There's no established human dose, so we don't list one.")]),
"kisspeptin":dict(badge=("research","Research purposes only"),h1="Kisspeptin: the libido hormone peptide, the trials & the unknowns",
 quick=["<strong>What it is:</strong> a natural brain hormone that switches on the reproductive system.","<strong>Status:</strong> research purposes only. Not FDA-approved.","<strong>Human evidence:</strong> small randomized brain-scan trials in men and women with low desire.","<strong>Headline result:</strong> up to 56% more penile tumescence vs placebo in men with low desire.","<strong>Watch out for:</strong> short research-clinic infusions only. See the safety box."],
 faq=[("Does kisspeptin increase libido?","In small randomized trials, it changed how the brain processed sexual cues in men and women with low desire, and in men it increased tumescence and \"happiness about sex.\""),("Is kisspeptin FDA-approved?","No."),("Does kisspeptin help anxiety?","A 2025 study found it raised reproductive hormones but didn't affect anxiety."),("What's the kisspeptin dosage?","There's no established human dose outside research infusions, so we don't list one.")]),
"cagrilintide":dict(badge=("research","Investigational: not FDA-approved"),h1="Cagrilintide & CagriSema: the amylin weight-loss combo, results & status",
 quick=["<strong>What it is:</strong> a long-acting amylin (fullness hormone) shot, paired with semaglutide as CagriSema.","<strong>Status:</strong> investigational. Novo submitted CagriSema to the FDA in Dec 2025; no decision announced.","<strong>Headline result:</strong> −20.4% average weight at 68 weeks in REDEFINE 1, vs −3.0% on placebo.","<strong>Side effects:</strong> mostly gastrointestinal.","<strong>Compounding:</strong> the FDA says cagrilintide can't be compounded."],
 faq=[("How much weight do people lose on CagriSema?","In REDEFINE 1, the average was −20.4% at 68 weeks vs −3.0% on placebo, counting dropouts. In people with type 2 diabetes (REDEFINE 2), −13.7% vs −3.4%."),("Is CagriSema FDA-approved?","Not yet. Novo Nordisk submitted it to the FDA on Dec 18, 2025, and no decision has been announced as of Oct 18, 2026."),("Can cagrilintide be compounded?","No. The FDA says cagrilintide cannot be used in compounding under federal law."),("What dose was used in trials?","The trial arm was cagrilintide 2.4 mg plus semaglutide 2.4 mg once weekly. There's no approved dose yet.")]),
"elamipretide":dict(badge=("approved","FDA-approved (as Forzinity)"),h1="SS-31 (elamipretide): the mitochondria peptide, approval & research",
 quick=["<strong>What it is:</strong> a mitochondria-targeting peptide that binds cardiolipin.","<strong>Status:</strong> FDA-approved as Forzinity (2025, accelerated approval) for Barth syndrome.","<strong>Evidence:</strong> muscle strength gains in a long open-label extension; anti-frailty effects in old mice.","<strong>Most common side effects:</strong> injection-site reactions.","<strong>Note:</strong> online \"SS-31\" vials are not Forzinity."],
 faq=[("Is SS-31 FDA-approved?","Elamipretide, the drug once called SS-31, is FDA-approved as Forzinity (Sept 2025, accelerated approval) to improve muscle strength in people with Barth syndrome weighing at least 30 kg."),("Does SS-31 slow aging?","In old mice, 8 weeks of treatment slowed frailty and partly reversed heart and muscle declines. That hasn't been tested in healthy people."),("What are the side effects of elamipretide?","On the FDA label, injection-site reactions (redness, pain, hardening, itching, bruising) are the most common. Increases in eosinophils, a type of white blood cell, were also seen."),("What is the Forzinity dose?","The FDA label: 40 mg under the skin once daily for patients weighing at least 30 kg, or 20 mg once daily in adults with eGFR under 30 who aren't on dialysis.")]),
"bpc-157-tb-500-stack":dict(badge=("research","Research purposes only"),h1="BPC-157 + TB-500 stack: what the research really shows",
 quick=["<strong>What it is:</strong> the two most popular recovery peptides, taken together.","<strong>Status:</strong> research purposes only. Neither is FDA-approved; both banned in sport.","<strong>Stack evidence:</strong> one rat tendon study (2026). The combo didn't beat either peptide alone.","<strong>Human evidence:</strong> tiny for BPC-157 (30 people), none for TB-500 products.","<strong>Watch out for:</strong> no human safety data on the combination. See the safety box."],
 faq=[("Does the BPC-157 and TB-500 stack work better together?","In the only study we found that tested the combination, a 2026 rat Achilles-tendon study, the combo did not add any benefit over either peptide alone."),("Is the Wolverine stack FDA-approved?","No. Neither BPC-157 nor TB-500 is FDA-approved, and both are banned in sport by WADA."),("What's the BPC-157 + TB-500 dosage?","There's no established human dose for either, so we don't list one.")]),
}
FORZ_DOSE=f'''<h2 id="dosing">Forzinity dosing: what the FDA label says</h2><p class="fine">For the approved use only, as prescribed. Online "SS-31" vials have no label and aren't Forzinity.</p><ul><li>Patients weighing at least 30 kg: <strong>40 mg</strong> under the skin once daily, at the same time each day.</li><li>Adults with severe kidney impairment (eGFR under 30 mL/min, not on dialysis): <strong>20 mg</strong> once daily.</li><li>Missed dose: skip it and take the next one on schedule. Don't double up.</li></ul><p class="fine">Source: <a href="{FORZ}" rel="noopener">Forzinity FDA label on DailyMed</a>.</p>'''
for k,x in B2_X.items():
    if k=="elamipretide": x["dosing"]=f'<aside class="safety" aria-label="Safety"><h2>Safety, in 20 seconds</h2><ul><li><strong>Most common side effects:</strong> injection-site redness, pain, hardening, itching and bruising; increases in eosinophils (a type of white blood cell) were also seen (<a href="{FORZ}" rel="noopener">FDA label</a>).</li><li><strong>Don\'t use</strong> with serious allergy to elamipretide or its ingredients.</li><li><strong>Research vials:</strong> "SS-31" sold online is unregulated. Here\'s <a href="{LEGIT}">how to tell if a source is legit</a>.</li></ul></aside>'+FORZ_DOSE
    elif k=="cagrilintide": x["dosing"]=B2_SAFE[k]+'<h2 id="dosing">Cagrilintide dosage: what we know</h2><p>There is <strong>no approved dose</strong>. The trials used one arm: cagrilintide 2.4 mg plus semaglutide 2.4 mg once weekly, the strength Novo submitted to the FDA. That\'s a trial arm name, not dosing advice.</p>'
    else:
        nm=B2_PEP[k][0].split(" (")[0]
        x["dosing"]=B2_SAFE[k]+f'<h2 id="dosing">{nm} dosage: what we know</h2><p>There is <strong>no approved or established human dose</strong>, so we don\'t list one.</p>'
B2_META={"epitalon":("longevity","Longevity & telomeres (in studies)","Injection (unregulated)",None),
"selank":("brain","Calm & focus (in studies)","Nasal spray (unregulated)",None),
"kpv":("recovery","Gut & inflammation (in animal studies)","Oral or injection (unregulated)",None),
"kisspeptin":("sexual","Libido & desire (in trials)","Injection or infusion (research)",None),
"cagrilintide":("weight","Weight loss (in trials)","Weekly shot (trials only)",None),
"elamipretide":("longevity","Mitochondria & muscle strength","Daily shot",None),
"bpc-157-tb-500-stack":("recovery","Injury recovery (claimed)","Injection (unregulated)",None)}
B2_EXCITE={
"epitalon":("The longevity peptide everyone links to telomeres.",["Lengthened telomeres in <strong>human cell lines</strong> in a 2025 lab study.","<strong>12.3% longer maximum lifespan</strong> in a 2003 mouse study.","Modeled on a pineal gland extract."],"The telomere peptide. Longer telomeres in cells, longer max lifespan in mice."),
"selank":("The calm-and-focus nasal peptide.",["Anti-anxiety effects reported in a <strong>60-patient</strong> Russian study.","Cut tranquilizer side effects when added to phenazepam in <strong>70</strong> patients.","Protected memory in rat studies."],"Semax's calming cousin. Anti-anxiety results in small studies."),
"kpv":("The 3-amino-acid peptide for gut and skin calm.",["Reduced colitis in <strong>two mouse models</strong>.","Blocked inflammation pathways in human gut cells at <strong>nanomolar</strong> amounts.","Calmed inflamed skin cells in the lab."],"Tiny tripeptide, big gut buzz. Calmed colitis in mice."),
"kisspeptin":("The hormone peptide that lights up the brain's desire circuits.",["Up to <strong>56% more penile tumescence</strong> vs placebo in men with low desire.","Shifted sexual brain processing in <strong>women</strong> with low desire too.","Randomized, placebo-controlled brain-scan trials."],"The libido hormone. Randomized trials in men and women."),
"cagrilintide":("The amylin booster that pushes semaglutide further.",["<strong>−20.4%</strong> average weight at 68 weeks in REDEFINE 1 (3,417 adults).","73.5% hit an HbA1c of 6.5% or less in REDEFINE 2.","Submitted to the FDA in Dec 2025."],"Amylin + semaglutide. −20.4% in Phase 3, FDA decision pending."),
"elamipretide":("The mitochondria peptide that made it to FDA approval.",["FDA-approved as <strong>Forzinity</strong> in 2025.","Slowed frailty and partly reversed declines in heart and muscle function in <strong>old mice</strong>.","Targets cardiolipin inside your cells' energy factories."],"SS-31 grew up: FDA-approved, with anti-frailty results in old mice."),
"bpc-157-tb-500-stack":("The \"Wolverine stack\" the recovery crowd swears by.",["Both peptides improved tendon structure in a <strong>2026 rat study</strong>.","TB-500 alone made the strongest tendons.","Plus BPC-157's 36-study, mostly animal, healing literature."],"The famous recovery combo, and the first study to test it."),
}
B2_TITLES={"peptides/epitalon.html":"Epitalon: telomere longevity peptide research & status","peptides/selank.html":"Selank: the calming nasal peptide, research & status",
"peptides/kpv.html":"KPV peptide: gut & inflammation research, status & FAQs","peptides/kisspeptin.html":"Kisspeptin: the libido peptide trials, status & FAQs",
"peptides/cagrilintide.html":"Cagrilintide & CagriSema: −20.4% results, side effects & status","peptides/elamipretide.html":"SS-31 (elamipretide, Forzinity): approval, dosing & research",
"peptides/bpc-157-tb-500-stack.html":"BPC-157 + TB-500 stack: what the research really shows"}
PEP3.update(B2_PEP); X3.update(B2_X); META3.update(B2_META); EXCITE3.update(B2_EXCITE); TITLES3.update(B2_TITLES)
QH3={"bpc-157-tb-500-stack":("What is the BPC-157 + TB-500 stack?","Are BPC-157 and TB-500 FDA-approved?"),
"cagrilintide":("What are cagrilintide and CagriSema?","Is CagriSema FDA-approved?"),
"elamipretide":("What is SS-31 (elamipretide)?","Is SS-31 FDA-approved?"),
"epitalon":("What is Epitalon?","Is Epitalon FDA-approved?")}

# ===== Bean tone update (Oct 18, 4:35 PM): one-line safety, bold headlines, less regulatory copy =====
def line(risks, status="Not FDA-approved; sold for research only."):
    return f'<p class="safety-line"><strong>{status}</strong> Known risks: {risks}. <a href="{LEGIT}">Choose a tested source.</a></p>'
NODOSE='<h2 id="dosing">Dosage</h2><p>There\'s <strong>no established human dose</strong>, so we don\'t list one.</p>'
ONE={
"melanotan-2":line(f'new and darkening moles ({pm(24334249,"case report, 2014")}), melanoma in a 20-year-old who also used sunbeds ({pm(24355990,"single case, 2014")}; a review says a link isn\'t proven, {pm(28266027,"2017")}), priapism ({pm(33460908,"case, 2021")}) and kidney infarction ({pm(31953620,"case, 2020")})'),
"epitalon":line(f'not well studied; long-term safety data are inadequate, per a 2026 review ({pm(42884164,"Int J Mol Sci")})'),
"selank":line(f'poorly studied, and it acts on GABA systems ({pm(34396551,"J Clin Pharmacol, 2021")})'),
"kpv":line('not well studied; there are no published human trials'),
"kisspeptin":line(f'unknown outside short research infusions; none were reported in the 2022 women\'s trial ({pm(36287566,"JAMA Netw Open")})'),
"cagrilintide":line(f'gastrointestinal side effects in 79.6% vs 39.9% on placebo in REDEFINE 1 ({pm(40544433,"NEJM, 2025")}); online "research" versions aren\'t the trial drug',status="Investigational, not FDA-approved."),
"bpc-157-tb-500-stack":line(f'not well studied; no human safety data on the combination; banned in sport (<a href="https://www.wada-ama.org/en/prohibited-list" rel="noopener">WADA</a>)'),
}
ONELINE=set(ONE)-{"cagrilintide"}  # pages where the footer research NOTE is dropped (the line covers it)
ONELINE|={"cagrilintide"}
X3["melanotan-2"]["dosing"]=ONE["melanotan-2"]+NODOSE.replace("<p>There","<p>The tiny 1990s studies dosed under medical supervision. There")
for k in ["epitalon","selank","kpv","kisspeptin","bpc-157-tb-500-stack"]: X3[k]["dosing"]=ONE[k]+NODOSE
X3["cagrilintide"]["dosing"]=ONE["cagrilintide"]+'<h2 id="dosing">Dosage</h2><p>No approved dose yet. The trials tested cagrilintide 2.4 mg plus semaglutide 2.4 mg once weekly, the strength Novo submitted to the FDA.</p>'
X3["elamipretide"]["dosing"]=f'<p class="safety-line"><strong>Most common side effects:</strong> injection-site reactions; eosinophil increases were also seen (<a href="{FORZ}" rel="noopener">FDA label</a>). Online "SS-31" isn\'t Forzinity.</p>'+FORZ_DOSE
H1S={"melanotan-2":"Melanotan II (MT2): the viral tan jab, and what studies really show",
"epitalon":"Epitalon: the telomere peptide behind the longevity buzz",
"selank":"Selank: the calm-and-focus nasal peptide everyone's talking about",
"kpv":"KPV: the 3-amino-acid peptide taking on gut inflammation",
"kisspeptin":"Kisspeptin: the hormone that lit up desire circuits in trials",
"cagrilintide":"CagriSema: the amylin + semaglutide shot behind −20.4% in Phase 3",
"elamipretide":"SS-31 (elamipretide): the mitochondria peptide that won FDA approval",
"bpc-157-tb-500-stack":"BPC-157 + TB-500: the Wolverine stack, put to the test"}
for k,h in H1S.items(): X3[k]["h1"]=h
for k in X3:
    X3[k]["quick"]=[q.replace(" See the safety box.","") for q in X3[k]["quick"]]
X3["melanotan-2"]["quick"][-1]="<strong>Known risks:</strong> mole changes and rare serious events in case reports."
for k,r in {"epitalon":"unknown long-term safety.","selank":"poorly studied in the West.","kpv":"unknown human safety.","kisspeptin":"only short research-clinic infusions tested.","bpc-157-tb-500-stack":"no human safety data on the combination."}.items():
    X3[k]["quick"]=[("<strong>Known risks:</strong> "+r) if q.startswith("<strong>Watch out for:</strong>") else q for q in X3[k]["quick"]]
# Shorter, less regulatory status paragraphs
def _setreg(k,txt): p=list(PEP3[k]); p[3]=txt; PEP3[k]=tuple(p)
_setreg("melanotan-2",f'<strong>Not FDA-approved</strong> ({pm(28266027,"Int J Dermatol, 2017")}). Its cousin afamelanotide (Melanotan I) is: it\'s Scenesse, an implant for the rare light-sensitivity condition EPP (<a href="{SCEN}" rel="noopener">FDA approval, 2019</a>).')
_vote=f'In July 2026 an FDA advisory committee voted to recommend allowing it in pharmacy compounding (<a href="{PCAC_VOTES}" rel="noopener">vote report</a>). The vote is non-binding.'
_setreg("epitalon",f'<strong>Not FDA-approved.</strong> {_vote}')
_setreg("kpv",f'<strong>Not FDA-approved.</strong> {_vote}')
_setreg("selank",'<strong>Not FDA-approved.</strong> Sold online as a research peptide and supplement.')
_setreg("kisspeptin",'<strong>Not FDA-approved.</strong> The human trials used research-clinic infusions.')
_setreg("cagrilintide",f'<strong>Investigational, not FDA-approved.</strong> Novo Nordisk submitted CagriSema to the FDA on Dec 18, 2025 (<a href="{NOVO_NDA}" rel="noopener">Novo Nordisk</a>); no decision has been announced.')
_setreg("bpc-157-tb-500-stack",f'<strong>Neither is FDA-approved.</strong> In July 2026 an FDA advisory committee voted to recommend allowing both in pharmacy compounding (<a href="{PCAC_VOTES}" rel="noopener">vote report</a>). The vote is non-binding.')
for k in ["epitalon","kpv"]:
    X3[k]["faq"]=[(q,(f"No. An FDA advisory committee voted in July 2026 to recommend allowing it in compounding, but that vote is non-binding." if q.endswith("FDA-approved?") else a)) for q,a in X3[k]["faq"]]
X3["melanotan-2"]["faq"]=[(q,("It's not FDA-approved. Its cousin afamelanotide is approved as Scenesse for the rare condition EPP." if q=="Is Melanotan II legal?" else a)) for q,a in X3["melanotan-2"]["faq"]]

# ===== Bean verified fact fixes (Oct 18, 4:44 PM) =====
FDA_RISK="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks"
PCAC_OCT24="https://www.fda.gov/media/185412/download"
PCAC_JUL26="https://www.fda.gov/advisory-committees/advisory-committee-calendar/july-23-24-2026-meeting-pharmacy-compounding-advisory-committee-07232026"
def _sub(d,k,old,new):
    assert old in d[k], (k,old[:40]); d[k]=d[k].replace(old,new)
def _pep(k,i,old,new):
    p=list(PEP3[k]); assert old in p[i],(k,old[:40]); p[i]=p[i].replace(old,new); PEP3[k]=tuple(p)
def _ex(k,old,new):
    h,b,c=EXCITE3[k]; b=[new if x==old else x for x in b]; assert new in b,(k,old[:40]); EXCITE3[k]=(h,b,c)
# 2) stack
STACK_RAT=f"In a 2026 study of 32 rats, TB-500 significantly improved tendon strength and structure. BPC-157 showed smaller gains that weren't statistically significant. Adding them together gave no extra benefit ({pm(42542926,'Jt Dis Relat Surg, 2026')})."
h,b,c=EXCITE3["bpc-157-tb-500-stack"]; EXCITE3["bpc-157-tb-500-stack"]=(h,[STACK_RAT]+[x for x in b if "tendon" not in x],c)
_pep("bpc-157-tb-500-stack",4,"32 rats after Achilles tendon repair, 8 per group. TB-500 alone made the strongest tendons; both peptides improved tendon structure. The <strong>combination did not add any benefit</strong> over either peptide alone.",
     "32 rats after Achilles tendon repair, 8 per group. TB-500 significantly improved tendon strength and structure. BPC-157 showed smaller gains that weren't statistically significant. <strong>Adding them together gave no extra benefit.</strong>")
# 3) KPV
_ex("kpv","Blocked inflammation pathways in human gut cells at <strong>nanomolar</strong> amounts.",f"Blocked inflammation pathways in lab-grown human gut cells at <strong>nanomolar</strong> amounts ({pm(18061177,'Gastroenterology, 2008')}).")
# 4) kisspeptin
_ex("kisspeptin","Up to <strong>56% more penile tumescence</strong> vs placebo in men with low desire.",f"Up to <strong>56% more penile tumescence</strong> vs placebo in a 32-man trial (a secondary result, during a 75-minute IV infusion of kisspeptin-54, not the kisspeptin-10 sold online) ({pm(36735255,'JAMA Netw Open, 2023')}).")
_pep("kisspeptin",3,"The human trials used research-clinic infusions.",f'The human trials used research-clinic infusions. FDA lists kisspeptin-10 among bulk compounding substances that may present significant safety risks (<a href="{FDA_RISK}" rel="noopener">FDA</a>), and its advisers voted 11–0 against allowing it in compounding in Oct 2024 (<a href="{PCAC_OCT24}" rel="noopener">FDA meeting minutes</a>).')
_pep("kisspeptin",4,"raised penile tumescence by up to 56% vs placebo, and increased","and, as secondary results during a 75-minute IV infusion of kisspeptin-54, raised penile tumescence by up to 56% vs placebo and increased")
X3["kisspeptin"]["quick"]=[q.replace("<strong>Headline result:</strong> up to 56% more penile tumescence vs placebo in men with low desire.","<strong>Headline result:</strong> up to 56% more penile tumescence vs placebo in men with low desire (a secondary result, IV kisspeptin-54).") for q in X3["kisspeptin"]["quick"]]
# 5) epitalon
_pep("epitalon",4,"through telomerase in some cells and an alternative pathway (ALT) in others","through telomerase in normal cells and an alternative pathway (ALT) in breast cancer cells")
_pep("epitalon",4,"54 mice per group, treated monthly for life.","54 female mice per group, injected 5 days a month from age 3 months until death.")
# 6) cagrilintide
_CAGL=f'<a href="{FDA_GLP1C}" rel="noopener">FDA says cagrilintide can\'t be compounded</a>'
X3["cagrilintide"]["quick"]=[q.replace("the FDA says cagrilintide can't be compounded.",f"the {_CAGL}.") for q in X3["cagrilintide"]["quick"]]
X3["cagrilintide"]["faq"]=[(q,(f'No. The <a href="{FDA_GLP1C}" rel="noopener">FDA says cagrilintide can\'t be compounded</a> under federal law.' if q=="Can cagrilintide be compounded?" else a)) for q,a in X3["cagrilintide"]["faq"]]
_ex("cagrilintide","<strong>−20.4%</strong> average weight at 68 weeks in REDEFINE 1 (3,417 adults).",f"<strong>−20.4%</strong> average weight at 68 weeks in REDEFINE 1 (3,417 adults; 2,108 on CagriSema) ({pm(40544433,'NEJM, 2025')}).")
_sub(X3["cagrilintide"],"dosing","the strength Novo submitted to the FDA.</p>","the strength Novo submitted to the FDA. This is Novo's fixed-dose trial product, not a guide for \"research\" cagrilintide.</p>")
# 7) MT2 FAQ
X3["melanotan-2"]["faq"]=[(q,a.replace("melanomas in users","a few melanoma cases (a causal link isn't proven)")) for q,a in X3["melanotan-2"]["faq"]]
assert any("causal link" in a for q,a in X3["melanotan-2"]["faq"])
# Optional: FDA meeting page alongside the vote report (FDA's page links the archived broadcasts with the tallies)
for k in ["epitalon","kpv","bpc-157-tb-500-stack"]:
    _pep(k,3,'(<a href="'+PCAC_VOTES+'" rel="noopener">vote report</a>)','(<a href="'+PCAC_JUL26+'" rel="noopener">FDA meeting page</a>; <a href="'+PCAC_VOTES+'" rel="noopener">vote report</a>)')
# Optional: Selank 2014 heading
_pep("selank",4,'({pm(25176261,"Russian study, 2014")})'.replace('{pm(25176261,"Russian study, 2014")}',pm(25176261,"Russian study, 2014")),'('+pm(25176261,"Russian study, 2014; design details not reported in English")+')')
