"""Revision of A2 (Scarcity Heuristic) — addressing critical review findings."""
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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

def insert_before(anchor_para, texts):
    for text in reversed(texts):
        new_p = make_para(text)
        anchor_para._p.addprevious(new_p)

doc = Document('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')

# ── FIX 1: Shorten Abstract ──────────────────────────────────────────────────
# Original abstract is ~165 words — trim to under 150
SHORT_ABSTRACT = (
    "Lipovetsky's hypermodern luxury thesis describes the transition from luxury as social "
    "display to luxury as existential experience. This article provides the explanatory "
    "substrate that sociology alone cannot supply: why this transition occurred. The central "
    "argument is that the migration from material to experiential luxury is a predictable "
    "adaptive response by a brain evolutionarily calibrated for scarcity, now operating in "
    "unprecedented material abundance. When imitation of possession signals becomes cheap, "
    "the mesolimbic dopaminergic system and orbitofrontal cortex shift toward genuinely "
    "scarce goods: time, qualified attention, authenticity, and irreproducible experiences. "
    "Integrating costly signaling theory, consumer neuroscience, and the philosophy of value, "
    "the article proposes the Multidimensional Perceived Scarcity (MPS) model and derives "
    "five testable propositions for luxury positioning research."
)

for para in doc.paragraphs:
    if para.text.strip().startswith("Lipovetsky's hypermodern luxury thesis describes"):
        # Replace the abstract text
        for run in para.runs:
            run.text = ''
        if para.runs:
            para.runs[0].text = SHORT_ABSTRACT
        else:
            para.add_run(SHORT_ABSTRACT)
        break

# ── FIX 2: Ethical Declarations ──────────────────────────────────────────────
# Add Funding and Conflict of Interest after AI Declaration block
for para in doc.paragraphs:
    if 'All intellectual content, theoretical arguments' in para.text:
        insert_after(para, [
            'Funding Declaration: This research received no specific grant from any '
            'funding agency in the public, commercial, or not-for-profit sectors.',
            'Declaration of Competing Interests: The author declares no competing '
            'financial or non-financial interests.',
        ])
        break

# ── ADDITION 1: Luxury Branding Literature in Section 2.1 ────────────────────
# After the paragraph ending "It does not explain why the brain responds to..."
for para in doc.paragraphs:
    if 'It does not explain why the brain responds to experiential scarcity' in para.text:
        insert_after(para, [
            'The luxury branding literature has mapped the constituent dimensions of luxury '
            'perception without explaining their neural origins. Vigneron and Johnson (1999) '
            'identified five luxury values that structure prestige-seeking consumption: '
            'conspicuousness (Veblen effect), uniqueness (snob effect), bandwagon adherence, '
            'hedonic value, and perfectionist quality perception. Berthon, Pitt, Parent, and '
            'Berthon (2009) observed that luxury brands balance three forces — functional, '
            'expressive, and aesthetic — and that the weight assigned to each varies by '
            'segment and cultural context. Ko, Costello, and Taylor (2019), in a systematic '
            'review of luxury consumption, identified perceived premium quality, justifiable '
            'price premium, exclusive image, authentic craft, and aspirational appeal as the '
            'defining characteristics of luxury from a consumer perspective. What this '
            'literature has not provided is the evolutionary and neurobiological explanation '
            'for why these specific characteristics activate luxury perception with the '
            'intensity they do — and why their relative salience shifts as material abundance '
            'increases. The MPS model addresses this explanatory gap.'
        ])
        break

# ── ADDITION 2: Belk + Tian in Section 3.1 ───────────────────────────────────
# After "The scarcity heuristic...is a robust adaptive mechanism..."
for para in doc.paragraphs:
    if 'The scarcity heuristic, the tendency to attribute greater value' in para.text:
        insert_after(para, [
            'The relevance of scarcity to self-constitution has deep roots in consumer '
            'research. Belk (1988), in his foundational analysis of possessions as '
            'extensions of the self, established that consumers use what they acquire and '
            'consume to define, situate, and extend their identities in the social world — '
            'making acquisition inherently an identity act. This implies that when possession '
            'signals become reproducible at low cost, the identity function of acquisition '
            'must migrate toward signals whose cost of imitation remains genuinely high. '
            'Tian, Bearden, and Hunter (2001) provided the motivational link: consumers '
            'with high need for uniqueness actively seek products and experiences that '
            'differentiate them from others, preferring goods with low availability and '
            'high distinctiveness. The scarcity heuristic, in this framework, is not merely '
            'a cognitive bias but a motivated social strategy: the brain does not simply '
            'overvalue scarce goods — it uses scarcity as a proxy for the identity '
            'differentiation value that the extended self (Belk, 1988) requires.'
        ])
        break

# ── ADDITION 3: Carter & Gilovich as Counterpoint in Section 4.3 ─────────────
# After "Van Boven and Gilovich (2003) empirically demonstrated..."
for para in doc.paragraphs:
    if 'Memories of experiences become progressively more positive' in para.text:
        insert_after(para, [
            'This experiential advantage has been further specified by Carter and Gilovich '
            '(2012), who demonstrated that the differential satisfaction from experiences '
            'versus possessions is partly mediated by the centrality of each to self-concept: '
            'people more strongly identify with their experiential choices than their material '
            'purchases, and this identity centrality predicts both anticipatory pleasure and '
            'retrospective satisfaction. For the MPS model, this finding is consequential: '
            'MPS Dimensions 4 and 5 (authenticity and irreproducible experience) generate '
            'high identity centrality because they cannot be delegated, replicated, or '
            'substituted — making them particularly robust scarcity signals in the '
            'context of Belk\'s extended self.'
        ])
        break

# ── ADDITION 4: Formal Propositions Section in Section 6 ─────────────────────
# Insert before "7. CONCLUDING REMARKS"
propositions = [
    '6.4 Formal Propositions',
    'The MPS model generates five testable propositions that structure the empirical '
    'research agenda for luxury positioning in contexts of material abundance. These '
    'propositions derive directly from the integration of costly signaling theory, '
    'consumer neuroscience, and the MPS dimensional framework.',
    'P1 (Signal Migration Proposition): As the replicability of material status signals '
    'increases within a given consumer market segment, the mean preference weight '
    'assigned to MPS Dimensions 2–5 will increase relative to Dimension 1, controlling '
    'for income level, cultural context, and cohort effects. Operationalization: '
    'conjoint analysis comparing willingness-to-pay for goods competing on each '
    'MPS dimension, across market segments differing in signal replicability.',
    'P2 (Orbitofrontal Value Encoding Proposition): Goods competing on MPS Dimensions '
    '3–5 (genuine attention, authenticity, irreproducible experience) will generate '
    'higher orbitofrontal cortex activation and greater willingness-to-pay premiums '
    'than materially equivalent goods competing on Dimension 1, as measured by '
    'neuroimaging during simulated purchase decisions (following Plassmann et al., 2007). '
    'This effect will be stronger for consumers with higher need for uniqueness '
    '(Tian et al., 2001).',
    'P3 (Mnemonic Dividend Proposition): Consumers will report higher retrospective '
    'satisfaction for goods competing on MPS Dimension 5 (irreproducible experience) '
    'than for goods competing on Dimension 1, and this advantage will increase over '
    'time (twelve and twenty-four months post-purchase), consistent with rose-colored '
    'reminiscence (Van Boven & Gilovich, 2003) and the episodic memory consolidation '
    'mechanisms described by Schacter (1996, 2001).',
    'P4 (Segment Stratification Proposition): The relative activation weight of MPS '
    'Dimensions 2–5 versus Dimension 1 will be positively associated with income level '
    'and negatively associated with income uncertainty: consumers facing economic '
    'precarity will exhibit stronger preference for Dimension 1 even when controlling '
    'for absolute income, because Dimension 1 signals — material possessions — '
    'remain the most legible status markers in their immediate social networks.',
    'P5 (Cultural Adaptation Proposition): The rank ordering of MPS dimensions will '
    'vary significantly across national cultural contexts. Collectivist cultures will '
    'assign higher weight to Dimension 6 (transgenerational symbolic capital) relative '
    'to individualist cultures, which will assign higher weight to Dimensions 2 and 3 '
    '(time and attention scarcity). The Brazilian context, characterized by active '
    'stratification across segments (ultra-high, premium, aspirational, as documented '
    'at SPIW 2026), requires specific adaptation of dimension weighting by socioeconomic '
    'segment rather than a single national profile.',
]

for para in doc.paragraphs:
    if para.text.strip().startswith('7. CONCLUDING REMARKS') or \
       para.text.strip().startswith('CONCLUDING REMARKS'):
        insert_before(para, propositions)
        break

# ── ADDITION 5: Expand Concluding Remarks with business implications ──────────
# Add after the penultimate paragraph of conclusions
for para in doc.paragraphs:
    if 'The limitations of this article are relevant' in para.text:
        insert_after(para, [
            'Beyond theoretical implications, the MPS model generates specific prescriptions '
            'for luxury brand strategy. Brands operating on Dimension 1 must invest in '
            'access rituals that maintain perception of exclusivity even as distribution '
            'widens. Brands operating on Dimensions 3–5 must resist scalability pressures '
            'that would erode the genuine scarcity that constitutes their value. The '
            'diagnostic power of the MPS emerges precisely in repositioning decisions: '
            'when a brand loses value, the appropriate question is not "how do we '
            'communicate better?" but "on which MPS dimension are we no longer scarce?" '
            'The answer determines the strategic response — and, as the cases of Netflix '
            'and Degoy illustrate, the most defensible competitive positions are those '
            'built on dimensions whose imitation cost remains structurally high.'
        ])
        break

# ── NEW REFERENCES ────────────────────────────────────────────────────────────
new_refs = [
    'Belk, R. W. (1988). Possessions and the extended self. Journal of Consumer Research, '
    '15(2), 139-168. https://doi.org/10.1086/209154',
    'Berthon, P., Pitt, L., Parent, M., & Berthon, J.-P. (2009). Aesthetics and '
    'ephemerality: Observing and preserving the luxury brand. California Management '
    'Review, 52(1), 45-66. https://doi.org/10.1525/cmr.2009.52.1.45',
    'Carter, T. J., & Gilovich, T. (2012). I am what I do, not what I have: The '
    'differential centrality of experiential and material purchases to the self. '
    'Journal of Personality and Social Psychology, 102(6), 1304-1317. '
    'https://doi.org/10.1037/a0027407',
    'Hirschman, E. C., & Holbrook, M. B. (1982). Hedonic consumption: Emerging '
    'concepts, methods and propositions. Journal of Marketing, 46(3), 92-101. '
    'https://doi.org/10.1177/002224298204600314',
    'Ko, E., Costello, J. P., & Taylor, C. R. (2019). What is a luxury? A consumer '
    'perspective. Journal of Business Research, 99, 120-129. '
    'https://doi.org/10.1016/j.jbusres.2017.08.029',
    'Tian, K. T., Bearden, W. O., & Hunter, G. L. (2001). Consumers\' need for '
    'uniqueness: Scale development and validation. Journal of Consumer Research, '
    '28(1), 50-66. https://doi.org/10.1086/321947',
    'Vigneron, F., & Johnson, L. W. (1999). A review and a conceptual framework of '
    'prestige-seeking consumer behavior. Academy of Marketing Science Review, 1(1), 1-15.',
]

for para in doc.paragraphs:
    if para.text.strip() == 'REFERENCES':
        insert_after(para, new_refs)
        break

doc.save('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')
print('✓ A2 revision saved.')
