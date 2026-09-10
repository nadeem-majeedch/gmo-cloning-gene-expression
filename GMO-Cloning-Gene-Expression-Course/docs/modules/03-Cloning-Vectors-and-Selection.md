# Module 3 — Cloning Vectors and Selection/Screening

**Level:** Beginner → Intermediate

---

## Learning objectives

1. Classify vector systems by host, purpose, capacity, and essential components.
2. Distinguish **selection**, **screening**, and **validation**, and explain why all three stages exist.
3. Choose an appropriate selection/screening strategy for a given cloning scenario.
4. Interpret the results of blue-white screening, colony PCR, and diagnostic digests.

---

## 1. Vector systems overview

| Vector class | Typical host | Purpose | Capacity / components | Strengths | Limitations |
|---|---|---|---|---|---|
| **General plasmid cloning vector** | *E. coli* | Propagate a fragment; subclone | ori, antibiotic marker, MCS; ~1–15 kb inserts | Simple, cheap, high copy | Limited capacity; no expression features |
| **Expression vector (bacterial)** | *E. coli* expression strains | Make protein (e.g., T7-based systems in DE3 strains) | Strong inducible promoter, RBS, tag, terminator | High yield, cheap protein | Many eukaryotic proteins misfold; inclusion bodies; codon issues |
| **Mammalian expression vector** | Transfected mammalian cells | Express genes in eukaryotic context | CMV/EF1α/PGK-type promoters, Kozak, intron, polyA signal, mammalian selectable marker (neo/puro/hygro) | Proper folding, PTMs; transient or stable | Transfection efficiency varies; silencing of integrated DNA |
| **Shuttle vector** | Two hosts (e.g., *E. coli* + yeast, or *E. coli* + mammalian) | Build in *E. coli*, use in second host | Two origins, two selectable markers | Flexible pipeline | Larger; more components to verify |
| **Viral vector (conceptual)** | Depends on virus (retro/lenti, AAV, adenoviral) | Efficient gene delivery into cells/animals | Envelope/packaging elements, transgene cassette; replication functions usually provided in trans by packaging cells | Excellent delivery, incl. non-dividing cells (AAV, lenti) | Cargo size limits (AAV ~4.7 kb); biosafety level depends on system; production complexity |
| **BAC (bacterial artificial chromosome)** | *E. coli* | Clone very large genomic loci (~100–300 kb) | F-factor-based single-copy ori, selection marker | Stable maintenance of huge DNA; low recombination | Low copy → low DNA yield; harder manipulation |
| **YAC (yeast artificial chromosome)** | *S. cerevisiae* | Clone megabase-scale fragments | Yeast centromere, telomeres, ARS, selection markers | Largest capacity (up to ~1 Mb) | Chimerism/instability; technically demanding |
| **Plant transformation vector (binary)** | *Agrobacterium tumefaciens* (+ *E. coli* build host) | Deliver T-DNA into plant genomes | Binary: T-DNA border repeats flanking the cassette on one plasmid; vir genes on a helper plasmid (or integrated in disarmed *Agrobacterium* strain) | Native plant transformation machinery | Plant tissue culture/regeneration is species-specific and slow |

Notes:

- "Examples of common architectures (pUC-, pBR322-, pET-, CMV-driven mammalian, binary Ti-derived)" are *archetypes* — thousands of derivatives exist. Consult the actual map of the vector you use.
- BACs and YACs matter for genomics: sequencing projects, transgenic loci with full regulatory context, and synthetic-genome assembly.

### 1.1 How capacity shapes use

```text
Capacity (log scale, kb)

  plasmids      BACs         YACs
  ────────  │  ─────────  │  ──────────
  1–15 kb   │  100–300 kb │  up to ~1000 kb
  genes,    │  gene loci  │  genome regions,
  cassettes │  with       │  synthetic genomes
            │  regulatory │
            │  context    │
```

*Figure 3.1 — Vector capacity ranges (approximate, log scale).*

---

## 2. Selection vs screening vs validation

These words are not synonyms. Confusing them causes experimental design errors.

| Concept | Definition | Acts on | Examples |
|---|---|---|---|
| **Selection** | A condition under which undesired cells **cannot grow** — population-level enrichment | Whole colonies/cells | Antibiotic resistance marker; auxotrophic complementation (host missing a gene survives only if plasmid supplies it) |
| **Screening** | A test applied **per candidate** to distinguish wanted from unwanted clones | Individual colonies | Blue-white; colony PCR; mini-prep digest; fluorescence |
| **Validation** | Definitive confirmation of identity/sequence/function | Candidate clones | Sanger sequencing; functional assay; expression check |

```text
Transformation
      ↓
Selection            ← only vector-carrying cells grow (marker)
      ↓
Candidate colonies   ← hundreds/thousands
      ↓
Screening            ← colony PCR / blue-white / digest → shortlist
      ↓
Molecular validation ← diagnostic digest pattern matches map
      ↓
Sequence confirmation← Sanger across junctions + full insert
      ↓
Functional validation← expression/assay appropriate to purpose
```

*Figure 3.2 — Why every stage is needed: selection removes cells *without vector*; screening removes clones *with the wrong vector*; validation proves the surviving clone is what you designed.*

### 2.1 Selectable markers in detail

- **Antibiotic resistance:** the workhorse. Ampicillin/carbenicillin, kanamycin, chloramphenicol, tetracycline, spectinomycin — each pairs with a resistance gene; concentrations are *institutional/protocol-specific* and not universal.
- **Auxotrophic selection:** the host lacks a biosynthetic gene (e.g., *hisB* or *ura3* deficiency); growth on minimal medium requires the plasmid-borne copy. Antibiotic-free alternative used in some industrial and yeast contexts.
- **Mammalian markers:** neo/G418, puromycin, hygromycin, blasticidin — used to derive stable cell lines.
- **Counter-selection tools** (conceptual): markers that *kill* cells carrying them under specific conditions (e.g., sacB on sucrose in many Gram-negatives; HSV-TK + ganciclovir in mammalian cells) — essential for scarless engineering workflows.

### 2.2 Screenable markers and blue-white screening

**Blue-white screening** exploits **lacZ α-complementation**: the host strain carries a deletion of lacZ α-domain; the vector supplies lacZα. On X-gal, an empty vector yields **blue** colonies (functional β-galactosidase); an insert disrupting lacZα yields **white** colonies. White = candidate insert, but insert presence ≠ correct insert — screen further.

Other screenable readouts:

- **Fluorescent reporters** (GFP etc.): direct visualization; also enable FACS sorting.
- **Colorimetric reporters:** lacZ/X-gal anywhere in a cassette; alkaline phosphatase histochemistry.
- **Positive-selection cloning:** vectors engineered so that insertion *restores* a lethal function or *disrupts* a toxic gene (ccdB-type systems) — reduces empty-vector background.

### 2.3 Molecular screening tools

**Colony PCR** — pick a colony into PCR mix with primers flanking the insertion site. Interpretation:

```text
        empty vector        correct insert       wrong-orientation insert
       (small band)        (insert-size band)     (bands differ)
            ┃                    ┃                     ┃
            ▼                    ▼                     ▼
        ~200 bp              ~1.5 kb              diagnostic pair
```

- Use one vector primer + one insert primer to *force* orientation-specific readout.
- Expect both an empty-vector-size band and an insert-size band possibility — design primers so the two are distinguishable.

**Diagnostic restriction digest** of mini-prep DNA: choose enzymes that cut asymmetrically so orientation gives different fragment patterns. A single uninformative band is a wasted experiment.

**Sanger sequencing** — final word for sequence identity, including PCR-introduced mutations.

### 2.4 Expression validation

Sequence-correct ≠ expressing. Confirm at the level your question requires:

- **RNA:** RT-PCR/RT-qPCR against the transcript.
- **Protein:** Western blot (anti-tag or anti-protein), or functional fluorescence.
- **Function:** enzyme activity, rescue phenotype, reporter output — depends entirely on the construct's purpose.

---

## 3. Worked example — choosing a strategy

**Scenario:** You ligate a 1.2 kb insert into a 3.5 kb vector carrying ampR and lacZα, and transform.

1. **Selection:** plate on ampicillin — every colony has *some* vector.
2. **Screen:** white colonies on X-gal are candidates; pick 6–12, colony PCR with a vector primer + insert primer.
3. **Validate:** mini-prep two PCR-positive clones; digest with EcoRI + HindIII (which flank the MCS); expect 1.2 kb + 3.5 kb bands, not the empty-vector pattern.
4. **Sequence:** Sanger from flanking vector primers covers the entire 1.2 kb insert and both junctions.
5. **Function:** if the construct is a promoter-reporter, transiently express in the relevant cell type and compare against promoterless vector and empty-vector controls.

---

## Figures

<figure markdown>
![Anatomy of a cloning plasmid: origin of replication, selectable marker, multiple cloning site, promoter and terminator.](../assets/DIAGRAMS/plasmid_map.png)

*Figure - Anatomy of a cloning plasmid: origin of replication, selectable marker, multiple cloning site, promoter and terminator.*
</figure>

<figure markdown>
![Selection versus screening versus validation: antibiotic selection, colony PCR screening and sequencing validation.](../assets/DIAGRAMS/selection_screening.png)

*Figure - Selection versus screening versus validation: antibiotic selection, colony PCR screening and sequencing validation.*
</figure>


## 4. Self-check questions

1. A transformation on antibiotic plates yields 500 colonies, all of which turn out by colony PCR to be empty vector. Which stage failed, and what are two fixes?
2. Why does blue-white screening not guarantee an insert of the *correct* sequence or size?
3. When would you choose a BAC over a standard plasmid? Give a concrete research question.
4. Distinguish auxotrophic selection from antibiotic selection, and give one situation where auxotrophy is preferable.
5. Your insert is toxic when expressed even weakly in *E. coli*. Which vector features help (ori copy number, promoter type, inducibility)? Explain.
---

## What you should know

Review the learning objectives at the top of this module and the self-check or quick-check questions above. When you can meet every objective unaided, you are ready to continue.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) questions for these topics.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [laboratory overview](../labs/index.md).

[<- DNA and Molecular Cloning Fundamentals](../modules/02-DNA-and-Molecular-Cloning.md) &middot; [Course home](../index.md) &middot; [Continue to next module ->](../modules/04-Cloning-Techniques.md)
