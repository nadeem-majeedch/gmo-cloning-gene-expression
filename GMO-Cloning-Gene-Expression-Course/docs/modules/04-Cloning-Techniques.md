# Module 4 — Cloning Techniques

**Level:** Intermediate

---

## Learning objectives

1. Explain the molecular basis of each major cloning technique: restriction/ligation, TA, blunt-end, Gibson, Golden Gate, Gateway (conceptual).
2. Choose the right technique for a given design problem, and justify the choice.
3. Predict the failure modes of each technique and the screening strategy that detects them.

---

## 1. Restriction-enzyme cloning

The classical method: cut insert and vector with **restriction endonucleases**, anneal the resulting ends, and seal with **DNA ligase**.

### 1.1 Restriction enzymes

- **Recognition:** specific palindromic (usually) sequences, typically 4–8 bp, e.g., EcoRI: `5′-G↓AATTC-3′`.
- **Cut position:** at or near the recognition site.
- **End type:**
  - **Sticky (cohesive) ends:** staggered cut → single-stranded overhangs (EcoRI → 5′-AATT overhangs; HindIII → 5′-AGCT).
  - **Blunt ends:** cut both strands at the same position (EcoRV, SmaI, PvuII).
- **Methylation sensitivity:** some enzymes fail on methylated DNA (e.g., dam/dcm methylation in common lab *E. coli* blocks some sites) — a real design consideration.
- **Compatible overhangs:** different enzymes can generate identical overhangs (e.g., BamHI and BglII both leave 5′-GATC); such "compatible ends" ligate but usually destroy both original sites — useful for directional subcloning.

### 1.2 Workflow

```text
   insert DNA                          vector DNA
       │                                   │
       ▼ restriction digest                ▼ restriction digest
   insert fragments                   linearized vector
       │                                   │
       ▼ gel purification                  ▼ gel purification
   clean insert                       dephosphorylate vector (optional*)
       │                                   │
       └────────────┬──────────────────────┘
                    ▼
              ligation (T4 DNA ligase, ATP)
                    │
                    ▼
          recombinant + background products
                    │
                    ▼
        transformation → selection → screening
```

*Why dephosphorylate the vector?* Removing 5′ phosphates from the vector prevents it from self-ligating; only insert-carrying molecules (which provide the missing phosphates) yield transformants efficiently. *The exact treatment depends on the enzyme/end combination — follow a validated protocol from your institution.*

**Insert:vector molar ratio:** ligation kinetics depend on effective concentrations. Typical starting points are 3:1 to 5:1 insert:vector molar ratios for sticky-end ligations (formulas and worked calculations appear in [Lab 03](../labs/Lab-03-Ligation-and-Transformation.md) and the [Cheat Sheet](../guide/cheat-sheet.md)). Too little insert → empty vector; too much → multiple inserts or concatemers.

**Directional cloning:** cut the vector with two different enzymes and the insert with the same two → non-identical sticky ends force the insert to ligate in one orientation only.

### 1.3 Strengths / limitations

- **Strengths:** cheap, well-understood; scarless at the junctions if sites preserved; directional possible.
- **Limitations:** need unique sites in both molecules; internal-site conflicts; multi-fragment assemblies become combinatorially painful; ligase is sequence-agnostic (background self-ligation).

---

## 2. TA cloning

**Principle:** *Taq* polymerase adds a single 3′-A overhang to PCR products (non-template-directed). A linear "T-vector" carries complementary 3′-T overhangs. A-overhangs anneal to T-overhangs; ligation completes the circle.

- **Advantages:** simple, fast, directional at the single-base level; ideal for capturing PCR products directly.
- **Limitations:** high-fidelity polymerases (Pfu, Q5-class) generate **blunt** products — they require an A-tailing step before TA cloning; orientation not controlled; background from non-specific bands.

---

## 3. Blunt-end cloning

**Principle:** ligate blunt-ended insert into blunt-ended vector. Any blunt molecule can ligate to any other, so:

- **Advantages:** universal — works when no convenient sites exist; any PCR product or sheared fragment can be used.
- **Limitations:** ligation is much less efficient than sticky-end ligation; no directionality; vector self-ligation is the dominant background → dephosphorylation is essentially mandatory; frequent need for high insert excess.

---

## 4. Gibson Assembly

**Principle:** an isothermal, one-step, multi-fragment assembly using three activities acting on fragments with **~20–40 bp terminal overlaps**:

```text
   5′ exonuclease       chew back 5′ ends → exposes 3′ single-stranded overhangs
        ↓
   annealing            overlapping ssDNA ends find each other by sequence
        ↓
   polymerase           fills gaps at the annealed junctions
        ↓
   DNA ligase           seals remaining nicks
```

- **Strengths:** seamless (no restriction-site scars); assembles many fragments in one tube; order and orientation determined by the overlaps themselves; tolerant of awkward sequences (no need for sites).
- **Limitations:** requires designing primers with correct overlaps; repeated sequences cause misassembly; very short or very long fragments each have sweet-spot ranges; cost of enzyme mix.

**Multi-fragment design intuition:** arrange fragments as a circle; each fragment's end must overlap its neighbor's start. The overlap *is* the addressing scheme — like matching jigsaw edges.

---

## 5. Golden Gate Assembly

**Principle:** exploit **Type IIS restriction enzymes** (BsaI, BsmBI, Esp3I, SapI...) that cut *outside* their recognition site, leaving **programmable 4-bp overhangs**.

```text
        recognition site    cut position
        GGTCTC(N1)  ▼  ──▶  NNNN|NNNN      ← the 4 overhang bases are
                        ▲                  whatever YOU design
```

- Because the overhang bases are designer-chosen, each fragment–fragment junction can be assigned a unique 4-bp "address".
- **One-pot assembly:** digest and ligate happen simultaneously; as the correct overhang pairs ligate, the recognition sites are consumed (they sit outside the final product), so the reaction becomes directional and self-selecting for the intended product.
- **Strengths:** highly efficient; unlimited (practically, tens of) parts; the core of **modular cloning** frameworks (e.g., MoClo-style hierarchies in plant and synthetic biology) — parts are stored in level-0 plasmids with standardized fusion sites, then combined into transcription units, then multi-gene constructs.
- **Limitations:** every part must be domesticated (internal Type IIS sites removed or silently mutated); scar at each junction is 4 bp (usually benign); designing the fusion-site map requires care; enzymes are temperature-sensitive (assembly often performed with alternating digestion/ligation cycling).

---

## 6. Gateway cloning (conceptual)

**Principle:** site-specific recombination borrowed from bacteriophage λ. Recombination between **att** sites moves a DNA segment ("cassette") between plasmids without cutting/ligating.

```text
  attB1-Gene-attB2  +  donor vector (attP1…attP2, ccdB⁺)
            │  BP clonase (λ integrase-type activity)
            ▼
      entry clone (attL1-Gene-attL2)         ← your gene, archived
            │  LR clonase (with destination vector attR1…attR2)
            ▼
      expression clones in many destination vectors
```

- **Entry clone:** a verified, sequence-confirmed archive of the gene.
- **Destination vector:** any backbone accepting the cassette (different promoters, tags, hosts).
- **Strengths:** one verified entry clone feeds unlimited destination vectors; excellent for parallel expression testing.
- **Limitations:** att-site recombination scars remain; destination-vector background requires counter-selection (commonly ccdB-based); clonase mixes are proprietary and costly; the cassette cannot be freely re-designed the way Gibson/Golden Gate allow.

*(This module describes the recombination logic; consult current vendor documentation for any actual system before use — this course does not endorse specific commercial products.)*

---

## 7. Comparison table

| Technique | Principle | Strength | Limitation | Typical application |
|---|---|---|---|---|
| **Restriction–ligation** | Endonuclease cuts → cohesive/blunt ends → ligase seals | Cheap, robust, well-trodden | Needs suitable unique sites; background self-ligation; poor for multi-fragment | Single-insert subcloning; directional insert swap |
| **TA cloning** | Taq A-overhang ↔ T-vector | Fast capture of PCR products | No orientation control; incompatible with blunt-products without A-tailing | Quick PCR-product archiving |
| **Blunt-end cloning** | Ligase joins flush ends | Universal — any blunt fragment | Low efficiency; no directionality; heavy background | Cloning when no sites available; adaptor-based workflows |
| **Gibson Assembly** | 5′ exonuclease + annealing + polymerase + ligase on overlapping fragments | Seamless; multi-fragment; no site constraints | Overlap design burden; repeats cause misassembly; enzyme mix cost | Synthetic constructs; joining several pieces; vector + 2 inserts |
| **Golden Gate** | Type IIS → designer 4-bp overhangs; digest+ligate one-pot | Extremely efficient; modular; multiplex | Domestication of internal sites; 4-bp scars; fusion-site planning | Modular cloning; combinatorial libraries; pathway assembly |
| **Gateway** | att-site recombinational transfer | Reuse one entry clone across many vectors | Recombination scars; proprietary; counter-selection background | Parallel expression-vector screening; ORFeome-style projects |

---

## 8. Choosing a technique — decision guide

```text
Need directional, seamless, multi-fragment?
   ├─ yes → Gibson (≤ ~6–8 fragments, custom overlaps)
   │        or Golden Gate (many parts, modular reuse, standardized parts)
   └─ no →
       Do unique restriction sites exist in both molecules?
           ├─ yes → restriction–ligation (directional, dephosphorylate vector)
           └─ no →
               PCR product capture only? → TA cloning
               otherwise → blunt-end cloning (accept lower efficiency)
Parallel reuse across many backbones? → Gateway
```

---

## Figures

<figure markdown>
![Restriction-enzyme cloning: the insert and vector are cut with compatible enzymes, then ligated directionally.](../assets/DIAGRAMS/restriction_cloning.png)

*Figure - Restriction-enzyme cloning: the insert and vector are cut with compatible enzymes, then ligated directionally.*
</figure>

<figure markdown>
![Gibson Assembly: a 5' exonuclease chews back ends, complementary overlaps anneal, polymerase and ligase seal the seams.](../assets/DIAGRAMS/gibson_assembly.png)

*Figure - Gibson Assembly: a 5' exonuclease chews back ends, complementary overlaps anneal, polymerase and ligase seal the seams.*
</figure>

<figure markdown>
![Golden Gate (type IIS) assembly: enzymes cut outside their recognition sites, creating programmable 4-bp overhangs for one-pot multi-part assembly.](../assets/DIAGRAMS/golden_gate.png)

*Figure - Golden Gate (type IIS) assembly: enzymes cut outside their recognition sites, creating programmable 4-bp overhangs for one-pot multi-part assembly.*
</figure>


## 9. Self-check questions

1. You must clone a 4.5 kb insert with an internal BamHI site into a vector cut with BamHI. Options?
2. Why does Golden Gate assembly become *more* product-specific as the reaction proceeds, while ordinary ligation does not?
3. Your Gibson assembly of 5 fragments produced colonies whose plasmids lack fragment 3. Name three design-level causes.
4. When is Gateway clearly better than Gibson? When is it clearly worse?
5. Explain why dephosphorylation helps blunt-end cloning far more than it helps a two-enzyme directional sticky-end cloning.
---

## What you should know

Review the learning objectives at the top of this module and the self-check or quick-check questions above. When you can meet every objective unaided, you are ready to continue.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) questions for these topics.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [laboratory overview](../labs/index.md).

[<- Cloning Vectors and Selection/Screening](../modules/03-Cloning-Vectors-and-Selection.md) &middot; [Course home](../index.md) &middot; [Continue to next module ->](../modules/05-Expression-Constructs-and-Reporter-Genes.md)
