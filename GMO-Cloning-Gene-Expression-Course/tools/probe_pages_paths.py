#!/usr/bin/env python3
"""Mimic the GitHub Pages project-site layout locally and probe key URLs.

Serves the built site (site/) from a directory named
`gmo-cloning-gene-expression/` so every URL is tested exactly as it will be
served at https://nadeem-majeedch.github.io/gmo-cloning-gene-expression/...

Usage: python tools/probe_pages_paths.py
"""
import http.server
import os
import shutil
import sys
import threading
import urllib.request
from functools import partial

COURSE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(COURSE, "site")
SANDBOX = os.path.join(COURSE, ".pagetest")
ROOT = os.path.join(SANDBOX, "gmo-cloning-gene-expression")
PORT = 8768

if os.path.isdir(SANDBOX):
    shutil.rmtree(SANDBOX)
os.makedirs(ROOT)
shutil.copytree(SITE, ROOT, dirs_exist_ok=True)

Handler = partial(http.server.SimpleHTTPRequestHandler, directory=SANDBOX)
httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

BASE = f"http://127.0.0.1:{PORT}/gmo-cloning-gene-expression"
PATHS = [
    "/",
    "/modules/01-Introduction-to-Genetic-Engineering/",
    "/modules/02-DNA-and-Molecular-Cloning/",
    "/modules/11-Gene-Expression-Experimental-Methods/",
    "/labs/",
    "/labs/Lab-05-Gene-Expression-Analysis/",
    "/assessment/MCQs/",
    "/guide/cheat-sheet/",
    "/guide/workbook/",
    "/guide/faqs/",
    "/downloads/",
    "/downloads/datasets/",
    "/downloads/cloning-data/",
    "/downloads/gene-expression-data/",
    "/downloads/spatial-expression-data/",
    "/downloads/diagrams/",
    "/projects/",
    "/references/",
    "/about/",
    "/assets/DIAGRAMS/plasmid_map.png",
    "/assets/DIAGRAMS/morphogen_gradient.png",
    "/assets/PDF/Complete-Tutorial.pdf",
    "/assets/PDF/Lab-Workbook.pdf",
    "/assets/PDF/Cheat-Sheet.pdf",
    "/assets/PDF/FAQs.pdf",
    "/assets/PDF/Assessment.pdf",
    "/assets/PPTX/GMO_Cloning_Gene_Expression.pptx",
    "/assets/DATA/cloning-data/pDevGFP_map.txt",
    "/assets/DATA/gene-expression-data/qpcr_timecourse.csv",
    "/assets/DATA/spatial-expression-data/spatial_matrix.csv",
    "/assets/DATA/spatial-expression-data/analysis_demo.py",
    "/stylesheets/extra.css",
    "/search/search_index.json",
]

failed = 0
for p in PATHS:
    try:
        with urllib.request.urlopen(BASE + p, timeout=10) as r:
            code, size = r.status, len(r.read())
        mark = "ok "
    except urllib.error.HTTPError as e:
        code, size = e.code, 0
        mark = "FAIL"
        failed += 1
    print(f"{mark} {code} {size:>9,} B  {p}")

httpd.shutdown()
print()
if failed:
    print(f"{failed} FAILURES - project-path serving broken")
    sys.exit(1)
print(f"all {len(PATHS)} URLs serve correctly under /gmo-cloning-gene-expression/ - project-path QA passed")
