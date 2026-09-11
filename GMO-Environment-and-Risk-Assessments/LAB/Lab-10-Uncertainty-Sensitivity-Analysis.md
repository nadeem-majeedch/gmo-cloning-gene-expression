# Lab 10 — Uncertainty and Sensitivity Analysis

**Activity type:** Computational Exercise
**Duration:** 3 hours · **Level:** Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Lab](Lab-09-Risk-Ranking-Matrix.md) · → [Next Lab](Lab-11-Case-Study-Regulatory-Assessment.md)
> 📚 Related Modules: [Module 16 — Unintended Effects and Uncertainty](../MARKDOWN/16-Unintended-Effects-and-Uncertainty.md), [Module 17 — Risk Characterization](../MARKDOWN/17-Risk-Characterization.md) · 📊 Dataset: [Exercise 10 — Uncertainty](../DATA/uncertainty/) · 📝 Assessment: [Data-Interpretation Questions](../ASSESSMENT/Data-Interpretation-Questions.md)

---

## Learning objectives

1. Propagate parameter uncertainty through a risk-relevant model with Monte Carlo simulation.
2. Separate variability (real-world heterogeneity) from uncertainty (state of knowledge).
3. Rank input parameters by influence on the output (sensitivity analysis) and justify resource allocation for further measurement.
4. Communicate an interval-based conclusion without false precision.

## Background

Every estimate in an ERA — outcrossing frequency, LC50, exposure dose — carries uncertainty. Module 16 teaches the taxonomy; this lab runs the machinery. The model: an **outcrossing-estimate** model combining edge frequency, decay constant, field area, and flowering overlap into a field-scale transgene-flow estimate. Students propagate uncertainty from the four inputs and discover which input dominates — the result changes what they would measure next.

## Scientific principle

Monte Carlo: draw each input from its stated distribution N times; compute the output each time; the output distribution *is* the uncertainty statement.

```text
F = a · exp(−b·d) · S · O     (edge freq, decay, area factor, overlap factor)
```

Sensitivity: correlation (or rank-correlation) of each input with the output across draws — a practical proxy for "which uncertainty matters."

## Materials/data

- `DATA/uncertainty/` — simulated parameter distributions (mean, CI, shape) for the four model inputs, plus 10,000-draw output summary. **Simulated data.**
- Python 3 (numpy); reference: `DATA/analysis_demo.py` Exercise 10.
- Output from Lab 03 (your fitted a, b) may be substituted for the defaults.

## Safety

No biosafety concerns.

## Step-by-step workflow

1. **Define the model** on paper — inputs, units, plausible ranges (Table 1).
2. **Set distributions** — uniform (sparse knowledge) vs normal (measured) vs lognormal (positive quantities); justify each choice.
3. **Run** 10,000 draws; plot the output distribution (histogram + 90% interval).
4. **Sensitivity** — rank inputs by rank-correlation with output (Table 2).
5. **Tornado plot** — effect of moving each input from its low to high bound, one at a time.
6. **Variability vs uncertainty** — treat flowering overlap as *variability* (site-years) and edge frequency as *uncertainty* (measurement); report the two intervals separately.
7. **Challenge:** add correlation between two inputs (a and b are often anti-correlated in fits) and show the effect on the output interval.

## Data tables

**Table 1 — input definitions:**

| Input | Baseline | Distribution + justification | Source |
|---|---|---|---|
| Edge frequency a | | | |
| Decay constant b | | | |
| Field-area factor S | | | |
| Overlap factor O | | | |

**Table 2 — sensitivity output:**

| Rank | Input | Rank-correlation with output | Action: measure better? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Calculations

- 10,000-draw Monte Carlo; report median, 5th, 95th percentiles.
- Rank (Spearman) correlations; one-line interpretation each.
- Interval comparison: deterministic (best-estimate inputs) vs probabilistic interval — quantify the gap false precision was hiding.

## Expected results

(Simulated — documented by `analysis_demo.py`.) The deterministic point estimate sits inside a wide 90% interval; **isolation-distance/decay parameter (b) dominates the output** (the documented interpretation: isolation distance dominates, not edge outcrossing). Acting on the ranking: the next field campaign should measure distance-decay more precisely, not the near-field frequency — a concrete, defensible resource-allocation statement.

## Interpretation

- The ranking converts uncertainty from a paragraph of hedging into a **decision about what to measure** — this is the practical payoff of sensitivity analysis.
- An interval that crosses a management threshold is *not* an excuse for inaction: it triggers either targeted measurement or conservative management (Module 19 adaptive logic).
- Reporting format that earns marks: "Median field-scale flow 0.12% (90% interval 0.03–0.45%), dominated by uncertainty in the distance-decay parameter; the median exceeds the 0.1% threshold in X% of draws, driven principally by parameter b."

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Interval implausibly narrow | Inputs treated as exact | Every input needs a distribution — audit Table 1 |
| Output distribution skewed wildly | Lognormal inputs with large σ | Check parameter units and tails; plot input draws |
| Sensitivity ranks unstable | Too few draws | Increase N; use rank correlation (robust to monotone noise) |

## Questions

1. Why is rank correlation preferred over Pearson for sensitivity here?
2. Your 90% interval spans a management threshold. Give three defensible responses and the assumptions each carries.
3. What does it mean that parameter b dominates — in terms of the *biology* of pollen flow?
4. Why report variability and uncertainty separately?

## Viva questions

1. Define measurement, model, and sampling uncertainty with an ERA example each.
2. What is a tornado plot used for?
3. Distinguish worst-case, plausible-worst-case, and central estimates.
4. Why is "conservative" not automatically "better" in risk assessment?

## Instructor answer key

- Q1: Relationships with the output may be monotone but non-linear; rank correlation captures influence without linearity assumptions and is outlier-robust.
- Q2: (i) Measure the dominant parameter better (costs time, buys precision); (ii) manage conservatively now (acts as if near-worst case); (iii) redesign the option/decision to be robust across the interval (robustness framing). Each embeds a different attitude to the cost of error.
- Q3: Decay with distance is the strongest lever on *total* field-scale flow — it aggregates every far-field receptor; edge frequency, by contrast, affects only a thin band.
- Q4: They answer different questions and demand different remedies — variability needs spatial/temporal design (more sites/years), uncertainty needs better measurement; conflating them misdirects both.

## Advanced challenge

Replace the fixed distributions with a two-level analysis: *within-model* Monte Carlo (as above) plus *between-model* comparison (exponential vs power-law decay from Lab 03). Report the model-uncertainty contribution to the total interval — the honest way to present structural uncertainty in a regulatory summary.

---

*Previous: [Lab 09 — Risk-Ranking Matrix](Lab-09-Risk-Ranking-Matrix.md) · Next: [Lab 11 — Case-Study Regulatory Assessment](Lab-11-Case-Study-Regulatory-Assessment.md)*
