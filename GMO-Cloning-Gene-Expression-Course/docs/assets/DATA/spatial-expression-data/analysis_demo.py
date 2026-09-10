#!/usr/bin/env python3
"""Lab-08 starter: bulk RNA-seq, single-cell and spatial mini-workflows.

All inputs are the SIMULATED course datasets in DATA/. Requires numpy,
pandas, scikit-learn (pip install numpy pandas scikit-learn matplotlib).
Run from the course root:  python DATA/spatial-expression-data/analysis_demo.py
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.dirname(HERE)


def load(name, folder="gene-expression-data", index_col=0):
    return pd.read_csv(os.path.join(DATA, folder, name), index_col=index_col)


# ---------------------------------------------------------------- Part A: bulk
def bulk_rnaseq():
    counts = load("rnaseq_counts.csv")
    meta = load("metadata.csv")
    lib = counts.sum(axis=0)
    lognorm = np.log2(counts / lib * 1e6 + 1)
    wt = lognorm[meta[meta.condition == "WT"].index]
    ko = lognorm[meta[meta.condition == "KO"].index]
    lfc = ko.mean(axis=1) - wt.mean(axis=1)
    # teaching-level t-test on log values (research practice: DESeq2/edgeR on counts)
    from scipy import stats
    pvals = np.asarray(stats.ttest_ind(ko.values, wt.values, axis=1).pvalue)
    # Benjamini-Hochberg FDR implemented directly (teaching version)
    order = np.argsort(pvals)
    ranked = pvals[order] * len(pvals) / (np.arange(len(pvals)) + 1)
    bh = np.minimum.accumulate(ranked[::-1])[::-1]
    fdr = np.empty_like(bh)
    fdr[order] = np.clip(bh, 0, 1)
    sig = (np.abs(lfc) > 1) & (fdr < 0.05)
    print(f"[bulk] genes passing |log2FC|>1 & FDR<0.05: {sig.sum()}")
    print(lfc[sig].sort_values().head(8))
    return lfc, fdr, sig


# ----------------------------------------------------------- Part B: single-cell
def single_cell():
    counts = load("single_cell_counts.csv")        # cells x genes (row per cell)
    cells = counts
    lib_size = cells.sum(axis=1)
    n_genes = (cells > 0).sum(axis=1)
    keep = (lib_size > 500) & (n_genes > 200)
    sub = cells.loc[keep]
    lognorm = np.log2(sub.div(sub.sum(axis=1), axis=0) * 1e6 + 1)
    X = lognorm.values
    Xc = X - X.mean(axis=0)
    Xc = Xc[:, Xc.std(axis=0) > 0]                          # drop zero-variance genes
    PCs_full = None  # PCs computed below from filtered matrix
    U, S, _ = np.linalg.svd(Xc, full_matrices=False)
    PCs = U[:, :2] * S[:2]
    from sklearn.cluster import KMeans
    labels = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(PCs)
    lab_series = pd.Series(labels, index=sub.index)
    for g in ["pax6a", "myod1", "hbbe1"]:
        if g in sub.columns:
            mean_by_cluster = sub[g].groupby(lab_series).mean()
            print(f"[sc] {g} mean by cluster: "
                  f"{ {int(k): v for k, v in mean_by_cluster.round(1).items()} }")
    print(f"[sc] cluster sizes: {lab_series.value_counts().sort_index().to_dict()}")
    print(f"[sc] cells kept: {keep.sum()}/{len(cells)}")
    return labels


# --------------------------------------------------------------- Part C: spatial
def spatial():
    mat = load("spatial_matrix.csv", "spatial-expression-data")
    coords = load("spot_coordinates.csv", "spatial-expression-data")
    regions = load("tissue_annotation.csv", "spatial-expression-data")
    region_means = mat.join(regions).groupby("region").mean()
    print("[spatial] top 3 markers per region:")
    for region in region_means.index:
        top = region_means.loc[region].sort_values(ascending=False).head(3)
        print(f"  {region}: {list(top.index)}")
    # gradient test on edge_gene vs distance from top edge (y)
    g = "edge_gene"
    expr = mat[g]
    r = np.corrcoef(expr.values, coords.loc[expr.index, "y"].values)[0, 1]
    print(f"[spatial] {g} vs distance-to-top-edge Pearson r = {r:.2f}")


if __name__ == "__main__":
    print("=== Part A: bulk RNA-seq (simulated) ===")
    bulk_rnaseq()
    print("\n=== Part B: single-cell (simulated) ===")
    single_cell()
    print("\n=== Part C: spatial (simulated) ===")
    spatial()
    print("\nAll results from SIMULATED teaching data - not real experiments.")
