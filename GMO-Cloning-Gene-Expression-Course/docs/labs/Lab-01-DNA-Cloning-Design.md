# Lab 01 — Molecular Cloning Design Exercise

**Type:** Simulation (no living organisms) · **Duration:** 1 session (~3 h)
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

## 1. Learning objectives

By the end of this lab you will be able to:
1. Design a restriction-based cloning plan from a vector map and insert sequence.
2. Choose enzymes for directional cloning and justify the choice.
3. Design PCR primers that add restriction sites and maintain reading frame.
4. Compute insert:vector molar ratios for ligation setup.
5. Predict the diagnostic-digest pattern that will confirm the final construct.

## 2. Background

Every cloning project begins *in silico*. Wrong design decisions cascade into wasted weeks; right ones make the bench work routine. This exercise simulates the full design phase for a reporter construct you will "build" in the following labs.

**Scenario:** You study a zebrafish developmental gene, ***shha*** (sonic hedgehog a), and want to test whether its promoter drives expression in the notochord/floor-plate. You will clone a 850 bp *shha* promoter fragment upstream of **GFP** in a 3.2 kb plasmid vector.

## 3. Principle

Directional restriction cloning: two different restriction enzymes generate non-compatible sticky ends on both vector and insert, forcing a single orientation. The design must verify (a) the chosen sites are unique in the vector, (b) they are absent from the insert, (c) reading frame and any tag junctions are preserved, (d) a diagnostic digest exists that distinguishes correct clones from empty vector.

## 4. Materials (simulation)

- Vector map `DATA/cloning-data/pDevGFP_map.txt` (MCS: EcoRI, BamHI, HindIII, XhoI — all unique; ori; kanR; T7/SP6 priming sites; lacZα)
- Insert sequence `DATA/cloning-data/shha_promoter_850bp.txt`
- In-silico tools: any restriction analyzer (or the provided scripts `DATA/cloning-data/design_check.py`)

## 5. Equipment

Computer with Python 3 or a plasmid-design application; text editor; calculator.

## 6. Safety

Simulation only — no organisms, no enzymes, no hazards. (When you later perform real digestion/ligation labs, your institution's biosafety and chemical-hygiene SOPs apply.)

## 7. Procedure / workflow

1. **Inspect the vector map.** Record total size, marker(s), MCS sites, priming sites.
2. **Scan the insert** for EcoRI/BamHI/HindIII/XhoI internal sites (script or manual).
3. **Choose the enzyme pair.** Justify with three criteria: unique in vector, absent in insert, directional.
4. **Design primers** that add the chosen sites (with 4–6 nt 5′ clamps for enzyme efficiency) to the 850 bp insert. Write the primer sequences.
5. **Plan the ligation** using the molar-ratio formula (below) for a 50 ng vector amount and 3:1 ratio.
6. **Design the diagnostic digest**: pick one enzyme pair that (a) cuts the final construct into ≥2 informative fragments and (b) gives a *different* pattern for empty vector.
7. **Predict everything in silico**: gel bands for (i) undigested construct, (ii) diagnostic digest, (iii) empty-vector digest.

**Molar-ratio formula:**

```text
ng insert = ng vector × (bp insert / bp vector) × (molar ratio desired)
```

## 8. Expected results

A complete, self-consistent design package: enzyme pair, primer table, ligation calculation, digest prediction table. There is **one best enzyme pair** given the insert's internal sites (the scripts will reveal it) — discovering why the others fail is the point.

## 9. Data tables to complete

| Item | Your answer |
|---|---|
| Vector size / marker / MCS sites | |
| Internal-site conflicts found | |
| Enzyme pair chosen + justification | |
| Forward primer (5′→3′) | |
| Reverse primer (5′→3′) | |
| Insert ng for 50 ng vector at 3:1 | |
| Diagnostic digest fragments (construct) | |
| Diagnostic digest fragments (empty vector) | |

## 10. Calculations

- Molar-ratio calculation (show work).
- Total expected construct size (vector + insert).
- Expected fragment sizes for the diagnostic digest.

## 11. Interpretation

- Why does the chosen pair enforce directionality?
- Which design error would produce *colonies on the plate but no correct clones*?

## 12. Troubleshooting (design-level)

| Symptom | Likely cause | Fix |
|---|---|---|
| Enzyme sites not unique | Internal site in insert | Alternative enzymes; Gibson instead |
| Frame broken at junction | Primer mis-design | Recheck frame/stop codon logic |
| Digest uninformative (one band) | Poor diagnostic choice | Pick asymmetric sites |

## 13. Post-lab questions

1. Why add 5′ clamp bases before restriction sites in primers?
2. Your insert contains one HindIII site. Give two alternative strategies.
3. What colony-PCR primer design would let you distinguish orientation without a digest?
4. Why is it useful to predict the *empty-vector* digest pattern too?

## 14. Viva questions

1. Define directional cloning.
2. What is the role of the 5′ clamp in primer design?
3. Which vector component determines colony selection here?

## Figures

<figure markdown>
![Anatomy of a cloning plasmid: origin of replication, selectable marker, multiple cloning site, promoter and terminator.](../assets/DIAGRAMS/plasmid_map.png)

*Figure - Anatomy of a cloning plasmid: origin of replication, selectable marker, multiple cloning site, promoter and terminator.*
</figure>

<figure markdown>
![The complete molecular-cloning workflow, from target-gene identification to sequence-confirmed recombinant construct.](../assets/DIAGRAMS/cloning_workflow.png)

*Figure - The complete molecular-cloning workflow, from target-gene identification to sequence-confirmed recombinant construct.*
</figure>


## 15. Instructor notes / answer key (summary)

- Correct pair: **EcoRI + HindIII** (BamHI is blocked by an internal site in the insert; XhoI lacks a distal mate for directionality in this design).
- Primer design must add 5′-clamp + EcoRI (forward) and 5′-clamp + HindIII + reverse-complement (reverse).
- 50 ng vector at 3:1 → insert ng = 50 × (850/4050) × 3 ≈ **31.5 ng**.
- Diagnostic digest (EcoRI+BamHI): construct → 1.9 kb + 2.15 kb; empty vector → single 3.2 kb.
- Full worked answers in the [Workbook](../guide/workbook.md).

## 16. Advanced challenge

Redesign the same construct with **Gibson Assembly**: write the 30-bp overlaps you would use, and state one scenario where Gibson is clearly the better choice here.

---

**Related resources:** [Lab workbook](../guide/workbook.md) · [Cheat sheet](../guide/cheat-sheet.md) · [Datasets](../downloads/datasets.md) · [Assessments](../assessment/index.md)

[Course home](../index.md)
