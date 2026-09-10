# Module 15 — Advanced Topics

**Level:** Advanced / Research-oriented (MS and advanced BS)

---

## 15.1 Enhancer–promoter interactions and 3D genome

- **TADs (topologically associating domains):** self-interacting chromatin regions constraining enhancer search space; boundaries marked by CTCF/cohesin.
- **Loops and enhancer hubs:** CTCF-anchored loops; enhancer clusters contacting multiple promoters; alternation with transcriptional condensate models.
- **Technologies (conceptual):** Hi-C/3C-family for contact maps; Capture-C/4C for locus-specific; ChIA-PET/HiChIP for TF/histone-mark-associated contacts; PLAC-seq/H3K4me3-linked.
- **Disease relevance:** structural variants, enhancer hijacking (e.g., oncogene activation by relocated enhancers), neo-loops.
- **Experimental entry point for students:** CRISPRi of a candidate enhancer + nascent RNA readout (PRO-seq) tests *transcriptional* impact directly.

## 15.2 Chromatin accessibility and epigenetic regulation

- **ATAC-seq** (and DNase-seq): transposase/endo-nuclease accessibility → open-chromatin map; footprints hint at bound TFs.
- **ChIP-seq / CUT&RUN / CUT&Tag:** histone marks and TF occupancy; H3K27ac for active enhancers, H3K4me1 primed enhancers, H3K4me3 active promoters, H3K27me3 Polycomb-repressed, H3K9me3 heterochromatin.
- **DNA methylation:** bisulfite sequencing; CpG-island promoters; imprinting control regions; global hypomethylation/hypermethylation dynamics in development and cancer.
- **Bivalency in development:** stem/precursor cells keep lineage genes poised (H3K4me3+H3K27me3) — commitment resolves the duality.

## 15.3 Super-enhancers and transcriptional condensates

- **Super-enhancers:** dense clusters of enhancers marked by exceptionally high H3K27ac/BRD4/Mediator occupancy; often control identity genes (e.g., pluripotency loci, lineage-defining genes).
- **Condensate model:** multivalent interactions among TFs/coactivators/RNAPII form phase-separated transcriptional compartments — a current, still-debated framework (state it as such).
- **Sensitivity:** SE-associated genes are exceptionally sensitive to transcriptional perturbation (e.g., BRD4 inhibition) — therapeutic relevance.

## 15.4 Transcriptional bursting and noise

- RNAPII transcription is intermittent in many genes — bursts of initiation separated by refractory periods; promoter-proximal pausing and enhancer dynamics shape bursting.
- Consequences: cell-to-cell variability in isogenic populations; noise shaping developmental robustness (and its limits).
- Measurement: live imaging of MS2/MCP-class stem-loop reporters, single-molecule RNA-FISH distributions (burst size/frequency inference).

## 15.5 Single-cell heterogeneity and trajectories

- **States vs types:** continuous state variation within a "type"; cell-cycle and stress signatures confound clustering.
- **Pseudotime:** ordering cells along transcriptional similarity; RNA velocity (spliced/unspliced ratios) adds directionality — developmental dynamics from static snapshots.
- **Lineage inference:** mitochondrial/CRISPR barcode lineage tracing; phylogenetic reconstruction of fate decisions.
- **Caveats:** pseudotime ≠ chronological time; velocity models assume splicing kinetics stationary within the sample.

## 15.6 Spatial transcriptomics — frontiers

- Subcellular-resolution platforms; whole-organism-scale atlases (e.g., developing embryo maps).
- **Deconvolution:** spot-level data mixing cell types → infer proportions using scRNA references.
- **Cell–cell communication inference:** ligand–receptor co-localization frameworks (e.g., neighboring-domain analysis) — hypothesis-generating.
- **Integration tasks:** aligning scRNA with spatial maps; mapping dissociated atlases back onto anatomy.

## 15.7 Synthetic gene circuits

- **Motifs to circuits:** toggle switches, repressilators, AND-gate promoters, band-pass filters.
- **Mammalian tools:** inducible systems (Tet-On/Off), recombinase logic (Cre/Flp), synNotch (custom ligand → transcriptional program).
- **Design constraints:** burden, orthogonality of parts, insulation, evolutionary stability.
- **Applications:** cell therapies (synNotch-based recognition), biosensors, developmental-pattern engineering (reaction–diffusion-inspired circuits).

## 15.8 Conditional and tissue-specific expression systems

| System | Logic | Use |
|---|---|---|
| **Cre-loxP** | Site-specific recombination at loxP sites; tissue-specific Cre driver × floxed allele | Conditional knockouts/knock-ins (mouse standard) |
| **Flp-FRT** | Analogous to Cre-lox | Complementary labeling/inversion |
| **Dre-rox** | Orthogonal recombinase pair | Multiplex logic |
| **Tet-On/Off** | Doxycycline-controlled transactivator | Temporal control in cells/animals |
| **Gal4/UAS (fly, zebrafish)** | Yeast TF drivers expression from UAS | Tissue-specific driver lines; enhancer trap collections |
| **GAL4-ER² / heat-shock promoters** | Ligand/temperature gating | Inducible developmental studies |

- **Intersectional strategies:** combining Cre + Flp (or split recombinases) restricts expression to overlapping domains — precision in dense tissues.

## 15.9 CRISPR beyond knockout

- **CRISPRa:** dCas9-VP64/p65/Rta-class or dCas9-SunTag recruit activators to promoters → targeted up-regulation (without genome change) — ideal for testing sufficiency.
- **CRISPRi:** dCas9-KRAB represses transcription (chromatin-based silencing) — ideal for testing necessity, especially of enhancers (CRISPRi of enhancers affects linked promoters with less steric hindrance than promoter targeting).
- **Base editing:** CBE (C→T), ABE (A→G), plus newer CGBE/GBE variants — DSB-free single-base edits; bystander-edit and off-target deamination remain key caveats.
- **Prime editing:** nickase + reverse transcriptase + pegRNA — search-and-replace edits (all 12 base changes, small indels) without donor templates; efficiency locus- and cell-dependent.
- **Multiplex engineering:** multiple sgRNAs (Cas12a processing arrays; tRNA/ribozyme-flanked guides) — pathways, polygenic traits, combinatorial screens.
- **Epigenome editing:** dCas9-DNMT3A/TET1 — targeted methylation changes; memory of epigenetic edits varies.

## 15.10 Research-planning checklist (synthesis)

```text
1. QUESTION: mechanistic, specific, falsifiable
2. SYSTEM: model organism / cell type — justified by the question
3. READOUT: matches the question's resolution (space? time? quantitation?)
4. PERTURBATION: knockout vs knockdown vs overexpression vs CRISPRi/a — necessity vs sufficiency
5. CONTROLS: genetic (wild-type, rescue), technical (probe/stain), staging, batch
6. VALIDATION: independent method (ISH validates scRNA; Western validates IF...)
7. QUANTIFICATION: pre-registered plan (what counts as a positive)
8. STATISTICS: n, test, FDR — before data collection
9. ETHICS/BIOSAFETY: approvals, containment, welfare
10. REPRODUCIBILITY: code/data sharing, versioned reagents
```

---

## Figures

<figure markdown>
![Base editing and prime editing modify DNA without a double-strand break.](../assets/DIAGRAMS/base_prime_editing.png)

*Figure - Base editing and prime editing modify DNA without a double-strand break.*
</figure>

<figure markdown>
![A developmental gene-regulatory network cascade linking signaling, transcription factors and terminal target genes.](../assets/DIAGRAMS/grn_cascade.png)

*Figure - A developmental gene-regulatory network cascade linking signaling, transcription factors and terminal target genes.*
</figure>


## Self-check (integrative) questions

1. Design a CRISPRi experiment to test whether a candidate enhancer drives *myod* expression in somites — include the readout and controls.
2. Why does RNA velocity need spliced *and* unspliced counts, and what assumption could break it in a developmental sample?
3. A structural variant moves a limb enhancer 500 kb closer to an oncogene. Predict the consequence and name the technology that would have detected the new loop.
4. Explain how synNotch differs conceptually from a Tet-On system (input → output mapping).
5. Which two technologies from this module would you combine to build a tissue-specific, temporally inducible reporter in zebrafish? Sketch the cross.
---

## What you should know

Review the learning objectives at the top of this module and the self-check or quick-check questions above. When you can meet every objective unaided, you are ready to continue.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) questions for these topics.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [laboratory overview](../labs/index.md).

[<- Ethics, Biosafety and Regulation](../modules/14-Ethics-Biosafety-and-Regulation.md) &middot; [Course home](../index.md)
