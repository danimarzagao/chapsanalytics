# Padrões de trabalho com textos da Daniela

Este arquivo vale para todo agente que trabalhar neste repositório: artigos acadêmicos,
ensaios da série VibeCoding em Contexto, pesquisa semanal e revisões.

As regras abaixo não são preferências de estilo. Cada uma vem de um erro que já foi
cometido e verificado. A origem está registrada em `docs/licoes-verificacao.md`.

---

## 1. Regras de argumento

**1.1 Não declare experimento controlado o que é seleção pela variável dependente.**
Escolher o maior sucesso e o maior fracasso, notar que diferem e chamar a diferença de
explicação é o vício mais velho da análise de caso. Se o argumento precisa de um par,
o par tem que ser de duas tentativas sérias sob o mesmo regime. Comparar uma empresa
com uma fraude não prova nada, porque qualquer variável separa as duas.

**1.2 Antes de afirmar "mesma condição", liste as condições e cheque uma a uma.**
Financiamento, sanção, origem do capital, competência dos fundadores, acesso a
fornecedor. Se qualquer uma diverge, a afirmação cai.

**1.3 Anomalia não é ruído a suavizar. É o ponto mais interessante do texto.**
Se um caso não cabe no modelo proposto, ele vai para o corpo do artigo, nomeado, e de
preferência com a pergunta em aberto declarada. Modelo que não explica o quinto caso é
lista bonita, não modelo.

**1.4 Narrativa corporativa não é cronologia verificada.**
Sempre pergunte quem está contando, quando, e com que interesse. Declaração feita pela
parte interessada depois do fato é evidência sobre o presente da declaração, não sobre
o passado que ela descreve. Trate como plausível, nunca como estabelecido.

**1.5 Desconfie de dilemas limpos.**
"A construiu" contra "A apenas revelou" costuma esconder que as duas coisas são
verdadeiras em camadas diferentes. Antes de escolher um lado, verifique se o fenômeno
tem subcamadas com respostas distintas.

**1.6 Defeater vai antes, não depois.**
Se existe um fato que enfraquece o número de abertura, ele entra logo depois do número.
Enterrar a objeção no fim, como item de uma lista de alternativas, é construir argumento
sobre base que o próprio texto sabe que é frágil.

**1.7 Nota de verificação não autoriza número não verificado.**
Ou o dado sustenta o argumento e precisa estar checado, ou não sustenta e não abre o
texto. Declarar incerteza no rodapé não conserta a abertura.

**1.8 Nomeie a tensão que você não resolve.**
Quando a evidência puxa nos dois sentidos, diga isso no corpo do texto. Tensão nomeada
é honestidade. Tensão implícita é o leitor descobrindo sozinho que o argumento tem
buraco.

**1.9 Afirmação comparativa exige checagem, mesmo quando parece óbvia.**
Frases do tipo "quase nenhum país ocidental faz X" caem em cinco segundos de busca.
Se a frase é sobre o que outros fazem ou deixam de fazer, cheque antes de escrever.

**1.10 Antes de declarar pergunta em aberto, veja se o autor já respondeu.**
Escrever "o teste está disponível, basta esperar" sobre um controle que já está no
apêndice do próprio artigo é pior do que não levantar a objeção. Leia os apêndices e as
seções de robustez antes de apresentar uma explicação concorrente como não testada.

**1.11 Cheque se a tendência antecede a causa que você atribui a ela.**
Uma divergência que já existia antes do evento que você está usando como explicação não
invalida o argumento, mas muda o que ele pode afirmar. Procure a linha de base anterior
antes de datar o início do fenômeno. Se o próprio autor reconhece a complicação e
apresenta defesa, isso é defesa, não ausência de problema, e o texto tem que dizer isso.

**1.12 Correção é afirmação, e exige a mesma verificação que o erro que ela corrige.**
Caso de origem: acusei o texto do HackTown de lavar autoria ao atribuir ao Banco Mundial
um contrafactual de produtividade, e escrevi um parágrafo de correção dizendo que a fonte
era Veloso e coautores. A autora abriu o relatório e a frase está no prefácio de *Emprego
e Crescimento: A Agenda da Produtividade* (Banco Mundial, 2018), em voz própria. A
atribuição original estava certa e a minha correção estava errada. Corrigir dá uma
sensação de rigor que dispensa checagem, e é exatamente aí que o erro entra. Antes de
publicar uma correção, abra o documento que ela invoca.

**1.13 Escreva sobre onde a exceção migra, não sobre a regra bonita.**
Todo regime tem a via rápida com prazo declarado e a via lenta sem relógio. O
comportamento do sistema é decidido pela segunda. Caso de origem: o artigo "Seis dias
úteis" celebrava a pista rápida da divulgação da OpenAI e passava ao largo da terceira
trilha, sem prazo fixo, que cede prioridade a obrigações de segurança e jurídicas
avaliadas pela mesma parte que decide divulgar. O título defendia a tese fraca.

**1.14 Prefira a formulação mais estreita que ainda faz o trabalho.**
Afirmação larga é fácil de escrever e fácil de derrubar. Estreitar não enfraquece:
blinda. Caso: "não há denominador" quebra diante de duas taxas publicadas; "falta o
denominador do sistema de reporte, e a própria empresa declara que a lista não é
exaustiva" sobrevive e diz mais.

**1.15 Um final só.**
Perguntas de fechamento, parágrafo de fecho e nota de verificação em sequência são três
finais, e em newsletter o leitor sai no primeiro. Decida qual é o fim. Se a melhor
pergunta está em terceiro lugar, ela não vai ser lida.

**1.16 Procure o mesmo componente em incidentes separados.**
Caso: o dia zero de julho aconteceu num proxy de cache de registro de pacotes, e o
quinto incidente de setembro usou o Artifactory interno como mural de recados. A mesma
peça de encanamento nos dois. A leitura responsável é perímetro, não conspiração, e é o
tipo de observação que a imprensa de tecnologia não faz.

---

## 2. Regras de números

**2.1 Uma régua por afirmação, e diga qual é.**
Antes de comparar duas medidas, prove que o instrumento é o mesmo. Isto é análise do
sistema de medição, e vale para dado de mercado exatamente como vale para processo.
Encadear três fontes com metodologias diferentes produz uma curva que nenhuma delas
desenhou.

**2.2 Orçamento anunciado não é dinheiro desembolsado.**
Sempre separe promessa de aporte. A diferença costuma ser de uma ordem de grandeza, e
costuma ser onde mora a história de verdade.

**2.3 Cheque agregação antes de somar.**
Participação de mercado publicada frequentemente já soma dois ou mais atores. Somar de
novo é dupla contagem. Leia a definição da série antes de usar o número.

**2.4 Unidade importa: die, chip, unidade embalada, unidade despachada não são a mesma coisa.**
Meta de produção não é produção. Produção não é despacho.

**2.5 Datar toda declaração oficial.**
Declaração sem data sugere admissão recente. Se é de seis anos atrás, o leitor precisa
saber.

**2.6 Superlativo invoca um ranking. Cheque a unidade do ranking.**
"Entre os dez maiores do mundo" só é verificável se a métrica citada for a métrica do
ranking. FP16 e FP64 são réguas diferentes, com uma ordem de grandeza entre elas.
Este tipo de erro costuma ser a própria notícia.

**2.7 Intervalo largo entra como ordem de grandeza, com a palavra "estimativa".**
Nunca como ponto.

**2.8 Razão derivada esconde os números brutos. Publique os brutos.**
"Sete vezes mais" é menos informativo que "52% contra 7%", e a razão sozinha impede o
leitor de ver que metade das vagas de entrada deixou de ser vaga de entrada. Sempre que
encontrar uma razão, ache os dois números que a produziram e use os dois.

**2.9 Afirmação de ausência exige a fonte primária aberta. É a mais frágil que existe.**
"Não há denominador", "ninguém publicou", "não existe dado sobre isso". Esse tipo de
frase é derrubada em trinta segundos por qualquer leitor que abra a página que você não
abriu. Caso de origem: escrevi que a divulgação da OpenAI não tinha denominador, e ela
publicava prevalência em dois casos, 2,15% dos resumos de compactação do GPT-5.6 Sol e
0,27% dos do GPT-6 Astra. Se a ausência sustenta o argumento, verificá-la é a primeira
tarefa, nunca a última.

**2.10 Recalcule todo intervalo de tempo antes de narrá-lo.**
"Cinco meses depois" eram dois. Data de publicação própria e alheia entram na conta, não
na memória, e a cronologia costuma ser a espinha do argumento.

**2.11 Número que cresce com o tempo tem prazo de validade.**
Totais acumulados, anos de operação, número de signatários, contagem de membros. O ASRS
passou de 1,8 para 2,3 milhões de relatos e de quarenta e cinco para cinquenta anos de
operação entre uma citação e a seguinte. Rebusque, não reaproveite.

---

## 3. Regras de fonte

**3.1 Referência sem autor identificável não é referência.**
Nada de "reportagem sobre X, conforme a nota de verificação". Todo número tem fonte
nomeável: autor, veículo, data.

**3.2 Verifique se a fonte citada sustenta o uso que você faz dela.**
Já aconteceu de a fonte citada como apoio conter a versão concorrente que contradiz o
argumento. Ler a fonte inteira, não a citação de segunda mão.

**3.3 Caracterize o crítico pelo que ele de fato objeta.**
Dizer que uma tese "tem crítica relevante" sem saber onde a crítica bate costuma
subestimar a própria posição. Frequentemente o núcleo que você usa sobrevive melhor do
que a ressalva genérica sugere.

**3.4 Enquadramento contestável é atribuído, não afirmado.**
Se a afirmação é a leitura de um autor e há contraexemplos plausíveis, escreva que é a
leitura dele. Deixe o leitor discordar do autor, não de você.

**3.5 Antes de chamar de triangulação, prove que as fontes são independentes.**
Esta é a regra mais cara da lista, porque o erro é invisível. Três números concordando
podem ser uma pesquisa medida três vezes: relatório de consultoria ou de laboratório
corporativo frequentemente cita um trabalho acadêmico, e a citação de segunda mão aponta
de volta ao mesmo instrumento numa safra anterior. Para cada fonte, abra a nota de rodapé
e veja de onde o número veio. Se duas apontam para o mesmo lugar, você tem uma série
dentro de um instrumento, não acordo entre instrumentos. A série não é pior; é outra
coisa, e afirma menos.

**3.6 Fonte primária bloqueada é tarefa pendente, não condição permanente.**
Registrar "o proxy bloqueou o domínio" e seguir é aceitável em rascunho e inaceitável em
texto publicado. Tente de novo antes de fechar, por outra rota se preciso. E nunca
afirme o que a fonte não contém quando você não conseguiu abri-la: foi assim que a regra
2.9 nasceu.

**3.7 Norma, circular e regulamento têm revisão vigente.**
Cheque a letra antes de citar. AC 00-46E contra 00-46F é a diferença entre parecer que
você leu e ter lido.

**3.8 Seu artigo anterior é fonte secundária sobre o mundo.**
Reaproveitar número do próprio texto sem reverificar é a regra 3.5 com o agravante de ser
autoinfligido. Caso: reusei as 18.476 propostas do conselho australiano vindas de um
texto meu, sem checar, três semanas depois de um episódio em que exatamente esse hábito
deu errado. Verificar custou uma consulta, e a fonte é Bromham, Dinnage e Hua, *Nature*
534:684–687, 2016.

**3.9 Nomeie as pessoas. É ganho gratuito.**
"Pesquisadores questionaram" custa o mesmo que "Alexander Meinke, da Apollo Research, e
Henry Papadatos, da Safer AI, questionaram", e vale muito mais.

**3.10 Ideia achada numa análise secundária é atribuída a ela.**
Apresentar como consenso da cobertura o que veio de um único blog é lavagem de autoria na
direção oposta à da regra 1.12, e o leitor que for atrás descobre.

**3.11 Paráfrase preserva o mecanismo, não só a conclusão.**
Caso: parafraseei "pode ampliar capacidades involuntariamente" e perdi o mecanismo
declarado, que era agentes se apoiarem em trabalho de outras rodadas e assim aumentarem o
poder de computação efetivo em tempo de teste. A paráfrase enfraqueceu o achado que eu
estava dizendo ser o mais importante do texto.

**3.12 A ressalva do autor viaja junto com o número.**
O comunicado de Stanford abre com "no widespread displacement". Quem cita os 19% sem isso
está citando metade, e a metade que falta é a que protege contra a leitura alarmista.

**3.13 Toda referência aparece no corpo, e toda citação do corpo aparece nas referências.**
Referência fantasma é o tipo de coisa que um leitor atento nota e que custa credibilidade
desproporcional ao erro. `scripts/voz.py` checa automaticamente.

**3.14 Procure a versão mais forte do fato dentro da própria documentação.**
Caso: tratei a neutralidade da NASA no sistema de reporte da aviação como característica
feliz. A documentação diz que foi a FAA que pediu à NASA, separada dos órgãos de
fiscalização e investigação, que administrasse o sistema. O regulador abriu mão de receber
o relato. É um fato muito mais forte e muda o fecho do texto inteiro. Para cada fato que
carrega peso, pergunte se a fonte tem uma versão melhor do que a que você está usando.

**3.15 Incidente tem singular, plural, data e particulares.**
Caso: escrevi "modelos subiram arquivos para a internet". Era um modelo, não lançado, em
duas datas, subindo registros para serviços públicos específicos, numa tarefa específica.
Generalizar o particular é erro silencioso, porque o texto continua soando verdadeiro.

---

## 4. Regras de forma (protocolo do humanizador)

Os textos passam por detecção de escrita gerada. Rode `python3 scripts/voz.py <arquivo>`
antes de entregar qualquer ensaio. As saídas são gatilhos de revisão, não veredito.

**4.1 Travessões: no máximo 2 a cada 500 palavras.**
Erro já registrado: 27 travessões em 2.800 palavras, 2,5 vezes o teto.

**4.2 O molde "Não é X. É Y." é banido por padrão, e não só na versão tripla.**
A proibição vale para a ocorrência isolada, não apenas para o bloco de negações paralelas.
Caso: quatro ocorrências num único ensaio que passava em todas as outras métricas. O
detector do script pega parte delas; a leitura pega o resto.

**4.3 Evite o sanduíche numerado.**
"As quatro condições" seguidas de "três perguntas" produz arrumação que a evidência
raramente sustenta. Se a lista tem quatro itens e o quinto caso não cabe, o problema é
a lista.

**4.4 Negrito é ênfase inline, não tese.**
Não abra todo parágrafo com negrito, e não use negrito para marcar a frase que você
gostaria que fosse citada.

**4.5 Fragmentação legítima: a segunda frase sobrevive sozinha?**
Ponto final em meia oração manufatura variação. "É contorno do medidor.", "É uma
quantidade de histórias.", "Foi criar o lugar.", "Acha olhando para o caminho." são todas
metades de frase com ponto no meio. Junte, e deixe o ritmo aparecer onde o pensamento
muda de unidade.

**4.6 O par de métricas que importa.**
Desvio-padrão do tamanho de frase deve **subir** enquanto a proporção de frases de até
seis palavras **cai**. Desvio alto acompanhado de muitas frases curtíssimas é burstiness
manufaturada. Alvos práticos, medidos pelo script: desvio-padrão em 11 ou mais, frases
curtíssimas em 10% ou menos. Referência do caso: o original marcava 16,2 de média com
10,2 de desvio e 15,9% de frases curtíssimas; a reescrita subiu para 20,9 e 11,7 com 8,2%.

**4.7 Preservar sempre, porque é o que marca autoria humana de verdade:**
primeira pessoa; mudança de curso admitida no meio do texto; ancoragem em datas e
nomes próprios; nota de verificação; e a admissão explícita do que não se sabe.

---

## 5. Ordem de trabalho

**Duas rodadas de verificação, sempre.**

A primeira, antes de montar o texto, funciona como projeto e decide o que pode abrir o
artigo. A segunda, com o texto pronto, contra as fontes primárias, e é ela que pega o que
a primeira errou. A versão final de "O pneu sobressalente" mudou duas vezes antes de
existir; a segunda rodada de "Nunca foi a cultura" mudou cinco números e desfez uma
correção da primeira.

Nota escrita antes é projeto. Nota escrita depois é desculpa.

**A nota de verificação registra as correções em relação à versão anterior.** Quando um
texto muda entre rascunhos por causa de verificação, isso vai na nota, com o que estava
escrito antes e o que a fonte diz. É a mesma prática que a série cobra das empresas sobre
as quais escreve.

Ao entregar qualquer texto, declare explicitamente:
- o que foi verificado em fonte primária;
- o que veio de cobertura secundária, com o veículo nomeado;
- o que não foi possível verificar e por quê;
- o que mudou desde a versão anterior.

Nunca apresentar como conferido o que não foi conferido na origem.

---

## 6. Ferramentas

- `/critica-academica [ID] [journal]` — revisão dura de artigo acadêmico para submissão
- `/verificacao-factual [arquivo]` — verificação de argumento, números e fontes de ensaio
- `python3 scripts/voz.py [arquivo]` — diagnóstico quantitativo de voz da seção 4
