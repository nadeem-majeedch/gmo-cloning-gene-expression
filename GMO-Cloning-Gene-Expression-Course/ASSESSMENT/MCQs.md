# Assessment — 50 Multiple-Choice Questions

**Course:** GMOs, Cloning Techniques, and Developmental & Spatial Gene Expression
**Levels:** Recall → Understanding → Application → Analysis → Evaluation
**Answers & explanations:** [Answer-Key.md](Answer-Key.md)

---

### Section A — Recall (Q1–10)

**1.** Which enzyme seals phosphodiester bonds during cloning?
A) Restriction endonuclease · B) DNA ligase · C) DNA polymerase · D) Reverse transcriptase

**2.** The sequence EcoRI recognizes is:
A) G^AATTC · B) GGATCC · C) AAGCTT · D) CTGCAG

**3.** A plasmid origin of replication controls:
A) Insert size limit · B) Copy number · C) Promoter strength · D) Antibiotic resistance

**4.** GFP was originally isolated from:
A) *Discosoma* sp. · B) Firefly · C) *Aequorea victoria* · D) *Renilla reniformis*

**5.** The PAM for SpCas9 is:
A) 5′-NGG-3′ · B) 5′-TTTV-3′ · C) 5′-NNGRRT-3′ · D) 5′-NG-3′

**6.** The "T" in a TA-cloning T-vector pairs with:
A) A 5′-A overhang · B) A 3′-A overhang · C) A blunt end · D) An RNA cap

**7.** Which model organism has an invariant cell lineage?
A) Mouse · B) Zebrafish · C) *C. elegans* · D) *Arabidopsis*

**8.** Blue-white screening uses disruption of:
A) ampR · B) lacZα · C) ori · D) GFP

**9.** Dolly the sheep was produced by:
A) Pronuclear microinjection · B) Somatic-cell nuclear transfer · C) ES-cell complementation · D) Viral transduction

**10.** Colinearity refers to the alignment between Hox gene order and:
A) Chromosome size · B) Expression along the body axis · C) GC content · D) Replication timing

### Section B — Understanding (Q11–20)

**11.** Dephosphorylating the vector before ligation primarily prevents:
A) Insert concatemerization · B) Vector self-ligation · C) Star activity · D) Methylation

**12.** Type IIS enzymes (e.g., BsaI) are useful in Golden Gate because they:
A) Cut only methylated DNA · B) Cut outside their recognition site · C) Leave blunt ends · D) Require RNA cofactors

**13.** A reporter gene under a tissue-specific promoter reports:
A) Protein folding · B) Where the promoter is active · C) Genome position effects · D) mRNA half-life

**14.** In RT-qPCR, the ΔΔCt method assumes:
A) 100% primer efficiency · B) Single-cell input · C) RNA is double-stranded · D) Reference genes vary by condition

**15.** NHEJ repair of a Cas9 cut usually produces:
A) Precise donor integration · B) Small indels · C) Base conversion A→G · D) methylation changes

**16.** An enhancer, compared with a promoter, is characteristically:
A) Position- and orientation-flexible · B) Always adjacent to the TSS · C) Coding · D) Prokaryotic-only

**17.** Gibson Assembly requires fragments with:
A) Blunt ends · B) Terminal sequence overlaps · C) 3′-A overhangs · D) Identical restriction sites

**18.** Single-cell RNA-seq primarily loses:
A) Gene identities · B) Spatial position of cells · C) UMI counts · D) Cluster structure

**19.** In spatial transcriptomics (array-based), one capture spot typically integrates:
A) One chromosome · B) Several cells · C) One nucleus · D) A whole organ

**20.** A BAC differs from a standard plasmid chiefly in:
A) Antibiotic marker · B) Insert capacity · C) Circular topology · D) Use of DNA ligase

### Section C — Application (Q21–32)

**21.** You must clone a 2 kb insert with an internal BamHI site into a vector; the best direct strategy is:
A) BamHI single digest · B) Two other compatible unique sites flanking the MCS · C) Ligase-only blunt ligation with no preparation · D) Skip validation

**22.** A colony is PCR-positive with vector+insert primers but the diagnostic digest disagrees with the map. You should trust:
A) The PCR — it is more sensitive · B) The digest — structural evidence · C) Coin-flip · D) Discard without analysis

**23.** To quantify promoter activity over time in cell culture with the widest dynamic range, choose:
A) lacZ/X-gal · B) Firefly luciferase (normalized) · C) Colony PCR · D) Sanger sequencing

**24.** For *absolute* transcript counts per single cell in tissue, choose:
A) Bulk RNA-seq · B) smFISH · C) Western blot · D) Colony PCR

**25.** A zebrafish F0 crispant shows mixed phenotypes across tissues; most likely explanation:
A) Sequencing error · B) Mosaicism · C) HDR repair · D) Sense-probe signal

**26.** To test whether a candidate enhancer is *necessary* for endogenous expression, the best first experiment is:
A) Enhancer-reporter assay · B) CRISPRi/knockout of the endogenous enhancer + ISH readout · C) Western blot of the enhancer · D) Delete the promoter

**27.** An RT-qPCR shows *myod1* up 8-fold at 18 hpf; the strongest independent spatial validation would be:
A) More qPCR replicates · B) ISH showing somite/paraxial signal at 18 hpf · C) Genomic PCR · D) Colony PCR

**28.** In a ligation with insert:vector 0:1 (vector only, not dephosphorylated), expected colony outcome:
A) Zero colonies · B) Background empty-vector colonies · C) All correct clones · D) Lambda phage plaques

**29.** Your Gibson assembly uses 12 bp overlaps between fragments; likely result:
A) Improved fidelity · B) Inefficient/unreliable assembly · C) Faster reaction · D) Star activity

**30.** To generate a C-terminal GFP fusion, the insert design must:
A) Include a stop codon before GFP · B) Lack a stop codon and be in-frame with GFP · C) Be blunt-ended · D) Use T7 terminator

**31.** A KO experiment yielded a viable F0 whose target PCR shows a 3-bp in-frame deletion; interpretation:
A) Knockout succeeded · B) Protein function may be preserved — screen for frameshift alleles or use protein-level validation · C) HDR occurred · D) The guide bound RNA

**32.** Which design change best reduces off-target risk?
A) Longer ligation · B) Guide re-design with off-target scoring + RNP delivery · C) More antibiotic · D) Higher-copy vector

### Section D — Analysis (Q33–42)

**33.** A digest of a "correct" construct yields fragments summing to 5.8 kb, but the map says 4.05 kb. Best conclusion:
A) Pippetting error only · B) Rearranged/duplicated plasmid · C) Perfect match · D) Sense-probe contamination

**34.** A DE analysis at FDR<0.05 returns 1,800 genes with |log2FC| < 0.1. Most likely explanation:
A) Biology is subtle but real · B) Under-powered/near-zero variance artifact — reconsider normalization/design · C) Genes are misnamed · D) FDR too strict

**35.** In a scRNA-seq UMAP, one cluster co-expresses *pax6a* and *myod1* at low levels. Most defensible interpretation:
A) Sequencing artifact — ignore · B) Possible transition state or doublet — verify with additional markers/QC · C) New species · D) Sense probe

**36.** A spatial matrix shows gene X high at the tissue edge, declining inward (r = −0.6 vs distance). This is best described as:
A) A domain · B) A gradient · C) A mosaic · D) A mutation

**37.** An enhancer-reporter works in orientation A but not B, reproducibly. Defensible statement:
A) It is a classic enhancer · B) It behaves promoter-like/orientation-dependent — check for cryptic promoter activity · C) Enhancers never show orientation effects · D) The Renilla failed

**38.** In a time course, a gene starts high and decays over early stages. Best annotation:
A) Zygotic activation · B) Maternal contribution · C) Housekeeping · D) Reporter artifact

**39.** A heat-killed "positive control" for transformation produces 300 colonies; your ligation plate has 2. Strongest conclusion:
A) Competent cells are fine — ligation/assembly failed · B) Cells are dead · C) Antibiotic wrong · D) Transformation worked great

**40.** Colony PCR (Set A, flanking primers) cannot determine orientation because:
A) Primers are identical on both strands · B) Product size is the same for both orientations · C) DNA is circular · D) PCR can't amplify plasmids

**41.** In an RNA-seq PCA, samples separate by batch, not condition. Correct action:
A) Report condition results anyway · B) Re-balance design or model the batch; do not interpret condition from this run · C) Delete batch samples · D) Increase reads 10×

**42.** An ISH sense-probe panel shows moderate uniform signal. Correct interpretation:
A) Gene is expressed everywhere · B) Background/trapping — antisense comparisons must subtract this · C) Probe degraded · D) Stage mismatch only

### Section E — Evaluation (Q43–50)

**43.** Which claim does a promoter-GFP zebrafish line NOT support?
A) The promoter is active in GFP-positive cells · B) GFP pattern matches promoter activity · C) The endogenous gene is expressed identically · D) The construct works in vivo

**44.** Golden Rice's primary scientific claim rests on:
A) Higher yield · B) Provitamin A accumulation in endosperm · C) Herbicide tolerance · D) Nitrogen fixation

**45.** "GMOs are 100% safe" as a universal statement is scientifically problematic because:
A) Safety is assessed per product/trait, not by category · B) GMOs don't exist · C) Safety cannot be studied · D) All assessments failed

**46.** Which pair correctly matches method and question?
A) ISH — protein localization · B) IF — mRNA localization · C) smFISH — absolute mRNA counts · D) qPCR — spatial maps

**47.** A reviewer asks whether your CRISPRi enhancer result could be off-target seed effects. Best response:
A) Ignore · B) Include independent sgRNAs and a non-targeting control ± rescue/motif-mutant comparison · C) Lower the FDR · D) Use more antibiotic

**48.** Bt-corn resistance evolution in target pests is best addressed by:
A) Abandoning the trait · B) Refuge + pyramided-toxin management strategies · C) Higher insecticide spraying · D) Ignoring monitoring

**49.** Which statement about germline editing of humans is most defensible in a scientific-ethics exam?
A) It is already routine · B) Technical possibility does not equal ethical readiness; oversight frameworks (e.g., WHO 2021) call for strict limits · C) No risks exist · D) Consent is unnecessary for future generations

**50.** The best final validation before declaring a new construct "confirmed":
A) Colony count · B) Sanger sequencing across junctions and full insert · C) Blue colony color · D) Correct antibiotic growth

---

**Total: 50 questions.** Answer key with explanations: [Answer-Key.md](Answer-Key.md) · Also see [Short Questions](Short-Questions.md), [Long Questions](Long-Questions.md), [Viva Questions](Viva-Questions.md), [Case Studies](Case-Studies.md)
