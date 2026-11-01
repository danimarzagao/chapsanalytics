# Pauta 25 (opção C): o agente com crachá — SK Telecom

Primeira rodada, 1/11/2026. Documento de projeto.

## Lido

**Comunicado da SKT, 26/10/2026 (primária, coreano; tradução minha).** "AI 거버넌스 리포트" (AI
Governance Report), primeira edição. CEO: 정재헌 (Jeong Jae-heon), o que resolve a divergência
de junho. Princípios T.H.E. AI (março de 2024). Governança integrada à proteção de dados, sob o
CPO (차호범, Cha Ho-beom). Agentes internos com critério único em desenvolvimento, teste, operação
e **encerramento** (종료). ISO/IEC 42001: em 2024 para serviços ao cliente; em outubro de 2026,
ampliada ao sistema de gestão de agentes internos. Cha: "No tempo dos agentes de IA, a governança
de IA fica ainda mais importante." **O comunicado não fala em KPI nem em avaliação de desempenho;
isso vem da reportagem abaixo, que cita o relatório.**

**Financial News (파이낸셜뉴스), 26/10, Yoon Hong-jip (윤홍집), citando o relatório.**
- "Sistema de número de funcionário para agentes" (에이전트 사번 제도): o agente pronto é
  registrado; passa por avaliação interna; se aprovado, recebe número; é gerido por tarefa,
  responsável, área, estado de operação e desempenho.
- **Responsável conforme impacto e autonomia:** agente que auxilia uma pessoa pode ser gerido pelo
  próprio usuário; agente de alto impacto ou alta autonomia fica sob líder de equipe ou executivo.
  Funções e dados acessíveis definidos pela natureza da tarefa. "Quanto maior a autonomia, mais
  fortes a revisão e a aprovação humanas."
- "Agent OS": registra execução, uso, histórico de mudanças, modelos e ferramentas usados, e o
  processo de execução, para achar a causa de problemas; pode interromper a execução.
- **Avaliação:** completude do trabalho, alcance do impacto, forma de acesso a dados, contribuição
  ao resultado; decide manter, melhorar ou encerrar. "No longo prazo, considera refletir os
  resultados nos KPIs centrais da organização."
- Plano: 2026 base (critérios, registro, dono, permissões); 2027 controles diferenciados por
  autonomia e impacto e revisão/aprovação/intervenção humana; 2028 ciclo completo, de operação a
  descarte (폐기).
- Serviço com risco residual inaceitável sem mitigação não é lançado.

**TelecomTV e Edaily (junho de 2026), estratégia "AX Innovation 2.0".** Agentes como "digital
employees" com número, departamento, função e permissões; "managed through procedures similar to
those of humans from hiring to termination". CEO Jeong Jae-heon.

## Livro (relido)

- Cap. 4, §4, "Calibrar autonomia": quatro parâmetros (especificidade do contexto, reversibilidade
  das ações, frequência de casos de fronteira, custo de erro). Delegar a humanos tem sinais
  implícitos (perguntas, histórico, fadiga); delegar a agente não tem nenhum.
- Cap. 4, §2: tarefas de execução, julgamento e cuidado. Nas de cuidado, "avaliações
  automatizadas de performance, onboarding por agente" degradam o tecido relacional.

## Tese candidata

**Convergência:** a SKT calibra pelo que o livro chama de custo de erro e de autonomia: quanto
mais impacto e autonomia, mais alto o responsável humano e mais forte a revisão. **Divergência:** a
SKT calibra *quem supervisiona*, não *quanto o agente pode fazer*; dois dos quatro parâmetros do
livro (especificidade do contexto, casos de fronteira) não aparecem no que foi publicado. **Achado
incômodo:** o "Agent OS" dá ao agente uma ficha que poucas empresas têm de seus empregados: cada
ação registrada, causa rastreável, avaliação por contribuição. O crachá não humaniza o agente;
burocratiza-o. A pergunta para o leitor: se o agente tem número, responsável, avaliação e
desligamento, o que distingue o empregado? E o empregado responsável por dez agentes passa a ser
avaliado por quê?

**Riscos:** conheço o relatório só pelo comunicado e pela Financial News. Não sei como a SKT
avalia pessoas, então não comparar sem fonte. Não sei se agentes já foram "desligados".

## Falta

1. O próprio "AI 거버넌스 리포트" (link de download no comunicado, news.sktelecom.com).
2. Opcional: o anúncio de junho em coreano, citado pela TelecomTV.

## Segunda rodada, 1/11: os dez arquivos de contexto

- **RCR Wireless, 18/6, e SBS Star:** confirmam o "AX Innovation 2.0": agentes como "digital
  employees" com número, departamento, função e permissões; "Agent Store" interno onde empregados
  compartilham agentes que criaram; agente de rede só lê o que precisa, "for the same reason a
  marketing hire wouldn't have" acesso a tudo.
- **Fortune, 10/3/2026, Nick Lichtenberg:** Tim Walsh (KPMG EUA) diz que a métrica que está
  redesenhando o quadro de pessoal é a **"labor cost margin"**, e não a receita por empregado.
  Pesquisa KPMG com 100 CEOs de grandes empresas: quase 80% destinam pelo menos 5% do orçamento de
  capital à IA; 41%, pelo menos 10%. **É de março: contexto, não notícia da semana.**
- **The Next Web:** pesquisa com **29** executivos de Fortune 500/1000; 75% otimistas com agentes;
  52% esperam quadro estável ou maior; 48% esperam reduzir. A própria matéria diz que a amostra é
  pequena demais para ser representativa. **Não usar como dado; no máximo como ilustração, com a
  ressalva.**
- **Allwork, maio:** ClickUp com cerca de 3.000 agentes internos, três por empregado, desde janeiro.
- **BBC (BBC Eye), Sofia Liguori:** "makes me feel ashamed to work at Google", em caráter pessoal,
  apesar de "contract restricting her from doing so"; Andreas Kirsch também saiu. Google: processo
  "consistent" de revisão de contratos e proibição de "retaliation of any kind". Mais Ynet, LBC,
  IBTimes e um quarto texto sobre a demissão.

## Tese ajustada

O artigo pode pôr lado a lado duas fichas de funcionário da mesma semana. O agente da SKT tem
número, responsável humano proporcional ao risco, registro de cada ação, avaliação de desempenho e
procedimento de desligamento, escrito e certificado por norma ISO. A engenheira do Google tem um
contrato que, segundo ela, a impede de criticar a empresa, e saiu para poder falar. Sem forçar a
analogia (regra 1.2: não é a mesma empresa nem a mesma condição): o ponto é que a governança mais
cuidadosa da semana foi escrita para o agente. O livro dá a régua para avaliar o desenho da SKT
(quatro parâmetros de calibração) e o alerta (onboarding e avaliação automatizados em tarefas de
cuidado).

**Prudência:** a comparação SKT x Google é retórica; cada caso precisa se sustentar sozinho. Se a
dupla parecer forçada, o texto fica só com a SKT e o livro.

## Terceira rodada, 1/11: o relatório (fonte primária, coreano, 40 pp.; tradução minha)

**"AI 거버넌스 리포트", SKT, outubro de 2026, Parte 3, pp. 25-30.**

- p. 25, sistema de número de funcionário: "핵심은 '책임 있는 자율적인 업무처리'" (o núcleo é o
  "processamento autônomo e responsável do trabalho"); quanto mais o agente faz sozinho, mais claro
  tem de ser quem supervisiona, com que critério e em que escopo. Componentes: registro (ID básico,
  número após cumprir critérios), responsável, permissões, avaliação, operação e encerramento.
- p. 26: agente que ajuda uma pessoa é gerido por ela; agente de maior impacto ou mais autônomo
  "deve obrigatoriamente" ter líder de equipe ou executivo como responsável. **E o nível de
  intervenção humana é desenhado por tarefa: "até onde o agente decide e executa sozinho, e em que
  ponto o humano intervém".** (Corrige a pauta: a SKT calibra também quanto o agente pode fazer,
  não só quem supervisiona.)
- p. 27, Agent OS: identificação (ID, dono, número), execução (registros, políticas, interrupção),
  auditoria, uso (tokens, chamadas, custo); grava cada etapa e permite interromper.
- **p. 28, três fatores obrigatórios para dar número e definir o escopo do agente: (1) se existe
  procedimento operacional padrão (SOP); (2) se o desempenho pode ser medido objetivamente; (3) se
  há capacidade de concluir a tarefa sem intervenção humana.** "Esses três fatores são a base para
  estimar a autonomia e o nível de risco." Supervisão em três momentos: revisão e aprovação antes de
  decisões importantes; monitoramento durante; verificação depois.
- **p. 29: "A SKT reconhece oficialmente o AI Agent com número de funcionário como uma nova força de
  trabalho (Workforce)."** Avaliação por dados de operação e indicadores definidos antes; usuário e
  responsável fazem autoavaliação; comitê de especialistas em IA avalia competência e desempenho.
  **Uso de curto prazo: vinculação à avaliação e à remuneração de executivos e prêmios a
  empregados. Longo prazo: inclusão no KPI organizacional.** "O resultado é base para expandir os
  agentes e melhorar a divisão de trabalho entre pessoas e agentes."
- p. 30: avaliação periódica de resultado, desempenho, **custo de operação** e funções; "o agente
  cuja necessidade diminuiu tem a operação encerrada".

## Tese, com o documento

1. **Convergência com o livro (cap. 4, §4):** supervisão proporcional ao impacto e à autonomia; o
   SOP e a capacidade de concluir sem humano são o avesso de "especificidade do contexto" e
   "frequência de casos de fronteira". A SKT pôs em norma quase os quatro parâmetros.
2. **O que a SKT acrescenta, e o livro não tem:** "o desempenho pode ser medido objetivamente" como
   condição de autonomia. É uma regra sensata e tem um efeito colateral: a autonomia vai para o
   trabalho mensurável, e o trabalho difícil de medir fica com as pessoas (e, pelo cap. 4 §2, é o de
   julgamento e cuidado). Liga com "Perguntar não mede".
3. **O achado da semana:** o desempenho do agente entra na avaliação e na remuneração de executivos
   e em prêmios de empregados. O humano responsável passa a ser avaliado também pelo agente que
   supervisiona. É o "contrato reformulado" do cap. 5 §9 visto de outro ângulo, e é o ponto mais
   novo do caso.
4. Contraste opcional: Sofia Liguori (BBC), que saiu para poder falar. Usar só se não forçar.
