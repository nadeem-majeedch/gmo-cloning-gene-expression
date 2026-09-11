#!/usr/bin/env python3
"""Companion-site generator for the GMO Environment and Risk Assessments course.

Extends the SAME MkDocs docs/ tree produced by the existing course's
tools/build_site.py (which delegates here at the end of build()) - one site,
two independent courses.

Adds into docs/:
  risk/index.md            course landing page
  risk/modules/*.md        25 modules (rewritten links, figure blocks, footers)
  risk/labs/*.md           12 labs + overview
  risk/assessment/*.md     question banks + answer key
  risk/guide/*.md          workbook / cheat sheet / FAQs
  risk/downloads/*.md      resources, datasets, diagram gallery
  risk/references.md, risk/capstone.md
  assets/risk/<dir>/       copies of DIAGRAMS/PDF/PPTX/DATA for downloads

Then merges the 'GMO Environment & Risk Assessments' tab into ../mkdocs.yml
(the existing generator owns the file; we edit it after it is written).

Run from the existing course root (GMO-Cloning-Gene-Expression-Course/):
    python ../GMO-Environment-and-Risk-Assessments/tools/build_site_risk.py
"""
import os, re, shutil, glob

THIS = os.path.dirname(os.path.abspath(__file__))                 # .../tools
RISK = os.path.abspath(os.path.join(THIS, os.pardir))             # .../GMO-Environment-and-Risk-Assessments
CLONE = os.path.dirname(RISK)                      # repo/course workspace root
COURSE = os.path.join(CLONE, "GMO-Cloning-Gene-Expression-Course")
DOCS = os.path.join(COURSE, "docs")

MD = os.path.join(RISK, "MARKDOWN")
LAB = os.path.join(RISK, "LAB")
CHAPTERS = sorted(f for f in os.listdir(MD) if f.endswith(".md"))
LABS = sorted(f for f in os.listdir(LAB) if f.endswith(".md"))
ASSESS = {
    "MCQs.md": "Multiple-choice questions",
    "Short-Questions.md": "Short-answer questions",
    "Long-Questions.md": "Long-answer questions",
    "Viva-Questions.md": "Viva questions",
    "Case-Based-Questions.md": "Case-based questions",
    "Data-Interpretation-Questions.md": "Data-interpretation questions",
    "Answer-Key.md": "Instructor answer key",
}
GUIDE = {
    "WORKBOOK/Practical-Workbook.md": ("workbook", "Practical workbook"),
    "CHEAT-SHEET/GMO-Environment-Risk-Assessments-Cheat-Sheet.md": ("cheat-sheet", "Cheat sheet"),
    "FAQ/GMO-Environment-Risk-Assessments-FAQs.md": ("faqs", "FAQs"),
}
ASSET_DIRS = ("DIAGRAMS", "PDF", "PPTX", "DATA")
BASE = "risk"

# Figure captions (doubles as alt text)
FIGS = {
    "01-hazard-vs-risk": "Hazard versus risk: exposure, dose-response and context convert a hazard into a characterized risk.",
    "02-era-framework": "The environmental risk-assessment framework from problem formulation to risk communication.",
    "03-gene-flow-decay": "Pollen-mediated gene flow decays with distance; buffer zones act on the steep segment of the curve.",
    "04-introgression-pathway": "The introgression pathway: every gate from sexual compatibility to trait persistence must pass.",
    "05-exposure-pathway": "An exposure pathway chain from Bt maize to predators, with transfer factors at each step.",
    "06-tiered-testing": "Tiered non-target testing: escalate only on concern at realistic exposure.",
    "07-resistance-scurve": "Resistance allele frequency follows a slow-then-explosive S-curve; refuges stretch the slow phase.",
    "08-monitoring-loop": "The adaptive monitoring loop: baseline, release, monitoring, evaluation, response.",
    "09-risk-matrix": "A qualitative risk matrix with pre-declared likelihood and consequence anchors.",
    "10-food-web": "Food-web routes by which trait effects propagate indirectly through communities.",
    "11-dose-response": "Logistic dose-response curves showing orders-of-magnitude selectivity between target and non-target species.",
    "12-monte-carlo": "Monte Carlo output is a distribution: median, interval and threshold exceedance, not a point.",
    "13-uncertainty-types": "Uncertainty types with their remedies; variability needs design coverage, not better instruments.",
    "14-risk-management-cycle": "The risk-management cycle: characterize, select instruments, implement, monitor, adapt.",
    "15-regulatory-landscape": "Regulatory approaches compared: product/use triggers, process triggers and the Cartagena framework.",
    "16-persistence-weediness-invasiveness": "Persistence, weediness and invasiveness are distinct concepts with distinct evidence bases.",
    "17-difference-vs-harm": "The interpretive chain from observed difference to characterized risk.",
    "18-allergenicity-woe": "The weight-of-evidence allergenicity assessment: no single test is decisive.",
    "19-communication": "Risk communication: poor vs good framing, with best-practice rules.",
    "20-course-roadmap": "The course roadmap across all 25 modules and 12 practicals.",
}
MODULE_FIGS = {
    "01": ["20-course-roadmap"], "02": ["01-hazard-vs-risk", "17-difference-vs-harm"],
    "03": ["02-era-framework"], "04": [], "05": [],
    "06": ["04-introgression-pathway", "03-gene-flow-decay"],
    "07": ["16-persistence-weediness-invasiveness"],
    "08": ["06-tiered-testing"], "09": [], "10": ["10-food-web"],
    "11": ["07-resistance-scurve"], "12": [], "13": ["05-exposure-pathway"],
    "14": [], "15": ["18-allergenicity-woe"], "16": ["13-uncertainty-types"],
    "17": ["09-risk-matrix"], "18": ["14-risk-management-cycle"],
    "19": ["08-monitoring-loop"], "20": [], "21": ["19-communication"],
    "22": ["15-regulatory-landscape"], "23": [], "24": ["12-monte-carlo"],
    "25": [],
}
LAB_FIGS = {"01": [], "02": ["02-era-framework"], "03": ["03-gene-flow-decay"],
            "04": ["06-tiered-testing"], "05": ["07-resistance-scurve"],
            "06": ["05-exposure-pathway"], "07": [], "08": ["11-dose-response"],
            "09": ["09-risk-matrix"], "10": ["12-monte-carlo"], "11": [], "12": ["20-course-roadmap"]}

# ------------------------------------------------------------------ utilities
def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()

def write(path, text):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full) or DOCS, exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("  wrote", path)

def title_of(path):
    for line in read(path).splitlines():
        if line.startswith("# "):
            return re.sub(r"^# (Module \d+|Lab \d+) \S+ ", "# ", line)[2:].strip()
    return os.path.basename(path)

def strip_nav(text):
    out, skipping = [], False
    emoji_line = re.compile(r"^> [\U0001F300-\U0001FAFF\u2753\u274C\u2705]")
    for line in text.splitlines():
        if line.startswith("> **Navigation:**"):
            skipping = True
            continue
        if skipping and emoji_line.match(line):
            continue
        skipping = False
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))

def risk_asset_url(dest_dir, sub):
    """File-relative URL from a docs page at risk/<dest_dir> to docs/assets/risk/<sub>.
    dest_dir 'risk' (depth 1) needs ../, 'risk/x' (depth 2) needs ../../."""
    depth = dest_dir.count("/") + 1
    depth = max(depth, 2)
    up = "../" * depth
    return f"{up}assets/risk/{sub}"

DIR_PAGE = {"DATA": "downloads/datasets.md", "DIAGRAMS": "downloads/diagrams.md",
            "LAB": "labs/index.md", "MARKDOWN": "index.md",
            "ASSESSMENT": "assessment/index.md", "CHEAT-SHEET": "guide/cheat-sheet.md",
            "FAQ": "guide/faqs.md", "WORKBOOK": "guide/workbook.md",
            "PDF": "downloads/index.md", "PPTX": "downloads/index.md"}

def _dir_link(dest_dir, page, anchor):
    """Relative URL for a dir-mapped page: DIR_PAGE paths are risk-relative."""
    depth = dest_dir.count("/")          # risk/ -> 0, risk/x/ -> 1
    up = "../" * depth
    return f"{up}{page}{anchor}"

def rewrite(text, dest_dir):
    """Rewrite links from the RISK course's repo-relative layout to site paths under risk/."""
    def repl(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("#", "http://", "https://", "mailto:")):
            return f"[{label}]({target})"
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if not target:
            return f"[{label}]({anchor})" if anchor else label
        t = target.replace("\\", "/")
        p = "../" if dest_dir == BASE else "../../"   # risk/ vs risk/<section>/
        if t.endswith("/"):
            segs = [s for s in t.rstrip("/").split("/") if s]
            base = segs[-1]
            if len(segs) >= 2 and segs[-2] == "DATA":
                return f"[{label}]({_dir_link(dest_dir, f'downloads/{base}.md', anchor)})"
            page = DIR_PAGE.get(base, "index.md")
            return f"[{label}]({_dir_link(dest_dir, page, anchor)})"
        if t.endswith(".md"):
            name = t.split("/")[-1]
            if name == "README.md":
                return f"[{label}]({p}{BASE}/index.md{anchor})"
            if re.match(r"^\d{2}-", name):
                return f"[{label}]({p}{BASE}/modules/{name}{anchor})"
            if name.startswith("Lab-"):
                return f"[{label}]({p}{BASE}/labs/{name}{anchor})"
            if name in ASSESS:
                return f"[{label}]({p}{BASE}/assessment/{name}{anchor})"
            if name == "REFERENCES.md":
                return f"[{label}]({p}{BASE}/references.md{anchor})"
            if name == "CAPSTONE.md":
                return f"[{label}]({p}{BASE}/capstone.md{anchor})"
            if name == "BUILD_REPORT.md":
                return f"[{label}]({p}{BASE}/index.md{anchor})"
            for rel_src, (slug, _t) in GUIDE.items():
                if name == os.path.basename(rel_src):
                    return f"[{label}]({p}{BASE}/guide/{slug}.md{anchor})"
            return f"[{label}]({anchor or '#'})"
        m = re.match(r"^(?:\.\./)*(DATA|DIAGRAMS|PDF|PPTX)/(.+)$", t)
        if m:
            return f"[{label}]({risk_asset_url(dest_dir, m.group(1) + '/' + m.group(2))}{anchor})"
        return f"[{label}]({anchor or '#'})"
    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", repl, text)

def figures_block(fig_keys, dest_dir):
    if not fig_keys:
        return ""
    lines = ["## Figures", ""]
    for key in fig_keys:
        cap = FIGS.get(key, key.replace("_", " "))
        lines += ["<figure markdown>",
                  f"![{cap}]({risk_asset_url(dest_dir, 'DIAGRAMS/' + key + '.png')})",
                  "",
                  f"*Figure - {cap}*",
                  "</figure>", ""]
    return "\n".join(lines) + "\n"

def module_footer(idx):
    prev_ch = CHAPTERS[idx - 1] if idx > 0 else None
    next_ch = CHAPTERS[idx + 1] if idx + 1 < len(CHAPTERS) else None
    lines = ["---", "",
             "## What you should know", "",
             "Review the learning objectives and quick-check questions above. Then continue the sequence.",
             "",
             "## What you should be able to do", "",
             "- Test yourself with the [multiple-choice questions](../assessment/MCQs.md) and the "
             "[short-answer](../assessment/Short-Questions.md) and [long-answer](../assessment/Long-Questions.md) banks.",
             "- Instructors: model answers are in the [answer key](../assessment/Answer-Key.md).",
             "- Quick revision: [cheat sheet](../guide/cheat-sheet.md) and [FAQs](../guide/faqs.md).",
             "- Hands-on practice: the [practical program overview](../labs/index.md).", ""]
    nav = []
    if prev_ch:
        nav.append(f"[<- {title_of(os.path.join(MD, prev_ch))}](../modules/{prev_ch})")
    nav.append("[Course home](../index.md)")
    if next_ch:
        nav.append(f"[Continue to next module ->](../modules/{next_ch})")
    return "\n".join(lines) + "\n" + " &middot; ".join(nav) + "\n"

def generic_footer(dest_dir, extra=""):
    up = "../index.md" if dest_dir == BASE else "../../index.md"
    lines = ["---", ""]
    if dest_dir.endswith("labs"):
        lines += ["**Related resources:** [Practical workbook](../guide/workbook.md) - "
                  "[Cheat sheet](../guide/cheat-sheet.md) - [Datasets](../downloads/datasets.md) - "
                  "[Assessments](../assessment/index.md)", ""]
    lines.append(f"[Course home]({up})")
    return "\n".join(lines) + extra + "\n"

def page_from(src, dest_dir, fig_keys=(), module_num=None, dest_name=None):
    text = strip_nav(read(src))
    text = rewrite(text, dest_dir)
    figs = figures_block(fig_keys, dest_dir)
    if figs:
        anchor_line = None
        for line in text.splitlines():
            if line.startswith("## ") and any(k in line.lower() for k in
                    ("self-check", "quick-check", "key points", "summary", "interpretation")):
                anchor_line = line[3:].strip()
                break
        if anchor_line:
            idx = text.index(anchor_line)
            head = text.rfind("## ", 0, idx)
            text = text[:head] + figs + "\n" + text[head:]
        else:
            text = text.rstrip() + "\n\n" + figs
    text = re.sub(r"\n-{3,}\s*$", "", text)
    if module_num:
        text += module_footer(CHAPTERS.index(os.path.basename(src)))
    else:
        text = text.rstrip() + "\n\n" + generic_footer(dest_dir)
    name = dest_name or os.path.basename(src)
    write(os.path.join(dest_dir, name) if dest_dir else name, text)

# ----------------------------------------------------------------------- build
def build():
    print("Risk-course site extension ->", DOCS)

    # assets
    for d in ASSET_DIRS:
        src = os.path.join(RISK, d)
        dst = os.path.join(DOCS, "assets", "risk", d)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints", "README.md"))
        print("  copied", d, "-> docs/assets/risk/" + d)

    # landing page
    cards = []
    for i, ch in enumerate(CHAPTERS):
        t = title_of(os.path.join(MD, ch))
        n_figs = len(MODULE_FIGS.get(ch[:2], []))
        cards.append(f'<a class="modcard" href="modules/{os.path.splitext(ch)[0]}/" title="{t}">'
                     f'**{ch[:2]} &middot; {t}**<br>'
                     f'<small>{n_figs} figure{"s" if n_figs != 1 else ""} - quick-check questions</small></a>')
    home = f"""---
title: GMO Environment and Risk Assessments
description: An evidence-based university course on the environmental risk assessment of genetically modified organisms.
---

<div class="hero" markdown>

# GMO Environment and Risk Assessments

### How science evaluates the environmental safety of GMOs - evidence, not advocacy

A complete course for BS/MS students in Molecular Biology, Biotechnology, Environmental Sciences,
Biosafety, Agriculture and Ecology: hazard identification, exposure assessment, risk characterization,
gene flow, non-target organisms, resistance evolution, food/feed safety, uncertainty, risk management,
monitoring, risk communication and regulatory frameworks - with 12 practicals, 10 datasets, a lecture
deck and a capstone.

[Start learning :material-arrow-right:](modules/{CHAPTERS[0]}){{ .md-button .md-button--primary }}
[Open the practical workbook :material-flask:](guide/workbook.md){{ .md-button }}
[Download the cheat sheet :material-download:](guide/cheat-sheet.md){{ .md-button }}
[Slides & PDFs :material-presentation:](downloads/index.md){{ .md-button }}

</div>

## Instructor

**Dr. Saira Azam** — Assistant Professor  
Centre of Excellence in Molecular Biology, University of the Punjab, Lahore

## How to use this site

<div class="grid cards" markdown>

- :material-map-marker-path: **Follow the arc** - GMO development to regulatory decision,
  across 25 modules that each end with quick-checks and a link to the next.
- :material-flask: **Do the practicals** - twelve exercises (simulation / computational / case-study)
  with instructor keys in the [practical workbook](guide/workbook.md).
- :material-database: **Analyze the data** - ten [datasets](downloads/datasets.md), all simulated,
  seeded and clearly labeled; `analysis_demo.py` reproduces every documented answer.
- :material-check-decagram: **Assess yourself** - [MCQs](assessment/MCQs.md), short/long questions,
  viva, case-based and data-interpretation banks with an instructor [answer key](assessment/Answer-Key.md).
- :material-school: **Finish with the capstone** - a complete conceptual ERA for a real GMO
  ([Lab 12](labs/Lab-12-Capstone-Environmental-Risk-Assessment.md)).

</div>

## Modules

<div class="grid cards" markdown>

{chr(10).join(cards)}

</div>

## Course at a glance

| Component | Where |
|---|---|
| 25 modules from terminology to research frontiers | Start with [Module 01](modules/{CHAPTERS[0]}) |
| 12 practicals with instructor keys | [Practical overview](labs/index.md) |
| 10 simulated datasets + worked analysis | [Datasets](downloads/datasets.md) |
| 89-slide lecture deck (PPTX) + five PDFs | [Downloads](downloads/index.md) |
| 67 FAQs + 4-page cheat sheet | [Guide](guide/cheat-sheet.md) |
| Assessment package + answer key | [Assessments](assessment/index.md) |
| Capstone: GMO Environmental Risk Assessment | [Capstone](capstone.md) |
| Authoritative references | [References](references.md) |

*Companion course: [GMO, Cloning Techniques & Developmental and Spatial Gene Expression](../index.md)*
"""
    write(f"{BASE}/index.md", home)

    # modules
    for i, ch in enumerate(CHAPTERS):
        page_from(os.path.join(MD, ch), f"{BASE}/modules", MODULE_FIGS.get(ch[:2], ()), module_num=i)

    # labs
    lab_index = ["---", "title: Practical program", "---", "", "# Practical program", "",
                 "Twelve practicals in five formats (simulation, computational, case study, "
                 "demonstration, capstone). No wet-lab GMO work anywhere in the program.", "",
                 "| Lab | Title |", "|---|---|"]
    for lb in LABS:
        lab_index.append(f"| {lb[4:6]} | [**{title_of(os.path.join(LAB, lb))}**]({lb}) |")
    lab_index += ["", "## Downloads", "",
                  f"- [Practical workbook (markdown)](../guide/workbook.md) and "
                  f"[PDF]({risk_asset_url('labs', 'PDF/Lab-Workbook.pdf')})",
                  f"- [All datasets](../downloads/datasets.md) - simulated, seeded, documented", ""]
    write(f"{BASE}/labs/index.md", "\n".join(lab_index))
    for lb in LABS:
        page_from(os.path.join(LAB, lb), f"{BASE}/labs", LAB_FIGS.get(lb[4:6], ()))

    # assessment
    a_idx = ["---", "title: Assessments", "---", "", "# Assessment package", "",
             "Question banks spanning recall to evaluation, all backed by an "
             "[instructor answer key](Answer-Key.md).", "",
             "| Section | Questions | File |", "|---|---|---|",
             "| Multiple-choice | 60 | [MCQs](MCQs.md) |",
             "| Short-answer | 30 | [Short questions](Short-Questions.md) |",
             "| Long-answer | 20 | [Long questions](Long-Questions.md) |",
             "| Viva | 40 | [Viva questions](Viva-Questions.md) |",
             "| Case-based | 15 | [Case-based](Case-Based-Questions.md) |",
             "| Data-interpretation | 15 | [Data interpretation](Data-Interpretation-Questions.md) |",
             "| Instructor key | all | [Answer key](Answer-Key.md) |", ""]
    write(f"{BASE}/assessment/index.md", "\n".join(a_idx))
    for f in ASSESS:
        page_from(os.path.join(RISK, "ASSESSMENT", f), f"{BASE}/assessment")

    # guide
    for rel_src, (slug, _t) in GUIDE.items():
        page_from(os.path.join(RISK, rel_src), f"{BASE}/guide", dest_name=slug + ".md")

    # downloads
    dl = ["---", "title: Resources & downloads", "---", "", "# Resources & downloads", "",
          "Every artifact of the risk course, straight from the repository.", "",
          "## Lecture slides", "",
          f"- :material-presentation: [GMO_Environment_Risk_Assessments.pptx]"
          f"({risk_asset_url('downloads', 'PPTX/GMO_Environment_Risk_Assessments.pptx')}) - "
          "89 slides with speaker notes (regenerate with `PPTX/build_pptx.py`).", "",
          "## Printable PDFs", ""]
    for pdf, desc in [("Complete-Tutorial.pdf", "all 25 modules + references"),
                      ("Lab-Workbook.pdf", "the 12-practical program with instructor keys"),
                      ("Cheat-Sheet.pdf", "4-page revision guide"),
                      ("FAQs.pdf", "67 questions and answers"),
                      ("Assessment.pdf", "full assessment package + answer key")]:
        dl.append(f"- :material-file-pdf-box: [{pdf}]({risk_asset_url('downloads', 'PDF/' + pdf)}) - {desc}")
    dl += ["", "## Data and diagrams", "",
           f"- [All datasets](datasets.md) with per-exercise pages",
           f"- [Diagram gallery](diagrams.md) - all 20 teaching figures", ""]
    write(f"{BASE}/downloads/index.md", "\n".join(dl))

    dsets = ["---", "title: Datasets", "---", "", "# Simulated datasets", "",
             "Ten exercises, all **simulated for teaching** and clearly labelled. Deterministic "
             "(seeded): regenerate with `DATA/generate_datasets.py`; verify answers with "
             f"`DATA/analysis_demo.py` ([script]({risk_asset_url('downloads', 'DATA/analysis_demo.py')})).", ""]
    for folder in sorted(os.listdir(os.path.join(RISK, "DATA"))):
        path = os.path.join(RISK, "DATA", folder)
        if not os.path.isdir(path):
            continue
        dsets += [f"## Exercise - {folder}", ""]
        files = sorted(os.listdir(path))
        for f in files:
            kb = os.path.getsize(os.path.join(path, f)) / 1024
            dsets.append(f"- [`{f}`]({risk_asset_url('downloads', 'DATA/' + folder + '/' + f)}) ({kb:.1f} KB)")
        dsets.append("")
        # per-exercise page (module data links target these)
        demo = risk_asset_url('downloads', 'DATA/analysis_demo.py')
        page = [f"---\ntitle: Dataset - {folder}\n---\n", "",
                f"# Dataset - {folder}", "",
                "**Simulated teaching data** - generated by `generate_datasets.py` "
                "(seeded, deterministic); documented answers reproducible via "
                f"[`analysis_demo.py`]({demo}).", ""]
        for f in sorted(os.listdir(os.path.join(RISK, "DATA", folder))):
            kb = os.path.getsize(os.path.join(RISK, "DATA", folder, f)) / 1024
            page.append(f"- [`{f}`]({risk_asset_url('downloads', 'DATA/' + folder + '/' + f)}) ({kb:.1f} KB)")
        page += ["", "Return to [all datasets](datasets.md).", ""]
        write(f"{BASE}/downloads/{folder}.md", "\n".join(page))
    write(f"{BASE}/downloads/datasets.md", "\n".join(dsets))

    dgr = ["---", "title: Diagram gallery", "---", "", "# Diagram gallery", "",
           "All 20 original teaching diagrams with captions (captions double as alt text).", ""]
    for key in sorted(FIGS):
        cap = FIGS[key]
        dgr += ["<figure markdown>",
                f"![{cap}]({risk_asset_url('downloads', 'DIAGRAMS/' + key + '.png')})",
                "",
                f"*{cap}*",
                "</figure>", ""]
    write(f"{BASE}/downloads/diagrams.md", "\n".join(dgr))

    # references + capstone (routed through page_from so links are rewritten)
    page_from(os.path.join(RISK, "REFERENCES.md"), BASE, dest_name="references.md")
    page_from(os.path.join(RISK, "CAPSTONE.md"), BASE, dest_name="capstone.md")

    # ------------------------------------------------ merge tab into mkdocs.yml
    mk_path = os.path.join(COURSE, "mkdocs.yml")
    mk = read(mk_path)
    chapter_nav = "\n".join(f'      - "{ch[:2]} - {title_of(os.path.join(MD, ch))}": risk/modules/{ch}'
                            for ch in CHAPTERS)
    lab_nav = "\n".join(f'      - "{title_of(os.path.join(LAB, lb))}": risk/labs/{lb}' for lb in LABS)
    assess_nav = "\n".join(f'      - "{t}": risk/assessment/{f}' for f, t in ASSESS.items())
    guide_nav = "\n".join(f'      - "{t}": risk/guide/{s}.md' for s, t in
                          [("workbook", "Practical workbook"), ("cheat-sheet", "Cheat sheet"), ("faqs", "FAQs")])
    risk_tab = f"""  - Risk Assessments:
      - "Course home": risk/index.md
      - "Capstone project": risk/capstone.md
{chapter_nav}
  - Risk Practicals:
      - "Overview": risk/labs/index.md
{lab_nav}
  - Risk Assessments Bank:
      - "Overview": risk/assessment/index.md
{assess_nav}
  - Risk Guide:
{guide_nav}
      - "Workbook (companion)": risk/guide/workbook.md
  - Risk Downloads:
      - "Resources & downloads": risk/downloads/index.md
      - "All datasets": risk/downloads/datasets.md
      - "Diagram gallery": risk/downloads/diagrams.md
      - "Dataset - composition": risk/downloads/composition.md
      - "Dataset - dose-response": risk/downloads/dose-response.md
      - "Dataset - exposure": risk/downloads/exposure.md
      - "Dataset - gene-flow": risk/downloads/gene-flow.md
      - "Dataset - non-target": risk/downloads/non-target.md
      - "Dataset - resistance": risk/downloads/resistance.md
      - "Dataset - risk-matrix": risk/downloads/risk-matrix.md
      - "Dataset - soil": risk/downloads/soil.md
      - "Dataset - uncertainty": risk/downloads/uncertainty.md
      - "References": risk/references.md
"""
    if "risk/index.md" not in mk:
        mk = mk.replace("  - References: references.md", risk_tab + "  - References: references.md")
        with open(mk_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(mk)
        print("  merged 'Risk Assessments' tabs into mkdocs.yml")
    else:
        print("  mkdocs.yml already contains the risk tabs")

    print("risk-course site extension done.")

if __name__ == "__main__":
    build()
