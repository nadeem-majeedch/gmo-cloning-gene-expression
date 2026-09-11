#!/usr/bin/env python3
"""Build GMO_Environment_Risk_Assessments.pptx (lecture deck, ~100 slides).
Usage:  python PPTX/build_pptx.py
Requires python-pptx. Content summarized from the course modules; diagrams from DIAGRAMS/.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
DIAGRAMS = os.path.join(ROOT, "DIAGRAMS")

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

INK = RGBColor(0x0F, 0x17, 0x2A)
BLUE = RGBColor(0x1D, 0x4E, 0xD8)
ACCENT = RGBColor(0xB4, 0x51, 0x08)
GRAY = RGBColor(0x47, 0x55, 0x69)
LIGHT = RGBColor(0xEF, 0xF6, 0xFF)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]
slide_count = [0]

def add_slide(title, bullets, notes=None, diagram=None, takeaway=None, section=False):
    slide = prs.slides.add_slide(BLANK)
    slide_count[0] += 1
    tbox = slide.shapes.add_textbox(Inches(0.5), Inches(0.28), SLIDE_W - Inches(1.0), Inches(0.9))
    tf = tbox.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run(); r.text = title
    r.font.size = Pt(30 if not section else 40); r.font.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if section else BLUE
    if section:
        bg = slide.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
        bg.fill.solid(); bg.fill.fore_color.rgb = BLUE
        bg.line.fill.background(); bg.shadow.inherit = False
        slide.shapes._spTree.remove(bg._element)
        slide.shapes._spTree.insert(2, bg._element)
        tbox.left = Inches(1.0); tbox.top = Inches(2.6)
        for para in tf.paragraphs:
            para.alignment = PP_ALIGN.LEFT
        sub = tf.add_paragraph(); sr = sub.add_run()
        sr.text = notes or ""
        sr.font.size = Pt(18); sr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        return slide
    rule = slide.shapes.add_shape(1, Inches(0.5), Inches(1.12), Inches(2.2), Pt(3))
    rule.fill.solid(); rule.fill.fore_color.rgb = ACCENT
    rule.line.fill.background(); rule.shadow.inherit = False
    btop = Inches(1.35)
    bwidth = Inches(6.6) if diagram else Inches(12.3)
    bbox = slide.shapes.add_textbox(Inches(0.55), btop, bwidth, SLIDE_H - btop - Inches(0.8))
    btf = bbox.text_frame; btf.word_wrap = True
    first = True
    for b in bullets:
        sub = b.startswith("  - ")
        p = btf.paragraphs[0] if first else btf.add_paragraph()
        first = False
        r = p.add_run()
        r.text = ("\u2022 " if not sub else "\u2013 ") + (b[4:] if sub else b)
        r.font.size = Pt(15 if not sub else 13.5)
        r.font.color.rgb = INK if not sub else GRAY
        p.space_after = Pt(7)
    if takeaway:
        strip = slide.shapes.add_shape(1, Inches(0.55), SLIDE_H - Inches(0.72),
                                       SLIDE_W - Inches(1.1), Inches(0.5))
        strip.fill.solid(); strip.fill.fore_color.rgb = LIGHT
        strip.line.color.rgb = BLUE; strip.line.width = Pt(1)
        strip.shadow.inherit = False
        stf = strip.text_frame; stf.word_wrap = True
        sp = stf.paragraphs[0]; sr = sp.add_run()
        sr.text = "Key takeaway: " + takeaway
        sr.font.size = Pt(12.5); sr.font.bold = True; sr.font.color.rgb = BLUE
    if diagram:
        path = os.path.join(DIAGRAMS, diagram)
        if os.path.exists(path):
            left = Inches(7.35); top = Inches(1.5)
            width = SLIDE_W - left - Inches(0.5)
            slide.shapes.add_picture(path, left, top, width=width)
    if notes and not section:
        slide.notes_slide.notes_text_frame.text = notes
    return slide

def title_slide():
    s = prs.slides.add_slide(BLANK)
    slide_count[0] += 1
    bg = s.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid(); bg.fill.fore_color.rgb = BLUE; bg.line.fill.background()
    bg.shadow.inherit = False
    tb = s.shapes.add_textbox(Inches(0.9), Inches(2.0), SLIDE_W - Inches(1.8), Inches(3.2))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run()
    r.text = "GMO Environment and Risk Assessments"
    r.font.size = Pt(44); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2 = tf.add_paragraph(); r2 = p2.add_run()
    r2.text = "An evidence-based university course on the environmental risk assessment of genetically modified organisms"
    r2.font.size = Pt(18); r2.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)
    p3 = tf.add_paragraph(); r3 = p3.add_run()
    r3.text = "Evidence, not advocacy - for BS/MS molecular biology, biotechnology, environmental science, agriculture & biosafety"
    r3.font.size = Pt(14); r3.font.italic = True; r3.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p4 = tf.add_paragraph(); r4 = p4.add_run()
    r4.text = "Instructor: Dr. Saira Azam \u00b7 Assistant Professor \u00b7 Centre of Excellence in Molecular Biology \u00b7 University of the Punjab, Lahore"
    r4.font.size = Pt(14); r4.font.bold = True; r4.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

def section_slide(title, subtitle):
    slide_count[0] += 1
    s = prs.slides.add_slide(BLANK)
    bg = s.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid(); bg.fill.fore_color.rgb = BLUE; bg.line.fill.background()
    bg.shadow.inherit = False
    tb = s.shapes.add_textbox(Inches(1.0), Inches(2.6), SLIDE_W - Inches(2), Inches(2))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run()
    r.text = title; r.font.size = Pt(40); r.font.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2 = tf.add_paragraph(); r2 = p2.add_run()
    r2.text = subtitle; r2.font.size = Pt(18)
    r2.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)

def closing_slide():
    s = prs.slides.add_slide(BLANK)
    slide_count[0] += 1
    bg = s.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid(); bg.fill.fore_color.rgb = BLUE; bg.line.fill.background()
    bg.shadow.inherit = False
    tb = s.shapes.add_textbox(Inches(0.9), Inches(2.2), SLIDE_W - Inches(1.8), Inches(3))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run()
    r.text = "Trait + Organism + Environment + Exposure + Evidence + Uncertainty"
    r.font.size = Pt(28); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2 = tf.add_paragraph(); r2 = p2.add_run()
    r2.text = "The course motto - evaluate every GMO as its own case; advocate nothing, hide nothing."
    r2.font.size = Pt(16); r2.font.italic = True; r2.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)
    p3 = tf.add_paragraph(); r3 = p3.add_run()
    r3.text = "Dr. Saira Azam \u00b7 CEMB \u00b7 University of the Punjab, Lahore - Thank you."
    r3.font.size = Pt(14); r3.font.bold = True; r3.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

# ================= 1. Introduction =================
title_slide()
section_slide("1 \u00b7 Introduction", "Modules 1-2 - why assess, and the hazard/risk distinction")
add_slide("Why assess GMO environmental risk?",
          ["Traits, organisms and receiving environments differ - no blanket judgments",
           "Assessment quantifies: what could go wrong, how likely, how serious, how certain",
           "Informs regulation - but is not itself the decision",
           "Course motto: Trait + Organism + Environment + Exposure + Evidence + Uncertainty"],
          notes="Open by contrasting a Bt crop, a vitamin-biofortified crop and a GM microorganism: same word 'GMO', entirely different assessment questions.",
          takeaway="Case-by-case is not a slogan - it is the epistemology of the field.")
add_slide("The teaching journey",
          ["Foundations (M1-3): terminology, hazard vs risk, the framework",
           "Characterization (M4-5): molecular and phenotypic/compositional",
           "Ecological hazards (M6-10): gene flow, persistence, non-targets, soil, webs",
           "Evolution & fate (M11-13): resistance, herbicide systems, exposure",
           "Food/feed & uncertainty (M14-16); characterization & management (M17-20)",
           "Communication, regulation, cases, data, frontiers (M21-25)"],
          diagram="20-course-roadmap.png",
          notes="Emphasize that labs 01-12 shadow the modules; the capstone synthesizes everything.")
add_slide("Hazard vs risk - the distinction everything rests on",
          ["Hazard: inherent potential to cause harm (agent-mechanism-endpoint)",
           "Exposure: contact between hazard and receptor - magnitude x duration",
           "Risk: hazard + exposure + dose-response + context (conceptual, not one formula)",
           "Cobra behind thick glass: a hazard at near-zero risk"],
          diagram="01-hazard-vs-risk.png",
          notes="Drill the three-part hazard statement: agent, mechanism, endpoint. Anything less is not assessable.",
          takeaway="Hazard without exposure is not risk - the monarch case will prove this empirically.")

# ================= 2. Risk fundamentals =================
section_slide("2 \u00b7 Risk fundamentals", "Framework stages and their inputs, outputs, limits")
add_slide("The ERA framework - memorize the spine",
          ["Problem formulation \u2192 hazard identification \u2192 hazard characterization",
           "\u2192 exposure assessment \u2192 risk characterization \u2192 uncertainty analysis",
           "\u2192 risk management \u2192 monitoring \u2192 risk communication",
           "Cartagena Annex III principles: case-by-case, science-based, step-wise"],
          diagram="02-era-framework.png",
          notes="For every stage know: inputs, questions, data, methods, outputs, limitations, example.",
          takeaway="Problem formulation defines what 'relevant' means - everything downstream inherits it.")
add_slide("Problem formulation",
          ["Define protection goals and assessment endpoints",
           "Specify the receiving environment (species, climate, practices)",
           "List plausible hazard pathways and analysis plan",
           "Output: a scoping document that bounds the entire assessment"],
          notes="Weak problem formulation is the most common root cause of contested assessments.",
          takeaway="Scope determines which evidence counts - set it before data collection.")
add_slide("Hazard identification vs characterization",
          ["Identification: agent-mechanism-endpoint statements, from construct biology",
           "Characterization: dose-response, tiers, severity/survival parameters",
           "Methods: forced-dose lab, semi-field, field - escalation criteria matter",
           "Every hazard statement must be falsifiable"],
          takeaway="If no data could refute it, it is advocacy - not a hazard statement.")
add_slide("Exposure assessment",
          ["Pathway mapping: source \u2192 transfer \u2192 attenuation \u2192 receptor",
           "Magnitude and duration at each step; biology vs management controls",
           "Outputs: receptor doses with uncertainty intervals",
           "Typical finding: orders-of-magnitude attenuation along the chain"],
          diagram="05-exposure-pathway.png",
          notes="Walk the five-box chain; each arrow is a transfer factor students compute in Lab 06.",
          takeaway="Exposure is where most 'scary hazard' stories die - and where management intervenes.")
add_slide("Risk characterization & uncertainty",
          ["Integrate hazard + exposure + dose-response + ecological context",
           "Qualitative (matrix) and quantitative (Monte Carlo) modes",
           "Uncertainty types: measurement, model, sampling, extrapolation, variability",
           "Output: risk statement WITH intervals - never bare adjectives"],
          diagram="12-monte-carlo.png",
          notes="Preview the Monte Carlo figure: a distribution, not a point. Lab 10 builds exactly this.",
          takeaway="'Safe' and 'unsafe' are not assessment outputs - characterized risk statements are.")

add_slide("Three different jobs",
          ["Assessment: characterize risk and uncertainty - science-led",
           "Management: accept, mitigate, contain, monitor - policy-laden",
           "Communication: exchange information with stakeholders",
           "Conflating them corrupts all three"],
          notes="Use the salmon example: assessors characterize escapement; managers choose containment; communicators explain triple-barrier facilities - three different products.",
          takeaway="Keep the jobs separate and each becomes defensible; merge them and all three become contestable.")
add_slide("Exposure has three dimensions",
          ["Magnitude: concentration at the receptor",
           "Duration: how long contact persists (seasons? decades?)",
           "Frequency: how often across the landscape",
           "Different hazards are dominated by different dimensions"],
          notes="Pollen exposure: high-magnitude, short-duration. Soil protein: low-magnitude, long-duration. Gene flow: rare, potentially irreversible. Each demands different data.",
          takeaway="Name which dimension drives your hazard before choosing study designs.")
add_slide("Uncertainty is communicated, not hidden",
          ["Intervals over adjectives - quantify, then speak",
           "Name the dominant driver and what would narrow the interval",
           "Precaution is a policy response to uncertainty - not a substitute for data",
           "False certainty is the most expensive communication error"],
          takeaway="An honest 'unknown' with a measurement plan beats a confident guess every time.")

# ================= 3. GMO characterization =================
section_slide("3 \u00b7 GMO characterization", "Modules 4-5 - molecular and comparative biology")
add_slide("Molecular characterization for ERA",
          ["Construct and insert: copy number, site, integrity, stability",
           "Expression profile: where, when, how much protein",
           "Protein identity and mode of action",
           "Genome-edited organisms: intended edit + potential off-targets"],
          notes="Links directly to hazard identification: what is expressed, where, how much determines exposure biology.",
          takeaway="Molecular data turn 'a GMO' into a specific, assessable object.")
add_slide("Phenotypic and compositional comparison",
          ["Near-isogenic comparator + commercial reference ranges",
           "Proximates, key nutrients, anti-nutrients, toxicants",
           "Intended differences separated from unintended flags",
           "Equivalence margins pre-declared - TOST, not bare t-tests"],
          notes="Preview Lab 07: one analyte among 50 will 'differ' by chance alone - multiplicity discipline.",
          takeaway="Substantial equivalence is a starting framework, not a verdict - teach its limits.")

add_slide("Biology sets the gene-flow baseline",
          ["Mating system: selfing (soybean) vs outcrossing (maize, OSR)",
           "Pollen: size, viability window, vector (wind/insect)",
           "Wild relatives: presence, compatibility, phenology overlap",
           "OECD biology consensus documents: the standard baseline source"],
          notes="Crop identity dominates: same trait, different crop = entirely different gene-flow assessment.",
          takeaway="Read the biology dossier first - the assessment inherits its facts.")
add_slide("Coexistence: crop-to-crop gene flow",
          ["Seed-purity thresholds drive isolation distances",
           "Volunteers and seed banks extend the problem across seasons",
           "Machinery hygiene and harvest sequencing",
           "A management/coexistence question - not automatically ecological harm"],
          takeaway="Crop-to-crop flow is quantified and managed routinely - treat it as logistics, not catastrophe.")
add_slide("Gene flow in the local context",
          ["Map compatible relatives before siting trials or releases",
           "Local flowering calendars decide overlap windows",
           "Sentinel plants quantify realized flow",
           "Verify local wild-relative status from national biodiversity sources"],
          notes="Encourage students to build local flowering-calendar overlays - it converts an abstract hazard into a testable seasonal window.",
          takeaway="Local ecology turns generic gene-flow theory into a specific, measurable exposure.")

# ================= 4. Gene flow =================
section_slide("4 \u00b7 Gene flow", "Module 6 - the most quantified ecological hazard")
add_slide("Gene flow: routes and gates",
          ["Pollen (distance-decaying), seed (machinery, spillage), volunteers",
           "Crop-to-crop = coexistence/seed-purity issue",
           "Crop-to-wild = ecological issue - requires ALL introgression gates",
           "Compatibility, overlap, hybrid fertility, backcross persistence"],
          diagram="04-introgression-pathway.png",
          notes="Each gate is a filter; introgression needs all of them - that is why it is often rare.",
          takeaway="Crop identity determines the route: oilseed rape vs soybean are different worlds.")
add_slide("Quantifying gene flow",
          ["f(d) = a\u00b7exp(-b\u00b7d): edge frequency and decay constant",
           "Threshold logic: d* = ln(a/threshold)/b",
           "Buffer zones act on the steep segment - the tail never reaches zero",
           "Report point-estimate AND upper-confidence distances"],
          diagram="03-gene-flow-decay.png",
          notes="Lab 03 walks the fit; the management sentence students must produce is threshold-based.",
          takeaway="'Acceptable frequency' is a management judgment informed by the curve - not a detection limit.")
add_slide("Managing gene flow",
          ["Isolation distances and border rows (dilution)",
           "Flowering-time management (synchrony gates the whole pathway)",
           "Machinery hygiene and harvest sequencing (seed route)",
           "Monitoring sentinels where wild relatives persist"],
          takeaway="Every instrument maps to a specific pathway step - name the step.")

# ================= 5. Persistence =================
section_slide("5 \u00b7 Persistence, weediness, invasiveness", "Module 7 - demography of escaped traits")
add_slide("Three different concepts",
          ["Persistence: population maintains itself (volunteers, seed bank)",
           "Weediness: persistence + interference with agriculture",
           "Invasiveness: spread into natural communities + ecological impact",
           "A trait may affect one without the others"],
          diagram="16-persistence-weediness-invasiveness.png",
          notes="HT volunteers are typically a management problem, not an invasiveness problem - keep categories clean.",
          takeaway="Evidence differs per concept: seed-bank data vs control-cost data vs community-spread data.")
add_slide("Assessment workflow for persistence",
          ["Trait characterization \u2192 phenotypic comparison vs conventional",
           "Environmental conditions \u2192 reproductive fitness components",
           "Persistence potential \u2192 ecological consequence",
           "Conclude only at the level of evidence gathered"],
          takeaway="Fitness is measured in components (survival, fecundity, dormancy) - not asserted.")
add_slide("Volunteer dynamics",
          ["Seed shed at harvest \u2192 dormancy \u2192 multi-season emergence",
           "Seed banks: oilseed rape volunteers persist for years",
           "Management: stale seedbeds, rotations, selective chemistry",
           "Trait-carrying volunteers narrow options - the practical risk"],
          takeaway="Volunteer risk is measured in seed-bank halves and control windows - both measurable.")
add_slide("Invasiveness: the highest bar",
          ["Requires spread BEYOND habitats of origin + ecological impact",
           "Most GM crops lack the trait portfolio for wildland invasiveness",
           "Domestication baggage: dependency on managed environments",
           "Assess per trait: stress tolerance shifts the question"],
          notes="Drought-tolerance traits deserve sharper invasiveness scrutiny in water-limited landscapes - trait-specific, not generic.",
          takeaway="Invasiveness is not the default assumption - it is a claim requiring its own evidence.")

# ================= 6. Non-target organisms =================
section_slide("6 \u00b7 Non-target organisms", "Module 8 - tiered testing and the monarch lesson")
add_slide("Non-target assessment",
          ["Groups: pollinators, predators, parasitoids, soil fauna, aquatic insects",
           "Routes: direct (pollen/tissue), tritrophic (via prey), residue",
           "Tiered testing: lab max-dose \u2192 semi-field \u2192 field",
           "Escalation only on concern at REALISTIC exposure"],
          diagram="06-tiered-testing.png",
          notes="Tier 1 is a hazard screen; tiers 2-3 are where risk lives. Lab 04 trains the analysis.",
          takeaway="The escalation criterion - realistic exposure - is the entire logic of the pyramid.")
add_slide("The monarch butterfly case",
          ["1999: lab note - Bt pollen harms monarch larvae (hazard)",
           "Multi-group response: pollen densities, per-event toxicity, phenology",
           "Landscape exposure far below effect doses \u2192 negligible risk",
           "Communication lesson: hazard headlines outrun exposure data"],
          notes="Perfect for discussing how one laboratory result became a global narrative before exposure analysis existed.",
          takeaway="A hazard finding is the start of assessment, never its end.")
add_slide("Comparators decide non-target conclusions",
          ["Compare against the regime REPLACED (sprayed conventional)",
           "Unsprayed isolines inflate apparent Bt harm",
           "Bt vs sprayed regimes usually favors Bt for natural enemies",
           "Always state the comparator explicitly"],
          notes="This is the most common analytical bias in public literature - Lab 04 quantifies it.",
          takeaway="No comparator, no conclusion.")
add_slide("Design pitfalls in non-target studies",
          ["Pseudoreplication: cages vs fields as the replicate",
           "Dose without route: forced feeding vs natural exposure",
           "Single life-stage testing - mismatch with field phenology",
           "Power: many published studies cannot detect 20% effects"],
          notes="These four pitfalls explain most contradictions between published non-target studies - students can now read that literature critically.",
          takeaway="Study design, not toxin chemistry, explains most literature conflicts.")
add_slide("Pollinator assessment specifics",
          ["Adults: pollen/nectar route, foraging ranges, hive-level effects",
           "Larvae: pollen-provisioned brood - a different window",
           "Semi-field tunnel studies bridge lab and landscape",
           "Colony-level endpoints beat single-bee mortality"],
          takeaway="Match life stage to exposure route - adult feeding tests cannot see brood effects.")

# ================= 7. Soil and ecosystems =================
section_slide("7 \u00b7 Soil, biodiversity, food webs", "Modules 9-10 - community-level assessment")
add_slide("Soil ecosystems",
          ["Exposure: exudates, residues, DNA/protein persistence",
           "Methods: community profiling, functional assays, decomposition",
           "Findings: generally small/transient - but study-dependent",
           "Interpretation: difference \u2192 relevance \u2192 adverse? chain"],
          notes="Natural spatial/temporal variability dominates soil noise; multi-season designs are essential.",
          takeaway="Soil conclusions are the most over-claimed in both directions - discipline required.")
add_slide("Biodiversity and food webs",
          ["Direct vs indirect (trophic) effects; buffering and amplification",
           "UK Farm-Scale Evaluations: herbicide REGIME, not trait alone",
           "Different HT systems produced opposite community outcomes",
           "Assess management systems - not traits in isolation"],
          diagram="10-food-web.png",
          notes="The weed-seed \u2192 bird pathway makes indirect effects tangible for students.",
          takeaway="Trait-only thinking misses the actual exposure pathway: the regime.")
add_slide("Ecosystem services as assessment endpoints",
          ["Pollination, biological control, nutrient cycling, soil fertility",
           "Services link community ecology to societal protection goals",
           "Trait effects priced in service terms are policy-relevant",
           "Endpoint choice declared in problem formulation"],
          notes="Bridging slide: ecosystem-service framing makes the Module 3 protection-goal language concrete.",
          takeaway="Services convert 'biodiversity' from a slogan into measurable endpoints.")

# ================= 8. Resistance =================
section_slide("8 \u00b7 Resistance evolution", "Modules 11-12 - the dominant realized risk")
add_slide("Resistance genetics",
          ["Constant selection from season-long toxin expression",
           "Rare-recessive dynamics: slow-then-explosive S-curve",
           "High-dose/refuge: susceptible alleles dilute resistance when rare",
           "Refuges must produce in-space/in-time susceptible mating"],
          diagram="07-resistance-scurve.png",
          notes="Lab 05 builds this recursion; the refuge effect is dramatic and compliance-dependent.",
          takeaway="Refuges work only while resistance is RARE - which is why monitoring is load-bearing.")
add_slide("Resistance management in practice",
          ["Pyramids/stacks: multiple toxins, distinct receptors, no cross-resistance",
           "Monitoring: diagnostic-dose bioassays, damage reports, F2 screens",
           "Pre-agreed trigger thresholds \u2192 defined responses",
           "Binding constraint is grower compliance, not laboratory science"],
          notes="Bt cotton: resistance risk is manageable with effective refuges - the constraint is enforcement.",
          takeaway="The strategy's weakest link is behavioral - build instruments accordingly.")
add_slide("Herbicide-resistant weeds - the system-level risk",
          ["Selection comes from the herbicide REGIME, not the trait molecule",
           "Repeated glyphosate selected resistant weed biotypes across the Americas",
           "Responses: rotations, mixtures, integrated weed management",
           "Trait-enabled practice \u2192 system-level consequence"],
          notes="Avoid the 'superweeds' shorthand - the accurate statement is selection under the management system.",
          takeaway="Assess the agronomic system the trait enables - that is where selection lives.")
add_slide("Resistance monitoring in practice",
          ["Diagnostic-dose bioassays: survivors above the discriminating dose",
           "F2 screens detect rare alleles conventional bioassays miss",
           "Unexpected-damage reports: the free early-warning system",
           "Data feed pre-agreed triggers - not annual reports that nobody reads"],
          notes="Pink bollworm case: monitoring with pre-agreed triggers enabled region-scale eradication programs.",
          takeaway="Monitoring design determines whether resistance is managed or merely documented.")

# ================= 9. Environmental fate =================
section_slide("9 \u00b7 Environmental fate & exposure", "Module 13 - what happens after release")
add_slide("Environmental fate",
          ["Release pathways: pollen, residue, exudates, debris, water",
           "Degradation (half-lives), transport, persistence",
           "Protein fate in soil; DNA persistence debates",
           "Fate parameters feed exposure assessment directly"],
          diagram="11-dose-response.png",
          notes="Link to the dose-response figure: fate determines realized exposure against LC50s.",
          takeaway="Fate + pathway + dose-response = the quantitative tripod of environmental risk.")
add_slide("Quantitative exposure logic",
          ["Chain: C_source x transfer factors x attenuation",
           "Hazard quotient = receptor dose / effect threshold",
           "HQ << 1 under worst-case assumptions \u2192 pathway negligible",
           "HQ near 1 \u2192 measure the dominant parameter better"],
          notes="Lab 06 computes the full chain; worst-case framing is a screening device, not a field estimate.",
          takeaway="An HQ near 1 flags what to measure - not necessarily a risk.")
add_slide("Exposure scenarios: central vs conservative",
          ["Central estimate: best-estimate parameters - the likely case",
           "Conservative: plausible-worst-case - the screening basis",
           "Worst-case: physically possible - rarely informative alone",
           "State which scenario every number belongs to"],
          notes="Mixing scenario types is a classic dossier defect - one table mixing central and worst-case values is unreadable.",
          takeaway="Scenario discipline is communication discipline - label everything.")

# ================= 10. Food/feed safety =================
section_slide("10 \u00b7 Food & feed safety", "Modules 14-15 - composition, toxicity, allergenicity")
add_slide("Food/feed safety assessment",
          ["Compositional comparison: analytes vs comparator + reference ranges",
           "New protein: identity, mode of action, acute toxicity, digestibility",
           "Feed performance: target-animal studies where warranted",
           "Intended differences separated; unintended flags followed up"],
          notes="Codex principles structure this worldwide; Lab 07 trains the table-reading.",
          takeaway="Composition is one evidence line - necessary, never sufficient alone.")
add_slide("Allergenicity - weight of evidence",
          ["Source-organism history; sequence homology to known allergens",
           "Pepsin resistance/stability - one line among several",
           "Glycosylation; serum screening where exposure history exists",
           "NO single test establishes allergenic safety"],
          diagram="18-allergenicity-woe.png",
          notes="StarLink: unresolved allergenicity + feed-only approval + commingling = regulatory failure case.",
          takeaway="Concordant lines support safety; any flag demands targeted follow-up.")
add_slide("Toxicity assessment",
          ["Hazard identification: mode of action first",
           "Acute oral studies; margins of exposure vs realistic intake",
           "Chronic considerations handled via composition + protein biology",
           "Do not invent toxicity values - cite and scope honestly"],
          takeaway="MOE ratios >> 1 with stated uncertainty - that is the professional output.")
add_slide("Animal feeding studies - role and limits",
          ["Target-animal performance: feed-efficiency endpoint",
           "90-day rodent studies: where warranted by molecular/compositional flags",
           "Sensitivity limits acknowledged in the literature - interpret honestly",
           "They complement - never replace - composition and protein work"],
          notes="The debate over feeding-study sensitivity is itself teachable: what power do these designs actually have for what endpoints?",
          takeaway="Feeding studies are one line of evidence with known limits - position them accordingly.")

# ================= 11. Unintended effects & uncertainty =================
section_slide("11 \u00b7 Unintended effects & uncertainty", "Modules 16 - interpretation discipline")
add_slide("Unintended effects",
          ["Mechanisms: position effects, pleiotropy, insertional variation",
           "Detection via molecular + phenotypic + compositional screening",
           "Difference \u2260 automatically harm - run the chain",
           "Environmental interaction can reveal latent phenotypes"],
          diagram="17-difference-vs-harm.png",
          notes="The chain: difference \u2192 relevance \u2192 adverse? \u2192 exposure? \u2192 risk? - course interpretive core.",
          takeaway="A difference is where analysis starts - never where it ends.")
add_slide("Uncertainty - taxonomy and treatment",
          ["Measurement, model, sampling, extrapolation, biological variability",
           "Quantify: CIs, Monte Carlo, model comparison",
           "Separate variability (design) from uncertainty (measurement)",
           "Sensitivity ranking \u2192 what to measure next"],
          diagram="13-uncertainty-types.png",
          notes="Lab 10 converts 'we are uncertain' into a measurement campaign - the practical payoff.",
          takeaway="Uncertainty is quantified and carried - never hidden, never used as an excuse to stop deciding.")
add_slide("The uncertainty matrix",
          ["Rows: key parameters; columns: type, impact, trend, response",
           "Impact = effect on the risk statement, not on the parameter",
           "Trend: more data will narrow / will not narrow this",
           "Response: measure better, manage conservatively, or accept and monitor"],
          diagram="13-uncertainty-types.png",
          notes="The matrix is the regulatory-summary format for Module 16 - students produce one in Lab 10.",
          takeaway="An uncertainty matrix converts hedging into a decision table.")

# ================= 12. Risk characterization =================
section_slide("12 \u00b7 Risk characterization & management", "Modules 17-18 - integration into decisions")
add_slide("Risk characterization",
          ["Integrate: hazard + exposure + dose-response + context + uncertainty",
           "Qualitative: matrices with PRE-DECLARED anchors",
           "Quantitative: distributions, exceedance probabilities",
           "Statement format: estimate + interval + driver + response options"],
          diagram="09-risk-matrix.png",
          notes="Lab 09: placements cite evidence; cross-group divergence traces to anchors, not logic.",
          takeaway="The matrix is presentation; the assessment is the reasoning behind each placement.")
add_slide("Risk management instruments",
          ["Avoidance/containment (exposure engineered away - GM salmon logic)",
           "Mitigation: refuges, rotations, mixtures, buffer zones",
           "Stewardship programs with compliance enforcement",
           "Every characterized risk needs an instrument and an owner"],
          diagram="14-risk-management-cycle.png",
          notes="Assessment and management are related but distinct - Lab 11 role-play enforces the boundary.",
          takeaway="A top-ranked risk without an instrument is an unmanaged risk - say so in the report.")
add_slide("Instruments matched to characterized risks",
          ["Resistance \u2192 refuges + monitoring triggers + stewardship",
           "Gene flow \u2192 isolation, borders, timing, hygiene",
           "Volunteers \u2192 rotation design, alternative chemistry",
           "Unanticipated effects \u2192 PMEM with response owners"],
          notes="The mapping table is the core of Module 18; students reproduce it for their capstone GMO.",
          takeaway="Match instrument to mechanism - generic conditions are compliance theater.")

# ================= 13. Monitoring =================
section_slide("13 \u00b7 Monitoring", "Modules 19-20 - adaptive management in practice")
add_slide("Environmental monitoring",
          ["Baseline data pre-release - the non-negotiable",
           "Indicators: resistance frequencies, gene-flow sentinels, non-targets",
           "Pre-agreed trigger thresholds with named response owners",
           "Adaptive management: monitor \u2192 evaluate \u2192 adjust"],
          diagram="08-monitoring-loop.png",
          notes="Pink bollworm case: monitoring with triggers enabled eradication - monitoring as active management.",
          takeaway="Monitoring without triggers is decoration; with triggers it is control.")
add_slide("Baselines: the non-negotiable",
          ["Pre-release reference data across representative sites and seasons",
           "Power matched to the trigger thresholds agreed later",
           "Without baselines, monitoring cannot attribute change",
           "The weakest link of post-market systems worldwide"],
          notes="Ask students: what would you sample for two years before a Bt chickpea release in Punjab? Indicators become concrete instantly.",
          takeaway="Monitoring design is decided BEFORE release - retrofitting baselines is impossible.")
add_slide("Post-market environmental monitoring (PMEM)",
          ["Case-specific monitoring: ERA-identified hazards",
           "General surveillance: broad, unanticipated-effect watch",
           "Reporting obligations; time-limited authorizations in some systems",
           "Weak link worldwide: maintained long-term baselines"],
          takeaway="Detecting slow change needs decades of baselines - the honest global gap.")

# ================= 14. Communication =================
section_slide("14 \u00b7 Risk communication", "Module 21 - the discipline of honest framing")
add_slide("Communicating risk",
          ["Hazard vs risk precision in every statement",
           "Name comparators; give intervals; admit unknowns",
           "Avoid sensationalism AND false reassurance - both are advocacy",
           "Stakeholder input informs decisions - not hazard tables"],
          diagram="19-communication.png",
          notes="Drill the poor vs good example pairs; students write their own for their capstone GMO.",
          takeaway="Communication is part of assessment - treat it with the same rigor as the statistics.")
add_slide("Communicating probabilities",
          ["Natural frequencies beat percentages for lay audiences",
           "Exceedance statements: 'threshold crossed in 5% of scenarios'",
           "Visualize the distribution - not just a line",
           "Test comprehension: communication that is not understood did not occur"],
          takeaway="A probability the audience cannot repeat back is not communicated.")

# ================= 15. Regulation =================
section_slide("15 \u00b7 Regulatory frameworks", "Module 22 - assessment vs decision")
add_slide("The regulatory landscape",
          ["Cartagena Protocol: transboundary LMOs, AIA, Annex III principles",
           "Codex: food-safety assessment principles; comparator; WoE allergenicity",
           "OECD: biology consensus documents; familiarity concept",
           "EFSA assesses; Commission and member states decide"],
          diagram="15-regulatory-landscape.png",
          notes="US product/use trigger vs EU process trigger vs Canada novel trait - same science, different rules.",
          takeaway="Assessment characterizes - jurisdictions decide; the boundary is the profession's core discipline.")
add_slide("Pakistan's framework",
          ["PEPA 1997 + Pakistan Biosafety Rules 2005",
           "NBC (approvals) \u00b7 TAC (technical review) \u00b7 IBCs (institutional oversight)",
           "Bt cotton approved; other cases case-by-case (verify current notifications)",
           "Cartagena Party since 2009"],
          notes="Direct students to current NBC notifications - rules and approval lists update periodically.",
          takeaway="National frameworks implement international principles - capacity and enforcement are the live questions.")
add_slide("The assessment/decision boundary in one slide",
          ["Assessment outputs: hazard list, characterized risks, uncertainty flags",
           "Decision inputs: those outputs + thresholds, values, alternatives",
           "Same assessment, different decisions across jurisdictions - legitimately",
           "Violations run both directions: assessors must not decide; regulators must not edit hazard tables"],
          notes="This slide is the course's regulatory thesis - Lab 11 role-play tests whether students can hold the boundary in real time.",
          takeaway="Guard the boundary: it is what makes both roles defensible.")

# ================= 16. Case studies =================
section_slide("16 \u00b7 Case studies", "Module 23 - fifteen documented trajectories")
add_slide("Case-study spectrum",
          ["Bt cotton (resistance dominant) \u00b7 Monarch (exposure decisive)",
           "HT crops (system-level change) \u00b7 OSR gene flow (low frequency \u2260 no consequence)",
           "StarLink (segregation failure) \u00b7 Golden Rice (benefit \u2260 safety argument)",
           "Papaya (low exposure) \u00b7 GMMs (reversibility) \u00b7 Salmon (containment)"],
          notes="Outcomes genuinely differ - because traits, organisms, environments and management differ.",
          takeaway="Fifteen cases, fifteen different risk profiles - the anti-lottery lesson.")
add_slide("Three cases that teach the boundary",
          ["Monarch: hazard headline \u2192 exposure quantification \u2192 negligible risk",
           "StarLink: feed-only approval failed on commingling - traceability is real",
           "Bt brinjal: same evidence, different national decisions - science vs policy"],
          notes="Use these three for the assessment/decision discussion; students defend positions from the evidence only.",
          takeaway="Controversy often encodes value differences - identify them explicitly.")
add_slide("Three more cases that teach method",
          ["UK FSE: measure the regime - community effects followed management, not molecules",
           "Pink bollworm: monitoring with triggers enabled eradication",
           "GM salmon: containment substituted for hazard characterization",
           "Method lessons transfer to every future GMO"],
          takeaway="Cases are method teachers - each one upgrades a specific assessment skill.")

# ================= 17. Quantitative =================
section_slide("17 \u00b7 Quantitative analysis", "Module 24 + Labs 03-10 - the working toolkit")
add_slide("The ten-dataset toolkit",
          ["Gene-flow decay & thresholds \u00b7 Non-target survival (Wilson CIs)",
           "Resistance recursion with refuges \u00b7 Weed-resistance counts",
           "Soil communities \u00b7 Composition (TOST) \u00b7 Exposure chains (HQ)",
           "Dose-response (LC50, MOE) \u00b7 Risk matrices \u00b7 Monte Carlo + sensitivity"],
          notes="All datasets simulated and labeled; analysis_demo.py reproduces every documented answer.",
          takeaway="Five certifiable skills: proportions, decay, recursion, dose-response, uncertainty propagation.")
add_slide("Reading numbers like an assessor",
          ["Effect size + interval + comparator - never a bare p-value",
           "'Not detected' \u2260 'absent' - state detection limits",
           "Multiplicity: 1-in-20 analytes differ by chance at \u03b1=0.05",
           "Sensitivity analysis converts uncertainty into measurement priorities"],
          notes="These four disciplines separate professional from amateur readings of identical data.",
          takeaway="Precision comes from design and n - not from decimal places.")
add_slide("From data to dossier language",
          ["Statistics \u2192 characterization sentence \u2192 uncertainty flag \u2192 instrument",
           "Every table feeds a paragraph; every paragraph feeds a decision element",
           "Orphan numbers (no interpretation) are defects, not depth",
           "Practice: convert Lab 03 output into dossier prose"],
          notes="A short exercise with outsized professional value - most scientists can compute, few can convert computation into assessable prose.",
          takeaway="The deliverable is not the analysis - it is the characterized, actionable sentence.")

# ================= 18. Advanced =================
section_slide("18 \u00b7 Advanced topics", "Module 25 - research frontiers")
add_slide("Frontier topics and their maturity",
          ["Population genetics & landscape gene-flow modeling",
           "Bayesian/probabilistic ERA; multi-criteria decision analysis",
           "Stacked traits; gene-edited organisms (NGTs)",
           "Synthetic biology releases; gene drives (conceptual - no releases approved)"],
          notes="Flag maturity explicitly: model-to-data ratio rises with topic novelty.",
          takeaway="Gene drives break introgression-rate assumptions - reversibility becomes the controlling question.")
add_slide("Probabilistic and Bayesian ERA",
          ["Monte Carlo propagation: risk distributions, not points",
           "Bayesian hierarchical models: pooling sparse field data",
           "Expert elicitation: formalized, disclosed, sensitivity-tested priors",
           "Separate variability from uncertainty in every output"],
          notes="Conceptual level only - students should recognize the vocabulary and demand disclosure of priors.",
          takeaway="Bayesian methods quantify uncertainty - they do not eliminate it; priors must be disclosed.")
add_slide("Climate interactions and long-term monitoring",
          ["Shifting pest ranges change selection landscapes",
           "Flowering-time shifts alter gene-flow windows",
           "Drought modifies trait expression and exposure",
           "Treat as scenario inputs - not computable predictions"],
          takeaway="Frontier topics demand uncertainty disclosure as a professional ethic.")

# ================= 19. Review =================
section_slide("19 \u00b7 Review & assessment", "Capstone and exam preparation")
add_slide("The capstone ERA",
          ["Choose a real GMO + specified receiving environment",
           "Full workflow: problem formulation \u2192 characterization \u2192 management \u2192 monitoring",
           "\u22654 quantitative elements from the course toolkit",
           "Defense: 15-minute presentation + viva from the question bank"],
          notes="Lab 12 template and rubric; conclusion must be falsifiable - what monitoring would change it?",
          takeaway="There is no single correct conclusion - there are correct disciplines.")
add_slide("Exam-critical distinctions",
          ["Hazard \u2260 risk \u00b7 assessment \u2260 decision \u00b7 difference \u2260 harm",
           "'Not detected' \u2260 'absent' \u00b7 approved \u2260 zero risk \u00b7 banned \u2260 proven harmful",
           "Comparator choice changes conclusions",
           "Every risk statement: evidence + uncertainty + instrument + trigger"],
          takeaway="If you can defend these four lines with cases, you have learned the course.")
add_slide("Assessment package",
          ["60 MCQs (Bloom's-graded) \u00b7 30 short \u00b7 20 long \u00b7 40 viva",
           "15 case-based \u00b7 15 data-interpretation questions",
           "Instructor answer key with rubrics",
           "67 FAQs + 4-page cheat sheet for revision"],
          takeaway="Assessment mirrors the course: structured reasoning, not recall alone.")
closing_slide()

out = os.path.join(BASE, "GMO_Environment_Risk_Assessments.pptx")
prs.save(out)
print(f"Saved {out} with {slide_count[0]} slides.")
