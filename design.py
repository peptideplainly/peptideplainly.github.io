"""Design pieces: icons, categories, per-guide meta (category, use, route, straight answer)."""
def svg(paths,label):
    return f'<svg class="ico" viewBox="0 0 48 48" width="48" height="48" role="img" aria-label="{label}" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">{paths}</svg>'
ICON={
"weight":('<path d="M10 14h28l-3 24H13z"/><path d="M18 14a6 6 0 0 1 12 0"/><path d="M24 22v6l4 3"/>',"Weight and metabolism icon"),
"recovery":('<rect x="6" y="18" width="36" height="12" rx="6" transform="rotate(-35 24 24)"/><circle cx="21" cy="22" r="1.2" fill="currentColor"/><circle cx="27" cy="26" r="1.2" fill="currentColor"/><circle cx="25" cy="21" r="1.2" fill="currentColor"/><circle cx="23" cy="27" r="1.2" fill="currentColor"/>',"Healing and recovery icon"),
"skin":('<path d="M24 6c6 9 11 15 11 22a11 11 0 0 1-22 0c0-7 5-13 11-22z"/><path d="M19 29a5 5 0 0 0 5 5"/>',"Skin icon"),
"gh":('<path d="M8 40h32"/><rect x="11" y="28" width="6" height="12"/><rect x="21" y="20" width="6" height="20"/><rect x="31" y="11" width="6" height="29"/>',"Growth hormone icon"),
"longevity":('<ellipse cx="24" cy="24" rx="17" ry="10"/><path d="M12 24c3-5 5 5 8 0s5 5 8 0 5 5 8 0"/>',"Mitochondria icon"),
"brain":('<path d="M20 10a6 6 0 0 0-10 5 6 6 0 0 0-2 10 6 6 0 0 0 5 9 6 6 0 0 0 7 4V10z"/><path d="M28 10a6 6 0 0 1 10 5 6 6 0 0 1 2 10 6 6 0 0 1-5 9 6 6 0 0 1-7 4V10z"/>',"Brain icon"),
"sexual":('<path d="M24 40S8 30 8 19a8 8 0 0 1 16-3 8 8 0 0 1 16 3c0 11-16 21-16 21z"/>',"Heart icon"),
}
CATS={"weight":"Weight & metabolism","recovery":"Healing & recovery","skin":"Skin","gh":"Growth hormone","longevity":"Longevity","brain":"Brain & focus","sexual":"Sexual health"}
def icon(c): p,l=ICON[c]; return svg(p,l)
# slug: (category, what it's for (short), how it's taken, straight answer for older guides)
META={
"semaglutide":("weight","Type 2 diabetes, weight loss, heart risk","Weekly shot or daily pill","Semaglutide works: big trials show real weight loss and fewer heart events, and the only doses that matter are the ones on the FDA label your prescriber follows."),
"tirzepatide":("weight","Type 2 diabetes, weight loss, sleep apnea","Weekly shot","Tirzepatide is the strongest approved weight-loss drug right now, and it beat semaglutide head-to-head in SURMOUNT-5."),
"retatrutide":("weight","Weight loss (in trials)","Weekly shot (trials only)",None),
"orforglipron":("weight","Weight loss","Daily pill",None),
"bpc-157":("recovery","Injury recovery (claimed)","Injection (unregulated)","BPC-157 has a lot of hype and almost no human data: 30 people across 3 weak studies. Nobody can honestly give you a proven dose."),
"tb-500":("recovery","Injury recovery (claimed)","Injection (unregulated)","TB-500 has no human trials of its own. The studies people cite tested a related protein, not the product sold online."),
"ghk-cu":("skin","Skin & hair","Cream/serum or injection","GHK-Cu in skincare is a normal cosmetic ingredient. Injecting it is a different thing with very little human data."),
"collagen-peptides":("skin","Skin hydration & elasticity","Powder or drink","Collagen peptides are one of the few peptide supplements with decent trial data for skin, usually after about 3 months of daily use."),
"tesamorelin":("gh","HIV-related belly fat","Daily shot",None),
"cjc-1295-ipamorelin":("gh","Growth hormone boost (claimed)","Injection (unregulated)",None),
"mots-c":("longevity","Metabolism & longevity (claimed)","Injection (unregulated)",None),
"semax":("brain","Focus & memory (claimed)","Nasal spray (unregulated)",None),
"pt-141":("sexual","Low sexual desire (women)","As-needed shot",None),
}
