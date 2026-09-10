# Lab 09 — Capstone Project: From Construct to Expression Pattern

**Type:** Integrated project (design + analysis + interpretation) · **Duration:** 2–3 weeks (checkpoints weekly)
**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression

> **Navigation:** [↑ Course Home](../README.md) · [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md) · 📊 [All datasets](../DATA/) · 📝 [Case studies](../ASSESSMENT/Case-Studies.md)

## 1. Project statement

Integrate the entire course: **design a construct → simulate its cloning and validation → design the expression experiment → analyze the (simulated) expression data → interpret spatiotemporally → defend the work.**

Students choose ONE of three tracks:

| Track | Focus | Deliverables lean toward |
|---|---|---|
| **A — Construct engineering** | Cloning design depth | Full design dossier + validation plan |
| **B — Expression analysis** | Data-analysis depth | Full analysis notebook + figures |
| **C — GMO case synthesis** | Applied/regulatory depth | Case dossier + risk/ethics analysis |

All tracks share a common spine (below) so grading is comparable.

## 2. Learning objectives

1. Integrate construct design, cloning, screening, and expression-analysis skills into one coherent project.
2. Apply course reporting standards (n, normalization, statistics, effect size, validation).
3. Defend design decisions in a viva-style presentation.
4. Connect technologies to a real biological or applied question.

## 3. Common spine (all tracks)

```text
Week 1: Question + design
   ├── Track A: construct map, cloning plan, diagnostic predictions
   ├── Track B: analysis plan for one provided dataset (which questions, which stats)
   └── Track C: GMO case selection + evidence inventory
Week 2: Execution (simulated) + data
   ├── Track A: in-silico assembly + screening simulation (Labs 1–4 tools)
   ├── Track B: run the pipeline; QC + figures
   └── Track C: mechanism + data summary + limitation analysis
Week 3: Synthesis + defense
   └── Report (≤ 8 pages) + presentation (10 min) + viva
```

## 4. Materials

All course datasets and tools; Modules 1–15; prior labs.

## 5. Equipment

Computer; Python venv; (no wet-lab component — the capstone is design/analysis/interpretation).

## 6. Safety

No organisms used. Track C must follow the Module 14 layering (evidence → risk → ethics → policy).

## 7. Procedure / workflow

### Track A — Construct engineering (example: conditional reporter)

1. Choose a developmental gene and a spatial question.
2. Design TWO constructs: (i) promoter-GFP reporter; (ii) CRISPRi-ready enhancer-test vector.
3. Full cloning plan: technique choice justified (Module 4 decision guide), primers, ratios, digests, screening plan, sequencing coverage.
4. Predict every failure mode and its detection method.
5. Write the *experiment-day protocol sketch* (conceptual, no operational parameters).

### Track B — Expression analysis (example: developmental time course)

1. Pick one dataset (time course, single-cell, or spatial).
2. Pre-register: question, hypotheses, QC thresholds, stats plan (before analyzing!).
3. Execute; produce ≥3 figures (profile, PCA/clusters, heatmap or spatial map).
4. Validate-plan: which result needs ISH/reporter follow-up, and how?
5. State limitations explicitly (dropout, resolution, n).

### Track C — GMO case synthesis

1. Choose a real GMO case (course list or approved alternative).
2. Reconstruct: modification type, construct logic, mechanism, evidence for benefit, documented risks, regulatory status (**verify current status — cite sources**).
3. Apply the Module 14 four-layer analysis.
4. Propose the *next experiment* that would resolve the case's main open question.

## 8. Expected results

- Report ≤8 pages (or notebook + summary), figures with captions, references (course standard: no fabricated citations).
- Presentation 10 min + 5 min questions.

## 9. Data table (report template)

| Section | Content required |
|---|---|
| Question | 1 paragraph, falsifiable |
| Design | maps/plan/statistics plan |
| Results | figures + captions |
| Interpretation | what is and is NOT proven |
| Validation plan | next experiments |
| References | verifiable sources only |

## 10. Calculations

Track-dependent (ratios, digest predictions, FC/ΔΔCt, FDR counts, gradient r).

## 11. Interpretation

Every track ends with the same question: **what claim does your evidence support, at what resolution, and what is the minimal next experiment?**

## 12. Troubleshooting (project-level)

| Symptom | Likely cause | Fix |
|---|---|---|
| Question too broad | Scope creep | One gene, one tissue, one question |
| Figures without captions | Reporting-standard gap | Caption = what/where/n |
| Overclaiming | Interpretation gap | Explicit "not proven" list |

## 13. Post-project questions

1. Which single course module was most load-bearing for your track, and why?
2. Where did your original plan change, and what did that teach about design?
3. State one thing your data *cannot* say (resolution or validation limit).

## 14. Viva questions (examples)

1. Defend your enzyme/technique choice against the alternatives.
2. Why is your reference gene / normalization choice valid here?
3. Your reporter disagrees with endogenous ISH — reconcile.
4. Which regulatory framework applies to your Track-C case in TWO different jurisdictions?

## 15. Instructor notes / answer key (summary)

- Rubric (100 pts): Question & design 25; Execution/analysis 25; Interpretation & validity 25; Defense & synthesis 15; Reporting standards 10.
- Model dossiers for one example per track are in the [Workbook](../WORKBOOK/GMO-Cloning-Gene-Expression-Lab-Workbook.md).

## 16. Advanced challenge

Design the **F0 experiment** that would combine your Track-A construct with a Track-B readout in zebrafish: which reagent goes into which tissue at which stage (conceptually), what controls, and what result would falsify your hypothesis?
