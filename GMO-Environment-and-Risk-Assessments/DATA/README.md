# DATA - simulated risk-assessment teaching datasets

**All datasets in this folder are SIMULATED for education.** They are biologically
plausible and seeded/deterministic (`DATA/generate_datasets.py`, seed 42), so instructors
and students regenerate identical files. They must NOT be cited as experimental results.

| Folder | Dataset | Used in | Exercise |
|---|---|---|---|
| `gene-flow/` | pollen_flow_distance.csv | Lab 03 | 1. Gene-flow frequency vs distance |
| `non-target/` | nontarget_survival.csv | Lab 04 | 2. Non-target survival (Bt vs control) |
| `resistance/` | bt_resistance_frequency.csv | Lab 05 | 3. Bt resistance allele frequency |
| `resistance/` | herbicide_resistant_weeds.csv | Lab 05/06 | 4. Herbicide-resistant weed emergence |
| `soil/` | soil_otu_counts.csv | Lab 06 | 5. Soil microbial community comparison |
| `composition/` | compositional_analysis.csv | Lab 07 | 6. Compositional (GM vs control) comparison |
| `exposure/` | environmental_concentrations.csv | Lab 06 | 7. Exposure concentration over season |
| `dose-response/` | dose_response_larvae.csv | Lab 08 | 8. Dose-response curve + IC50 |
| `risk-matrix/` | risk_matrix_scores.csv | Lab 09 | 9. Risk-ranking matrix |
| `uncertainty/` | sensitivity_runs.csv | Lab 10 | 10. Sensitivity / uncertainty analysis |

## Analyze them

```bash
python DATA/analysis_demo.py     # runs all 10 exercises end to end
```

Worked, commented analyses for every exercise are in `analysis_demo.py`; lab handouts in
`../LAB/` pair each dataset with questions, expected outputs, interpretation guidance, and
an instructor key in `../WORKBOOK/`.
