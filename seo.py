"""SEO polish: short titles (<=70 chars), trimmed meta descriptions (<=155), JSON-LD for Peptides 101, Glossary, About."""
TITLE_FIX={
"index.html":"Peptide Plainly: retatrutide, tirzepatide, BPC-157 & more, explained",
"peptides/index.html":"Peptide guides: semaglutide, tirzepatide, retatrutide, BPC-157 & more",
"peptides/bpc-157.html":"BPC-157: benefits, research & what it's used for | Peptide Plainly",
"peptides/tb-500.html":"TB-500 (thymosin beta-4): benefits & research | Peptide Plainly",
"peptides/ghk-cu.html":"GHK-Cu copper peptide: skin benefits & research | Peptide Plainly",
"peptides/collagen-peptides.html":"Collagen peptides: skin results & how to take them | Peptide Plainly",
"peptides/tesamorelin.html":"Tesamorelin (Egrifta): belly-fat results, benefits & label dosing",
"peptides/cjc-1295-ipamorelin.html":"CJC-1295 & ipamorelin: GH stack benefits & research | Peptide Plainly",
"peptides/mots-c.html":"MOTS-c, the 'exercise' peptide: benefits & research | Peptide Plainly",
"peptides/pt-141.html":"PT-141 (bremelanotide, Vyleesi): results & how to take it",
"peptides/semax.html":"Semax nasal brain peptide: benefits & research | Peptide Plainly",
}
DESC_FIX={
"peptides/index.html":"Compare 13 popular peptides side by side: what each is for, FDA status and how it's taken. Semaglutide, tirzepatide, retatrutide, BPC-157 & more.",
"index.html":"The real results behind today's hottest peptides: weight loss, recovery, skin and longevity. Sourced, plain-English guides plus a free weekly email.",
"advertise.html":"Put your brand in front of curious peptide beginners. Sponsor Peptide Plainly's guides or Friday newsletter. Lab-tested vendors only, always disclosed.",
}
def crumbs(BASE,items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate([("Home",BASE+"/")]+items)]}
def apply(pages,BASE,ORG,G):
    for k,t in TITLE_FIX.items():
        v=list(pages[k]); v[0]=t; pages[k]=tuple(v)
    for k,d in DESC_FIX.items():
        v=list(pages[k]); v[1]=d; pages[k]=tuple(v)
    t,d,b=pages["peptides-101.html"][:3]; u=BASE+"/peptides-101.html"
    pages["peptides-101.html"]=(t,d,b,[ORG,{"@type":"Article","headline":"Peptides 101: a beginner's guide to peptides","description":d,"url":u,"inLanguage":"en","datePublished":"2026-10-16","dateModified":"2026-10-17","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},crumbs(BASE,[("Peptides 101",u)])])
    t,d,b=pages["glossary.html"][:3]; u=BASE+"/glossary.html"
    pages["glossary.html"]=(t,d,b,[ORG,{"@type":"DefinedTermSet","@id":u+"#terms","name":"Peptide research glossary","description":d,"url":u,"inLanguage":"en","publisher":{"@id":BASE+"/#org"},
        "hasDefinedTerm":[{"@type":"DefinedTerm","name":n,"description":x,"url":f"{u}#{n.split()[0].lower()}","inDefinedTermSet":u+"#terms"} for n,x in G]},crumbs(BASE,[("Glossary",u)])])
def about_schema(BASE,ORG):
    u=BASE+"/about.html"
    return [ORG,{"@type":"AboutPage","name":"About Peptide Plainly & medical disclaimer","url":u,"inLanguage":"en","about":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}},crumbs(BASE,[("About",u)])]
def check(pages):
    bad=[(k,len(v[0])) for k,v in pages.items() if len(v[0])>70]+[(k,len(v[1])) for k,v in pages.items() if len(v[1])>155]
    assert not bad, f"SEO length check failed: {bad}"
