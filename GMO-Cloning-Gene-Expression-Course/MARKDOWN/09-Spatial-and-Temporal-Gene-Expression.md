# Module 9 — Spatial and Temporal Gene Expression

**Level:** Intermediate → Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](08-Developmental-Gene-Expression.md) · → [Next Topic](10-Gene-Regulatory-Networks.md)
> 🧪 Related Labs: [Lab 07 — Spatial Gene Expression](../LAB/Lab-07-Spatial-Gene-Expression.md) · [Lab 08 — Computational Gene Expression](../LAB/Lab-08-Computational-Gene-Expression.md) · 📊 Data: [Spatial data](../DATA/spatial-expression-data/) · 📝 [Assessment](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Cloning-Gene-Expression-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Cloning-Gene-Expression-FAQs.md)

---

## Learning objectives

1. Distinguish **where** (spatial), **when** (temporal), and **where+when** (spatiotemporal) expression, and state why each axis matters.
2. Define tissue-specific, cell-type-specific, and developmental-stage-specific expression.
3. Interpret expression gradients and domains in real developmental contexts.
4. Choose methods that resolve space vs time appropriately (bridge to Modules 11–12).

---

## 1. Three axes of one question

Every gene-expression statement should locate itself on three axes:

```text
   SPATIAL    —  where in the organism/tissue/cell?
   TEMPORAL   —  when in development/cell cycle/response?
   QUANTITATIVE — how much, relative to what?
```

**Why the distinction matters:** a bulk RNA-seq of a whole embryo integrates over space and time. It can say "gene X rises at stage 12" but cannot say "gene X turns on in the notochord at stage 12, 20 minutes after notochord fate is specified." Different questions require different resolutions.

| Concept | Question answered | Example |
|---|---|---|
| **Spatial expression** | Where is the gene expressed? | *shh* in floor plate/notochord; *eve* stripes in Drosophila embryo |
| **Temporal expression** | When is it expressed? | *myoD* up-regulation at myogenic commitment |
| **Spatiotemporal** | Where and when, jointly? | *pax6* in eye field from 8-somite stage onward |
| **Tissue-specific** | Restricted to a tissue | insulin in β-cells |
| **Cell-type-specific** | Restricted to a cell type within a tissue | motor-neuron markers within spinal cord |
| **Stage-specific** | Restricted to a developmental window | *hunchback* early before cellularization |
| **Expression gradient** | Continuous concentration change across space | Bicoid A–P gradient; Shh DV gradient |
| **Expression domain** | Sharply bounded region of expression | *eve* stripe 2; *engrailed* stripes |

---

## 2. Gradients vs domains — two geometries

```text
  GRADIENT (continuous)                DOMAIN (bounded)
  conc.                                conc.
   ▲  ┌──╮                              ▲
   │ ╱    ╲                             │      ┌────────┐
   │╱      ╰──╮                         │      │        │
   │          ╰───╮                     │ ─────┘        └─────
   └───────────────▶ position          └────────────────────▶ position
   response follows thresholds         response is binary, region-limited
```

*Figure 9.1 — Gradients carry positional information continuously; domains are discrete regions (often shaped by cross-regulation on top of gradients).*

Biologically, gradients usually *inform*, domains usually *execute*: the Shh gradient informs, the sharply-bounded *olfm*/*nkx2.2*/*pax6* domains of the neural tube execute.

---

## 3. Spatiotemporal thinking in real examples

### 3.1 Drosophila anterior–posterior axis

- **Maternal stage:** *bicoid* mRNA localized anteriorly → Bicoid protein gradient (spatial) forms in early nuclear cycles (temporal).
- **Zygotic stage:** Bicoid activates *hunchback*; gap genes form broad domains; pair-rule genes (eve, ftz) resolve to 7 stripes; segment-polarity genes (en, wg) to 14 stripes.
- **Takeaway:** each successive layer is both more spatially precise and later in time — patterning is a temporal *refinement cascade* on spatial information.

### 3.2 Zebrafish somitogenesis

- Somites bud off the presomitic mesoderm (PSM) on a ~30-minute clock.
- **Temporal:** cyclic genes (e.g., *her1/her7*, linked to Notch signaling) oscillate in the PSM.
- **Spatial:** as cells pass the determination front (FGF/Wnt gradient high posterior, low anterior), oscillations freeze into a boundary.
- **Takeaway:** the classic "clock-and-wavefront" — temporal oscillation + spatial gradient = periodic structure. Reading the two axes separately is essential.

### 3.3 Neural tube DV patterning

- **Spatial:** Shh from notochord/floor plate → ventral gradient; BMPs from roof plate → dorsal gradient.
- **Temporal:** duration and concentration jointly specify class (V3 → motor → V2 → V1 ventrally).
- **Takeaway:** morphogen interpretation depends on *both* concentration and exposure time; a purely spatial view misses this.

### 3.4 Arabidopsis flower development

- **Spatial:** ABC-model classes occupy concentric whorls (A outer sepals/petals; B petals/stamens; C stamens/carpels).
- **Temporal:** floral meristem identity (LFY/AP1) precedes organ identity; MADS-box expression initiates in defined stages.
- **Takeaway:** radial spatial organization + staged temporal initiation = deterministic organ pattern.

---

## 4. Mapping expression — method fit

| Method | Spatial resolution | Temporal resolution | Best for |
|---|---|---|---|
| In situ hybridization (chromogenic) | Tissue/cell | Endpoint | Domain mapping, publication figures |
| In situ (fluorescent, RNAscope-class) | Single-cell, subcellular | Endpoint | Low-abundance transcripts, multiplexing |
| RNA-FISH | Single-molecule spots | Endpoint | Absolute transcript counts per cell |
| Immunohistochemistry / IF | Subcellular | Endpoint | Protein-level spatial readout |
| GFP/lacZ/luciferase reporters | Cell (live) | Live, continuous | Dynamics; enhancer activity |
| Bulk RT-qPCR / RNA-seq | None (averaged) | Discrete samples | Magnitude, time courses |
| Single-cell RNA-seq | Cell (lost coordinates) | Snapshot | Cell types, trajectories |
| Spatial transcriptomics (array-based, imaging-based) | Spot (~10–100 µm) or subcellular | Snapshot (time courses by sampling) | Whole-tissue expression maps |

*(Details and workflows in Modules 11 and 12.)*

---

## 5. Designing a spatiotemporal study — checklist

1. **State the question in both axes:** "Where is gene X at stage Y?" or "How does the *domain* of X change from stage A to B?"
2. **Choose resolution:** cell type vs tissue region vs whole-embryo.
3. **Choose method(s):** endpoint (in situ, IF) vs live (reporter) vs snapshot-transcriptomic (scRNA/spatial).
4. **Stage control:** developmental staging is the temporal variable — define it rigorously (e.g., zebrafish hpf/somite count; Drosophila embryonic stage; E-days for mouse).
5. **Replicates:** biological (clutches/litters), technical (stains/probes).
6. **Controls:** sense probe (or no-probe) for ISH; known marker gene to validate staging/region; reporter-vector controls (Module 5).
7. **Quantification plan:** domain area, intensity, cell counts — decide before imaging.

---

## 6. Self-check questions

1. You have bulk RNA-seq showing gene X peaks at 24 hpf in zebrafish. Design the minimal two-experiment follow-up to locate *where*.
2. Why can a gradient and a domain coexist for the same pathway (Shh gradient vs *nkx2.2* domain)?
3. In somitogenesis, which data would convince you a gene is part of the *clock* rather than the *wavefront*?
4. A reporter shows expression in a domain, but in situ for the endogenous gene shows a wider domain. Give two plausible reasons.
5. Which method would you choose to quantify absolute transcript numbers per cell in a tissue? Which for live dynamics?

---

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](08-Developmental-Gene-Expression.md) · → [Next Topic](10-Gene-Regulatory-Networks.md)
