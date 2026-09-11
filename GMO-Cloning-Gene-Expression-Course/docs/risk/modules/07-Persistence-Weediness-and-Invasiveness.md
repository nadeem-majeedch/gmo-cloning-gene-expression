# Module 7 — Persistence, Weediness and Invasiveness

**Level:** Intermediate

---

## Learning objectives

1. Distinguish **persistence**, **volunteer plants**, **weediness**, and **invasiveness** — four related but distinct concepts.
2. Explain how a GM trait could change each property, in which direction, and why most traits do not.
3. Work through the conceptual assessment workflow from trait characterization to ecological consequence.
4. Interpret fitness-component evidence (dormancy, dormancy-breaking, competitive ability) in context.

---

## Definition

- **Persistence** — survival and continuation of a population (here, of GM plants or their offspring) in a location over time, including seed banks.
- **Volunteer plants** — plants arising in a subsequent crop from seed shed by a previous crop (a *temporary* persistence phenomenon inside managed systems).
- **Weediness** — the property of thriving where humans don't want the plant: interfering with the intended crop/land use. A managed-system concept.
- **Invasiveness** — establishment and spread into *natural/semi-natural* communities beyond managed land, with self-sustaining populations.

These are nested but not equivalent: volunteers are persistence *inside* fields; invasiveness is persistence *plus spread* *outside* them.

## Why it matters

Persistence determines exposure duration (a seed bank is a memory of the GM trait for years); volunteers determine resistance-selection pressure (an uncontrolled HT volunteer is an unrefuged population); invasiveness is the pathway with the highest consequence class and the lowest reversibility. Assessment must therefore distinguish *how long the trait stays* from *whether it spreads*.

## Beginner explanation

A dropped tomato seed sprouting in your lawn is a volunteer — it dies with the first frost or mower. Wheat persisting three seasons in a field is persistence. A plant thriving in farm fields is weediness. A plant leaving farms, establishing in forests and displacing natives is invasiveness. Each step requires the plant to survive *more* conditions without human help — most crops are terrible at it, after millennia of domestication selection for human care.

## Scientific explanation

### 7.1 What decides each property

| Property | Decided by | Typical GM-trait relevance |
|---|---|---|
| Persistence | seed dormancy, seed bank dynamics, volunteer control practices | dormancy-altering traits matter; most traits don't touch this |
| Volunteer status | previous crop seed loss, control efficacy, herbicide options available | HT volunteers are harder to kill *with that herbicide* — management shifts to other tools |
| Weediness | competitive ability, reproduction in disturbed habitats, control difficulty | traits increasing competitive ability or reproduction in disturbed habitats |
| Invasiveness | broad ecological amplitude, dispersal machinery, self-sustaining populations in natural communities | rare; domestication usually removed wild-survival machinery — but case-by-case |

### 7.2 The crucial asymmetry: domestication

Thousands of years of selection made crops dependent: non-shattering seed heads, uniform germination (dormancy bred out), palatability (defense chemicals reduced), reliance on tillage/inputs. This is the *familiarity* baseline (Module 1 §2). A random gene insertion is unlikely to reverse domestication; a trait *deliberately targeting* wild-survival functions (dormancy, drought tolerance, perenniality) changes that calculus — the assessment asks precisely this question.

### 7.3 Assessment workflow

```text
Trait characterization (what does the edit/insert actually do?)
        ↓
Phenotypic comparison (Module 5 data: dormancy, vigor, reproduction vs comparator)
        ↓
Environmental conditions (managed field? field margin? natural community? stresses?)
        ↓
Reproductive fitness components (seed output, dormancy, survival, competition — vs counterpart)
        ↓
Persistence potential (seed-bank models; volunteer dynamics; feral population viability)
        ↓
Ecological consequence (if established outside farms: displacement? community change?)
        ↓
Risk characterization (Module 17) → management (Module 18)
```

### 7.4 Fitness components — what to measure

1. **Seed output** per plant (reproduction quantity)
2. **Seed dormancy/survival** in soil (persistence engine)
3. **Germination synchrony** (escape from control windows)
4. **Competitive ability** (vs crop and vs wild species)
5. **Stress tolerance** (drought, cold — niche expansion candidates)
6. **Dispersal** (shattering, wind, animal vectors)

A trait neutral on all six leaves persistence dynamics essentially unchanged — the standard expectation, verified case-by-case (Module 5 phenotypic data feed exactly these components).

### 7.5 The volunteer-specific logic for HT crops

A glyphosate-tolerant volunteer is not "more weedy" — it is *harder to control with glyphosate*. Consequence: rotation and herbicide-mix management adapt (other mode-of-action herbicides, tillage timing). Risk statement shape: "volunteer control failure probability rises if management relies on a single mode of action; resistance-management diversification (Module 12) addresses this."

### 7.6 Persistence modeling (conceptual)

Seed-bank dynamics: seed rain × survival × germination fraction, iterated over seasons with control efficacy — the *invasion-critical* parameter is whether the population growth rate exceeds 1 in the unmanaged context. Assessors ask: does the trait push λ over that line for any plausible habitat? (Module 25 §2 extends this to population-genetic and landscape models.)

## Real-world examples

- **Oilseed rape (canola) volunteers:** well documented as persistent volunteers in rotations — driven by secondary seed dormancy, *not* GM status; HT volunteers merely change which control chemistry works. Canonical case for separating "persistence (crop trait)" from "GM trait consequence."
- **Crops rarely feral:** maize cannot persist without human planting in most temperate zones (seed structure); a GMO maize's invasiveness assessment starts from that baseline.
- **The hypothetical alert class:** a GM perennial grass engineered for drought tolerance, grown near wild grasslands — trait function (stress tolerance) *is* a wild-survival function, so the persistence/invasiveness pathway stays open until data close it.

## Step-by-step example: interpreting a dormancy result

Suppose Module-5 phenotyping finds GM seed dormancy 18% vs comparator 15%, both within the reference-variety envelope (12–24%):

```text
Difference: +3 percentage points (not statistically robust, within envelope)
→ Biological relevance: negligible vs envelope
→ Persistence consequence: seed-bank models show <5% change in volunteer density
→ Risk statement: no meaningful change in persistence potential (uncertainty: moderate)
```

If instead the trait *doubled* dormancy (a plausible stress-tolerance side effect), the workflow would escalate: targeted seed-bank experiments, volunteer monitoring design, and possibly conditional approval with seed-bank triggers.

## Common misconceptions

| Misconception | Reality |
|---|---|
| "GM crops become superweeds" | Domesticated crops rarely gain wild-survival machinery from single traits; assessment is trait-specific, not categorical |
| "Volunteers are a GM problem" | Volunteers are a *crop* phenomenon; GM changes only which control tools work (for HT) |
| "Persistence outside farms is the default outcome" | Persistence requires surviving without human care — most crops fail fast |
| "More persistence = more risk, always" | Persistence amplifies exposure for whatever trait exists; if the trait is ecologically neutral, persistence matters mainly for seed purity and rotation management |

## Exam points

- Define the four terms and place them on the managed↔natural gradient.
- Explain the domestication baseline and which trait classes escape it.
- Walk the persistence workflow for a drought-tolerance trait in a grass.
- Explain why HT volunteer risk is a *management-system* statement, not a plant-fitness statement.

## Figures

<figure markdown>
![Persistence, weediness and invasiveness are distinct concepts with distinct evidence bases.](../../assets/risk/DIAGRAMS/16-persistence-weediness-invasiveness.png)

*Figure - Persistence, weediness and invasiveness are distinct concepts with distinct evidence bases.*
</figure>


## Quick-check questions

1. Classify: shattering seed heads restoring wild dispersal; herbicide-tolerant volunteer surviving a glyphosate pass; canola patch persisting 5 years at a rail loading point. Which concept does each illustrate?
2. Which fitness component would you measure first for a trait altering flowering time, and what pathway does it feed?
3. Why is "dormancy increased 3 percentage points, within envelope" not a persistence risk, while "doubled dormancy" would trigger new experiments?
4. Construct the risk statement for a drought-tolerant GM perennial near a nature reserve — hazard, exposure, consequence, uncertainty.
5. How does trait choice (vs management) determine whether invasiveness assessment closes at Filter 1?

---

*Next: [Module 8 — Non-Target Organisms](../../risk/modules/08-Non-Target-Organisms.md): the organisms around the crop that assessment must also protect.*---

## What you should know

Review the learning objectives and quick-check questions above. Then continue the sequence.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) banks.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [practical program overview](../labs/index.md).

[<- Gene Flow and Introgression](../modules/06-Gene-Flow-and-Introgression.md) &middot; [Course home](../index.md) &middot; [Continue to next module ->](../modules/08-Non-Target-Organisms.md)
