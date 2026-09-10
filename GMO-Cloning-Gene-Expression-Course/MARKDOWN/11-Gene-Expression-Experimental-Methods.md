# Module 11 — Gene-Expression Experimental Methods

**Level:** Intermediate → Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](10-Gene-Regulatory-Networks.md) · → [Next Topic](12-Data-Analysis.md)
> 🧪 Related Labs: [Lab 05](../LAB/Lab-05-Gene-Expression-Analysis.md) · [Lab 06](../LAB/Lab-06-Reporter-Gene-Analysis.md) · [Lab 07](../LAB/Lab-07-Spatial-Gene-Expression.md) · [Lab 08](../LAB/Lab-08-Computational-Gene-Expression.md) · 📊 Data: [Gene-expression data](../DATA/gene-expression-data/) · [Spatial data](../DATA/spatial-expression-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Cloning-Gene-Expression-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md)

---

## Learning objectives

1. For each method below, state: question answered, input, principle, workflow, output, strengths, limitations, controls, and interpretation.
2. Match method to biological question (resolution, quantitation, live vs endpoint).
3. Distinguish mRNA-level from protein-level readouts and explain why the difference matters.

---

## 1. Method matrix (quick reference)

| Method | Level | Where/When resolution | Quantitative? | Live? |
|---|---|---|---|---|
| RT-PCR | mRNA | none | semi | no |
| RT-qPCR | mRNA | none | yes (relative/absolute) | no |
| RNA-seq (bulk) | transcriptome | none (averaged) | relative | no |
| scRNA-seq | transcriptome | cell type (position lost) | relative (sparse) | no |
| Spatial transcriptomics | transcriptome | tissue spot/cell | relative | no |
| RNA-FISH / smFISH | mRNA | subcellular | absolute counts | no |
| In situ hybridization | mRNA | cell/tissue | semi | no |
| Reporter (GFP/lacZ/luc) | regulatory output | cell/tissue; live | semi–good | yes |
| Immunohistochemistry/IF | protein | subcellular | semi | no |
| Western blot | protein | none | semi | no |
| ELISA | protein | none | yes | no |

---

## 2. RNA methods

### 2.1 RT-PCR and RT-qPCR

- **Question:** is transcript X present? How much relative to a reference?
- **Input:** purified RNA (DNA-free); reverse transcription → cDNA.
- **Principle:** reverse transcription + PCR; qPCR monitors amplification in real time (SYBR Green intercalation or TaqMan probe hydrolysis).
- **Workflow:** RNA extraction & QC → DNase → RT → qPCR (technical triplicates) → Ct/Cq values → normalization → ΔΔCt analysis.
- **Output:** relative expression (fold change) or absolute copies (with standard curve).
- **Controls:**
  - **No-RT control** — detects genomic-DNA contamination.
  - **No-template control** — detects reagent contamination.
  - **Reference genes** (housekeeping) — validated as stable in the actual condition; multiple references recommended (e.g., *GAPDH/ACTB/18S* — but validate!).
  - **Inter-run calibrator** for cross-plate comparisons.
- **Common pitfalls:** primer-dimer (melt curves), reference-gene instability across treatments, efficiency ≠ 100% (ΔΔCt assumes ~2× per cycle), RNA degradation (3′:5′ bias).
- **Interpretation:** fold change is relative to your control; state the reference genes and the control condition explicitly.

### 2.2 Bulk RNA-seq

- **Question:** which transcripts, at what relative abundance, genome-wide?
- **Input:** RNA → library (fragmentation → cDNA → adapters → indexing).
- **Principle:** high-throughput short-read (or long-read) sequencing of cDNA; reads map to transcriptome; counts ∝ abundance.
- **Output:** count matrix → normalization (TPM for within-sample gene-level expression; DESeq2/edgeR-class models for between-condition testing on raw counts) → differential expression, pathway enrichment.
- **Controls/considerations:** biological replicates (≥3); batch structure (randomization, balanced design); strandedness; spike-ins optional; polyA vs total RNA (pre-mRNA inclusion).
- **Limitations:** averages over cells (heterogeneity masked — the problem scRNA-seq solves); low-abundance transcripts under-sampled; alternative splicing needs deeper depth/long reads.

---

## 3. Imaging-based methods

### 3.1 Fluorescence microscopy & reporters

- **Question:** where is a protein (fusion) or where is a regulatory element active (promoter-reporter)?
- **Principle:** genetically encoded fluorophores (GFP family) or immuno-stained fluorophores imaged by epifluorescence/confocal.
- **Controls:** non-transgenic/non-transfected background; spectral bleed-through controls; photobleaching awareness; for fusions — endogenous pattern comparison (in situ/IF).
- **Limitations:** fusion perturbation; autofluorescence; out-of-focus blur in thick tissue (confocal/light-sheet mitigate); maturation kinetics.

### 3.2 Immunohistochemistry / immunofluorescence (IHC/IF)

- **Question:** where is the *protein*?
- **Principle:** antibody binding (direct-labeled or secondary-labeled) → chromogenic or fluorescent signal.
- **Controls:** no-primary; isotype control; knockout/known-negative tissue; known-positive tissue; secondary-only.
- **Limitations:** antibody specificity varies (validate!); fixation/permeabilization artifacts; epitope masking; endogenous pigment/autofluorescence in some tissues.

---

## 4. RNA localization methods

### 4.1 In situ hybridization (ISH) — conceptual workflow

```text
Sample preparation (fixation, permeabilization)
      ↓
Probe design (antisense, labeled: DIG/fluor/hapten)
      ↓
Hybridization (probe base-pairs with target RNA in situ)
      ↓
Stringent washing (temperature/salt set specificity)
      ↓
Signal detection (chromogenic alkaline-phosphatase/NBT-BCIP,
   or fluorescence; RNAscope-class signal amplification)
      ↓
Imaging
      ↓
Spatial-expression interpretation
```

**Probe logic:**

- **Antisense probe** — complementary to the transcript → true signal.
- **Sense probe** — same sequence as the transcript → cannot base-pair specifically → *negative control*.
- **Specificity** — determined by probe length/region, hybridization stringency, and organism background; repeated elements must be masked in probe design.
- **Positive control** — a transcript with known, robust spatial pattern (validates the protocol and staging).

**Controls summary:** sense/no-probe (negative), known-marker probe (positive), staging validation, replicates across clutches/litters.

**Strengths/limits:** superb spatial mapping at endogenous expression; semi-quantitative at best; endpoint; probe-by-probe optimization; low-abundance transcripts need amplification strategies (RNAscope-class).

### 4.2 RNA-FISH / smFISH

- Single-molecule sensitivity via many short oligos per transcript → diffraction-limited spots = single transcripts.
- Absolute counts per cell; subcellular localization (e.g., nascent transcription sites, mRNA localization granules).
- Multiplexing (MERFISH/seqFISH-class) scales to hundreds–thousands of genes with barcoded sequential imaging — the bridge between ISH and spatial transcriptomics.

---

## 5. Genomic-scale methods

### 5.1 Single-cell RNA-seq (scRNA-seq) — conceptual

```text
Dissociated single-cell suspension
      ↓
Barcoding/capture (droplet or plate-based; UMI counting)
      ↓
Library preparation → sequencing
      ↓
Expression matrix (cells × genes, UMI counts)
      ↓
QC (filter empty droplets, low-quality/dying cells, doublets)
      ↓
Normalization → dimensionality reduction (PCA/UMAP)
      ↓
Clustering → cell-type annotation (marker genes)
      ↓
Differential expression per cluster;
   trajectory/pseudotime (developmental ordering)
```

- **Strengths:** unbiased cell-type discovery; developmental trajectories; rare populations.
- **Limitations:** dissociation loses spatial context; dropout/sparsity; dissociation biases (some cell types lyse); pseudo-time ≠ real time without additional anchors (RNA velocity, lineage tracing).
- **Controls/considerations:** batch design and integration; cell-count balance across conditions; ambient-RNA correction.

### 5.2 Spatial transcriptomics — conceptual

Two broad families:

- **Array-based** (e.g., Visium-class): tissue on a slide with spotted capture areas (~55 µm spots in the canonical system) — spots capture mRNA with spatial barcodes; after sequencing, each spot carries a spatially-resolved expression profile (spot ≈ several cells).
- **Imaging-based** (MERFISH/seqFISH+/cosMx-class): barcoded probes imaged in situ, iteratively decoded → single-cell/subcellular maps of hundreds of genes.

```text
Tissue section on capture surface
      ↓
Spatially barcoded capture (array)  OR  barcoded probe imaging
      ↓
Library prep → sequencing (array)  OR  image decoding (imaging)
      ↓
Spatially-resolved expression matrix
      ↓
Align to histology → tissue-region annotation
      ↓
Spatial patterns: gradients, domains, ligand–receiver pairs
```

- **Strengths:** keeps spatial context; connects histology with molecular state.
- **Limitations:** lower gene plex (array) or lower throughput (imaging); deconvolution needed when spots contain multiple cell types; resolution–plex trade-offs.

---

## 6. Choosing a method — decision guide

```text
Question: WHERE is it expressed? (one/few genes, endogenous)
      → ISH / RNA-FISH / IF (protein)

Question: WHERE + DYNAMICS?
      → reporter (known regulatory element) + ISH validation

Question: WHICH GENES define a cell type/region?
      → scRNA-seq (no coordinates) or spatial transcriptomics

Question: HOW MUCH over time, one/few genes?
      → RT-qPCR time course

Question: GENOME-WIDE, whole tissue, across stages?
      → bulk RNA-seq (+ scRNA/spatial for heterogeneity)
```

**Rule of thumb:** sequence/discover broadly → then *validate spatially and functionally* with targeted methods (ISH, reporter, perturbation).

---

## 7. Self-check questions

1. Your qPCR shows a 4-fold increase in gene X after treatment, but Western shows no protein change. Give three plausible explanations.
2. Why is the sense probe such a strong negative control — mechanistically?
3. A scRNA-seq cluster expresses two mutually exclusive marker genes. What could this mean (three possibilities)?
4. You need to test whether a candidate enhancer is active in the developing limb. Which method first, and which second for validation?
5. Why can spatial transcriptomics detect ligand–receiver pairs that scRNA-seq on dissociated cells cannot reliably infer?

---

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](10-Gene-Regulatory-Networks.md) · → [Next Topic](12-Data-Analysis.md)
