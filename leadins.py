# Oct 26 2026: Bean's guide lead-ins (guide_leadins.md). Every number already on its page.
import re
def pm(i,t): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{t}</a>'
def a(u,t): return f'<a href="{u}" rel="noopener">{t}</a>'
DAF=lambda n:f"https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo={n}"
DM=lambda s:f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={s}"
RO="https://pubmed.ncbi.nlm.nih.gov/"
L={
"semaglutide":(None,f'The one that started it all: −15.3 kg on average in STEP 1 ({pm(33567185,"NEJM 2021")}), plus fewer heart events in a 17,604-person trial ({pm(37952131,"SELECT, NEJM 2023")}), and FDA-approved ({a(DAF(209637),"Ozempic")}, {a(DAF(213051),"Rybelsus")}, {a(DAF(215256),"Wegovy")}).'),
"tirzepatide":(None,f'It went head-to-head with semaglutide and won: −20.2% average body weight vs −13.7% at 72 weeks ({pm(40353578,"SURMOUNT-5, NEJM 2025")}), and it\'s FDA-approved ({a(DAF(215866),"Mounjaro")}, {a(DAF(217806),"Zepbound")}).'),
"orforglipron":(None,f'GLP-1 power with no needles: up to −11.2% average weight at 72 weeks from one daily pill ({pm(40960239,"ATTAIN-1, NEJM 2025")}), FDA-approved as Foundayo in April 2026 ({a("https://www.fda.gov/news-events/press-announcements/fda-approves-first-new-molecular-entity-under-national-priority-voucher-program","FDA")}).'),
"retatrutide":(None,f'−25.0% average body weight at 80 weeks on the 12 mg dose in TRIUMPH-1 ({pm(42814954,"NEJM 2026")}), a bigger average than tirzepatide\'s −20.2% in SURMOUNT-5, in a separate trial. <strong>Investigational and not FDA-approved. Lilly plans to file in Q1 2027.</strong>'),
"tesamorelin":(None,f'FDA-approved (as Egrifta) to reduce excess belly fat in adults with HIV lipodystrophy ({a(DM("839334d3-8c1d-4c26-9036-2ab524a6ea75"),"FDA label")}), and in its pivotal trial deep belly fat fell 15.2% in 26 weeks while it rose 5.0% on placebo ({pm(18057338,"NEJM 2007")}).'),
"pt-141":(None,f'FDA-approved (as Vyleesi) for low sexual desire that causes distress in premenopausal women ({a(DM("f1d0c1b5-2f39-4bad-a6a4-0066e3ad5dcf"),"FDA label")}). It works on desire in the brain, not blood flow, and beat placebo in two Phase 3 trials of 1,267 women ({pm(31599840,"RECONNECT")}; {pm(31599847,"Obstet Gynecol 2019")}).'),
"elamipretide":(None,f'The mitochondria peptide that made it to the FDA: approved as Forzinity in Sept 2025, under accelerated approval, to improve muscle strength in people with Barth syndrome who weigh at least 30 kg ({a(DM("146bf34c-76f2-48db-ac07-fb29cce2cd75"),"FDA label")}; {a(DAF(215244),"Drugs@FDA")}).'),
"bpc-157":("What researchers are excited about: 36 studies on muscle, tendon, ligament and bone healing (35 in animals)",f'A big animal literature on healing ({pm(40756949,"HSS J 2025")}), plus a first small, uncontrolled human report: 14 of 16 people with knee pain reported relief after BPC-157 knee injections ({pm(34324435,"Altern Ther Health Med 2021")}).'),
"tb-500":("What researchers are excited about: the body's own repair protein, thymosin beta-4",f'In a 96-patient heart-attack trial of thymosin beta-4 (not "TB-500" products), patients dosed early showed a benefit. That was a subgroup finding, and the overall result wasn\'t significant ({pm(41229390,"Cardiovasc Res 2025")}).'),
"bpc-157-tb-500-stack":("What researchers are excited about: the first head-to-head \"Wolverine stack\" study (in rats)",f'In 32 rats after Achilles repair, TB-500 significantly improved tendon strength and structure. The stack didn\'t beat it alone ({pm(42542926,"Jt Dis Relat Surg 2026")}).'),
"kpv":("What researchers are excited about: a 3-amino-acid peptide that calmed gut inflammation in mice",f'It reduced colitis in two mouse models and blocked inflammation pathways in lab-grown human gut cells at tiny, nanomolar amounts ({pm(18061177,"Gastroenterology 2008")}; {pm(28143741,"Mol Ther 2017")}). There are no human trials yet.'),
"ghk-cu":("What researchers are excited about: the copper peptide tied to skin repair and collagen (lab research)",f'Lab and gene-expression research links GHK-Cu to skin repair and collagen production ({pm(29986520,"Int J Mol Sci 2018")}), and it helped ligament healing in a rat model ({pm(25731775,"J Orthop Res 2015")}). It\'s already a skincare staple, listed as "copper tripeptide-1."'),
"cjc-1295-ipamorelin":("What researchers are excited about: one CJC-1295 shot, days of higher growth hormone",f'In small placebo-controlled studies in healthy adults, a single CJC-1295 injection raised growth hormone 2–10× for 6+ days and IGF-1 1.5–3× for 9–11 days ({pm(16352683,"J Clin Endocrinol Metab 2006")}). That\'s hormone levels, not muscle or fat.'),
"mots-c":("What researchers are excited about: the \"exercise in a vial\" peptide your mitochondria make",f'In mice it improved how the body handles sugar and fat, preventing diet-induced obesity and insulin resistance ({pm(25738459,"Cell Metab 2015")}), and the first Phase 2a human trial, in prediabetes, is now registered, with no results yet ({a("https://clinicaltrials.gov/study/NCT07505745","NCT07505745")}).'),
"semax":("What researchers are excited about: the nasal brain peptide that raised BDNF in stroke rehab",f'In a 110-patient stroke-rehab study, the Semax groups had higher BDNF (a brain growth factor) and better daily-function scores. The study wasn\'t described as randomized or blinded ({pm(29798983,"2018 study")}).'),
"selank":("What researchers are excited about: the calm-and-focus nasal peptide from Russian clinical research",f'A 60-patient Russian study reported a pronounced anti-anxiety effect ({pm(25176261,"2014")}), and adding Selank to the tranquilizer phenazepam was linked to fewer side effects in 70 patients ({pm(26356395,"2015")}). Both are small studies published in Russian.'),
"epitalon":("What researchers are excited about: longer telomeres in lab cells, and a longer maximum lifespan in mice",f'Epitalon lengthened telomeres in human cell lines in a dish ({pm(40908429,"Biogerontology 2025")}), and mice given it had a 12.3% longer maximum lifespan, while mean lifespan didn\'t change ({pm(14501183,"Biogerontology 2003")}). No randomized human trial has proven a benefit ({pm(42884164,"Int J Mol Sci 2026")}).'),
"kisspeptin":("What researchers are excited about: the hormone that lit up the brain's desire circuits in scan trials",f'In small randomized, placebo-controlled brain-scan trials, kisspeptin shifted sexual brain processing in men and women with low desire ({pm(36735255,"JAMA Netw Open 2023")}; {pm(36287566,"JAMA Netw Open 2022")}). In men it also raised tumescence by up to 56% vs placebo during a research IV infusion of kisspeptin-54, not the kisspeptin-10 sold online.'),
"melanotan-2":("What researchers are excited about: the tanning hormone mimic from 1990s Arizona trials",f'In the first tiny human pilot, 2 of 3 men tanned measurably after 5 injections ({pm(8637402,"Life Sci 1996")}), and in a 10-man placebo-controlled study 8 of 10 with psychogenic ED had erections ({pm(9679884,"J Urol 1998")}). These are small 1990s studies with real side effects.'),
"cagrilintide":(None,f'−20.4% average body weight at 68 weeks in REDEFINE 1, 3,417 adults ({pm(40544432,"NEJM 2025")}). <strong>Investigational: Novo submitted CagriSema to the FDA in Dec 2025, and no decision has been announced.</strong>'),
"collagen-peptides":(None,f'Better-hydrated, bouncier skin, backed by 26 randomized trials and 1,721 people ({pm(37432180,"Nutrients 2023")}). A second analysis of 19 trials found benefits for wrinkles too ({pm(33742704,"Int J Dermatol 2021")}).'),
}
STATUS_LEAD=f'Five positive Phase 3 trials and a filing planned for Q1 2027. Here\'s every win so far, and why it\'s still <strong>not FDA-approved</strong>.'
def block(h,lead):
    hh=f'<p class="lead-h"><strong>{h}</strong></p>' if h else ''
    return f'<div class="g-lead">{hh}<p>{lead}</p></div>'
def nums(t):
    t=re.sub(r'<a [^>]*>.*?</a>','',t); t=re.sub('<[^>]+>','',t)
    return set(re.findall(r'\d[\d,.]*',t))
def text(h): return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',h)).replace('&#x27;',"'")
def apply(pages):
    skipped=[];done=[]
    for slug,(h,lead) in L.items():
        k=f"peptides/{slug}.html"; v=list(pages[k]); body=v[2]
        miss=[n.rstrip('.,') for n in nums((h or '')+' '+lead) if n.rstrip('.,') not in text(body)]
        if miss: skipped.append((slug,miss)); continue
        assert body.count('</header>')==1,slug
        v[2]=body.replace('</header>','</header>'+block(h,lead),1); pages[k]=tuple(v); done.append(slug)
    k="peptides/retatrutide-fda-approval-status.html"; v=list(pages[k])
    miss=[n for n in nums(STATUS_LEAD) if n not in text(v[2])]
    if miss: skipped.append(("retatrutide-fda-approval-status",miss))
    else:
        i=v[2].index('</h1>')+5
        v[2]=v[2][:i]+'<p><span class="badge research">Investigational · not FDA-approved</span></p>'+block(None,STATUS_LEAD)+v[2][i:]; pages[k]=tuple(v); done.append("retatrutide-fda-approval-status")
    return done,skipped
CSS='.g-lead{margin:14px 0 6px;font-size:1.06rem}.g-lead p{margin:0 0 6px}.lead-h{font-family:var(--serif);font-size:1.12rem}'
