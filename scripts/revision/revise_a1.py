"""Revision of A1 (DIP) — addressing critical review findings."""
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
    """Insert paragraphs after anchor, preserving order."""
    current = anchor_para._p
    for text in texts:
        new_p = make_para(text)
        current.addnext(new_p)
        current = new_p

def insert_before(anchor_para, texts):
    """Insert paragraphs before anchor, preserving order."""
    for text in reversed(texts):
        new_p = make_para(text)
        anchor_para._p.addprevious(new_p)

def modify_run_text(para, old, new):
    full = para.text
    if old not in full:
        return False
    for run in para.runs:
        if old in run.text:
            run.text = run.text.replace(old, new)
            return True
    # Fallback: replace across runs by rebuilding
    para.clear()
    run = para.add_run(full.replace(old, new))
    return True

doc = Document('/home/user/chapsanalytics/articles/A1_DIP_humanizado.docx')

# ── ADDITION 1 ──────────────────────────────────────────────────────────────
# After "O ponto não é categorial..." → add Turkle/Zuboff/Danaher positioning
for para in doc.paragraphs:
    if para.text.startswith('O ponto não é categorial:'):
        insert_after(para, [
            'A questão foi documentada em suas dimensões tecnológica e política. '
            'Turkle (2011) demonstrou como a delegação de funções comunicativas e emocionais '
            'a dispositivos digitais corrói a capacidade de solidão reflexiva e de presença '
            'interpessoal plena — o que ela nomeia de "estar junto, mas sozinhos". Zuboff (2019) '
            'mapeou como o capitalismo de vigilância captura comportamento humano como insumo '
            'produtivo, convertendo ação em commodity preditiva. Danaher (2019) formulou o risco '
            'de "algocracy" — governança por algoritmos — e seu efeito de esvaziamento de agência '
            'política e decisória. Essas análises descrevem aspectos reais e complementares do '
            'problema, mas operam em registros distintos do que aqui interessa: Turkle descreve '
            'erosão comunicativa; Zuboff descreve expropriação de dados; Danaher descreve erosão '
            'de agência política. Nenhuma das três formula o problema em termos da constituição '
            'neurocognitiva do self profissional: o que acontece com a identidade narrativa do '
            'sujeito quando os atos de agência que definem sua competência são sistematicamente '
            'executados por agentes artificiais? É essa lacuna que o conceito de DIP endereça.'
        ])
        break

# ── ADDITION 2 ──────────────────────────────────────────────────────────────
# After Sennett paragraph (ends "delega as próprias ações que constituiriam o projeto")
# → add Albert & Whetten + Cascio & Montealegre on organizational identity
for para in doc.paragraphs:
    if 'delega as próprias ações que constituiriam o projeto' in para.text:
        insert_after(para, [
            'Na teoria organizacional, Albert e Whetten (1985) estabeleceram que a identidade '
            'organizacional responde a três perguntas fundamentais: o que somos, como operamos, '
            'e o que nos distingue. A identidade profissional individual tem estrutura análoga: '
            'o que faço, como faço, e o que me torna reconhecível como competente nessa função. '
            'A DIP opera precisamente sobre o segundo e o terceiro elementos dessa estrutura. '
            'Cascio e Montealegre (2016), em revisão abrangente sobre tecnologia e trabalho, '
            'documentaram que sucessivas ondas de automação tendem a modificar não apenas '
            'estruturas de emprego, mas as próprias categorias de competência pelas quais '
            'trabalhadores constroem sentido de si. A DIP especifica o mecanismo neurocognitivo '
            'pelo qual essa modificação opera no plano subjetivo: quando os atos de diagnóstico, '
            'formulação e julgamento são delegados a agentes artificiais, a identidade profissional '
            'perde seu referente experiencial — reduzindo-se a uma identidade de título que não '
            'foi constituída pela experiência de agência que a tornaria psicologicamente sustentável.'
        ])
        break

# ── ADDITION 3 ──────────────────────────────────────────────────────────────
# Add stets & burke citation to section 2 (self and identity)
for para in doc.paragraphs:
    if 'O self não é uma coisa que se tem.' in para.text:
        insert_after(para, [
            'Stets e Burke (2000) articularam a distinção entre teoria da identidade e teoria '
            'da identidade social, mostrando que identidade pessoal se constitui por verificação '
            'de comportamentos que confirmam o significado do self em uma dada posição. Essa '
            'formulação é convergente com a de Damasio: o self requer confirmação contínua via '
            'ação. Quando a ação é delegada, a verificação de identidade perde seu principal '
            'mecanismo de alimentação.'
        ])
        break

# ── ADDITION 4 ──────────────────────────────────────────────────────────────
# Add formal propositions section before "6. CONSIDERAÇÕES FINAIS"
propositions = [
    '5.4 PROPOSIÇÕES TEÓRICAS',
    'O framework da DIP gera quatro proposições empiricamente testáveis que estruturam '
    'a agenda de pesquisa subsequente e permitem distinguir a DIP de construtos adjacentes '
    'como burnout, workaholism ou alienação tecnológica.',
    'P1 (Proposição da Proporcionalidade): A prevalência de DIP em uma função profissional '
    'é positivamente correlacionada com a proporção de atos cognitivamente significativos '
    'dessa função delegados a agentes de IA, e negativamente correlacionada com o grau em '
    'que o sujeito percebe autoria sobre o output final — operacionalizado por instrumento '
    'de percepção de agência e autoria profissional.',
    'P2 (Proposição da Erosão Neurocognitiva): Sujeitos em condição de DIP elevada '
    'apresentarão hipoativação do default mode network em tarefas de reflexão autobiográfica '
    'profissional (avaliada por fMRI), e menor coerência de narrativa autobiográfica avaliada '
    'por instrumentos como o Narrative Identity Coding System — comparados a sujeitos em '
    'condições de trabalho de alta agência, controlando por tempo de experiência e setor.',
    'P3 (Proposição da Mediação da Saúde Mental): A DIP mediará a relação entre nível de '
    'agentificação de IA no trabalho e indicadores de saúde mental (burnout, despersonalização, '
    'ansiedade generalizada), de modo que funções com maior proporção de atos identitários '
    'delegados apresentarão maior incidência de sintomatologia, mesmo controlando por volume '
    'de trabalho e complexidade percebida.',
    'P4 (Proposição do Design Moderador): Intervenções de design organizacional que '
    'preservam atos identitários específicos — autoria visível de diagnóstico, formulação '
    'e julgamento — moderarão negativamente a relação entre nível de agentificação e '
    'desenvolvimento de DIP, sugerindo que o fenômeno é de design, não de tecnologia per se. '
    'Essa proposição tem implicação direta: a resposta à DIP não é rejeitar agentes de IA, '
    'mas redesenhar deliberadamente os ambientes onde esses agentes operam.',
]

for para in doc.paragraphs:
    if 'CONSIDERAÇÕES FINAIS' in para.text and para.text.strip().startswith('6'):
        insert_before(para, propositions)
        break

# ── FIX ─────────────────────────────────────────────────────────────────────
# Fix Alexandre reference (no surname — replace with formatted version)
for para in doc.paragraphs:
    if 'ALEXANDRE (palestrante)' in para.text or ('ALEXANDRE' in para.text and 'palestrante' in para.text):
        for run in para.runs:
            if 'ALEXANDRE (palestrante). Solidão no trabalho' in run.text:
                run.text = (
                    'ALEXANDRE, P. Solidão no trabalho, fadiga relacional e segurança psicológica '
                    'nas organizações contemporâneas. In: São Paulo Innovation Week 2026, '
                    '13 maio 2026, São Paulo. Apresentação oral. [Psicólogo, apresentação da '
                    'plataforma de saúde mental no ambiente corporativo]'
                )
            elif 'Alexandre' in run.text and 'psicólogo' in run.text.lower():
                run.text = run.text.replace(
                    'Alexandre, psicólogo presente no evento',
                    'Alexandre (2026), psicólogo com atuação em saúde mental corporativa'
                )

# ── NEW REFERENCES ───────────────────────────────────────────────────────────
new_refs = [
    'ALBERT, S.; WHETTEN, D. A. Organizational identity. Research in Organizational '
    'Behavior, v. 7, p. 263-295, 1985.',
    'CASCIO, W. F.; MONTEALEGRE, R. How technology is changing work and organizations. '
    'Annual Review of Organizational Psychology and Organizational Behavior, v. 3, '
    'p. 349-375, 2016.',
    'DANAHER, J. Automation and Utopia: Human Flourishing in a World without Work. '
    'Cambridge: Harvard University Press, 2019.',
    'STETS, J. E.; BURKE, P. J. Identity theory and social identity theory. '
    'Social Psychology Quarterly, v. 63, n. 3, p. 224-237, 2000.',
    'TURKLE, S. Alone Together: Why We Expect More from Technology and Less from '
    'Each Other. New York: Basic Books, 2011.',
    'ZUBOFF, S. The Age of Surveillance Capitalism: The Fight for a Human Future '
    'at the New Frontier of Power. New York: PublicAffairs, 2019.',
]

for para in doc.paragraphs:
    if para.text.strip() == 'REFERÊNCIAS':
        insert_after(para, new_refs)
        break

doc.save('/home/user/chapsanalytics/articles/A1_DIP_humanizado.docx')
print('✓ A1 revision saved.')
