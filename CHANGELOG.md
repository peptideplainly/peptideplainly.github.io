# Changelog

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
