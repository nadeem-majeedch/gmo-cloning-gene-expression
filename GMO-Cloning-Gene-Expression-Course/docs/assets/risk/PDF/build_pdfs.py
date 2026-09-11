#!/usr/bin/env python3
"""Build the 5 course PDFs with reportlab (title page, TOC, page numbers,
tables, diagrams, consistent typography).
Usage: python PDF/build_pdfs.py
Requires: reportlab, matplotlib-generated DIAGRAMS.
"""
import os, re, glob
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Table, TableStyle, Image,
                                KeepTogether, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents
from xml.sax.saxutils import escape as xml_escape

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

INK = HexColor("#0f172a")
BLUE = HexColor("#1d4ed8")
ACCENT = HexColor("#b45108")
GRAY = HexColor("#475569")
LIGHT = HexColor("#eff6ff")

styles = getSampleStyleSheet()
def st(name, **kw):
    base = kw.pop("parent", styles["Normal"])
    if name not in styles:
        styles.add(ParagraphStyle(name, parent=base, **kw))
    return styles[name]

H1 = st("CH1", fontName="Helvetica-Bold", fontSize=17, leading=21,
        textColor=BLUE, spaceBefore=16, spaceAfter=8)
H2 = st("CH2", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
        textColor=INK, spaceBefore=13, spaceAfter=6)
H3 = st("CH3", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
        textColor=INK, spaceBefore=10, spaceAfter=4)
BODY = st("Body9", fontSize=9.8, leading=13.6, textColor=INK, spaceAfter=5)
SMALL = st("Small9", fontSize=8.6, leading=11.6, textColor=GRAY)
CODE = st("Code9", fontName="Courier", fontSize=8.0, leading=10.5,
          backColor=HexColor("#f1f5f9"), borderPadding=4, spaceAfter=6,
          textColor=INK, leftIndent=6)
BUL = st("Bul9", parent=BODY, leftIndent=12, bulletIndent=4, spaceAfter=3)
CAPTION = st("Cap9", fontSize=8.2, leading=10.5, textColor=GRAY,
             alignment=TA_CENTER, spaceBefore=2, spaceAfter=8)
TITLE = st("Title9", fontName="Helvetica-Bold", fontSize=26, leading=32,
           textColor=BLUE, alignment=TA_CENTER, spaceAfter=14)
SUBTITLE = st("Subtitle9", fontSize=13, leading=18, textColor=GRAY,
              alignment=TA_CENTER, spaceAfter=8)

def md_inline(t):
    """Markdown-inline -> reportlab markup via single-pass tokenizer
    (handles **bold**, *italic*, `code`, [links](url) without nesting bugs)."""
    token_re = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\*[^*\s][^*]*\*|\[[^\]]+\]\([^)]+\))")
    out, pos = [], 0
    for m in token_re.finditer(t):
        out.append(xml_escape(t[pos:m.start()]))
        tok = m.group(0)
        if tok.startswith("**"):
            out.append("<b>" + xml_escape(tok[2:-2]) + "</b>")
        elif tok.startswith("`"):
            out.append("<font face='Courier' size='8.6'>" +
                       xml_escape(tok[1:-1]) + "</font>")
        elif tok.startswith("["):
            label = re.sub(r"\[(.+)\]\(.+\)", r"\1", tok)
            out.append(xml_escape(label))
        else:  # *italic*
            out.append("<i>" + xml_escape(tok[1:-1]) + "</i>")
        pos = m.end()
    out.append(xml_escape(t[pos:]))
    return "".join(out)

def parse_md(path):
    """Parse a course markdown file into flowables."""
    flow = []
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    i = 0
    in_code = False
    code_buf = []
    table_buf = []

    def flush_table():
        nonlocal table_buf
        if not table_buf:
            return
        rows = []
        for ln in table_buf:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            rows.append(cells)
        table_buf = []
        if not rows:
            return
        ncol = max(len(r) for r in rows)
        data = [[Paragraph(md_inline(c), st("TH", fontName="Helvetica-Bold",
                 fontSize=8.2, leading=10.5, textColor=HexColor("#ffffff")))
                 for c in (r + [""] * (ncol - len(r)))] for r in rows]
        for ri in range(1, len(data)):
            data[ri] = [Paragraph(md_inline(c), st("TD", fontSize=8.2,
                        leading=10.5, textColor=INK)) for c in
                        (rows[ri] + [""] * (ncol - len(rows[ri])))]
        t = Table(data, colWidths=[(17.0 * cm) / ncol] * ncol, repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), BLUE),
            ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#cbd5e1")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [HexColor("#ffffff"), HexColor("#f8fafc")]),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        flow.append(t)
        flow.append(Spacer(1, 6))

    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            if in_code:
                flow.append(Paragraph("<br/>".join(
                    xml_escape(c) for c in code_buf) or "&nbsp;", CODE))
                code_buf = []
            in_code = not in_code
            i += 1; continue
        if in_code:
            code_buf.append(ln); i += 1; continue
        if ln.strip().startswith("|"):
            table_buf.append(ln); i += 1; continue
        elif table_buf:
            flush_table()
        s = ln.strip()
        if not s:
            i += 1; continue
        if s.startswith("### "):
            flow.append(Paragraph(md_inline(s[4:]), H3))
        elif s.startswith("## "):
            flow.append(Paragraph(md_inline(s[3:]), H2))
        elif s.startswith("# "):
            flow.append(Paragraph(md_inline(s[2:]), H1))
        elif s.startswith("> "):
            flow.append(Paragraph("<i>" + md_inline(s[2:]) + "</i>", SMALL))
        elif s.startswith("- ") or s.startswith("* "):
            flow.append(Paragraph("\u2022 " + md_inline(s[2:]), BUL))
        elif re.match(r"^\d+\.\s", s):
            num, rest = s.split(".", 1)
            flow.append(Paragraph(f"{num}. " + md_inline(rest), BUL))
        elif s.startswith("**") and s.endswith("**") and len(s) > 4:
            flow.append(Paragraph(md_inline(s), H3))
        elif s.startswith("---"):
            flow.append(HRFlowable(width="100%", thickness=0.5,
                                   color=HexColor("#cbd5e1"),
                                   spaceBefore=6, spaceAfter=6))
        else:
            flow.append(Paragraph(md_inline(s), BODY))
        i += 1
    if table_buf:
        flush_table()
    return flow

def add_figure(story, img_name, caption, width=13.5):
    p = os.path.join(ROOT, "DIAGRAMS", img_name)
    if os.path.exists(p):
        img = Image(p, width=width * cm, height=width * cm * 0.6,
                    kind="proportional")
        img.hAlign = "CENTER"
        story.append(KeepTogether([img, Paragraph(xml_escape(caption), CAPTION)]))

# ---------------------------------------------------------------- doc template
class CourseDoc(BaseDocTemplate):
    def __init__(self, path, title, toc=True, **kw):
        super().__init__(path, pagesize=A4, leftMargin=2.0 * cm,
                         rightMargin=2.0 * cm, topMargin=2.0 * cm,
                         bottomMargin=1.9 * cm, title=title, **kw)
        self.doc_title = title
        self.show_toc = toc
        frame = Frame(self.leftMargin, self.bottomMargin, self.width,
                      self.height, id="main")
        self.addPageTemplates([PageTemplate(id="page", frames=[frame],
                                            onPage=self.deco)])
        self.h1s = []
        self.toc_entries = []

    def deco(self, canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7.6)
        canv.setFillColor(GRAY)
        canv.drawString(2.0 * cm, A4[1] - 1.25 * cm, self.doc_title)
        canv.drawRightString(A4[0] - 2.0 * cm, 1.15 * cm, f"Page {doc.page}")
        canv.setStrokeColor(HexColor("#cbd5e1"))
        canv.setLineWidth(0.4)
        canv.line(2.0 * cm, A4[1] - 1.45 * cm, A4[0] - 2.0 * cm, A4[1] - 1.45 * cm)
        canv.line(2.0 * cm, 1.4 * cm, A4[0] - 2.0 * cm, 1.4 * cm)
        canv.restoreState()

    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph):
            stn = fl.style.name
            if stn == "CH1":
                text = fl.getPlainText()
                key = f"h1-{len(self.h1s)}"
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text[:80], key, level=0, closed=False)
                self.notify("TOCEntry", (0, text, self.page))
            elif stn == "CH2":
                text = fl.getPlainText()
                key = f"h2-{self.page}-{abs(hash(text)) % 99999}"
                self.canv.bookmarkPage(key)
                self.notify("TOCEntry", (1, text, self.page))

def title_block(doc_title, subtitle,
                author="Instructor: Dr. Saira Azam - Assistant Professor, Centre of Excellence in "
                       "Molecular Biology, University of the Punjab, Lahore"):
    return [
        Spacer(1, 3.2 * cm),
        Paragraph(xml_escape(doc_title), TITLE),
        Paragraph(xml_escape(subtitle), SUBTITLE),
        Spacer(1, 0.6 * cm),
        Paragraph(xml_escape(author), SUBTITLE),
        Spacer(1, 0.8 * cm),
        HRFlowable(width="40%", thickness=1, color=ACCENT, hAlign="CENTER"),
        Spacer(1, 1.4 * cm),
        Paragraph("All datasets used in this package are simulated teaching data, "
                  "clearly labelled as such. This course involves no wet-lab work with "
                  "living GMOs; case studies and regulatory summaries reflect published "
                  "evidence and should be verified against current primary sources.",
                  st("Disc", fontSize=9, leading=13, textColor=GRAY,
                     alignment=TA_CENTER)),
        PageBreak(),
    ]

def toc_block():
    toc = TableOfContents()
    toc.levelStyles = [
        st("TOC1", fontName="Helvetica-Bold", fontSize=10.5, leading=15,
           textColor=BLUE, leftIndent=2),
        st("TOC2", fontSize=9.5, leading=13, textColor=INK, leftIndent=14),
    ]
    return [Paragraph("Table of Contents", H1), toc, PageBreak()]

# ================================================================ build PDFs
os.makedirs(BASE, exist_ok=True)

# ---- 1. Complete tutorial (all 25 modules + references) --------------------
doc = CourseDoc(os.path.join(BASE, "Complete-Tutorial.pdf"),
                "GMO Environment and Risk Assessments - Complete Tutorial")
story = []
story += title_block(
    "GMO Environment and Risk Assessments - a complete university course on the "
    "environmental risk assessment of genetically modified organisms",
    "Evidence-based and objective - for BS/MS Molecular Biology, Biotechnology, "
    "Environmental Sciences, Biosafety, Agriculture and Ecology")
story += toc_block()
mods = sorted(glob.glob(os.path.join(ROOT, "MARKDOWN", "*.md")))
for m in mods:
    story += parse_md(m)
    story.append(PageBreak())
story.append(Paragraph("References", H1))
story += parse_md(os.path.join(ROOT, "REFERENCES.md"))
doc.build(story)
print("Complete-Tutorial.pdf")

# ---- 2. Lab workbook -------------------------------------------------------
doc = CourseDoc(os.path.join(BASE, "Lab-Workbook.pdf"),
                "Practical Workbook - GMO Environment and Risk Assessments")
story = []
story += title_block(
    "The complete practical program: 12 labs covering terminology, workflow, "
    "gene flow, non-target analysis, resistance simulation, exposure, composition, "
    "dose-response, risk matrices, uncertainty, regulatory role-play and the capstone",
    "Simulation, computational and case-study formats - no wet-lab GMO work; "
    "instructor keys included")
story += toc_block()
for m in sorted(glob.glob(os.path.join(ROOT, "LAB", "*.md"))):
    story += parse_md(m)
    story.append(PageBreak())
story += parse_md(os.path.join(ROOT, "WORKBOOK", "Practical-Workbook.md"))
doc.build(story)
print("Lab-Workbook.pdf")

# ---- 3. Cheat sheet --------------------------------------------------------
doc = CourseDoc(os.path.join(BASE, "Cheat-Sheet.pdf"),
                "Cheat Sheet - GMO Environment and Risk Assessments")
story = []
story += title_block("Revision guide: terminology, hazard vs risk, frameworks, "
                     "workflows, exam points and common misconceptions", "Revision aid")
story += parse_md(os.path.join(ROOT, "CHEAT-SHEET",
                "GMO-Environment-Risk-Assessments-Cheat-Sheet.md"))
add_figure(story, "02-era-framework.png",
           "The risk-assessment framework (revision figure).", width=11)
add_figure(story, "01-hazard-vs-risk.png",
           "Hazard vs risk: exposure makes the difference (revision figure).", width=11)
add_figure(story, "09-risk-matrix.png",
           "Risk matrix with pre-declared anchors (revision figure).", width=11)
doc.build(story)
print("Cheat-Sheet.pdf")

# ---- 4. FAQs ---------------------------------------------------------------
doc = CourseDoc(os.path.join(BASE, "FAQs.pdf"),
                "FAQs - GMO Environment and Risk Assessments")
story = []
story += title_block("67 frequently asked questions across 12 categories, "
                     "with concise, scientifically accurate answers",
                     "FAQ compendium")
story += toc_block()
story += parse_md(os.path.join(ROOT, "FAQ",
                "GMO-Environment-Risk-Assessments-FAQs.md"))
doc.build(story)
print("FAQs.pdf")

# ---- 5. Assessment ---------------------------------------------------------
doc = CourseDoc(os.path.join(BASE, "Assessment.pdf"),
                "Assessment Package - GMO Environment and Risk Assessments")
story = []
story += title_block("60 MCQs, 30 short, 20 long, 40 viva, 15 case-based, "
                     "15 data-interpretation questions - with the full instructor "
                     "answer key and rubrics",
                     "Instructor assessment package")
story += toc_block()
for f in ["MCQs.md", "Short-Questions.md", "Long-Questions.md",
          "Viva-Questions.md", "Case-Based-Questions.md",
          "Data-Interpretation-Questions.md", "Answer-Key.md"]:
    story += parse_md(os.path.join(ROOT, "ASSESSMENT", f))
    story.append(PageBreak())
doc.build(story)
print("Assessment.pdf")
