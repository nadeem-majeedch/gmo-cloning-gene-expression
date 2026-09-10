# DIAGRAMS — Course Figures

Figures are **programmatically generated** (matplotlib) by `generate_diagrams.py` and used in the PPTX deck and PDFs. All diagrams are schematic teaching illustrations (not photographs of real data).

| File | Module | Shows |
|---|---|---|
| `plasmid_map.png` | 2–3 | Plasmid architecture: ori, marker, MCS, promoter–GOI–terminator cassette |
| `restriction_cloning.png` | 4 | Cut → anneal → ligate with sticky ends |
| `gibson_assembly.png` | 4 | Overlap chew-back → anneal → fill → seal |
| `golden_gate.png` | 4 | Type IIS cut outside recognition site → designer overhangs |
| `expression_cassette.png` | 5 | Promoter–UTR–CDS–terminator anatomy |
| `reporter_constructs.png` | 5, 9 | Promoter-reporter vs enhancer-reporter vs fusion |
| `crispr_mechanism.png` | 7 | sgRNA–PAM target recognition + DSB → NHEJ/HDR outcomes |
| `base_prime_editing.png` | 7, 15 | Base-editor and prime-editor concepts |
| `morphogen_gradient.png` | 8, 9 | French-flag thresholds over a gradient |
| `grn_cascade.png` | 8, 10 | Drosophila-style segmentation hierarchy |
| `neural_tube_pattern.png` | 8, 9 | DV fates vs Shh/BMP opposing gradients |
| `cloning_workflow.png` | 2 | 11-stage cloning pipeline |
| `selection_screening.png` | 3 | Selection → screening → validation funnel |
| `gmo_workflows.png` | 6 | Bacteria vs plant vs animal modification workflow |
| `ish_workflow.png` | 11 | In situ hybridization pipeline |
| `qpcr_workflow.png` | 11, 12 | RT → qPCR → ΔΔCt logic |
| `rnaseq_workflow.png` | 11, 12 | Bulk RNA-seq pipeline |
| `scrnaseq_workflow.png` | 11, 12 | Single-cell workflow: QC → PCA → clusters → annotation |
| `spatial_workflow.png` | 11, 12 | Array-based spatial transcriptomics pipeline |
| `expression_heatmap.png` | 12 | Simulated developmental time-course heatmap |
| `spatial_map_sim.png` | 12 | In-silico spatial map of region markers |

Regenerate: `python DIAGRAMS/generate_diagrams.py` (requires matplotlib).
