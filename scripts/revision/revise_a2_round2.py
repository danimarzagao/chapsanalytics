"""A2 Round 2: structural fix + deepen 3 key arguments."""
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

doc = Document('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')

# ── STRUCTURAL FIX: reorder propositions section ──────────────────────────────
# Current wrong order: P5, P4, P3, P2, P1, intro, "6.4 Formal Propositions", CONCLUDING REMARKS
# Target order:        "6.4 Formal Propositions", intro, P1, P2, P3, P4, P5, CONCLUDING REMARKS

heading_p = intro_p = p1 = p2 = p3 = p4 = p5 = anchor_p = None
for para in doc.paragraphs:
    t = para.text.strip()
    if t == '6.4 Formal Propositions':
        heading_p = para
    elif t.startswith('The MPS model generates five testable propositions'):
        intro_p = para
    elif t.startswith('P1 (Signal Migration Proposition)'):
        p1 = para
    elif t.startswith('P2 (Orbitofrontal Value Encoding Proposition)'):
        p2 = para
    elif t.startswith('P3 (Mnemonic Dividend Proposition)'):
        p3 = para
    elif t.startswith('P4 (Segment Stratification Proposition)'):
        p4 = para
    elif t.startswith('P5 (Cultural Adaptation Proposition)'):
        p5 = para
    elif t.startswith('7. CONCLUDING REMARKS') or t == 'CONCLUDING REMARKS':
        anchor_p = para

if all([heading_p, intro_p, p1, p2, p3, p4, p5, anchor_p]):
    ordered = [heading_p, intro_p, p1, p2, p3, p4, p5]
    elems = [p._p for p in ordered]
    for e in elems:
        e.getparent().remove(e)
    for e in elems:
        anchor_p._p.addprevious(e)
    print('✓ A2 propositions reordered')
else:
    missing = [name for name, v in [('heading', heading_p), ('intro', intro_p),
               ('p1', p1), ('p2', p2), ('p3', p3), ('p4', p4), ('p5', p5),
               ('anchor', anchor_p)] if v is None]
    print(f'WARNING: could not find: {missing}')

# ── EXPANSION 1: Price changes neurophysiology (after OFC implications para) ──
for para in doc.paragraphs:
    if 'particularly sensitive to dimensions of value that are difficult to monetize' in para.text:
        insert_after(para, [
            'The strategic implication of this finding deserves explicit statement. If the OFC encodes '
            'subjective value in a way that incorporates the price signal as contextual information, '
            'then discounting a luxury experience does not merely communicate that it is "less '
            'luxurious" — it literally diminishes the pleasurable experience the OFC generates. The '
            'hedonic quality of a restaurant meal, a spa treatment, or a premium hospitality experience '
            'is neurophysiologically reduced by a discount, even holding constant all other parameters '
            'of the experience. This is not irrational consumer behavior: it is the OFC performing '
            'exactly the function it evolved for, integrating all available contextual signals — '
            'including price — into a unified subjective value estimate. Brands that discount luxury '
            'experiences are not simply repositioning — they are performing a neurobiological '
            'intervention that reduces the actual experiential quality of what they sell. For products '
            'competing on MPS Dimension 5 (irreproducible experience), the pricing architecture is '
            'not separable from the experiential content: the price paid is part of what the OFC '
            'registers as the experience.'
        ])
        break

# ── EXPANSION 2: Triple Hedonic Dividend (after Carter & Gilovich para) ───────
for para in doc.paragraphs:
    if 'identity centrality predicts both anticipatory pleasure and retrospective satisfaction' in para.text:
        insert_after(para, [
            'The three neuroscientific mechanisms reviewed in this section converge into what this '
            'article proposes to call the Triple Hedonic Dividend of experiential luxury. The first '
            'dividend is anticipatory: nucleus accumbens activation generates dopaminergic pleasure '
            'before the experience occurs (Knutson et al., 2001, 2007). The second is experiential: '
            'OFC activation encodes subjective value as the experience unfolds, incorporating '
            'emotional, sensory, and contextual signals — including price — into a unified value '
            'representation (Plassmann et al., 2007). The third is mnemonic: episodic memory '
            'consolidation preferentially preserves emotionally intense and contextually distinctive '
            'events, and rose-colored reminiscence progressively enhances retrospective valuation '
            'over time (Schacter, 1996, 2001; Van Boven & Gilovich, 2003). Material goods generate '
            'predominantly the second dividend with attenuated first and third. Goods competing on '
            'MPS Dimensions 4 and 5 — authenticity and irreproducible experience — generate all '
            'three, with the third dividend accumulating over years after the experience has ended. '
            'This asymmetry in dividend structure is the core mechanistic explanation for why '
            'experiential luxury generates higher lifetime satisfaction than material luxury of '
            'equivalent nominal cost: the experiential good continues to generate hedonic value '
            'through memory long after the material good has been assimilated into the background '
            'of ownership.'
        ])
        break

# ── EXPANSION 3: Baudrillard strategic resolution (after Baudrillardian tension para) ──
for para in doc.paragraphs:
    if 'The Baudrillardian tension does not invalidate the neurological argument' in para.text:
        insert_after(para, [
            'This tension has a strategic resolution that Baudrillard\'s framework, focused on '
            'critique, does not supply. The impossibility of verifying absolute interiority in the '
            'abstract does not prevent brands from creating the conditions under which genuine '
            'interiority accumulates. Brands that survive the Baudrillardian critique are those '
            'that generate experiences that become part of the consumer\'s autobiography — not '
            'simulations of authentic experience, but occasions for the actual formation of '
            'biographical memory. A wine tour that produces a story told for twenty years, a hotel '
            'room associated with a decisive life choice, a travel experience tied to a relationship '
            'that was formed or transformed — these are not hyperreal simulations of authenticity. '
            'They are genuine autobiographical events. The MPS framework suggests that brands '
            'competing on Dimension 5 succeed not by claiming authenticity as a brand attribute but '
            'by designing experiences with the structural features — emotional intensity, contextual '
            'distinctiveness, narrative coherence — that Schacter\'s episodic memory consolidation '
            'preferentially preserves. Authenticity, in this account, is an outcome of memory, not '
            'a property of the experience at the moment of occurrence. The Baudrillardian trap '
            'remains open for brands that perform authenticity; it closes for brands that engineer '
            'the conditions for autobiographical accumulation.'
        ])
        break

doc.save('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')
print('✓ A2 round 2 saved.')
