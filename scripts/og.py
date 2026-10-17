#!/usr/bin/env python3
"""Render 1200x630 Open Graph cards from og/cards.json (written by make_site.py).
Run: /workspace/.pwvenv/bin/python scripts/og.py && .venv/bin/python build.py   (second build wires og:image)"""
import json, html, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
F = "/usr/share/fonts/truetype/sand-box/google"
BADGE = {"approved": ("#dcf5e3", "#14532d"), "research": ("#ece9fb", "#3b2a8f"), "supplement": ("#fdf0cf", "#7a3e05")}
CSS = f"""*{{box-sizing:border-box;margin:0}}body{{width:1200px;height:630px;background:#fbf6ee;font-family:Inter,sans-serif;color:#1b1f24;padding:44px}}
.card{{position:relative;height:100%;background:#fffdf9;border:4px solid #1b1f24;border-radius:28px;box-shadow:14px 14px 0 #e8b04b;padding:46px 56px;display:flex;flex-direction:column;overflow:hidden}}
.top{{display:flex;align-items:center;gap:14px;font-family:Fraunces,serif;font-weight:600;font-size:34px}}.top b{{font-weight:800}}
.k{{margin-top:34px;font-weight:700;font-size:24px;letter-spacing:.08em;text-transform:uppercase;color:#0f766e}}
h1{{font-family:Fraunces,serif;font-weight:800;line-height:1.04;margin-top:12px;letter-spacing:-.01em}}
.sub{{margin-top:18px;font-size:30px;color:#56606b;line-height:1.3;max-width:900px}}
.foot{{margin-top:auto;display:flex;white-space:nowrap;align-items:center;gap:18px;font-size:24px;font-weight:700}}
.badge{{border:3px solid currentColor;border-radius:999px;padding:6px 20px;font-size:24px}}.url{{margin-left:auto;color:#56606b;font-weight:600}}
.hot{{position:absolute;top:40px;right:48px;background:#c2410c;color:#fff;font-weight:800;font-size:24px;padding:8px 18px;border-radius:999px;border:3px solid #1b1f24}}
.dots{{position:absolute;right:-40px;bottom:-40px;opacity:.13}}"""
LOGO = '<svg viewBox="0 0 40 40" width="58" height="58"><circle cx="9" cy="20" r="6" fill="#0f766e"/><circle cx="20" cy="20" r="6" fill="#e8b04b"/><circle cx="31" cy="20" r="6" fill="#c2410c"/></svg>'
DOTS = '<svg class="dots" width="380" height="380" viewBox="0 0 40 40"><circle cx="9" cy="20" r="6" fill="#0f766e"/><circle cx="20" cy="20" r="6" fill="#e8b04b"/><circle cx="31" cy="20" r="6" fill="#c2410c"/></svg>'
def card(c):
    e = html.escape; n = len(c["title"]); size = 92 if n <= 20 else 74 if n <= 34 else 62 if n <= 48 else 54
    b = ""
    if c["badge"]:
        bg, fg = BADGE[c["badge"]]; b = f'<span class="badge" style="background:{bg};color:{fg}">{e(c["badge_t"])}</span>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="card">{DOTS}
<div class="top">{LOGO}<span>Peptide <b>Plainly</b></span></div>{'<span class="hot">🔥 Hot right now</span>' if c["hot"] else ''}
<p class="k">{e(c["kicker"])}</p><h1 style="font-size:{size}px">{e(c["title"])}</h1><p class="sub">{e(c["sub"])}</p>
<div class="foot">{b}{'' if len(c['badge_t'])>26 else '<span>Peptides, plainly. No BS.</span>'}<span class="url">peptideplainly.com</span></div></div></body></html>"""
cards = json.loads((ROOT / "og" / "cards.json").read_text())
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1200, "height": 630})
    for path, c in cards.items():
        pg.set_content(card(c)); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
        out = ROOT / "og" / f'{c["card"]}.png'; pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        print(out.name, out.stat().st_size // 1024, "KB")
    br.close()
