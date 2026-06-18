"""A3 Round 2: structural fix + deepen 3 key arguments + fix abstract redundancy."""
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

doc = Document('/home/user/chapsanalytics/articles/A3_Instrumento_humanizado.docx')

# ── STRUCTURAL FIX: reorder propositions section ──────────────────────────────
# Current wrong order: P4, P3, P2, P1, intro, "6. PROPOSIÇÕES TEÓRICAS", CONSIDERAÇÕES FINAIS
# Target order:        "6. PROPOSIÇÕES TEÓRICAS", intro, P1, P2, P3, P4, CONSIDERAÇÕES FINAIS

heading_p = intro_p = p1 = p2 = p3 = p4 = anchor_p = None
for para in doc.paragraphs:
    t = para.text.strip()
    if t == '6. PROPOSIÇÕES TEÓRICAS':
        heading_p = para
    elif t.startswith('O framework ANO e os conceitos de DCO'):
        intro_p = para
    elif t.startswith('P1 (Hipótese do Substrato Decisório)'):
        p1 = para
    elif t.startswith('P2 (Hipótese da Mediação Neurobiológica)'):
        p2 = para
    elif t.startswith('P3 (Hipótese do Debt Cognitivo'):
        p3 = para
    elif t.startswith('P4 (Hipótese do Efeito Moderador'):
        p4 = para
    elif t.startswith('7. CONSIDERAÇÕES FINAIS'):
        anchor_p = para

if all([heading_p, intro_p, p1, p2, p3, p4, anchor_p]):
    ordered = [heading_p, intro_p, p1, p2, p3, p4]
    elems = [p._p for p in ordered]
    for e in elems:
        e.getparent().remove(e)
    for e in elems:
        anchor_p._p.addprevious(e)
    print('✓ A3 propositions reordered')
else:
    missing = [name for name, v in [('heading', heading_p), ('intro', intro_p),
               ('p1', p1), ('p2', p2), ('p3', p3), ('p4', p4),
               ('anchor', anchor_p)] if v is None]
    print(f'WARNING: could not find: {missing}')

# ── FIX: Considerações Finais opening redundancy ─────────────────────────────
for para in doc.paragraphs:
    if 'Este ensaio partiu da distinção desenvolvida neste ensaio entre' in para.text:
        for run in para.runs:
            if 'desenvolvida neste ensaio' in run.text:
                run.text = run.text.replace(
                    'da distinção desenvolvida neste ensaio entre',
                    'da distinção entre'
                )
        break

# ── EXPANSION 1: Paradox of self-assessment (after degradação imperceptível) ──
for para in doc.paragraphs:
    if 'O PFC comprometido não pode avaliar seu próprio comprometimento' in para.text:
        insert_after(para, [
            'As consequências organizacionais desse ponto são mais radicais do que habitualmente se '
            'reconhece. Os instrumentos de diagnóstico organizacional padrão — pesquisas de clima, '
            'avaliações 360°, entrevistas de saída, relatórios de engajamento, indicadores de '
            'bem-estar — dependem integralmente da capacidade de auto-relato dos indivíduos que os '
            'respondem. Um PFC comprometido por carga alostática elevada não apenas toma decisões de '
            'qualidade inferior: ele também produz auto-avaliações sistematicamente distorcidas. '
            'Arnsten (2009, 2015) e os dados do DDI Global Leadership Forecast (2026) convergem '
            'nessa direção: líderes em condição de esgotamento crônico tendem a subestimar sua '
            'própria degradação cognitiva, a sobrestimar a qualidade de suas decisões passadas e a '
            'atribuir dificuldades ao ambiente externo em vez de ao estado interno. O paradoxo da '
            'autoavaliação — o instrumento degradado não pode diagnosticar sua própria degradação — '
            'torna o kit diagnóstico padrão de RH estruturalmente cego exatamente à condição que '
            'mais precisa detectar. É precisamente por isso que a ANO propõe métricas que não '
            'dependem de auto-relato: HRV, PSS-10 e prevalência de uso de medicação psiquiátrica '
            'são indicadores que contornam o viés de autoavaliação inerente ao PFC sob carga '
            'alostática elevada. Diagnosticar o instrumento requer instrumentos que não dependam '
            'do instrumento sendo diagnosticado.'
        ])
        break

# ── EXPANSION 2: Evolutionary mismatch (after March/exploitation para) ────────
for para in doc.paragraphs:
    if 'revela o substrato neurobiológico da competency trap' in para.text:
        insert_after(para, [
            'É importante precisar o argumento: a deriva em direção a exploitation sob estresse não '
            'é um erro cognitivo corrigível por treinamento ou consciência gerencial. É a resposta '
            'neurologicamente correta ao tipo de ambiente para o qual o eixo HPA foi calibrado '
            'evolutivamente. Em ambientes de ameaça física aguda e curta duração — o contexto '
            'ancestral no qual o sistema de estresse foi moldado — a exploitation de padrões '
            'conhecidos é genuinamente mais segura do que a exploration de novos: o caçador que '
            'enfrenta um predador não está em momento de experimentar técnicas desconhecidas. O '
            'problema não é o mecanismo; é o mismatch entre o contexto evolutivo (ameaça física, '
            'duração curta, resolução possível por ação imediata) e o contexto organizacional '
            'contemporâneo (ameaça social difusa, duração crônica, sem resolução por ação imediata). '
            'O DCO é, portanto, o acúmulo da inadaptação evolutiva: um mecanismo de sobrevivência '
            'operando em ambiente para o qual não foi calibrado, produzindo ininterruptamente o '
            'viés de exploitation que, no ambiente ancestral, era proteção adaptativa e, no ambiente '
            'organizacional, é armadilha estratégica. Compreender isso tem consequência prática '
            'direta: não há intervenção motivacional ou de liderança que consiga reverter o DCO '
            'sem modificar as condições ambientais que ativam o eixo HPA — porque o viés não é '
            'cognitivo, é neurobiológico.'
        ])
        break

# ── EXPANSION 3: ANO Dimension 4 operationalization ──────────────────────────
for para in doc.paragraphs:
    if 'Dimensão 4: proporção de deliberação real' in para.text:
        insert_after(para, [
            'A Dimensão 4 merece atenção especial como inovação metodológica. Sua operacionalização '
            'em campo não requer acesso a conteúdos de reuniões: é possível aproximá-la por '
            'indicadores de processo disponíveis — duração média de reuniões decisórias versus '
            'tempo de preparação individual documentado; proporção de decisões tomadas em reuniões '
            'convocadas com menos de 24h de antecedência; relação entre número de participantes '
            'em reuniões e profundidade de debate medida por pesquisa pós-reunião. Em organizações '
            'onde o DCO está instalado, esses indicadores tendem a produzir um padrão reconhecível: '
            'muitas reuniões, pouca preparação, decisões tomadas sob pressão de tempo, e sensação '
            'persistente de que "as decisões reais já foram tomadas antes da reunião". A Dimensão 4 '
            'é a tentativa de tornar mensurável esse padrão — convertendo em indicador de '
            'governança o que os membros organizacionais frequentemente descrevem como cultura, '
            'mas que tem origem na degradação do substrato neurobiológico da deliberação.'
        ])
        break

doc.save('/home/user/chapsanalytics/articles/A3_Instrumento_humanizado.docx')
print('✓ A3 round 2 saved.')
