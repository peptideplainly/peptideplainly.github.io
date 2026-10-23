# Oct 23 2026: Dose Track affiliate placement (Sponsored)
COPY="Track your doses and schedule in one app. Code <strong>PEPTIDEPLAINLY</strong> gets a 14-day Pro trial."
def block(slug):
    u=f"https://dosetrack.app/peptideplainly?utm_source=peptideplainly&amp;utm_medium=affiliate&amp;utm_campaign={slug}"
    return (f'<aside class="sponsor" aria-label="Sponsored"><p class="sponsor-tag">Sponsored</p>'
            f'<p class="sponsor-body"><strong>Dose Track</strong>: {COPY} '
            f'<a href="{u}" rel="sponsored noopener" target="_blank" data-goatcounter-click="dosetrack-{slug}">Try Dose Track</a></p>'
            f'<p class="sponsor-disc">We earn a reward if you join.</p></aside>')
CSS='.sponsor{border:1px dashed var(--line);border-radius:12px;padding:10px 14px;margin:20px 0;background:var(--card);font-size:.92rem;overflow-wrap:anywhere}.sponsor p{margin:0}.sponsor-tag{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}.sponsor-body{margin:4px 0 2px!important}.sponsor-disc{font-size:.8rem;color:var(--muted)}'
def apply(pages,CALC):
    D='<p class="disclaimer">'
    done=[]
    for k in list(pages):
        if (k.startswith("peptides/") and k!="peptides/index.html") or k==CALC:
            v=list(pages[k])
            if D not in v[2]: continue
            slug=k.split("/")[-1][:-5]
            i=v[2].rindex(D); v[2]=v[2][:i]+block(slug)+v[2][i:]; pages[k]=tuple(v); done.append(k)
    return done
