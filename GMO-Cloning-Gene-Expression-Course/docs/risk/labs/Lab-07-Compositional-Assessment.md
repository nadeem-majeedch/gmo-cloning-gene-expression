# Lab 07 — Compositional Assessment Data Interpretation

**Activity type:** Computational Exercise / Case Study
**Duration:** 2.5 hours · **Level:** Intermediate

---

## Learning objectives

1. Interpret compositional (proximate + key nutrients/anti-nutrients) comparisons between a GM line and its conventional comparator.
2. Apply equivalence-interval logic rather than raw significance testing.
3. Recognise the role of natural range data from conventional varieties (site-to-site, year-to-year variation).
4. Explain what compositional equivalence can and cannot establish (the bridge to Module 16's unintended-effects logic).

## Background

Food/feed safety assessment (Module 14) begins with **comparative composition**: is the GM crop materially equivalent to its conventional counterpart, allowing for the intended change? The comparator is not "perfectly identical" — conventional crops vary hugely with site, year, and genotype. Regulators therefore use reference ranges built from many conventional lines. This lab trains the reading of such tables — the single most common dossier artefact students will meet in practice.

## Scientific principle

For each analyte:

```text
Difference = GM mean − Comparator mean
95% CI on difference (or equivalence test against pre-set margins)
```

Then place the difference in context: is GM mean **within the conventional reference range**? An equivalence margin (e.g., ±20% of comparator mean, as used illustratively in regulatory guidance) plus a confidence-interval test (TOST: two one-sided tests) answers "equivalent" properly; a plain t-test only answers "detectably different," which low power can hide and high power always finds.

## Materials/data

- `DATA/composition/` — simulated proximates (protein, fat, fibre, ash, moisture), minerals, vitamins, anti-nutrients for GM line, near-isogenic comparator, and six conventional reference lines across sites. **Simulated data.**
- Python 3; reference: `DATA/analysis_demo.py` Exercise 6.

## Safety

No biosafety concerns.

## Step-by-step workflow

1. **Compute** GM vs comparator means, % difference, 95% CI for each analyte (Table 1).
2. **Equivalence test** at ±20% margins — classify each analyte equivalent / not equivalent / inconclusive.
3. **Reference-range check** — is the GM mean inside the pooled conventional range (min–max of the six reference lines)?
4. **Flag intended differences** (e.g., the trait's expected metabolic effect) and separate them from *unintended* flags.
5. **Interpret** — write a dossier-style conclusion paragraph for the compositional section.
6. **Challenge:** re-run the equivalence test with ±10% margins; how do conclusions move and what does that teach about margin choice?

## Data tables

**Table 1 (per analyte):**

| Analyte | Comparator mean | GM mean | % diff | 95% CI of diff | Within conventional range? | Verdict |
|---|---|---|---|---|---|---|
| Protein | | | | | | |
| Fat | | | | | | |
| Fibre | | | | | | |
| (…all analytes) | | | | | | |

**Table 2 — summary counts:** equivalent / not equivalent / inconclusive / intended-difference.

## Calculations

- Standard equivalence test (TOST) at the stated margin; show one worked analyte by hand.
- Pooled conventional reference range (min–max across lines/sites).
- Optional: mixed-model site effect to show why site, not GM status, often dominates variance.

## Expected results

(Simulated — documented by `analysis_demo.py`.) Most analytes are equivalent and within reference ranges; one analyte shows a small shift consistent with the intended metabolic change; one or two fall "inconclusive" at small margins — demonstrating that margin choice drives verdicts and must be pre-declared, not post-hoc.

## Interpretation

- **Equivalent ≠ identical:** compositional assessment supports "no indication of unexpected compositional change," not "proven safe."
- **Intended differences are expected:** e.g., a provitamin-A biofortified line *must* differ in carotenoids; the assessment asks whether *other* analytes are unremarkable.
- **A significant p-value on one analyte among fifty is expected by chance alone** — multiplicity logic (Module 24); look for consistency across sites and the pattern across related analytes before flagging.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Half the analytes "not equivalent" | Comparing to the wrong comparator (not near-isogenic, different maturity) | Verify comparator identity; check agronomic confounders |
| CI of difference absurdly wide | Too few sites/replicates | Report power limitation honestly; do not claim equivalence |
| One extreme outlier analyte | Unit/conversion error (fresh vs dry weight) | Normalise basis first; recompute |

## Questions

1. Why is a plain t-test the wrong tool for "is this crop compositionally equivalent?"
2. One analyte differs by 12% (CI 6–18%), inside the conventional range. Flag or not — and what further evidence would you want?
3. Why must the equivalence margin be pre-declared?
4. What can compositional analysis *never* detect?

## Viva questions

1. Define substantial equivalence and state one criticism of it.
2. What is a near-isogenic comparator and why does maturity matter?
3. Name three analyte classes always assessed in a crop dossier.
4. How do anti-nutrients figure in feed-safety assessment?

## Instructor answer key

- Q1: Equivalence is a claim about being *similar within margins*; a t-test tests difference and conflates power with equivalence — underpowered tests "pass" spuriously; TOST targets the right hypothesis.
- Q2: Within-range differences are typically not flagged alone; follow-up would seek consistency across sites/years and a plausible mechanism (or absence of one) before classification.
- Q3: Post-hoc margins invite verdict-shopping; pre-declaration keeps the equivalence claim falsifiable and comparable across dossiers.
- Q4: Compounds not measured, unknown modes of action, downstream product effects (processing), long-term dietary interactions — composition is one line of evidence, never the whole.

## Advanced challenge

Simulate a 50-analyte panel with no true GM effect and show that at α=0.05 roughly 2–3 analytes appear "significantly different" by chance. Then show how the reference-range check suppresses these false flags. Write the paragraph a risk assessor should include about multiplicity.

---

*Previous: [Lab 06 — Environmental Exposure Analysis](../../risk/labs/Lab-06-Environmental-Exposure-Analysis.md) · Next: [Lab 08 — Dose-Response Analysis](../../risk/labs/Lab-08-Dose-Response-Analysis.md)*

---

**Related resources:** [Practical workbook](../guide/workbook.md) - [Cheat sheet](../guide/cheat-sheet.md) - [Datasets](../downloads/datasets.md) - [Assessments](../assessment/index.md)

[Course home](../../index.md)
