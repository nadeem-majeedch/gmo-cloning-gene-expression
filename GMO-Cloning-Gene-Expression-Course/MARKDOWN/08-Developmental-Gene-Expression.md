# Module 8 — Developmental Gene Expression

**Level:** Intermediate → Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](07-Genome-Editing-and-CRISPR.md) · → [Next Topic](09-Spatial-and-Temporal-Gene-Expression.md)
> 🧪 Related Labs: [Lab 05](../LAB/Lab-05-Gene-Expression-Analysis.md) · [Lab 07 — Spatial Gene Expression](../LAB/Lab-07-Spatial-Gene-Expression.md) · 📊 Data: [Gene-expression data](../DATA/gene-expression-data/) · [Spatial data](../DATA/spatial-expression-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Cloning-Gene-Expression-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md)

---

## Learning objectives

1. Explain differential gene expression as the cellular basis of development.
2. Define cell fate, differentiation, determination, commitment, and potency.
3. Describe how morphogen gradients and signaling pathways pattern tissues.
4. Recognize the major model organisms and the landmark genes used to study them.
5. Read a simple gene-regulatory network and reason about feedback and cross-regulation.

---

## 1. Differential gene expression

Every nucleated cell in a multicellular organism carries (essentially) the same genome. A neuron, a hepatocyte, and a lymphocyte differ because they **transcribe and translate different subsets** of that genome — and because their chromatin states, transcription-factor milieus, and signaling histories differ.

```text
    Zygote (one genome)
        │
        ▼  divisions, asymmetric cues
   ┌────┴─────┐
   ▼          ▼
 ectoderm   mesendoderm        ← different genes ON in each
   │            │                (differential transcription)
   ▼            ▼
 neurons    muscle, gut, blood ← different genes ON again
```

*Figure 8.1 — Development as progressive restriction of gene-expression programs.*

**Key corollary:** developmental biology is largely the study of **which genes are on, where, when, and why** — which is why the cloning/reporter modules and the expression-analysis modules converge here.

## 2. Core vocabulary

| Term | Definition | Example |
|---|---|---|
| **Cell fate** | What a cell (or its descendants) will normally become | "neural plate border fate" |
| **Determination / commitment** | Fate is fixed even if transplanted to a new environment | Presumptive somite committed after a specific stage |
| **Differentiation** | Acquisition of specialized structure/function | Myoblast → myotube |
| **Potency** | Range of possible fates | Totipotent (zygote) → pluripotent (ESC) → multipotent (HSC) → unipotent |
| **Differential gene expression** | Same genome, different transcriptional outputs | Hox expression domains |
| **Master regulatory gene** | A gene whose product (usually a TF) can initiate/reprogram a whole program | *myoD* in muscle (Davis, Weintraub & Lassar, 1987), Pax6 in eye development |

**Master regulators caveat:** "master" describes the experimental result (forced expression induces the program), not necessarily an in-vivo developmental mechanism. *myoD* converts fibroblasts to myoblasts — a landmark sufficiency result — but endogenous muscle specification involves pax3/pax7, signaling inputs, and chromatin context.

---

## 3. Morphogens and gradients

**Morphogen concept (Turing 1952; Wolpert's "French flag" model, 1969):** a signaling molecule produced by a localized source diffuses, creating a concentration gradient; cells respond according to concentration thresholds, producing different fates at different distances.

```text
  Source                                Sink
  ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓
  ░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░
  ──────────────── concentration ────────▶
  Fate A  Fate A  Fate B  Fate B  Fate C  Fate C
  (high)  (high)  (med)   (med)   (low)   (low)

  ↑ thresholds define boundaries (French-flag model)
```

*Figure 8.2 — Morphogen gradient and threshold responses.*

Real mechanisms include diffusion with degradation, planar transcytosis, and cytonemes — the details differ by system; the *threshold-response* logic is shared.

**Landmark examples:**

- **Shh (Sonic hedgehog)** — ventral neural tube: notochord/floor-plate-derived Shh induces ventral neuronal fates (V3 interneurons, motor neurons, V2, V1…) at decreasing concentrations/durations (dorsal–ventral patterning).
- **Shh** — limb: ZPA (zone of polarizing activity) gradient patterns anterior–posterior digit identity.
- **BMP gradient** — dorsal neural tube; BMP inhibition by organizer-secreted antagonists (Noggin, Chordin, Follistatin) is central to neural induction.
- **Wnt gradient** — A–P patterning, segmentation; canonical Wnt/β-catenin specifies dorsal organizer in zebrafish/xenopus.
- **Drosophila Bicoid** — maternal mRNA localized anteriorly; translated into an anterior–posterior protein gradient activating *hunchback* and other zygotic targets (Nüsslein-Volhard & Wieschaus put the segmentation hierarchy together in their 1980 Nature mutagenesis screen; Nobel 1995).
- **Retinoic acid** — rostrocaudal patterning of the hindbrain and limb proximodistal patterning (endogenous metabolite, graded by synthesizing (RALDH) and degrading (CYP26) enzymes).

---

## 4. Signaling pathways (the recurring cast)

| Pathway | Ligand class | Canonical signal transduction (conceptual) | Developmental roles (examples) |
|---|---|---|---|
| **Wnt/β-catenin** | Wnts | Receptor (Frizzled+LRP5/6) → inhibit destruction complex → β-catenin enters nucleus → TCF/LEF targets | Axis formation, segment polarity, stem-cell compartments |
| **Hedgehog** | Shh/Ihh/Dhh | Ptched inhibition → Smoothened → Gli activators/repressors | Neural-tube DV patterning; limb AP; somite sclerotome |
| **TGF-β / BMP / Nodal / Activin** | TGF-β superfamily | Type I/II receptor serine-threonine kinases → SMADs → nucleus | Mesoderm induction (Nodal), DV ectoderm patterning (BMP), amnion/chorion |
| **Notch** | Delta/Jagged | Cell-contact-dependent; cleaved NICD → RBPJ targets | Lateral inhibition (neurogenesis), somite boundaries, vascular tip cells |
| **FGF** | FGFs | RTK → MAPK/PI3K/PLCγ | Mesoderm migration, limb bud outgrowth (AER), neural induction contexts |
| **Retinoic acid** | Retinoic acid | Nuclear receptors (RAR/RXR) → direct gene regulation | Hindbrain/caudalization; limb PD patterning; somite |
| **JAK/STAT, Hippo, YAP/TAZ** | Cytokines/mechanical |STAT/dimeric TFs; mechanotransduction | Growth control, regeneration, organ size |

These pathways' outputs converge on **cis-regulatory elements** (Module 10); a cell's *combinations* of active pathways — its "positional information" — drive fate decisions.

---

## 5. Model organisms — who does what best

| Model | Strengths for developmental genetics | Classic tools/genes |
|---|---|---|
| ***Drosophila melanogaster*** | Forward genetics at scale; short generation; segmental body plan | Bicoid/Nanos/Caudal; gap/pair-rule/segment-polarity genes; Hox (ANT-C/BX-C); Ubx/abd-A |
| ***C. elegans*** | Invariant cell lineage (Sulston); apoptosis genetics; RNAi uptake | *lin-4/let-7* (miRNAs), programmed cell death genes (ced-3/4/9), Notch lateral-inhibition |
| ***Danio rerio*** (zebrafish) | External transparent development; large clutches; forward screens; live imaging | *no tail* (ntl/Tbx6), *pax2.1/no isthmus*, shh (somites/floor plate), *spadetail* |
| ***Mus musculus*** (mouse) | Mammalian genetics; ES-cell knockouts; conditional alleles | Hox clusters, Pax6 (*Small eye*), Shh, Wnt1, Fgf8, Cre-lox systems |
| ***Arabidopsis thaliana*** | Plant development; genetics; short life cycle | *WUSCHEL/CLAVATA* (stem-cell niche), *KNOX* genes, *STM (shootmeristemless)*, *LFY*, ABC-floral model (MADS-box genes) |

*(Gene names are italicized for genes, roman for proteins; different conventions apply in different communities — e.g., Drosophila lowercase for recessive alleles.)*

---

## 6. Landmark genes and what they taught

- **Hox genes** — conserved colinear clusters specifying A–P identity (Lewis 1978; McGinnis & Krumlauf). **Colinearity:** 3′ genes expressed anterior/early; 5′ posterior/late. Disruption → homeotic transformations (antennapedia legs where antennae should be).
- **Pax6** — eye-field specification, conserved from flies (*eyeless*) to humans; ectopic expression makes ectopic eyes in Drosophila (Halder, Callaerts & Gehring, 1995).
- **Sonic hedgehog** — morphogen for neural tube/limb (above).
- **Wnt1** — midbrain/hindbrain boundary; canonical Wnt workhorse.
- **myoD** — master-regulator sufficiency for myogenesis (above).
- **Bicoid** — first morphogen with defined molecular identity (maternal mRNA gradient).

---

## 7. Gene regulatory networks — first pass

A **gene regulatory network (GRN)** is the graph of transcription factors, signaling components, and cis-regulatory elements that specifies a fate or process.

```text
        Maternal inputs (Bcd/Nos)
                 │
                 ▼
        Gap genes (Hb, Kr, Gt, Kni)
                 │  (cross-regulation sharpens boundaries)
                 ▼
        Pair-rule genes (eve, ftz, hairy)
                 │
                 ▼
        Segment-polarity genes (en, wg, hh)
                 │
                 ▼
        Hox genes (segment identity)
                 │
                 ▼
        Terminal target genes → differentiated cell types
```

*Figure 8.3 — Drosophila segmentation GRN hierarchy. Each level feeds the next; cross-regulation within levels sharpens domains.*

GRN reasoning rules:

- **Positive feedback** locks a fate in (self-maintaining TF expression).
- **Negative feedback** creates oscillations/refinement (Notch lateral inhibition; somite clock).
- **Cross-repression** creates sharp boundaries (Gt/Kni mutual repression; eve/frtz).
- **Feed-forward loops** filter transient inputs.

---

## 8. Self-check questions

1. A cell transplanted from a neural-tube ventral region to a dorsal region *after stage X* still becomes a motor neuron. What property does this illustrate, and when did it arise?
2. Why does a *bicoid* null mother produce embryos without heads — and what does adding anterior bicoid mRNA do (cite the classic result)?
3. Name the pathway and the cis-regulatory logic that makes Notch signaling a "lateral inhibition" device.
4. Why is *myoD* called a master regulator, and what is the caveat to that title?
5. Sketch the DV neural-tube fates as a function of Shh concentration and duration; where do V3, motor neurons, V2, V1 sit?

---

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](07-Genome-Editing-and-CRISPR.md) · → [Next Topic](09-Spatial-and-Temporal-Gene-Expression.md)
