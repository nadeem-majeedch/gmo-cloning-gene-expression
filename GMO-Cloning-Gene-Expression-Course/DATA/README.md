# DATA — Simulated Teaching Datasets

**All files in this folder are SIMULATED for education.** They are biologically plausible, deterministic (seeded), and **not real experimental results**. Gene names are used for realistic context only.

Regenerate everything identically:

```bash
python DATA/generate_datasets.py     # requires numpy
```

## cloning-data/ (Labs 01–04)

| File | Content |
|---|---|
| `pDevGFP_map.txt` | Teaching vector map (3.2 kb, kanR, EcoRI/BamHI/HindIII/XhoI MCS) |
| `shha_promoter_850bp.txt` | Simulated promoter fragment for Lab-01 design (contains internal BamHI) |
| `design_check.py` | Restriction-site uniqueness checker |
| `gel_migration_ladder.csv` | Ladder sizes + migration for Lab-02 sizing |
| `digest_band_positions.csv` | Digest band migrations for plasmids A/B/C (correct/empty/rearranged) |
| `colony_pcr_results.csv` | 24 simulated colonies × 2 primer sets (Lab-04) |
| `transformation_plates.csv` | Colony counts + correct-clone rates for conditions L1–L4 (Lab-03) |

## gene-expression-data/ (Labs 05, 06, 08 + Module 12)

| File | Content |
|---|---|
| `qPCR_timecourse.csv` | Cq values: 3 targets + 2 refs × 4 stages × 4 replicates (zebrafish-style) |
| `reference_gene_stability.csv` | geNorm-style M-values for reference choice |
| `rnaseq_counts.csv` | 500 genes × 6 samples (WT/KO × 3); 18 DE genes incl. a 5-gene module |
| `metadata.csv` | Sample sheet (condition, batch — balanced) |
| `single_cell_counts.csv` | 600 cells × 300 genes; 3 populations + transition state |
| `cell_metadata.csv` | Cell labels (instructor key) + QC hints |
| `developmental_timecourse.csv` | 10 genes × 7 stages (maternal-decay vs zygotic-rise patterns) |
| `dual_luciferase.csv` | Firefly/Renilla for 6 constructs × 4 replicates (Lab-06) |
| `gfp_reporter_images_summary.csv` | Region GFP intensities for 2 constructs (Lab-06 part 2) |

## spatial-expression-data/ (Lab 07–08 + Module 12)

| File | Content |
|---|---|
| `spatial_matrix.csv` | 200 spots × 200 genes incl. region markers + one edge-gradient gene |
| `spot_coordinates.csv` | x,y per spot (grid) |
| `tissue_annotation.csv` | Spot → region key (neural_tube / somites / notochord) — instructor key |

## Integrity notes

- Deterministic seed (42) → regenerating reproduces identical files.
- `qPCR_timecourse.csv` values are Cq (lower = more transcript).
- `spatial_matrix.csv` `edge_gene` declines monotonically with **y** — used for the gradient-vs-domain exercise.
- Instructors: keep `tissue_annotation.csv` and `cell_metadata.csv` as keys if students should derive labels themselves.
