"""Side-effects/tolerability table for semaglutide-vs-tirzepatide (trial data only)."""
import json
def pm(i,label): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{i}/" rel="noopener">{label}</a>'
def ct(n,label): return f'<a href="https://clinicaltrials.gov/study/{n}?tab=results" rel="noopener">{label}</a>'
LILLY_S5="https://www.prnewswire.com/news-releases/zepbound-tirzepatide-showed-superior-weight-loss-over-wegovy-semaglutide-in-complete-surmount-5-results-published-in-the-new-england-journal-of-medicine-302451241.html"
BC="https://www2.gov.bc.ca/assets/gov/health/health-drug-coverage/pharmacare/newsletters/pad_refill_nov_2025_tirz_vs_sema_weight_loss.pdf"
# (numAffected, numAtRisk) from ClinicalTrials.gov posted results, "other" adverse events table
CT={
"s5_tirz":dict(n=374,nausea=163,diarrhea=88,vomiting=56,constipation=101),
"s5_sema":dict(n=376,nausea=167,diarrhea=88,vomiting=80,constipation=107),
"step1_sema":dict(n=1306,nausea=576,diarrhea=411,vomiting=321,constipation=305),
"step1_pbo":dict(n=655,nausea=114,diarrhea=104,vomiting=43,constipation=62),
"sm1_5":dict(n=630,nausea=160,diarrhea=128,vomiting=58,constipation=113),
"sm1_10":dict(n=636,nausea=217,diarrhea=143,vomiting=74,constipation=117),
"sm1_15":dict(n=630,nausea=201,diarrhea=149,vomiting=81,constipation=80),
"sm1_pbo":dict(n=643,nausea=63,diarrhea=51,vomiting=12,constipation=38),
}
def p(k,e): d=CT[k]; return f"{100*d[e]/d['n']:.1f}%"
S5=ct("NCT05822830","SURMOUNT-5 results, ClinicalTrials.gov")
ST1=ct("NCT03548935","STEP 1 results, ClinicalTrials.gov")
SM1=ct("NCT04184622","SURMOUNT-1 results, ClinicalTrials.gov")
ROWS=[
("SURMOUNT-5 · tirzepatide (10 or 15 mg)","s5_tirz",f'6.1% (<a href="{LILLY_S5}" rel="noopener">Lilly</a>); 2.7% for GI events (<a href="{BC}" rel="noopener">BC PharmaCare</a>)'),
("SURMOUNT-5 · semaglutide (1.7 or 2.4 mg)","s5_sema",f'8.0% (<a href="{LILLY_S5}" rel="noopener">Lilly</a>); 5.6% for GI events (<a href="{BC}" rel="noopener">BC PharmaCare</a>)'),
("STEP 1 · semaglutide 2.4 mg","step1_sema",f'4.5% for GI events ({pm(33567185,"NEJM 2021")})'),
("STEP 1 · placebo","step1_pbo",f'0.8% for GI events ({pm(33567185,"NEJM 2021")})'),
("SURMOUNT-1 · tirzepatide 5 mg","sm1_5",f'4.3% ({pm(35658024,"NEJM 2022")})'),
("SURMOUNT-1 · tirzepatide 10 mg","sm1_10",f'7.1% ({pm(35658024,"NEJM 2022")})'),
("SURMOUNT-1 · tirzepatide 15 mg","sm1_15",f'6.2% ({pm(35658024,"NEJM 2022")})'),
("SURMOUNT-1 · placebo","sm1_pbo",f'2.6% ({pm(35658024,"NEJM 2022")})'),
]
def section():
    tr="".join(f'<tr><th scope="row">{a}</th><td>{p(k,"nausea")}</td><td>{p(k,"diarrhea")}</td><td>{p(k,"vomiting")}</td><td>{p(k,"constipation")}</td><td>{d}</td></tr>' for a,k,d in ROWS)
    return f'''<h2 id="side-effects">Side effects compared: what the trials recorded</h2>
<p>Stomach side effects are the big one for both drugs, and in SURMOUNT-5 nausea was almost identical (43.6% vs 44.4%). Fewer people stopped tirzepatide for side effects than semaglutide (6.1% vs 8.0%), though Lilly notes the trial wasn't powered to compare safety. Only SURMOUNT-5 is head-to-head; STEP 1 and SURMOUNT-1 were separate placebo-controlled trials, so compare those rows loosely.</p>
<div class="table-wrap"><table class="compare"><caption class="sr">GI side effects and stopping for side effects in SURMOUNT-5, STEP 1 and SURMOUNT-1</caption><thead><tr><th scope="col">Trial · arm</th><th scope="col">Nausea</th><th scope="col">Diarrhea</th><th scope="col">Vomiting</th><th scope="col">Constipation</th><th scope="col">Stopped for side effects</th></tr></thead><tbody>{tr}</tbody></table></div>
<p class="fine">Nausea, diarrhea, vomiting and constipation are the share of each arm reporting the event, from the posted trial results ({S5}, weeks 0–72; {ST1}, weeks 0–75; {SM1}, which covers up to week 193 including the extension). "Stopped for side effects" is the share who discontinued treatment because of adverse events (or GI events, where noted), from the sources linked in each cell. Most GI events were mild to moderate and happened during dose escalation.</p>'''
