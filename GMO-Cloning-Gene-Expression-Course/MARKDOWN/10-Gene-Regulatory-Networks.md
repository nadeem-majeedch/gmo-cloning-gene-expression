# Module 10 — Gene Regulatory Networks

**Level:** Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](09-Spatial-and-Temporal-Gene-Expression.md) · → [Next Topic](11-Gene-Expression-Experimental-Methods.md)
> 🧪 Related Labs: [Lab 05](../LAB/Lab-05-Gene-Expression-Analysis.md) · [Lab 08](../LAB/Lab-08-Computational-Gene-Expression.md) · 📊 Data: [Gene-expression data](../DATA/gene-expression-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Cloning-Gene-Expression-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md)

---

## Learning objectives

1. Define the components of a gene regulatory network (GRN): TFs, cis-regulatory modules, signaling inputs.
2. Read and reason about network motifs: feedback, feed-forward, cross-repression, incoherent feed-forward.
3. Explain enhancer–promoter communication and the role of chromatin in development.
4. Place transcriptomic data (Modules 11–12) inside network logic: inference and its limits.

---

## 1. The parts

- **Transcription factors (TFs):** sequence-specific DNA-binding proteins with activator or repressor domains. Combinatorial control: few TF families (Homeodomain, bHLH, bZIP, nuclear receptor, Zinc finger, MADS...) → enormous regulatory diversity.
- **Cis-regulatory modules (CRMs):** clusters of TF binding sites — **promoters** (proximal, initiation) and **enhancers/silencers** (distal, modular). Each CRM integrates its bound TFs → activation/repression output.
- **Signaling inputs:** pathways (Module 8) modify TF activity (SMADs, β-catenin/TCF, Gli, NICD enter the nucleus) — extracellular state becomes transcriptional state.
- **Chromatin state:** accessibility (ATAC/DNase), histone marks, DNA methylation, 3D contacts — permissive vs silent configuration of each CRM.

```text
        extracellular signal
                │
                ▼
        signaling pathway (e.g., Wnt)
                │
                ▼ active TF (β-catenin+TCF)
   ┌────────────────────────────────┐
   │  cis-regulatory module         │
   │  sites: [TF-A][TF-B][TCF][cof] │
   └──────────────┬─────────────────┘
                  ▼
             gene expression
                  │
        feeds back on network
```

*Figure 10.1 — A CRM as an information-integration device.*

## 2. Network motifs and what they do

| Motif | Wiring | Functional consequence | Example |
|---|---|---|---|
| **Positive autoregulation** | TF activates its own gene | Locks in fate; persistence after signal gone | MEF2/myogenic maintenance |
| **Negative autoregulation** | TF represses its own gene | Homeostasis; faster response times | Many repressors |
| **Mutual repression (toggle)** | A ⊣ B, B ⊣ A | Bistability; sharp fate borders | Gt/Kni in Drosophila; neuronal vs glial switches |
| **Positive feedback pair** | A → B, B → A | Stable commitment | Cell-fate stabilization circuits |
| **Feed-forward loop (coherent)** | A → B, A → C, B → C | Sign persistence; noise filtering | Common in developmental GRNs |
| **Incoherent feed-forward** | A → C, A → B ⊣ C | Pulse/adaptation | Signaling response dynamics |
| **Lateral inhibition** | Delta–Notch between neighbors | Salt-and-pepper fate patterns | Neurogenesis; vulval lineages |

## 3. Enhancer–promoter communication

Enhancers act over large genomic distances; the mechanisms debated and likely multiple:

- **Looping/contact models:** enhancer–promoter physical contact (chromatin loops; TADs organize who can contact whom).
- **Trackability / condensate models:** transcriptional condensates phase-separate components.

Whatever the mechanism, two experimental truths matter:

1. **TAD boundaries constrain enhancer action** — moving an enhancer across a boundary changes its targets (relevant to disease: structural variants can create *neo-enhancers* near oncogenes).
2. **Enhancer activity is context-dependent** — the same enhancer drives different genes in different tissues (Mammalian enhancer–gene maps e.g., from FANTOM5/GeneHancer resources).

## 4. Chromatin and developmental regulation

- **Histone marks (conceptual):** H3K4me1 with H3K27ac = active enhancer; H3K27me3 = Polycomb-repressed; H3K9me3 = heterochromatin; H3K4me3 = active promoter.
- **DNA methylation:** CpG methylation generally correlates with stable repression; germline/imprinting dynamics; demethylation during early development.
- **Bivalency:** promoters marked with both H3K4me3 and H3K27me3 ("poised") are common in stem/precursor cells — ready for either lineage choice.
- **Pioneer factors:** TFs (e.g., FoxA, Pou5f1/Oct4-class) that bind nucleosomal DNA and open chromatin — why some TFs reprogram cell identity.

## 5. From data to networks — the inference loop

```text
   Expression data (scRNA-seq / time course)
   + chromatin data (ATAC-seq, ChIP for TFs/marks)
   + motif information
            │
            ▼
   Infer candidate edges (TF → target):
      co-expression, motif enrichment in ATAC peaks,
      perturbation signatures (KO/KD, CRISPR screens)
            │
            ▼
   Prioritize edges → test by perturbation + reporter
   (Module 5 constructs; CRISPRi enhancer tests)
            │
            ▼
   Validate network function: does perturbing a hub
   change the predicted downstream fates?
```

**Caveats:** co-expression is not causation; inferred edges are hypotheses; the gold standard remains *perturbation* (genetic or pharmacological) with readout at the target level.

## 6. Worked example — a small developmental GRN

**Specification of myoblasts (simplified):**

```text
   signaling cues (Wnt/Shh/FGF from somite patterning)
            │
            ▼
   Pax3/Pax7  ──activates──▶  Myf5 / Myod  (commitment)
            ▲                       │
            │  cross-positive       ▼
            └────────────  Myogenin (differentiation)
                                    │
                                    ▼
                        muscle structural genes (Actc1, Myh…)
```

- Pax3/Pax7 maintain the progenitor state; Myf5/Myod drive commitment; myogenin executes differentiation. Each arrow is supported by knockout/overexpression literature — and each was tested *by perturbation*, not co-expression alone.

## 7. Self-check questions

1. Why does mutual repression produce sharp boundaries while a single activator gradient does not?
2. What experimental design distinguishes a true feed-forward loop from a coincidental co-expression cluster?
3. Why can an enhancer be validated by CRISPRi more cleanly than by reporter assay? What does the reporter assay still offer?
4. Explain bivalency: why is a "poised" promoter useful in a multipotent cell?
5. In the myogenic network above, which edges would you test first by perturbation, and why?

---

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](09-Spatial-and-Temporal-Gene-Expression.md) · → [Next Topic](11-Gene-Expression-Experimental-Methods.md)
