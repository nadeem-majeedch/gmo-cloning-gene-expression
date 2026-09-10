# Lab 05 — Gene-Expression Analysis with qPCR Data

**Type:** Computational (simulated qPCR dataset) · **Duration:** 1 session (~3 h)
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

> **Navigation:** [↑ Course Home](../README.md) · [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md) · 📊 [Gene-expression data](../DATA/gene-expression-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md)

## 1. Learning objectives

1. Apply the ΔΔCt method to a multi-replicate qPCR dataset.
2. Choose and justify reference genes using provided stability data.
3. Interpret a developmental time course (zebrafish *shha*, *myod1*, *pax6a*).
4. Report results to course standards (n, normalization, statistics, effect size).

## 2. Background

RT-qPCR quantifies transcripts relative to references. The ΔΔCt method converts Cq values to fold changes; the analysis is only as good as (a) RNA quality, (b) primer specificity/efficiency, and (c) reference-gene stability in the *actual* comparison. This lab uses a simulated zebrafish developmental time course (10–24 hpf, 4 stages × 4 biological replicates × 3 genes + 2 reference candidates).

## 3. Principle

```text
ΔCt   = Cq(target) − Cq(reference)
ΔΔCt  = ΔCt(stage) − ΔCt(calibrator stage)
FC    = 2^(−ΔΔCt)
```

Assumes ~100% amplification efficiency; efficiency-corrected methods (Pfaffl) when measured efficiencies differ. Statistics are performed on ΔCt (or log2 FC), not on fold changes.

## 4. Materials

- `DATA/gene-expression-data/qPCR_timecourse.csv` — Cq values (targets: *shha*, *myod1*, *pax6a*; references: *ef1a*, *rpl13a*; stages: 10, 12, 18, 24 hpf; n = 4 replicates)
- `DATA/gene-expression-data/reference_gene_stability.csv` — computed M-values/geNorm-style stability
- Python 3 (pandas, matplotlib) or spreadsheet software

## 5. Equipment

Computer with Python 3 and pandas/matplotlib.

## 6. Safety

Simulation only.

## 7. Procedure / workflow

1. Load the CSV; compute mean Cq per (gene, stage, replicate).
2. Evaluate reference stability from the provided table; choose the stable reference (or the geometric mean of both).
3. Compute ΔCt, then ΔΔCt vs the 10 hpf calibrator, then fold change.
4. Plot log2 fold change vs stage for the three genes.
5. Test stage effects on ΔCt (ANOVA or linear model — your choice; state it).
6. Write a results paragraph to course reporting standards.

## 8. Expected results (shape of the story)

- ***shha***: expression present from 10 hpf, modest change — early patterning gene.
- ***myod1***: strong rise between 12→18 hpf — myogenic commitment wave.
- ***pax6a***: rise from 12 hpf and plateau — anterior/neural specification.
- *(Simulated magnitudes; interpret the pattern, not the exact values.)*

## 9. Data table

| Gene | 10 hpf (calibrator) | 12 hpf FC | 18 hpf FC | 24 hpf FC | Stage effect p |
|---|---|---|---|---|---|
| *shha* | 1.0 | | | | |
| *myod1* | 1.0 | | | | |
| *pax6a* | 1.0 | | | | |

## 10. Calculations

- Full ΔCt/ΔΔCt/FC worked for *myod1* at 18 hpf (show arithmetic on replicate means of ΔCt).
- Reference-gene choice justification from stability values.

## 11. Interpretation

- Why analyze ΔCt statistically rather than fold change?
- Why is 10 hpf a reasonable calibrator here, and what would change if you picked 24 hpf?
- How would you *validate* the *myod1* result at the spatial level? (Method choice from Module 11.)

## 12. Troubleshooting (conceptual)

| Symptom | Likely cause | Fix |
|---|---|---|
| One replicate Cq 3 cycles late | Pipetting/RNA-quality outlier | Investigate; document exclusion rule |
| No-RT control amplifies | Genomic contamination | DNase; intron-spanning primers |
| References shift with stage | Unstable reference | Use validated alternative(s) |

## 13. Post-lab questions

1. Why is n = 4 *biological* replicates the minimum here rather than 4 technical replicates?
2. Your no-template control shows amplification at Cq 35. Diagnose.
3. Which spatial method would you choose to confirm the *myod1* result, and what would a positive result look like?

## 14. Viva questions

1. Define Cq/Ct.
2. Why must reference genes be validated per experiment?
3. What does a melt-curve peak at the wrong temperature indicate?

## 15. Instructor notes / answer key (summary)

- Reference choice: *ef1a* and *rpl13a* both stable; geometric-mean normalization is best practice.
- *myod1* 18 hpf: ΔCt ≈ 8.6 → ΔΔCt ≈ −2.9 → FC ≈ 7.5× vs 10 hpf (simulated values; workbook shows the arithmetic).
- Full solution and plots in the [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md).

## 16. Advanced challenge

Add an efficiency-correction step: given per-primer efficiencies from a (provided) dilution series table, recompute fold changes with the Pfaffl method and compare conclusions with ΔΔCt.
