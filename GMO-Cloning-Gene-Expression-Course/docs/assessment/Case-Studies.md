# Assessment — 12 Case-Based Questions + 10 Experimental/Data-Interpretation Questions

**Model answers:** [Answer-Key.md](../assessment/Answer-Key.md) · Background reading: [Case-Studies module](../modules/13-Applications-and-Case-Studies.md)

---

## Part I — Case-based questions (12)

**Case 1 — The failing Bt field.** A region growing Bt cotton for 8 years reports rising insect damage.
(a) What evolutionary process explains this? (b) Why do refuge strategies slow it? (c) Propose two monitoring data streams a program should collect.

**Case 2 — Golden Rice approval.** A country must decide on GR2E deployment.
(a) Summarize the mechanism. (b) What food-safety evidence would you require? (c) Separate the scientific, ethical, and policy layers of the decision (Module 14 framework).

**Case 3 — Insulin to the clinic.** Explain why *E. coli* was viable for insulin production but not for a glycoprotein like EPO, and what host features each requires.

**Case 4 — The GFP that vanished.** A student's promoter-GFP line shows bright signal at F0 but fading lines over generations.
(a) List three mechanisms (silencing, position effects, breeding-away). (b) Which molecular confirmation distinguishes them?

**Case 5 — A confusing disease model.** An *apoE*⁻/⁻ mouse model shows diet-dependent lesions but a new drug fails in trial.
(a) What does this teach about model validity? (b) Name the three validity types used in modeling.

**Case 6 — The in-frame escape.** A CRISPR knockout targeting exon 2 yields a founder with a 3-bp deletion, healthy phenotype.
(a) Why can this happen? (b) Design two follow-ups to establish whether function is truly lost.

**Case 7 — Edited mushroom controversy.** A non-browning mushroom produced by CRISPR knockout historically escaped USDA regulation in the US.
(a) Why (process vs product framing)? (b) Contrast with an EU-style process-based assessment outcome.

**Case 8 — Antennapedia.** A fly misexpresses a Hox gene and grows legs where antennae belong.
(a) What does this demonstrate about Hox function? (b) Why does colinearity suggest regulatory/chromatin mechanisms?

**Case 9 — Bicoid rescue.** A *bicoid* null mother produces headless embryos; anterior *bicoid* mRNA injection rescues patterning.
(a) What does the rescue prove about Bicoid's role? (b) What does the gradient's formation tell you about maternal vs zygotic contribution?

**Case 10 — The Shh dose question.** Ectopic Shh in the dorsal neural tube induces floor-plate markers near the source and motor neurons further away.
(a) What model explains the two fates? (b) What experiment separates concentration from duration effects?

**Case 11 — Lost coordinates.** A scRNA-seq of developing gut finds an "absorptive precursor" cluster; a reviewer asks where these cells *are*.
(a) Why can't scRNA-seq answer this? (b) Name two methods that would, and what each adds.

**Case 12 — Spatial rumor.** A spatial-transcriptomics map suggests ligand L in region A neighbors receptor R in region B.
(a) What inference does this license? (b) What validation would upgrade it from hypothesis to finding?

---

## Part II — Experimental/data-interpretation questions (10)

*(Datasets referenced are in `DATA/`; all simulated.)*

**D1 — Gel.** A digest of candidate clone X shows bands at 3.2 kb only; clone Y at 4.05 + 0.85 kb. Which is correct, and what is X? (Dataset: `cloning-data/`)

**D2 — Fragment sum.** Clone Z's digest gives 2.3 + 1.7 + 0.9 kb; the map says the plasmid is 3.2 kb. Diagnose with reasoning.

**D3 — Colony PCR table.** Using `colony_pcr_results.csv`, tabulate how many of the 24 colonies are correct / empty / wrong-orientation / ambiguous, and justify one discrepancy vs plate color.

**D4 — Transformation counts.** From `transformation_plates.csv`, rank conditions L1–L4 by *correct-clone* rate (not colony count) and explain why the rankings differ.

**D5 — qPCR.** From `qPCR_timecourse.csv`, compute *myod1* fold change at 18 hpf vs 10 hpf (geometric-mean reference) and state the statistical treatment you would report.

**D6 — Reference failure.** Your qPCR shows apparent 3-fold *shha* induction using *ef1a* alone, but the stability table flags *ef1a* as stage-variable. Recompute with the stable reference and reinterpret.

**D7 — Volcano.** From `rnaseq_counts.csv`, produce (or describe) the volcano plot; how many genes pass FDR<0.05 AND |log2FC|>1, and what module do the top hits form?

**D8 — Clusters.** From `single_cell_counts.csv`, cluster at k=3 and annotate each cluster with its marker gene. What does the k=4 subcluster suggest?

**D9 — Spatial marker.** From `spatial_matrix.csv` + `spot_coordinates.csv`, identify the top marker of each region and plot one marker's x,y distribution. Which region would you call "notochord-like" and why?

**D10 — Gradient test.** Correlate the edge-gradient gene's expression with distance-to-edge (r ≈ ?). State the criterion that distinguishes this pattern from a domain, and the ISH experiment that would validate it.

---

**Grading guide:** case questions are scored for mechanism accuracy (40%), layering of evidence/risk/ethics/policy where relevant (30%), and proposed experiments' validity (30%). Data questions: correct interpretation (50%), correct quantitative handling (30%), stated limitations (20%).

---

[Course home](../index.md)
