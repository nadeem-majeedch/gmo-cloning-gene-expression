# Module 11 — Resistance Evolution

**Level:** Intermediate → Advanced

---

## Learning objectives

1. Explain resistance evolution as ordinary natural selection under strong, sustained selection pressure.
2. Apply the **high-dose/refuge** strategy logic — why it works, what assumptions it needs, and how it fails.
3. Describe resistance monitoring (F2 screens, sentinel fields) and interpret allele-frequency data.
4. Connect resistance risk to the risk-assessment framework: it is a *predictable, manageable, but unavoidable* evolutionary consequence of continuous selection.
5. Use trade-off concepts to explain why resistance can carry costs — and why costs don't prevent resistance.

---

## Definition

**Resistance** is a heritable reduction in a pest population's susceptibility to a control agent. **Resistance evolution** is the increase in resistance allele frequency under selection. It is not a malfunction of the technology — it is textbook population genetics applied to whatever control measure (chemical, protein, cultural) exerts consistent pressure.

## Why it matters

For Bt crops, resistance is the *dominant* risk-management story: it threatens the technology's utility for everyone (a public-goods problem), it is monitored by name in regulatory conditions, and its management (refuges) is the clearest example of risk management built into the approval of a GM crop. For herbicide-tolerant systems, the parallel story is weed resistance (Module 12). Any course claiming scientific neutrality must present resistance as an expected dynamic to be managed — not a scandal, and not a non-issue.

## Beginner explanation

Imagine a field where every pest dies except the rare mutant born with a tolerance gene. Those survivors eat, mate, and pass the gene on. Repeat for years and the once-rare gene becomes common. The pesticide didn't *create* the mutation — selection *amplified* it. Refuge fields of non-GM crop act like a conservation zone for susceptible genes, diluting the resistant ones each generation.

## Scientific explanation

### 11.1 The selection dynamic

```text
Continuous selection pressure (every larva on Bt tissue tested)
   × standing genetic variation (resistance alleles present at low frequency)
   → differential survival (resistant genotypes survive the toxin)
   → reproduction (resistant survivors mate)
   → allele frequency rises (fast when rare-advantage is large and refuge absent)
   → field-level failure once frequency crosses practical thresholds
```

Key genetics:
- **Recessive resistance** (common for Bt): only homozygotes survive high toxin doses; heterozygotes die. This makes resistance *slow to start* (invisible while rare) and makes refuges *highly effective* (susceptible homozygotes from refuges swamp resistant alleles in mating).
- **Dominant/minor-gene resistance:** visible immediately, harder to manage by refuges alone.
- **Fitness costs:** resistant genotypes sometimes pay a cost off-toxin (slower development, lower fecundity). Costs slow but do not prevent evolution under sustained selection — and resistance to *multiple* toxins (pyramids) raises the needed cost level.

### 11.2 The high-dose/refuge strategy

| Component | Requirement | Purpose |
|---|---|---|
| High dose | toxin kills > 99% of susceptible *and* heterozygote larvae | makes resistance functionally recessive |
| Refuge | portion of crop (or area) without the toxin; pest population thrives there | supplies susceptible mates each generation |
| Combination | heterozygote × refuge cross → mostly susceptible offspring | dilutes resistance allele frequency per generation |

Success case: this architecture delayed practical resistance for over a decade across large areas (though compliance and biology both constrain it — see failures below). Failure modes:
- **No/unenforced refuges** → selection runs unopposed ([DATA/resistance](../downloads/resistance.md) Exercise 3 shows the simulated divergence).
- **Low-dose events** (trait expressed too low in some tissues) → heterozygotes survive → resistance becomes effectively dominant.
- **Cross-resistance** between similar toxins (same binding site in pyramids) → pyramid advantage vanishes.

### 11.3 Monitoring — how resistance is watched

| Method | What it detects | Sensitivity |
|---|---|---|
| **F2 screen / DNA-based allele test** | resistance *alleles* while still rare (per-generation frequency) | the early-warning system |
| **Sentinel/diagnostic-dose field bioassays** | phenotype-level susceptibility shift | detects later-stage change |
| **Field-failure reports** | practical control loss | the late alarm — regulatory trigger |

The monitoring *trigger* architecture: allele-frequency bands → stewardship response (refuge enforcement, alternative tools) → field failure = response escalation. Simulated dataset Exercise 3 shows exactly why frequency-based (not failure-based) monitoring matters: between gen 10 and 20 the no-refuge trajectory jumps from ~0.2% to >10% — an early-warning window that field-failure reports would miss.

### 11.4 Resistance cases (real-world, framed for assessment)

- **Bt cotton pink bollworm (India):** widespread resistance documented after years of intensive Bt cotton with limited refuge compliance; response included refuge + integrated practices + (in some regions) replacement strategies. *Assessment lesson:* biology (4+ generations/year, low dispersal) + social compliance failure = predictable outcome.
- **Bt corn rootworm (US maize):** resistance to several events documented where continuous maize + low/no refuge occurred; some cases implicated *non-recessive* inheritance. *Lesson:* high-dose assumption is testable per event and must not be assumed.
- **Success counter-case — pink bollworm eradication (US):* coordinated Bt + pheromone + sterile-insect program drove regional eradication; resistance *management* succeeded when embedded in an integrated program. *Lesson:* resistance risk is real but manageable with layered, enforced strategies.

*(Detailed case treatments in [Module 23](../../risk/modules/23-Case-Studies.md), Cases 5–6; [FAQ - resistance].)*

### 11.5 Trade-offs and multi-toxin dynamics

- **Fitness costs:** if resistant alleles cost fitness on refuge plants, refuges *select against* resistance there — the two-component synergy that makes high-dose/refuge work. Costs are event-and-allele specific; must be measured, not assumed.
- **Pyramids (stacked toxins, different binding sites):** require resistance to multiple loci simultaneously to survive — dramatically slows evolution *if* no cross-resistance and each toxin is high-dose.
- **Rotations vs sequences:** alternating toxins selects for *generalist* resistance over long horizons; sequencing decisions are resistance-modeling exercises (Module 25 §3).

## Step-by-step workflow: resistance risk assessment

```text
1. Biology of the target pest (generations/year, dispersal, mating system)
2. Toxin dose profile by tissue (is the high-dose assumption met per event?)
3. Baseline susceptibility & known variation in the pest population
4. Refuge design (size, placement, compliance mechanics) & model per-generation dilution
5. Monitoring design (F2/allele screens: n per site, frequency bands, triggers)
6. Cross-resistance audit of stacked/sequenced toxins
7. Compliance plan (education, contracts, enforcement reality)
8. Risk statement: expected useful life under design vs no-management scenarios
```

## Example data

From [DATA/resistance/bt_resistance_frequency.csv](../../assets/risk/DATA/resistance/bt_resistance_frequency.csv) (simulated high-dose/refuge model):

| Regime | Gen 0 | Gen 10 | Gen 20 | >1% reached |
|---|---|---|---|---|
| No refuge | 0.0001 | 0.002 | 0.109 | generation 14 |
| Structured 50% refuge | 0.0001 | 0.001 | 0.002 | not within 20 generations |

The nonlinearity is the lesson: resistance is nearly invisible for many generations, then accelerates — the monitoring window (frequency bands) exists precisely because waiting for field failure is too late.

## Figures

<figure markdown>
![Resistance allele frequency follows a slow-then-explosive S-curve; refuges stretch the slow phase.](../../assets/risk/DIAGRAMS/07-resistance-scurve.png)

*Figure - Resistance allele frequency follows a slow-then-explosive S-curve; refuges stretch the slow phase.*
</figure>


## Interpretation

- Resistance is *expected* under continuous selection; the assessment question is *how long the tool lasts under which management*, not whether evolution occurs.
- Compliance is a biological parameter, not just a policy nicety — models must include realistic refuge adherence.
- Frequency-based monitoring buys management time; failure-based response concedes it.

## Common misconceptions

| Misconception | Reality |
|---|---|
| "Bt resistance means the technology failed" | Resistance to *every* control tactic evolves; management goal is useful-life extension |
| "Refuges are bureaucratic hoops" | They are the biological engine of the strategy — non-compliance has measurable population-genetic costs |
| "Fitness costs solve resistance" | Costs slow evolution; rarely eliminate it under continuous selection |
| "Pyramids make resistance impossible" | Only with no cross-resistance + high dose per component + compliant refuges |

## Exam points

- Derive (in words) why recessive resistance + refuges delay resistance; what changes with dominant inheritance?
- Interpret an allele-frequency table: identify the monitoring window and the trigger logic.
- Explain cross-resistance's effect on pyramid strategy.
- Argue why compliance must enter the risk model, with the S23 scenario from the risk matrix.

## Quick-check questions

1. A pest has 6 generations/year and restricted dispersal. Refuges must be placed *how*, and why does dispersal matter?
2. From the table: what is the ratio of practical-resistance timing between regimes, and what does that imply for stewardship value?
3. Design a monitoring program (method, n, frequency, trigger) for a regional Bt maize system.
4. Why does a *low-dose* event effectively convert recessive resistance into a dominant problem?
5. Contrast the pink bollworm India-resistance and US-eradication stories: what one variable most differed?

---

*Next: [Module 12 — Herbicide Resistance and Weed Management](../../risk/modules/12-Herbicide-Resistance-and-Weed-Management.md): the same evolution, one trophic level up.*---

## What you should know

Review the learning objectives and quick-check questions above. Then continue the sequence.

## What you should be able to do

- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the [short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) banks.
- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).
- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).
- Hands-on practice: the [practical program overview](../labs/index.md).

[<- Biodiversity and Food Webs](../modules/10-Biodiversity-and-Food-Webs.md) &middot; [Course home](../index.md) &middot; [Continue to next module ->](../modules/12-Herbicide-Resistance-and-Weed-Management.md)
