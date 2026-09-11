# Module 13 — Environmental Fate and Exposure

**Level:** Intermediate

---

## Learning objectives

1. Define environmental fate and exposure assessment for GMO-derived products (proteins, plant material, seed, DNA).
2. Diagram the compartment model: where the product goes and how it moves.
3. Explain decay, dilution, and degradation — and how half-lives shape exposure duration.
4. Construct exposure-pathway chains (crop → pollen → non-target plant → herbivore → predator) and estimate magnitudes.
5. Distinguish realistic vs bounding (worst-case) exposure scenarios and their roles.

---

## Definition

**Environmental fate** — what happens to a GMO-derived substance (expressed protein, residues, DNA) after release into the environment: distribution among compartments, persistence, degradation, transport. **Exposure assessment** — the quantification of contact between those substances and living organisms: route, magnitude, frequency, duration.

## Why it matters

Exposure is the hinge of risk (Module 2). Two GMOs with identical hazard profiles can have opposite risk conclusions if one stays on the field and the other spreads via streams. Fate data also drive monitoring design (measure *where* the model says exposure lives) and management design (intervene where exposure is created).

## Beginner explanation

Drop sugar into still water vs a flowing stream. Still water: dissolves, stays, slowly consumed. Stream: swept away, diluted fast. Now the sugar is a protein in crop debris; the field is a compartment; rain, microbes, sunlight are the moving forces. Exposure assessment is following the molecule with a map and a stopwatch: where does it go, how long does it last, who walks by?

## Scientific explanation

### 13.1 The compartment model

```text
                    ┌──────────── crop canopy ────────────┐
                    │  pollen (anthesis)   tissue (season)│
GM crop ────────────┤                                     ├──→ herbivores/pollinators
                    │  roots/exudates (season-long)       │
                    └── debris + residues (post-harvest) ─┘
                         │            │
                    soil surface   runoff water
                         │            └──→ streams (shredders)
                    soil profile (adsorption, decay)
                         └──→ soil fauna, rhizosphere (Module 9)
```

Each compartment has: input (expression × biomass), output (decay/removal), and a resident community (the exposure audience).

### 13.2 The decay law and half-life

First-order decay: `C(t) = C₀ · e^(−kt)`; half-life `t½ = ln2/k`.

From the simulated season dataset ([DATA/exposure](../downloads/exposure.md)):

| Compartment | C₀ (illustrative) | Model k | approx. half-life | Exposure audience |
|---|---|---|---|---|
| Rhizosphere soil | 18 ng/g | 0.045 | ~15 days | soil invertebrates, microbes |
| Crop debris | 42 ng/g | 0.020 | ~35 days | detritivores, aquatic shredders |
| Runoff water | 0.9 ng/L | 0.12 | ~6 days | stream invertebrates (pulse) |
| Pollen trap | ~6 (rel.) | anthesis-driven | seasonal window | flower visitors, margin larvae |

Teaching pattern (literature-consistent in kind): **debris dominates duration; runoff gives pulses; pollen gives a narrow seasonal window**. Exposure "lives" in different compartments for different audiences.

### 13.3 Building a pathway chain (magnitude bookkeeping)

```text
Crop (expression: 42 ng/g debris)
  → debris retained in margin stream (dilution/concentration: ×f₁)
    → shredder larva eats debris (diet fraction ×f₂, assimilation ×f₃)
      → predator eats shredder (diet ×f₄)
```

Each step multiplies — and usually *shrinks* (digestion, decay, dilution). The assessment chain answers: does the endpoint organism's estimated intake approach its hazard threshold (Module 8 §8.4's IC50 comparison)? If intake ≪ threshold with margin, the pathway closes; if comparable, escalate tiers.

### 13.4 Realistic vs bounding scenarios

| Scenario type | Definition | Use |
|---|---|---|
| **Realistic case** | typical management, typical weather, central estimates | the risk conclusion's backbone |
| **Bounding (worst plausible) case** | maximum credible expression × maximum retention × sensitive species | Tier-1 screening; if even this shows large safety margin → pathway closes |
| **Worst conceivable** | physically absurd combinations | not assessment — has no inferential value |

Anti-pattern to teach: assessments attacked for "worst-case thinking" are usually mixing bounding with conceivable. Discipline: every bounding parameter must remain *physically attainable*.

### 13.5 Measurement and modeling (how exposure numbers exist)

- **Measurement:** immunoassay/analytical chemistry on sampled compartments (soil cores, water, debris bags, pollen traps) — the dataset above is exactly this shape.
- **Modeling:** decay models + landscape GIS + dietary intake models extend sparse measurements to scenarios (weather years, field layouts).
- **Reconciliation:** models are validated against measurements; measurement gaps become model uncertainty (Module 16 §4).

## Step-by-step workflow

```text
1. List compartments + audiences for THIS trait/organism
2. Expression inventory (tissue × stage × level — Module 4)
3. Fate parameters per compartment (decay, adsorption, transport)
4. Pathway chains to each valued receptor (with bookkeeping factors)
5. Estimate intake per receptor (realistic + bounding)
6. Compare with hazard thresholds (dose-response — Module 8)
7. Close or escalate each pathway; state uncertainty
8. Feed monitoring: sample where the model puts exposure mass
```

## Example intake estimate (teaching-scale, simulated numbers)

Lacewing larva via contaminated prey:

```text
prey aphid on Bt tissue: tissue 12 ng/g → aphid gut content ~ 8 ng/g (×0.7 retention)
larva eats 5 aphids/day × 0.3 mg each = 1.5 mg prey/day
→ intake ≈ 8 ng/g × 1.5 mg = 0.012 ng/day vs lacewing IC50 (simulated: ≫1,000 ng/day)
→ margin > 10⁵ → pathway closed at Tier 1 (consistent with Exercise 2's null survival signal)
```

The structure — not the specific numbers — is the exam skill.

## Figures

<figure markdown>
![An exposure pathway chain from Bt maize to predators, with transfer factors at each step.](../../assets/risk/DIAGRAMS/05-exposure-pathway.png)

*Figure - An exposure pathway chain from Bt maize to predators, with transfer factors at each step.*
</figure>


## Interpretation

- Exposure converts *hazard lists* into *risk statements*; without it, everything is speculation in both directions.
- Duration × magnitude matters: low-level, months-long debris exposure ≠ brief, high pollen pulse; different organs, different organisms.
- The model's worst honest case belongs in the report — with its assumptions labeled.

## Common misconceptions

| Misconception | Reality |
|---|---|
| "Exposure = presence anywhere" | Exposure = contact at magnitude × duration for a specific receptor |
| "If it's measured in soil, soil organisms are at risk" | Intake must approach the organism's effect threshold |
| "Worst case = any imaginable scenario" | Bounding cases must remain physically attainable |
| "Models replace measurement" | Models extend measurement; unvalidated models are hypotheses |

## Exam points

- Reproduce the compartment model with audiences per compartment.
- Compute a half-life from a decay table (Lab 06) and interpret exposure windows.
- Build a 4-step pathway chain with bookkeeping factors and a margin-of-safety conclusion.
- Distinguish realistic vs bounding scenarios and their assessment roles.

## Quick-check questions

1. Why does debris dominate duration while runoff dominates *pulse* exposure — and which audiences care about each?
2. Expression rises 10× in a new event. Which pathway's margin closes first: pollen-margin larvae or soil fauna? Justify with the table.
3. Your model puts 90% of exposure mass in debris; where do monitoring resources go, and why not to the stream?
4. Construct one physically *unattainable* "worst case" and explain why including it would mislead.
5. A reviewer says: "You modeled intake, not measured it." Draft the one-paragraph defense (and concession).

---

*Next: [Module 14 — Food and Feed Safety](../../risk/modules/14-Food-and-Feed-Safety.md): the human/animal endpoint of the assessment chain.*---

## What you should know

Review the learning objectives and quick-check questions above. Then continue the sequence.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) banks.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [practical program overview](../labs/index.md).

[<- Herbicide Resistance and Weed Management](../modules/12-Herbicide-Resistance-and-Weed-Management.md) &middot; [Course home](../index.md) &middot; [Continue to next module ->](../modules/14-Food-and-Feed-Safety.md)
