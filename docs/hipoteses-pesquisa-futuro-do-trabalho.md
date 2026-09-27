# Hipóteses de pesquisa: futuro do trabalho em três unidades de análise

Derivadas do livro *O Trabalho que Vem* e do corpus de ensaios da série VibeCoding em
Contexto. Levantamento de 27 de setembro de 2026.

Cada hipótese traz predição direcional, variáveis, estratégia de identificação e a condição
de falsificação. A condição de falsificação é a parte que importa: hipótese que não pode
perder não é hipótese.

---

## Duas escolhas de método que atravessam as três unidades

Antes das hipóteses, porque elas decidem se qualquer uma é testável.

**1. Medir capacidade com a ferramenta removida.**

O experimento de Cruces e coautores (NBER 34851, 2026) fez a coisa mais importante e menos
imitada da literatura: mediu o desempenho com IA e depois mediu de novo sem IA. O ganho de
produtividade era real, e o estoque de conhecimento subjacente não havia se movido. O gap
voltou integralmente.

Quase toda a literatura de produtividade com IA mede o output assistido. Isso responde a
uma pergunta de curto prazo e não responde à pergunta de formação de capacidade. A
arquitetura mínima para as hipóteses do bloco individual é medição em três pontos: linha de
base sem ferramenta, desempenho com ferramenta, e desempenho sem ferramenta em T mais n.

**2. Várias hipóteses pedem dispersão como variável dependente, não média.**

Redundância de julgamento, divergência entre single e double-loop, variância intracoorte por
gênero, concentração de expertise em poucos portadores. Em todos esses casos a média esconde
o fenômeno. A variável dependente correta é variância, coeficiente de Gini ou assimetria da
distribuição, e isso muda o desenho estatístico.

Há ainda uma oportunidade de dado brasileiro que a série já identificou e que segue
inexplorada: CAGED e RAIS são registro administrativo com identificação de ocupação por CBO,
cobrindo o emprego formal inteiro, com frequência mensal. O desenho de Stanford para os 19%
é replicável aqui, e nenhuma das hipóteses abaixo que dependem de dado de emprego precisa de
coleta nova.

---

# Unidade 1 — O indivíduo no mundo corporativo

## H1.1 O efeito da IA sobre formação de capacidade é moderado por estoque prévio, com limiar

**Construto.** Capacidade absortiva e *prior related knowledge* (Cohen e Levinthal, 1990)
como moderadores da *augmentation trap* (Caosun e Aral, 2026).

**Predição.** A relação entre intensidade de adoção de IA e retenção de habilidade não é
monotônica. Ela é moderada pelo estoque prévio relacionado, com ponto de inflexão. Abaixo do
limiar, intensidade de adoção prediz perda de capacidade em estado estacionário. Acima,
prediz ganho. O efeito principal da adoção, isolado, deve ser próximo de nulo ou ambíguo,
que é exatamente o que a literatura vem encontrando.

**Variáveis.** Independente: intensidade de adoção, medida por frequência e profundidade de
delegação, não por autorrelato de uso. Moderador: estoque prévio no domínio, medido sem
ferramenta na linha de base. Dependente: desempenho sem ferramenta em T mais n, menos linha
de base.

**Identificação.** Experimento com randomização da intensidade de adoção dentro de faixas de
estoque prévio medido. Alternativa quase-experimental: implantação escalonada de ferramenta
por unidade, com estoque prévio medido antes do anúncio.

**Falsificação.** Se o termo de interação for nulo e o efeito principal negativo sobreviver,
a moderação cai e a história simples de desqualificação vence. Esse é o resultado que
derrubaria boa parte do Capítulo 5.

**Custo e prazo.** Médio. Exige instrumento de medição de domínio e janela de doze meses.

---

## H1.2 Delegação identitária patológica é separável de perda de habilidade

**Construto.** DIP (Marzagão, 2026), a partir de identidade narrativa em Ricoeur e de
sensemaking em Weick.

Esta é a hipótese de maior risco e maior retorno do conjunto, porque DIP hoje é ensaio
teórico sem medição. Se ela não se separar empiricamente de desqualificação, o construto não
sobrevive, e é melhor descobrir isso num desenho próprio do que num parecer de revisor.

**Predição.** Dois profissionais com decaimento de habilidade estatisticamente idêntico
apresentam desfechos diferentes em intenção de saída, disposição a tentar tarefa inédita e
comportamento de pedir ajuda, em função do grau em que as tarefas delegadas eram
constitutivas de identidade e não apenas operacionais.

**Variáveis.** Independente: centralidade identitária das tarefas efetivamente delegadas.
Medida por elicitação prévia, perguntando à pessoa quais tarefas a tornam boa no que faz, e
cruzando com o log do que a ferramenta assumiu. Controle: decaimento de habilidade medido
pelo protocolo da H1.1. Dependentes: intenção de saída, iniciativa em tarefa nova, busca de
ajuda, e uma medida de continuidade narrativa profissional.

**Identificação.** O desenho elegante é experimento natural sobre *qual* tarefa a ferramenta
automatiza primeiro, que é exógeno ao investimento identitário do indivíduo. Se uma
implantação automatiza a tarefa A em algumas unidades e a B em outras, e A e B diferem em
centralidade identitária mas não em conteúdo de habilidade, há identificação.

**Falsificação.** Se os desfechos acompanharem a perda de habilidade e não a centralidade
identitária, DIP colapsa em desqualificação e deixa de ser construto distinto.

**Custo e prazo.** Alto. Exige desenvolvimento de instrumento antes do estudo principal.

---

## H1.3 O paradoxo da senioridade tem prazo de validade mensurável

**Construto.** *Competency trap* de March no nível individual, aplicada ao achado de
Brynjolfsson, Li e Raymond (novatos mais 34%, veteranos quase nada).

**Predição.** O ganho dos novatos vem de disseminação do julgamento tácito dos sêniores, que
é julgamento de ontem. Logo, o ganho decai em função da distância entre a distribuição de
casos corrente e a distribuição em que aquele julgamento foi formado. Em regimes de alto
deslocamento distributivo, o ganho do novato encolhe ou inverte, e o do veterano se torna
positivo.

**Variáveis.** Independente: deslocamento distributivo, medido por entrada de produto novo,
mudança regulatória, tipo inédito de demanda, ou distância estatística entre a distribuição
de casos do período e a do período de treino. Moderador: tempo de casa. Dependente:
produtividade e qualidade resolvida.

**Identificação.** Dados de operação logados, com choques de deslocamento datáveis e
exógenos ao trabalhador, como mudança regulatória. Interação entre deslocamento e senioridade.

**Falsificação.** Se o ganho do novato for estável entre regimes de deslocamento, o mecanismo
do julgamento de ontem cai, e o achado de Brynjolfsson passa a valer sem a condição de
contorno.

**Por que é a mais publicável do bloco.** Toma um resultado célebre e propõe a condição de
contorno que ele não testou. Isso é contribuição de fronteira, não replicação.

---

## H1.4 Arquiteto de contexto: a habilidade é externalização de tácito e é treinável

**Construto.** Arquiteto de contexto (Marzagão, 2026) mais a distinção de Farach e coautores
entre *scaffolding* cognitivo e comportamental.

**Predição.** Em trabalho mediado por agente, o desempenho é melhor predito pela capacidade
de externalizar conhecimento tácito em instrução executável do que por profundidade de
domínio isolada, e as duas capacidades são separáveis. Segunda parte: *reframing* cognitivo
eleva a capacidade de externalização; protocolo comportamental de uso não eleva, e pode
reduzir.

**Variáveis.** Independentes: profundidade de domínio medida sem ferramenta; capacidade de
externalização medida pela qualidade do briefing produzido, avaliada separadamente do output.
Dependente: qualidade do output do agente na tarefa de domínio.

**Identificação.** Randomizar a intervenção formativa entre *reframing* e protocolo, com
domínio medido na linha de base. Avaliar briefing e output por juízes cegos à condição.

**Falsificação.** Se a variância do output for explicada por domínio e a qualidade do
briefing não acrescentar nada, o construto não tem função incremental.

**Custo e prazo.** Baixo. É o experimento mais barato do conjunto e o mais rápido de rodar.

---

# Unidade 2 — Os gestores

## H2.1 Calibração de autonomia é competência distinta de delegação a humanos

Esta é a de maior valor prático imediato e a que eu priorizaria primeiro.

**Construto.** Calibração de autonomia com os quatro parâmetros do Capítulo 4:
especificidade do contexto, reversibilidade das ações, frequência de casos de fronteira e
custo de erro.

**Predição.** A afirmação forte do livro é que delegar a agente não é extensão natural de
delegar a humano, porque os sinais implícitos que permitem calibrar estão ausentes. Isso
implica correlação baixa entre habilidade de delegação humana e habilidade de calibração de
autonomia no mesmo gestor. E implica que a segunda, não a primeira, prediz taxa de incidente
com agentes na unidade.

**Variáveis.** Independentes: escore de delegação humana por instrumento validado; escore de
calibração de autonomia por instrumento novo, construído a partir dos quatro parâmetros e
aplicado por vinhetas. Dependentes: taxa de incidente com agente, custo de retrabalho,
proporção de agentes rebaixados ou desativados por lacuna de governança.

**Identificação.** Corte transversal com múltiplas unidades da mesma organização, controlando
por complexidade de processo e maturidade de adoção. Painel se houver duas ondas.

**Falsificação.** Se os dois escores correlacionarem forte, calibração não é competência nova,
e a implicação de treinamento do livro desaparece.

**Ancoragem externa.** A previsão do Gartner de que até 2027 40% das empresas vão rebaixar ou
desativar agentes autônomos por lacunas de governança identificadas apenas após incidente em
produção dá à hipótese uma variável dependente com base setorial.

---

## H2.2 A assinatura observável do debt cognitivo organizacional é a divergência entre os dois loops

**Construto.** DCO (Marzagão, 2026) mais a distinção de Argyris e Schön entre single e
double-loop learning.

O problema de DCO como construto é que ele é estoque latente, e estoque latente é difícil de
medir diretamente. A saída é prever *onde* o sinal aparece primeiro.

**Predição.** Organizações com DCO mais alto apresentam melhora sustentada em indicadores
dentro dos parâmetros e degradação simultânea na taxa e na qualidade de revisão dos próprios
parâmetros. O DCO prediz a *divergência* entre os dois, não o nível de nenhum dos dois
isoladamente. É a formalização de "todos os indicadores verdes, estratégia obsoleta".

**Variáveis.** Proxies de DCO: amplitude de controle, carga de reunião, frequência de
interrupção, latência de decisão, segurança psicológica pela escala de Edmondson.
Single-loop: tendência de KPI operacional. Double-loop: taxa e profundidade de revisão de
parâmetro, medida por redefinição de métrica, mudança de set point, projeto encerrado por
decisão e não por conclusão, reformulação de segmento.

**Identificação.** Painel organizacional com efeito fixo de firma, porque o interesse está na
trajetória interna e não no nível entre firmas.

**Falsificação.** Se os proxies de DCO predisserem queda nos dois loops, o mecanismo
específico cai e sobra uma história convencional de sobrecarga e estresse.

**Por que vale.** Operacionaliza a *competency trap* de March por divergência de dois sinais
em vez de declínio de um. Isso é mensurável em dado de arquivo e não existe na literatura
nessa forma.

---

## H2.3 O critério de atrito produtivo deliberado é prospectivamente preditivo

**Construto.** Atrito produtivo deliberado, com o critério operacional do Capítulo 4: se a
remoção do atrito tornaria a pessoa incapaz de supervisionar o output do agente que a
substituiu naquela tarefa, o atrito estava formando capacidade.

**Predição.** A classificação feita por gestores segundo esse critério, antes da automação,
prediz qual equipe retém capacidade de supervisão doze a dezoito meses depois.

**Variáveis.** Independente: classificação ex ante de cada tarefa como atrito formativo ou
ineficiência removível. Dependente: capacidade de supervisão medida pelo protocolo de
ferramenta removida da H1.1, mais taxa de detecção de erro de agente em auditoria cega.

**Identificação.** Implantação escalonada, com automação de tarefas de ambos os tipos em
ordem determinada por disponibilidade de fornecedor e não por escolha do gestor. Isso separa
o critério da preferência de quem classifica.

**Falsificação.** Se a classificação não predisser, o critério é retoricamente elegante e
operacionalmente vazio, e o Capítulo 4 perde sua recomendação central.

---

## H2.4 Mentoria cruzada age sobre dispersão de julgamento, não sobre média

**Construto.** Arquitetura de mentoria cruzada do Capítulo 6, contra as duas faces do risco
tácito: saída pelo topo e erosão pela base.

**Predição.** Mentoria reversa, de júnior a sênior sobre ferramenta, e mentoria tradicional,
de sênior a júnior sobre julgamento, têm efeitos assimétricos, e a combinação é
superaditiva sobre capacidade absortiva organizacional. O mecanismo observável é aumento de
redundância de julgamento, medido como redução da concentração de quem consegue decidir, e
não como elevação da média.

**Variáveis.** Dependente principal: dispersão da capacidade de julgamento na equipe,
medida por variância ou Gini de um instrumento de decisão aplicado a todos. Dependente
secundária: tempo de recuperação após saída não planejada de um portador de expertise.

**Identificação.** Ensaio aleatorizado por equipe em quatro braços: só reversa, só
tradicional, ambas, controle com diagnóstico.

**Falsificação.** Se o efeito aparecer na média e não na dispersão, a tese de redundância cai
e o programa é apenas treinamento com outro nome.

---

## H2.5 O viés etário contra 40 mais tem custo mensurável em supervisão de agentes

**Construto.** Gen X como ponte tecnológica (Capítulo 8), contra o dado de PwC e FGV Brasil
de que 72% dos gestores de seleção preferem candidatos abaixo de 40 para liderança e 86% das
empresas não têm plano de carreira acima de 40.

**Predição.** Firmas com maior proporção de profissionais acima de 40 em posições de
supervisão sobre sistemas agênticos apresentam menor taxa de incidente e maior captura de
valor de IA, controlando por setor, porte e investimento em IA. O efeito deve sobreviver ao
controle por tempo de casa, porque a hipótese é sobre substrato de julgamento contextual e
não sobre antiguidade na firma.

**Variáveis.** Independente: composição etária de posições de supervisão. Dependentes: taxa
de incidente, ganho de produtividade retido.

**Identificação.** Esta é a hipótese com melhor dado brasileiro disponível. RAIS dá idade por
ocupação por firma, com cobertura do emprego formal inteiro. PINTEC dá adoção de tecnologia e
inovação. O pareamento das duas bases é factível e não exige coleta.

**Falsificação.** Se o efeito desaparecer ao controlar por tempo de casa, é experiência na
firma e não coorte, e a tese geracional do Capítulo 8 perde essa perna.

---

# Unidade 3 — Estratégia empresarial e inovação corporativa

## H3.1 A capacidade absortiva organizacional declina de forma composta

Esta é a afirmação mais forte e mais falsificável do livro, e a que eu levaria primeiro a
um journal de estratégia.

**Construto.** Capacidade absortiva organizacional (Cohen e Levinthal) com a extensão do
Capítulo 9: cada mudança subsequente é mais caro de absorver do que a anterior, porque o
estoque prévio que tornaria a absorção rápida está menor.

Essa é uma predição sobre segunda derivada, o que é raro e testável.

**Predição.** Em firmas que automatizaram tarefas formativas de entrada cedo, o custo e o
tempo de absorção de cada onda tecnológica sucessiva aumentam. Em firmas que preservaram
tarefas formativas, a curva é plana ou declinante.

**Variáveis.** Dependente: inclinação do custo de absorção ao longo de adoções sucessivas na
mesma firma, com custo medido por tempo até uso produtivo, retrabalho e proporção de projetos
que não saem do piloto. Independente: timing e profundidade da automação de tarefas de
entrada.

**Identificação.** Dentro da firma, com efeito fixo, porque a comparação de interesse é
temporal. Instrumento possível para o timing da automação: disponibilidade de fornecedor por
categoria de tarefa, que é exógena à decisão da firma.

**Falsificação.** Se o custo de absorção for plano ou declinante independentemente da
automação de entrada, a tese do declínio composto cai, e com ela a articulação central entre
as Partes II e III do livro.

---

## H3.2 Make-or-buy de talento: internalizar julgamento prediz retenção de valor

**Construto.** Make-or-buy de talento com a atualização de Williamson do Capítulo 9: o novo
núcleo de especificidade de ativo não é execução de tarefa, é julgamento contextual sobre
quando e como usar agentes.

**Predição.** Firmas que internalizam papéis de julgamento e externalizam execução capturam
maior parcela do ganho de produtividade do que firmas com o padrão inverso, controlando pelo
nível de investimento em IA. A matriz de decisão cruza especificidade de contexto por
velocidade de obsolescência do julgamento.

**Variáveis.** Independente: padrão de internalização, com papéis classificados pelas duas
dimensões da matriz. Dependente: captura de valor, medida como parcela do ganho de
produtividade retida em margem em vez de repassada em preço.

**Falsificação.** Se o nível de investimento em IA predisser sozinho e o padrão de
internalização não acrescentar nada, a atualização de Williamson não se sustenta.

---

## H3.3 No canal agêntico, seleciona a dimensão de escassez mais difícil de imitar

**Construto.** Modelo EPM de escassez percebida, com as seis dimensões de tempo, atenção,
competência contextual, exclusividade, autenticidade e acesso, mais comércio agêntico e
fornecedor invisível do algoritmo (Diver, SPIW 2026).

**Predição.** Em ambiente de compra mediada por agente, a seleção do fornecedor é predita
pelas dimensões difíceis de imitar, autenticidade e acesso, e não pelas fáceis de sinalizar,
exclusividade e tempo. Corolário: marca com histórico verificável é menos penalizada do que
marca com narrativa de marketing, porque o agente verifica de forma independente.

**Identificação.** Esta é a única hipótese do conjunto que pode ser testada nesta semana, com
custo quase nulo. Rodar tarefas de compra através de agentes, com fornecedores codificados
independentemente nas seis dimensões por juízes cegos, e regredir seleção sobre as dimensões,
controlando por preço e disponibilidade.

**Falsificação.** Se a seleção acompanhar apenas preço e disponibilidade, o EPM não acrescenta
nada no canal agêntico, e o Capítulo 9 perde a ponte entre posicionamento e comércio agêntico.

**Por que priorizar.** Barata, rápida, e quase ninguém está fazendo. É a que tem maior chance
de virar artigo antes de o campo lotar.

---

## H3.4 A divergência entre os dois loops prediz obsolescência estratégica

Versão de firma da H2.2, com variável dependente de resultado em vez de processo.

**Predição.** Firmas com KPI operacional em melhora e taxa de revisão de parâmetro em queda
têm probabilidade mais alta de obsolescência estratégica em três a cinco anos, medida por
perda de participação, reestruturação forçada ou troca de controle, do que firmas com os dois
sinais em melhora. O padrão de risco é indicador verde com estratégia envelhecendo.

**Identificação.** Arquivo. KPI de demonstração financeira; revisão de parâmetro a partir de
divulgação de estratégia, redefinição de segmento, descontinuação de linha, mudança de
composição de conselho. Análise de sobrevivência.

**Falsificação.** Se a divergência não predisser nada além do que o nível de desempenho
operacional já prediz, o sinal é redundante.

---

## H3.5 A janela de legitimidade da média empresa brasileira está se fechando

**Construto.** Legitimidade social como quarta dimensão de durabilidade, com a afirmação
específica do Capítulo 9 de que a grande empresa com marca consolidada tem proteção parcial
contra invisibilidade algorítmica e a média empresa tem janela menor.

**Predição.** A penalidade por ausência de histórico verificável em seleção mediada por
agente é maior para empresa média do que para grande, e cresce ao longo do tempo. Efeito de
interação entre porte e presença de histórico verificável, com tendência temporal positiva.

**Identificação.** Extensão longitudinal do desenho da H3.3, com painel de fornecedores de
portes diferentes e medições repetidas conforme os modelos evoluem.

**Falsificação.** Se a penalidade for igual entre portes, a implicação estratégica específica
para média empresa brasileira, que é boa parte do público do livro, não se sustenta.

---

# O que o corpus ainda não sustenta, e que é preciso declarar

**Os cenários de 2050 não são hipóteses e não devem ser apresentados como tal.** O Brasil
Assimétrico, com 15, 45 e 40 por cento, é construção de cenário. Cenário não é falsificável
por desenho, e tratá-lo como predição testável enfraqueceria o resto. O que é testável são os
pontos de inflexão do Apêndice D, individualmente.

**DCO e DIP não têm instrumento.** Ambos são construtos autorais com fundamentação
neurobiológica e filosófica, e nenhum tem escala validada. Antes de qualquer estudo
substantivo há um estudo de desenvolvimento e validação de instrumento, com análise fatorial
e validade convergente e discriminante. Isso é um artigo próprio, e provavelmente o primeiro
a escrever.

**O framework de durabilidade tem quatro dimensões e nenhuma medida publicada.** Mesma
situação. A hipótese H3.1 contorna isso testando uma dimensão isolada, que é a estratégia
correta: validar uma antes de propor as quatro.

**Vários números do livro vêm de fonte secundária ou de survey de consultoria.** Deloitte,
McKinsey, Gartner, LSE e Protiviti, PwC e FGV. Servem para motivar hipótese e não para
sustentá-la. Qualquer submissão vai exigir que a evidência central venha de dado primário ou
de registro administrativo.

**Uma ausência que vale nomear.** Nenhuma hipótese acima testa o efeito sobre quem está fora
do emprego formal. Os 40% de informalidade estrutural do cenário provável não aparecem em
CAGED, RAIS ou PINTEC, e não aparecem em nenhum desenho proposto aqui. É a maior lacuna do
conjunto, e ela é herdada do livro.

---

# Ordem de execução sugerida

Por relação entre custo e retorno, não por importância.

1. **H3.3**, comércio agêntico e EPM. Barata, rápida, campo vazio.
2. **H1.4**, arquiteto de contexto. Experimento pequeno, desenho limpo.
3. **H2.5** e **H3.1**, com RAIS, PINTEC e CAGED. Sem coleta nova.
4. **H2.1**, calibração de autonomia. Exige instrumento, e o instrumento tem valor próprio.
5. **H1.3**, prazo do paradoxo da senioridade. Depende de acesso a dado operacional logado.
6. **H2.2** e **H3.4**, divergência entre loops. Depende de operacionalizar revisão de
   parâmetro, que é a parte difícil.
7. **H1.1**, **H1.2**, **H2.3**, **H2.4**. Exigem janela de doze a dezoito meses e, nos casos
   de DIP e DCO, desenvolvimento de instrumento antes.

---

## Fontes primárias do levantamento

MARZAGÃO, Daniela. *O Trabalho que Vem: Como Você e Sua Empresa se Preparam para o Futuro*.
Dez capítulos, quatro apêndices, junho de 2026. Doc
`1qpNZnCtYJ2iB3U9NDp8S170FCxJDhVe5vKv9DEKW2Aw`.

Corpus de ensaios da série VibeCoding em Contexto, abril a setembro de 2026, indexado em
`ensaios/INDEX.md`.

Artigos acadêmicos: delegação identitária patológica e o instrumento e suas condições de
operação, submetidos à RAE; heurística da escassez no consumo hipermoderno, submetido ao JBR.
