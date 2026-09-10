#!/usr/bin/env python3
"""Build GMO_Cloning_Gene_Expression.pptx (lecture deck, 100+ slides).
Usage:  python PPTX/build_pptx.py
Requires python-pptx. All content summarized from the course modules.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
DIAGRAMS = os.path.join(ROOT, "DIAGRAMS")

# 16:9
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

INK = RGBColor(0x0F, 0x17, 0x2A)
BLUE = RGBColor(0x1D, 0x4E, 0xD8)
ACCENT = RGBColor(0xB9, 0x1C, 0x1C)
GRAY = RGBColor(0x47, 0x55, 0x69)
LIGHT = RGBColor(0xEF, 0xF6, 0xFF)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]

slide_count = [0]

def add_slide(title, bullets, notes=None, diagram=None, takeaway=None, section=False):
    """bullets: list of strings; sub-bullets prefixed with '  - '"""
    slide = prs.slides.add_slide(BLANK)
    slide_count[0] += 1

    # title bar
    tbox = slide.shapes.add_textbox(Inches(0.5), Inches(0.28), SLIDE_W - Inches(1.0), Inches(0.9))
    tf = tbox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = title
    r.font.size = Pt(30 if not section else 40); r.font.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if section else BLUE
    if section:
        bg = slide.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
        bg.fill.solid(); bg.fill.fore_color.rgb = BLUE
        bg.line.fill.background()
        bg.shadow.inherit = False
        # move bg behind title
        slide.shapes._spTree.remove(bg._element)
        slide.shapes._spTree.insert(2, bg._element)
        tbox.left = Inches(1.0); tbox.top = Inches(2.6)
        for para in tf.paragraphs:
            para.alignment = PP_ALIGN.LEFT
        sub = tf.add_paragraph(); sr = sub.add_run()
        sr.text = notes or ""
        sr.font.size = Pt(18); sr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        return slide

    # accent rule
    rule = slide.shapes.add_shape(1, Inches(0.5), Inches(1.12), Inches(2.2), Pt(3))
    rule.fill.solid(); rule.fill.fore_color.rgb = ACCENT
    rule.line.fill.background(); rule.shadow.inherit = False

    # bullets
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
        r.text = ("• " if not sub else "– ") + (b[4:] if sub else b)
        r.font.size = Pt(15 if not sub else 13.5)
        r.font.color.rgb = INK if not sub else GRAY
        p.space_after = Pt(7)
    # takeaway strip
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
    # diagram
    if diagram:
        path = os.path.join(DIAGRAMS, diagram)
        if os.path.exists(path):
            left = Inches(7.35)
            top = Inches(1.5)
            width = SLIDE_W - left - Inches(0.5)
            slide.shapes.add_picture(path, left, top, width=width)
    # notes
    if notes and not section:
        slide.notes_slide.notes_text_frame.text = notes
    return slide

def title_slide():
    s = prs.slides.add_slide(BLANK)
    slide_count[0] += 1
    bg = s.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid(); bg.fill.fore_color.rgb = BLUE; bg.line.fill.background()
    bg.shadow.inherit = False
    tb = s.shapes.add_textbox(Inches(0.9), Inches(2.1), SLIDE_W - Inches(1.8), Inches(3))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run()
    r.text = "GMOs, Cloning Techniques & Developmental and Spatial Gene Expression"
    r.font.size = Pt(40); r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2 = tf.add_paragraph(); r2 = p2.add_run()
    r2.text = "A university teaching module for BS/MS molecular biology, biotechnology, genetics & bioinformatics"
    r2.font.size = Pt(18); r2.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)
    p3 = tf.add_paragraph(); r3 = p3.add_run()
    r3.text = "Theory → Mechanism → Workflow → Data → Lab → Case studies → Assessment"
    r3.font.size = Pt(14); r3.font.italic = True; r3.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p4 = tf.add_paragraph(); r4 = p4.add_run()
    r4.text = "Instructor: Dr. Saira Azam · Assistant Professor · Centre of Excellence in Molecular Biology · University of the Punjab, Lahore"
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

# =====================================================================
title_slide()

# ------------------------------------------------ 1. INTRODUCTION
section_slide("1 · Introduction to Genetic Engineering", "From classical genetics to spatial genomics (Module 1)")
add_slide("What is genetic engineering?",
    ["Direct, deliberate modification of genetic material using laboratory techniques",
     "Recombinant DNA technology: join DNA from >1 source → propagate in a host",
     "Molecular cloning = building the blueprint; expression engineering = making it work",
     "Sits inside biotechnology, alongside classical uses and analytical omics"],
    notes="Emphasize precision of intent: the change is designed before the experiment. "
          "The 1973 Cohen–Boyer experiment is the canonical demonstration of cut → join → propagate → select.",
    takeaway="Genetic engineering = designed molecular change + a way to propagate or deliver it.")
add_slide("The vocabulary — use it precisely",
    ["GMO — umbrella term; the definition is REGULATORY and varies by country",
     "Transgenic — foreign (cross-species) DNA · Cisgenic — same-species DNA",
     "Gene-edited — change made by a targeted editor; may add no foreign DNA",
     "Stable (inherited) vs transient (fades over hours–days)",
     "The reagent can be transient while the consequence (edit) is stable"],
    notes="Students routinely conflate these. Give the Bt-corn and base-edited crop examples: "
          "same scientific descriptors, different regulatory labels in different jurisdictions.",
    takeaway="Scientific descriptors are unambiguous; regulatory labels are not.")
add_slide("Why modify organisms?",
    ["Research: assign function, build models, visualize biology (most GM work worldwide)",
     "Medicine: recombinant insulin (1982 — first rDNA drug), gene/cell therapy, mRNA vaccines",
     "Agriculture: Bt crops, virus-resistant papaya, Golden Rice, gene-edited crops",
     "Industry: enzymes, bio-based materials, engineered biosensors"],
    notes="Stress that basic research dominates the volume of genetic engineering; "
          "products are the visible minority.",
    takeaway="Every engineered organism answers a question — research, product, or both.")
add_slide("Historical milestones I — foundations",
    ["1865–1900s: Mendel → chromosome theory",
     "1928–1944: Griffith's transforming principle → Avery: DNA is the genetic material",
     "1953: double helix (Watson, Crick, Franklin, Wilkins)",
     "1968–70: restriction enzymes (Arber, Smith, Nathans; EcoRI purification) — Nobel 1978",
     "1972–73: Berg's first in-vitro rDNA; Cohen–Boyer functional recombinant plasmids"],
    diagram=None,
    notes="The arc is: inheritance becomes chemistry, chemistry becomes cuttable, "
          "cuttable DNA becomes clonable.",
    takeaway="Each era supplied the tool the next era needed.")
add_slide("Historical milestones II — the modern era",
    ["1975: Asilomar — scientists self-regulate; origin of biosafety frameworks",
     "1977–82: Sanger sequencing; recombinant insulin approved (Humulin, 1982)",
     "1981–83: transgenic mice; Agrobacterium plant transformation; PCR (Mullis)",
     "1994: GFP as a genetically encoded reporter (Chalfie) — Nobel 2008",
     "2012–13: CRISPR–Cas9 editing (Jinek; Cong/Mali/Zhang) — Nobel 2020",
     "2009–2026: single-cell then spatial transcriptomics — expression read in place"],
    notes="Two revolutions to keep separate: rDNA (1970s–90s, ADD DNA anywhere) vs "
          "genome editing (2010s–, CHANGE DNA at a chosen address).",
    takeaway="Read → copy → add → edit → watch: each capability built on the last.")

# ------------------------------------------------ 2. CLONING FUNDAMENTALS
section_slide("2 · Molecular Cloning Fundamentals", "Parts, plasmids and the eleven-stage workflow (Modules 2–3)")
add_slide("Anatomy of a cloning project",
    ["Insert — the DNA you want · Vector — the vehicle · Backbone — vector minus insert",
     "Every vector component has a job; every job can fail"],
    diagram="plasmid_map.png",
    notes="Walk the map: ori, marker, MCS, promoter cassette. Ask students what breaks "
          "when each is missing.",
    takeaway="A vector is not 'a circle with a hole' — it is a machine with parts.")
add_slide("Vector components and failure modes",
    ["ori → copy number (high pUC-class ~500; low pSC101 ~5; BAC single-copy)",
     "Selectable marker → without it you cannot recover transformants",
     "MCS / assembly architecture → where DNA enters",
     "Promoter + RBS/Kozak + terminator → expression or silence",
     "Reporter / tags → visibility and purification"],
    notes="High-copy for yield; low-copy for burden-sensitive inserts. "
          "Ask: which component would you change to reduce toxicity of expression?",
    takeaway="Design-stage attention to each component saves weeks at the bench.")
add_slide("The eleven-stage cloning workflow",
    ["Identify target → design construct → obtain/amplify DNA → prepare vector",
     "Assemble insert+vector → introduce into host → select → screen",
     "Validate (digest) → sequence-confirm → USE the construct"],
    diagram="cloning_workflow.png",
    notes="Module 2 details purpose/inputs/outputs/errors/validation for each stage — "
          "this slide is the map of the territory.",
    takeaway="Design decisions cascade; sequencing is the last gate before use.")
add_slide("Copy number, capacity, host range",
    ["High copy: more DNA per prep; more burden on unstable/toxic inserts",
     "Low copy: gentler, better for large or unstable DNA",
     "Plasmids 1–15 kb · BACs 100–300 kb (F-factor, single-copy, stable) · YACs up to ~1 Mb",
     "Shuttle vectors: two origins + two markers → build in E. coli, use elsewhere"],
    notes="BACs matter for loci with full regulatory context (Hox, atonal-class clusters). "
          "YACs enabled megabase-scale genomics but are chimerism-prone.",
    takeaway="Match capacity to the question: cassette vs locus vs genome region.")
add_slide("Selection vs screening vs validation",
    ["SELECTION: undesired cells cannot grow (antibiotic, auxotrophy) — population level",
     "SCREENING: per-candidate test (blue-white, colony PCR, digest) — clone level",
     "VALIDATION: definitive proof (Sanger; then function) — molecule level"],
    diagram="selection_screening.png",
    notes="The funnel is the point: each stage removes a different class of wrong answer. "
          "A colony count is not a correct-clone count.",
    takeaway="Selection enriches populations; screening classifies individuals; validation proves identity.")
add_slide("Blue-white screening — mechanism and limits",
    ["Host strain carries lacZ α-deletion; vector supplies lacZα",
     "Empty vector → functional β-galactosidase → BLUE colonies on X-gal",
     "Insert disrupting lacZα → WHITE colonies — candidates, not proof",
     "Anomalies exist: PCR-positive blue colonies happen (lacZα-sparing insertions)"],
    notes="Use the Lab-04 anomaly as a teaching hook: screening readouts are probabilistic "
          "evidence, not verdicts.",
    takeaway="Screening shortlists; validation settles.")
add_slide("Reading a plasmid map — the 7-point checklist",
    ["ori and copy-number class",
     "Selectable marker(s) — and whether bacterial vs mammalian parts differ",
     "MCS / assembly-scar architecture — which sites are unique?",
     "Promoter(s) and DIRECTION (arrow)",
     "Insert position and orientation — explicitly stated?",
     "Total size — expected band on a digest gel",
     "Priming sites — where can sequencing primers bind?"],
    notes="Exam tip to repeat: a map without orientation arrows is ambiguous; always state "
          "orientation relative to the promoter.",
    takeaway="Map-reading is a skill with a checklist — practice it.")
add_slide("Why every validation stage exists",
    ["Selection alone: 500 colonies could ALL be empty vector",
     "Screening alone: PCR can't see point mutations or rearrangements",
     "Digest alone: uninformative if enzyme choice is poor (single band)",
     "Sequencing alone (without function): sequence-correct ≠ expressing",
     "The chain: selection → screen → digest → Sanger → functional assay"],
    notes="Use the Lab-03/Lab-04 storyline: high colony counts with 85% empty clones "
          "(condition L3) make the point vividly.",
    takeaway="Each stage removes a different class of wrong answer — skip one and it survives.")

# ------------------------------------------------ 3. CLONING TECHNIQUES
section_slide("3 · Cloning Techniques", "Restriction · TA · blunt · Gibson · Golden Gate · Gateway (Module 4)")
add_slide("Restriction enzyme cloning",
    ["Recognition sites 4–8 bp, usually palindromic: EcoRI G^AATTC, HindIII A^AGCTT",
     "Sticky (5′/3′ overhangs) vs blunt ends; compatible ends (BamHI/BglII → GATC)",
     "Directional cloning: two different enzymes force one orientation",
     "Dephosphorylate vector → blocks self-ligation; insert restores phosphates",
     "Insert:vector molar ratio ~3:1 as a starting point (kinetics, not law)"],
    diagram="restriction_cloning.png",
    notes="Methylation sensitivity can block sites in common lab E. coli DNA — a real "
          "design consideration.",
    takeaway="Cut → anneal → ligate: simple, cheap, background-prone.")
add_slide("TA cloning and blunt-end cloning",
    ["TA: Taq adds 3′-A overhangs; T-vector carries 3′-T — fast PCR-product capture",
     "TA limits: no orientation control; high-fidelity polymerases give blunt ends (A-tail first)",
     "Blunt: universal — any flush fragment ligates to any other",
     "Blunt limits: low efficiency, no directionality → dephosphorylation essentially mandatory"],
    notes="Ask students when blunt is the ONLY option: no convenient sites and non-PCR "
          "input (e.g., sheared/adaptor fragments).",
    takeaway="Convenience vs control: TA is fast, blunt is universal, neither is directional.")
add_slide("Gibson Assembly — overlaps do the addressing",
    ["Fragments carry 20–40 bp terminal overlaps",
     "5′ exonuclease chews back → overlaps anneal → polymerase fills → ligase seals",
     "Seamless; multi-fragment; no restriction sites needed",
     "Limits: repeat-driven misassembly; overlap design burden"],
    diagram="gibson_assembly.png",
    notes="The overlap IS the addressing scheme — jigsaw edges. Repeats confuse the jigsaw.",
    takeaway="Design-level addressing: sequence, not restriction sites, defines the product.")
add_slide("Golden Gate — programmable overhangs",
    ["Type IIS enzymes (BsaI, BsmBI, SapI…) cut OUTSIDE the recognition site",
     "4-bp overhang bases are designer-chosen → each junction has an address",
     "One-pot digest+ligation; correct products consumed their recognition sites → self-selecting",
     "Basis of modular cloning hierarchies (MoClo-style level-0 parts → units → multigene)"],
    diagram="golden_gate.png",
    notes="Domestication: internal Type IIS sites must be removed or silently mutated. "
          "Note temperature-cycling for BsaI-class enzymes.",
    takeaway="Scars are 4 bp; efficiency and modularity are unmatched.")
add_slide("Gateway — recombination-based transfer",
    ["attB/P → attL (entry clone) via BP; attL/R → attB (expression clone) via LR",
     "One sequence-verified entry clone feeds many destination vectors",
     "Strength: parallel expression testing across backbones",
     "Limits: att scars; proprietary mixes; counter-selection background (ccdB-type)"],
    notes="Conceptual level only; vendor systems evolve — consult current documentation "
          "before lab use.",
    takeaway="Archive once, deploy everywhere — at the cost of fixed recombination scars.")
add_slide("Choosing a technique — decision guide",
    ["Multi-fragment, seamless? → Gibson (≤ ~6–8) or Golden Gate (many, modular)",
     "Single insert with good unique sites? → restriction–ligation (directional)",
     "Quick PCR capture? → TA. No sites at all? → blunt",
     "One gene → many backbones in parallel? → Gateway"],
    notes="Run the Lab-01 scenario live: internal BamHI forces EcoRI+HindIII.",
    takeaway="The technique choice is a design decision, not a habit.")

# ------------------------------------------------ 4. EXPRESSION & REPORTERS
section_slide("4 · Expression Constructs & Reporters", "Regulatory parts and measurable outputs (Module 5)")
add_slide("Anatomy of an expression cassette",
    ["Promoter → 5′ UTR / RBS (Shine–Dalgarno) or Kozak context → CDS ± tag",
     "3′ UTR → terminator (bacteria) or polyadenylation signal (eukaryotes)",
     "Enhancers/silencers: distal, orientation-flexible modulators",
     "Operators (prokaryotes): repressor/activator binding → inducibility"],
    diagram="expression_cassette.png",
    notes="Same CDS + different regulatory parts = different experiments entirely. "
          "This is the lever students most often under-use.",
    takeaway="The cassette, not just the gene, encodes the experiment.")
add_slide("Expression modes — four dials",
    ["Constitutive: always on — production, housekeeping studies",
     "Inducible: signal-gated (lac/IPTG, Tet/doxycycline, Gal4-ER) — toxicity, timing",
     "Tissue-specific: spatial restriction — reporters, cell-type biology",
     "Developmentally regulated: staged activation — patterning studies"],
    notes="Swap-the-promoter thought experiment: same GFP, four different questions.",
    takeaway="Changing one regulatory element changes the question the construct answers.")
add_slide("Reporter genes — the cast",
    ["GFP: autocatalytic chromophore, needs only O2 → live spatial imaging (Nobel 2008)",
     "RFP/mCherry: red shift → tissue penetration + dual-color with GFP",
     "lacZ: X-gal histochemistry — vivid fixed-tissue maps, enzyme-amplified",
     "Luciferase: luciferin+ATP → photons; quantitative dynamic range; dual-luciferase normalization"],
    notes="Fluorescence = spatial detail; luminescence = quantitation. Choose by question.",
    takeaway="Reporters convert invisible regulatory states into measurable signals.")
add_slide("Reporter design patterns and controls",
    ["Promoter-reporter: 'where is this promoter active?'",
     "Enhancer-reporter: minimal promoter + candidate enhancer (test both orientations)",
     "Fusion reporter: where does the PROTEIN go? (frame, linker, termini matter)",
     "Controls: promoterless + empty vectors, motif mutant, known-active promoter, normalization"],
    diagram="reporter_constructs.png",
    notes="Reporter reports the SEQUENCE's behavior — chromatin context can be missing. "
          "Always pair with endogenous validation (ISH/IF) for strong claims.",
    takeaway="A reporter is sufficiency evidence — not an endogenous-expression verdict.")
add_slide("Landmark: GFP goes live (1994)",
    ["Chalfie et al. expressed GFP in C. elegans touch neurons and E. coli",
     "No substrate, no cofactors beyond O2 → genetically encoded fluorescence",
     "Tsien-engineered variants: brightness, folding, color palette",
     "Consequence: live developmental imaging became routine"],
    notes="Bridge slide: cloning technology (Module 2–4) becomes developmental observation "
          "(Module 8–9).",
    takeaway="One jellyfish protein joined genetic engineering to developmental biology.")
add_slide("Cloning techniques — the comparison table",
    ["Restriction–ligation: cheap, directional possible; needs unique sites; self-ligation background",
     "TA: fast PCR capture; no orientation; A-tailing needed for high-fidelity products",
     "Blunt: universal; low efficiency; heavy background",
     "Gibson: seamless, multi-fragment; overlap design; repeat misassembly",
     "Golden Gate: one-pot, modular, multiplex; domestication of internal sites; 4-bp scars",
     "Gateway: one entry → many destinations; att scars; counter-selection background"],
    notes="Have students reproduce this table from memory — it is the Module-4 anchor. "
          "Each row: mechanism → strength → limitation → scenario.",
    takeaway="No universal technique: the constraint set picks the method.")
add_slide("Worked design — the Lab-01 construct",
    ["Goal: 850-bp zebrafish shha promoter → GFP in a 3.2-kb vector",
     "Scan insert: internal BamHI site → BamHI pair ELIMINATED",
     "Choice: EcoRI + HindIII (unique in vector, absent in insert, directional)",
     "Primers: 5′ clamp + site + gene-specific sequence (frame/termini checked)",
     "Ligation: 50 ng vector at 3:1 → ~31.5 ng insert (molar math)",
     "Diagnostic digest: EcoRI+BamHI → 1.9 + 2.15 kb (empty vector: 3.2 kb single)",
     "Screening: white colonies → colony PCR (Set A + B) → mini-prep → Sanger"],
    notes="Run this live with the design_check.py script on the simulated insert — "
          "students see the internal-site scan that forces the enzyme decision.",
    takeaway="Design is decision-making under constraints — document every choice.")
add_slide("Fusion proteins — in-frame matters",
    ["Insert must join the tag without frameshift → single continuous ORF",
     "Linkers (Gly-Ser repeats) preserve independent folding of both parts",
     "N-terminal fusions: tag's start codon dominates; C-terminal: no premature stop",
     "Fusions can perturb localization/function — always validate against endogenous",
     "Common tags: His6 (purification), FLAG/HA (detection), GFP (imaging), GST (solubility)"],
    notes="The aggregation case: a mispositioned tag can bury a signal peptide or block "
          "an active site — three design causes, three fixes.",
    takeaway="A fusion is a new protein — verify it still behaves.")
add_slide("Transformation and selection — the plating logic",
    ["Chemical transformation (heat shock) or electroporation — per institutional SOP",
     "Positive control (known plasmid) and negative control (no DNA) are mandatory",
     "Selection marker must match the vector — check concentration classes",
     "Colony number ≠ correct-clone number; controls calibrate the background",
     "Electroporation: salt in DNA prep → arcing → dead cells"],
    notes="The positive control is the diagnostic: if it fails, the cells/buffer are the "
          "problem, not your ligation.",
    takeaway="Controls turn colony counts into interpretable data.")
add_slide("Promoter selection — matching promoter to purpose",
    ["Prokaryotic: T7-class (expression strains), lac/tac/trc (tunable), constitutive housekeeping",
     "Mammalian: CMV (strong, broad), EF1α (stable), PGK/UbC (moderate) — silencing varies",
     "Plant: 35S (constitutive), ubiquitin-class, tissue/development-specific promoters",
     "Developmental: endogenous/tissue-specific promoters for spatial questions",
     "Inducible systems: Tet-On/Off, Gal4-ER, heat-shock — temporal control"],
    notes="CMV-driven expression of a gene that is normally tissue-restricted answers a "
          "different question than the endogenous promoter — make students articulate which.",
    takeaway="The promoter is the experimental design, encoded in DNA.")
add_slide("Reporter fusions vs promoter reporters — choosing the readout",
    ["Promoter-reporter: regulatory ELEMENT activity (transcriptional readout)",
     "Fusion reporter: protein localization/dynamics (post-transcriptional readout)",
     "They can disagree — post-transcriptional regulation is real biology",
     "Destabilized reporters (degron-tagged GFP): read CURRENT expression, not history",
     "For quantitation over time: luciferase wins; for spatial detail: fluorescence wins"],
    notes="Case: a protein whose mRNA is everywhere but protein is nuclear-only — the two "
          "reporter designs tell different true stories.",
    takeaway="Match the reporter's biological level (RNA vs protein) to the question.")

# ------------------------------------------------ 5. GMO GENERATION
section_slide("5 · GMO Generation", "Bacteria, plants, animals — shared spine, different biology (Module 6)")
add_slide("What makes an organism 'modified'?",
    ["Laboratory-altered genetic material in a defined, designed way",
     "Transgenic / cisgenic / gene-edited / knockout / knock-in / reporter",
     "Stable = inherited (integration, maintained plasmid) vs transient = fading",
     "In embryos: reagents transient, edits stable — the distinction that confuses everyone"],
    notes="Anchor with the five example classes; ask students to classify Golden Rice, "
          "an apoE knockout mouse, and a plasmid-transfected culture.",
    takeaway="Category determines interpretation — and often regulation.")
add_slide("Bacteria — the fast lane",
    ["Construct → transformation/electroporation → selection → screen → validate → phenotype",
     "Landmark: recombinant insulin (Humulin, 1982 — first rDNA drug)",
     "Industrial enzymes (amylases, chymosin); engineered metabolism (artemisinic acid)",
     "Colony = organism: days, not months"],
    notes="Note host choice: insulin is non-glycosylated — E. coli/yeast fine; glycoproteins "
          "need CHO-class hosts.",
    takeaway="Microbes trade complexity for speed.")
add_slide("Plants — totipotency does the heavy lifting",
    ["Agrobacterium: natural T-DNA transfer (Ti plasmid, border repeats, vir genes)",
     "Disarmed systems + binary vectors: cassette between borders; vir in trans",
     "Biolistics: DNA-coated particles — for recalcitrant species, chloroplast targets",
     "Tissue culture → regeneration → selection → molecular confirmation → field trials under permit"],
    diagram="gmo_workflows.png",
    notes="Totipotency: one modified somatic cell regenerates a whole plant — conceptually "
          "simpler than embryo-by-embryo animal work.",
    takeaway="The plant regenerates itself; engineering is delivery + selection.")
add_slide("Landmark crops — history to present",
    ["Bt cotton/corn (1996→): Cry proteins; resistance managed by refuges/pyramids",
     "Herbicide-tolerant soybean/corn: CP4 EPSPS; weed-resistance drove trait evolution",
     "PRSV-resistant 'Rainbow' papaya: saved the Hawaiian industry (public sector)",
     "Golden Rice: psy+crtI → provitamin A; GR2E food-safety approvals (2021→, verify current status)",
     "Gene-edited crops: waxy corn, MLO-edited wheat, non-browning mushroom — status varies by country"],
    notes="Statuses change — mechanisms are stable, regulations are not. Flag "
          "re-verification for any commercial claim.",
    takeaway="Traits succeed or fail as agronomy + policy, not just molecular biology.")
add_slide("Animals — embryo routes and founder logic",
    ["Pronuclear microinjection (classic transgenesis, 1981–82 'supermouse')",
     "ES-cell knockouts (Capecchi/Smithies/Evans, Nobel 2007) — targeted mammalian genetics",
     "SCNT: Dolly (1996/97) — cloning ≠ transgenesis; reprogramming in vivo",
     "CRISPR era: cytoplasmic editing reagents → F0 screening (species-dependent)",
     "Founder identification → germline transmission → breeding → phenotyping under animal-care approval"],
    notes="No operational animal parameters in this course — species/jurisdiction-specific, "
          "under animal-care protocols.",
    takeaway="Mosaic founders and slow breeding shape every animal-engineering design.")

# ------------------------------------------------ 6. CRISPR
section_slide("6 · Genome Editing & CRISPR", "Programmable changes at chosen addresses (Module 7)")
add_slide("CRISPR–Cas9 in one picture",
    ["Bacterial adaptive immunity → laboratory programmability",
     "sgRNA (~20-nt guide) + Cas9 + PAM (SpCas9: NGG)",
     "Guide-target pairing → R-loop → HNH/RuvC cleavage → blunt DSB ~3 bp from PAM",
     "The cell's repair choice writes the edit"],
    diagram="crispr_mechanism.png",
    notes="PAM is required for initiation — that's why it constrains targetable space "
          "and contributes to specificity.",
    takeaway="CRISPR does not edit; it creates the break. REPAIR does the editing.")
add_slide("Repair pathways decide the outcome",
    ["NHEJ: active through the cell cycle; error-prone → indels → KNOCKOUT",
     "HDR: S/G2-biased, needs donor → precise correction/KNOCK-IN",
     "Knock-ins are hard: HDR-inefficiency in primary cells; alternatives: HITI, editors",
     "In-frame indels can escape knockouts — screen alleles, validate protein"],
    notes="The Ma et al. 2017 MYBPC3 embryo work and its follow-up literature illustrate "
          "why repair-mechanism context matters.",
    takeaway="Design for the repair pathway you need — not the one you get by default.")
add_slide("Beyond nucleases — base and prime editing",
    ["Base editors: dead/nickase Cas9 + deaminase → C→T, A→G (no DSB; bystander risk)",
     "Prime editors: nickase + reverse transcriptase + pegRNA → all base swaps + small indels",
     "dCas9 chassis → CRISPRa (sufficiency) / CRISPRi (necessity) without genome change",
     "Cas12a (staggered cuts, multiplexing), Cas13 (RNA targets)"],
    diagram="base_prime_editing.png",
    notes="Editors trade HDR-dependence for window/bystander/efficiency constraints — "
          "honest comparison on the slide.",
    takeaway="No-DSB editors solve the HDR problem and create their own.")
add_slide("Transgenesis vs genome editing — the honest table",
    ["Transgenesis ADDS a designed unit; editing CHANGES an endogenous sequence",
     "Random vs defined locus; positional effects vs native context",
     "Multiplexing: each construct vs several sgRNAs in one experiment",
     "Big cargo (BACs/transposons) vs size-limited delivery",
     "Modern projects often use both: edited allele + transgenic reporter"],
    notes="Ask the class: which approach for (a) a loss-of-function allele, (b) a "
          "lineage reporter with full enhancer context?",
    takeaway="Pick by goal: add a program or change a letter.")
add_slide("Off-targets, mosaicism, validation",
    ["Off-targets: partial-match sites; mitigate by guide design, hi-fi variants, RNP delivery — and EMPIRICAL checks",
     "Mosaicism: post-one-cell editing → different alleles per tissue → genotype multiple tissues",
     "Validation: bulk genotyping → isolate → zygosity → off-target screen → outcross → line",
     "F0 screens (zebrafish crispants) ≠ founder genetics (mouse) — timing of germline differs"],
    notes="Genotyping depth and tissue choice are where editing projects quietly fail.",
    takeaway="The edit is not done until the line is genotyped and the protein checked.")
add_slide("CRISPR workflow — design to genotyped line",
    ["Design: guide choice (on-target + off-target scoring), donor if knock-in",
     "Delivery: RNP / mRNA / plasmid — transient expression limits exposure",
     "Bulk genotyping: amplicon sequencing or Sanger-deconvolution (ICE-class)",
     "Isolate founders/colonies → zygosity → off-target screen → outcross → line",
     "Protein/function validation: Western, activity, phenotype rescue"],
    notes="RNP delivery reduces off-target exposure because the nuclease degrades quickly — "
          "a design lever students should connect to the mosaicism slide.",
    takeaway="Editing projects are genotyping projects with a biology question at the end.")
add_slide("CRISPR screens — loss-of-function at scale",
    ["Genome-wide sgRNA libraries → pooled cell populations",
     "Dropout/enrichment analysis → essential genes, drug-resistance factors",
     "Landmark: Shalem/Wang 2014 genome-wide knockout screens",
     "CRISPRa/i screens: gain-of-function and repression coverage",
     "Analysis discipline: multiple guides per gene, FDR, copy-number correction"],
    notes="Screens moved CRISPR from 'one gene at a time' to systematic discovery — "
          "connect to Module 10's network-inference loop.",
    takeaway="Pooled genetics with programmable guides rewired functional genomics.")
add_slide("Editing vs classical genetics — timing compared",
    ["Classical mouse KO: ES-cell targeting → chimeras → breeding: 1–2 years",
     "CRISPR mouse F0: weeks — but mosaicism and off-targets to manage",
     "Zebrafish crispants: days for loss-of-function phenotypes (F0, transient mosaic)",
     "Arabidopsis: floral-dip transformation + edited lines via segregation",
     "The trade: speed vs cleanliness — know which your question needs"],
    notes="F0 zebrafish phenotyping is powerful but mosaic — confirm with stable lines "
          "for publication-grade claims.",
    takeaway="Editing compressed genetics from years to weeks — with new QC duties.")

# ------------------------------------------------ 7. DEVELOPMENTAL GENE EXPRESSION
section_slide("7 · Developmental Gene Expression", "Differential expression, morphogens, GRNs (Modules 8–10)")
add_slide("Development = differential gene expression",
    ["One genome; different transcriptional programs per cell",
     "Cell fate → determination (fixed despite transplantation) → differentiation",
     "Potency narrows: totipotent → pluripotent → multipotent → unipotent",
     "Master regulators: sufficiency demonstrated (myoD) — endogenous mechanisms are multi-input"],
    notes="The myoD caveat matters: 'master' describes the experimental result, "
          "not the whole in-vivo mechanism (Pax3/7 + signaling + chromatin).",
    takeaway="Developmental biology = which genes are on, where, when, and why.")
add_slide("Morphogens — the French-flag logic",
    ["Localized source → diffusion + degradation → concentration gradient",
     "Cells respond to thresholds → distinct fates at distinct distances",
     "Mechanisms vary (diffusion, transcytosis, cytonemes) — threshold logic is shared"],
    diagram="morphogen_gradient.png",
    notes="Turing 1952; Wolpert 1969. Duration of exposure matters as much as "
          "concentration in the neural tube.",
    takeaway="A gradient is positional information; interpretation is thresholded.")
add_slide("The recurring signaling cast",
    ["Wnt/β-catenin — axis, stem compartments, organizer (dorsal zebrafish)",
     "Hedgehog/Shh — neural-tube DV, limb A–P (ZPA), sclerotome",
     "TGF-β/BMP/Nodal — mesoderm induction, neural induction via BMP inhibition",
     "Notch — lateral inhibition, boundaries (Delta/Jagged → NICD)",
     "FGF — outgrowth (AER), mesoderm migration; Retinoic acid — hindbrain/limb PD"],
    notes="Pathway outputs converge on cis-regulatory elements — a cell's combination of "
          "active pathways is its positional address.",
    takeaway="Seven pathways, endlessly recombined, pattern most of the embryo.")
add_slide("Model organisms — who does what best",
    ["Drosophila: forward genetics; segmentation hierarchy (Nüsslein-Volhard/Wieschaus, Nobel 1995)",
     "C. elegans: invariant lineage (Sulston); apoptosis, miRNA (lin-4/let-7)",
     "Zebrafish: transparent external development; live imaging; F0 screens",
     "Mouse: mammalian genetics; ES-cell/conditional alleles (Cre-lox)",
     "Arabidopsis: plant development; WUS/CLV stem-cell niche; ABC floral model"],
    notes="Match organism to question: lineage precision vs live vertebrate imaging vs "
          "mammalian relevance vs plant cell biology.",
    takeaway="The model is a tool chosen by the question, not by habit.")
add_slide("Hox genes and body-plan identity",
    ["Conserved clusters specifying A–P identity (Lewis 1978; McGinnis/Krumlauf)",
     "Colinearity: 3′ = anterior/early; 5′ = posterior/late",
     "Ectopic expression → homeotic transformations (Antennapedia legs-for-antennae)",
     "Colinearity implies shared chromatin/regulatory architecture"],
    notes="Enhancer deletions shift domain boundaries — link to Module 10 CRM logic.",
    takeaway="One regulatory architecture, deployed along the axis, in nearly all animals.")
add_slide("Drosophila segmentation — the first GRN",
    ["Maternal gradients (Bicoid/Nanos) → gap genes → pair-rule (7 stripes) → segment-polarity (14) → Hox",
     "Cross-regulation sharpens every boundary (mutual repression, e.g., Gt/Kni)",
     "Each layer is more spatially precise AND later in time — refinement cascade"],
    diagram="grn_cascade.png",
    notes="The 1980 saturation screen found zygotic genes — maternal ones needed separate "
          "genetics. Ask why (embryo lethality of mothers).",
    takeaway="Patterning is a temporal refinement cascade over spatial information.")
add_slide("Neural tube — the Shh textbook case",
    ["Shh from notochord/floor plate; BMPs from roof plate — opposing gradients",
     "Concentration AND duration of Shh → V3 → motor → V2 → V1 ventral classes",
     "Ectopic Shh induces ventral fates dorsally — sufficiency demonstrated",
     "Domains (nkx2.2, pax6, olfm-class boundaries) execute what gradients inform"],
    diagram="neural_tube_pattern.png",
    notes="Ask: why do domains sharpen beyond the gradient shape? Cross-repression "
          "(Module 10 motifs).",
    takeaway="Gradients inform; domains execute; cross-repression sharpens.")

# ------------------------------------------------ 8. SPATIAL & TEMPORAL
section_slide("8 · Spatial & Temporal Expression", "Where, when — and the methods that resolve each (Module 9)")
add_slide("Three axes of every expression statement",
    ["SPATIAL — where in organism/tissue/cell?",
     "TEMPORAL — when in development/response?",
     "QUANTITATIVE — how much, relative to what control?",
     "Bulk measurements integrate all three away — resolution is a design choice"],
    notes="The zebrafish example: bulk RNA-seq says 'gene X peaks at 24 hpf'; ISH says "
          "'in the notochord from 10-somite stage'. Different claims, different tools.",
    takeaway="State the axis before choosing the method.")
add_slide("Spatial concepts — gradient vs domain",
    ["Gradient: continuous concentration change (Bicoid A–P; Shh D–V)",
     "Domain: sharply bounded expression region (eve stripe 2; nkx2.2)",
     "Tissue- vs cell-type- vs stage-specificity — nested restrictions",
     "Gradients usually inform; domains usually execute"],
    notes="Zebrafish somitogenesis is the cleanest two-axis example: her1/7 oscillations "
          "(time) freeze at the determination front (space) — clock-and-wavefront.",
    takeaway="Gradient geometry carries information; domain geometry records decisions.")
add_slide("Spatiotemporal case studies",
    ["Drosophila A–P: maternal gradient → zygotic stripes — refinement cascade",
     "Zebrafish somitogenesis: clock (Notch-linked oscillations) + wavefront (FGF/Wnt)",
     "Neural tube: gradient × duration → fate classes",
     "Arabidopsis flower: concentric ABC classes × staged identity (LFY/AP1 first)"],
    notes="Each case pairs one spatial mechanism with one temporal mechanism — have "
          "students name both axes explicitly.",
    takeaway="Every developmental pattern is an intersection of space and time.")
add_slide("Method fit — resolving space and time",
    ["ISH / RNA-FISH: endogenous mRNA, spatial (endpoint)",
     "IHC/IF: protein spatial map (endpoint; antibody-dependent)",
     "Reporters (GFP/luc): LIVE dynamics of a regulatory element",
     "RT-qPCR: magnitude over time (no space)",
     "scRNA-seq: cell types (no coordinates); Spatial transcriptomics: cells + coordinates"],
    notes="The decision matrix from Module 9 §4 — students should reproduce it from memory "
          "in the exam.",
    takeaway="Each method buys resolution on one axis by spending it on another.")
add_slide("Temporal expression — developmental timing",
    ["Stage-specific genes: windows of activity (hunchback early; myod1 at commitment)",
     "Maternal → zygotic transition: maternal mRNAs decay, zygotic genome activates",
     "Oscillating genes: segmentation clocks (her1/7 in zebrafish PSM)",
     "Staging rigor: hpf/somite counts/E-days — the temporal variable must be controlled",
     "Heatmap reading: decaying rows = maternal; rising rows = zygotic"],
    diagram="expression_heatmap.png",
    notes="The heatmap is the simulated developmental timecourse from DATA/ — the single "
          "most transferable visualization in developmental transcriptomics.",
    takeaway="Temporal patterns have signatures — learn to read decay vs rise vs oscillation.")
add_slide("Expression gradients — case gallery",
    ["Bicoid (Drosophila): maternal mRNA → A–P protein gradient → hunchback activation",
     "Shh (vertebrates): notochord/floor-plate source → DV neural tube + limb ZPA",
     "BMP (dorsal ectoderm): opposing Shh — dorsal fates",
     "Wnt: axis elongation, organizer, stem niches",
     "Retinoic acid: RALDH-synthesis vs CYP26-degradation gradients — hindbrain/limb"],
    notes="Each gradient pairs a source and a sink/mechanism — synthesis and degradation "
          "enzymes shape RA, not simple diffusion alone.",
    takeaway="Gradients are built by production AND destruction — both are regulatory.")
add_slide("Expression domains — case gallery",
    ["eve stripe 2 (Drosophila): the classic enhancer-dissection textbook case",
     "engrailed stripes: segment-polarity maintenance via wg/hh feedback",
     "nkx2.2 / pax6 boundary (neural tube): cross-repression sharpens the edge",
     "ABC-class MADS genes (Arabidopsis): concentric whorl domains",
     "Domains often sit ON gradients — the readout is binary, the input is analog"],
    notes="eve stripe 2: multiple activator/repressor sites in one CRM integrate maternal "
          "and gap-gene inputs — connect to Module 10.",
    takeaway="Domains are the writable output of gradient-reading circuits.")
add_slide("Designing a spatiotemporal study — the 7-point checklist",
    ["State the question on BOTH axes (where AND when)",
     "Choose resolution: cell type vs region vs whole embryo",
     "Choose method(s): endpoint (ISH/IF) vs live (reporter) vs snapshot omics",
     "Staging control: define the temporal variable rigorously",
     "Replicates: biological (clutches/litters) — not just technical",
     "Controls: sense/no-probe, known marker, reporter controls",
     "Quantification plan BEFORE imaging: area, intensity, counts"],
    notes="Have students apply this checklist to their capstone designs — it is the "
          "grading rubric for Lab-09.",
    takeaway="Spatial studies fail on staging and quantification planning, not on stains.")

# ------------------------------------------------ 9. METHODS
section_slide("9 · Experimental Methods", "From probe design to spatial matrices (Module 11)")
add_slide("In situ hybridization — endogenous spatial mapping",
    ["Fix/permeabilize → antisense labeled probe → hybridize → stringent wash → detect → image",
     "Antisense = true signal; sense probe = CANNOT pair → the clean negative control",
     "Controls: no-probe, known-marker (positive + staging), replicates",
     "Semi-quantitative: pattern is trustworthy; absolute amount is not"],
    diagram="ish_workflow.png",
    notes="Probe design must mask repeats; low-abundance targets need "
          "amplification-based approaches (RNAscope-class).",
    takeaway="ISH answers 'where, endogenously' — at the cost of being an endpoint.")
add_slide("RNA-based quantitation — RT-qPCR and RNA-seq",
    ["RT-qPCR: RT → real-time amplification → Cq → ΔΔCt vs validated references",
     "Controls: no-RT (genomic DNA), no-template (contamination), reference stability",
     "Bulk RNA-seq: library → sequence → count matrix → normalize → model → FDR",
     "Bulk = average over cells: heterogeneity and small hot regions vanish"],
    diagram="qpcr_workflow.png",
    notes="Statistics on ΔCt, not fold change. For RNA-seq: n≥3 biological, balanced "
          "batches, negative-binomial modeling in research practice.",
    takeaway="Quantitation needs validated references — and honest averages.")
add_slide("Single-cell RNA-seq — types without places",
    ["Dissociate → barcode (UMIs) → sequence → cells × genes matrix",
     "QC (library size, genes/cell, doublets) → normalize → PCA/UMAP → cluster → marker annotation",
     "Trajectories/pseudotime: transcriptional order, NOT clock time",
     "Dropout: absence of a low transcript ≠ absence of biology"],
    diagram="scrnaseq_workflow.png",
    notes="Spatial context is severed at dissociation — the motivation for spatial methods. "
          "Cell-type discovery is the superpower; coordinates are the cost.",
    takeaway="scRNA-seq resolves WHAT cells are — not WHERE they are.")
add_slide("Spatial transcriptomics — expression in place",
    ["Array-based: tissue on barcoded spots (~55 µm; spot = several cells → deconvolution)",
     "Imaging-based (MERFISH/seqFISH-class): barcoded probes decoded in situ — hundreds of genes, single cell",
     "Output: expression matrix WITH coordinates, aligned to histology",
     "Enables: region markers, gradients, ligand–receiver neighborhood logic"],
    diagram="spatial_workflow.png",
    notes="Nature Methods 'Method of the Year 2020'. Trade-off: plex vs resolution vs "
          "throughput.",
    takeaway="Spatial transcriptomics reconnects molecular state to anatomy.")
add_slide("smFISH and multiplexed imaging — single molecules in place",
    ["Many short oligos per transcript → diffraction-limited spots = single mRNAs",
     "Absolute counts per cell; nascent transcription sites visible",
     "Subcellular localization: mRNA transport, granules, cortical enrichment",
     "MERFISH/seqFISH-class: barcoded sequential imaging → hundreds–thousands of genes",
     "The bridge between classical ISH and spatial transcriptomics"],
    notes="Absolute quantitation is the superpower: burst-size and frequency inference "
          "comes from these distributions (Module 15).",
    takeaway="Counting molecules in place turns expression into measurable distributions.")
add_slide("Immunohistochemistry / immunofluorescence — the protein layer",
    ["Antibody binding → chromogenic or fluorescent detection of PROTEIN",
     "Controls: no-primary, isotype, knockout tissue, secondary-only",
     "Specificity must be validated — antibodies are the field's known weak point",
     "IHC/ISH disagreement = post-transcriptional regulation — real biology, not error"],
    notes="Knockout-tissue control is the gold standard for antibody specificity — "
          "much stronger than vendor claims.",
    takeaway="Protein maps complete mRNA maps — disagreement is information.")
add_slide("Method choice — the one-slide decision guide",
    ["WHERE, one/few genes, endogenous? → ISH / RNA-FISH / IF",
     "WHERE + DYNAMICS? → reporter (validated element) + ISH confirmation",
     "WHICH GENES define a cell type/region? → scRNA-seq or spatial transcriptomics",
     "HOW MUCH over time, few genes? → RT-qPCR time course",
     "GENOME-WIDE across stages? → bulk RNA-seq + targeted validation"],
    notes="The Module-11 decision guide verbatim — students reproduce this in the exam.",
    takeaway="Discover broadly → validate spatially and functionally.")

# ------------------------------------------------ 10. DATA ANALYSIS
section_slide("10 · Computational Analysis", "Reading gels, Cqs and count matrices (Module 12)")
add_slide("Cloning data — the diagnostic logic",
    ["Gel: migration ∝ log(size); interpolate against a ladder",
     "Colony PCR: flanking primers = size; vector+insert primers = orientation",
     "Diagnostic digest: fragments must match the map AND sum to plasmid size",
     "Sum > map size → rearrangement — the check everyone skips"],
    notes="Work the Lab-02 examples: A correct, B empty, C rearranged (2.3+1.7+0.9 = 4.9 kb ≠ 3.2 kb).",
    takeaway="Two rules: interpolate against the ladder; always sum the fragments.")
add_slide("qPCR — ΔΔCt done right",
    ["ΔCt = Cq(target) − Cq(reference) · ΔΔCt vs calibrator · FC = 2^(−ΔΔCt)",
     "Assumes ~100% efficiency; otherwise efficiency-corrected (Pfaffl)",
     "Statistics on ΔCt (normal-ish), never on fold changes (skewed)",
     "Geometric-mean references; report n, references, test, effect size"],
    notes="Lab-05 numbers: myod1 18 hpf ≈ 7.5× vs 10 hpf — then validate spatially (ISH).",
    takeaway="Validated references are the difference between data and noise.")
add_slide("Bulk RNA-seq analysis",
    ["Filter low counts → normalize (size factors/CPM) → model → Benjamini–Hochberg FDR",
     "Sort by effect size (|log2FC|), filter by FDR — never p alone",
     "20,000 tests at 5% FDR ≈ 1,000 expected false calls — that's what FDR means",
     "Batch must not confound condition — check PCA BEFORE interpreting"],
    diagram="rnaseq_workflow.png",
    notes="Mini-workflow on the simulated 500×6 dataset; research practice = DESeq2/edgeR-class "
          "negative-binomial models.",
    takeaway="Design and multiple-testing discipline precede any gene list.")
add_slide("Single-cell analysis",
    ["QC: library size, detected genes, doublets → normalize/log → PCA → cluster",
     "Annotate clusters with marker genes (pax6a-neural; myod1-muscle; hbbe1-blood)",
     "Subclusters reveal transitions (low-myod1 differentiating precursors)",
     "Pseudotime orders transcriptional states — developmental sequence, not time"],
    notes="Lab-08 dataset: 600 cells → 3 clean clusters + a k=4 transition subcluster. "
          "Absence (dropout) is not evidence of absence.",
    takeaway="Clusters are hypotheses; markers and validation turn them into cell types.")
add_slide("Spatial data analysis",
    ["Join matrix + coordinates + (training) region labels",
     "Region-mean expression → top marker per region → in-silico in situ (x,y plots)",
     "Gradient test: correlate expression with distance (r ≈ −0.6 edge-gene example)",
     "Ligand in region A neighboring receptor in region B = hypothesis to validate"],
    diagram="spatial_map_sim.png",
    notes="End every spatial finding with its independent check: ISH for the gradient gene, "
          "reporter or perturbation for the axis.",
    takeaway="Spatial matrices generate spatial hypotheses; ISH and perturbation confirm them.")
add_slide("RNA-seq quality discipline",
    ["Biological replicates: n≥3 is the floor — technical reps never substitute",
     "Batch balance: randomize/interleave conditions across processing batches",
     "Strandedness, polyA vs total RNA — declare and record library choices",
     "QC before interpretation: mapping rate, duplication, 3′ bias, PCA",
     "Report: n, normalization, test, FDR, effect size — every time"],
    notes="The PCA-first rule: if batch explains the data, no downstream gene list is "
          "interpretable.",
    takeaway="RNA-seq credibility is decided at design time, not analysis time.")
add_slide("Volcano plots and honest gene lists",
    ["x = log2FC (effect), y = −log10 p (evidence) — read both, filter by FDR",
     "The 1,800-gene-no-effect trap: near-zero FCs at scale = design artifact",
     "Low-count genes: unstable FCs — filter before testing",
     "Annotate gene lists with what you KNOW (pathway membership) — interpret, don't just rank"],
    notes="Demo on the simulated 500×6 dataset: 18 genes pass FDR<0.05 & |log2FC|>1, "
          "including a coherent 5-gene module.",
    takeaway="Effect size + FDR + biology = an interpretable gene list.")

# ------------------------------------------------ 11. CASE STUDIES
section_slide("11 · Case Studies", "Twelve cases linking tools to biology (Module 13)")
add_slide("Agricultural GMOs — three arcs",
    ["Bt crops: Cry toxins; pesticide-use reductions; resistance evolution → refuges/pyramids",
     "Golden Rice: endosperm provitamin A (psy+crtI); approvals 2021→; deployment debates",
     "Gene-edited crops: native-locus knockouts (waxy corn, MLO wheat) — product vs process regulation"],
    notes="All three: mechanism is settled; deployment is agronomy + regulation + acceptance. "
          "Keep the Module-14 layering when discussing.",
    takeaway="Traits live or die on evidence AND governance.")
add_slide("Medical and research classics",
    ["Recombinant insulin (1982): rDNA's clinical proof — small, non-glycosylated protein",
     "GFP organisms (1994→): live imaging revolution — promoter vs fusion logic",
     "Disease models: apoE−/−, mdx, SOD1-G93A — face/content/predictive validity; partial replication",
     "CRISPR knockouts/screens (2014→): loss-of-function genetics democratized"],
    notes="Use SOD1 as the model-limit discussion: why some trial successes in mice failed "
          "clinically.",
    takeaway="Models are tools with known failure modes — state them.")
add_slide("Developmental case studies",
    ["Hox regulation: colinear clusters; enhancer deletions shift boundaries",
     "Drosophila patterning: the first fully-worked GRN cascade",
     "Shh spatial signaling: gradient → threshold fates (V3→V1); duration matters",
     "Single-cell atlases: cell-type catalogs far richer than histology suggested",
     "Spatial transcriptomics: molecular anatomy — Method of the Year 2020"],
    notes="Each case is a cloning + expression + data-analysis story — the course in miniature.",
    takeaway="Developmental cases show WHY the tools matter.")
add_slide("Case study — PRSV-resistant papaya",
    ["Biological question: can pathogen-derived resistance save a devastated industry?",
     "Strategy: viral coat-protein gene expressed in papaya ('Rainbow', 1998)",
     "Mechanism: coat-protein-mediated resistance against Papaya Ringspot Virus",
     "Result: Hawaiian papaya production recovered; classic public-sector GMO",
     "Lesson: trait design from the pathogen's own biology"],
    notes="Contrast with Bt (toxin-based) and Golden Rice (metabolic) — three different "
          "mechanism classes in agriculture.",
    takeaway="Resistance can be engineered FROM the pathogen itself.")
add_slide("Case study — single-cell atlas of development",
    ["Question: how many cell types exist, and how do they arise?",
     "Strategy: scRNA-seq across stages (organogenesis atlases; zebrafish embryogenesis)",
     "Result: cell-type catalogs far richer than histology suggested; trajectory structure",
     "Interpretation: development as a branching transcriptional landscape",
     "Limits: no coordinates (motivates spatial methods); dropout; snapshots"],
    notes="Ask: which claims REQUIRE spatial validation? (anything about WHERE cells are "
          "or how they contact each other.)",
    takeaway="scRNA-seq redefined the unit of developmental biology: the cell type.")

# ------------------------------------------------ 12. ETHICS
section_slide("12 · Ethics, Biosafety & Regulation", "Four layers, kept distinct (Module 14)")
add_slide("The four-layer framework",
    ["Scientific evidence — what we can measure (gene flow, resistance, safety studies)",
     "Risk assessment — structured hazard × exposure × consequence, vs baseline practice",
     "Ethical considerations — autonomy, justice, animal welfare, germline consent",
     "Policy/regulation — process-based (EU) vs product-based (US) framings"],
    notes="Conclusions at one layer are not evidence at another. Labeling debates are "
          "ethics/policy, not food-safety data.",
    takeaway="Separate the layers — then argue explicitly.")
add_slide("Biosafety in practice",
    ["Containment levels by organism/system; institutional IBC/ETH approval governs",
     "Teaching labs: disabled strains, instructor-approved materials, institutional SOPs",
     "This course: conceptual workflows + simulations; no operational animal/viral parameters",
     "DURC and gain-of-function research: dedicated oversight frameworks"],
    notes="Reinforce: students never self-assign biosafety levels. Approved SOPs only.",
    takeaway="Biosafety is a practice, not a paragraph.")
add_slide("Editing humans — the bright line",
    ["2018 He Jiankui CCR5 case: condemned broadly — oversight, consent, transparency failures",
     "WHO 2021 governance framework: strict limits on heritable human editing",
     "Somatic vs germline distinction: therapy for a patient vs changes to future persons",
     "Technical possibility ≠ ethical readiness"],
    notes="Keep this evidence-first: what happened, what frameworks now say, what remains "
          "contested.",
    takeaway="Some lines are drawn by governance capacity, not by technique.")
add_slide("Gene flow and environmental questions",
    ["Pollen-mediated outcrossing: documented for canola, maize (low frequencies)",
     "Depends on species, distance, sexual compatibility with wild relatives",
     "Horizontal gene transfer mechanisms exist — assessed case-by-case",
     "Resistance evolution: documented in Bt target pests; refuge/pyramid management",
     "Herbicide-tolerance weeds: selection pressure — a management, not gene-flow, issue"],
    notes="Keep claims product- and trait-specific: 'gene flow happens' is a mechanism, "
          "not a risk magnitude — exposure and consequence vary.",
    takeaway="Environmental risk assessment is quantitative, not categorical.")
add_slide("Food safety assessment frameworks",
    ["Codex Alimentarius: the international reference for GM food safety assessment",
     "Compositional equivalence: targeted comparison with conventional counterparts",
     "Novel protein screening: digestibility, homology to allergens/toxins",
     "Feeding studies where indicated — case-by-case, not universal",
     "Decades of consumption through major regulatory systems + documented challenges"],
    notes="Both truths held together: reassuring assessments for products evaluated through "
          "major systems, AND real documented issues (resistance, IP concentration).",
    takeaway="Safety is assessed per product — the category label settles nothing.")

# ------------------------------------------------ 13. ADVANCED
section_slide("13 · Advanced Concepts", "Chromatin, circuits, and the editing frontier (Module 15)")
add_slide("Regulatory chromatin",
    ["H3K4me1+H3K27ac = active enhancer · H3K27me3 = Polycomb · bivalency = poised lineage genes",
     "ATAC-seq: open chromatin + TF footprints; ChIP/CUT&Tag: occupancy maps",
     "Pioneer factors open nucleosomal DNA — why some TFs reprogram identity",
     "DNA methylation: stable repression; imprinting; developmental dynamics"],
    notes="Bivalency is the developmental punchline: stem cells hold lineage genes ready "
          "for either direction.",
    takeaway="Chromatin is the cell's memory and its option book.")
add_slide("3D genome and super-enhancers",
    ["TADs constrain enhancer search space (CTCF/cohesin boundaries)",
     "Loops and condensate models — active research debate, present as such",
     "Super-enhancers: dense H3K27ac/Mediator/BRD4 clusters controlling identity genes",
     "Enhancer hijacking: structural variants relocate enhancers near oncogenes"],
    notes="CRISPRi of a candidate enhancer + PRO-seq nascent readout = clean student-level "
          "entry experiment.",
    takeaway="Who contacts whom is regulatory information.")
add_slide("Synthetic circuits and conditional systems",
    ["Motifs → circuits: toggles, repressilators, AND-gates, band-pass filters",
     "Conditional toolkits: Cre-lox, Flp-FRT, Dre-rox; Tet-On/Off; Gal4/UAS (fly, fish)",
     "Intersectional strategies: Cre+Flp overlaps → precision expression",
     "SynNotch: custom ligand → transcriptional program (cell-therapy logic)"],
    notes="Bridge from Module 8's GRN motifs to engineering the same motifs.",
    takeaway="The motifs developmental biology discovered became engineering parts.")
add_slide("CRISPR frontier — multiplex and epigenome",
    ["Multiplexing: Cas12a arrays, tRNA/ribozyme-flanked guides — pathways, polygenic traits",
     "CRISPRa/i: targeted up/down-regulation — sufficiency/necessity without DNA change",
     "Epigenome editing: dCas9-DNMT3A/TET1 — targeted methylation (memory varies)",
     "Prime editing: search-and-replace without donors — locus- and cell-dependent efficiency"],
    notes="Have students map each tool to necessity vs sufficiency testing.",
    takeaway="The editing frontier is about control precision, not just cutting.")
add_slide("Advanced — gene regulatory network inference",
    ["Inputs: expression (scRNA/time-course) + chromatin (ATAC/ChIP) + motifs",
     "Edge inference: co-expression, motif enrichment, perturbation signatures",
     "Prioritize → perturb (KO/CRISPRi) → reporter test → validate downstream fates",
     "Co-expression is not causation — perturbation is the gold standard"],
    notes="The myogenic network example: every edge (Pax3/7 → Myf5/Myod → myogenin) was "
          "established by perturbation, not correlation.",
    takeaway="Inferred edges are hypotheses; perturbation is the referee.")
add_slide("Advanced — developmental trajectories and lineage",
    ["Pseudotime: order cells by transcriptional similarity along a trajectory",
     "RNA velocity: spliced/unspliced ratios add directionality (assumptions apply)",
     "Lineage tracing: barcode-based phylogenies reconstruct fate decisions",
     "States vs types: continuous variation within a type; cell-cycle confounds",
     "Pseudotime ≠ chronological time — anchor with real timepoints where possible"],
    notes="Velocity assumptions (stationary splicing kinetics) can break in developmental "
          "samples — state them when interpreting.",
    takeaway="Trajectories reconstruct sequence from snapshots — carefully.")
add_slide("Advanced — transcriptional bursting and noise",
    ["RNAPII transcription is intermittent: bursts separated by refractory periods",
     "Consequences: cell-to-cell variability in isogenic populations",
     "Measurement: MS2/MCP live stem-loop imaging; smFISH distributions",
     "Burst size vs frequency: promoter kinetics from count distributions",
     "Noise is developmental material: robustness mechanisms exist because noise exists"],
    notes="Connect to feedback motifs (Module 10): negative feedback suppresses noise, "
          "positive feedback amplifies commitment.",
    takeaway="Gene expression is stochastic — regulation means shaping distributions.")

# ------------------------------------------------ 14. REVIEW
section_slide("14 · Review & Assessment", "Consolidate and test (Assessment package)")
add_slide("The course in one slide",
    ["Tools: cloning (restriction → Gibson/Golden Gate/Gateway) → constructs → reporters",
     "Delivery: transformation / Agrobacterium / embryo editing → GMOs",
     "Editing: CRISPR → NHEJ/HDR → base/prime editors",
     "Biology: differential expression → morphogens → GRNs → spatial-temporal maps",
     "Reading data: gels → ΔΔCt → RNA-seq FDR → clusters → spatial gradients",
     "Responsibility: evidence → risk → ethics → policy"],
    notes="Run as an oral review: students supply the example for each line.",
    takeaway="One coherent pipeline: build → deliver → measure → interpret → justify.")
add_slide("Cheat-sheet highlights — the exam's favorite traps",
    ["Dolly = cloning, not transgenesis · PAM is on the genomic side",
     "White colony = candidate, not proof · PCR counts ≠ correct-clone counts",
     "Statistics on ΔCt, not fold change · dropout ≠ absence",
     "Reporter = sufficiency; ISH = endogenous; perturbation = necessity",
     "Gradient (continuous) vs domain (bounded); sum digest fragments!"],
    diagram=None,
    notes="These twelve traps map to the cheat sheet's 'common exam mistakes' section.",
    takeaway="Most lost marks are category errors — fixable by terminology discipline.")
add_slide("Assessment map",
    ["50 MCQs (recall → evaluation) with explained key",
     "30 short · 20 long · 40 viva questions with model answers",
     "12 case-based + 10 data-interpretation questions",
     "9 labs with workbook keys · capstone project with rubric",
     "Everything cross-linked: labs ↔ modules ↔ datasets ↔ cheat sheet"],
    notes="Point instructors to BUILD_REPORT.md for counts and to the Answer Key for "
          "distribution of cognitive levels.",
    takeaway="Assessment mirrors the course: every tool tested in context.")

prs.save(os.path.join(BASE, "GMO_Cloning_Gene_Expression.pptx"))
print(f"Saved PPTX with {slide_count[0]} slides.")
