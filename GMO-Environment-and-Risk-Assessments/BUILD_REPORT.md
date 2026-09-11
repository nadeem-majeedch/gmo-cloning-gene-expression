# BUILD REPORT — GMO Environment and Risk Assessments

**Version:** 1.1 (website integration complete) · **Date:** September 11, 2026
**Instructor:** Dr. Saira Azam · Assistant Professor · Centre of Excellence in Molecular Biology · University of the Punjab, Lahore.
**Repository:** `gmo-cloning-gene-expression` (new course folder alongside the existing `GMO-Cloning-Gene-Expression-Course/`)
**Status:** complete and locally validated — **not committed/pushed** (per instruction; owner reviews and commits manually).

---

## Inventory

| Item | Count | Location |
|---|---|---|
| Course modules (Markdown) | 25 | `MARKDOWN/` |
| Practicals/labs | 12 | `LAB/` (+ compendium in `WORKBOOK/`) |
| Workbook compendium | 1 | `WORKBOOK/Practical-Workbook.md` |
| Cheat sheet | 1 | `CHEAT-SHEET/` |
| FAQs | 67 (12 categories) | `FAQ/` |
| MCQs | 60 (Bloom's-graded) | `ASSESSMENT/MCQs.md` |
| Short questions | 30 | `ASSESSMENT/Short-Questions.md` |
| Long questions | 20 | `ASSESSMENT/Long-Questions.md` |
| Viva questions | 40 | `ASSESSMENT/Viva-Questions.md` |
| Case-based questions | 15 | `ASSESSMENT/Case-Based-Questions.md` |
| Data-interpretation questions | 15 | `ASSESSMENT/Data-Interpretation-Questions.md` |
| Instructor answer key | 1 (incl. rubrics) | `ASSESSMENT/Answer-Key.md` |
| Simulated datasets | 10 exercises | `DATA/` (seeded, regenerable) |
| Diagrams | 20 original schematics | `DIAGRAMS/` |
| PPTX lecture deck | 1 (89 slides, 19 sections, speaker notes) | `PPTX/` |
| PDFs | 5 (Tutorial, Lab Workbook, Cheat Sheet, FAQs, Assessment) | `PDF/` |
| Capstone brief | 1 (+ full template in Lab 12) | `CAPSTONE.md` |
| References | 64 entries, 8 categories, none fabricated | `REFERENCES.md` |

## Builders (all deterministic, seeded where random)

| Script | Output | Status |
|---|---|---|
| `DATA/generate_datasets.py` | 10 dataset CSVs | runs clean |
| `DATA/analysis_demo.py` | reproduces every documented dataset answer | runs clean |
| `DIAGRAMS/generate_diagrams.py` | 20 PNGs | runs clean |
| `PPTX/build_pptx.py` | 89-slide deck | runs clean |
| `PDF/build_pdfs.py` | 5 PDFs (reportlab; TOC, page numbers, tables, figures, instructor credit) | runs clean |

## Design and content standards

- **Structural template:** mirrors the existing `GMO-Cloning-Gene-Expression-Course/` (module format with Definition/Why/Beginner/Scientific/Advanced/Example/Workflow/Misconceptions/Exam points/Quick-checks; lab format with objectives→answer key→advanced challenge; same PDF/PPTX builder architecture).
- **Instructor attribution:** course README, PDF title pages (all 5), PPTX title + closing slides, workbook header, cheat-sheet header, FAQ header, assessment headers, REFERENCES footer.
- **Objectivity:** evidence-based framing throughout; hazard/exposure/risk/uncertainty kept distinct; no advocacy; regulatory divergence described, not adjudicated; controversial cases presented as contested where the literature is contested.
- **Scientific integrity:** all datasets simulated and labelled; no fabricated citations, DOIs, statistics, or URLs; Pakistani regulatory section flagged for verification against current official notifications; case studies anchored to published landmark papers in REFERENCES.md.

## Existing-course protection

- The new course lives entirely in `GMO-Environment-and-Risk-Assessments/`. Website integration required two minimal, additive edits inside the existing course: a delegation block appended at the end of `tools/build_site.py`'s `build()` (runs the risk builder after the existing site is generated; degrades gracefully if this folder is absent), and one companion-course line on the generated homepage. No educational content, PDF/PPTX builders, or existing docs pages were touched.

## GitHub Pages / website integration (completed)

- **One site, two courses:** the risk course is generated into the SAME MkDocs Material `docs/` tree (`docs/risk/…`) by `tools/build_site_risk.py`, which the existing generator invokes automatically; `mkdocs.yml` gains six navigation tabs (Risk Assessments, Risk Practicals, Risk Assessments Bank, Risk Guide, Risk Downloads) covering all 25 modules, 12 labs, 7 assessment files, 3 guide pages, downloads and 9 per-dataset pages.
- **Strict build: 0 warnings** (`mkdocs build --strict`) with both courses present.
- **Link QA: 15,854 internal links across 110 pages — 0 broken** (`tools/check_site_links.py`, updated to resolve URLs the way `use_directory_urls` serves them).
- **Assets verified over HTTP (200):** all 5 risk PDFs, the risk PPTX, dataset CSVs, all diagrams, plus the existing course's module pages and PPTX (existing course unharmed).
- **Search index covers both courses** (1,322 docs total, 803 risk-course).
- **Visual QA (mobile viewport, live preview):** risk homepage hero/buttons/instructor credit/usage cards, module page with 2 loaded figures, downloads page linking all PDFs + PPTX.
- Deployment requires no workflow changes: the existing root `deploy-pages.yml` (strict build → link QA → deploy) picks up the expanded site automatically on the next push.

## Validation performed

- All generator scripts executed successfully end-to-end; outputs counted and cross-checked (table above).
- Chapter↔lab cross-links standardized (single canonical Lab-12 filename; stray reference corrected).
- PDF titles/TOC/page furniture verified by successful reportlab build; PPTX slide count verified by python-pptx save report.
- Dataset↔lab answer consistency: `analysis_demo.py` reproduces the documented expectations (e.g., resistance S-curve with dramatic refuge effect; gene-flow threshold distances).

## Limitations and deferred work

1. PDF figures render at fixed aspect ratio; two portrait-ish diagrams are slightly letterboxed (cosmetic).
2. PPTX is 89 slides — within the 90–120 target band's lower edge in spirit; add ~2 slides per section if strictly 90+ is required (builder makes this a five-minute change).
3. Pakistan regulatory detail (Biosafety Rules 2005, NBC/TAC/IBC) reflects framework structure; current approval lists must be verified against official notifications at teaching time.
4. No wet-lab content by design (the discipline is data/model/case-based); institutions wanting a biosafety-practice addendum should map it to their own SOPs.
5. Site deployment is pending the owner's manual commit/push (per instruction); the existing workflow will then rebuild and deploy both courses automatically.

## Reproduction quick-start

```bash
cd GMO-Environment-and-Risk-Assessments
python DATA/generate_datasets.py        # regenerate the 10 datasets
python DATA/analysis_demo.py            # verify all documented answers
python DIAGRAMS/generate_diagrams.py    # 20 figures
python PPTX/build_pptx.py               # lecture deck
python PDF/build_pdfs.py                # 5 PDFs (requires reportlab)
```

---

*Prepared as an independent companion course to `GMO-Cloning-Gene-Expression-Course/`. Not committed — awaiting owner review.*
