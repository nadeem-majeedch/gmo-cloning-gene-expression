#!/usr/bin/env python3
"""Generate all teaching diagrams for the GMO Environment and Risk Assessments course.

All figures are ORIGINAL schematic teaching diagrams (matplotlib) - no copyrighted
material reproduced. Deterministic; regenerate with:
    python DIAGRAMS/generate_diagrams.py   (from course root)
Outputs ~20 PNGs into DIAGRAMS/.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(42)

BLUE, GREEN, ORANGE, RED, GREY = "#2563eb", "#16a34a", "#ea580c", "#dc2626", "#6b7280"

def box(ax, x, y, w, h, text, fc="#eff6ff", ec=BLUE, fs=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.02", fc=fc, ec=ec, lw=1.6))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, weight=weight, wrap=True)

def arrow(ax, x1, y1, x2, y2, color=GREY, lw=1.8, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                 mutation_scale=16, color=color, lw=lw))

def canvas(w=10, h=6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    return fig, ax

def save(fig, name):
    fig.savefig(os.path.join(HERE, name), dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("  wrote", name)

# ---------- 01 Hazard vs Risk ----------
fig, ax = canvas()
box(ax, 2.5, 4.5, 3.6, 1.6, "HAZARD\nInherent potential to cause harm\n(agent - mechanism - endpoint)", fc="#fef3c7", ec=ORANGE, weight="bold")
box(ax, 7.5, 4.5, 3.6, 1.6, "RISK\nFunction of hazard x exposure\nx consequence, in context", fc="#dcfce7", ec=GREEN, weight="bold")
box(ax, 5, 2.6, 4.6, 1.0, "EXPOSURE  (contact: magnitude x duration)", fc="#eff6ff", ec=BLUE)
arrow(ax, 3.4, 3.7, 4.2, 3.1, ORANGE)
arrow(ax, 6.6, 3.1, 7.4, 3.7, GREEN)
ax.text(5, 1.6, "Hazard without exposure = no risk  (cobra behind thick glass)",
        ha="center", fontsize=11, style="italic")
ax.text(5, 1.0, "Conceptual relationship - not one universal equation; frameworks differ",
        ha="center", fontsize=9, color=GREY)
save(fig, "01-hazard-vs-risk.png")

# ---------- 02 ERA framework ----------
fig, ax = canvas(10, 7)
stages = ["Problem\nformulation", "Hazard\nidentification", "Hazard\ncharacterization",
          "Exposure\nassessment", "Risk\ncharacterization", "Uncertainty\nanalysis",
          "Risk\nmanagement", "Monitoring", "Risk\ncommunication"]
colors = [BLUE]*5 + [ORANGE] + [GREEN]*3
for i, (s, c) in enumerate(zip(stages, colors)):
    x = 1.55 + (i % 3) * 3.4
    y = 5.2 - (i // 3) * 1.8
    box(ax, x, y, 2.9, 1.25, s, fc="white", ec=c, weight="bold", fs=10)
    if i % 3 < 2:
        arrow(ax, x + 1.5, y, x + 1.9, y)
    if i % 3 == 2 and i < 8:
        arrow(ax, x, y - 0.68, x - 0.4, y - 1.1)
ax.text(5, 0.35, "Case-by-case - science-based - step-wise (Cartagena Annex III principles)",
        ha="center", fontsize=10, color=GREY, style="italic")
save(fig, "02-era-framework.png")

# ---------- 03 Gene flow decay ----------
fig, ax = plt.subplots(figsize=(9, 5.5))
d = np.linspace(0.5, 100, 300)
f = 0.03 * np.exp(-0.18 * d) + 0.00015
ax.semilogy(d, f, color=BLUE, lw=2.5, label="Model: f(d) = a·exp(-b·d)")
dist = np.array([1, 5, 10, 25, 50, 100])
obs = 0.03 * np.exp(-0.18 * dist) + 0.00015
ax.scatter(dist, obs, color=RED, zorder=5, s=45, label="Simulated field data")
ax.axhline(0.001, color=GREEN, ls="--", lw=1.5)
ax.text(60, 0.00135, "management threshold (0.1%)", color=GREEN, fontsize=9)
ax.set_xlabel("Distance from pollen source (m)")
ax.set_ylabel("Hybrid frequency (log scale)")
ax.set_title("Pollen-mediated gene flow decays with distance - buffer zones act on the steep segment")
ax.legend(); ax.grid(alpha=0.3)
save(fig, "03-gene-flow-decay.png")

# ---------- 04 Introgression pathway ----------
fig, ax = canvas(10, 5.5)
chain = ["GM crop", "Pollen\nshed & drift", "Wild relative\nfertilized", "F1 hybrid\n(viable, fertile?)", "Backcross\ngenerations", "INTROGRESSION\nin wild population"]
cols = [ORANGE]*5 + [RED]
for i, (t, c) in enumerate(zip(chain, cols)):
    box(ax, 1.1 + i * 1.56, 4.3, 1.75, 1.1, t, fc="white", ec=c, fs=8.5, weight="bold" if i == 5 else "normal")
    if i < 5:
        arrow(ax, 1.1 + i * 1.56 + 0.9, 4.3, 1.1 + (i + 1) * 1.56 - 0.9, 4.3)
gates = ["Sexual\ncompatibility", "Flowering\noverlap", "Hybrid\nfertility", "Backcross\nsuccess", "Trait\npersistence"]
for i, g in enumerate(gates):
    ax.text(1.1 + i * 1.56 + 0.78, 3.35, g, ha="center", fontsize=7.5, color=BLUE)
ax.text(5, 2.3, "Every gate is a filter - introgression requires ALL conditions",
        ha="center", fontsize=10, style="italic")
ax.text(5, 1.6, "Crop-to-crop: same pathway, consequence = seed purity / coexistence",
        ha="center", fontsize=9, color=GREY)
save(fig, "04-introgression-pathway.png")

# ---------- 05 Exposure pathway chain ----------
fig, ax = canvas(10, 5.5)
steps = [("Bt maize\n(toxin source)", ORANGE), ("Pollen\nshed & drift", GREY),
         ("Deposition on\nnon-target plants", BLUE), ("Herbivore larvae\nfeeding", GREEN),
         ("Predator /\nparasitoid", RED)]
for i, (t, c) in enumerate(steps):
    x = 1.2 + i * 1.9
    box(ax, x, 4.2, 1.8, 1.15, t, fc="white", ec=c, fs=9)
    if i < 4:
        arrow(ax, x + 0.95, 4.2, x + 1.9 - 0.95, 4.2)
        tf = ["shedding", "drift &\ndeposition", "consumption", "predation"][i]
        ax.text(x + 1.425, 4.85, tf, ha="center", fontsize=7.5, color=GREY)
ax.text(5, 2.9, "Each step multiplies a transfer factor - exposure typically attenuates by orders of magnitude",
        ha="center", fontsize=10, style="italic")
ax.text(5, 2.2, "Biology controls: shedding, degradation, synchrony", ha="center", fontsize=9, color=BLUE)
ax.text(5, 1.7, "Management controls: border rows, distance, planting date, residue timing", ha="center", fontsize=9, color=GREEN)
save(fig, "05-exposure-pathway.png")

# ---------- 06 Tiered testing ----------
fig, ax = canvas(10, 5.5)
tiers = [("TIER 1\nLaboratory\n(maximum hazard dose)", RED),
         ("TIER 2\nSemi-field\n(realistic dose, contained)", ORANGE),
         ("TIER 3\nField\n(realistic exposure, open)", GREEN)]
for i, (t, c) in enumerate(tiers):
    box(ax, 5, 4.6 - i * 1.5, 5.2, 1.2, t, fc="white", ec=c, weight="bold")
    if i < 2:
        ax.text(8.35, 4.6 - i * 1.5 - 0.55, "concern at realistic\nexposure? escalate",
                fontsize=8, color=GREY, ha="left")
        arrow(ax, 7.7, 4.6 - i * 1.5 - 0.25, 7.7, 4.6 - (i + 1) * 1.5 + 0.25)
ax.text(1.5, 4.6, "Escalation\ncriterion:\nrealistic\nexposure", fontsize=9, color=BLUE, ha="center", va="center")
ax.text(5, 0.55, "Lower tiers prevent wasted field trials AND premature 'no risk' claims",
        ha="center", fontsize=10, style="italic")
save(fig, "06-tiered-testing.png")

# ---------- 07 Resistance S-curve ----------
fig, ax = plt.subplots(figsize=(9, 5.5))
gens = np.arange(0, 26)
def recursion(q, r, h=0.02, s_rr=1.0, s_rs=0.02, s_ss=0.6):
    out = [q]
    for _ in gens[1:]:
        w_bar = (q**2)*s_rr + 2*q*(1-q)*s_rs + ((1-q)**2)*s_ss
        q_bt = ((q**2)*s_rr + q*(1-q)*s_rs) / w_bar
        q = q_bt * (1 - r) + q * r
        out.append(min(q, 1.0))
    return np.array(out)
for r, c, lbl in [(0.0, RED, "0% refuge"), (0.1, ORANGE, "10% refuge"), (0.2, GREEN, "20% refuge")]:
    ax.plot(gens, recursion(0.001, r), color=c, lw=2.4, label=lbl)
ax.axhline(0.5, color=GREY, ls="--", lw=1)
ax.text(0.4, 0.53, "resistance threshold (0.5)", fontsize=9, color=GREY)
ax.set_xlabel("Generation"); ax.set_ylabel("Resistance allele frequency q")
ax.set_title("Resistance build-up is slow, then explosive - refuges stretch the slow phase")
ax.legend(); ax.grid(alpha=0.3)
save(fig, "07-resistance-scurve.png")

# ---------- 08 Monitoring loop ----------
fig, ax = canvas(10, 6)
steps = ["Baseline\ndata", "Release\n(with conditions)", "Monitoring\n(indicators)", "Data analysis\nvs baseline",
         "Change\ndetected?", "Risk\nevaluation", "Management\nresponse"]
pos = [(1.4, 4.8), (3.7, 4.8), (6.0, 4.8), (8.3, 4.8), (8.3, 2.3), (6.0, 2.3), (3.7, 2.3)]
for (t, (x, y)) in zip(steps, pos):
    c = RED if t.startswith("Change") else BLUE
    box(ax, x, y, 2.0, 1.1, t, fc="white", ec=c, fs=9)
for i in range(3):
    arrow(ax, pos[i][0] + 1.05, pos[i][1], pos[i+1][0] - 1.05, pos[i+1][1])
arrow(ax, pos[3][0], pos[3][1] - 0.6, pos[4][0], pos[4][1] + 0.6)
arrow(ax, pos[4][0] - 1.05, pos[4][1], pos[5][0] + 1.05, pos[5][1])
arrow(ax, pos[5][0] - 1.05, pos[5][1], pos[6][0] + 1.05, pos[6][1])
ax.text(1.6, 2.3, "no change →\ncontinue\nmonitoring", fontsize=8.5, color=GREEN, ha="center")
arrow(ax, pos[4][0] - 1.05, pos[4][1] + 0.3, pos[2][0] + 1.05, pos[2][1] - 0.3, color=GREEN)
ax.text(5, 0.9, "Adaptive management: monitoring triggers are pre-agreed, with named response owners",
        ha="center", fontsize=10, style="italic")
save(fig, "08-monitoring-loop.png")

# ---------- 09 Risk matrix ----------
fig, ax = plt.subplots(figsize=(8.5, 6.5))
grid = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        grid[i, j] = (i + 1) * (j + 1)
ax.imshow(grid, cmap="RdYlGn_r", origin="lower", vmin=1, vmax=25, alpha=0.75)
hazards = {"Resistance (Cry1Ac)": (4, 3), "Gene flow to wild rel.": (3, 2),
           "Non-target predators": (2, 2), "Soil-community shift": (2, 1),
           "Volunteers (HT)": (3, 3), "HGT to microbes": (1, 1),
           "Herbicide-use shift": (4, 4), "New protein (food)": (1, 3)}
for name, (L, C) in hazards.items():
    ax.scatter(L - 1, C - 1, s=800, color="white", edgecolor="black", zorder=5)
    ax.text(L - 1, C - 1, name.split()[0][:4], ha="center", va="center", fontsize=7, zorder=6)
ax.set_xticks(range(5), ["1\nrare", "2\nunlikely", "3\npossible", "4\nlikely", "5\nfrequent"])
ax.set_yticks(range(5), ["1\nminor", "2\nmoderate", "3\nserious", "4\nmajor", "5\nsevere"])
ax.set_xlabel("Likelihood score"); ax.set_ylabel("Consequence score")
ax.set_title("Risk matrix (simulated scores) - placements cite evidence; anchors pre-declared")
for (n, xy) in [("Resist.", (4, 3)), ("Wild rel.", (3, 2)), ("Predator", (2, 2)), ("Soil", (2, 1)),
                ("Volunt.", (3, 3)), ("HGT", (1, 1)), ("Herb.", (4, 4)), ("Protein", (1, 3))]:
    ax.annotate(n, xy, xytext=(xy[0] - 1 + 0.18, xy[1] - 1 + 0.35), fontsize=7)
save(fig, "09-risk-matrix.png")

# ---------- 10 Food web ----------
fig, ax = canvas(10, 6)
nodes = {"GM crop": (2.0, 4.8, ORANGE), "Non-target\nplants/weeds": (4.6, 4.8, BLUE),
         "Herbivores": (2.0, 3.2, GREEN), "Pollinators": (4.6, 3.2, GREEN),
         "Predators &\nparasitoids": (3.3, 1.8, RED), "Granivorous\nbirds": (6.8, 3.2, RED),
         "Soil community": (1.4, 1.8, GREY)}
for n, (x, y, c) in nodes.items():
    box(ax, x, y, 1.9, 0.95, n, fc="white", ec=c, fs=8.5)
for (a, b) in [("GM crop", "Herbivores"), ("Non-target\nplants/weeds", "Herbivores"),
               ("GM crop", "Pollinators"), ("Non-target\nplants/weeds", "Pollinators"),
               ("Herbivores", "Predators &\nparasitoids"), ("Pollinators", "Predators &\nparasitoids"),
               ("Non-target\nplants/weeds", "Granivorous\nbirds"), ("GM crop", "Soil community"),
               ("Herbivores", "Granivorous\nbirds")]:
    x1, y1, _ = nodes[a]; x2, y2, _ = nodes[b]
    arrow(ax, x1, y1 - 0.2, x2, y2 + 0.2, lw=1.2)
ax.text(5, 0.7, "Trait effects propagate indirectly: fewer weeds → fewer seeds → fewer birds (UK FSE logic)",
        ha="center", fontsize=9.5, style="italic")
save(fig, "10-food-web.png")

# ---------- 11 Dose-response ----------
fig, ax = plt.subplots(figsize=(9, 5.5))
d = np.logspace(-2, 4, 300)
def logistic(dd, lc50, beta): return 1 / (1 + np.exp(-beta * (np.log10(dd) - np.log10(lc50))))
ax.plot(d, logistic(d, 1, 3) * 100, color=RED, lw=2.5, label="Target larva (LC50 ≈ 1)")
ax.plot(d, logistic(d, 3000, 1.5) * 100, color=GREEN, lw=2.5, label="Non-target predator (LC50 ≈ 3000)")
ax.plot(d, logistic(d, 8000, 1.2) * 100, color=BLUE, lw=2.5, label="Non-target Collembolan")
ax.axvline(0.05, color=GREY, ls="--", lw=1.2)
ax.text(0.055, 55, "max field-realistic\nexposure", fontsize=8.5, color=GREY)
ax.set_xscale("log"); ax.set_xlabel("Concentration (relative dose, log)")
ax.set_ylabel("Mortality (%)")
ax.set_title("Dose-response selectivity: orders-of-magnitude LC50 separation")
ax.legend(); ax.grid(alpha=0.3)
save(fig, "11-dose-response.png")

# ---------- 12 Monte Carlo uncertainty ----------
fig, ax = plt.subplots(figsize=(9, 5.5))
a = rng.uniform(0.02, 0.05, 10000); b = rng.uniform(0.10, 0.30, 10000)
S = rng.uniform(0.8, 1.2, 10000); O = rng.uniform(0.6, 1.0, 10000)
F = a * np.exp(-b * 12) * S * O * 100  # % at 12 m
ax.hist(F, bins=80, color=BLUE, alpha=0.75)
p5, p50, p95 = np.percentile(F, [5, 50, 95])
for v, lbl in [(p50, "median"), (p5, "5th"), (p95, "95th")]:
    ax.axvline(v, color=RED if lbl == "median" else GREY, ls="--" if lbl != "median" else "-", lw=1.6)
ax.axvline(0.1, color=GREEN, lw=2)
ax.text(0.102, ax.get_ylim()[1]*0.9, "management threshold", fontsize=9, color=GREEN)
ax.set_xlabel("Field-scale gene-flow estimate (%)"); ax.set_ylabel("Monte Carlo draws")
ax.set_title("Monte Carlo output: a distribution, not a point (simulated)")
save(fig, "12-monte-carlo.png")

# ---------- 13 Uncertainty types ----------
fig, ax = canvas(10, 5.5)
types = [("Measurement\nuncertainty", "instrument/precision", "better assays"),
         ("Model\nuncertainty", "wrong functional form", "model comparison"),
         ("Sampling\nuncertainty", "rare events missed", "more sampling/power"),
         ("Extrapolation\nuncertainty", "lab→field, species", "confirmatory field tiers"),
         ("Biological\nvariability", "site-year heterogeneity", "design coverage (NOT measurement)")]
for i, (t, d_, r) in enumerate(types):
    y = 5.0 - i * 0.95
    box(ax, 1.7, y, 2.6, 0.8, t, fc="#eff6ff", ec=BLUE, fs=9, weight="bold")
    ax.text(4.6, y, d_, fontsize=9, va="center")
    ax.text(7.6, y, "→ " + r, fontsize=9, va="center", color=GREEN)
ax.set_xlim(0, 10); ax.set_ylim(0.3, 5.6)
ax.text(5, 0.45, "Report intervals, not adjectives; separate variability from uncertainty",
        ha="center", fontsize=10, style="italic")
save(fig, "13-uncertainty-types.png")

# ---------- 14 Risk management cycle ----------
fig, ax = canvas(10, 6)
steps = ["Risk\ncharacterization", "Select\ninstrument", "Implement\n(refuges, buffers,\ncontainment)", "Monitor\ncompliance & effect",
         "Evaluate\nagainst triggers", "Adapt / enforce /\nre-assess"]
pos = [(1.5, 4.8), (3.8, 4.8), (6.3, 4.8), (8.5, 4.8), (8.5, 2.2), (6.0, 2.2)]
for t, (x, y) in zip(steps, pos):
    box(ax, x, y, 2.1, 1.1, t, fc="white", ec=GREEN, fs=8.5)
for i in range(3):
    arrow(ax, pos[i][0] + 1.1, pos[i][1], pos[i+1][0] - 1.1, pos[i+1][1])
arrow(ax, pos[3][0], pos[3][1] - 0.6, pos[4][0], pos[4][1] + 0.6)
arrow(ax, pos[4][0] - 1.1, pos[4][1], pos[5][0] + 1.1, pos[5][1])
arrow(ax, pos[5][0] - 0.2, pos[5][1] + 0.6, pos[0][0], pos[0][1] - 0.6)
ax.text(3.0, 2.2, "Assessment ≠ management:\nrelated but distinct processes", fontsize=9.5,
        color=ORANGE, ha="center")
save(fig, "14-risk-management-cycle.png")

# ---------- 15 Regulatory landscape ----------
fig, ax = canvas(10, 5.5)
juris = [("US\nCoordinated Framework", "product/use trigger\nUSDA · EPA · FDA", BLUE),
         ("EU\n2001/18 + 1829/2003", "process trigger\nPMEM · traceability · labelling", ORANGE),
         ("Canada\nNovel trait", "product-based\ntrait novelty trigger", GREEN),
         ("Cartagena Protocol", "transboundary LMOs\nAIA · Annex III", PURPLE := "#7c3aed"),
         ("Pakistan\nPEPA 1997 + Rules 2005", "NBC · TAC · IBC\ncase-by-case", RED)]
for i, (n, d_, c) in enumerate(juris):
    x = 1.2 + (i % 3) * 3.3
    y = 4.4 - (i // 3) * 2.0
    box(ax, x, y, 2.9, 1.5, n + "\n" + d_, fc="white", ec=c, fs=8)
ax.text(5, 0.9, "Same science largely - different decision rules and acceptable-risk thresholds",
        ha="center", fontsize=10, style="italic")
ax.text(5, 0.35, "Assessment characterizes - jurisdictions decide", ha="center", fontsize=9, color=GREY)
save(fig, "15-regulatory-landscape.png")

# ---------- 16 Persistence vs weediness vs invasiveness ----------
fig, ax = canvas(10, 5)
box(ax, 1.7, 3.8, 2.6, 1.1, "PERSISTENCE\npopulation maintains\nitself (volunteers)", fc="#eff6ff", ec=BLUE, fs=9)
box(ax, 5.0, 3.8, 2.6, 1.1, "WEEDINESS\npersistence + interference\nwith agriculture", fc="#fef3c7", ec=ORANGE, fs=9)
box(ax, 8.3, 3.8, 2.6, 1.1, "INVASIVENESS\nspread into natural\ncommunities + impact", fc="#fee2e2", ec=RED, fs=9)
arrow(ax, 3.0, 3.8, 3.7, 3.8); arrow(ax, 6.3, 3.8, 7.0, 3.8)
ax.text(5, 2.4, "A trait may affect one without the others - each needs distinct evidence", ha="center", fontsize=10, style="italic")
wfl = ["Trait\ncharacterization", "Phenotypic\ncomparison", "Environment\nconditions", "Reproductive\nfitness", "Persistence\npotential", "Ecological\nconsequence"]
for i, t in enumerate(wfl):
    box(ax, 1.1 + i * 1.56, 1.1, 1.6, 0.95, t, fc="white", ec=GREY, fs=7.5)
    if i < 5:
        arrow(ax, 1.1 + i * 1.56 + 0.85, 1.1, 1.1 + (i+1) * 1.56 - 0.85, 1.1, lw=1.2)
save(fig, "16-persistence-weediness-invasiveness.png")

# ---------- 17 Difference-vs-harm chain ----------
fig, ax = canvas(10, 3.6)
chain = ["Observed\ndifference", "Biological\nrelevance?", "Adverse\neffect?", "Exposure\npresent?", "RISK?"]
for i, t in enumerate(chain):
    c = RED if i == 4 else BLUE
    box(ax, 1.2 + i * 1.9, 2.3, 1.75, 1.2, t, fc="white", ec=c, fs=9.5,
        weight="bold" if i == 4 else "normal")
    if i < 4:
        arrow(ax, 1.2 + i * 1.9 + 0.9, 2.3, 1.2 + (i+1) * 1.9 - 0.9, 2.3)
ax.text(5, 0.8, "A difference is where analysis starts - never where it ends",
        ha="center", fontsize=11, style="italic")
save(fig, "17-difference-vs-harm.png")

# ---------- 18 Allergenicity weight of evidence ----------
fig, ax = canvas(10, 5.5)
lines = [("Source organism\nhistory", "known allergen source?"),
         ("Sequence homology", "vs known allergens (>35% over 80 aa flag)"),
         ("Pepsin resistance /\nstability", "digestibility - one line only"),
         ("Glycosylation", "novel glycan patterns"),
         ("Serum screening\n(where relevant)", "IgE binding if exposure history exists")]
for i, (t, d_) in enumerate(lines):
    y = 4.9 - i * 0.92
    box(ax, 2.0, y, 2.9, 0.8, t, fc="white", ec=ORANGE, fs=8.5, weight="bold")
    ax.text(5.6, y, d_, fontsize=8.5, va="center", color=GREY)
ax.text(5, 0.35, "No single test establishes allergenic safety - concordant lines, honest flags",
        ha="center", fontsize=10, style="italic", color=RED)
save(fig, "18-allergenicity-woe.png")

# ---------- 19 Communication do/don't ----------
fig, ax = canvas(10, 5)
box(ax, 2.6, 4.0, 4.2, 1.3, "POOR: 'GM pollen kills butterflies'\n(hazard fragment as risk conclusion;\nno exposure, no comparators)", fc="#fee2e2", ec=RED, fs=9.5)
box(ax, 7.4, 4.0, 4.4, 1.3, "GOOD: 'At field-edge pollen densities,\nlarval exposure stays far below effect\ndoses; dominant uncertainty is deposition.'", fc="#dcfce7", ec=GREEN, fs=9.5)
rules = ["hazard vs risk precision", "name the comparator", "give intervals",
         "admit unknowns", "no false reassurance", "no sensationalism"]
for i, r in enumerate(rules):
    ax.text(1.2 + (i % 3) * 2.7, 2.6 - (i // 3) * 0.75, "✓ " + r, fontsize=10, color=GREEN, ha="left")
ax.text(5, 0.75, "Communication is part of assessment - Module 21", ha="center", fontsize=9.5, color=GREY)
save(fig, "19-communication.png")

# ---------- 20 Course roadmap ----------
fig, ax = canvas(10, 5.5)
groups = [("Foundations\nM1-3", BLUE), ("GMO characterization\nM4-5", GREEN),
          ("Ecological hazards\nM6-10", ORANGE), ("Evolution & fate\nM11-13", RED),
          ("Food/feed & uncertainty\nM14-16", PURPLE := "#7c3aed"),
          ("Characterization &\nmanagement M17-20", BLUE),
          ("Communication,\nregulation, cases M21-23", GREEN),
          ("Data & frontiers\nM24-25", ORANGE)]
for i, (t, c) in enumerate(groups):
    x = 1.0 + (i % 4) * 2.45
    y = 4.3 - (i // 4) * 1.7
    box(ax, x, y, 2.2, 1.25, t, fc="white", ec=c, fs=8, weight="bold")
    if i % 4 < 3:
        arrow(ax, x + 1.15, y, x + 1.3, y, lw=1.4)
labs = "Labs 01-12: terminology → workflow → gene flow → non-target → resistance → exposure → composition → dose-response → matrix → uncertainty → regulatory role-play → capstone"
ax.text(5, 1.15, labs, ha="center", fontsize=8.5, color=GREY, wrap=True)
ax.text(5, 0.45, "Trait + Organism + Environment + Exposure + Evidence + Uncertainty",
        ha="center", fontsize=11, color=BLUE, weight="bold")
save(fig, "20-course-roadmap.png")

print("All diagrams generated.")
