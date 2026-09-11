# Module 15 — Allergenicity and Toxicity Assessment

**Level:** Intermediate → Advanced

> **Navigation:** [↑ Course Home](../README.md) · ← [Previous Topic](14-Food-and-Feed-Safety.md) · → [Next Topic](16-Unintended-Effects-and-Uncertainty.md)
> 🧪 Related Practicals: [Lab 08](../LAB/Lab-08-Dose-Response-Analysis.md) · [Lab 07](../LAB/Lab-07-Compositional-Assessment.md) · 📊 Data: [Dose-response](../DATA/dose-response/) · 📝 Assessment: [MCQs](../ASSESSMENT/MCQs.md) · 📌 [Cheat Sheet](../CHEAT-SHEET/GMO-Environment-Risk-Assessment-Cheat-Sheet.md) · ❓ [FAQ](../FAQ/GMO-Environment-Risk-Assessment-FAQs.md)

---

## Learning objectives

1. Explain why **no single test establishes allergenic safety** and describe the weight-of-evidence approach.
2. Walk the allergenicity assessment lines: source, sequence identity, epitope scan, pepsin resistance, heat stability, glycosylation, serum screening where available.
3. Structure a toxicity assessment: hazard identification → dose-response → exposure → risk, with correct endpoint vocabulary.
4. Interpret dose-response data (IC50/NOAEL-style logic) without inventing values.
5. Distinguish the toxicological question for a *new protein* from that for a *whole food*.

---

## Definition

**Allergenicity assessment** evaluates the potential of a newly expressed protein (or food) to sensitize or elicit allergy, by weight of evidence across structured lines of inquiry. **Toxicity assessment** evaluates adverse effects of substances under defined exposure, through hazard identification and dose-response characterization.

## Why it matters

Allergy and toxicity are the two concrete health mechanisms a new food component could act through. Both sciences are comparative and tiered; both are heavily standardized in GMO frameworks (Codex-aligned weight-of-evidence for allergenicity; classical toxicology for proteins and stacks). Getting their *logic* right prevents both over- and under-claiming.

## Beginner explanation

For allergy, there's no standalone "allergy test" for a new protein. Assessors ask a sequence of narrowing questions: Is it from an allergy-known source? Does it look like known allergens? Would it survive digestion and cooking? Does it resemble allergens in blood tests? Each line can *raise* a flag or *lower* concern; the conclusion is the pattern, not any single result. For toxicity, the core is simpler: give increasing doses, watch for effects, find where effects begin — then compare real exposures to that point.

## Scientific explanation

### 15.1 Allergenicity — the weight-of-evidence lines

| Line | Question | Interpreting |
|---|---|---|
| **Source identity** | Is the donor organism allergenic (e.g., derived from a known allergen family)? | allergenic sources ⇒ burden of proof rises sharply; products of such sources often declined or heavily tested |
| **Sequence identity to known allergens** | sliding-window identity; contiguous (e.g., ≥ 8 aa exact match conventions) & overall identity thresholds | hits → assume cross-reactivity risk unless serum evidence excludes |
| **Epitope scanning** | linear epitope motifs vs allergen databases | supportive, not definitive (conformational epitopes exist) |
| **Pepsin resistance (SGF digestibility)** | does it persist in simulated gastric fluid like stable allergens do? | rapid digestion lowers (not eliminates) concern; persistent proteins raise it |
| **Heat/process stability** | does cooking inactivate it? | heat-labile proteins lose food-allergy relevance; heat-stable ones resemble classic allergens |
| **Glycosylation status** | plant glycosylation can alter immunogenicity | characterized case-by-case |
| **Serum screening (where source/identity warrants)** | IgE binding in sera of allergic donors | positive ⇒ strong flag; negative with poor rationale ⇒ limited value |

**The honest bottom line (required phrasing):** *no single test establishes allergenic safety.* A protein can pass every screen and still, in principle, act as a novel sensitizer; the weight-of-evidence framework exists because allergy mechanisms are complex and partly conformational. Conversely, one positive line (e.g., serum IgE) is decisive caution. Regulatory history's much-cited cautionary case: a Brazil-nut 2S albumin transferred to soybean provoked sera reactivity in allergic patients and the product was abandoned pre-market — evidence lines worked *as designed*.

### 15.2 Toxicity — the classical structure

```text
Hazard identification  (what adverse effect could this substance cause?)
      ↓  mode-of-action & structure (bioinformatics; enzyme-class history)
Dose-response          (graded responses; NOAEL / BMD / IC50)
      ↓  acute oral (mouse) as the protein-tier screen
Exposure               (dietary intake, processing factor, frequency)
      ↓  margins of exposure (MOE = threshold / estimated intake)
Risk characterization  (MOE size + uncertainty)
```

Key teaching discipline: **do not invent values.** The skill is the *structure*: where each number comes from (a study with n, endpoints, design), what the margin means, and how uncertainty moves the conclusion. The simulated dose-response dataset ([DATA/dose-response](../DATA/dose-response/), Lab 08) lets students *fit* an IC50 (~40 ng/cm², illustrative) and see the sigmoid logic — while the lab handout reminds that regulatory submissions use validated GLP designs, not teaching fits.

### 15.3 New protein vs whole food (two different questions)

| Question | Object | Method |
|---|---|---|
| "Is this protein toxic?" | purified new protein | acute oral; mode-of-action; margins vs intake |
| "Is this food safe as a matrix?" | the whole grain/meal | compositional equivalence + 90-day rodent whole-food study + livestock performance (Module 14) |

Whole-food chronic-dosing designs face the classic limitation: you cannot feed huge excess of any food without nutritional imbalance confounding everything — which is *why* the matrix question is answered compositionally, not by mega-dose gavage. Students should be able to argue this point precisely; it is the most common public misunderstanding of "no long-term feeding study."

### 15.4 Endpoints and vocabulary (checklist)

- NOAEL/LOAEL; benchmark dose (BMD); IC50/EC50/LC50 (population-level effect sizes)
- Margin of exposure (MOE); margin of safety
- Acute vs subchronic vs chronic (and when each applies: protein screen → acute; matrix → subchronic)
- GLP (good laboratory practice) — data quality standard for regulatory studies
- Weight of evidence; concordance

## Step-by-step workflow (allergenicity, condensed)

```text
1. Source & family audit (allergenic donor? known family?)
2. Sequence scans (identity + contiguous-match conventions)
3. Digestibility (SGF) + heat stability
4. Glycosylation characterization (if expressed in plants)
5. Serum IgE screens triggered by steps 1-2
6. Integrate: pattern across lines → conclusion + uncertainty
7. Post-market note: any surveillance hooks if concerns were marginal
```

## Example data (dose-response teaching fit)

[DATA/dose-response/dose_response_larvae.csv](../DATA/dose-response/dose_response_larvae.csv): 7 doses × 8 reps × 12 larvae; hill fit → IC50 ≈ 42 ng/cm², slope ≈ 1.6; zero-dose control anchors the top plateau. Interpretation discipline: the *hazard* is characterized; *risk* requires placing real environmental/dietary exposures against this curve (Module 13).

## Interpretation

- Allergenicity: pattern-over-single-line logic; decisive lines are source identity and serum reactivity, not digestibility alone.
- Toxicity: margins-of-exposure framing converts dose-response into risk language.
- Both feed the Module 14 stack; both demand explicit uncertainty statements.

## Common misconceptions

| Misconception | Reality |
|---|---|
| "Digestible = can't be an allergen" | Rapid digestion lowers concern; some allergens transiently resist; weight of evidence still needed |
| "90-day rodent study is missing → unsafe" | Matrix logic: compositional + whole-food design constraints; protein-tier tests carry the novel-molecule question |
| "IC50 from a teaching dataset is a regulatory number" | Teaching numbers illustrate structure; regulatory values come from validated GLP studies |
| "One serum test settles allergenicity" | Sera are powerful *when indicated and well-panelled*; interpretation needs context |

## Exam points

- List ≥ 5 weight-of-evidence lines for allergenicity with correct interpretation direction.
- State the Brazil-nut-2S-soybean case as the framework's historical validation.
- Draw the toxicity structure with MOE definition.
- Argue the new-protein vs whole-food distinction and why mega-dose food studies are confounded.

## Quick-check questions

1. A protein shows 6/8 contiguous-identity hits to a pollen allergen. What does the framework now require?
2. Why is heat stability *safety-relevant* evidence rather than a technical detail?
3. Write the MOE sentence for: NOAEL-equivalent threshold 100 (units arbitrary), estimated intake 0.1 — and state what remains uncertain.
4. Why can't a 90-day rodent study use 1000× food doses, while an acute oral protein gavage can?
5. Which two lines of allergenicity evidence are *decisive* (can stop or green-light alone), and why are others supportive only?

---

*Next: [Module 16 — Unintended Effects and Uncertainty](16-Unintended-Effects-and-Uncertainty.md): what happens when the picture is incomplete.*
