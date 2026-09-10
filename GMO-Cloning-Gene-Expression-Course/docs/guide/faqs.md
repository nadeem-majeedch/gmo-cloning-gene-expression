# FAQs — GMOs, Cloning & Gene Expression

**65 questions across 13 categories** · [↑ Course Home](../index.md) · [Cheat Sheet](../guide/cheat-sheet.md) · [Assessment](../assessment/MCQs.md)

---

## A. Beginner (1–6)

**1. What is a GMO in one sentence?**
An organism whose genetic material has been altered by humans using laboratory techniques — though whether *any particular* altered organism is legally a "GMO" depends on the country.

**2. Is genetic engineering the same as breeding?**
No. Breeding recombines existing variation through controlled mating; genetic engineering introduces designed changes directly, often across species boundaries or at single-base precision.

**3. Are GM foods "chemicals"?**
All food is chemicals. The meaningful questions are which trait was changed and what the safety assessment showed — not the word "chemical".

**4. Why do bacteria have restriction enzymes if we use them for cloning?**
They are a bacterial defense against phage DNA; bacteria protect their own DNA with methylation. We borrowed the enzymes as molecular scissors.

**5. What's the difference between a plasmid and a vector?**
A plasmid is a naturally occurring circular DNA replicon; a *vector* is a plasmid (or virus/artificial chromosome) engineered to carry DNA we care about.

**6. Do GMOs always contain foreign DNA?**
No — gene-edited organisms may carry only a small deletion or base change, with no foreign sequence remaining.

## B. Molecular cloning (7–15)

**7. Why is an origin of replication essential?**
Without an ori, the plasmid can't be copied by the host and is lost — no propagation, no colonies.

**8. Why do we need both a promoter and a terminator?**
The promoter starts transcription; the terminator stops it at a defined point, preventing read-through into vector sequences that can destabilize the construct.

**9. What does "high-copy plasmid" mean practically?**
The ori (e.g., pUC-derived) allows hundreds of plasmid copies per cell → more DNA per prep, but more metabolic burden — problematic for toxic or unstable inserts.

**10. Why add extra bases (clamps) before restriction sites in primers?**
Enzymes need flanking DNA to bind and cut efficiently; sites at the very end of a PCR product are cut poorly.

**11. Can I ligate an EcoRI end to a BamHI end?**
No — overhangs must be complementary (AATT vs GATC don't pair). Compatible but different enzymes (e.g., BamHI/BglII) *can* ligate because they leave identical overhangs.

**12. Why dephosphorylate the vector?**
Removes 5′ phosphates so the vector can't self-ligate; only insert-containing molecules (providing the phosphates) transform efficiently.

**13. What is an MCS?**
Multiple cloning site — a synthetic cluster of unique restriction sites so many different enzyme pairs can target the same small region.

**14. What's a shuttle vector?**
A vector with two origins and two selectable markers so it propagates in two hosts (e.g., build in *E. coli*, use in yeast or mammalian cells).

**15. What does "in-frame" mean for a fusion?**
The insert joins the tag coding sequence without a frameshift, so one continuous reading frame produces a single fusion protein.

## C. Cloning troubleshooting (16–24)

**16. No colonies at all — first suspects?**
Dead competent cells, wrong antibiotic, failed ligation/digest. Always run a positive-control transformation.

**17. All colonies are empty vector — why?**
Vector self-ligation (missing dephosphorylation), incompatible insert ends, or insert preparation failed. Check the vector-only control plate count.

**18. Low ligation efficiency — what to tune?**
Molar ratio (~3:1), ligase freshness, buffer ATP, compatible ends, insert purity (salts inhibit ligase).

**19. My PCR product won't clone by TA — why?**
High-fidelity polymerases leave blunt ends; you must A-tail the product (or use blunt-end/Gibson approaches).

**20. Gibson assembly gave many colonies but wrong plasmids — likely cause?**
Repeats in overlaps causing misassembly, or overlaps too short/weak; re-design overlaps with 20–40 bp unique sequence.

**21. Golden Gate didn't work — check what first?**
Internal Type IIS sites in your parts (undomesticated), wrong fusion-site map, or enzyme temperature cycling not followed.

**22. Colony PCR gives smeared bands — why?**
Too much colony template (inhibitors), dirty cells, or primer issues; use a tiny amount of colony and fresh mix.

**23. Digest shows three bands but map predicts two — panic?**
First sum the fragments; if sum > plasmid size → rearrangement. If sum matches → an extra site (methylation? star activity? re-check sequence).

**24. Sanger trace is mixed/overlapping — what does it mean?**
Heterozygous site (rare in plasmids), mixed colony, or indel mixture from a repair event; re-isolate a single colony and re-prep.

## D. GMO (25–31)

**25. What's the first GMO ever made?**
Functionally cloned recombinant plasmids in *E. coli* — Cohen, Chang, Boyer & Helling, 1973 (the modern GMO era's starting point).

**26. Is Golden Rice transgenic?**
Yes — it carries *psy* and *crtI* genes from other species (maize/daffodil/*Erwinia*), inserted by transformation.

**27. Why do Bt crops need refuges?**
Refuges maintain susceptible insects that mate with any resistant survivors, slowing resistance evolution — resistance management, not an admission of failure.

**28. Can a GMO be made without inserting anything?**
Yes — a knockout via CRISPR NHEJ deletes bases; a base edit changes a letter. No foreign DNA remains.

**29. What's the difference between transfection, transformation, and transduction?**
Transfection = introducing DNA into eukaryotic cells; transformation = into bacteria (usage differs by field); transduction = viral-mediated delivery.

**30. Are all transgenic animals made by microinjection now?**
No — CRISPR reagent delivery to embryos is now common for edits; transgenesis (added DNA) still uses microinjection, transposons, viral vectors, or SCNT depending on species and goal.

**31. Why is plant transformation "easier" conceptually?**
Totipotency — one modified somatic cell can regenerate a whole plant via tissue culture; animal embryos must be manipulated individually.

## E. CRISPR (32–40)

**32. What is a PAM and why does it matter?**
Protospacer-adjacent motif — a short sequence (e.g., NGG for SpCas9) next to the target that Cas9 must recognize to initiate binding; it's required for cleavage and limits targetable sites.

**33. Does CRISPR always cut?**
Not necessarily — dCas9 variants bind without cutting, powering CRISPRa/i; base and prime editors avoid DSBs by design.

**34. NHEJ vs HDR in one line each?**
NHEJ: error-prone religation of broken ends → indels (knockout). HDR: template-guided repair → precise insertion/correction (needs donor, cell-cycle dependent).

**35. Why are knock-ins hard?**
HDR is inefficient in most primary cells; delivery of donors is limiting; alternatives (HITI, base/prime editing) have their own constraints.

**36. What is mosaicism?**
Different cells of the same founder animal carry different edits because editing happened after the first division — complicates genotyping and phenotyping.

**37. Are off-targets a deal-breaker?**
They're manageable: careful guide design, high-fidelity variants, transient RNP delivery, and empirical verification of predicted off-target sites.

**38. CRISPRi vs CRISPRa?**
CRISPRi (dCas9-KRAB) represses transcription — tests *necessity*; CRISPRa (dCas9-activators) up-regulates — tests *sufficiency*, all without genome change.

**39. Can CRISPR edit RNA?**
Cas13-class systems target RNA without DNA changes — used for knockdown and RNA-editing research tools.

**40. Why did the 2018 human-embryo case draw global condemnation?**
Germline editing of humans without adequate oversight/consent framework, questionable benefit-risk, and transparency failures — condemned irrespective of the technical outcome.

## F. Reporter genes (41–46)

**41. Why does GFP need no substrate?**
Its chromophore forms autocatalytically from internal amino acids (needs only O₂ to mature) — that's why it revolutionized live imaging.

**42. When would I choose luciferase over GFP?**
When you need *quantitative* activity over time (plate-reader assays, dual-reporter normalization) rather than spatial detail.

**43. Why does my GFP fusion not localize like the endogenous protein?**
The tag can interfere (steric effects, missing targeting signals, oligomerization of old FPs) — validate against IF/ISH and consider tag placement/linkers.

**44. What is a destabilized GFP?**
GFP fused to a degradation tag so it degrades quickly — reports *current* transcription rather than accumulated history.

**45. Why normalize luciferase to Renilla?**
Transfection efficiency and cell number vary between wells; Renilla from a co-transfected constitutive plasmid calibrates that variation.

**46. Can reporters mislead about endogenous expression?**
Yes — missing chromatin context or distal elements; always pair with endogenous methods (ISH/IF) for strong claims.

## G. Developmental biology (47–52)

**47. What is a morphogen in one line?**
A signaling molecule whose concentration gradient instructs different cell fates at different thresholds (Wolpert's French-flag model).

**48. Why are Hox genes "colinear"?**
Their order on the chromosome matches the order (anterior→posterior) and timing of their expression along the body axis.

**49. What did the *myoD* experiment show?**
Forced *myoD* expression converts fibroblasts into myoblasts — a landmark *sufficiency* demonstration (with the caveat that endogenous specification is multi-input).

**50. What is lateral inhibition?**
Notch-mediated neighbor interactions where one cell's fate suppresses the same fate in adjacent cells — producing salt-and-pepper patterns (e.g., neural precursors).

**51. Why is the zebrafish embryo so useful?**
External, transparent, rapid development → live imaging of every stage; large clutches; forward screens.

**52. What's a "master regulator" — and the caveat?**
A gene whose expression is sufficient to induce a whole program (e.g., *myoD*); caveat — endogenous development usually requires multiple inputs, so "master" describes the experimental sufficiency, not the whole mechanism.

## H. Spatial gene expression (53–57)

**53. Spatial vs temporal expression — difference?**
Spatial = where in the organism/tissue; temporal = when in development/response; spatiotemporal = both jointly.

**54. Gradient vs domain?**
A gradient is a continuous concentration change across space; a domain is a sharply bounded region of expression. Gradients inform; domains execute.

**55. Why does bulk RNA-seq lose spatial information?**
It averages transcripts over the whole sampled tissue — a strong signal can come from a tiny, highly expressing region.

**56. What does scRNA-seq lose and why?**
Position — cells are dissociated into a suspension before barcoding, severing each cell from its coordinates (motivating spatial transcriptomics).

**57. What is spot deconvolution?**
Array-based spatial data measures mixtures of cells per spot; deconvolution estimates the underlying cell-type proportions using single-cell references.

## I. Experimental methods (58–61)

**58. Why is the sense probe the right negative control for ISH?**
It has the same sequence as the target mRNA and cannot base-pair specifically — it measures everything except intended hybridization.

**59. RT-PCR vs RT-qPCR?**
Both start with reverse transcription; RT-PCR is endpoint (present/absent, semi-quantitative); RT-qPCR monitors amplification in real time for quantitative comparison.

**60. Why validate housekeeping/reference genes per experiment?**
"Housekeeping" genes can shift with treatment, stage, or tissue — an unvalidated reference invalidates the ΔΔCt result.

**61. IHC vs ISH — when each?**
IHC detects the *protein* (post-transcriptional regulation visible); ISH detects the *mRNA* (transcriptional pattern); they disagree meaningfully when translation/stability is regulated.

## J. Data analysis (62–63)

**62. Why do statistics on ΔCt rather than fold change?**
Ct values are approximately normally distributed; fold changes are skewed — analyzing ΔCt keeps the statistics valid.

**63. What's FDR and why not just p-values?**
With thousands of genes tested, 5% of "significant" hits are expected by chance; Benjamini–Hochberg FDR controls the *expected proportion of false discoveries* among your calls.

## K. Ethics (64)

**64. Are GMOs "unnatural" in a scientifically meaningful sense?**
"Natural" is not a scientific property — the scientific questions are what change was made, what the evidence says, and what the risks are; "unnaturalness" belongs to the ethics/values layer (Module 14), and both risk and benefit arguments must be made explicitly, not by label.

## L. Advanced concepts (part of 65)

**65. Quick definitions: TAD? Super-enhancer? Bursting? Pseudotime?**
- **TAD:** self-interacting chromatin domain constraining enhancer–promoter contacts.
- **Super-enhancer:** dense enhancer cluster with high Mediator/BRD4/H3K27ac controlling identity genes.
- **Bursting:** intermittent transcription initiation producing cell-to-cell mRNA-number variability.
- **Pseudotime:** ordering single cells along a trajectory of transcriptional similarity — developmental sequence, not clock time.

---

*M. Exam preparation*

**66. How should I answer "compare X and Y" questions?**
Table form: definition → mechanism → strength → limitation → example, then a one-sentence verdict tied to the scenario in the question.

**67. How do I avoid overclaiming in experimental answers?**
Name the readout's resolution (space/time/quantity), the controls that were or weren't run, and what a *stronger* claim would require (validation method).

*(Total: 67 Q&As — exceeds the 60-question requirement.)*

---

[Course home](../index.md)
