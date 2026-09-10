# GMO, Cloning & Gene-Expression Lab Workbook

**Consolidated instructor/student workbook for Labs 01–09**
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

> **Navigation:** [↑ Course Home](../README.md) · [Labs](../LAB/Lab-01-DNA-Cloning-Design.md) · [Cheat Sheet](../CHEAT-SHEET/GMO-Cloning-Gene-Expression-Cheat-Sheet.md) · [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md) · [Answer keys](../ASSESSMENT/Answer-Key.md)

**How to use this workbook:** each section pairs one lab with its model answers, worked calculations, and grading notes. Lab documents themselves contain the objectives/procedure; this workbook carries the *solutions and teaching guidance*. Student-facing copies should be issued **without** Sections marked **[Instructor]**.

---

## Contents

1. [Lab 01 — Cloning design (solutions)](#lab-01)
2. [Lab 02 — Restriction digestion (solutions)](#lab-02)
3. [Lab 03 — Ligation & transformation (solutions)](#lab-03)
4. [Lab 04 — Colony PCR & screening (solutions)](#lab-04)
5. [Lab 05 — qPCR expression analysis (solutions)](#lab-05)
6. [Lab 06 — Reporter analysis (solutions)](#lab-06)
7. [Lab 07 — Spatial expression (solutions)](#lab-07)
8. [Lab 08 — Computational expression (solutions)](#lab-08)
9. [Lab 09 — Capstone (rubric + models)](#lab-09)
10. [Grading rubrics and reporting standards](#standards)

---

## Lab 01 — Cloning design <a id="lab-01"></a>

**[Instructor] Model answers**

- **Vector inventory:** 3,200 bp; kanR; ori high-copy (pUC-class); MCS sites EcoRI, BamHI, HindIII, XhoI all unique; T7/SP6 priming sites flank MCS; lacZα present.
- **Insert scan:** *shha* promoter 850 bp contains **one internal BamHI** site (position 512); no EcoRI/HindIII/XhoI.
- **Enzyme pair:** **EcoRI + HindIII**. BamHI fails (internal site); XhoI alone can't give directionality with only one flanking mate in the MCS layout.
- **Primers (model):**
  - Forward: `5′-GCACGAATTC<21 nt of promoter start>-3′` (clamp + EcoRI)
  - Reverse: `5′-GCACAAGCTT<revcomp of promoter end>-3′` (clamp + HindIII)
  - (Clamps: 4–6 nt; GC clamp at 3′ end of the gene-specific portion.)
- **Ligation math (3:1, 50 ng vector):** ng insert = 50 × (850/4050) × 3 ≈ **31.5 ng**.
- **Diagnostic digest (EcoRI + BamHI):** construct → **1.9 kb + 2.15 kb**; empty vector → **3.2 kb single band** (BamHI unique; insert adds the second EcoRI-proximal cut point... full derivation in dataset README).
- **Common failure to discuss:** primer design forgetting the clamp → enzyme can't cut the PCR product efficiently → no insert preparation at all.

---

## Lab 02 — Restriction digestion <a id="lab-02"></a>

**[Instructor] Model answers**

- Ladder interpolation: fit log10(size) vs migration → linear (r² > 0.99 in provided data).
- **Plasmid A:** digest-1 observed 4.05 + 0.85 kb ⇒ **correct construct** (vector 3.2 + insert 0.85); digest-2 consistent.
- **Plasmid B:** digest-1 observed 3.2 kb only ⇒ **empty vector** (single site — the "insert" never integrated).
- **Plasmid C:** digest-1 observed 2.3 + 1.7 + 0.9 kb; **sum = 4.9 kb ≠ 3.2 kb** ⇒ plasmid is larger than the map ⇒ **rearrangement/duplication** (a second copy of part of the insert, or concatenated assembly) — inferred because *fragment sum exceeds nominal size*.
- **Teaching point:** always sum fragment sizes; a size mismatch is the fingerprint of rearrangement that a single "bands match" reading can miss.
- Post-lab answers: uncut plasmid supercoiling; third-site causes; semilog ladder rationale (Module 12 §1.1).

---

## Lab 03 — Ligation & transformation <a id="lab-03"></a>

**[Instructor] Model answers & expected pattern**

- Setup math: 3:1 ⇒ 31.5 ng insert; 10:1 ⇒ 105 ng insert (50 ng vector).
- Expected colony pattern (provided CSV):

| Condition | Colonies (simulated) | Interpretation |
|---|---|---|
| L1 vector-only, dephosphorylated | ~12 | background baseline |
| L2 3:1, dephosphorylated | ~180 | good yield; screen ~8–12 |
| L3 3:1, NOT dephosphorylated | ~140 but ~85% empty | self-ligation dominated |
| L4 10:1, dephosphorylated | ~150 but concatemer-heavy | insert excess pathology |

- Screening decision: white-colony pick ×12 (vector has lacZα) + colony PCR Set A.
- **Grading emphasis:** students must articulate that colony *number* alone can rank conditions wrongly (L3 high count, bad outcome) — screening rates are the meaningful metric.

---

## Lab 04 — Colony PCR & screening <a id="lab-04"></a>

**[Instructor] Model answers**

- Set A (flanking): empty ≈ 0.20 kb; insert ≈ 1.05 kb; orientation-blind.
- Set B (vector-F + insert-R): correct orientation ≈ 0.7 kb; wrong orientation = no band.
- **CSV ground truth (24 colonies):** 14 correct; 4 empty; 2 wrong-orientation; 2 mixed; 2 PCR-failure.
- Blue-white cross-check: all 4 empty colonies blue (consistent); 1 blue colony is PCR-positive → carry forward for digest (possible lacZα-sparing insertion at MCS edge) — designed teaching anomaly.
- Sanger plan: F + R vector-primed reads (≈700–900 bp each) cover 850 bp insert + junctions; no internal primer needed.
- **Grading emphasis:** the "PCR-positive but digest-negative" contradiction (one mixed colony) — students must resolve it by trusting *structural* evidence over *amplification* evidence.

---

## Lab 05 — qPCR expression analysis <a id="lab-05"></a>

**[Instructor] Model answers**

- Reference selection: *ef1a* M = 0.31, *rpl13a* M = 0.34 (stable); use geometric mean.
- Worked *myod1* @ 18 hpf (simulated data): mean Cq target 24.1; mean Cq ref 15.5 → ΔCt 8.6; calibrator (10 hpf) ΔCt 11.5 → ΔΔCt = −2.9 → **FC ≈ 7.5×**.
- Stage effect: *myod1* ANOVA p < 0.001 (12→18 hpf rise); *shha* p = 0.21 (stable); *pax6a* p = 0.004 (rise then plateau).
- Reporting-standard check: n = 4 biological; stats on ΔCt; fold change reported with CI or SD of ΔCt.
- Spatial validation expectation: *myod1* signal in somites/adaxial cells by ISH at 18 hpf (Lab 07 panels).

---

## Lab 06 — Reporter analysis <a id="lab-06"></a>

**[Instructor] Model answers**

- Normalization: ratio Firefly/Renilla per replicate → mean ± SD (n = 4).
- Simulated results: WT promoter 12.3 ± 1.1; motif-mutant 2.4 ± 0.5 (**~80% reduction**); minimal-only 1.1 ± 0.2; enhancer-A 9.8 ± 0.9; enhancer-B 9.1 ± 1.0 (orientation-flexible ⇒ enhancer-like); empty 1.0 ± 0.1.
- Statistics: t-test WT vs mutant p < 0.001; WT vs minimal p < 0.001; A vs B p = 0.38 (n.s. → consistent with enhancer behavior).
- Fluorescence panel: notochord GFP ≫ somite ≈ neural-tube background — concordant with endogenous *shha* literature.
- Validity ceiling (must appear in student answers): reporter ≠ endogenous claim; sufficiency-not-necessity for enhancer.

---

## Lab 07 — Spatial expression <a id="lab-07"></a>

**[Instructor] Model answers**

- Scoring key (0–3):

| Panel | notochord | floor plate | somites | PSM | forebrain | eye | type |
|---|---|---|---|---|---|---|---|
| *shha* | 3 | 3 | 0 | 0 | 0 | 0 | graded DV decrease |
| *myod1* | 0 | 0 | 3 | 1 | 0 | 0 | domains, stage-dependent |
| *pax6a* | 0 | 0 | 0 | 0 | 3 | 3 | broad anterior domain |
| *ntl* | 3 | 1 | 0 | 3 | 0 | 0 | staging marker |
| sense / no-probe | ≤1 everywhere | | | | | | background |

- Gradient vs domain: *shha* DV profile decreases continuously (monotonic, no plateau-to-zero step) ⇒ gradient-consistent; students must state the quantitative criterion they used.
- Staging check: *ntl* PSM positivity confirms pre-mid-somitogenesis for the *myod1* panel.
- Probe design (egr2b/krox20): hindbrain rhombomeres 3/5 expected; same control set.

---

## Lab 08 — Computational expression <a id="lab-08"></a>

**[Instructor] Model answers**

- **Bulk:** 18 genes at FDR < 0.05 & |log2FC| > 1; top hit log2FC = −3.2 (KO-down); volcano separates a coherent 5-gene module (provided pathway list) — discuss batch balance (metadata confirms 3 WT/3 KO balanced across 2 batches).
- **Single-cell:** QC keeps ~540/600 cells; k=3 clusters ≈ 220 (pax6a-high, neural) / 210 (myod1-high, muscle) / 170 (hbbe1-high, blood); k=4 reveals a 60-cell intermediate (low myod1, low actc1) ⇒ differentiating muscle precursors.
- **Spatial:** region markers recover annotation labels (spot-level accuracy ~92%); edge-gradient gene r = −0.6 (expression highest at tissue edge, p < 0.001, n = 200 spots).
- **Teaching emphasis:** each analysis ends with a validation plan (ISH for the gradient gene; qPCR for the top DE gene).

---

## Lab 09 — Capstone <a id="lab-09"></a>

**[Instructor] Rubric (100 pts)**

| Component | Points | Excellence marker |
|---|---|---|
| Question & design | 25 | falsifiable, single-variable, resolution matched to question |
| Execution / analysis | 25 | correct workflows; QC explicit; stats appropriate |
| Interpretation & validity | 25 | claims bounded; "not proven" list present |
| Defense & synthesis | 15 | answers *why*, not just *what*; connects modules |
| Reporting standards | 10 | n/normalization/stats/effect-size stated; no fabricated citations |

**Model spine (Track A example):** *shha* promoter-GFP (Lab-01 construct) + CRISPRi enhancer-test vector; EcoRI/HindIII plan; validation = colony PCR → digest → Sanger; expression readout = simulated GFP panels (Lab 06/07 logic); falsification test = motif-mutant reporter + CRISPRi endogenous enhancer with ISH readout.

---

## Grading rubrics and reporting standards <a id="standards"></a>

**Standard lab rubric (20 pts each):**

| Component | Points |
|---|---|
| Objectives met / correct workflow | 6 |
| Data tables complete & correct | 5 |
| Calculations shown | 4 |
| Interpretation (incl. controls discussion) | 3 |
| Post-lab & viva performance | 2 |

**Course reporting standards (apply everywhere):**

1. **n** = biological replicates (technical replicates stated separately).
2. **Normalization:** reference genes / size factors named.
3. **Statistics:** test + correction + threshold.
4. **Effect size:** fold change / log2FC, not only p-values.
5. **Validation:** every major claim paired with its independent-method check.
6. **Integrity:** simulated data labeled as simulated; no fabricated citations or results.
