"""Advertise page packages. Founding rates lead; regular-price links render as a small 'Pay regular rate' link under each card."""
# Regular-price Stripe links (small 'Pay regular rate' link under each card):
REGULAR_LINKS={
 "newsletter-feature":("$150","https://buy.stripe.com/cNifZg5jqgmH0CI4EAafS00"),
 "newsletter-month":("$500","https://buy.stripe.com/3cI7sKh28dav99e7QMafS02"),
 "site-sponsor":("$250/mo","https://buy.stripe.com/7sYcN47ry6M7gBGgniafS04"),
 "founding-partner-bundle":("$700/mo","https://buy.stripe.com/5kQ7sK9zG3zVgBG0okafS06"),
}
BANNER="Founding rates: first 5 sponsors, through Dec 31, 2026"
CALC="peptide-reconstitution-calculator.html"
PACKAGES=[
 ("newsletter-feature","Newsletter Feature","$99","$150",None,
  ["One Friday issue","Sole sponsor of that issue","Your logo","~75 words of copy","One link","Click report"],
  "https://buy.stripe.com/3cI3cu8vCb2ngBG6MIafS01"),
 ("newsletter-month","Newsletter Month","$349","$500",None,
  ["4 Friday issues in a row","Plus a recap"],
  "https://buy.stripe.com/00w28q27eb2n4SY8UQafS03"),
 ("site-sponsor","Site Sponsor","$175/mo","$250/mo",None,
  [f'A labeled "Sponsored" card on the <a href="{CALC}">peptide reconstitution calculator</a>',
   'The same card on the GLP-1 guide pages (<a href="peptides/semaglutide.html">semaglutide</a>, <a href="peptides/tirzepatide.html">tirzepatide</a>, <a href="peptides/retatrutide.html">retatrutide</a>, <a href="peptides/orforglipron.html">orforglipron</a>)',
   "Runs for 30 days"],
  "https://buy.stripe.com/8x2bJ0dPW0nJ2KQ2wsafS05"),
 ("founding-partner-bundle","Founding Partner Bundle","$499/mo","$700/mo","for the first 3 months, then $700/mo",
  ["Newsletter Month","Site Sponsor","A founding-sponsor mention","Best value"],
  "https://buy.stripe.com/14AdR88vC9Yjadic72afS07"),
]
def cards():
    out=[]
    for slug,name,price,reg,note,items,url in PACKAGES:
        li="".join(f"<li>{x}</li>" for x in items)
        n=f'<p class="pkg-note">{note}</p>' if note else '<p class="pkg-note">Founding rate</p>'
        feat=' pkg-feat' if slug=="founding-partner-bundle" else ''
        out.append(f'<div class="pkg{feat}" id="{slug}"><h3>{name}</h3><p class="pkg-price"><strong>{price}</strong> <s aria-label="regular price {reg}">{reg}</s></p>{n}<ul>{li}</ul>'
                   f'<a class="btn pkg-btn" href="{url}" rel="noopener" data-goatcounter-click="book-{slug}">Book this slot</a>'
                   f'<p class="pkg-reg"><a href="{REGULAR_LINKS[slug][1]}" rel="noopener" data-goatcounter-click="book-{slug}-regular">Pay regular rate ({REGULAR_LINKS[slug][0]})</a></p></div>')
    return f'<p class="pkg-banner" role="note">🎉 {BANNER}</p><div class="pkgs">{"".join(out)}</div>'
TERMS=["Sponsor content is always labeled \"Sponsored\".","Sponsors get no editorial control over our guides or newsletter coverage.","No dosing claims in sponsor copy, and nothing that encourages human use of research-only compounds.","We review your copy before anything goes live.","We confirm your booking within 1 business day of payment."]
def terms(): return '<h2 id="terms">Sponsor terms</h2><ul class="terms">'+"".join(f"<li>{t}</li>" for t in TERMS)+'</ul>'
STEPS=[("Pick a package","from the cards above."),("Pay","securely through Stripe with the Book this slot button."),("Send your assets:","logo, copy and link, by email."),("We review","your copy against our terms."),("It goes live,","clearly labeled \"Sponsored\"."),("You get a report","with your clicks.")]
def steps(): return '<h2>How booking works</h2><ol>'+"".join(f"<li><strong>{a}</strong> {b}</li>" for a,b in STEPS)+'</ol>'
CSS=""".pkg-banner{background:var(--sun);color:var(--ink);border:2px solid var(--ink);border-radius:12px;padding:10px 14px;font-weight:700;margin:1em 0}
.pkgs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:16px;margin:1em 0 1.5em}
.pkg{background:var(--card);border:2px solid var(--ink);border-radius:var(--r);padding:18px;display:flex;flex-direction:column;min-width:0}
.pkg-feat{box-shadow:5px 5px 0 var(--sun)}
.pkg h3{margin:0 0 .3em}.pkg-price{margin:0;font-size:1.5rem}.pkg-price s{color:var(--muted);font-size:1rem;margin-left:.3em}
.pkg-note{margin:.2em 0 .6em;color:var(--muted);font-size:.9rem}.pkg ul{padding-left:1.2em;margin:0 0 1em;flex:1}.pkg li{margin:.3em 0;overflow-wrap:anywhere}
.pkg .pkg-btn{text-align:center;align-self:stretch}
.pkg-reg{margin:.6em 0 0;text-align:center;font-size:.85rem}.pkg-reg a{color:var(--muted)}
"""
