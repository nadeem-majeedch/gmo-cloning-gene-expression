# Data-Interpretation Questions — GMO Environment and Risk Assessments

**15 questions on the course's simulated datasets · each: read → compute → interpret → limit**
*Instructor: Dr. Saira Azam, CEMB, University of the Punjab, Lahore. Datasets: [DATA/](../DATA/); answers reproducible via `DATA/analysis_demo.py`.*

---

**DQ1. [gene-flow]** From `gene_flow_by_distance.csv`, report mean frequency at each distance and state the direction/shape of decay. What single sentence conveys the management implication?
*Guide:* steep exponential-style decay from ≈3% (1 m) toward ≈0.02% (100 m); sentence: "buffer distances act on the steep segment; the tail persists, so management targets thresholds, not zero."

**DQ2. [gene-flow]** Fit ln(frequency) vs distance; report a, b, R². At what distance does the point estimate cross 0.001? Why is the upper-bound distance larger?
*Guide:* ln-linear fit; d* = ln(a/0.001)/b (≈15–30 m in the simulated data); the 95% bound sits above the point estimate, so a confidence-based buffer is longer — regulator-relevant distinction.

**DQ3. [non-target]** Compute survival proportions and Wilson 95% CIs for all treatments. Which comparisons are compatible with no effect?
*Guide:* field-realistic Bt-pollen vs control overlapping CIs → compatible with no effect; high-dose may show a small significant drop (hazard flag); conventional-insecticide group markedly lower (comparator realism).

**DQ4. [non-target]** A colleague reports "Bt pollen significant at p=0.04" for parasitoid emergence. Using the dataset, write the three-sentence correct interpretation.
*Guide:* effect size first (tiny), interval nearly touching null, multiplicity context; comparator (insecticide) dwarfs it; conclusion: flag for confirmation, not a risk conclusion — and no single-season claim (Lab 04 discipline).

**DQ5. [resistance]** Plot q vs generation for 0/10/20% refuge; report generation of q=0.5 each. Why is the curve flat, then steep?
*Guide:* S-curve — rare-recessive selection weak early (Δq ∝ q²), compounding late; refuges add susceptible mating throughout, stretching the flat phase dramatically (documented dramatic refuge effect).

**DQ6. [resistance]** Vary q₀ (1e-4 → 1e-2) at 10% refuge. Which sensitivity is larger — doubling q₀ or halving the refuge? Justify from the recursion.
*Guide:* typically halving refuge dominates (mating-pool dilution is the engine); q₀ matters mostly for timing onset. Both must be reported conservatively because both are hard to measure (Module 11).

**DQ7. [exposure]** From pollen-decay and protein half-life data, compute the field-edge receptor dose chain and its hazard quotient at 5/25/100 m.
*Guide:* multiply transfer factors through the pathway (Lab 06); HQ at 5 m largest but still ≪1 in simulated data; at 100 m margin widens by orders of magnitude; identify the dominant parameter (edge deposition).

**DQ8. [exposure]** Half-life estimate: from protein decay time series, fit exponential and report half-life with CI. Why does the CI matter more than the point?
*Guide:* HQ sensitivity to persistence (longer half-life → longer exposure windows); interval crossing days-to-weeks changes residue-timing guidance — point estimates invite false precision.

**DQ9. [composition]** Build the per-analyte table: % diff, CI, within-reference-range? Which analytes are (i) intended differences, (ii) flagged, (iii) benign?
*Guide:* classify with TOST at ±20% (Lab 07); intended: the trait's target metabolite; flagged: pattern/consistency test before calling unintended; benign: within-range single-test differences (multiplicity).

**DQ10. [composition]** One analyte: comparator 1.20, GM 1.34, CI of difference [0.06, 0.22], conventional range 0.9–1.9. Verdict chain?
*Guide:* significant, marginally outside ±20% at upper bound, well within natural range → not equivalent by test but biologically unremarkable; response: consistency check across sites, mechanism search; record as "within natural variation; monitored."

**DQ11. [dose-response]** Report LC50 and slope per species; compute the target→non-target selectivity margin. What field-exposure line would make the margin moot?
*Guide:* simulated margins span orders of magnitude; margin moot if field exposure approached the *non-target* LC50 — i.e., only at doses far above any documented pollen/tissue exposure; report as inequality when unmeasured.

**DQ12. [dose-response]** A shallow slope for the Collembolan means what for threshold-setting, given ±3× measurement error on concentration?
*Guide:* shallow β → response shifts greatly with small dose error; thresholds need uncertainty buffers (use CI, not point); ties to chronic/sublethal caveat — LC50 logic doesn't cover them (Lab 08 limits).

**DQ13. [risk-matrix]** Using pre-declared anchors, place eight hazards; then re-score without comparator studies. Which placements moved and why?
*Guide:* resistance ranks top with comparators (regime replaced is worse); non-target and protein-food hazards drop without comparators inflating them → comparator availability, not logic, shifts rankings (Lab 09 challenge).

**DQ14. [uncertainty]** Run the 10,000-draw MC; report median, 90% interval, and rank-correlation sensitivities. Which input dominates and what measurement campaign follows?
*Guide:* isolation-distance/decay parameter b dominates (documented); campaign: multi-distance pollen-decay study across seasons, prioritized over edge-frequency replication — sensitivity analysis as resource allocation.

**DQ15. [uncertainty]** The 90% interval straddles the 0.1% threshold. Write the regulatory sentence that neither over- nor under-states this.
*Guide:* "Median estimate 0.12% (90% CI 0.03–0.45%) exceeds the 0.1% threshold in ~55% of draws, driven by decay-parameter uncertainty; decision options are refined measurement of distance-decay or conservative buffer management while measured." — interval + driver + response, no adjectives (Lab 10 template).

---

*Datasets: [DATA/README](../DATA/README.md) · Related labs: [Lab 03](../LAB/Lab-03-Gene-Flow-Data-Analysis.md)–[Lab 10](../LAB/Lab-10-Uncertainty-Sensitivity-Analysis.md) · [Answer-Key](Answer-Key.md)*
