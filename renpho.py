# Nov 3 2026: RENPHO affiliate placement (Impact program 8013132). Tracking-only framing; no health claims.
PAGES=["peptides/semaglutide.html","peptides/tirzepatide.html","peptides/retatrutide.html","peptides/orforglipron.html","glp1-comparison.html","semaglutide-vs-tirzepatide.html"]
PRODUCTS=[("morphoscan","MorphoScan Nova","smart body composition scale","https://renpho.sjv.io/DW6yeb","renpho-morphoscan-nova.webp"),
          ("tape","Smart Tape Measure+","smart tape measure","https://renpho.sjv.io/QY9jn6","renpho-smart-tape.webp")]
DEFAULT="https://renpho.sjv.io/R0rGbv"
def block(slug,root):
    items="".join(f'<li><img src="{root}img/aff/{img}" alt="RENPHO {n}" width="64" height="64" loading="lazy" decoding="async">'
        f'<span><strong>{n}</strong><br><span class="aff-what">{what}</span></span>'
        f'<a class="btn aff-btn" href="{u}" rel="sponsored noopener" target="_blank" data-goatcounter-click="affiliate-renpho-{k}-{slug}">View</a></li>' for k,n,what,u,img in PRODUCTS)
    return (f'<aside class="affiliate" aria-label="Affiliate"><p class="sponsor-tag">Affiliate</p>'
        f'<p class="aff-body"><strong>RENPHO</strong>: tools for tracking weight, body composition and measurements over time.</p>'
        f'<ul class="aff-list">{items}</ul>'
        f'<p class="aff-more"><a href="{DEFAULT}" rel="sponsored noopener" target="_blank" data-goatcounter-click="affiliate-renpho-default-{slug}">See all RENPHO products</a></p>'
        f'<p class="sponsor-disc">Affiliate links: we earn a commission if you buy through these links, at no extra cost to you. Tracking tools only; not a substitute for your clinician.</p></aside>')
def apply(pages):
    D='<p class="disclaimer">'; done=[]
    for k in PAGES:
        if k not in pages: continue
        v=list(pages[k])
        if D not in v[2]: continue
        slug=k.split("/")[-1][:-5]; root="../" if "/" in k else ""
        i=v[2].rindex(D); v[2]=v[2][:i]+block(slug,root)+v[2][i:]; pages[k]=tuple(v); done.append(k)
    return done
