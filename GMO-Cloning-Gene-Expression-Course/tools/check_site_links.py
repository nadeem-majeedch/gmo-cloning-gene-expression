#!/usr/bin/env python3
"""Link QA for the built MkDocs site: verify every internal href/src in site/**/*.html
resolves to a real file on disk. Exits non-zero on any broken link.

Usage: python tools/check_site_links.py   (run after `mkdocs build`)
"""
import os
import re
import sys
from urllib.parse import urlparse, unquote

COURSE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(COURSE, "site")

broken, checked = [], 0
html_files = []
for root, _dirs, files in os.walk(SITE):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

ICON_HREF = re.compile(r"^(?:\.\./)*(?:material|fontawesome|octicons|simple|bootstrap|mdi|academicons|gist)/")

for page in sorted(html_files):
    if os.path.basename(page) == "404.html":
        # The 404 page legitimately uses absolute site_url-based paths, which only
        # resolve once the site is deployed under /REPOSITORY/ on GitHub Pages.
        continue
    with open(page, encoding="utf-8") as fh:
        html = fh.read()
    for url in re.findall(r'(?:href|src)="([^"]+)"', html):
        parsed = urlparse(url)
        if parsed.scheme in ("http", "https", "mailto", "javascript") or url.startswith(("#", "data:")):
            continue
        if ICON_HREF.match(url):
            continue  # Material theme icon sprite references, not real hyperlinks
        path = unquote(parsed.path)
        if not path:
            continue
        checked += 1
        target = os.path.normpath(os.path.join(os.path.dirname(page), path))
        if os.path.isdir(target):
            # directory URLs: index.html inside (use_directory_urls)
            target = os.path.join(target, "index.html")
        if not os.path.exists(target) and not os.path.exists(target + ".html"):
            broken.append((os.path.relpath(page, SITE), url))

print(f"checked {checked} internal links across {len(html_files)} pages")
if broken:
    print(f"BROKEN ({len(broken)}):")
    for p, u in broken:
        print("  ", p, "->", u)
    sys.exit(1)
print("all internal links resolve - site link QA passed")
