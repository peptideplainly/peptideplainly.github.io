"""Generate static pages. Run: python3 site.py"""
import pathlib,html
P=pathlib.Path(__file__).parent; BASE="https://peptideplainly.com"  # placeholder domain
NAV=[("peptides/index.html","Peptide guides"),("peptides-101.html","Peptides 101"),("glossary.html","Glossary"),("newsletter.html","Newsletter"),("about.html","About"),("advertise.html","Advertise")]
EMBED='<div class="bh-embed"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="a82b15dd-c14b-4719-8c4a-a19f32016cdc"></script></div><p class="fine sub-fallback">Form not loading? <a href="https://peptideplainly.beehiiv.com/subscribe" data-goatcounter-click="signup-cta" rel="noopener">Subscribe here</a>.</p>'
ATTR='<script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script>'
def pm(i,label): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{label}</a>, PMID {i}'
import json
ORG={'@type':'Organization','@id':BASE+'/#org','name':'Peptide Plainly','url':BASE+'/','logo':BASE+'/preview.png'}
def ld(objs): return ''.join('<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org',**o},ensure_ascii=False)+'</script>' for o in objs)
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;600;700&display=optional" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;600;700&display=optional"></noscript><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
LOGO='<svg class="logo" viewBox="0 0 40 40" width="34" height="34" aria-hidden="true"><circle cx="9" cy="20" r="6" fill="#0f766e"/><circle cx="20" cy="20" r="6" fill="#e8b04b"/><circle cx="31" cy="20" r="6" fill="#c2410c"/></svg>'
OG_IMG={}  # path -> og/<card>.png, filled in below for pages whose card exists (render cards: .pwvenv/bin/python scripts/og.py)
def page(path,title,desc,body,schema=(),root=None,robots=""):
    """Shared layout for every page: header nav (incl. Advertise), signup band, footer, GoatCounter.
    root: link prefix; pass "/" for pages served at arbitrary URLs (404.html)."""
    root="../"*path.count("/") if root is None else root
    cur=path
    og=OG_IMG.get(path,"preview.png")
    nav="".join(f'<a href="{root}{h}"'+(' aria-current="page"' if h==cur else '')+f'>{t}</a>' for h,t in NAV)
    url=f"{BASE}/{path}".replace("/index.html","/")
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}"><meta name="theme-color" content="#0f766e">{robots and f'<meta name="robots" content="{robots}">'}
<meta property="og:type" content="website"><meta property="og:site_name" content="Peptide Plainly"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{html.escape(title)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{BASE}/{og}">
{FONTS}<link rel="stylesheet" href="{root}style.css?v=13">{ld(schema)}<script data-goatcounter="https://peptideplainly.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="nav-in"><a class="brand" href="{root}index.html">{LOGO}<span>Peptide <b>Plainly</b></span></a><nav aria-label="Main">{nav}<a class="nav-sub" href="https://peptideplainly.beehiiv.com/subscribe" data-goatcounter-click="signup-cta" rel="noopener">Get the Friday email</a></nav></div></header>
<main id="main">{body}</main>
<section class="cta-band" id="signup"><div class="cta-in"><p class="kicker">Every Friday · free</p><h2>The week's biggest peptide news. Five minutes. Free.</h2><p>New results, new compounds, explained plainly every Friday.</p>
{EMBED}</div></section>
<footer><div class="foot-in"><p class="brand-foot">Peptide <b>Plainly</b></p><p><a href="{root}peptides/index.html">All guides</a> · <a href="{root}peptides-101.html">Peptides 101</a> · <a href="{root}glossary.html">Glossary</a> · <a href="{root}newsletter.html">This week&#39;s issue</a> · <a href="{root}why-peptide-info-is-confusing.html">Why so confusing?</a> · <a href="{root}peptide-reconstitution-calculator.html">Peptide calculator</a> · <a href="{root}how-to-tell-if-a-peptide-source-is-legit.html">Is your source legit?</a> · <a href="{root}about.html">About &amp; disclaimer</a> · <a href="{root}advertise.html">Advertise</a></p><p class="fine">Not medical advice. Education only. Sources linked on every claim. © 2026 Peptide Plainly</p></div></footer>{ATTR}</body></html>'''
DISC='<p class="disclaimer"><strong>Not medical advice.</strong> Education only. We don\'t sell anything or tell you what to take. Label doses are there so you can follow along with your prescriber. Talk to a licensed clinician about your health.</p>'
pages={}
# ---- Newsletter: only the newest SENT issue is published, at /newsletter.html ----
# An issue is published only if issues/issue-NNN.md starts with front matter containing `sent: true`:
#   ---
#   sent: true
#   headline: One-line teaser for the home page (optional)
#   ---
# Unmarked issues are skipped entirely: no HTML, not "newest", not in sitemap or llms.txt.
import markdown as _md, re as _r2, datetime as _dt
def _issue(p):
    t=p.read_text(); fm={}
    m=_r2.match(r"---\s*\n(.*?)\n---\s*\n",t,_r2.S)
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln: k,v=ln.split(":",1); fm[k.strip().lower()]=v.strip().strip('"')
        t=t[m.end():]
    n=int(p.stem.split("-")[1]); dm=_r2.search(r"Week of ([A-Z][a-z]+ \d{1,2}, \d{4})",t)
    date=dm.group(1) if dm else ""
    heads=_r2.findall(r"^## (.+)$",t,_r2.M)
    return dict(n=n,stem=p.stem,md=t,sent=fm.get("sent","").lower()=="true" or fm.get("status","").lower()=="sent",date=date,
        iso=_dt.datetime.strptime(date,"%B %d, %Y").date().isoformat() if date else "",
        headline=fm.get("headline") or (heads[0].split(". ",1)[-1] if heads else f"Issue #{n}"),count=len(heads))
ALL_ISSUES=sorted((_issue(p) for p in (P/"issues").glob("issue-*.md")),key=lambda i:i["n"])
SENT=[i for i in ALL_ISSUES if i["sent"]]
CUR=SENT[-1] if SENT else None
if CUR:
    _body=_md.markdown(CUR["md"],extensions=["extra","nl2br"])
    _body=_r2.sub(r"<h1>.*?</h1>","",_body,count=1,flags=_r2.S)
    _d=f"Issue #{CUR['n']} of Peptide Plainly"+(f", week of {CUR['date']}" if CUR['date'] else "")+f": {CUR['count']} new peptide studies, explained plainly. New issue every Friday."
    _eb="This week's issue · Issue #"+str(CUR["n"])+(" · "+CUR["date"] if CUR["date"] else "")
    pages["newsletter.html"]=("This week's issue: Peptide Plainly newsletter",_d[:155],
     f'''<article class="issue"><p class="eyebrow">{_eb}</p><h1>This week's issue</h1>{_body}
<div class="nl-cta"><h2>Get next Friday's issue in your inbox</h2><p>Free, five minutes, every Friday.</p><p><a class="btn" href="https://peptideplainly.beehiiv.com/subscribe" data-goatcounter-click="signup-newsletter-page" rel="noopener">Get next Friday's issue</a></p></div></article>''',
     [ORG,{"@type":"Article","headline":f"Peptide Plainly Issue #{CUR['n']}","url":BASE+"/newsletter.html","datePublished":CUR["iso"],"author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}}])
    HOME_ISSUE=f'<a class="row-link" href="newsletter.html"><span class="issue-n">#{CUR["n"]}</span><span><strong>{html.escape(CUR["headline"])}</strong><br><span class="fine">{CUR["date"]} · {CUR["count"]} studies</span></span></a>'
else:
    HOME_ISSUE='<p>The first issue lands Friday. <a href="#signup">Get it in your inbox</a>.</p>'
pages["peptides-101.html"]=("Peptides 101: a beginner's guide to peptides | Peptide Plainly","What are peptides? A plain-English beginner's guide: approved medicines vs research-only compounds, how to read a study, and how to pick a quality source.",f'''<article class="issue">
<p class="eyebrow">Beginner's guide</p><h1>Peptides 101</h1><p class="lead">Welcome! If peptide videos have left you more confused than when you started, you're in the right place. Here's everything you need, in about five minutes.</p>
<h2>What is a peptide?</h2><p>A peptide is a short chain of <strong>amino acids</strong>, the same building blocks that make up proteins. Long chains are called proteins and short ones are called peptides. Your body makes thousands of them, and many act as messengers. <strong>Insulin</strong>, for example, is a peptide hormone that helps control blood sugar.</p>
<p>"Peptides" is a huge, loose category. It covers prescription medicines, ingredients in skin creams, food supplements like collagen, and experimental compounds that have never been properly tested in people. The word alone tells you nothing about whether something is safe or works.</p>
<h2>Approved medicines vs. "research-only" compounds</h2>
<ul><li><strong>Approved drugs</strong> (for example semaglutide and tirzepatide) have passed large clinical trials. Regulators like the U.S. FDA reviewed the data, and they're made under strict quality controls. They're prescribed by clinicians.</li>
<li><strong>Dietary supplements</strong> (for example collagen peptides) are sold as foods. In the U.S. the <a href="https://www.fda.gov/food/information-consumers-using-dietary-supplements/questions-and-answers-dietary-supplements">FDA does not approve supplements before they are marketed</a>.</li>
<li><strong><span class="badge research">Research purposes only</span></strong> compounds (for example BPC-157 and TB-500) aren't FDA-approved medicines. Product quality can vary, and the human evidence is usually early and limited. Some, including BPC-157 and TB-500, are banned in sport under the <a href="https://www.wada-ama.org/en/prohibited-list">WADA Prohibited List</a>.</li></ul>
<h2>How to read a study (the quick version)</h2>
<ol><li><strong>Who was studied?</strong> Cells in a dish → animals → people. Lab and animal results often don't hold up in humans.</li>
<li><strong>How many?</strong> 12 people is a pilot. Thousands is much more convincing.</li>
<li><strong>Was there a comparison group?</strong> A randomized controlled trial (RCT) compares people who got the treatment with people who got a placebo. Without one, it's hard to know whether the treatment did anything.</li>
<li><strong>What was measured?</strong> A lab marker isn't the same as feeling better or living longer.</li>
<li><strong>Who paid?</strong> Industry funding is common and not automatically bad, but it's worth noting.</li>
<li><strong>One study is never the final word.</strong> Look for systematic reviews and meta-analyses that pool many studies.</li></ol>
<p>New to the terms? See the <a href="glossary.html">glossary</a>.</p>
<h2>How to pick a quality source</h2>
<ul><li><strong>Third-party lab tests.</strong> Look for a recent certificate of analysis (COA) from an independent lab, matched to your batch.</li>
<li><strong>Citations you can click.</strong> The best sources link to the actual study or FDA label.</li>
<li><strong>Clear labeling.</strong> Purity, amount per vial, and batch number should be easy to find.</li>
<li><strong>Know the study type.</strong> Human trials, animal studies and lab work each tell you something different.</li>
<li><strong>Transparent sellers.</strong> Real contact details, clear policies, and honest disclosure of affiliate links.</li>
<li><strong>For prescription drugs,</strong> go through a licensed prescriber and pharmacy.</li></ul>
<h2>Where to go next</h2><p>Read our plain-English <a href="peptides/index.html">guides to popular peptides</a>, or read <a href="newsletter.html">this week&#39;s issue</a>.</p>{DISC}</article>''')
G=[("Abstract","A short summary at the top of a research paper."),("Amino acid","A building block of proteins and peptides. There are 20 standard ones."),("Animal study","Research done in animals, often mice or rats. Results often don't carry over to humans."),("Bias","Anything that systematically skews a study's results away from the truth."),("Case report","A description of one patient or a few patients. Useful for ideas, weak as evidence."),("Clinical trial","A study that tests a treatment in people."),("Cohort study","An observational study that follows groups of people over time. It can show links but not cause and effect."),("Confidence interval (CI)","The range the true effect probably falls in. Narrow is more precise."),("Control group","Participants who don't get the treatment, used for comparison."),("Double-blind","Neither participants nor researchers know who got the real treatment."),("FDA","U.S. Food and Drug Administration, which approves medicines in the U.S."),("GLP-1","A natural gut hormone (glucagon-like peptide-1) involved in appetite and blood sugar. Semaglutide mimics it."),("GLP-1 receptor agonist","A drug that activates the GLP-1 receptor, such as semaglutide."),("Hazard ratio (HR)","Compares how often an event happens in two groups. Below 1 means less often in the treatment group."),("In vitro","Done in cells or tissue in a lab, not in a living body."),("Meta-analysis","A study that statistically combines the results of many earlier studies."),("Observational study","Researchers watch what happens without assigning treatments."),("Peptide","A short chain of amino acids."),("Pilot study","A small, early study to test whether a bigger one is feasible."),("Placebo","An inactive dummy treatment used for comparison."),("PMID","PubMed ID, a unique number for each paper on PubMed."),("PubMed","A free database of medical research run by the U.S. National Library of Medicine."),("Randomized controlled trial (RCT)","Participants are randomly assigned to a treatment or a control. The gold standard for testing treatments."),("Research chemical","A compound sold for lab research, not approved for human use."),("Retrospective study","Looks back at existing records rather than following people forward."),("Systematic review","A structured review of all studies on a question, following a set method."),("WADA","World Anti-Doping Agency, which maintains the list of substances banned in sport.")]
pages["glossary.html"]=("Peptide research glossary: plain-English definitions | Peptide Plainly","Plain-English definitions of peptide and research terms: RCT, meta-analysis, placebo, hazard ratio, GLP-1, PMID and more.",'<article class="issue"><p class="eyebrow">Reference</p><h1>Glossary</h1><p class="lead">Research terms, translated into plain English.</p><dl class="gloss">'+"".join(f'<dt id="{t.split()[0].lower()}">{t}</dt><dd>{d}</dd>' for t,d in G)+'</dl><p>Ready to use them? Try <a href="peptides-101.html">Peptides 101</a>.</p>'+DISC+'</article>')
PEP={
"semaglutide":("Semaglutide","What is semaglutide (Ozempic, Wegovy)? A plain-English guide to what it is, its approval status, the key human trials, and common myths.",
"Semaglutide is a lab-made version of the gut hormone GLP-1. It's sold under brand names including Ozempic and Rybelsus (type 2 diabetes) and Wegovy (weight management).",
'FDA-approved prescription medicine. Ozempic (injection) and Rybelsus are labeled for blood-sugar control in adults with type 2 diabetes, and Ozempic also for lowering heart-event risk in some of those adults. Wegovy is labeled for long-term weight management in certain adults and children 12+, and for lowering major heart-event risk in adults with heart disease and overweight or obesity. Sources: Drugs@FDA <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=209637">Ozempic</a>, <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=213051">Rybelsus</a>, <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=215256">Wegovy</a>. Exact indications are in the current FDA label.',
f'''<li><strong>STEP 1</strong> ({pm(33567185,"NEJM, 2021")}): an RCT in adults with overweight or obesity. Over 68 weeks, weight changed by −15.3 kg with semaglutide vs. −2.6 kg with placebo, alongside lifestyle intervention. Nausea and diarrhea were the most common side effects.</li>
<li><strong>SELECT</strong> ({pm(37952131,"NEJM, 2023")}): 17,604 people with heart disease and overweight/obesity but no diabetes. Major cardiovascular events occurred in 6.5% on semaglutide vs. 8.0% on placebo.</li>
<li><strong>Kidney disease trial</strong> ({pm(42823485,"Nature Medicine, 2026")}): a 106-person RCT exploring how it may protect the kidneys in type 2 diabetes. Covered in our <a href="../newsletter.html">newsletter</a>.</li>''',
["<strong>Myth: it works without side effects.</strong> Gastrointestinal side effects are common in trials, and some people stop treatment because of them.","<strong>Myth: \"research\" or compounded versions are the same thing.</strong> Only the approved products went through the regulatory review of the trial data described above."]),
"tirzepatide":("Tirzepatide","What is tirzepatide (Mounjaro, Zepbound)? A plain-English guide to how it works, its approval status, key trials, and myths.",
"Tirzepatide activates two hormone receptors, GIP and GLP-1. It's sold as Mounjaro (type 2 diabetes) and Zepbound (weight management).",
'FDA-approved prescription medicine. Mounjaro (approved 2022) is labeled for blood-sugar control in type 2 diabetes. Zepbound (approved 2023) is labeled for long-term weight management in certain adults and for moderate-to-severe obstructive sleep apnea in adults with obesity. Sources: Drugs@FDA <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=215866">Mounjaro</a>, <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=217806">Zepbound</a>.',
f'''<li><strong>SURMOUNT-1</strong> ({pm(35658024,"NEJM, 2022")}): a 72-week RCT in adults with obesity that found substantial, sustained weight reduction vs. placebo. GI side effects were the most common.</li>
<li><strong>SURMOUNT-5</strong> ({pm(40353578,"NEJM, 2025")}): a head-to-head trial in 751 people with obesity but without diabetes. Average weight change was −20.2% with tirzepatide vs. −13.7% with semaglutide at 72 weeks.</li>
<li><strong>Real-world heart outcomes</strong> ({pm(42840232,"2026")}): an observational study linking tirzepatide to fewer cardiovascular events than semaglutide in type 2 diabetes. Association only. Covered in our <a href="../newsletter.html">newsletter</a>.</li>''',
["<strong>Myth: it's just a stronger semaglutide.</strong> It acts on an extra receptor (GIP), so it's a different molecule with its own trial record.","<strong>Myth: weight stays off after stopping.</strong> These trials measured people while they were on treatment. Ask a clinician about what happens after stopping."]),
"bpc-157":("BPC-157","What is BPC-157? A plain-English, evidence-first look at the 'healing peptide': regulatory status, the limited human evidence, and common myths.",
"BPC-157 (\"Body Protection Compound-157\") is a synthetic peptide of 15 amino acids, originally derived from a protein found in stomach juice. It's popular online for injury recovery.",
'Not an FDA-approved drug for any use. It is banned at all times in sport: the <a href="https://www.wada-ama.org/en/prohibited-list">2026 WADA Prohibited List</a> names BPC-157 under S0 (non-approved substances). In 2023 the FDA listed BPC-157 among bulk substances that "may present significant safety risks" for compounding, noting limited human safety information. In April 2026 it was removed from that category after its nomination was withdrawn, which does <em>not</em> mean it was approved. Its compounding status is under FDA advisory-committee review (<a href="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks">FDA page</a>). It is widely sold online as a "research chemical."',
f'''<li><strong>Systematic review, 2026</strong> ({pm(42885452,"Acta Orthop Belg")}): found 3 small human studies with 30 people in total: knee injections (16 people), bladder instillation (12) and an IV safety pilot (2). Most participants reported improvement, with no treatment-related side effects. Because the studies are small and early, with no control groups, the authors rated the certainty of evidence <em>very low</em> and call for proper clinical trials.</li>
<li><strong>Systematic review, 2025</strong> ({pm(40756949,"HSS Journal")}): 36 studies, almost all in animals, showing better healing of muscle, tendon, ligament and bone injuries. Its one human study is the knee-injection chart review below. The authors note there is no clinical safety data in humans yet.</li>
<li><strong>Knee injection study, 2021</strong> ({pm(34324435,"Altern Ther Health Med")}): a look back at 16 patients who got BPC-157 knee injections. 14 of 16 (87.5%) reported knee pain relief, including 11 of the 12 who got BPC-157 alone. (The 2025 review above reports this study as 7 of 12 with relief lasting over 6 months.) It's a small, uncontrolled study.</li>''',
["<strong>Myth: \"it's proven to heal tendons.\"</strong> Healing results come mostly from animal studies. Human data is tiny and low quality.","<strong>Myth: \"no side effects = safe.\"</strong> No reported side effects in 30 people isn't evidence of safety, and products bought online may not contain what the label says."]),
"tb-500":("TB-500 (thymosin beta-4)","What is TB-500? A plain-English guide to thymosin beta-4 and TB-500: what they are, regulatory status, the human evidence, and myths.",
"Thymosin beta-4 (Tβ4) is a natural protein involved in cell movement and tissue repair. \"TB-500\" is the name used online for a synthetic product based on part of Tβ4. TB-500 itself is not the same molecule that has been tested in clinical trials.",
'Neither TB-500 nor thymosin beta-4 is an FDA-approved drug. The <a href="https://www.wada-ama.org/en/prohibited-list">2026 WADA Prohibited List</a> bans "thymosin-β4 and its derivatives e.g. TB-500" at all times (section S2). FDA\'s compounding safety page says it identified no human exposure data for the TB-500 fragment (<a href="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks">FDA page</a>). Its compounding status is also under review in 2026.',
f'''<li><strong>Heart attack trial</strong> ({pm(41229390,"Cardiovasc Res, 2025")}): recombinant human Tβ4 was tested in 96 heart-attack patients. The overall difference in infarct size vs. placebo was <em>not</em> significant. A benefit was seen only in a subgroup dosed early.</li>
<li><strong>Eye research review</strong> ({pm(30063853,"Expert Opin Biol Ther, 2018")}): describes Tβ4 eye drops being developed for corneal and dry-eye conditions. This is a researcher's narrative review, not trial results.</li>
<li>We found <strong>no</strong> controlled human trials of products sold as "TB-500."</li>''',
["<strong>Myth: TB-500 is a clinically tested drug.</strong> Clinical research has used thymosin beta-4 itself, not the online TB-500 product.","<strong>Myth: it speeds up any injury.</strong> Most repair data comes from lab and animal studies."]),
"ghk-cu":("GHK-Cu (copper peptide)","What is GHK-Cu, the copper peptide? A plain-English guide: what it is, where it's used, what the evidence shows, and common myths.",
"GHK is a tiny natural peptide made of three amino acids (glycine, histidine, lysine) that binds copper, which gives the name GHK-Cu. It's best known as a skincare ingredient.",
'It\'s common in skincare products (often listed as "copper tripeptide-1"). U.S. cosmetics and their ingredients <a href="https://www.fda.gov/cosmetics/cosmetics-laws-regulations/fda-authority-over-cosmetics-how-cosmetics-are-not-fda-approved-are-fda-regulated">don\'t need FDA premarket approval</a>. GHK-Cu isn\'t an FDA-approved drug. For injectable use, FDA has cited immunogenicity risk and limited human data (<a href="https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks">FDA page</a>), and its compounding status is under review.',
f'''<li><strong>Review, 2018</strong> ({pm(29986520,"Int J Mol Sci")}): summarizes lab, animal, and gene-expression research suggesting roles in skin repair and collagen production. The evidence comes mainly from lab and gene-expression data, not large human clinical trials.</li>
<li>Most other recent research is in cells or animals, for example a rat ligament-healing model ({pm(25731775,"J Orthop Res, 2015")}).</li>
<li>We did not find large randomized trials of GHK-Cu in people, injected or applied to the skin.</li>''',
["<strong>Myth: it reverses aging.</strong> Lab findings on gene activity don't show anti-aging effects in people.","<strong>Myth: skincare results apply to injections.</strong> Skin creams and injected research products are very different things."]),
"collagen-peptides":("Collagen peptides","Do collagen peptides work? A plain-English guide to collagen supplements: what they are, regulatory status, what meta-analyses show for skin, and myths.",
"Collagen peptides (hydrolyzed collagen) are collagen protein broken into small pieces, usually from cows, pigs, or fish. They're sold as powders and drinks.",
'Sold as dietary supplements and foods. Under the 1994 DSHEA law, the <a href="https://www.fda.gov/food/information-consumers-using-dietary-supplements/questions-and-answers-dietary-supplements">FDA does not have authority to approve dietary supplements before they are marketed</a>. Manufacturers are responsible for safety and labeling.',
f'''<li><strong>Meta-analysis, 2023</strong> ({pm(37432180,"Nutrients")}): 26 RCTs with 1,721 people found improved skin hydration and elasticity vs. placebo. The authors flagged biases in the studies and called for larger trials.</li>
<li><strong>Meta-analysis, 2021</strong> ({pm(33742704,"Int J Dermatol")}): 19 RCTs with 1,125 people (95% women) found favorable effects on hydration, elasticity, and wrinkles.</li>''',
["<strong>Myth: collagen you eat goes directly to your skin.</strong> It's digested into smaller pieces first. How the benefits seen in trials happen is still being studied.","<strong>Myth: every collagen product is backed by these trials.</strong> The studies tested specific products, sources, and durations, and some studies had industry funding."]),
}
from extras import X
from extras2 import PEP2,X2
from design import META,CATS,icon
from tone import EXCITE,INTRO,NOTE,BOTTOM,DESC,H1,QUICKFIX,FAQFIX
from extras3 import PEP3,X3,META3,EXCITE3,TITLES3
META.update(META3); EXCITE.update(EXCITE3)
PEP.update(PEP2); PEP.update(PEP3); X.update(X2); X.update(X3); PEP={k:PEP[k] for k in META}
for k,d in DESC.items(): PEP[k]=(PEP[k][0],d)+PEP[k][2:]
for k in X:
    X[k]['h1']=H1.get(k,X[k]['h1']); X[k].pop('str'+'aight',None)
    fx=QUICKFIX.get(k,{}); X[k]['quick']=[next((v for lab,v in fx.items() if q.startswith(f'<strong>{lab}:')),q) for q in X[k]['quick']]
    X[k]['faq']=[(q,FAQFIX.get((k,q),a)) for q,a in X[k]['faq']]
for k,b in BOTTOM.items(): X[k]['quick']=[q for q in X[k]['quick'] if 'Bottom line' not in q]+[b]
LOWER={"Semaglutide","Tirzepatide","Retatrutide","Orforglipron","Tesamorelin"}
QH={"collagen-peptides":("What are collagen peptides?","Are collagen peptides FDA-approved?"),"cjc-1295-ipamorelin":("What are CJC-1295 and ipamorelin?","Are CJC-1295 and ipamorelin FDA-approved?")}
GLP1=["semaglutide","tirzepatide","retatrutide","orforglipron"]
GLP1_DESC={'semaglutide': 'What is semaglutide (Ozempic, Wegovy, Rybelsus)? How it works, STEP 1 and SELECT results, FDA label dosing, side effects and FAQs.', 'tirzepatide': 'What is tirzepatide (Mounjaro, Zepbound)? How it works, how it beat semaglutide in SURMOUNT-5, FDA label dosing, side effects and FAQs.', 'retatrutide': "What is retatrutide? Lilly's triple-agonist shot hit up to −25% average weight change in TRIUMPH-1. Results, side effects, FDA status and FAQs.", 'orforglipron': "What is orforglipron (Foundayo)? Lilly's FDA-approved daily GLP-1 pill: how it works, ATTAIN-1 results, label dosing, side effects and FAQs."}
GLP1_TITLE={'semaglutide': 'What is semaglutide? Ozempic & Wegovy results, dosing', 'tirzepatide': 'What is tirzepatide? Mounjaro & Zepbound results, dosing', 'retatrutide': 'What is retatrutide? Results, side effects & status', 'orforglipron': 'What is orforglipron (Foundayo)? The GLP-1 pill explained'}
for k,d in GLP1_DESC.items(): PEP[k]=(PEP[k][0],d)+PEP[k][2:]
def glp1_spot(R,h="h2"):
    cards=""
    for s in GLP1:
        bk,bt=X[s]["badge"]; hot=s=="retatrutide"
        cards+=f'<a class="pcard cat-weight glp1-card{" hot" if hot else ""}" href="{R}{s}.html" data-goatcounter-click="glp1-{s}">{'<span class="hot-tag">🔥 Hot right now</span>' if hot else ''}<span class="pbody"><strong class="pname">{PEP[s][0]}</strong><span class="badge {bk}">{bt}</span><span class="puse">{EXCITE[s][2]}</span><span class="glp1-go">Read the guide →</span></span></a>'
    return f'<section class="wide glp1" aria-label="GLP-1 spotlight"><div class="glp1-in"><p class="kicker">Spotlight · weight loss</p><{h}>The GLP-1s everyone&#39;s talking about</{h}><p class="glp1-sub">The four biggest names in weight loss right now, from the drug that started it all to the triple-threat in trials.</p><div class="glp1-grid">{cards}</div><!--GLP1CMP:{R}--></div></section>'
def glp1_compare(slug):
    o="".join(f'<li><a href="{s}.html" data-goatcounter-click="compare-{slug}-{s}">{PEP[s][0]}</a></li>' for s in GLP1 if s!=slug)
    return f'<nav class="related glp1-compare" aria-label="Compare the GLP-1s"><h2>Compare the GLP-1s</h2><ul>{o}</ul><p><a href="../glp1-comparison.html" data-goatcounter-click="compare-{slug}-all">See all four side by side →</a></p></nav>'
STATUS_CLASS=lambda bk:{"approved":"approved","research":"research","supplement":"supplement"}[bk]
HOMECARDS=""; rows=""; gcards=""
for slug,(name,desc,what,reg,ev,myths) in PEP.items():
    x=X[slug]; bk,bt=x["badge"]; cat,use,how,_=META[slug]
    card=f'<a class="pcard cat-{cat}" href="{{R}}{slug}.html" data-cat="{cat}"><span class="pic">{icon(cat)}</span><span class="pbody"><span class="pcat">{CATS[cat]}</span><strong class="pname">{name}</strong><span class="badge {bk}">{bt}</span><span class="puse">{EXCITE[slug][2]}</span></span></a>'
    HOMECARDS+=card.replace("{R}","peptides/"); gcards+=card.replace("{R}","")
    rows+=f'<tr data-cat="{cat}"><th scope="row"><a href="{slug}.html">{name}</a></th><td>{use}</td><td><span class="badge {bk}">{bt}</span></td><td>{how}</td></tr>'
for slug,(name,desc,what,reg,ev,myths) in PEP.items():
    x=X[slug]; bk,bt=x["badge"]; cat=META[slug][0]
    sib=[s for s in PEP if META[s][0]==cat and s!=slug]
    others=" · ".join(f'<a href="{s}.html">{PEP[s][0]}</a>' for s in PEP if s!=slug)
    rel="".join(f'<li><a href="{s}.html">{PEP[s][0]}</a></li>' for s in sib)
    faqh="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in x["faq"])
    url=f"{BASE}/peptides/{slug}.html"; short=name.split(" (")[0]; low=short.lower() if short in LOWER else short
    schema=[ORG,{"@type":"MedicalWebPage","name":x["h1"],"description":desc,"url":url,"inLanguage":"en","lastReviewed":"2026-10-16","publisher":{"@id":BASE+"/#org"},"about":{"@type":"Drug" if bk!="supplement" else "DietarySupplement","name":short}},
      {"@type":"Article","headline":x["h1"],"description":desc,"url":url,"datePublished":"2026-10-16","dateModified":"2026-10-16","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":html.unescape(__import__('re').sub('<[^>]+>','',a))}} for q,a in x["faq"]]},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Peptide guides","item":BASE+"/peptides/"},{"@type":"ListItem","position":3,"name":short,"item":url}]}]
    pages[f"peptides/{slug}.html"]=(GLP1_TITLE.get(slug,x["h1"]+" | Peptide Plainly"),desc,f'''<article class="guide cat-{cat}"><p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Peptide guides</a> / {short}</p>
<header class="g-head"><span class="pic big">{icon(cat)}</span><div><p class="pcat">{CATS[cat]}</p><h1>{x["h1"]}</h1><p><span class="badge {bk}">{bt}</span> <span class="fine">Checked against official sources Oct 16, 2026</span></p></div></header>
<aside class="excite" aria-label="Why people are excited"><p class="kicker">Why people are excited</p><p class="sa">{EXCITE[slug][0]}</p><ul>{"".join(f"<li>{h}</li>" for h in EXCITE[slug][1])}</ul></aside>
<div class="quick"><h2>Quick facts</h2><ul>{"".join(f"<li>{q}</li>" for q in x["quick"])}</ul><p class="jump"><a href="#dosing">Dosing &amp; timing</a><a href="#evidence">Evidence</a><a href="#faq">FAQ</a></p></div>{glp1_compare(slug) if slug in GLP1 else ""}
<h2>{QH.get(slug,(f"What is {low}?",))[0]}</h2><p>{INTRO.get(slug,what)}</p><h2>{QH.get(slug,(0,f"Is {low} FDA-approved?"))[1]}</h2><p>{reg}</p>
{x["dosing"]}
<h2 id="evidence">What the research shows</h2><ul>{ev}</ul><p class="fine">New to these terms? See the <a href="../glossary.html">glossary</a>.</p>
<h2 id="faq">{short} FAQ</h2>{faqh}{NOTE if bk=="research" else ""}{DISC}
{"" if slug in GLP1 else (f'<nav class="related" aria-label="Related guides"><h2>Same category</h2><ul>{rel}</ul></nav>' if rel else '')}
<p class="fine">All guides: {others} · <a href="../peptides-101.html">Peptides 101</a> · <a href="../why-peptide-info-is-confusing.html">Why is peptide info so confusing?</a></p></article>''',schema)
chips='<button type="button" class="chip" aria-pressed="true" data-f="all">All</button>'+"".join(f'<button type="button" class="chip" aria-pressed="false" data-f="{c}">{icon(c)}{l}</button>' for c,l in CATS.items())
FILTERJS='<script>(function(){var b=document.querySelectorAll(".chip");b.forEach(function(x){x.addEventListener("click",function(){var f=x.dataset.f;b.forEach(function(y){y.setAttribute("aria-pressed",y===x)});document.querySelectorAll("[data-cat]").forEach(function(e){e.hidden=!(f==="all"||e.dataset.cat===f)})})})})();</script>'
names=", ".join(v[0].split(" (")[0] for v in PEP.values())
pages["peptides/index.html"]=("Peptide guides: semaglutide, tirzepatide, retatrutide, BPC-157 & more compared | Peptide Plainly",f"Compare popular peptides side by side: what each is for, FDA status, and how it's taken. Plain-English guides to {names}.",f'''<section class="wide"><p class="crumbs"><a href="../index.html">Home</a> / Peptide guides</p><h1>Find your peptide</h1><p class="lead">Weight loss, recovery, skin, growth hormone, longevity, focus: what each one does and how it's taken. Green means FDA-approved. Purple means research purposes only. Tap a category to filter.</p></section>{glp1_spot("")}<section class="wide">
<div class="chips" role="group" aria-label="Filter by category">{chips}</div>
<div class="table-wrap"><table class="compare"><caption class="sr">Peptide comparison table</caption><thead><tr><th scope="col">Peptide</th><th scope="col">What it's for</th><th scope="col">Status (U.S.)</th><th scope="col">How it's taken</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Guides</h2><div class="cards">{gcards}</div></section>{DISC}{FILTERJS}''',[ORG,{"@type":"CollectionPage","name":"Peptide guides","url":BASE+"/peptides/","publisher":{"@id":BASE+"/#org"},"hasPart":[{"@type":"MedicalWebPage","name":X[s]["h1"],"url":f"{BASE}/peptides/{s}.html"} for s in PEP]}])
pages["why-peptide-info-is-confusing.html"]=("Why is peptide info so confusing? A calm explainer | Peptide Plainly","Why do peptide videos and websites disagree so much? A friendly explainer on where conflicting peptide advice comes from and how to find clear answers.",f'''<article class="issue"><p class="eyebrow">Start here</p><h1>Why is peptide info so confusing?</h1>
<p class="lead">If you've watched three videos and heard three different answers, you're not alone, and it isn't your fault. Here's why it happens, and how to cut through it.</p>
<h2>1. "Peptide" covers very different things</h2><p>FDA-approved prescription drugs, skincare ingredients, food supplements, and <span class="badge research">Research purposes only</span> compounds all get called "peptides." Advice that fits one doesn't fit another. Our <a href="peptides/index.html">guides</a> label each one clearly.</p>
<h2>2. Animal results get presented as human results</h2><p>Many claims come from rat or mouse studies. These matter for science, but they often don't hold up in people. We always tell you which kind of study a claim comes from.</p>
<h2>3. Dose numbers get copied without sources</h2><p>For approved drugs, the official dose schedule is on the FDA label, and we link it. For research-only peptides there is no established human dose, so numbers online usually trace back to animal studies or personal anecdotes.</p>
<h2>4. Money shapes the message</h2><p>Some "educators" also sell products or earn affiliate commissions. That doesn't make them wrong, but it's worth knowing.</p>
<h2>5. The science really is still moving</h2><p>Regulations and evidence change, and in 2026 they changed for several peptides. We date-stamp our pages and link official sources.</p>
<h2>How to get clear answers</h2><ul><li>Start with our <a href="peptides-101.html">Peptides 101</a> guide.</li><li>Check the "Why people are excited" box and the source link on every claim.</li><li>Bring your questions to a clinician you trust.</li><li>Get the <a href="https://peptideplainly.beehiiv.com/subscribe" data-goatcounter-click="signup-cta">free Friday newsletter</a> for new research, explained plainly.</li></ul>{DISC}</article>''',[ORG,{"@type":"Article","headline":"Why is peptide info so confusing?","url":BASE+"/why-peptide-info-is-confusing.html","datePublished":"2026-10-16","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}}])
pages["index.html"]=("Peptide Plainly: peptides explained plainly | retatrutide, tirzepatide, BPC-157 & more","The real results behind today's hottest peptides, from weight loss to recovery, skin and longevity. Sourced, plain-English guides plus a free weekly email.",f'''
<section class="hero"><div class="hero-txt"><p class="kicker">Peptides, plainly. No BS.</p>
<h1>Lose the weight. Heal faster. Glow up. <span class="hl">Know what actually works.</span></h1>
<p class="lead">Retatrutide, tirzepatide, BPC-157, GHK-Cu and more: the real results from the real studies, explained in plain English. Whether you're new, in the gym, or chasing longevity, start here.</p>
<div class="hero-cta"><a class="btn" href="peptides/index.html">Find your peptide</a><a class="btn ghost" href="#signup">Get the Friday email</a></div></div>
<div class="hero-art" aria-hidden="true"><svg viewBox="0 0 320 260" width="320" height="260"><g stroke="#1b1f24" stroke-width="3"><line x1="60" y1="70" x2="140" y2="110"/><line x1="140" y1="110" x2="110" y2="190"/><line x1="140" y1="110" x2="230" y2="80"/><line x1="230" y1="80" x2="260" y2="170"/><line x1="110" y1="190" x2="200" y2="215"/><line x1="200" y1="215" x2="260" y2="170"/></g><circle cx="60" cy="70" r="26" fill="#0f766e"/><circle cx="140" cy="110" r="30" fill="#e8b04b"/><circle cx="230" cy="80" r="22" fill="#c2410c"/><circle cx="110" cy="190" r="22" fill="#f3d9c4"/><circle cx="260" cy="170" r="28" fill="#0f766e"/><circle cx="200" cy="215" r="18" fill="#1b1f24"/><text x="140" y="117" text-anchor="middle" font-family="Fraunces,serif" font-weight="800" font-size="20" fill="#1b1f24">?</text></svg></div></section>
{glp1_spot("peptides/")}
<section class="rules" aria-label="How we work"><div><span class="rule-n">01</span><h3>Real results</h3><p>The biggest numbers from the actual trials, front and center.</p></div><div><span class="rule-n">02</span><h3>Every goal covered</h3><p>Weight loss, recovery, skin, growth hormone, longevity, focus.</p></div><div><span class="rule-n">03</span><h3>Sourced, so you can trust it</h3><p>Every claim links to the study or FDA label behind it.</p></div></section>
<section class="wide"><div class="sec-head"><h2>The hottest peptides right now</h2><a href="peptides/index.html">Compare all {len(PEP)} →</a></div><div class="cards">{HOMECARDS}</div></section>
<section class="wide two"><a class="tile" href="why-peptide-info-is-confusing.html"><h3>Tired of conflicting videos?</h3><p>Why advice clashes, and how to find the answer fast.</p></a><a class="tile" href="peptides-101.html"><h3>New here? Peptides 101</h3><p>Everything a beginner needs, in five minutes.</p></a><a class="tile" href="glossary.html"><h3>Glossary</h3><p>RCT, meta-analysis, placebo and the rest, in plain English.</p></a></section>
<section id="this-week"><h2>This week's issue</h2>
{HOME_ISSUE}</section>{DISC}''')
from urllib.parse import quote as _q
ADV_EMAIL="teganjmcnealy@gmail.com"
ADV_BODY="Hi Peptide Plainly team,\n\nBrand:\nWebsite:\nProduct to promote:\nPlacement interest (site, newsletter, or both):\nPreferred dates:\n\nThanks!"
ADV_MAILTO=f"mailto:{ADV_EMAIL}?subject={_q('Sponsoring Peptide Plainly')}&amp;body={_q(ADV_BODY)}"
ADV_FAQ=[("Are sponsored placements labeled?","Always. Every sponsored spot on the site and in the newsletter is clearly labeled \"Sponsored\"."),
 ("Can sponsors influence what the guides say?","No. Sponsors get a placement, never a say in our guides or newsletter coverage. That independence is why readers trust us, and why a spot here is worth having."),
 ("How long do placements run?","It's flexible. Tell us the dates you have in mind and we'll work out a run that fits."),
 ("How does payment work?","We confirm the details with you, then send an invoice through Stripe. Your placement is scheduled once payment is in.")]
pages["advertise.html"]=("Advertise with Peptide Plainly: sponsor guides & newsletter","Put your brand in front of curious peptide beginners. Sponsor Peptide Plainly's guides or Friday newsletter. Lab-tested vendors only, always disclosed.",f'''<article class="issue"><p class="eyebrow">Advertise</p><h1>Sponsor Peptide Plainly</h1>
<p class="lead">Peptides, plainly. No BS. People come here to finally get what all the peptide hype is about, and they stick around because we make it exciting and easy. Want your brand in that moment? Let's talk.</p>
<p><a class="btn" href="{ADV_MAILTO}" data-goatcounter-click="advertise-contact-top">Sponsor us</a></p>
<h2>Who reads Peptide Plainly</h2><ul><li><strong>Peptide beginners</strong> who just heard about retatrutide, BPC-157 or GHK-Cu and want the real story, fast.</li><li><strong>A broad, curious audience</strong> into weight loss, recovery, skin and longevity who want plain-English, hype-forward guides instead of jargon.</li><li><strong>Newsletter subscribers</strong> who opted in to hear about new peptide research every Friday.</li></ul><p>Audience stats are available on request.</p>
<h2>What we publish</h2><ul><li><a href="peptides/index.html">{len(PEP)} in-depth peptide guides</a>, from semaglutide and tirzepatide to BPC-157, TB-500, GHK-Cu and more.</li><li><a href="peptides-101.html">Peptides 101</a>, our start-here guide for total beginners.</li><li>A <a href="glossary.html">plain-English glossary</a> of peptide terms.</li><li>A free newsletter: the week's biggest peptide news in five minutes, every Friday.</li></ul>
<h2>Available placements</h2><div class="cards"><div class="tile"><h3>Sponsored slot on the site</h3><p>Your brand featured on guide pages and the home page, clearly labeled "Sponsored".</p></div><div class="tile"><h3>Newsletter sponsorship</h3><p>A spot in our Friday email, clearly labeled "Sponsored".</p></div></div>
<h2>How sponsoring works</h2><ol><li><strong>Email us</strong> with your brand and what you'd like to promote.</li><li><strong>We send audience stats and options</strong> so you can pick the placements and dates that fit.</li><li><strong>You send your assets:</strong> logo, short copy and link.</li><li><strong>We confirm and invoice</strong> through Stripe.</li><li><strong>You go live</strong>, clearly labeled "Sponsored".</li><li><strong>You get a recap</strong> when your placement ends.</li></ol>
<h2>What we need from you</h2><ul><li>Your logo</li><li>Short copy (a line or two about your product)</li><li>The link you want readers to visit</li><li>Preferred dates</li><li>Preferred placements: site, newsletter, or both</li></ul>
<h2>Who's a fit</h2><p>We only work with lab-tested vendors, and we disclose every partnership. That includes research-purposes-only suppliers, as long as your products come with independent third-party lab testing. If that's you, we'd love to hear from you. Sponsored placements are always labeled, and sponsors never change what our guides say. That trust is exactly why readers listen.</p>
<h2>Sponsor FAQ</h2>{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in ADV_FAQ)}
<h2>Let's build something</h2><p>Tell us about your brand and what you'd like to promote. We'll send audience stats and placement details.</p>
<p><a class="btn" href="{ADV_MAILTO}" data-goatcounter-click="advertise-contact-bottom">Email us about sponsoring</a></p>
<p class="fine">Email not opening? Write to us at <strong>{ADV_EMAIL}</strong> with the subject "Sponsoring Peptide Plainly".</p></article>''',[ORG,{"@type":"WebPage","name":"Advertise with Peptide Plainly","url":BASE+"/advertise.html","description":"Sponsor Peptide Plainly's peptide guides and Friday newsletter.","publisher":{"@id":BASE+"/#org"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in ADV_FAQ]}])
import glp1cmp
import seo; seo.TITLE_FIX.update(TITLES3); seo.apply(pages,BASE,ORG,G)
import newpages; newpages.add(pages,BASE,ORG,DISC,NOTE,X); newpages.link_in(pages); newpages.link_guides(pages,PEP)
t,d,b=pages["index.html"]
pages["index.html"]=(t,d,b,[ORG,{"@type":"WebSite","name":"Peptide Plainly","url":BASE+"/","description":d,"publisher":{"@id":BASE+"/#org"}}])
import glp1cmp; pages["glp1-comparison.html"]=glp1cmp.build(BASE,ORG,DISC)
# "Compare all four GLP-1s" button: rendered only if Bean's comparison page exists at build time
# (a pages["glp1-comparison.html"] entry in the generator, or a glp1-comparison.html file in the repo root).
import newpages2; newpages2.add(pages,BASE,ORG,DISC,NOTE,X,glp1cmp.ROWS); newpages2.wire(pages)
# Above-the-fold signup strip: FALLBACK picks (no GoatCounter API token on the box, Oct 17 2026): home + the two GLP-1 bread-winners
ATF_SIGNUP=[("index.html","home"),("peptides/semaglutide.html","semaglutide"),("peptides/retatrutide.html","retatrutide")]
newpages2.signup_atf(pages,ATF_SIGNUP)
import newpages3; newpages3.add(pages,BASE,ORG,DISC); newpages3.wire(pages)
import extras3; extras3.wire3(pages)
seo.check(pages)
# ---- OG cards: manifest for scripts/og.py; wire og:image only where the PNG exists ----
CARDS={}
for _s in PEP:
    _bk,_bt=X[_s]["badge"]; CARDS[f"peptides/{_s}.html"]=dict(card=_s,kicker=CATS[META[_s][0]],title=PEP[_s][0],sub=EXCITE[_s][2],badge=_bk,badge_t=_bt,hot=_s=="retatrutide")
CARDS["glp1-comparison.html"]=dict(card="glp1-comparison",kicker="Spotlight · weight loss",title="Semaglutide vs tirzepatide vs retatrutide vs orforglipron",sub="The big four GLP-1s, side by side.",badge="",badge_t="",hot=False)
CARDS.update(newpages.CARDS); CARDS.update(newpages2.CARDS); CARDS.update(newpages3.CARDS)
(P/"og").mkdir(exist_ok=True); (P/"og"/"cards.json").write_text(json.dumps(CARDS,ensure_ascii=False,indent=1))
for _p,_c in CARDS.items():
    if (P/"og"/f"{_c['card']}.png").exists(): OG_IMG[_p]=f"og/{_c['card']}.png"
HAS_GLP1CMP="glp1-comparison.html" in pages or (P/"glp1-comparison.html").exists()
import re as _re
def _cmp(m): return f'<p class="glp1-cta"><a class="btn" href="{"../" if m.group(1)=="" else ""}glp1-comparison.html" data-goatcounter-click="glp1-compare">Compare all four GLP-1s →</a></p>' if HAS_GLP1CMP else ""
for path,v in pages.items():
    (P/path).parent.mkdir(exist_ok=True); (P/path).write_text(_re.sub(r'<!--GLP1CMP:([^>]*)-->',_cmp,page(path,*v)))
import datetime;LASTMOD=datetime.date.today().isoformat()
(P/"404.html").write_text(page("404.html","Page not found | Peptide Plainly","That page doesn't exist, but the peptide guides do. Find your peptide or get the free Friday newsletter.",f'''<article class="issue"><p class="eyebrow">404</p><h1>That page took a rest day.</h1>
<p class="lead">Peptides, plainly. No BS. This link doesn't go anywhere, but everything good is one click away.</p>
<div class="hero-cta"><a class="btn" href="/peptides/">Browse all {len(PEP)} peptide guides</a><a class="btn ghost" href="#signup">Get the Friday email</a></div>
<h2>Popular guides</h2><ul>{"".join(f'<li><a href="/peptides/{s}.html">{PEP[s][0]}</a></li>' for s in list(PEP)[:6])}</ul>
<h2>Or start here</h2><ul><li><a href="/peptides-101.html">Peptides 101</a>, everything a beginner needs in five minutes</li><li><a href="/glossary.html">Glossary</a></li><li><a href="/newsletter.html">This week&#39;s issue</a></li><li><a href="/">Home</a></li></ul></article>''',root="/",robots="noindex"))
# Every sent issue URL is a tiny noindex redirect stub to /newsletter.html (so old links never 404).
# Issue HTML for unsent or deleted .md files is removed so nothing goes live early.
_stub='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Peptide Plainly newsletter</title><meta name="robots" content="noindex"><link rel="canonical" href="'+BASE+'/newsletter.html"><meta http-equiv="refresh" content="0; url=../newsletter.html"></head><body><p>This issue has moved. <a href="../newsletter.html">Read this week&#39;s issue</a>.</p></body></html>\n'
_sent={i["stem"] for i in SENT}
for h in (P/"issues").glob("issue-*.html"):
    if h.stem not in _sent: h.unlink()
for st in _sent: (P/"issues"/f"{st}.html").write_text(_stub)
(P/newpages.OLD_CALC).write_text(newpages.OLD_CALC_HTML)
urls=list(pages)+["about.html"]
(P/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>{LASTMOD}</lastmod></url>\n".replace("/index.html","/") for u in urls)+"</urlset>\n")
# IndexNow key file (served at /<key>.txt). Ping with: python3 scripts/indexnow.py  (needs Tegan OK)
INDEXNOW_KEY="9a85cb3b2d8f745f25610a7da0dbad98"
(P/f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
(P/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
ab=(P/"about_body.html").read_text()
(P/"about.html").write_text(page("about.html","About Peptide Plainly & medical disclaimer","About Peptide Plainly: how we summarize peptide research from PubMed, plus our full medical disclaimer.",ab,seo.about_schema(BASE,ORG)))

LL=["# Peptide Plainly","","> Friendly, plain-English explanations of peptide research, plus a free newsletter every Friday. Every claim links to PubMed or official FDA/WADA sources. Education only, not medical advice. We never give doses for research-only peptides; for FDA-approved drugs we summarize the official label and note that the prescriber sets the dose.","","## Start here",f"- [Peptides 101]({BASE}/peptides-101.html): what peptides are, approved vs research-only, reading studies",f"- [Why is peptide info so confusing?]({BASE}/why-peptide-info-is-confusing.html)",f"- [Glossary]({BASE}/glossary.html)","","## Peptide guides (why people are excited, quick facts, dosing & timing, evidence, FAQ)"]
LL[LL.index("## Start here"):LL.index("## Start here")]=["## Featured: the GLP-1 weight-loss guides","Our most popular guides. Retatrutide is the hottest one right now."]+[f"- [{glp1cmp.TITLE}]({BASE}/glp1-comparison.html): {glp1cmp.DESC}"]+[f"- [{GLP1_TITLE[s]}]({BASE}/peptides/{s}.html): {X[s]['badge'][1]}. {PEP[s][1]}" for s in GLP1]+[""]
for slug,(name,desc,*_) in PEP.items(): LL.append(f"- [{X[slug]['h1']}]({BASE}/peptides/{slug}.html): {X[slug]['badge'][1]}. {desc}")
LL+=["","## Tools & buyer guides"]+[f"- [{t}]({BASE}/{u}): {d}" for t,u,d in newpages.LLMS+newpages2.LLMS+newpages3.LLMS]
LL+=["","## Newsletter (free, every Friday)"]+([f"- [This week's issue]({BASE}/newsletter.html): Issue #{CUR['n']}, {CUR['date']}"] if CUR else [])+["- Subscribe: https://peptideplainly.beehiiv.com/subscribe","",f"## About\n- [About & medical disclaimer]({BASE}/about.html)",f"- [Advertise with us]({BASE}/advertise.html): sponsor the guides or the Friday newsletter (lab-tested vendors only, always labeled Sponsored)"]
(P/"llms.txt").write_text("\n".join(LL)+"\n")
