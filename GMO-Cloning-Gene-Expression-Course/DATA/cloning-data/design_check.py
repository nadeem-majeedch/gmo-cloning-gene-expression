#!/usr/bin/env python3
"""Lab-01 helper: check enzyme uniqueness in the (simulated) insert."""
import sys
SITES = {"EcoRI": "GAATTC", "BamHI": "GGATCC", "HindIII": "AAGCTT", "XhoI": "CTCGAG"}
seq = "".join(l.strip() for l in open(sys.argv[1]) if not l.startswith(">"))
for name, site in SITES.items():
    pos, idx = [], seq.find(site)
    while idx != -1:
        pos.append(idx + 1); idx = seq.find(site, idx + 1)
    status = "UNIQUE" if len(pos) == 0 else f"{len(pos)} internal site(s) at {pos}"
    print(f"{name:8s} {status}")
