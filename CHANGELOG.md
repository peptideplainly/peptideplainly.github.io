# Changelog

## 2026-10-18 — Bean verified fact fixes
- Advertise: small "Pay regular rate" link under each package (contact email unchanged).
- Stack rat-study wording; KPV "lab-grown human gut cells"; kisspeptin hero (secondary result, IV kisspeptin-54) + kisspeptin-10 FDA safety-risk listing and Oct 2024 11–0 advisory vote; Epitalon cell/mouse details; CagriSema compounding links, 2,108-on-CagriSema count, dosage note; MT2 melanoma FAQ wording.
- July 2026 vote now cites the FDA meeting page alongside the vote report; Selank 2014 citation notes design details not reported in English.

## 2026-10-18 — Batch 3b: sitewide pages
- About rewritten (live guide count, sponsor policy, one short disclaimer). Peptides 101: bold H1, lighter intro and research-only copy with a legit-source link.
- Calculator callouts now describe the general reconstitution calculator. Tesamorelin badge: "FDA-approved (as Egrifta)".
- Advertise packages/terms, signup and share blocks, and Katz wording untouched.

## 2026-10-18 — Batch 3a: sitewide tone pass on guides
- Bold H1s on all older guides; general-audience framing for tesamorelin, PT-141, Semax (indication kept as one short line, trial populations named).
- Research-only guides (BPC-157, TB-500, MOTS-c, Semax, CJC-1295/ipamorelin, injectable GHK-Cu): one sourced risk line + "Choose a tested source"; short no-dose section; regulatory paragraphs trimmed.
- One short disclaimer per page (footer), duplicate research note removed; label-dosing preamble shortened.

## 2026-10-18 — Bean tone pass on batch 2 + MT2
- Safety/legal boxes replaced with one sourced line + "Choose a tested source" link (MT2 keeps its risk citations inline).
- Bolder H1s; shorter status paragraphs (regulatory detail trimmed); duplicate research footer note dropped on these pages.

## 2026-10-18 — Advertise page: bookable packages
- 4 founding-rate package cards with Stripe "Book this slot" buttons (GoatCounter book-<slug>), struck-through regular prices, founding banner.
- Sponsor terms section; 6-step book-and-pay flow; tightened vendor welcome. Regular-price Stripe links kept in advertise.py (not rendered). No sponsor placements built.

## 2026-10-18 — Batch 2 guides
- New guides: Epitalon, Selank, KPV, Kisspeptin, Cagrilintide & CagriSema, SS-31 (elamipretide, Forzinity), BPC-157 + TB-500 stack.
- FDA status confirmed: elamipretide approved as Forzinity (NDA 215244, Sept 19, 2025, accelerated approval, Barth syndrome ≥30 kg; label dosing copied). CagriSema investigational (NDA submitted Dec 18, 2025). Others: no FDA approval in Drugs@FDA.
- Safety & legal box + legit-source link on every research-only page. No human doses for research-only compounds.
- OG cards for all 7.

## 2026-10-18 (Bean's batch 1 fact fixes)
- MT2: single-case melanoma wording; Scenesse approval cited to FDA approval letter (Oct 8, 2019); appetite bullet/FAQ narrowed (one small trial, one mouse study, injected into the brain); tiny-pilot tanning FAQ; PMID 28266027 for not-approved; "label doses" footer line removed on research-only pages.
- Old calculator URL: meta refresh + JS location.replace + canonical (kept permanently; pinned X post).
- Home calculator tile blurb; retatrutide hero cites Lilly May 21, 2026 release; retatrutide badge now "Investigational: not approved; only available in Lilly clinical trials" (Lilly).

## 2026-10-18 (broad push, batch 1)
- New guide: /peptides/melanotan-2.html (Dorr 1996, Wessells 1998/2000, mouse appetite study 2022, case reports and reviews for risks; MHRA FOI; Scenesse label). Safety & legal box with legit-source link. No human dosing.
- Calculator generalized: /peptide-reconstitution-calculator.html (vial mg + water mL + amount in mcg/mg -> concentration, mL, U-100 units; math only, no presets). Old /glp1-units-calculator.html is a meta-refresh + canonical redirect stub (not in sitemap). Linked from every guide's Keep going block; share block kept.
- Home: retatrutide hero card (TRIUMPH-1 −25.0%, treatment-regimen; investigational, Lilly plans FDA submission Q1 2027).

## 2026-10-18 (traffic push 3)
- semaglutide-vs-tirzepatide.html: new "Where does retatrutide fit?" section (phase 2 NEJM 2023, TRIUMPH-1 NEJM, TRIUMPH-2 Lancet; estimand labelled per trial; not head-to-head; investigational, Lilly plans FDA submission Q1 2027). Title/description/JSON-LD/OG card now cover all three.
- New: /compounded-vs-brand-semaglutide-tirzepatide.html (FDA compounding Q&A, FDA GLP-1 concerns page, FDA dosing-errors alert, NDC Directory, DailyMed packaging; Katz et al., Obes Sci Pract 2026 photo-review study). Linked from semaglutide and tirzepatide guides and the calculator.

## 2026-10-17 (traffic push 2)
- New: /semaglutide-vs-tirzepatide.html (SURMOUNT-5, STEP 1, SURMOUNT-1 from PubMed abstracts) and /peptides/retatrutide-fda-approval-status.html (TRIUMPH timeline from Lilly releases, ClinicalTrials.gov, NEJM/Lancet; FDA Oct 2 2026 classification letter).
- Calculator: share block (navigator.share + clipboard fallback, X and Reddit intents, GoatCounter events); calculator callouts on all GLP-1 pages and the home page.
- Above-the-fold signup strip on home, semaglutide, retatrutide. FALLBACK choice: no GoatCounter API token available, so no real traffic ranking was used.

## 2026-10-17 (traffic push)
- SEO: JSON-LD on Peptides 101 (Article, BreadcrumbList), Glossary (DefinedTermSet), About (AboutPage); all titles <=70 chars, all meta descriptions <=155 (enforced by seo.check at build).
- IndexNow: key file /9a85cb3b2d8f745f25610a7da0dbad98.txt; scripts/indexnow.py (POSTs sitemap URLs; --dry-run available). Not pinged yet, waiting on Tegan's OK.
- New pages: /peptides/retatrutide-side-effects.html (JAMA Netw Open, Oct 14 2026, doi:10.1001/jamanetworkopen.2026.38929), /glp1-units-calculator.html (math-only, U-100), /how-to-tell-if-a-peptide-source-is-legit.html.
- OG cards (og/*.png, rendered by scripts/og.py) for all 13 guides, GLP-1 comparison and the new pages; "Keep going" links on every guide.

## 2026-10-16 (welcoming redesign)
- Warmer, beginner-first tone; calm "Research purposes only" badges for non-FDA-approved peptides (BPC-157, TB-500, injectable GHK-Cu), plus "FDA-approved" and "Dietary supplement" badges.
- Every peptide page: Quick answer box, "Dosing & timing: what we actually know" section (FDA label schedules from DailyMed for Ozempic/Wegovy/Rybelsus/Mounjaro/Zepbound; no human doses for research-only peptides, with study routes, why numbers conflict, and clinician questions), FAQ.
- New page: Why is peptide info so confusing?
- schema.org JSON-LD (Organization, WebSite, Article, MedicalWebPage, FAQPage), llms.txt, answer-first headings, sitemap lastmod.

- Replaced all signup placeholders (home hero + signup banner on every page, incl. issues) with the Beehiiv embed form; added Beehiiv attribution script to every page; added a 'Subscribe' nav link and fallback link to https://peptideplainly.beehiiv.com/subscribe. Templates in make_site.py/build.py updated.
- Moved the site to the `peptideplainly` GitHub org (repo `peptideplainly/peptideplainly.github.io`), now live at https://peptideplainly.github.io/ (was https://teganjmcnealy.github.io/peptideplainly/).
- Updated canonical/Open Graph URLs, sitemap.xml and robots.txt to the new root URL.
- Verified regulatory claims against WADA 2026 Prohibited List, Drugs@FDA, FDA compounding and DSHEA/cosmetics pages; added official source links.
- Added Peptides 101, six peptide explainers, glossary, SEO tags.
- Launched v1: home page, about/disclaimer, Issue #1, weekly PubMed fetch script.

## 2026-10-16 — Redesign + 7 new guides
- New guides: retatrutide, orforglipron (Foundayo), tesamorelin (Egrifta), CJC-1295 & ipamorelin, MOTS-c, Semax, PT-141 (Vyleesi).
- Editorial redesign: Fraunces + Inter, warm paper palette, category SVG icons, summary box (since replaced by "Why people are excited"), compare table with filter chips, sticky nav.
- BreadcrumbList + CollectionPage schema; sitemap/llms.txt updated.

- Tone pass 2: benefit-led H1s, positive quick facts and FAQs, Peptides 101 'How to pick a quality source', new social preview image, removed legacy summary-box code.
