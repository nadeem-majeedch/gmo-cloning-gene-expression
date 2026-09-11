# Module 10 — Biodiversity and Food Webs

**Level:** Intermediate

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](09-Soil-Ecosystems-and-Microbial-Interactions.md) · → [Next Topic](11-Resistance-Evolution.md)
> 🧪 Related Practicals: [Lab 04](../LAB/Lab-04-Non-Target-Data-Analysis.md) · [Lab 09](../LAB/Lab-09-Risk-Ranking-Matrix.md) · 📊 Data: [Non-target survival](../DATA/non-target/) · [Risk matrix](../DATA/risk-matrix/) · 📝 Assessment: [MCQs](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Environment-Risk-Assessment-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Environment-Risk-Assessment-FAQs.md)

---

## Learning objectives

1. Describe trophic structure and how effects propagate through food webs.
2. Distinguish species-level, community-level, and ecosystem-service-level questions.
3. Explain why a laboratory finding does not automatically translate into ecosystem-level risk — and what does scale up.
4. Name biodiversity indicators used in monitoring and how they are chosen.
5. Articulate the comparison-baseline problem: against what do we measure biodiversity change?

---

## Definition

**Biodiversity** — variability among living organisms at genetic, species, and ecosystem levels. **Food web** — the network of who-eats-whom in a community. **Community-level effect** — a change in composition, richness, or interaction structure across species. **Ecosystem services** — benefits humans derive from ecosystem processes (pollination, pest suppression, decomposition, nutrient cycling).

## Why it matters

Single-species tests (Module 8) cannot show everything: real risk can hide in weak links, compensatory responses, and indirect chains. Conversely, public debate leaps from one lab species to "ecosystem collapse" — a claim that needs community-level evidence. Assessment must connect the tiers honestly: which mechanisms *can* scale, and which data would demonstrate that they did?

## Beginner explanation

A food web is a city's restaurant economy: plants cook the food (producers), herbivores eat the meals (primary consumers), predators eat the diners (secondary), decomposers recycle the leftovers. Remove or sicken one participant and the effects ripple — but webs are also *buffered*: competitors expand, prey switch, generalists compensate. The question is never "could X affect the web?" (almost anything could) but "how much, through which links, compared with what baseline?"

## Scientific explanation

### 10.1 From protein to ecosystem: the transmission ladder

```text
Molecular interaction (protein binds receptors in susceptible taxa)
  → individual effect (mortality / sublethal change)
    → population effect (density change IF exposure is broad enough)
      → community effect (composition shifts, link rewiring)
        → ecosystem-service change (pollination / pest suppression / decomposition)
```

Each arrow requires *amplification conditions*: enough exposed individuals, weak compensation, sensitive functional redundancy being low. Most lab-detectable effects die at the first arrow because exposure is narrow (Module 13). The risk assessor's job is identifying *which pathways could realistically pass each arrow* — and requesting the data that would show it.

### 10.2 Buffering mechanisms (why scaling is hard)

| Buffer | Mechanism |
|---|---|
| Density compensation | surviving competitors expand into vacated niches |
| Functional redundancy | multiple species perform similar roles |
| Prey/pollen switching | consumers shift resources |
| Spatial refugia | unexposed patches reseed populations |
| Indirect benefits | e.g., fewer insecticide sprays help natural enemies (Bt systems) |

### 10.3 Indicators — what gets measured

| Indicator type | Examples | Strengths/limits |
|---|---|---|
| Taxonomic richness/diversity | species counts, Shannon (Lab 06 style) | intuitive; sensitive to sampling effort |
| Functional groups | predators/parasitoids ratios, decomposer guilds | closer to services; classification judgment |
| Process rates | decomposition, pollination success, predation rates | service-relevant; labor-intensive |
| Sentinel/population trends | butterfly larval counts, bird indices | public salience; attribution hard |
| Landscape metrics | habitat area/connectivity in GM vs non-GM mosaics | context for all of the above |

Good monitoring programs (Module 19) pick *few* indicators with clear trigger thresholds, not long unmeasurable lists.

### 10.4 The comparison-baseline problem

"Biodiversity declined in the GM region" is meaningless without the counterfactual. Legitimate baselines:

1. **Conventional-counterpart fields** (same crop, standard practice) — isolates GM effect.
2. **The alternative practice** (e.g., insecticide-sprayed non-Bt) — the *policy-relevant* comparison: what happens if the GMO is not used?
3. **Pre-change baseline** (time series) — captures trends independent of the intervention.
4. **Reference/natural sites** — context for magnitudes.

Different baselines answer different questions; disagreements about "GMO biodiversity effects" often trace to silently switching baselines. Assessment should state its baseline explicitly — and where possible report against more than one.

### 10.5 Evidence structure at community scale

- **Farm-scale comparisons** (Bt vs conventional fields, paired designs) — detect net community differences.
- **Landscape studies** — correlate GM-crop area with regional trends (attribution caveat: many confounders).
- **Long-term surveillance** — trend detection with triggers (Module 20).
- **Meta-analysis** — the strongest synthesis tool; the multi-study Bt/non-target literature is a canonical case of converging on "net effects small; management context dominates."

## Real-world example threads

- **Bt cotton in China (farmer-scale):** reduced insecticide spraying → documented increases in beneficial arthropods; a community-level *positive* indirect effect running through management change.
- **Herbicide-tolerant crop systems:** the biodiversity question moved to farmland flora and seed resources (weed seed banks feed farmland birds) — effects of *herbicide programs*, not the tolerance protein; a pure example of management-mediated community effects (Module 12).
- **Monarch follow-ups:** the pathway's community relevance was settled by exposure measurement across the landscape, not more lab toxicity — a demonstration that *population-relevance lives in exposure geography*.

## Interpretation

- Lab → field is a *modeling* step, not an automatic one: state the amplification conditions required.
- Both "harm found in lab" and "no harm found in field" can be true simultaneously; they answer different questions at different tiers.
- Service-level framing (pollination, pest suppression) often resolves disputes: services integrate direct + indirect effects and are what society actually protects (problem formulation, Module 3 §3.1).

## Common misconceptions

| Misconception | Reality |
|---|---|
| "One affected species = ecosystem damage" | Communities buffer; scaling requires exposure breadth + weak redundancy |
| "No community change = no individual effects" | Subtle individual effects can hide under compensatory dynamics |
| "Biodiversity = species counts" | Genetic, functional, and structural diversity also matter (indicators differ) |
| "GM vs wild comparisons answer policy questions" | Policy relevance usually lives in GM vs *alternative practice* |

## Exam points

- Draw the transmission ladder with the amplification conditions at each arrow.
- Explain three buffering mechanisms and what they imply for detecting effects.
- Contrast the two key baselines (counterpart vs alternative practice) with an example where they give different answers.
- Name two indicator types and a good trigger design for one.

## Quick-check questions

1. A predator population declines 10% in a 5-year landscape study correlating with GM crop area. List three confounders and one design strengthening attribution.
2. Which amplification condition is most likely to fail for a pollen-borne effect limited to field margins? Justify.
3. Why can Bt fields show higher invertebrate diversity than sprayed conventional fields while a small direct protein pathway still exists?
4. Design a two-indicator monitoring set for a new HT crop's farmland-biodiversity pathway, with trigger thresholds.
5. Explain, with the ladder, why "the protein kills larvae in a dish" and "the region's butterflies are fine" are compatible findings.

---

*Next: [Module 11 — Resistance Evolution](11-Resistance-Evolution.md): the evolutionary dynamic that has defined GMO risk management in practice.*
