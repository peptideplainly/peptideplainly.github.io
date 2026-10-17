# Changelog

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
