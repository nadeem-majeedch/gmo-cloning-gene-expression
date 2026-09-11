# Lab 09 — Risk-Ranking Matrix

**Activity type:** Computational Exercise / Case Study
**Duration:** 2 hours · **Level:** Intermediate

---

## Learning objectives

1. Construct a qualitative risk matrix (likelihood × consequence) for identified GMO hazards.
2. Rank hazards consistently and justify placements with evidence, not intuition.
3. Demonstrate matrix sensitivity: how placements shift with scoring definitions.
4. Connect matrix output to management prioritisation and monitoring design.

## Background

Risk characterization (Module 17) often begins qualitatively: list hazards, estimate likelihood and consequence, rank. A risk matrix is a communication and prioritisation tool — not a measurement. Used carelessly it manufactures false precision; used well it makes the reasoning transparent and contestable. This lab teaches the disciplined use.

## Scientific principle

```text
Risk score = Likelihood score × Consequence score   (ordinal scales, e.g., 1–5)
```

Each axis is anchored with **written descriptors** (what makes a "3" a 3?), and every placement must cite the evidence used. Matrix cells map to action classes (accept / manage / monitor / reject). Sensitivity analysis asks: if two reasonable assessors score the same hazard, do they land in the same action class? If not, the *descriptors*, not the assessors, need work.

## Materials/data

- `DATA/risk-matrix/` — simulated scored hazard/exposure pairs from a hypothetical Bt-cotton ERA (hazard list with likelihood/consequence scores and one-line justifications). **Simulated data.**
- Hazard list from Lab 01's worksheet (your own version).
- Python (matplotlib heatmap) or paper grid.

## Safety

No biosafety concerns.

## Step-by-step workflow

1. **Define scales** — write anchor descriptors for likelihood 1–5 and consequence 1–5 *before* scoring anything (Table 1).
2. **Score** the course's standard hazard list (below) using those anchors; cite evidence per score.
3. **Plot** the 5×5 matrix with hazards placed; colour action classes.
4. **Cross-validate** — swap matrices with another group; identify placements where descriptors allowed divergence.
5. **Refine** descriptors that produced divergence; re-score; record placement changes.
6. **Link to management** — for the top three hazards, name the management/monitoring instrument each would trigger (Modules 18–19).
7. **Challenge:** replace multiplicative scoring with an ordinal 3×3 matrix; which hazards move action class?

## Data tables

**Table 1 — scale anchors (write your own):**

| Score | Likelihood anchor | Consequence anchor |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

**Table 2 — hazard scores:**

| Hazard | L | C | Score | Action class | Evidence cited |
|---|---|---|---|---|---|
| Resistance evolution (Cry1Ac) | | | | | |
| Gene flow to wild relatives | | | | | |
| Non-target predator effects | | | | | |
| Soil-community shift | | | | | |
| Volunteer persistence | | | | | |
| Horizontal gene transfer to microbes | | | | | |
| Herbicide-management shift | | | | | |
| Food/feed safety (new protein) | | | | | |

## Calculations

- Score = L × C; action-class map: <4 accept/monitor · 4–9 manage · 10–16 manage intensively · ≥17 reject/re-design (illustrative mapping — declare your own).

## Expected results

(Simulated dataset — documented by `analysis_demo.py`.) Resistance evolution scores highest (high likelihood under continuous selection; high consequence for trait durability); food/feed protein hazard scores low on likelihood given weight-of-evidence but non-trivial consequence; HGT-to-microbes scores low on consequence under current evidence. Cross-group placements will typically diverge by one cell on 2–3 hazards — that finding *is* the lesson about descriptor quality.

## Figures

<figure markdown>
![A qualitative risk matrix with pre-declared likelihood and consequence anchors.](../../assets/risk/DIAGRAMS/09-risk-matrix.png)

*Figure - A qualitative risk matrix with pre-declared likelihood and consequence anchors.*
</figure>


## Interpretation

- Matrices make prioritisation **explicit and contestable** — their value; they do not measure risk — their limit.
- Placement disputes almost always trace to likelihood anchors (rare-event calibration) — write those anchors with the most care.
- Every high-ranked hazard should map to a management or monitoring line in the ERA report; a top-ranked hazard with no instrument is an unmanaged risk, and the assessment must say so.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Everything lands mid-matrix | Averaging the axes ("3ish, 3ish") | Force extremity: anchors must describe *observable* endpoints |
| Scores drift between groups | Vague anchors | Rewrite as frequencies/magnitudes, not adjectives |
| Matrix used as final output | Tool misuse | Attach the evidence table; matrix is presentation, assessment is the reasoning |

## Questions

1. Why should anchors be written before scoring?
2. Two groups place the same hazard one cell apart. What — precisely — resolved it?
3. Which hazard in Table 2 has the largest gap between scientific evidence and matrix placement, and why?
4. Why is HGT-to-microbes scored low on consequence despite being famous in public debate?

## Viva questions

1. Distinguish qualitative, semi-quantitative, and quantitative risk characterization.
2. What makes a matrix cell "actionable"?
3. Why can a low-likelihood hazard still be the top priority?
4. How does the matrix connect to adaptive management?

## Instructor answer key

- Q1: Pre-declared anchors prevent post-hoc fitting of scores to preferred conclusions — the matrix equivalent of pre-registering hypotheses.
- Q2: One or more anchor descriptors were ambiguous; the fix is descriptor language, not scorer calibration (calibration invites groupthink).
- Q3: Typically HGT — public salience high, assessed consequence low (Module 9's evidence review); teaches the communication/assessment gap (Module 21).
- Q4: Under current evidence natural transformation of soil bacteria with plant transgenes is exceedingly rare and without demonstrated establishment — consequence is scored on evidence, not fame.

## Advanced challenge

Score all eight hazards twice: once with *your* evidence base, once deliberately withholding the comparator studies (sprayed-conventional baselines). Compare matrices. Write a short note on how comparator availability — not logic — changes risk rankings, and what that implies for regulatory data requirements.

---

*Previous: [Lab 08 — Dose-Response Analysis](../../risk/labs/Lab-08-Dose-Response-Analysis.md) · Next: [Lab 10 — Uncertainty and Sensitivity Analysis](../../risk/labs/Lab-10-Uncertainty-Sensitivity-Analysis.md)*

---

**Related resources:** [Practical workbook](../guide/workbook.md) - [Cheat sheet](../guide/cheat-sheet.md) - [Datasets](../downloads/datasets.md) - [Assessments](../assessment/index.md)

[Course home](../../index.md)
