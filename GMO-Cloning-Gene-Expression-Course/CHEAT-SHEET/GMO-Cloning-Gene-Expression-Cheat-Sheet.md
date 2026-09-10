# Cheat Sheet — GMOs, Cloning & Gene Expression

**2–4 page revision guide** · [↑ Course Home](../README.md) · [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md) · [Assessment](../ASSESSMENT/MCQs.md)

---

## 1. Essential terminology

| Term | One-line definition |
|---|---|
| Genetic engineering | Deliberate, direct modification of genetic material using lab techniques |
| Recombinant DNA | DNA joined from >1 source into a propagatable molecule |
| Molecular cloning | Building + amplifying a defined DNA molecule in a host |
| GMO | Organism with lab-altered genetic material (definition is regulatory!) |
| Transgenic | Carries foreign (cross-species) DNA |
| Cisgenic | Carries same-species DNA |
| Gene-edited | Targeted editor (CRISPR etc.) made the change |
| Knockout / Knock-in | Gene inactivated / defined sequence inserted at a locus |
| Stable vs transient | Inherited vs fading (plasmid/integration vs transfection) |
| Expression cassette | promoter → 5′ UTR/RBS → CDS → terminator/polyA |

## 2. Cloning vocabulary

**Insert** (passenger) · **Vector** (vehicle) · **Backbone** (vector minus insert) · **ori** (replication origin; sets copy number) · **MCS** (multi-cloning site) · **Selectable marker** (cell survives only with vector) · **Screenable marker** (distinguishes clones visually) · **Fusion protein** (in-frame tag+protein) · **Shuttle vector** (two hosts) · **BAC/YAC** (100–300 kb / ~1 Mb capacity).

## 3. Vector components — what breaks without them

| Component | Missing → |
|---|---|
| ori | no propagation |
| Selectable marker | can't select transformants |
| MCS | insertion impractical |
| Promoter/RBS/Kozak | clone but no expression |
| Terminator/polyA | read-through / unstable transcripts |
| Reporter | expression invisible |

## 4. Restriction enzymes & ligase

- Recognition sites 4–8 bp, usually palindromic; **EcoRI** `G↓AATTC` (sticky 5′-AATT), **EcoRV** blunt, **BamHI** `G↓GATCC`, **HindIII** `A↓AGCTT`.
- **Sticky vs blunt** ends; **compatible ends** (BamHI/BglII → same overhang).
- **T4 DNA ligase** seals 5′P–3′OH nicks (ATP-dependent).
- **Dephosphorylation** of vector blocks self-ligation.
- **Insert:vector ratio** ~3:1 (molar) for sticky-end ligations (start point, not law).
- Methylation sensitivity can block some sites in lab *E. coli* DNA.

## 5. Cloning methods at a glance

| Method | Principle | Best for |
|---|---|---|
| Restriction–ligation | cut+anneal+ligate | single insert, directional |
| TA | Taq A-overhang ↔ T-vector | fast PCR capture |
| Blunt | flush-end ligation | no sites available |
| Gibson | exonuclease chew-back + overlap anneal + fill + seal | seamless multi-fragment |
| Golden Gate | Type IIS → designer 4-bp overhangs, one-pot | modular, multiplex |
| Gateway | att-site recombination (entry → destination) | one entry → many vectors |

**Golden rule:** Gibson/Golden Gate = design-driven addressing; restriction = site-driven; Gateway = recombination-driven.

## 6. Selection vs screening vs validation

```text
Selection      → only vector-bearing cells grow (antibiotic/auxotrophy)
Screening      → which colonies have the RIGHT vector (blue-white, colony PCR)
Validation     → prove structure (digest) then sequence (Sanger), then function
```

- **Blue-white:** white = insert-disrupted lacZα (candidate, not proof).
- **Colony PCR:** vector+insert primer combo = orientation readout.
- **Diagnostic digest:** fragments must match map AND sum to plasmid size.
- **Sanger:** junctions + full insert coverage; final word.

## 7. Reporter genes

| Reporter | Signal | Needs substrate? | Best at |
|---|---|---|---|
| GFP | fluorescence ~508 nm | no (needs O₂) | live spatial imaging |
| mCherry/RFP | red fluorescence | no | dual-color with GFP |
| lacZ | blue (X-gal) | yes | fixed-tissue histology |
| Luciferase (firefly) | photons | luciferin+ATP | quantitative dynamics |

**Controls:** promoterless & empty vector; positive promoter; motif mutant; normalization (dual-luciferase / co-transfection). **Caveat:** reporter = regulatory-sequence behavior, not necessarily endogenous gene behavior.

## 8. GMO terminology recap

Transgenic ≠ cisgenic ≠ gene-edited. **The reagent is transient; the edit can be stable.** SCNT (Dolly) = cloning, no new DNA. Random integration (classic transgenesis) vs targeted edit (CRISPR era).

## 9. CRISPR terminology

- **sgRNA** ~20-nt guide + scaffold; **PAM** (SpCas9: NGG) required for recognition.
- **DSB → repair:** **NHEJ** = indels = knockout; **HDR** = donor template = knock-in/correction.
- **Base editors** (C→T, A→G) and **prime editors** = no DSB.
- **dCas9** = binding-only chassis → **CRISPRa** (activate) / **CRISPRi** (repress, e.g., KRAB).
- Pitfalls: off-targets, mosaicism (F0), in-frame indels escaping knockout.

## 10. Developmental gene regulation

- Differential gene expression = same genome, different transcriptional programs.
- **Cell fate → determination → differentiation**; potency: totipotent → pluripotent → multipotent.
- **Morphogen gradient + thresholds** (French-flag): Shh (neural tube DV, limb ZPA), Bicoid (Drosophila A–P), BMP (dorsal ectoderm), Wnt (axis), RA (hindbrain/limb PD).
- **GRN motifs:** positive feedback (lock fate), mutual repression (sharp borders), feed-forward (filter), lateral inhibition (salt-and-pepper, Notch).
- Landmark genes: **Hox** (colinear A–P identity), **Pax6** (eye field), **Shh**, **Wnt1**, **myoD** (myogenic master — sufficiency caveat).

## 11. Spatial vs temporal expression

| Question | Method of choice |
|---|---|
| Where (endogenous mRNA)? | ISH / RNA-FISH |
| Where (protein)? | IHC / IF |
| Where + dynamics? | Reporter (GFP/luc) |
| How much over time (few genes)? | RT-qPCR (ΔΔCt) |
| Which genes define a cell type? | scRNA-seq |
| Which genes define a region? | spatial transcriptomics |

**Gradient** = continuous concentration field; **domain** = bounded region. Gradients inform; domains execute.

## 12. Experimental-method quick table

| Method | Level | Resolution | Quantitative? |
|---|---|---|---|
| RT-qPCR | mRNA | none | yes (relative) |
| Bulk RNA-seq | transcriptome | none (mean) | relative |
| scRNA-seq | transcriptome | cell (position lost) | relative, sparse |
| Spatial transcriptomics | transcriptome | spot/cell | relative |
| smFISH | mRNA | subcellular | absolute counts |
| ISH | mRNA | cell/tissue | semi |
| IHC/IF | protein | subcellular | semi |
| Reporter | regulatory output | cell/tissue, live | semi–good |

## 13. Data-analysis concepts

- **ΔΔCt:** ΔCt = Cq(target) − Cq(ref); FC = 2^(−ΔΔCt). Stats on ΔCt, not FC.
- **RNA-seq:** normalize (CPM/size factors) → model → **FDR** (BH). |log2FC| with FDR filter; beware low counts.
- **scRNA:** QC (library, genes, doublets) → normalize/log → PCA → cluster → **marker annotation**. Dropout ≠ absence.
- **Spatial:** matrix + coordinates → region markers → gradient test (correlation with distance).
- **Heatmaps:** z-score genes to compare *patterns* regardless of magnitude.
- Report: n, normalization, test, effect size, version. Always.

## 14. Important comparisons (rapid-fire)

- Transgenesis **adds**; editing **changes**. 
- Selection **enriches populations**; screening **classifies individuals**; validation **proves identity**.
- Gradient **informs**; domain **executes**.
- Fluorescence **spatial**; luminescence **quantitative**.
- NHEJ **breaks**; HDR **writes**.
- Bulk **averages**; single-cell **resolves types**; spatial **resolves places**.
- CRISPRa tests **sufficiency**; CRISPRi/knockout tests **necessity**.

## 15. Common exam mistakes

1. Calling any transgenic organism a "clone" (or vice versa — Dolly wasn't transgenic).
2. Reading colony count as correct-clone count (screening is separate!).
3. Blue colony = always empty / white = always correct (exceptions exist).
4. Confusing PAM (genomic side) with protospacer (guide-target region).
5. Saying CRISPR "inserts a gene" by default (NHEJ knocks out; knock-ins need HDR/donors or editors).
6. ΔΔCt applied to unstable reference genes.
7. Interpreting a reporter domain as the endogenous pattern without ISH validation.
8. Confusing gradient (continuous) with domain (bounded).
9. Treating dropout in scRNA-seq as biological absence.
10. Claiming an enhancer is "necessary" from a reporter (sufficiency only).
11. Summing digest fragments is skipped → rearranged plasmids pass unnoticed.
12. Confusing cis-regulatory elements (on the DNA) with trans-acting factors (the proteins that bind them).

---

*Print tip: this file paginates to ~4 pages at A4 in the generated PDF. Related: [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md) · [References](../REFERENCES.md)*
