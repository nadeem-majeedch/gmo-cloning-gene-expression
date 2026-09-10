# Lab 03 — Ligation and Transformation Workflow (Simulation)

**Type:** Simulation (wet-lab procedures are institution-SOP dependent) · **Duration:** 1 session (~3 h)
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

> **Navigation:** [↑ Course Home](../README.md) · [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md) · 📊 [Cloning data](../DATA/cloning-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md)

## 1. Learning objectives

1. Set up a ligation logically: molar ratios, controls, and dephosphorylation decisions.
2. Predict transformation outcomes from ligation composition.
3. Interpret plate counts (positive/negative/experimental) quantitatively.
4. Decide which colonies to screen and why.

## 2. Background

Ligation joins prepared insert and vector; transformation introduces the products into competent cells. Both steps are probabilistic — the design of controls is what makes the outcomes interpretable. This lab simulates the workflow so students learn the *decision logic* before (or instead of) bench practice.

## 3. Principle

- T4 DNA ligase seals phosphodiester bonds between adjacent 5′-phosphate and 3′-OH ends; ATP-dependent.
- Vector self-ligation competes with insert incorporation → dephosphorylation of vector 5′ ends (where appropriate) and correct insert:vector molar ratios matter.
- Chemical transformation and electroporation introduce plasmids into competent cells with empirically defined efficiency — *follow institutional SOPs; protocols vary by strain/equipment*.

## 4. Materials (simulation)

- `DATA/cloning-data/ligation_setup.csv` — vector/insert masses, sizes, ratios for four ligation conditions
- `DATA/cloning-data/transformation_plates.csv` — colony counts for each condition
- Calculator or the workbook sheet

**Conditions (teaching design):**

| Ligation | Vector | Insert | Dephosphorylated? | Purpose |
|---|---|---|---|---|
| L1 | + | – | yes | vector-only control (background) |
| L2 | + | + (3:1) | yes | experimental |
| L3 | + | + (0:1... see data) | no | ratio-error demonstration |
| L4 | + | + (10:1) | yes | insert-excess demonstration |

## 5. Equipment

Computer/calculator. (Wet-lab version requires competent cells, selective plates etc. **per institutional SOP and instructor approval only**.)

## 6. Safety

Simulation: none. Wet-lab version: standard BSL-1 containment and disinfection per institutional SOPs; no operational parameters are specified here by design.

## 7. Procedure / workflow

1. Compute ng of insert needed for each ratio (Lab-01 formula).
2. Complete the ligation-setup table.
3. Open `transformation_plates.csv`; compute colonies per condition (and colonies/ng if provided).
4. Classify each condition's outcome: background level, good yield, ratio error, or contamination.
5. For the best condition, decide *how many colonies to screen* and which screen (colony PCR vs blue-white) fits this vector (kanR + lacZα, per Lab-01 map).

## 8. Expected results

- L1 (vector-only) → low background (a few colonies) — the baseline empty-vector rate.
- L2 (3:1, dephosphorylated) → highest proportion of correct clones.
- L3 → high empty-vector background (no dephosphorylation).
- L4 → many multi-insert/concatemer events (higher-than-expected insert-size colonies).

## 9. Data table

| Condition | Colonies | Empty-vector rate | Correct-clone rate (from later screening data) |
|---|---|---|---|
| L1 | | | — |
| L2 | | | |
| L3 | | | |
| L4 | | | |

## 10. Calculations

- Insert ng per condition (3:1 and 10:1 with 50 ng vector; insert 850 bp, vector 3.2 kb).
- Transformation efficiency = colonies / µg DNA (where the dataset provides it).

## 11. Interpretation

- Why does dephosphorylation *reduce* L1 colonies specifically?
- Why does excess insert produce concatemers rather than more correct clones?

## 12. Troubleshooting (conceptual)

| Symptom | Likely cause | Fix |
|---|---|---|
| No colonies anywhere | Dead competent cells / wrong antibiotic | Positive-control transformation |
| L2 ≈ L1 | Ligation failed or insert ends incompatible | Recheck digest/ends |
| Too many colonies on L1 | Over-dephosphorylation failure; over-plating | Repeat with fresh CIP/rSAP step |

## 13. Post-lab questions

1. Why is the L1 control essential to interpreting L2?
2. What would you change first if L4 yields concatemers?
3. Why must the "correct-clone rate" be measured by screening, not by colony number?

## 14. Viva questions

1. What cofactor does T4 ligase require?
2. Define competent cells (conceptual).
3. Why dephosphorylate the vector in blunt-end cloning *always*, but not necessarily in two-enzyme directional cloning?

## 15. Instructor notes / answer key (summary)

- Expected pattern: L1 < L3 < L2 in correct-clone rate; L4 shows concatemers. Colony counts are in the CSV; class-average discussion points are in the [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md).
- Wet-lab conversion: if the institution permits a real transformation teaching exercise, substitute the approved SOP for Section 7 and add the SOP reference to Section 6; keep the same data tables.

## 16. Advanced challenge

Design a ligation strategy using **two inserts** (promoter + GFP) into one vector in a *single* reaction — state the order/orientation logic and which technique (restriction vs Gibson vs Golden Gate) you would pick and why.
