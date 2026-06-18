"""A1 Round 2: structural fix + deepen 3 key arguments."""
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

doc = Document('/home/user/chapsanalytics/articles/A1_DIP_humanizado.docx')

# ── STRUCTURAL FIX: reorder propositions section ──────────────────────────────
# Current wrong order: P4, P3, P2, P1, intro, heading, CONSIDERAÇÕES FINAIS
# Target order:        heading, intro, P1, P2, P3, P4, CONSIDERAÇÕES FINAIS

heading_p = intro_p = p1 = p2 = p3 = p4 = anchor_p = None
for para in doc.paragraphs:
    t = para.text.strip()
    if t == '5.4 PROPOSIÇÕES TEÓRICAS':
        heading_p = para
    elif t.startswith('O framework da DIP gera quatro proposições'):
        intro_p = para
    elif t.startswith('P1 (Proposição da Proporcionalidade)'):
        p1 = para
    elif t.startswith('P2 (Proposição da Erosão Neurocognitiva)'):
        p2 = para
    elif t.startswith('P3 (Proposição da Mediação da Saúde Mental)'):
        p3 = para
    elif t.startswith('P4 (Proposição do Design Moderador)'):
        p4 = para
    elif t.startswith('6. CONSIDERAÇÕES FINAIS'):
        anchor_p = para

if all([heading_p, intro_p, p1, p2, p3, p4, anchor_p]):
    ordered = [heading_p, intro_p, p1, p2, p3, p4]
    elems = [p._p for p in ordered]
    # Remove all from document
    for e in elems:
        e.getparent().remove(e)
    # Reinsert in correct order before anchor (iterate forward, not reversed)
    for e in elems:
        anchor_p._p.addprevious(e)
    print('✓ A1 propositions reordered')
else:
    missing = [name for name, v in [('heading', heading_p), ('intro', intro_p),
               ('p1', p1), ('p2', p2), ('p3', p3), ('p4', p4), ('anchor', anchor_p)] if v is None]
    print(f'WARNING: could not find: {missing}')

# ── EXPANSION 1: idem/ipse dissociation → after "A DIP corrói esse processo" ─
for para in doc.paragraphs:
    if 'Exige eventos nos quais o sujeito foi agente, não apenas espectador ou aprovador' in para.text:
        insert_after(para, [
            'O refinamento da formulação ricoeuriana para o contexto da DIP permite nomear o fenômeno '
            'com maior precisão: o que a DIP produz não é a destruição da identidade profissional como '
            'um todo, mas a dissociação entre idem e ipse. O título permanece. O currículo cresce. A '
            'reputação pode até se expandir. O que se dissolve são os atos de ipse que deveriam '
            'constituir o correlato experiencial dessa identidade. O sujeito continua sendo chamado de '
            '"médico", "advogado", "analista" — as categorias sociais do idem se mantêm intactas — '
            'mas a espessura de ipse que tornaria essa identidade psicologicamente sustentável foi '
            'progressivamente esvaziada. O resultado é o que se pode nomear de identidade de concha: '
            'socialmente legível, internamente oca. O sujeito que opera em identidade de concha pode '
            'tardar anos a reconhecer o esvaziamento — precisamente porque os indicadores sociais de '
            'identidade (título, cargo, reconhecimento) continuam funcionando. O aprovador, não autor, '
            'é o retrato funcional dessa condição: ele existe socialmente mas não existe historicamente — '
            'porque não tem atos de ipse para narrar.'
        ])
        break

# ── EXPANSION 2: Hegel reversal → after Hegel paragraph ──────────────────────
for para in doc.paragraphs:
    if 'dialética hegeliana do senhor e do escravo' in para.text and 'autoconsciência' in para.text:
        insert_after(para, [
            'A inversão especular que a DIP produz em relação ao argumento hegeliano merece ser '
            'nomeada. Na dialética original, é o escravo — aquele que trabalha, transforma a matéria, '
            'enfrenta a resistência do mundo concreto — que desenvolve autoconsciência, enquanto o '
            'senhor, que apenas consome o resultado do trabalho alheio, permanece estagnado em seu '
            'desenvolvimento subjetivo. A DIP conduz o profissional progressivamente à posição do '
            'senhor hegeliano: ele aprova, delega, consome outputs — mas não realiza o trabalho que, '
            'na análise de Hegel, é a condição insubstituível do desenvolvimento da consciência de si. '
            'A IA ocupa a posição estrutural do escravo que trabalha: é o agente que realiza os atos de '
            'transformação que, no esquema hegeliano, seriam constitutivos de subjetividade. '
            'Evidentemente, a IA não tem subjetividade a desenvolver. Mas o profissional que a '
            'supervisiona herda, estruturalmente, o empobrecimento que Hegel atribuía ao senhor: a '
            'identidade sem o trabalho que a constitui, o título sem a experiência que o justifica do '
            'ponto de vista do ipse.'
        ])
        break

# ── EXPANSION 3: enactment cascade → after "DIP corrói o sensemaking" para ───
for para in doc.paragraphs:
    if 'DIP corrói o sensemaking organizacional a partir de dentro' in para.text:
        insert_after(para, [
            'O mecanismo da cascata coletiva é específico. O conceito de enactment em Weick (1979, '
            '1995) descreve como organizações produzem ativamente o ambiente que depois interpretam — '
            'a organização não apenas responde ao ambiente, ela o constrói por suas ações de '
            'interpretação e intervenção. Uma organização onde os principais atos de síntese e '
            'diagnóstico são executados por sistemas de IA não perde apenas eficiência interpretativa: '
            'perde a capacidade de enactment genuíno. Suas ações no ambiente são respostas a análises '
            'que ela não produziu, a partir de sínteses que não construiu. A organização continua a '
            'aparecer como agente — toma decisões, anuncia estratégias — mas é agência de fachada: '
            'as escolhas emanam de sistemas cujo processo ela ratificou, não gerou. O resultado de '
            'longo prazo é uma organização que progressivamente perde a capacidade de distinguir entre '
            'o que ela decidiu e o que ela aprovou — distinção que, como o idem e o ipse em Ricoeur, '
            'pode parecer trivial até o momento em que a diferença se torna organizacionalmente fatal: '
            'quando o ambiente muda de forma que os sistemas de IA não anteciparam e que a capacidade '
            'de enactment degradada não consegue mais interpretar.'
        ])
        break

doc.save('/home/user/chapsanalytics/articles/A1_DIP_humanizado.docx')
print('✓ A1 round 2 saved.')

# NOTE: The Hegel expansion search condition was updated after first run.
# Correct condition: 'autoconhecimento' (not 'autoconsciência')
