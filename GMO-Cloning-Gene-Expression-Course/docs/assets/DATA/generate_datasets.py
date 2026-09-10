#!/usr/bin/env python3
"""Generate all simulated teaching datasets for the course.

All data are SIMULATED for education - clearly labeled, biologically plausible,
not real experimental results. Deterministic (seeded) so instructors can
regenerate identical files with:  python DATA/generate_datasets.py
"""
import numpy as np
import os

rng = np.random.default_rng(42)
BASE = os.path.dirname(os.path.abspath(__file__))

def w(path, text):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(text)
    print("wrote", path)

def wcsv(path, header, rows):
    w(path, header + "\n" + "\n".join(rows) + "\n")

# ============================================================
# 1. CLONING DATA
# ============================================================
VEC_SIZE = 3200
INS_SIZE = 850
CONSTRUCT_SIZE = VEC_SIZE + INS_SIZE   # 4050

wcsv("cloning-data/gel_migration_ladder.csv", "band,migration_mm,size_bp",
     ["1,10,10000", "2,20,3000", "3,30,1000", "4,40,500", "5,50,100"])

# colony PCR: 24 colonies. Ground truth: 14 correct, 4 empty, 2 wrong-orientation,
# 2 mixed, 2 PCR-failure. Set A = flanking primers (empty 200 bp; insert 1050 bp).
# Set B = vector-F + insert-R (correct orientation 700 bp; wrong orientation none).
truth = (["correct"]*14 + ["empty"]*4 + ["wrong_orientation"]*2
         + ["mixed"]*2 + ["pcr_failure"]*2)
rng.shuffle(truth)
rows = ["colony,plate_color,setA_band_bp,setB_band_bp"]
for i, t in enumerate(truth, 1):
    if t == "correct":
        color, a, b = "white", 1050, 700
    elif t == "empty":
        color, a, b = "blue", 200, 0
    elif t == "wrong_orientation":
        color, a, b = "white", 1050, 0
    elif t == "mixed":
        color, a, b = rng.choice(["white", "blue"]), 0, 0   # both bands: recorded as special
    else:
        color, a, b = "white", 0, 0
    if t == "mixed":
        rows.append(f"{i},{color},1050;200,700")
    else:
        rows.append(f"{i},{color},{a},{b}")
wcsv("cloning-data/colony_pcr_results.csv",
     "NOTE this file pairs with Lab-04; ground truth in workbook", [])

# transformation plates: L1 background, L2 good, L3 self-ligation-heavy, L4 concatemers
wcsv("cloning-data/transformation_plates.csv",
     "condition,vector,insert,dephosphorylated,colonies,screened_correct_rate",
     ["L1,yes,no,yes,12,0.00",
      "L2,yes,yes(3:1),yes,180,0.68",
      "L3,yes,yes(3:1),no,140,0.15",
      "L4,yes,yes(10:1),yes,150,0.30"])

# plasmid scenarios for Lab 02 digest interpretation (sizes in bp)
wcsv("cloning-data/digest_band_positions.csv",
     "plasmid,digest,band_migration_mm",
     # migration -> size via ladder: 30mm~1000bp scale (see generator logic)
     # A = correct: 4050 vector+insert; digest1 (EcoRI+BamHI) -> 1900 + 2150
     #   1900bp ~ 25.2mm ; 2150bp ~ 24.0mm (log-linear on provided ladder fit)
     "A,digest1_EcoRI_BamHI,25.2\nA,digest1_EcoRI_BamHI,24.0\n"
     # B = empty vector: 3200 only -> ~22.5mm
     "B,digest1_EcoRI_BamHI,22.5\n"
     # C = rearranged: fragments 2300+1700+900 (sum 4900 > 3200 -> duplication)
     "C,digest1_EcoRI_BamHI,23.0\nC,digest1_EcoRI_BamHI,25.5\nC,digest1_EcoRI_BamHI,28.5")

w("cloning-data/pDevGFP_map.txt",
  "pDevGFP - teaching vector map (SIMULATED, not a real plasmid)\n"
  "Total size: 3200 bp | Marker: kanR | ori: pUC-class (high copy)\n"
  "MCS (all unique): EcoRI(1000) - BamHI(1050) - HindIII(1120) - XhoI(1200)\n"
  "lacZ alpha: 1400-1700 | T7 primer site: 950 | SP6 primer site: 1250\n"
  "Designed for Lab-01: clone shha promoter (850 bp) into EcoRI+HindIII.\n"
  "NOTE: vector-only teaching artifact; contains no functional pathogenic element.\n")

w("cloning-data/shha_promoter_850bp.txt",
  ">shha_promoter_fragment_850bp SIMULATED_SEQUENCE_for_Lab01\n"
  "TTGACAGCTAGCTAGCTTACGGATCCATCGATCGGATCCATCGGATCCGATCGATCGATCCGATC\n"
  "GGATCCATCGATCGGATCCATCGATCGATCGATCCGATCGGATCCATCGATCGATCCGGATCCA\n"
  "TCGATCCGGATCCGATCGGATCCATCGATCCGGATCCGGATCGATCCGGATCCATCGGATCCA\n"
  "TCGATCCGGATCCGGATCCGATCCGGATCCATCGGATCCGATCCGGATCCGGATCCATCCGAT\n"
  "CGGATCCGGATCCGATCCGGATCCATCGATCCGGATCCGGATCCGATCCGGATCCGGATCCAT\n"
  "CGATCCGGATCCGGATCCGATCCGGATCCATCGGATCCGATCCGGATCCGGATCCATCGATCC\n"
  "GGATCCGGATCCGATCCGGATCCATCGATCCGGATCCGGATCCGGATCCATCGGATCCGATCC\n"
  "GGATCCGGATCCATCCGGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGATCCGGAT\n"
  "CCGGATCCATCGGATCCGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGGATCCATC\n"
  "GGATCCGGATCCATCCGGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGATCCGGAT\n"
  "CCGGATCCATCGGATCCGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGGATCCATC\n"
  "GGATCCGGATCCATCCGGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGATCCGGAT\n"
  "CCGGATCCATCGGATCCGATCCGGATCCGGATCCATCGATCCGGATCCGGATCCGGATCCATC\n")
# NOTE for instructors: this placeholder fragment deliberately contains an internal
# BamHI site pattern (GGATCC) to match the Lab-01 design decision (EcoRI+HindIII).

w("cloning-data/design_check.py",
  '#!/usr/bin/env python3\n'
  '"""Lab-01 helper: check enzyme uniqueness in the (simulated) insert."""\n'
  'import sys\n'
  'SITES = {"EcoRI": "GAATTC", "BamHI": "GGATCC", "HindIII": "AAGCTT", "XhoI": "CTCGAG"}\n'
  'seq = "".join(l.strip() for l in open(sys.argv[1]) if not l.startswith(">"))\n'
  'for name, site in SITES.items():\n'
  '    pos, idx = [], seq.find(site)\n'
  '    while idx != -1:\n'
  '        pos.append(idx + 1); idx = seq.find(site, idx + 1)\n'
  '    status = "UNIQUE" if len(pos) == 0 else f"{len(pos)} internal site(s) at {pos}"\n'
  '    print(f"{name:8s} {status}")\n')

# ============================================================
# 2. GENE-EXPRESSION DATA
# ============================================================
# qPCR timecourse: 3 targets + 2 refs x 4 stages x 4 biological replicates
wcsv("gene-expression-data/qPCR_timecourse.csv",
     "NOTE SIMULATED teaching data - pairs with Lab-05", [])
rows = ["gene,stage_hpf,replicate,Cq"]
base = {"shha": 24.0, "myod1": 27.0, "pax6a": 26.0, "ef1a": 16.0, "rpl13a": 16.4}
trend = {"shha": [0.0, 0.3, 0.2, 0.1],
         "myod1": [0.0, -0.4, -2.9, -3.1],
         "pax6a": [0.0, -1.2, -2.0, -2.1],
         "ef1a":  [0.0, 0.0, 0.0, 0.0],
         "rpl13a":[0.0, 0.05, -0.05, 0.0]}
for gene, b in base.items():
    for si, stage in enumerate([10, 12, 18, 24]):
        for rep in range(1, 5):
            cq = b + trend[gene][si] + rng.normal(0, 0.25)
            rows.append(f"{gene},{stage},{rep},{cq:.2f}")
wcsv("gene-expression-data/qPCR_timecourse.csv", "gene,stage_hpf,replicate,Cq", rows[1:])

# reference gene stability (geNorm-style M values, lower = more stable)
wcsv("gene-expression-data/reference_gene_stability.csv", "gene,M_value,verdict",
     ["ef1a,0.31,stable", "rpl13a,0.34,stable", "gapdh,0.89,stage-variable - avoid alone"])

# bulk RNA-seq: 500 genes x 6 samples (WT/KO x 3), 18 DE genes incl. a 5-gene module
n_genes, n_samples = 500, 6
gene_names = [f"g{ i:03d}".replace(" ", "") for i in range(1, n_genes+1)]
module = ["g011", "g012", "g013", "g014", "g015"]
up = [f"g0{i:02d}" for i in range(16, 29)]               # KO-up set
base_mean = rng.uniform(60, 200, size=n_genes)            # per-gene base abundance
counts = rng.poisson(base_mean[:, None] * np.ones((1, n_samples))).astype(float)
for i, name in enumerate(gene_names):
    if name in module:
        counts[i, 3:6] = np.round(counts[i, 3:6] / 15)    # strongly down in KO
    elif name in up:
        counts[i, 3:6] = np.round(counts[i, 3:6] * 8)     # up in KO
wcsv("gene-expression-data/rnaseq_counts.csv", "gene," + ",".join(
    [f"WT_rep{r}" for r in (1,2,3)] + [f"KO_rep{r}" for r in (1,2,3)]),
    [f"{gene_names[i]}," + ",".join(str(int(x)) for x in counts[i])
     for i in range(n_genes)])
wcsv("gene-expression-data/metadata.csv", "sample,condition,batch",
     ["WT_rep1,WT,1", "WT_rep2,WT,1", "WT_rep3,WT,2",
      "KO_rep1,KO,1", "KO_rep2,KO,2", "KO_rep3,KO,2"])

# single-cell: 600 cells x 300 genes, 3 latent populations + 60-cell transition
n_cells, sc_genes = 600, 300
labels = (["neural"]*220 + ["muscle"]*210 + ["blood"]*170
          + ["transition"]*0)                      # transition folded into muscle set
rng.shuffle(labels)
markers = {"neural": ("pax6a", 36), "muscle": ("myod1", 34), "blood": ("hbbe1", 35)}
genes = [f"s{i:03d}" for i in range(1, sc_genes-2)] + ["pax6a", "myod1", "hbbe1"]
rows = ["cell," + ",".join(genes)]
cell_rows, meta_rows = [], []
transition_count = 0
for c in range(n_cells):
    lab = labels[c]
    # ~14% of muscle cells become a low-myod1 transition state
    if lab == "muscle" and transition_count < 60 and rng.random() < 0.35:
        lab = "transition"
        transition_count += 1
    base_vec = rng.negative_binomial(2, 0.25, size=len(genes) - 3).astype(float)
    vec = list(base_vec) + [0.0, 0.0, 0.0]
    if lab in markers:                                # clean cluster marker boost
        idx = genes.index(markers[lab][0])
        vec[idx] += rng.poisson(markers[lab][1])
    elif lab == "transition":
        vec[genes.index("myod1")] += rng.poisson(8)   # LOW myod1
    meta_rows.append(f"cell{c:04d},{lab},0,0")
    cell_rows.append(f"cell{c:04d}," + ",".join(str(int(x)) for x in vec))
wcsv("gene-expression-data/single_cell_counts.csv", rows[0].split(",", 1)[0] + "," + ",".join(genes), cell_rows[1:])
wcsv("gene-expression-data/cell_metadata.csv", "cell,latent_label,transition_flag,extra", meta_rows)

# developmental timecourse heatmap data (genes x stages)
stages = ["1cell", "oblong", "shield", "10hpf", "18hpf", "24hpf", "48hpf"]
maternal = ["nanos1", "dazl", "sox21a"]
zygotic  = ["myod1", "pax6a", "shha", "ntl", "eve1", "wnt8a", "notch1a"]
rows = ["gene," + ",".join(stages)]
for g in maternal:
    vals = [8.5, 8.0, 6.5, 4.0, 1.5, 0.5, 0.2]        # decaying (maternal)
    rows.append(f"{g}," + ",".join(f"{v + rng.normal(0,0.15):.2f}" for v in vals))
for g in zygotic:
    start = rng.uniform(6, 9)                          # rising (zygotic)
    peak = rng.uniform(2, 5)
    vals = [0.1, 0.2, peak*0.3, peak, start, start*0.9, start*0.6]
    rows.append(f"{g}," + ",".join(f"{v + rng.normal(0,0.15):.2f}" for v in vals))
wcsv("gene-expression-data/developmental_timecourse.csv", rows[0], rows[1:])

# dual luciferase (Lab 06): n=4 per construct
wcsv("gene-expression-data/dual_luciferase.csv",
     "construct,replicate,firefly,renilla",
     sum(([f"{c},{r},{rng.uniform(*rng_):.0f},{rng.uniform(90000, 110000):.0f}"
           for r in range(1, 5)]
          for c, rng_ in [("shha_promoter_WT", (90000, 130000)),
                          ("shha_promoter_motifmut", (15000, 26000)),
                          ("minimal_promoter_only", (7000, 13000)),
                          ("enhancer_orientA", (80000, 105000)),
                          ("enhancer_orientB", (75000, 98000)),
                          ("empty_vector", (6000, 12000))]), []))

# GFP region intensities (Lab 06 part 2)
wcsv("gene-expression-data/gfp_reporter_images_summary.csv",
     "construct,region_notochord,region_somite,region_neuraltube",
     sum(([f"{c},{rng.uniform(800, 1200):.0f},{rng.uniform(60, 110):.0f},{rng.uniform(40, 90):.0f}"
           for _ in range(3)]
          for c in ["shha_promoter_GFP", "minimal_GFP_control"]), []))

# ============================================================
# 3. SPATIAL EXPRESSION DATA
# ============================================================
n_spots, sp_genes = 200, 200
sp_gene_names = [f"sp{i:03d}" for i in range(1, sp_genes - 4)] + [
    "shha", "myod1", "pax6a", "gradient_gene", "edge_gene"]
# regions in a grid: 0 notochord (center strip), 1 somites (flanks), 2 neural tube (top)
coords, regions = [], []
for i in range(n_spots):
    x = float(i % 20) * 0.1
    y = float(i // 20) * 0.1
    coords.append((x, y))
    if y < 0.35:   regions.append("neural_tube")
    elif 0.35 <= y < 0.75 and 0.25 < x < 1.75: regions.append("somites")
    elif 0.9 <= y: regions.append("neural_tube")
    else:          regions.append("notochord")
wcsv("spatial-expression-data/spot_coordinates.csv", "spot,x,y",
     [f"spot{i:03d},{coords[i][0]:.1f},{coords[i][1]:.1f}" for i in range(n_spots)])
wcsv("spatial-expression-data/tissue_annotation.csv", "spot,region",
     [f"spot{i:03d},{regions[i]}" for i in range(n_spots)])

mat = rng.negative_binomial(2, 0.25, size=(n_spots, len(sp_gene_names))).astype(float)
for i in range(n_spots):
    reg = regions[i]
    x, y = coords[i]
    for j, g in enumerate(sp_gene_names):
        if g == "shha" and reg == "notochord":       mat[i, j] += rng.poisson(30)
        if g == "myod1" and reg == "somites":        mat[i, j] += rng.poisson(25)
        if g == "pax6a" and reg == "neural_tube":    mat[i, j] += rng.poisson(28)
        if g == "edge_gene":                          mat[i, j] += rng.poisson(max(0, int(40 * (0.9 - y))))  # gradient: declines with y
wcsv("spatial-expression-data/spatial_matrix.csv", "spot," + ",".join(sp_gene_names),
     [f"spot{i:03d}," + ",".join(str(int(v)) for v in mat[i]) for i in range(n_spots)])

print("\nAll datasets generated. All files are SIMULATED teaching data.")
