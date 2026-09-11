# Lab 04 — Non-Target Organism Data Analysis

**Activity type:** Computational Exercise
**Duration:** 2.5 hours · **Level:** Intermediate

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Lab](Lab-03-Gene-Flow-Data-Analysis.md) · → [Next Lab](Lab-05-Resistance-Evolution-Simulation.md)
> 📚 Related Module: [Module 8 — Non-Target Organisms](../MARKDOWN/08-Non-Target-Organisms.md) · 📊 Dataset: [Exercise 2 — Non-target survival](../DATA/non-target/) · 📝 Assessment: [Data-Interpretation Questions](../ASSESSMENT/Data-Interpretation-Questions.md)

---

## Learning objectives

1. Estimate survival proportions with defensible confidence intervals (Wilson).
2. Distinguish *statistical* from *biological* significance using effect size + interval + comparator.
3. Explain why a laboratory hazard finding becomes a risk claim only after exposure quantification.
4. Compare an effect against the correct ecological comparator (insecticide regime, not idealised unsprayed crop).

## Background

Non-target assessment (Module 8) proceeds in tiers: laboratory toxicity → semi-field → field. A common failure mode is stopping at the laboratory stage, where doses are high and exposure is forced. The analysis taught here — effect size, interval, comparator — is the analytical core of every tier.

## Scientific principle

For survival data, each treatment group gives an estimate `p̂ = alive/n`. The **Wilson score interval** behaves well at small n and extreme proportions:

```text
CI = [ p̂ + z²/2n ± z·√( p̂(1−p̂)/n + z²/4n² ) ] / (1 + z²/n)
```

The ERA question is then threefold: (1) is the interval compatible with no effect? (2) is the *point estimate* biologically meaningful at field exposure? (3) compared with what alternative — the insecticide regime the Bt crop replaces?

## Materials/data

- `DATA/non-target/` — simulated survival of a beneficial predator and a parasitoid under: control diet, Bt-protein diet (high dose), Bt-pollen diet (field-realistic), conventional-insecticide exposure (positive realism control). n=200 per group. **Simulated data.**
- Python 3 (numpy, pandas, matplotlib); reference: `DATA/analysis_demo.py` Exercise 2.

## Safety

No biosafety concerns.

## Step-by-step workflow

1. **Load** survival counts; build the treatment × species table.
2. **Estimate** survival per group with Wilson 95% CIs.
3. **Contrast** Bt-pollen (field-realistic) vs control: difference in proportions + interval.
4. **Comparator analysis:** same contrast vs the conventional-insecticide group.
5. **Exposure mapping:** assign each treatment to its ERA tier (forced-dose lab / realistic pollen / field regime) and re-plot as a tiered figure.
6. **Write** the three-sentence risk statement (estimate → uncertainty → comparator).
7. **Challenge:** power analysis — what n would detect a true 3-point survival drop with 80% power?

## Data tables

| Species | Treatment | n | Alive | Survival | Wilson 95% CI |
|---|---|---|---|---|---|
| Predator | Control | | | | |
| Predator | Bt high-dose | | | | |
| Predator | Bt pollen (field) | | | | |
| Predator | Conventional insecticide | | | | |
| Parasitoid | (same four rows) | | | | |

## Calculations

- Wilson CI per group (show one hand calculation, then automate).
- Difference in proportions with Newcombe-style interval (or bootstrap) for Bt-pollen vs control.
- Power calculation for the 80%/3-point detection (normal approximation acceptable; state it).

## Expected results

(Simulated — per `analysis_demo.py`.) Bt high-dose may show a small, interval-compatible reduction; Bt pollen (field-realistic) indistinguishable from control; conventional insecticide shows a large, unambiguous reduction. The documented teaching pattern: **hazard at forced dose, no risk at realistic exposure, comparator regime is worse.**

## Interpretation

The three-sentence template students must produce, e.g.:

> "Predator survival under field-realistic Bt pollen was 0.93 vs 0.93 in controls (difference −0.003, 95% CI −0.06 to +0.05), compatible with no effect. The high-dose laboratory treatment suggests a hazard exists at sufficient dose. Under the comparator regime (single conventional insecticide application), survival fell to 0.62 — so the relevant ecological comparison favours the Bt system for this endpoint."

Note what this does *not* say: it does not say "Bt is safe for all non-targets" — one species, one route, one season.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| CI very wide | n too small per group | Report n; avoid over-interpretation; power analysis |
| "Significant" tiny difference | Very large n | Report effect size first; ask biological relevance (Module 16) |
| Comparator treated as 'control' | Design confusion | The comparator is a *treatment*, not a control; label clearly |

## Questions

1. Why is the conventional-insecticide group essential to the risk conclusion?
2. The high-dose group shows a small drop with CI [−0.08, −0.01]. Does this establish field risk? Why not?
3. What would make the parasitoid's exposure pathway different from the predator's?
4. Why is "no significant difference" not the same as "no effect"?

## Viva questions

1. Define non-target organism and give two examples with different trophic positions.
2. What is a tritrophic exposure pathway?
3. Why do regulatory non-target studies use maximum hazard dosing at tier 1?
4. Name two field-level confounders in non-target monitoring.

## Instructor answer key

- Q1: It supplies the ecological counterfactual — the regime Bt replaces; without it "small or no Bt effect" has no decision meaning.
- Q2: No — forced-dose exposure has no field counterpart; risk requires exposure quantification (Module 2/8); tier 1 is a hazard screen.
- Q3: Parasitoids develop inside hosts — exposure via host tissue/haemolymph (a tritrophic route), whereas the predator consumes prey whole; timing and dose differ.
- Q4: Underpowered test; CI may include large effects; equivalence needs an equivalence margin, not a failed significance test.

## Advanced challenge

Using the same simulated machinery, generate 1,000 bootstrap datasets and report the probability that the Bt-pollen effect appears "significant" (p<0.05) in at least one of ten endpoints — the garden of forking paths quantified. Connect to multiplicity in real dossiers.

---

*Previous: [Lab 03 — Gene-Flow Data Analysis](Lab-03-Gene-Flow-Data-Analysis.md) · Next: [Lab 05 — Resistance Evolution Simulation](Lab-05-Resistance-Evolution-Simulation.md)*
