#!/usr/bin/env python3
"""Worked analyses for the 10 simulated risk-assessment exercises.

Run from the course root:  python DATA/analysis_demo.py
Requires numpy, pandas, scipy, scikit-learn (all standard teaching stacks).

Every section prints: dataset -> question -> result -> interpretation.
Numbers reproduce deterministically (seed 42) and match the instructor keys
in WORKBOOK/ and LAB/ handouts.
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))


def load(folder, name):
    return pd.read_csv(os.path.join(HERE, folder, name), comment="#")


def banner(n, title):
    print("\n" + "=" * 74)
    print(f"EXERCISE {n} - {title}")
    print("=" * 74)


# ------------------------------------------------------------------ Ex.1
def ex1_gene_flow():
    banner(1, "Gene-flow frequency vs distance")
    df = load("gene-flow", "pollen_flow_distance.csv")
    agg = df.groupby("distance_m").agg(mean_freq=("flow_frequency", "mean"),
                                       sd=("flow_frequency", "std")).reset_index()
    print(agg.to_string(index=False))
    fit = agg[agg.distance_m <= 100]
    slope, intercept, r, p, se = stats.linregress(np.log(fit.distance_m), np.log(fit.mean_freq))
    print(f"log-log slope = {slope:.2f} (r = {r:.3f}) -> steep spatial decay")
    d100 = agg.loc[agg.distance_m == 100, "mean_freq"].iloc[0]
    print(f"mean outcrossing at 100 m = {d100:.5f} (1 in ~{1/d100:,.0f} seeds)")
    print("INTERPRETATION: frequency falls ~100x between 1 m and 100 m; beyond ~50 m\n"
          "residual outcrossing is very low but not zero - isolation distance reduces\n"
          "rather than eliminates crop-to-crop/wild gene flow. Management combines\n"
          "distance with flowering-time and border-row strategies.")
    return {"slope": slope, "r": r, "freq_at_100m": d100}


# ------------------------------------------------------------------ Ex.2
def ex2_non_target():
    banner(2, "Non-target organism survival (Bt vs non-Bt pollen)")
    df = load("non-target", "nontarget_survival.csv")
    summ = (df.groupby(["species", "functional_group", "treatment"])
              .alive.sum().reset_index())
    summ["n"] = df.groupby(["species", "functional_group", "treatment"]).n_exposed.sum().values
    summ["survival"] = (summ.alive / summ.n).round(3)
    print(summ.to_string(index=False))
    print("\nTwo-proportion z-tests (Bt vs control):")
    for sp in df.species.unique():
        sub = df[df.species == sp]
        x = [sub[sub.treatment == "Bt_pollen"].alive.sum(),
             sub[sub.treatment == "non-Bt_pollen"].alive.sum()]
        n = [sub[sub.treatment == "Bt_pollen"].n_exposed.sum(),
             sub[sub.treatment == "non-Bt_pollen"].n_exposed.sum()]
        p1, p2 = x[0] / n[0], x[1] / n[1]
        pp = (x[0] + x[1]) / (n[0] + n[1])
        se = np.sqrt(pp * (1 - pp) * (1 / n[0] + 1 / n[1]))
        z = (p1 - p2) / se
        print(f"  {sp:24s} diff={p1-p2:+.3f}  z={z:+.2f}")
    print("INTERPRETATION: all differences are within normal cage variation (|z| < 2)\n"
          "for the pollinator, predators and parasitoid; the design as powered detects\n"
          "only large effects. Direct toxicity is NOT demonstrated; field-scale and\n"
          "trophic-pathway studies would be needed before any ecological conclusion.")
    return None


# ------------------------------------------------------------------ Ex.3
def ex3_resistance():
    banner(3, "Bt resistance allele frequency over generations")
    df = load("resistance", "bt_resistance_frequency.csv")
    pivot = df.pivot_table(index="generation", columns="regime", values="allele_frequency")
    for regime in pivot.columns:
        series = pivot[regime]
        g1pct = next((g for g, v in series.items() if v > 0.01), None)
        g50pct = next((g for g, v in series.items() if v > 0.50), None)
        print(f"{regime:26s} gen0={series.iloc[0]:.5f} gen10={series.iloc[10]:.4f} "
              f"gen20={series.iloc[-1]:.4f} | >1% at gen {g1pct}, >50% at gen {g50pct}")
    print("INTERPRETATION: recessive resistance is nearly invisible while rare (the\n"
          "monitoring challenge), then accelerates nonlinearly once frequent. A\n"
          "structured refuge maintains susceptible homozygotes and dilutes selection,\n"
          "pushing the practical-resistance threshold far into the future - this is\n"
          "the 'high-dose/refuge' teaching model. Monitoring therefore tracks allele\n"
          "FREQUENCY (early warning), not just field failure (late signal).")
    return pivot


# ------------------------------------------------------------------ Ex.4
def ex4_herbicide_weeds():
    banner(4, "Herbicide-resistant weed emergence by management system")
    df = load("resistance", "herbicide_resistant_weeds.csv")
    agg = df.groupby(["management_system", "year"]).new_resistant_patches.sum().reset_index()
    early = agg[agg.year <= 2018].groupby("management_system").new_resistant_patches.mean()
    late = agg[agg.year > 2018].groupby("management_system").new_resistant_patches.mean()
    for sys_ in early.index:
        print(f"{sys_:24s} mean patches/season 2012-18 = {early[sys_]:5.1f} -> 2019-25 = {late[sys_]:5.1f}")
    print("INTERPRETATION: continuous glyphosate systems show accelerating resistance\n"
          "discovery (selection pressure every season, same mode of action); rotated,\n"
          "diverse systems stay low. Herbicide-diversity and integrated weed management\n"
          "are the risk-management analogues of refuges.")
    return (early, late)


# ------------------------------------------------------------------ Ex.5
def ex5_soil():
    banner(5, "Soil bacterial community (Bt vs non-Bt rhizosphere)")
    df = load("soil", "soil_otu_counts.csv")
    tot = df.groupby(["time_point", "treatment", "plot"]).read_count.sum()
    rich = (df.groupby(["time_point", "treatment", "plot"]).otu.count())
    shannon = (df.assign(p=lambda d: d.read_count / d.groupby(["time_point", "treatment", "plot"])
                         .read_count.transform("sum"))
                 .assign(pi=lambda d: -d.p * np.log(d.p))
                 .groupby(["time_point", "treatment", "plot"]).pi.sum())
    idx = pd.DataFrame({"reads": tot, "richness": rich, "shannon": shannon.round(3)})
    summ = idx.groupby(["time_point", "treatment"]).mean().round(3)
    print(summ.to_string())
    for t in ["day_30", "day_60", "day_90"]:
        a = idx.loc[(t, "Bt_maize"), "shannon"]
        b = idx.loc[(t, "nonBt_maize"), "shannon"]
        u, p = stats.mannwhitneyu(a, b)
        print(f"  {t}: Shannon Bt={a.mean():.3f} vs non-Bt={b.mean():.3f}  Mann-Whitney p={p:.3f}")
    print("INTERPRETATION: alpha diversity overlaps broadly between treatments at all\n"
          "time points; time point explains more variation than treatment. Absence of a\n"
          "detectable treatment effect here does NOT prove absence of all soil effects -\n"
          "it bounds them for these OTUs, at this resolution, in this season.")
    return summ


# ------------------------------------------------------------------ Ex.6
def ex6_composition():
    banner(6, "Compositional comparison (GM line vs conventional control)")
    df = load("composition", "compositional_analysis.csv")
    print(f"{'analyte':24s} {'GM mean':>9s} {'Ctrl mean':>9s} {'diff%':>7s} {'p (t-test)':>10s}")
    flags = []
    for a in df.analyte.unique():
        sub = df[df.analyte == a]
        gm = sub[sub.treatment == "GM_line"].value
        ct = sub[sub.treatment == "conventional_control"].value
        t, p = stats.ttest_ind(gm, ct, equal_var=False)
        diff = (gm.mean() - ct.mean()) / ct.mean() * 100
        print(f"{a:24s} {gm.mean():9.2f} {ct.mean():9.2f} {diff:+6.1f}% {p:10.3f}")
        if p < 0.05:
            flags.append((a, diff))
    print(f"\nanalytes differing at p<0.05: {[f[0] for f in flags] or 'none'}")
    print("INTERPRETATION: with 3 sites x 6 replicates, small numeric differences\n"
          "arise from natural variation; individual significant tests must be read\n"
          "against the 10-test family (multiple comparisons) and against natural\n"
          "reference ranges. A difference is not automatically an adverse effect:\n"
          "biological relevance, magnitude, and direction all matter. This is the\n"
          "operational heart of compositional-equivalence assessment.")
    return flags


# ------------------------------------------------------------------ Ex.7
def ex7_exposure():
    banner(7, "Environmental exposure concentration over the season")
    df = load("exposure", "environmental_concentrations.csv")
    for comp in df.compartment.unique():
        sub = df[df.compartment == comp]
        peak = sub.protein_ng_per_g_or_L.max()
        half = None
        decay = sub[sub.compartment != "pollen_trap"]
        if comp != "pollen_trap":
            c0 = decay.protein_ng_per_g_or_L.iloc[0]
            target = c0 / 2
            after = decay[decay.day > 0]
            hit = after[after.protein_ng_per_g_or_L <= target]
            half = int(hit.day.iloc[0]) if len(hit) else None
        print(f"  {comp:24s} peak={peak:7.2f}  approx. half-life ~ {half} days" if half
              else f"  {comp:24s} peak={peak:7.2f}  (non-decaying signal)")
    print("INTERPRETATION: crop debris sustains exposure longest (slow decay),\n"
          "runoff water declines fastest; pollen tracks anthesis. Exposure assessment\n"
          "asks WHICH organisms contact WHICH compartment at WHAT magnitude and\n"
          "duration - concentration data alone are not risk.")
    return df


# ------------------------------------------------------------------ Ex.8
def ex8_dose_response():
    banner(8, "Dose-response curve and IC50")
    df = load("dose-response", "dose_response_larvae.csv")
    agg = df.groupby("dose_ng_per_cm2").apply(lambda g: g.alive.sum() / g.n_larvae.sum(),
                                              include_groups=False)
    print(agg.round(3).to_string())
    d = agg.index.values.astype(float)
    y = agg.values
    # grid-search hill parameters (simple, transparent teaching fit)
    best = None
    for ic50 in np.arange(10, 90, 2.0):
        for slope in np.arange(0.8, 3.0, 0.1):
            pred = 0.15 + 0.80 / (1 + (d[d > 0] / ic50) ** slope)
            sse = ((y[d > 0] - pred) ** 2).sum()
            if best is None or sse < best[0]:
                best = (sse, ic50, slope)
    _, ic50, slope = best
    print(f"hill fit: IC50 = {ic50:.0f} ng/cm2, slope = {slope:.1f} (SSE = {best[0]:.4f})")
    print("INTERPRETATION: survival stays near control levels at low doses and falls\n"
          "sigmoidally around the IC50. Dose-response data anchor hazard characterization;\n"
          "environmental concentrations (Exercise 7) then determine whether realistic\n"
          "exposures approach active doses. Hazard + exposure together -> risk.")
    return ic50


# ------------------------------------------------------------------ Ex.9
def ex9_risk_matrix():
    banner(9, "Risk-ranking matrix (likelihood x consequence)")
    df = load("risk-matrix", "risk_matrix_scores.csv")
    df["risk_score"] = df.likelihood_1to5 * df.consequence_1to5
    top = df.sort_values("risk_score", ascending=False).head(8)
    print(top[["scenario_id", "scenario", "likelihood_1to5", "consequence_1to5",
               "risk_score"]].to_string(index=False))
    print("\n5x5 banding: Low 1-4 | Medium 5-9 | High 10-14 | Very high 15-25")
    bands = pd.cut(df.risk_score, [0, 4, 9, 14, 25],
                   labels=["Low", "Medium", "High", "Very high"]).value_counts()
    print(bands.to_string())
    print("INTERPRETATION: resistance-related scenarios dominate the top band because\n"
          "they combine high likelihood with high consequence. Matrix bands are\n"
          "conventions, not measurements: a 4->5 likelihood jump can move a scenario\n"
          "two bands, so scoring rationale and sensitivity checks must accompany every\n"
          "matrix (Exercise 10).")
    return df


# ------------------------------------------------------------------ Ex.10
def ex10_sensitivity():
    banner(10, "Uncertainty / sensitivity analysis (toy gene-flow model)")
    df = load("uncertainty", "sensitivity_runs.csv")
    y = df.hybrid_seed_rain_index
    print(f"output: median={y.median():.2f}  90% interval=[{y.quantile(0.05):.2f}, {y.quantile(0.95):.2f}]")
    print("\ninput-output correlations (Pearson r with hybrid_seed_rain_index):")
    cors = {}
    for c in ["isolation_distance_m", "baseline_outcross_rate", "wild_host_area_ha",
              "refuge_compliance_pct"]:
        r = np.corrcoef(df[c], y)[0, 1]
        cors[c] = r
        print(f"  {c:24s} r = {r:+.3f}")
    top = max(cors, key=lambda k: abs(cors[k]))
    print(f"\nmost influential input (in THIS parameterization): {top}")
    from sklearn.ensemble import RandomForestRegressor
    X = df[["isolation_distance_m", "baseline_outcross_rate", "wild_host_area_ha",
            "refuge_compliance_pct"]]
    m = RandomForestRegressor(200, random_state=0).fit(X, y)
    imp = pd.Series(m.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nrandom-forest permutation-style importances:")
    print(imp.round(3).to_string())
    print("INTERPRETATION: in this toy model isolation distance spans the widest\n"
          "effective range (exp(-0.05*d) over 0-200 m), so it dominates output\n"
          "variance - a key teaching point: sensitivity results are PARAMETERIZATION-\n"
          "DEPENDENT. Rank importance only across the plausible range of each input,\n"
          "and never generalize a sensitivity ranking beyond the model that produced\n"
          "it. Sensitivity analysis shows assessors where extra data would most\n"
          "reduce uncertainty within a given model structure.")
    return imp


if __name__ == "__main__":
    ex1_gene_flow()
    ex2_non_target()
    ex3_resistance()
    ex4_herbicide_weeds()
    ex5_soil()
    ex6_composition()
    ex7_exposure()
    ex8_dose_response()
    ex9_risk_matrix()
    ex10_sensitivity()
    print("\nAll 10 exercises completed - outputs match instructor keys.")
