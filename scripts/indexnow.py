#!/usr/bin/env python3
"""Submit every URL in sitemap.xml to IndexNow (Bing, Yandex, Seznam, Naver, Yep...).

Usage (from the repo root, after a deploy is live):
    python3 scripts/indexnow.py --dry-run   # show what would be sent, send nothing
    python3 scripts/indexnow.py             # POST to https://api.indexnow.org/indexnow

Reads the local sitemap.xml (same file GitHub Pages serves) and the key from make_site.py.
The key file must already be live at https://peptideplainly.com/<key>.txt.
"""
import json, pathlib, re, sys, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "peptideplainly.com"
ENDPOINT = "https://api.indexnow.org/indexnow"

def key():
    m = re.search(r'^INDEXNOW_KEY="([0-9a-f]{8,128})"', (ROOT / "make_site.py").read_text(), re.M)
    if not m: sys.exit("INDEXNOW_KEY not found in make_site.py")
    k = m.group(1)
    if not (ROOT / f"{k}.txt").exists(): sys.exit(f"{k}.txt missing: run build.py first")
    return k

def urls():
    locs = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text())
    locs = [u for u in locs if u.startswith(f"https://{HOST}/")]
    if not locs: sys.exit("no URLs in sitemap.xml")
    return locs

def main():
    k = key()
    payload = {"host": HOST, "key": k, "keyLocation": f"https://{HOST}/{k}.txt", "urlList": urls()}
    print(f"{len(payload['urlList'])} URLs, keyLocation {payload['keyLocation']}")
    if "--dry-run" in sys.argv:
        print(json.dumps(payload, indent=2)); return
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} (200/202 = accepted)")
    except urllib.error.HTTPError as e:
        # 400 bad request, 403 key not valid/not found, 422 URLs don't match host, 429 too many requests
        sys.exit(f"IndexNow: HTTP {e.code} {e.read().decode(errors='replace')[:300]}")

if __name__ == "__main__":
    main()
