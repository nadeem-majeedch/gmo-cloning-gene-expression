---
title: All datasets
---

# All datasets

All course datasets are **simulated for education** - biologically plausible, deterministic (seeded) and clearly labeled. They must not be cited as experimental data.

| Collection | Used in | Contents |
|---|---|---|
| [Cloning data](cloning-data.md) | Labs 01-04 | Vector maps, digest predictions, colony-PCR results |
| [Gene-expression data](gene-expression-data.md) | Labs 05, 06, 08 | qPCR time courses, bulk RNA-seq, single-cell matrix, dual-luciferase data |
| [Spatial-expression data](spatial-expression-data.md) | Labs 07, 08 | Spot-gene spatial matrix, coordinates, region key |

Regenerate: `python DATA/generate_datasets.py` ([script](../assets/DATA/generate_datasets.py)). A worked analysis walkthrough ships as [`analysis_demo.py`](../assets/DATA/spatial-expression-data/analysis_demo.py).
