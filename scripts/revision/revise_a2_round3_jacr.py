"""A2 Round 3: JACR formatting compliance + reference fixes + voice + content depth."""
from docx import Document
from docx.oxml import OxmlElement

def make_para(text):
    new_p = OxmlElement('w:p')
    new_r = OxmlElement('w:r')
    new_t = OxmlElement('w:t')
    new_t.text = text
    new_t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    new_r.append(new_t)
    new_p.append(new_r)
    return new_p

def insert_after(anchor_para, texts):
    current = anchor_para._p
    for text in texts:
        new_p = make_para(text)
        current.addnext(new_p)
        current = new_p

def replace_in_para(para, old_text, new_text):
    if old_text not in para.text:
        return False
    full = para.text
    for run in para.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)
            return True
    # Text spans multiple runs — rebuild
    para.clear()
    para.add_run(full.replace(old_text, new_text))
    return True

doc = Document('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')

# ── 1. KEYWORDS: trim from 8 to 6 ────────────────────────────────────────────
for para in doc.paragraphs:
    if para.text.startswith('Keywords:') and 'orbitofrontal cortex' in para.text:
        replace_in_para(para,
            'Keywords: hypermodern luxury; scarcity heuristic; evolutionary psychology; '
            'consumer neuroscience; existential experience; costly signaling; perceived scarcity; orbitofrontal cortex.',
            'Keywords: hypermodern luxury; scarcity heuristic; evolutionary psychology; '
            'consumer neuroscience; existential experience; costly signaling.'
        )
        print('✓ Keywords trimmed to 6')
        break

# ── 2. MOVE DECLARATIONS to Acknowledgements (before References) ──────────────
# Find and remove declaration paragraphs from current position (before Introduction)
decl_ai_heading = decl_ai_text = decl_funding = decl_coi = None
for para in doc.paragraphs:
    t = para.text.strip()
    if t == 'Declaration of AI Use':
        decl_ai_heading = para
    elif t.startswith('AI-assisted tools were used during the preparation'):
        decl_ai_text = para
    elif t.startswith('Funding Declaration:'):
        decl_funding = para
    elif t.startswith('Declaration of Competing Interests:'):
        decl_coi = para

if all([decl_ai_heading, decl_ai_text, decl_funding, decl_coi]):
    # Store the text before removing
    ai_heading_text = decl_ai_heading.text
    ai_body_text = decl_ai_text.text
    funding_text = decl_funding.text
    coi_text = decl_coi.text
    # Remove from current location
    for para in [decl_ai_heading, decl_ai_text, decl_funding, decl_coi]:
        para._p.getparent().remove(para._p)
    print('✓ Declarations removed from pre-Introduction position')
else:
    print('WARNING: could not find all declaration paragraphs')
    ai_heading_text = 'Declaration of AI Use'
    ai_body_text = 'AI-assisted tools were used during the preparation of this manuscript to support language revision and structural organization. All intellectual content, theoretical arguments, conceptual contributions, and conclusions are original and remain the exclusive responsibility of the author.'
    funding_text = 'Funding: This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.'
    coi_text = 'Conflict of Interest: The author declares no competing financial or non-financial interests.'

# ── 3. ADD ACKNOWLEDGEMENTS SECTION before REFERENCES ────────────────────────
references_para = None
for para in doc.paragraphs:
    if para.text.strip() == 'REFERENCES':
        references_para = para
        break

if references_para:
    ack_texts = [
        'ACKNOWLEDGEMENTS',
        ai_heading_text,
        ai_body_text,
        funding_text,
        coi_text,
    ]
    # Insert in forward order before References
    for text in ack_texts:
        new_p = make_para(text)
        references_para._p.addprevious(new_p)
    print('✓ Acknowledgements section added before References')

# ── 4. FIX REFERENCE CITATIONS IN BODY ───────────────────────────────────────

# Fix Baudrillard: "(1981, 1983)" → "(1981)" (1983 work not in references)
for para in doc.paragraphs:
    if 'Baudrillard (1981, 1983)' in para.text:
        replace_in_para(para, 'Baudrillard (1981, 1983)', 'Baudrillard (1981)')
        print('✓ Baudrillard citation fixed')

# Fix Kivetz: "(2002, 2007)" → "(2002)" (2007 work not in references)
for para in doc.paragraphs:
    if 'Kivetz and Simonson (2002, 2007)' in para.text:
        replace_in_para(para, 'Kivetz and Simonson (2002, 2007)', 'Kivetz and Simonson (2002)')
        print('✓ Kivetz citation fixed')

# ── 5. VOICE FIXES ────────────────────────────────────────────────────────────

# Fix 1: "The strategic implication of this finding deserves explicit statement."
for para in doc.paragraphs:
    if 'The strategic implication of this finding deserves explicit statement.' in para.text:
        replace_in_para(para,
            'The strategic implication of this finding deserves explicit statement. If the OFC encodes',
            'What this finding implies for luxury pricing is rarely stated so directly. If the OFC encodes'
        )
        print('✓ OFC voice fix applied')
        break

# Fix 2: "what this article proposes to call the Triple Hedonic Dividend"
for para in doc.paragraphs:
    if 'what this article proposes to call the Triple Hedonic Dividend' in para.text:
        replace_in_para(para,
            'what this article proposes to call the Triple Hedonic Dividend',
            'a mechanism I term here the Triple Hedonic Dividend'
        )
        print('✓ Triple Hedonic Dividend voice fix applied')
        break

# Fix 3: Dimension listing in 6.1 — add connecting sentence between D5 and D6
for para in doc.paragraphs:
    if 'Dimension 5, irreproducible experience scarcity, describes goods providing a lived experience' in para.text:
        replace_in_para(para,
            'Dimension 6, transgenerational symbolic capital scarcity, describes goods carrying legacy value.',
            'Dimension 6, transgenerational symbolic capital scarcity, describes goods that carry value '
            'across generations — objects that are custodied rather than consumed, whose scarcity derives '
            'from historical accumulation and irreversibility of time.'
        )
        print('✓ Dimension 6 description improved in 6.1')
        break

# ── 6. CONTENT: Pine & Gilmore in section 2.1 ────────────────────────────────
for para in doc.paragraphs:
    if "The sociological description is accurate. But it does not explain the mechanism." in para.text:
        insert_after(para, [
            'The broader economic trajectory anticipated this shift. Pine and Gilmore (1999) argued that '
            'advanced economies had entered an "experience economy" in which consumers progressively seek '
            'staged, memorable events over goods and services — value that exists in the time of '
            'engagement, not in physical possession. Their observation was economic and phenomenological. '
            'What remained unspecified was the psychological and neurobiological mechanism that makes '
            'experiences intrinsically more valuable than goods for consumers operating in conditions of '
            'material abundance. The present article addresses that specification.'
        ])
        print('✓ Pine & Gilmore paragraph added in section 2.1')
        break

# ── 7. CONTENT: Hirschman & Holbrook citation in section 4 ───────────────────
# Add citation in the Triple Hedonic Dividend paragraph where we discuss hedonic value
for para in doc.paragraphs:
    if 'a mechanism I term here the Triple Hedonic Dividend' in para.text:
        replace_in_para(para,
            'a mechanism I term here the Triple Hedonic Dividend of experiential luxury.',
            'a mechanism I term here the Triple Hedonic Dividend of experiential luxury — '
            'building on Hirschman and Holbrook\'s (1982) foundational characterization of '
            'hedonic consumption as multisensory, fantasy-driven, and emotionally absorptive '
            'rather than functional in character.'
        )
        print('✓ Hirschman & Holbrook cited in body')
        break

# ── 8. CONTENT: Dimension 6 development paragraph ────────────────────────────
# After the MPS dimensions description paragraph, add Dimension 6 development
for para in doc.paragraphs:
    if 'transgenerational symbolic capital scarcity, describes goods that carry value' in para.text:
        insert_after(para, [
            'Dimension 6 occupies a structurally distinct position from the other five. Whereas '
            'Dimensions 1 through 5 operate primarily through the individual consumer\'s direct '
            'experience — of ownership, time, attention, authenticity, and lived event — Dimension 6 '
            'involves goods that serve as carriers of cultural and familial identity across generations. '
            'A Patek Philippe timepiece passed from parent to child, Japanese urushi lacquerware '
            'maintained across a century, a cellar assembled for a grandchild\'s wedding: these objects '
            'are not consumed; they are custodied. The OFC encodes their value not through direct '
            'sensory pleasure but through the narrative of stewardship — the owner derives present '
            'satisfaction from the story of caring for something that will outlast them. This '
            'mechanism is particularly potent in high-inequality contexts where multigenerational '
            'wealth is being actively constructed and in collectivist cultures where identity is '
            'constituted relationally across generations rather than individually within a lifetime. '
            'Dimension 6 is also the most imitation-resistant dimension in the MPS: genuine '
            'transgenerational capital requires the irreversible passage of time, which no amount '
            'of expenditure can replicate. The Patek Philippe campaign slogan — "You never actually '
            'own a Patek Philippe. You merely look after it for the next generation" — is, in MPS '
            'terms, a precise statement of the Dimension 6 value proposition.'
        ])
        print('✓ Dimension 6 development paragraph added')
        break

# ── 9. CONTENT: Expand P3 with methodological note ───────────────────────────
for para in doc.paragraphs:
    if 'P3 (Mnemonic Dividend Proposition)' in para.text:
        insert_after(para, [
            'The longitudinal structure of P3 carries a methodological implication: designs with a '
            'single post-purchase measurement systematically underestimate the mnemonic dividend, '
            'since rose-colored reminiscence operates progressively over months and years. Studies '
            'testing P3 require at minimum two follow-up waves — at approximately twelve and '
            'twenty-four months — and ideally ecological momentary assessment of spontaneous '
            'memory retrieval between waves, since frequency of unprompted recall is itself a '
            'component of the mnemonic dividend that retrospective surveys miss.'
        ])
        print('✓ P3 methodological note added')
        break

# ── 10. CONTENT: Methods note in Concluding Remarks ─────────────────────────
for para in doc.paragraphs:
    if 'The limitations of this article are relevant.' in para.text:
        insert_after(para, [
            'Testing the MPS propositions will require a portfolio of methods, since no single '
            'methodology captures all five dimensions simultaneously. P1 is suited to conjoint '
            'analysis and discrete choice experiments. P2 requires functional neuroimaging — '
            'preferably fMRI in naturalistic purchase simulation tasks — combined with psychophysiological '
            'measures for ecological validity. P3 is best tested by longitudinal survey with ecological '
            'momentary assessment components. P4 and P5 require nationally representative samples '
            'with segment stratification by income level, income uncertainty, and cultural context. '
            'For Brazil specifically, the stratification documented at SPIW 2026 (ultra-high, premium, '
            'aspirational) suggests that any nationally representative MPS study must oversample '
            'the ultra-high segment, which is demographically small but theoretically central to '
            'understanding Dimension 5 dynamics.'
        ])
        print('✓ Methods note added to conclusions')
        break

# ── 11. ADD MISSING REFERENCES ────────────────────────────────────────────────
new_refs = [
    'Lipovetsky, G. (1987). L\'Empire de l\'éphémère: La mode et son destin dans les sociétés modernes. Gallimard.',
    'Lipovetsky, G. (2007). Le bonheur paradoxal: Essai sur la société d\'hyperconsommation. Gallimard.',
    'Pine, B. J., & Gilmore, J. H. (1999). The experience economy: Work is theatre and every business a stage. Harvard Business School Press.',
]

for para in doc.paragraphs:
    if para.text.strip() == 'REFERENCES':
        insert_after(para, new_refs)
        print('✓ Missing references added')
        break

# Also remove Hirschman & Holbrook from references if it had no page numbers
# (it's now cited in body so we can keep it — just make sure it stays)

doc.save('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')
print('✓ A2 round 3 (JACR) saved.')
