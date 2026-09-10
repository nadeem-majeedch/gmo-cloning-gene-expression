# Lab 07 — Spatial Gene-Expression Interpretation (In-situ-style images/data)

**Type:** Simulation / Image-interpretation · **Duration:** 1 session (~3 h)
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

## 1. Learning objectives

1. Interpret simulated in-situ-hybridization images (domains, gradients, staging artifacts).
2. Design the probe/controls for a new spatial target.
3. Quantify spatial patterns (domain area, intensity profile) from provided data.
4. Distinguish gradient from domain quantitatively.

## 2. Background

In situ hybridization maps endogenous mRNA spatially (Module 11). Reading ISH images is a core developmental-biology skill: identifying domains, comparing across stages, and recognizing artifacts (staining heterogeneity, probe trapping, staging mismatch).

## 3. Principle

Antisense probe hybridizes to target RNA; detection yields spatial signal. Sense/no-probe controls bound background; a known marker validates staging and protocol. Signal intensity is *semi*-quantitative — pattern (where) is trustworthy; absolute amount is not.

## 4. Materials (simulation)

- `DATA/spatial-expression-data/ish_sim_images/` — 6 synthetic embryo panels (anterior up): *shha* (notochord/floor-plate domain), *myod1* (somites), *pax6a* (forebrain/eye), *ntl* (presomitic mesoderm + notochord), sense-probe control, no-probe control
- `DATA/spatial-expression-data/intensity_profiles.csv` — dorsal–ventral intensity profiles per panel
- Python 3 (matplotlib) or image-analysis software
- *All images are generated simulations labeled as such — no real embryos are depicted.*

## 5. Equipment

Computer (Python 3: matplotlib, pandas).

## 6. Safety

Simulation only. (Real ISH teaching demonstrations involve fixed specimens and formamide-containing buffers — instructor-demonstration only, per institutional chemical-hygiene SOPs.)

## 7. Procedure / workflow

1. **Inventory the panels:** gene, stage, view, probe type (antisense/sense/none).
2. **Score each panel** (0 = absent, 1 = weak, 2 = moderate, 3 = strong) by region: notochord, floor plate, somites, PSM, forebrain, eye, neural tube.
3. **Compare antisense vs controls** — establish background level.
4. **Domain vs gradient:** for *shha*, plot the DV intensity profile; fit a monotonic decrease (gradient) vs step (domain) — which does the data support?
5. **Staging check:** use *ntl* (PSM marker) to verify the stage annotation of each panel.
6. **Design the next probe:** pick one gene from Module 8 (e.g., *krox20/egr2b*) and specify probe region, controls, expected pattern.

## 8. Expected results (shape)

| Gene | Domain(s) | Pattern type |
|---|---|---|
| *shha* | notochord/floor plate | graded dorsal decrease |
| *myod1* | somites (formed), adaxial cells | domains, stage-dependent |
| *pax6a* | forebrain/eye field | broad domain |
| *ntl* | PSM + notochord | domains; staging marker |
| sense / no-probe | uniform faint/no signal | background |

## 9. Data table

| Panel | Region scores (0–3 each) | Background level | Pattern type |
|---|---|---|---|
| *shha* | | | |
| *myod1* | | | |
| *pax6a* | | | |
| *ntl* | | | |
| sense | | | |
| no-probe | | | |

## 10. Calculations

- From `intensity_profiles.csv`: compute the dorsal-to-ventral intensity ratio for *shha*; state whether it is consistent with a gradient (continuous) or a domain (step).
- Domain area: threshold the *pax6a* panel at background + 2 SD; compute fraction of embryo area positive.

## 11. Interpretation

- Why is the sense-probe panel the *only* valid background reference for this protocol?
- A colleague claims *shha* shows a "step function". What plot settles it?
- Why does *ntl* expression in both PSM and notochord complicate staging calls if used alone?

## 12. Troubleshooting (image-level)

| Symptom | Likely cause | Fix |
|---|---|---|
| Speckled background | Probe trapping / poor washing | Re-wash; longer stringency |
| Uniform signal everywhere | Probe too short/repetitive; overstaining | Redesign probe; shorten development |
| No signal anywhere | Probe degradation; RNA destroyed | Positive-control probe run |

## 13. Post-lab questions

1. Why validate staging with an independent marker rather than morphology alone?
2. Your target gene's ISH shows signal in "everything". Name three causes and fixes.
3. What does ISH *not* tell you about gene expression that a reporter would? (Dynamics.)

## 14. Viva questions

1. Antisense vs sense probe — define.
2. Why is ISH semi-quantitative at best?
3. What does an RNAscope-class method add over classical ISH?

## Figures

<figure markdown>
![In situ hybridization workflow: probe design, hybridization, washing, detection and spatial interpretation.](../assets/DIAGRAMS/ish_workflow.png)

*Figure - In situ hybridization workflow: probe design, hybridization, washing, detection and spatial interpretation.*
</figure>

<figure markdown>
![In-silico spatial expression map used in the computational labs (region markers and gradients).](../assets/DIAGRAMS/spatial_map_sim.png)

*Figure - In-silico spatial expression map used in the computational labs (region markers and gradients).*
</figure>


## 15. Instructor notes / answer key (summary)

- Scoring keys and profile analysis are in the [Workbook](../guide/workbook.md).
- The *shha* DV profile in the simulation decreases continuously — gradient-consistent; students should articulate the quantitative criterion used.

## 16. Advanced challenge

Given the simulated *myod1* panels at two stages, quantify the change in somite-domain area and propose a biological explanation involving somitogenesis timing (Module 9).

---

**Related resources:** [Lab workbook](../guide/workbook.md) · [Cheat sheet](../guide/cheat-sheet.md) · [Datasets](../downloads/datasets.md) · [Assessments](../assessment/index.md)

[Course home](../index.md)
