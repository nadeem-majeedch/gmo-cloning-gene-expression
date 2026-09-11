# Module 2 — Hazard, Risk and Exposure

**Level:** Beginner (the conceptual core of the course)

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](01-Introduction-to-GMO-Risk-Assessment.md) · → [Next Topic](03-GMO-Environmental-Risk-Assessment-Framework.md)
> 🧪 Related Practicals: [Lab 01](../LAB/Lab-01-Terminology-and-Hazard-Identification.md) · [Lab 09](../LAB/Lab-09-Risk-Ranking-Matrix.md) · 📊 Data: [Risk-matrix scores](../DATA/risk-matrix/) · 📝 Assessment: [MCQs](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Environment-Risk-Assessment-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Environment-Risk-Assessment-FAQs.md)

---

## Learning objectives

1. Define **hazard**, **exposure**, and **risk**, and use them with precision.
2. Explain the teaching relationship *Hazard + Exposure + Dose/Response + Context → Risk*, and its limits.
3. Apply the distinction to four GMO classes: Bt crops, herbicide-tolerant crops, gene-edited organisms, GM microorganisms.
4. Diagnose the most common public and professional conflations of hazard with risk.

---

## Definition

- **Hazard** — a property or situation with the *potential* to cause harm. A hazard exists whether or not anyone is ever exposed. Statements about hazard begin "X *can*…".
- **Exposure** — the contact between a hazard and a valued entity (organism, population, ecosystem service), characterized by route, magnitude, frequency, and duration.
- **Risk** — the likelihood and severity of harm *realized* through that contact, in a specific context. Statements about risk begin "X *will*… with probability…".

## Why it matters

Hazard-only thinking produces two opposite, equally wrong conclusions:
- "It's a toxin, so it's dangerous" (ignoring that exposure may be zero),
- "No exposure detected, so nothing can go wrong" (ignoring scale, duration, and change over time).

Risk thinking replaces both with an analyzable structure. It is also the vocabulary regulators use: frameworks worldwide assess hazard, exposure, and risk as distinct steps (Module 3, 22).

## Beginner explanation

A pit viper is a **hazard**. A pit viper behind museum glass is **no risk** to visitors — exposure is zero. The same snake on a hiking trail at ankle height is a different, nonzero risk. The snake never changed; the *exposure and context* changed.

Everyday version: a kitchen knife is a hazard; a knife locked in a drawer presents negligible risk; a knife waved around at a party does not.

## Scientific explanation

Risk frameworks formalize this as an analytical chain:

```text
  HAZARD  (intrinsic potential to harm)
     +
  EXPOSURE  (route × magnitude × frequency × duration)
     +
  DOSE–RESPONSE  (how effect scales with amount)
     +
  CONTEXT  (species, environment, mitigation, values at stake)
     =
  RISK CHARACTERIZATION  (qualitative or quantitative judgment)
```

**Important caveat (required by scientific honesty):** this is a *teaching* relationship, not a universal equation. Different frameworks combine these elements differently — some multiply formal probabilities, some rank ordinally (high/medium/low), some integrate weight-of-evidence narratives. What is universal is the *separation of concerns*: identify what could harm, establish who/what contacts it and how much, then combine — and state the uncertainty of every step.

### 2.1 Dose–response: the bridge between hazard and risk

A hazard that is real at one dose may be irrelevant at environmentally plausible doses. Classic tools:

- **NOAEL/LOAEL** — no/lowest observed adverse effect level in a study.
- **Benchmark dose** — dose producing a pre-defined response change.
- **Sigmoid (hill) curves** — typical of many toxicological and protein-mediated effects: minimal response at low dose, steep transition around an IC50/EC50 (see [Lab 08](../LAB/Lab-08-Dose-Response-Analysis.md), Exercise 8).

No environmental exposure (Module 13) means even a potent hazard yields ≈ zero risk; high, repeated exposure to a weak hazard can matter.

## Real-world examples (four GMO classes)

### 2.2 Bt crops

| Element | Analysis |
|---|---|
| Hazard (candidate) | Cry proteins are selectively active in the guts of susceptible insect orders (Lepidoptera, Diptera, Coleoptera); they are proteins, digestible, and not active in vertebrates or in most non-target invertebrates studied |
| Exposure | Pollen, plant tissue, root exudates, crop debris; eaten by non-target herbivores only if those species feed on the crop or its residues |
| Dose–response | Species-specific activity curves; environmental concentrations often orders of magnitude below active doses for insensitive species |
| Context | Field margins, milkweed-type larval host plants, feeding behavior, season |
| Risk conclusion style | "For species X feeding on compartment Y, estimated exposure is Z× below the dose causing effect A; uncertainty: …" |

The 1999 lab-findings vs field-reality episode (larval effects on a butterfly in laboratory conditions vs negligible field exposure under standard management) is the canonical demonstration that **hazard identification is not risk characterization** (Module 23, Case 7).

### 2.3 Herbicide-tolerant (HT) crops

| Element | Analysis |
|---|---|
| Hazard (candidate) | The tolerance protein itself is typically assessed as not hazardous to non-targets; the *management change* — greatly increased use of one broad-spectrum herbicide — is a hazard pathway for weeds (selection) and for farmland plant diversity |
| Exposure | Weeds: continuous, across whole fields. Farmland flora: via herbicide programs. Volunteers: seed bank |
| Dose–response | Selection intensity on weed populations scales with herbicide use frequency and efficacy |
| Context | agronomic system, resistance history in region |
| Risk conclusion style | "Risk of resistance evolution in system S over N years is high absent management M" — an *indirect* risk arising from how the crop is used |

Key teaching point: for HT crops the most consequential environmental hazard is often **not the protein but the practice**. Risk assessment therefore extends to changed herbicide regimes (Module 12).

### 2.4 Gene-edited organisms

| Element | Analysis |
|---|---|
| Hazard (candidate) | Depends entirely on the edit: a small deletion silencing a gene may create no novel product at all; a base change encoding a new enzyme function may create a novel metabolic capability |
| Exposure | Same ecology as the organism itself — the edit rarely creates a new exposure route |
| Dose–response | Only applies when a new product is expressed |
| Context | Regulatory treatment varies by jurisdiction — some regulate the *product* (novel trait), others the *process* (any edit) |
| Risk conclusion style | "Trait-based analysis: the edit alters phenotype P; ecological consequences of P in environment E are/are not distinguishable from conventional breeding outcomes" |

Teaching point: editing technology changes *how precisely* a change is made, not whether ecological consequences follow from phenotypic change. Risk assessment remains phenotype-and-environment-driven (Module 4, 25).

### 2.5 GM microorganisms (GMMs)

| Element | Analysis |
|---|---|
| Hazard (candidate) | Persistence and multiplication in unusual niches; horizontal gene transfer of constructs to native microbes; altered metabolic competition |
| Exposure | Application to soil/water, dispersal, survival windows |
| Dose–response | Population-establishment thresholds rather than single-organism toxicity |
| Context | Microbial evolution operates on short timescales; containment/recovery harder than for crops |
| Risk conclusion style | "Establishment probability in niche N under conditions C is low/unknown; HGT potential assessed via construct design and niche overlap" |

GMMs are where hazard–exposure separation is most fragile, because a released microbe can *maintain its own exposure* by multiplying. This is why GMM frameworks emphasize containment, disability (auxotrophy), and suicide systems (Module 23, Case 13).

## Step-by-step workflow: from hazard concern to risk statement

```text
1. State the concern precisely  ("X could harm Y via route R")
2. Characterize the hazard      (mechanism, specificity, dose-response)
3. Characterize exposure        (route, magnitude, frequency, duration; worst case + realistic case)
4. Place in ecological context  (receiving environment, species present, mitigations)
5. Combine & characterize risk  (qualitative banding or quantitative estimate)
6. State uncertainty explicitly (what is assumed, what is unknown, sensitivity)
7. Identify management options  (reduce exposure? reduce hazard? monitor?)
8. Draft the risk statement     ("Risk of H to V via R is [band], given [evidence], with [uncertainty]")
```

## Example data

Using the simulated risk-matrix dataset ([DATA/risk-matrix](../DATA/risk-matrix/)):

| Scenario | Hazard present? | Exposure? | Likelihood × consequence | Band |
|---|---|---|---|---|
| S03 — GM pollen × wild relative 800 km away | Yes (gene flow possible in principle) | ~None (distance) | 1×2 | Low |
| S02 — same, compatible wild relative within 200 m | Yes | Real | 4×2 | Medium |
| S06 — target-pest resistance, no refuge | Yes (selection certain) | Continuous | 5×4 | Very high |
| S10 — DNA uptake by soil bacteria | Yes (in principle) | Likely but ephemeral | 2×1 | Low |

Same class of hazard; four different risks because exposure and context differ.

## Interpretation

- Ask of every scary headline: *what is the hazard, and what is the exposure?*
- Ask of every reassuring claim: *was exposure measured, at what scale, over how long?*
- A risk statement without an exposure sentence is incomplete.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Hazardous = risky" | Hazard requires exposure to become risk |
| "No detected risk = no risk" | Detection limits, scale, and duration bound what was excluded |
| "Natural = no hazard" | Many natural alleles/compounds are hazards; origin is not a safety property |
| "GM hazard is unique" | Assessment compares like with like: GM vs conventional counterpart, not GM vs ideal |
| "Risk = probability × severity, always" | Some frameworks integrate qualitatively; the formula is one formalism among several |

## Exam points

- Be able to write a complete risk statement (hazard + exposure + context + uncertainty).
- Explain why lab-only findings (hazard, favorable exposure) cannot alone justify field risk conclusions.
- Explain why HT-crop risk assessment must include management-system effects.
- Know that frameworks differ in how they combine elements; the *separation* is the universal part.

## Quick-check questions

1. A reporter writes: "GM crop produces insecticidal protein — is it dangerous?" Answer in the hazard/risk vocabulary in ≤ 3 sentences.
2. Construct one scenario where a mild hazard produces high risk, and one where a severe hazard produces negligible risk.
3. Why is dose–response the bridge between hazard and risk? What replaces dose–response for GMM establishment risk?
4. In the S06 vs S07 contrast (no refuge vs structured refuge), which element of the risk chain did management change?
5. A gene-edited, promoter-less cisgenic-type edit shows no novel protein. What hazard pathways remain worth assessing?

---

*Next: [Module 3 — The GMO Environmental Risk-Assessment Framework](03-GMO-Environmental-Risk-Assessment-Framework.md) formalizes these concepts into the standard workflow.*
