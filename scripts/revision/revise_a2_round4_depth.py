"""A2 Round 4: Fix theoretical gaps + reach 6,000-word minimum for JACR."""
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
    para.clear()
    para.add_run(full.replace(old_text, new_text))
    return True

doc = Document('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')

# ── A) Formal definition of "existential luxury" ─────────────────────────────
# Insert after Lipovetsky's four displacements paragraph
for para in doc.paragraphs:
    if 'four displacements defining hypermodern luxury: from object to experience' in para.text:
        insert_after(para, [
            'The term "existential luxury," as used throughout this article, requires formal '
            'definition. Existential luxury designates goods, experiences, and services whose '
            'premium positioning rests primarily on their capacity to constitute the consumer\'s '
            'sense of identity, biography, and temporal experience — rather than on material '
            'rarity or social display per se. The qualifier "existential" distinguishes this '
            'category from both traditional luxury (exclusive materials, craftsmanship, brand '
            'heritage as social signal) and the experience economy broadly: existential luxury '
            'specifically addresses the consumer\'s relationship to time, meaning, and self-'
            'continuity. It is luxury not in the sense of excess but in the sense of access to '
            'dimensions of experience the consumer apprehends as genuinely scarce — and whose '
            'scarcity cannot be resolved by additional purchasing power alone. A private island '
            'is expensive luxury; an afternoon of undivided attention from someone who matters '
            'is existential luxury. The distinction is not merely sociological. It generates '
            'predictions about which neural systems are primarily engaged, which memory traces '
            'are formed, and which competitive positions are most imitation-resistant.'
        ])
        print('✓ A) Existential luxury formally defined in section 2.1')
        break

# ── B) Scarcity heuristic vs costly signaling clarification ──────────────────
# Insert after the main scarcity heuristic paragraph in 3.1
for para in doc.paragraphs:
    if 'The scarcity heuristic, the tendency to attribute greater value to goods perceived' in para.text:
        insert_after(para, [
            'Two mechanisms are at work in the scarcity-value relationship, and the MPS model '
            'integrates both. The first is the scarcity heuristic proper: a within-individual '
            'cognitive shortcut in which rarity is used as a proxy for quality, operating at '
            'the level of the individual consumer\'s evaluation (Cialdini, 1984; Lynn, 1991). '
            'The second is costly signaling in the Zahavian sense: a between-individual '
            'signaling game in which the signal\'s value derives from its cost of imitation, '
            'operating at the level of social visibility and receiver inference (Zahavi, 1975; '
            'Grafen, 1990). These are conceptually distinct: a hermit consuming a rare good '
            'in private would experience the heuristic without the signal. A consumer '
            'displaying a common good in a context where others believe it to be rare would '
            'benefit from the signal without the heuristic. The MPS model is concerned '
            'primarily with the signaling dimension, because it is the devaluation of '
            'signals — not the devaluation of individual hedonic experiences — that drives '
            'the migration toward new scarcity dimensions. When D1 goods are counterfeited '
            'at scale, individual consumers may still value them hedonically; what changes is '
            'that others no longer reliably infer high cost from display, eroding the signal\'s '
            'social function.'
        ])
        print('✓ B) Scarcity heuristic vs costly signaling distinction added in 3.1')
        break

# ── C) Hyperbolic discounting tension resolution ──────────────────────────────
# Insert after the hyperbolic discounting paragraph in 3.3
for para in doc.paragraphs:
    if "Lipovetsky, by asserting that the luxury consumer wants to 'buy an eternalized moment'" in para.text:
        insert_after(para, [
            'A potential tension exists between hyperbolic discounting — the preference for '
            'present over future rewards — and the mnemonic dividend, which might appear to '
            'be a deferred benefit. The tension dissolves when one recognizes that episodic '
            'memory retrieval is a present experience, not a future one. The mnemonic dividend '
            'is not "happiness later" — it is "happiness now, triggered by the act of '
            'remembering." Each subsequent retrieval of an intense experience — elicited by a '
            'photograph, a scent, a conversation, a location that reinstates the original '
            'context — is itself a present hedonic event. Hyperbolic discounting penalizes '
            'promises of future pleasure; it does not penalize present experiences of memory. '
            'The consumer who chooses an extraordinary dinner over a material equivalent is '
            'not overriding their discount function; they are purchasing a present experience '
            'that will generate additional present experiences at low marginal cost for '
            'months or years. This is why the mnemonic dividend functions as a renewable '
            'present resource rather than a deferred payoff — and why it can simultaneously '
            'be consistent with hyperbolic discounting and generate long-run hedonic '
            'advantages over material purchases.'
        ])
        print('✓ C) Hyperbolic discounting tension resolved in 3.3')
        break

# ── D) Material goods' attenuated anticipatory dividend clarification ─────────
# Expand/add after the Triple Hedonic Dividend paragraph
for para in doc.paragraphs:
    if 'a mechanism I term here the Triple Hedonic Dividend' in para.text:
        insert_after(para, [
            'The claim that material goods generate an attenuated anticipatory dividend requires '
            'specification, since high-value material purchases — a luxury automobile, a piece '
            'of fine jewelry — plainly activate anticipatory dopaminergic systems. The '
            'attenuation is not about intensity at the moment of acquisition but about '
            'temporal structure: the anticipatory phase for material goods collapses rapidly '
            'upon acquisition. Once the good is owned, the anticipatory state terminates and '
            'hedonic adaptation begins immediately (Frederick & Loewenstein, 1999). '
            'Experiential goods maintain the anticipatory mode longer because their '
            'consumption is temporally distributed — a trip to Japan is anticipated throughout '
            'weeks of planning, and each planning stage generates its own NAcc activation — '
            'and because they cannot be fully "acquired" in advance: they remain accessible '
            'only at the moment of occurrence. The anticipatory dividend is therefore not '
            'merely larger for experiential goods; it is structurally richer, consisting of '
            'multiple anticipatory episodes rather than a single pre-acquisition peak. '
            'Kumar and Gilovich (2015) documented exactly this: the anticipatory phase for '
            'experiential purchases generates more positive affect, more social discussion, '
            'and greater contribution to reported life satisfaction than equivalent material '
            'anticipation — consistent with the hypothesis that anticipatory episodes '
            'themselves constitute part of the experiential purchase, not merely precursors to it.'
        ])
        print('✓ D) Triple Hedonic Dividend anticipatory attenuation clarified')
        break

# ── E) D4 vs D5 analytical distinction with counter-example ──────────────────
# Insert after the Dimension 6 development paragraph
for para in doc.paragraphs:
    if "You never actually own a Patek Philippe. You merely look after it" in para.text:
        insert_after(para, [
            'The analytical separability of the MPS dimensions merits attention, particularly '
            'for Dimensions 4 and 5, which frequently co-occur in practice. A product '
            'competes on Dimension 4 (authenticity scarcity) without competing on Dimension 5 '
            '(irreproducible experience) when its value derives from origin narrative rather '
            'than lived engagement: a single-origin olive oil whose terroir and harvest story '
            'add value even when consumption is a routine act, or a limited-edition print '
            'authenticated by provenance rather than by the singularity of viewing it. '
            'Conversely, a product competes on Dimension 5 without competing on Dimension 4 '
            'when the experience is unrepeatable but not authenticated by artisanal or heritage '
            'narrative: an improvised encounter with a street musician that becomes a '
            'biographical memory, or a spontaneous dinner conversation that reorients a '
            'relationship — neither of which any brand can claim or package. The Degoy case '
            'is strategically instructive precisely because it occupies both: D4 (each piece '
            'carries the signature of the same hands) and D5 (the encounter with the artisan '
            'during purchase cannot be reproduced). When D4 and D5 co-occur, they create the '
            'highest imitation-resistance in the MPS, because successfully replicating either '
            'dimension would require dismantling what makes the other possible. A brand that '
            'scales to machine production (losing D4) simultaneously loses the conditions for '
            'the singular experience (D5). The two dimensions are co-constitutive at high '
            'competitive intensity, even if they are analytically separable.'
        ])
        print('✓ E) D4 vs D5 analytical distinction added in 6.1')
        break

# ── F) P2 logical problem resolution ─────────────────────────────────────────
# Insert after P2 paragraph
for para in doc.paragraphs:
    if 'P2 (Orbitofrontal Value Encoding Proposition)' in para.text:
        insert_after(para, [
            'P2 rests on a distinction the Plassmann et al. (2007) paradigm establishes but '
            'does not fully exploit: the difference between price-driven OFC activation and '
            'meaning-driven OFC activation. In Plassmann\'s wine study, the same liquid '
            'generated higher OFC activation when labeled at a higher price — demonstrating '
            'that contextual pricing signals reach the subjective value computation. Dimension '
            '1 goods leverage this mechanism maximally through high sticker prices. The '
            'prediction in P2 is that Dimensions 3–5 generate a distinct mode of OFC '
            'activation: one that operates through narrative richness, irreplicability, and '
            'the impossibility of direct price comparison — features that resist the '
            'downward valuation that competition produces for D1 goods. The testable '
            'implication of this distinction is that presenting D3-5 goods without explicit '
            'price information should reduce OFC activation and willingness-to-pay less '
            'than removing price information from equivalent D1 goods, since D3-5 value '
            'partially resides in features whose scarcity is legible without price as a proxy. '
            'Price for D1 is the primary signal; for D3-5, price is one among several '
            'redundant signals, each reinforcing the others.'
        ])
        print('✓ F) P2 OFC mechanism distinction added')
        break

# ── G) P4 precarity tension resolved ─────────────────────────────────────────
# Insert after P4 paragraph
for para in doc.paragraphs:
    if 'P4 (Segment Stratification Proposition)' in para.text:
        insert_after(para, [
            'P4 requires clarification about the mechanism connecting economic precarity to '
            'D1 preference, since genuinely precarious consumers typically cannot afford '
            'canonical D1 goods (the very goods whose cost makes them reliable status '
            'signals). The resolution lies in the concept of aspirational D1 positioning: '
            'precarious consumers allocate discretionary income to accessible D1 '
            'approximations — entry-level items from aspirational brands, carefully selected '
            'pieces that anchor social positioning — because even partial D1 display '
            'generates more immediate social recognition in networks where material '
            'signaling is the dominant legibility code. A dinner at a Michelin-starred '
            'restaurant (D5) generates less social recognition in a network whose members '
            'cannot interpret experiential capital or whose status grammar is written '
            'primarily in possessions. This implies a network-level moderator for P4: '
            'the effect will be strongest in socially closed networks with high D1 '
            'literacy, weaker in networks where experiential capital circulates '
            'as a recognized form of status — consistent with Bourdieu\'s (1984) '
            'observation that the dominant class tends to use cultural and experiential '
            'distinctions precisely to exclude forms of capital that new money can easily '
            'acquire.'
        ])
        print('✓ G) P4 precarity mechanism resolved with Bourdieu grounding')
        break

# ── Add Bourdieu (1984) and Frederick & Loewenstein (1999) references ─────────
# Find REFERENCES and add after (they'll be re-sorted on next pass if needed)
refs_para = None
for para in doc.paragraphs:
    if para.text.strip() == 'REFERENCES':
        refs_para = para
        break

if refs_para:
    insert_after(refs_para, [
        'Bourdieu, P. (1984). Distinction: A social critique of the judgement of taste. '
        'Harvard University Press. (Original work published 1979)',
        'Frederick, S., & Loewenstein, G. (1999). Hedonic adaptation. In D. Kahneman, '
        'E. Diener, & N. Schwarz (Eds.), Well-being: The foundations of hedonic '
        'psychology (pp. 302-329). Russell Sage Foundation.',
    ])
    print('✓ Bourdieu (1984) and Frederick & Loewenstein (1999) added to references')

doc.save('/home/user/chapsanalytics/articles/A2_Scarcity_humanizado.docx')
print('✓ A2 round 4 (depth) saved.')
