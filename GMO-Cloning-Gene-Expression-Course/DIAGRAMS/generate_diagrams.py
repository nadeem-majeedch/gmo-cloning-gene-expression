#!/usr/bin/env python3
"""Generate all schematic teaching diagrams for the course (matplotlib).
Schematic illustrations only - no real microscopy/data images.
Usage: python DIAGRAMS/generate_diagrams.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Wedge

BASE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)

plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})

def save(fig, name):
    fig.savefig(os.path.join(BASE, name), dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("wrote", name)

def box(ax, x, y, w, h, text, fc="#dbeafe", ec="#1e3a8a", fs=8, lw=1.2):
    r = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                       fc=fc, ec=ec, lw=lw)
    ax.add_patch(r)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs)

def arrow(ax, x1, y1, x2, y2, color="#1e3a8a"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                 arrowstyle="-|>", mutation_scale=12, color=color, lw=1.4))

# ------------------------------------------------------------------
def plasmid_map():
    fig, ax = plt.subplots(figsize=(6, 5.4))
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.5, 1.5); ax.axis("off")
    circ = Circle((0, 0), 1.0, fill=False, ec="#1e3a8a", lw=3)
    ax.add_patch(circ)
    ax.text(0, -1.32, "pDevGFP-style cloning vector (schematic, 3.2 kb)",
            ha="center", fontsize=8, style="italic")
    marks = [("ori", (0.72, -0.72)), ("kanR", (-0.72, -0.72)),
             ("promoter", (-0.85, 0.45)), ("GFP/reporter", (0.0, 0.95)),
             ("terminator", (0.85, 0.45)), ("MCS", (0.0, -0.02))]
    for label, (x, y) in marks:
        ax.plot([x*1.0, x*1.22], [y*1.0, y*1.22], color="#64748b", lw=1)
        ax.text(x*1.3, y*1.3, label, ha="center", va="center", fontsize=8.5,
                bbox=dict(boxstyle="round,pad=0.25", fc="#dbeafe", ec="#1e3a8a", lw=0.8))
    ax.plot(0, 0, "o", ms=4, color="#dc2626")
    ax.text(0.06, -0.12, "MCS", fontsize=8, color="#dc2626")
    save(fig, "plasmid_map.png")

def restriction_cloning():
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    box(ax, 0.2, 2.6, 3.6, 0.7, "Insert DNA (with EcoRI / HindIII ends)", "#fef3c7", "#b45309")
    box(ax, 0.2, 0.7, 3.6, 0.7, "Vector DNA (cut with same enzymes)", "#dbeafe", "#1e3a8a")
    box(ax, 4.5, 1.55, 2.4, 0.9, "Mix + T4\nDNA ligase", "#dcfce7", "#15803d")
    box(ax, 7.5, 1.55, 2.2, 0.9, "Recombinant\nplasmid", "#fee2e2", "#b91c1c")
    arrow(ax, 3.9, 2.95, 4.4, 2.35)
    arrow(ax, 3.9, 1.05, 4.4, 1.65)
    arrow(ax, 7.0, 2.0, 7.4, 2.0)
    ax.text(5.0, 0.6, "compatible sticky ends anneal → ligase seals",
            fontsize=8, ha="center", color="#334155")
    save(fig, "restriction_cloning.png")

def gibson_assembly():
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    steps = [("1. 5′ exonuclease\nchews back ends", 0.3, "#fee2e2", "#b91c1c"),
             ("2. Overlaps\nanneal", 2.85, "#dbeafe", "#1e3a8a"),
             ("3. Polymerase\nfills gaps", 5.4, "#dcfce7", "#15803d"),
             ("4. Ligase seals\nnicks", 7.7, "#fef3c7", "#b45309")]
    for i, (t, x, fc, ec) in enumerate(steps):
        box(ax, x, 2.2, 2.1, 1.0, t, fc, ec)
        if i < 3: arrow(ax, x + 2.15, 2.7, x + 2.5, 2.7)
    ax.text(5, 1.3, "Fragments designed with 20–40 bp terminal overlaps →\n"
                    "seamless multi-fragment assembly in one tube",
            ha="center", fontsize=8.5, color="#334155")
    save(fig, "gibson_assembly.png")

def golden_gate():
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    ax.text(5, 3.55, "Type IIS enzyme cuts OUTSIDE its recognition site", ha="center",
            fontsize=9.5, weight="bold")
    # recognition site and cut positions
    ax.plot([1, 9], [2.3, 2.3], color="#1e3a8a", lw=2)
    ax.plot([1, 9], [1.9, 1.9], color="#1e3a8a", lw=2)
    ax.add_patch(Rectangle((3.0, 1.85), 1.4, 0.5, fc="#fee2e2", ec="#b91c1c"))
    ax.text(3.7, 2.55, "recognition site (GGTCTC)", ha="center", fontsize=8, color="#b91c1c")
    for xc in (2.6, 4.9):
        ax.plot([xc, xc], [1.8, 2.4], color="#dc2626", lw=2)
    ax.text(2.6, 1.45, "cut", ha="center", fontsize=8, color="#dc2626")
    ax.text(4.9, 1.45, "cut", ha="center", fontsize=8, color="#dc2626")
    ax.text(5.9, 2.1, "→ 4-bp overhang = designer-chosen", fontsize=8.5, color="#15803d")
    ax.text(5, 0.6, "Digest + ligate in one pot: correct overhang pairs assemble directionally;\n"
                    "recognition sites are consumed → modular, multiplex cloning",
            ha="center", fontsize=8.5, color="#334155")
    save(fig, "golden_gate.png")

def expression_cassette():
    fig, ax = plt.subplots(figsize=(8, 2.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    parts = [("Promoter", 0.4, 1.7, "#dbeafe", "#1e3a8a"),
             ("5′UTR /\nKozak-RBS", 2.3, 1.4, "#e0f2fe", "#0369a1"),
             ("CDS /\nGOI", 3.9, 1.6, "#dcfce7", "#15803d"),
             ("Tag\n(optional)", 5.7, 1.4, "#fef9c3", "#a16207"),
             ("3′UTR", 7.3, 1.2, "#e0f2fe", "#0369a1"),
             ("Terminator /\npolyA", 8.7, 1.8, "#fee2e2", "#b91c1c")]
    for t, x, w, fc, ec in parts:
        box(ax, x, 1.0, w, 1.0, t, fc, ec)
    arrow(ax, 0.5, 2.35, 11.4, 2.35, "#64748b")
    ax.text(6, 2.6, "transcription →", ha="center", fontsize=8.5, color="#64748b")
    ax.text(6, 0.45, "One expression cassette = promoter → translation-initiation context → coding "
                     "sequence (± tag) → terminator/polyA",
            ha="center", fontsize=8.5, color="#334155")
    save(fig, "expression_cassette.png")

def reporter_constructs():
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 4.4); ax.axis("off")
    ax.text(6, 4.1, "Three reporter designs answer three questions", ha="center",
            fontsize=9.5, weight="bold")
    box(ax, 0.3, 2.9, 4.4, 0.8, "[promoter/enhancer] → [reporter]\nQ: where/when is it ACTIVE?", "#dbeafe", "#1e3a8a")
    box(ax, 5.3, 2.9, 6.2, 0.8, "[candidate enhancer] + [minimal promoter → reporter]\nQ: does this sequence ENHANCE?", "#e0f2fe", "#0369a1")
    box(ax, 0.3, 1.2, 4.4, 0.8, "[strong promoter] → [protein::GFP]\nQ: where does the PROTEIN go?", "#dcfce7", "#15803d")
    box(ax, 5.3, 1.2, 6.2, 0.8, "Controls: promoterless vector · empty vector · motif mutant\n"
                                "known-active promoter · transfection normalization",
        "#fef3c7", "#b45309")
    ax.text(6, 0.4, "Reporter reports the regulatory SEQUENCE's behavior — validate against endogenous expression (ISH/IF).",
            ha="center", fontsize=8, color="#b91c1c")
    save(fig, "reporter_constructs.png")

def crispr_mechanism():
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 5); ax.axis("off")
    ax.text(6, 4.7, "CRISPR–Cas9: target recognition and repair outcomes", ha="center",
            fontsize=9.5, weight="bold")
    ax.plot([1, 11], [3.4, 3.4], color="#1e3a8a", lw=2.4)
    ax.plot([1, 11], [3.0, 3.0], color="#1e3a8a", lw=2.4)
    ax.add_patch(Rectangle((3.0, 2.95), 4.4, 0.5, fc="#dcfce7", ec="#15803d"))  # protospacer
    ax.add_patch(Rectangle((7.4, 2.95), 0.8, 0.5, fc="#fef3c7", ec="#b45309"))  # PAM
    ax.text(5.2, 3.65, "protospacer (20 nt, guide pairs here)", ha="center", fontsize=8, color="#15803d")
    ax.text(7.8, 2.6, "PAM (NGG)", ha="center", fontsize=8, color="#b45309")
    ax.plot([5.2, 5.2], [2.7, 3.7], color="#dc2626", lw=2.4)
    ax.text(5.2, 2.35, "DSB", ha="center", fontsize=9, color="#dc2626", weight="bold")
    box(ax, 1.0, 0.6, 4.2, 1.2, "NHEJ (error-prone)\n→ small indels → KNOCKOUT", "#fee2e2", "#b91c1c")
    box(ax, 6.8, 0.6, 4.2, 1.2, "HDR (donor template)\n→ precise insert/correction → KNOCK-IN", "#dbeafe", "#1e3a8a")
    arrow(ax, 4.6, 2.2, 3.1, 1.85)
    arrow(ax, 5.8, 2.2, 8.9, 1.85)
    save(fig, "crispr_mechanism.png")

def base_prime_editing():
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 4); ax.axis("off")
    box(ax, 0.3, 2.2, 5.4, 1.3, "BASE EDITORS\nCas9(dead/nick) + deaminase\nC→T · A→G conversions, no DSB\n(limit: editing window, bystanders)",
        "#dbeafe", "#1e3a8a")
    box(ax, 6.3, 2.2, 5.4, 1.3, "PRIME EDITORS\nCas9-nickase + reverse transcriptase\n+ pegRNA: search-and-replace\n(limit: efficiency, edit size)",
        "#dcfce7", "#15803d")
    ax.text(6, 1.2, "Both avoid double-strand breaks → no reliance on HDR", ha="center",
            fontsize=9, color="#334155")
    save(fig, "base_prime_editing.png")

def morphogen_gradient():
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    x = np.linspace(0, 10, 200)
    y = np.exp(-0.28 * x)
    ax.plot(x, y, color="#b91c1c", lw=2.5)
    ax.fill_between(x, 0, y, color="#fecaca", alpha=0.5)
    for i, (th, lab) in enumerate([(0.62, "Fate A"), (0.30, "Fate B"), (0.10, "Fate C")]):
        ax.axhline(th, color="#1e3a8a", ls="--", lw=1)
        ax.text(9.6, th + 0.02, lab, fontsize=9, ha="right", color="#1e3a8a")
    ax.text(0.2, 1.0, "source (e.g., Shh from floor plate/notochord)", fontsize=8.5, color="#b91c1c")
    ax.set_xlabel("distance from source"); ax.set_ylabel("signal concentration")
    ax.set_title("Morphogen gradient + thresholds → distinct fates (French-flag model)")
    ax.set_ylim(0, 1.1); ax.set_xlim(0, 10)
    save(fig, "morphogen_gradient.png")

def grn_cascade():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); ax.axis("off")
    levels = [("Maternal inputs (Bcd / Nos)", 4.5, "#fee2e2", "#b91c1c"),
              ("Gap genes (Hb, Kr, Gt, Kni)", 3.7, "#fef3c7", "#b45309"),
              ("Pair-rule genes (eve, ftz) — 7 stripes", 2.9, "#dbeafe", "#1e3a8a"),
              ("Segment-polarity genes (en, wg) — 14 stripes", 2.1, "#dcfce7", "#15803d"),
              ("Hox genes — segment identity", 1.3, "#e0f2fe", "#0369a1"),
              ("Terminal differentiation genes", 0.5, "#f1f5f9", "#334155")]
    for t, y, fc, ec in levels:
        box(ax, 1.4, y, 7.2, 0.55, t, fc, ec)
    for y in [4.5, 3.7, 2.9, 2.1, 1.3]:
        arrow(ax, 5, y - 0.02, 5, y - 0.16)
    ax.text(9.2, 2.7, "cross-regulation\nsharpens boundaries", fontsize=8, color="#334155")
    save(fig, "grn_cascade.png")

def neural_tube_pattern():
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.set_xlim(0, 8); ax.set_ylim(0, 6); ax.axis("off")
    ax.add_patch(Rectangle((3, 0.6), 2, 4.8, fc="#f1f5f9", ec="#334155"))
    ax.text(4, 5.65, "neural tube (cross-section)", ha="center", fontsize=9)
    ax.add_patch(Rectangle((3.0, 0.6), 2, 0.55, fc="#fca5a5"))
    ax.add_patch(Rectangle((3.0, 1.15), 2, 0.8, fc="#fdba74"))
    ax.add_patch(Rectangle((3.0, 1.95), 2, 1.1, fc="#fde047"))
    ax.add_patch(Rectangle((3.0, 3.05), 2, 2.35, fc="#a5f3fc"))
    ax.text(5.2, 0.87, "floor plate / V3", fontsize=8)
    ax.text(5.2, 1.5, "motor neurons", fontsize=8)
    ax.text(5.2, 2.45, "V2 / V1", fontsize=8)
    ax.text(5.2, 4.1, "dorsal interneurons (BMP)", fontsize=8)
    ax.text(1.6, 1.0, "Shh\n(notochord /\nfloor plate)", fontsize=8.5, color="#b91c1c", ha="center")
    arrow(ax, 2.4, 1.2, 3.4, 1.6, "#b91c1c")
    ax.text(1.7, 4.6, "BMPs\n(roof plate)", fontsize=8.5, color="#0369a1", ha="center")
    arrow(ax, 2.4, 4.6, 3.4, 4.3, "#0369a1")
    save(fig, "neural_tube_pattern.png")

def cloning_workflow():
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")
    stages = ["Identify\ntarget gene", "Design\nconstruct", "Obtain/amplify\nDNA", "Prepare\nvector",
              "Assemble\ninsert+vector", "Introduce\ninto host", "Select\ntransformants",
              "Screen\ncolonies", "Validate\ndigest", "Sequence\nconfirm", "Use\nconstruct"]
    xs = np.linspace(0.5, 10.6, 11)
    for i, (s, x) in enumerate(zip(stages, xs)):
        box(ax, x, 2.4, 1.05, 1.2, s, "#dbeafe" if i % 2 == 0 else "#e0f2fe", "#1e3a8a", fs=6.6)
        if i < 10:
            arrow(ax, x + 1.08, 3.0, x + 1.42, 3.0)
    ax.text(6, 1.4, "every stage: purpose · principle · inputs · outputs · common errors · validation",
            ha="center", fontsize=8.5, color="#334155")
    save(fig, "cloning_workflow.png")

def selection_screening():
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    funnel = [("Transformation — everything mixed", 9.0, "#f1f5f9", "#334155"),
              ("SELECTION (antibiotic) — vector-carriers only", 7.6, "#dbeafe", "#1e3a8a"),
              ("Candidate colonies (hundreds)", 6.2, "#e0f2fe", "#0369a1"),
              ("SCREENING (colony PCR / blue-white) — shortlist", 4.8, "#fef3c7", "#b45309"),
              ("VALIDATION (digest matches map)", 3.4, "#dcfce7", "#15803d"),
              ("SEQUENCE confirmation (Sanger)", 2.2, "#fee2e2", "#b91c1c"),
              ("FUNCTIONAL validation — the actual science", 1.0, "#ede9fe", "#6d28d9")]
    for t, w, fc, ec in funnel:
        box(ax, (10 - w) / 2, 0, w, 0.9, t, fc, ec, fs=8)
        ax.set_ylim(0, 6)
    for y in [6.2, 4.8, 3.4, 2.2, 1.0]:
        pass
    ax.clear(); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    for i, (t, w, fc, ec) in enumerate(funnel):
        y = 5.0 - i * 0.78
        box(ax, (10 - w) / 2, y, w, 0.62, t, fc, ec, fs=7.8)
        if i < len(funnel) - 1:
            arrow(ax, 5, y - 0.02, 5, y - 0.16)
    save(fig, "selection_screening.png")

def gmo_workflows():
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 5); ax.axis("off")
    cols = [("BACTERIA", 0.3, "transform\n→ select → screen", "#dbeafe", "#1e3a8a"),
            ("PLANTS", 4.2, "Agrobacterium /\nbiolistics → tissue culture\n→ regenerate plant", "#dcfce7", "#15803d"),
            ("ANIMALS", 8.1, "embryo injection /\nSCNT / ES cells → founders\n→ germline breeding", "#fef3c7", "#b45309")]
    for title, x, body, fc, ec in cols:
        box(ax, x, 3.4, 3.6, 0.6, title, fc, ec)
        box(ax, x, 1.1, 3.6, 2.1, body, "#ffffff", ec)
        arrow(ax, x + 1.8, 3.35, x + 1.8, 3.25)
    ax.text(6, 0.4, "Common spine: construct → delivery → selection → screening → validation → phenotype",
            ha="center", fontsize=8.5, color="#334155")
    save(fig, "gmo_workflows.png")

def ish_workflow():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = ["Sample\npreparation", "Probe design\n(antisense)", "Hybridization", "Stringent\nwashing",
             "Detection\n(chromogenic/fluor)", "Imaging", "Spatial\ninterpretation"]
    xs = np.linspace(0.4, 9.9, 7)
    for i, (s, x) in enumerate(zip(steps, xs)):
        box(ax, x, 1.0, 1.35, 1.1, s, "#dbeafe" if i % 2 else "#e0f2fe", "#1e3a8a", fs=6.6)
        if i < 6: arrow(ax, x + 1.38, 1.55, x + 1.62, 1.55)
    ax.text(6, 0.35, "Controls: sense probe / no-probe (negative) · known-marker probe (positive) · staging check",
            ha="center", fontsize=8, color="#334155")
    save(fig, "ish_workflow.png")

def qpcr_workflow():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = ["RNA + DNase", "Reverse\ntranscription", "qPCR\n(triplicates)", "Cq values",
             "ΔCt vs reference", "ΔΔCt vs control", "Fold change\n2^(−ΔΔCt)"]
    xs = np.linspace(0.4, 9.9, 7)
    for i, (s, x) in enumerate(zip(steps, xs)):
        box(ax, x, 1.0, 1.35, 1.1, s, "#dcfce7" if i % 2 else "#e0f2fe", "#15803d", fs=6.6)
        if i < 6: arrow(ax, x + 1.38, 1.55, x + 1.62, 1.55)
    ax.text(6, 0.35, "Controls: no-RT · no-template · validated reference genes · inter-run calibrator",
            ha="center", fontsize=8, color="#334155")
    save(fig, "qpcr_workflow.png")

def rnaseq_workflow():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = ["RNA", "Library prep\n(fragment→cDNA)", "Sequencing", "Map/quantify\n(counts)",
             "Normalize\n(size factors)", "Model + FDR", "DE genes /\npathways"]
    xs = np.linspace(0.4, 9.9, 7)
    for i, (s, x) in enumerate(zip(steps, xs)):
        box(ax, x, 1.0, 1.35, 1.1, s, "#fee2e2" if i % 2 else "#e0f2fe", "#b91c1c", fs=6.4)
        if i < 6: arrow(ax, x + 1.38, 1.55, x + 1.62, 1.55)
    ax.text(6, 0.35, "≥3 biological replicates · balanced batch design · report effect size + FDR",
            ha="center", fontsize=8, color="#334155")
    save(fig, "rnaseq_workflow.png")

def scrnaseq_workflow():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = ["Single-cell\nsuspension", "Barcoding\n(UMIs)", "Sequencing", "Count matrix\n(cells×genes)",
             "QC + normalize", "PCA + cluster", "Annotate +\ntrajectory"]
    xs = np.linspace(0.4, 9.9, 7)
    for i, (s, x) in enumerate(zip(steps, xs)):
        box(ax, x, 1.0, 1.35, 1.1, s, "#dbeafe" if i % 2 else "#fef3c7", "#1e3a8a", fs=6.4)
        if i < 6: arrow(ax, x + 1.38, 1.55, x + 1.62, 1.55)
    ax.text(6, 0.35, "Spatial context is LOST at dissociation → pair with spatial methods for location claims",
            ha="center", fontsize=8, color="#b91c1c")
    save(fig, "scrnaseq_workflow.png")

def spatial_workflow():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 3); ax.axis("off")
    steps = ["Tissue\nsection", "Barcoded capture\nOR probe imaging", "Sequencing /\ndecoding", "Spatial\nmatrix",
             "Align to\nhistology", "Region annotation", "Gradients · domains\n· ligand–receiver"]
    xs = np.linspace(0.4, 9.9, 7)
    for i, (s, x) in enumerate(zip(steps, xs)):
        box(ax, x, 1.0, 1.35, 1.1, s, "#dcfce7" if i % 2 else "#dbeafe", "#15803d", fs=6.2)
        if i < 6: arrow(ax, x + 1.38, 1.55, x + 1.62, 1.55)
    ax.text(6, 0.35, "Keeps what scRNA-seq loses: position (spot ≈ 1–several cells → deconvolution may be needed)",
            ha="center", fontsize=8, color="#334155")
    save(fig, "spatial_workflow.png")

def expression_heatmap():
    stages = ["1-cell", "oblong", "shield", "10 hpf", "18 hpf", "24 hpf", "48 hpf"]
    genes = ["nanos1", "dazl", "sox21a", "myod1", "pax6a", "shha", "ntl", "eve1", "wnt8a", "notch1a"]
    z = np.zeros((len(genes), len(stages)))
    for i, g in enumerate(genes[:3]):        # maternal: decay
        z[i] = np.linspace(2.2, -2.2, len(stages)) + rng.normal(0, 0.12, len(stages))
    for i, g in enumerate(genes[3:]):        # zygotic: rise
        lin = np.linspace(-2.0, 2.2, len(stages))
        z[i+3] = np.sign(lin) * (np.abs(lin) ** 1.4) * rng.uniform(0.8, 1.2) + rng.normal(0, 0.12, len(stages))
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    im = ax.imshow(z, cmap="RdBu_r", vmin=-2.5, vmax=2.5, aspect="auto")
    ax.set_xticks(range(len(stages))); ax.set_xticklabels(stages, rotation=30)
    ax.set_yticks(range(len(genes))); ax.set_yticklabels(genes)
    ax.set_title("Developmental expression profiles (SIMULATED teaching data)\n"
                 "top rows: maternal (decay) · bottom rows: zygotic (rise)", fontsize=9)
    plt.colorbar(im, label="z-scored expression")
    save(fig, "expression_heatmap.png")

def spatial_map_sim():
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
    n = 20
    x, y = np.meshgrid(np.linspace(0, 1.9, n), np.linspace(0, 1.9, n))
    noto = np.exp(-((y - 0.5) ** 2) / 0.008) * np.exp(-((x - 0.95) ** 2) / 1.2)
    somites = ((y > 0.7) & (y < 1.5) & (x > 0.5) & (x < 1.7)).astype(float) * 0.9
    neural = (y > 1.5).astype(float) * 0.9
    for ax, img, title in zip(axes, [noto, somites, neural],
                              ["'shha' → notochord", "'myod1' → somites", "'pax6a' → neural tube"]):
        im = ax.imshow(img + rng.normal(0, 0.05, img.shape), cmap="viridis", vmin=0, vmax=1.1)
        ax.set_title(title + " (in-silico)", fontsize=9)
        ax.set_xticks([]); ax.set_yticks([])
    fig.colorbar(im, ax=axes, shrink=0.8, label="relative expression (simulated)")
    fig.suptitle("Spatial-expression maps from the simulated spatial matrix (Module 12)", fontsize=10)
    save(fig, "spatial_map_sim.png")

if __name__ == "__main__":
    plasmid_map(); restriction_cloning(); gibson_assembly(); golden_gate()
    expression_cassette(); reporter_constructs(); crispr_mechanism(); base_prime_editing()
    morphogen_gradient(); grn_cascade(); neural_tube_pattern(); cloning_workflow()
    selection_screening(); gmo_workflows(); ish_workflow(); qpcr_workflow()
    rnaseq_workflow(); scrnaseq_workflow(); spatial_workflow()
    expression_heatmap(); spatial_map_sim()
    print("\nAll diagrams generated.")
