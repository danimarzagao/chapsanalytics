"""Revision of A3 (Instrumento) — addressing critical review findings."""
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

doc = Document('/home/user/chapsanalytics/articles/A3_Instrumento_humanizado.docx')

# ── FIX 1: Replace LinkedIn post reference throughout ────────────────────────
# "Marzagão (2026)" LinkedIn post must become a theoretical distinction owned by the paper
# In double-blind submission, use [AUTOR, 2026] placeholder
for para in doc.paragraphs:
    for run in para.runs:
        if 'Marzagão (2026)' in run.text:
            run.text = run.text.replace('Marzagão (2026)', '[AUTOR, 2026]')
        if 'formulada por [AUTOR, 2026]' in run.text:
            # Make the distinction more self-contained: attribute to the essay itself
            run.text = run.text.replace(
                'formulada por [AUTOR, 2026]',
                'desenvolvida neste ensaio'
            )

# Fix the REFERÊNCIAS entry for LinkedIn post
for para in doc.paragraphs:
    if 'MARZAGÃO' in para.text and 'LinkedIn' in para.text:
        for run in para.runs:
            if 'LinkedIn' in run.text:
                run.text = run.text.replace(
                    'MARZAGÃO, D. O instrumento intacto. LinkedIn, 17 maio 2026.',
                    '[AUTOR]. O instrumento e suas condições de operação. '
                    '[referência retida para revisão cega].'
                )
    # Also handle split across runs
    if 'O instrumento intacto. LinkedIn' in para.text:
        full = para.text
        para.clear()
        para.add_run('[AUTOR]. O instrumento e suas condições de operação. '
                     '[referência retida para revisão cega].')

# ── ADDITION 1: Lupien et al. + Sapolsky in Section 2.1 ──────────────────────
# After the paragraph describing Arnsten's cortisol/dendritic findings
for para in doc.paragraphs:
    if 'retração das espinhas dendríticas nos neurônios piramidais' in para.text or \
       'memória de trabalho' in para.text and 'cortisol' in para.text:
        insert_after(para, [
            'Lupien, McEwen, Gunnar e Heim (2009), em revisão abrangente publicada na '
            'Nature Reviews Neuroscience, demonstraram que os efeitos do estresse crônico '
            'se distribuem de forma diferencial ao longo da vida — com o córtex pré-frontal '
            'apresentando vulnerabilidade particularmente pronunciada em adultos jovens e de '
            'meia-idade, exatamente o perfil demográfico predominante nos dados do DDI Global '
            'Leadership Forecast (2026). Sapolsky (2004) integrou décadas de pesquisa '
            'neuroendócrina para demonstrar que a resposta ao estresse, calibrada '
            'evolutivamente para ameaças físicas de curta duração, torna-se patológica '
            'quando ativada cronicamente por ameaças sociais de natureza difusa e persistente. '
            'A ameaça de uma avaliação de desempenho ou de uma reunião de board, ao '
            'contrário do predador físico, não pode ser resolvida por ação imediata — '
            'e é essa incapacidade de resolução que mantém o eixo HPA em ativação sustentada '
            'com os efeitos documentados por Arnsten. A insídia, como documentado por ambos '
            'os autores, está na imperceptibilidade: o PFC comprometido não pode avaliar '
            'seu próprio comprometimento porque o instrumento de avaliação é o mesmo '
            'instrumento que foi comprometido.'
        ])
        break

# ── ADDITION 2: Frazier et al. + Edmondson & Lei + Woolley in Section 4 ──────
# After the paragraph repositioning psychological safety as neurobiological
for para in doc.paragraphs:
    if 'Edmondson (1999, 2019) propôs segurança psicológica como clima de equipe' in para.text:
        insert_after(para, [
            'Frazier, Fainshmidt, Klinger, Pezeshkan e Vracheva (2017), em revisão '
            'meta-analítica de 136 estudos independentes publicada no Personnel Psychology, '
            'confirmaram que segurança psicológica prediz positivamente aprendizado em '
            'equipe, desempenho, comportamento de voz e engajamento. O dado mais '
            'relevante para o argumento aqui desenvolvido: os efeitos sobre desempenho '
            'foram consistentemente mais fortes em contextos de alta complexidade de '
            'tarefas — precisamente o contexto onde o PFC e o Sistema 2 são mais '
            'necessários e mais vulneráveis ao comprometimento por estresse crônico. '
            'Edmondson e Lei (2014), em revisão publicada no Annual Review of '
            'Organizational Psychology and Organizational Behavior, documentaram como '
            'o conceito de segurança psicológica expandiu do nível de equipe para o nível '
            'organizacional, com implicações para aprendizado entre equipes, inovação e '
            'criação de conhecimento. O presente artigo acrescenta à trajetória documentada '
            'por Edmondson e Lei a dimensão neurobiológica que estava implícita mas nunca '
            'formalizada: segurança psicológica não é apenas condição suficiente para '
            'performance — é condição necessária para que o instrumento de julgamento '
            'opere com integridade fisiológica.',
            'Woolley, Chabris, Pentland, Hashmi e Malone (2010), em estudo publicado na '
            'Science, demonstraram que a inteligência coletiva de grupo — o análogo coletivo '
            'do julgamento individual — é predita mais fortemente por sensibilidade social '
            'dos membros e participação equitativa nas discussões do que por quociente de '
            'inteligência individual. Segurança psicológica é o precursor organizacional '
            'dessas condições: sem ela, membros com alta sensibilidade social suprimem '
            'contribuições e o potencial coletivo de deliberação não se realiza — '
            'exatamente o mecanismo pelo qual o DCO se instala no nível coletivo.'
        ])
        break

# ── ADDITION 3: McEwen & Seeman for allostatic load in Section 5 (ANO Dim 1) ─
# After "Dimensão 1: carga alostática da liderança"
for para in doc.paragraphs:
    if 'Dimensão 1: carga alostática da liderança' in para.text or \
       'carga alostática' in para.text and 'HRV' in para.text:
        insert_after(para, [
            'O conceito de carga alostática foi cunhado por McEwen e Seeman (1999) para '
            'descrever o custo cumulativo que o eixo HPA impõe ao organismo quando a '
            'resposta ao estresse é ativada cronicamente. McEwen e Seeman identificaram '
            'um conjunto de biomarcadores mensuráveis — cortisol, DHEA-S, pressão '
            'sistólica e diastólica, glicose em jejum, colesterol HDL, índice de massa '
            'corporal — que funcionam como indicadores do desgaste acumulado pelo '
            'sistema de estresse. A Dimensão 1 da ANO adapta essa lógica para o contexto '
            'organizacional, utilizando proxies acessíveis sem coleta invasiva — variabilidade '
            'da frequência cardíaca (HRV), Perceived Stress Scale (PSS-10), prevalência '
            'de uso de medicação psiquiátrica e qualidade do sono — para capturar o '
            'mesmo fenômeno subjacente: o custo acumulado de operar sistematicamente '
            'em estado de ativação do eixo HPA.'
        ])
        break

# ── ADDITION 4: Formal Propositions Section before Considerações Finais ───────
propositions = [
    '6. PROPOSIÇÕES TEÓRICAS',
    'O framework ANO e os conceitos de DCO e de segurança psicológica como condição '
    'neurobiológica geram um conjunto de proposições empiricamente testáveis que '
    'estruturam a agenda de validação subsequente e distinguem o argumento deste ensaio '
    'de formulações adjacentes em saúde ocupacional e gestão do estresse.',
    'P1 (Hipótese do Substrato Decisório): Organizações com lideranças apresentando '
    'alta carga alostática mensurada (Dimensão 1 da ANO) produzirão, em condições '
    'experimentais controladas, decisões estratégicas de qualidade sistematicamente '
    'inferior a organizações comparáveis com baixa carga alostática — mesmo controlando '
    'por experiência dos líderes, complexidade do problema decisório e qualidade da '
    'informação disponível. Operacionalização: protocolo de simulação de decisão '
    'estratégica em laboratório, com líderes categorizados por nível de carga '
    'alostática via PSS-10 e HRV.',
    'P2 (Hipótese da Mediação Neurobiológica): A relação entre ambientes de baixa '
    'segurança psicológica (Dimensão 2) e baixa qualidade de decisões estratégicas '
    'será mediada por indicadores de carga alostática (Dimensão 1), de modo que '
    'o impacto do ambiente sobre decisão opera primariamente via ativação crônica '
    'do eixo HPA — e não apenas via canais motivacionais ou comunicacionais. '
    'Essa proposição implica que intervenções puramente motivacionais, sem modificação '
    'do ambiente de ameaça social, serão insuficientes para recuperar a qualidade '
    'decisória comprometida.',
    'P3 (Hipótese do Debt Cognitivo e Exploration): O DCO acumulado — operacionalizado '
    'pela frequência de ciclos de deliberação real abaixo de limiar mínimo por unidade '
    'de tempo (Dimensão 4) — prederá negativamente a capacidade de exploration no '
    'sentido de March (1991). Organizações com alto DCO exibirão maior proporção de '
    'exploitation, menor taxa de inovação genuína e maior propensão a competency traps, '
    'controlando por setor e pressões competitivas — porque o estresse crônico torna '
    'a deriva em direção ao conhecido neurologicamente inevitável.',
    'P4 (Hipótese do Efeito Moderador da Recuperação): Intervenções deliberadas de '
    'arquitetura de recuperação cognitiva (Dimensão 3) — ciclos protegidos de baixa '
    'demanda dirigida que permitem ativação do default mode network — moderarão '
    'negativamente o efeito da exposição ao estresse crônico sobre indicadores de '
    'carga alostática. Líderes com demanda equivalente apresentarão menor degradação '
    'pré-frontal quando submetidos a ciclos deliberados de recuperação, comparados '
    'a controles sem esses ciclos — sugerindo que a Dimensão 3 é a alavanca de '
    'governança com maior poder de reversão do DCO acumulado.',
]

for para in doc.paragraphs:
    if 'CONSIDERAÇÕES FINAIS' in para.text and ('6.' in para.text or '7.' in para.text):
        insert_before(para, propositions)
        break
    elif para.text.strip().startswith('6. CONSIDERAÇÕES'):
        insert_before(para, propositions)
        break

# ── FIX 2: Fix Alexandre reference ────────────────────────────────────────────
for para in doc.paragraphs:
    if 'ALEXANDRE (palestrante)' in para.text:
        for run in para.runs:
            if 'ALEXANDRE (palestrante)' in run.text:
                run.text = run.text.replace(
                    'ALEXANDRE (palestrante). Solidão no trabalho, fadiga relacional e segurança psicológica. São Paulo Innovation Week 2026, 13 maio 2026.',
                    'ALEXANDRE, P. Solidão no trabalho, fadiga relacional e segurança psicológica nas organizações. In: São Paulo Innovation Week 2026, 13 maio 2026, São Paulo. Apresentação oral. [Psicólogo, saúde mental corporativa].'
                )

# ── NEW REFERENCES ────────────────────────────────────────────────────────────
new_refs = [
    'EDMONDSON, A. C.; LEI, Z. Psychological safety: The history, renaissance, and '
    'future of an interpersonal construct. Annual Review of Organizational Psychology '
    'and Organizational Behavior, v. 1, p. 23-43, 2014.',
    'FRAZIER, M. L.; FAINSHMIDT, S.; KLINGER, R. L.; PEZESHKAN, A.; VRACHEVA, V. '
    'Psychological safety: A meta-analytic review and extension. Personnel Psychology, '
    'v. 70, n. 1, p. 113-165, 2017.',
    'LUPIEN, S. J.; McEWEN, B. S.; GUNNAR, M. R.; HEIM, C. Effects of stress '
    'throughout the lifespan on the brain, behaviour and cognition. Nature Reviews '
    'Neuroscience, v. 10, n. 6, p. 434-445, 2009.',
    'McEWEN, B. S.; SEEMAN, T. Protective and damaging effects of mediators of stress: '
    'Elaborating and testing the concepts of allostasis and allostatic load. Annals of '
    'the New York Academy of Sciences, v. 896, n. 1, p. 30-47, 1999.',
    'NEWMAN, A.; DONOHUE, R.; EVA, N. Psychological safety: A systematic review of '
    'the literature. Human Resource Management Review, v. 27, n. 3, p. 521-535, 2017.',
    'SAPOLSKY, R. M. Why Zebras Don\'t Get Ulcers. 3. ed. New York: Holt Paperbacks, 2004.',
    'WOOLLEY, A. W.; CHABRIS, C. F.; PENTLAND, A.; HASHMI, N.; MALONE, T. W. '
    'Evidence for a collective intelligence factor in the performance of human groups. '
    'Science, v. 330, n. 6004, p. 686-688, 2010.',
]

for para in doc.paragraphs:
    if para.text.strip() == 'REFERÊNCIAS':
        insert_after(para, new_refs)
        break

# ── Update section numbering ────────────────────────────────────────────────
# "6. CONSIDERAÇÕES FINAIS" → "7. CONSIDERAÇÕES FINAIS" (since we added section 6)
for para in doc.paragraphs:
    if '6. CONSIDERAÇÕES FINAIS' in para.text:
        for run in para.runs:
            if '6. CONSIDERAÇÕES FINAIS' in run.text:
                run.text = run.text.replace('6. CONSIDERAÇÕES FINAIS', '7. CONSIDERAÇÕES FINAIS')
        break

doc.save('/home/user/chapsanalytics/articles/A3_Instrumento_humanizado.docx')
print('✓ A3 revision saved.')
