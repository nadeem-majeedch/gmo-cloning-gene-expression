# GMO Environment and Risk Assessments

**A complete university-level course on the environmental risk assessment of genetically modified organisms — evidence-based, objective, and framework-driven.**

## Instructor

**Dr. Saira Azam**
Assistant Professor
Centre of Excellence in Molecular Biology
University of the Punjab, Lahore.

---

**For BS/MS students in Molecular Biology, Biotechnology, Environmental Sciences, Biosafety, Agriculture, Ecology and related disciplines.**

## Course purpose

How do scientists decide — objectively — whether a GMO is environmentally safe? This course teaches the full discipline: from GMO development and intended traits through hazard identification, exposure assessment, risk characterization, ecological and food/feed considerations, risk management, monitoring, and regulatory decisions. The emphasis throughout is **evidence-based risk assessment rather than advocacy for or against GMOs**. Students learn to keep hazard, exposure, risk, uncertainty, management, and communication as distinct analytical categories — and to evaluate every GMO as its own case:

**Trait + Organism + Environment + Exposure + Evidence + Uncertainty**

## Repository structure

```text
GMO-Environment-and-Risk-Assessments/
│
├── README.md            ← you are here
├── REFERENCES.md        ← authoritative sources (verified, non-fabricated)
├── BUILD_REPORT.md      ← build/QA record
├── LICENSE
│
├── MARKDOWN/            ← 25 course modules (beginner → research-oriented)
├── LAB/                 ← 12 practicals (simulation/computational/case-study)
├── WORKBOOK/            ← practical compendium
├── CHEAT-SHEET/         ← 4-page revision sheet
├── FAQ/                 ← 67 FAQs in 12 categories
├── ASSESSMENT/          ← 60 MCQs, 30 short, 20 long, 40 viva, 15 case,
│                          15 data-interpretation + instructor answer key
├── DATA/                ← 10 simulated datasets + analysis demo (seeded)
├── DIAGRAMS/            ← 20 original schematic teaching diagrams
├── PPTX/                ← 89-slide lecture deck with speaker notes
└── PDF/                 ← 5 printable PDFs (tutorial, workbook, cheat sheet,
                            FAQs, assessment)
```

## The teaching arc

```text
GMO Development → Intended Trait → Hazard Identification → Exposure Assessment
→ Risk Characterization → Environmental Assessment → Food/Feed Considerations
→ Ecological Assessment → Risk Management → Monitoring → Regulatory Decision
```

## Modules (MARKDOWN/)

| # | Module | # | Module |
|---|---|---|---|
| 01 | Introduction to GMO Risk Assessment | 14 | Food and Feed Safety |
| 02 | Hazard, Risk and Exposure | 15 | Allergenicity and Toxicity Assessment |
| 03 | The ERA Framework | 16 | Unintended Effects and Uncertainty |
| 04 | Molecular Characterization | 17 | Risk Characterization |
| 05 | Phenotypic and Compositional Assessment | 18 | Risk Management |
| 06 | Gene Flow and Introgression | 19 | Environmental Monitoring |
| 07 | Persistence, Weediness and Invasiveness | 20 | Post-Market Monitoring |
| 08 | Non-Target Organisms | 21 | Risk Communication |
| 09 | Soil Ecosystems and Microbial Interactions | 22 | Regulatory Frameworks |
| 10 | Biodiversity and Food Webs | 23 | Case Studies (15) |
| 11 | Resistance Evolution | 24 | Data Analysis |
| 12 | Herbicide Resistance and Weed Management | 25 | Advanced Topics |
| 13 | Environmental Fate and Exposure | | |

## How to study this course

1. **Read modules in order** — each has Definition → Why it matters → Beginner/Scientific/Advanced explanations → Real-world example → Workflow → Example data → Misconceptions → Exam points → Quick-checks.
2. **Do the practicals alongside** (LAB/): Labs 01–02 after Module 3; Labs 03–10 with Modules 6–17; Lab 11 after Module 22; Lab 12 (capstone) last.
3. **Analyze the datasets** (`DATA/`): run `python DATA/analysis_demo.py` to reproduce every documented answer; datasets are clearly labelled simulations, seeded and regenerable.
4. **Test yourself**: module quick-checks → FAQ categories → assessment package (with self-checking against the instructor key).
5. **Finish with the capstone** (Lab 12): a complete conceptual ERA for a real GMO of your choice.

## For instructors

- Every lab includes instructor answer keys, viva banks, and an advanced challenge.
- The assessment package carries Bloom's-graded MCQs with explanations and rubrics for open questions.
- The PPTX deck (89 slides, 19 sections) includes speaker notes for complex concepts; rebuild with `python PPTX/build_pptx.py`.
- PDFs regenerate with `python PDF/build_pdfs.py` (requires reportlab); diagrams with `python DIAGRAMS/generate_diagrams.py`; datasets with `python DATA/generate_datasets.py`.
- Regenerate the whole package from source in under five minutes; everything is deterministic (seeded).

## Scientific integrity statement

- All quantitative datasets are **simulated for teaching** and labelled as such; no fabricated real-world statistics are presented as data.
- Real case studies (Bt cotton, monarch, StarLink, golden rice, UK FSE, etc.) are built from published evidence; students are directed to primary sources in [REFERENCES.md](REFERENCES.md) — no citations are fabricated.
- Controversial topics are treated as contested where the evidence base is contested; regulatory divergence is described, not adjudicated.
- The course takes no advocacy position; its examinable skill is disciplined, uncertainty-honest reasoning.

## License

MIT — see [LICENSE](LICENSE).
