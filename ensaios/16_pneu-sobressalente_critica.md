# Crítica e verificação — "O pneu sobressalente"

Diagnóstico em três camadas: o que quebra o argumento, o que quebra os números, o que quebra as fontes. Ordenado por gravidade, não pela ordem do texto.

---

## Parte 1 — Argumento

### 1.1 O "experimento controlado" não é controlado. É o problema mais grave do texto.

O parágrafo que o próprio artigo marca como "a única conclusão sólida deste texto" é este:

> "A Huawei e a HSMC operaram sob exatamente a mesma proteção. Mesmo Estado, mesma política, mesmo bloqueio externo, mesmo acesso a subsídio."

As quatro afirmações são falsas.

| | Huawei | HSMC (Wuhan Hongxin) |
|---|---|---|
| Quem financiou | Receita própria; subsídio e incentivo fiscal centrais após 2019 | Governo do distrito de Dongxihu, Wuhan. Sem Big Fund, sem dinheiro central |
| Dinheiro público efetivamente aportado | Não divulgado | ¥15,3 bi (~US$ 2,4 bi) até dez/2019 |
| Bloqueio externo | Entity List desde maio/2019; FDPR em set/2020 | Nunca sancionada. Comprou litografia da ASML |
| Quem fundou | Engenharia com 20+ anos de P&D | Três sócios sem experiência em semicondutores. Um vinha de restaurantes e venda de bebida de arroz |
| Capital registrado | Real | Majoritariamente fictício |

Comparar as duas não é um experimento controlado. É comparar uma empresa com uma fraude. E a fraude é o caso mais fácil de explicar de toda a indústria chinesa, o que faz dela o pior contraste possível: qualquer variável explica a diferença, inclusive "um dos lados era golpe".

Há também um problema metodológico clássico embutido: **seleção pela variável dependente.** O texto escolhe o maior sucesso e o maior fracasso, observa que diferem, e declara a diferença explicativa. Para sustentar "proteção não explica nada", o par precisaria ser de duas tentativas sérias sob o mesmo regime.

A conclusão pode continuar de pé. A evidência oferecida para ela, não.

### 1.2 O caso que desmonta a versão fácil e que o artigo não menciona: a YMTC

O texto enterra a Tsinghua Unigroup no cemitério ("O projeto foi cancelado em 2022. A empresa foi à falência"). Duas correções e uma consequência.

**Correção 1.** A Unigroup não faliu. Passou por recuperação judicial (破产重整), concluída em julho de 2022, com troca de controle para um consórcio liderado pela Wise Road/JAC. Reorganização, não liquidação.

**Correção 2.** A Unigroup controlava a **YMTC**, única fabricante chinesa de 3D NAND. A YMTC sobreviveu à reestruturação, sobreviveu à Entity List de dezembro de 2022, está construindo a terceira fábrica em Wuhan e monta uma linha com equipamento doméstico mirando cerca de 15% do mercado global de NAND até o fim de 2026.

**Consequência.** A YMTC é a anomalia que interessa. Ela não tinha os "quinze anos de estoque prévio" da HiSilicon. Tinha dinheiro estatal, demanda cativa e um mercado protegido, exatamente o combo que o artigo diz não bastar. Se ela funcionou, ou a lista de quatro condições está errada, ou "estoque prévio" é bem mais barato de construir do que o texto sugere.

Isso não enfraquece o artigo. É a coisa mais interessante que ele poderia investigar, e cai direto na regra que você aplica nos seus textos técnicos: anomalia não é ruído a suavizar, é o ponto mais interessante do argumento.

### 1.3 A cronologia de 2004 é a Huawei contando, em 2019, a história de 2004

Este é o ponto que muda o texto de bom para incomum.

O artigo constrói seu pivô inteiro sobre a data de fundação da HiSilicon e sobre a intenção declarada por trás dela ("uma hipótese explícita de trabalho: um dia, todos os chips americanos ficariam indisponíveis"). A fonte dessa intenção é a carta de He Tingbo. De 2019. Escrita pela parte interessada, no dia seguinte à sanção, para consumo interno e imediatamente viral.

E existe uma versão concorrente da origem. O RUSI atribui a fundação da HiSilicon em 2004 à estratégia de autossuficiência que se seguiu à **tentativa frustrada de aquisição da Huawei pela Motorola em 2003**. Motivo de controle acionário e independência, não previsão de sanção.

As duas coisas podem ser verdade ao mesmo tempo. O que não se sustenta é tratar a narrativa corporativa como cronologia verificada. Quinze anos de documentos não vieram a público. O que veio a público foi uma carta.

Você tem uma metáfora melhor do que a que está no texto, e ela é de teatro: a espingarda de Tchekhov está pendurada na parede do primeiro ato porque alguém já escreveu o terceiro. A Huawei mostrou a espingarda em 2019 e disse que ela estava lá desde 2004.

### 1.4 Falso dilema: "a sanção construiu" versus "a sanção encontrou estoque"

As duas não são exclusivas, e a divisão limpa esconde o fato mais importante da história.

A HiSilicon de 2004 era **fabless**. Projetava chips e dependia da TSMC para fabricá-los. O pneu sobressalente cobria design. Não cobria fabricação, EDA, empacotamento avançado nem HBM.

A regra que realmente machucou não foi a Entity List de maio de 2019. Foi a **Foreign Direct Product Rule de setembro de 2020**, que cortou o acesso à TSMC. Para essa, não havia pneu. O 7nm da SMIC que apareceu no Mate 60 Pro em agosto de 2023 é capacidade construída **depois** do choque, sob restrição, não recuperada do cofre.

Ou seja: o estoque prévio determinou a **velocidade**. A restrição determinou a **direção**, e uma parte relevante da pilha foi de fato construída sob pressão. A frase de fechamento do artigo ("restrição não constrói nada, ela revela o que já estava construído") é elegante e forte demais para a evidência.

### 1.5 A causalidade reversa está no lugar errado

O artigo põe "causalidade parcialmente reversa" como a quinta de cinco explicações concorrentes, perto do fim. Ela não é uma explicação entre outras. É um **defeater** do número que abre o texto.

E ficou ainda mais forte do que o artigo supõe: em 2026 os EUA liberaram a venda do H200 para a China com tarifa de 25% e teto de unidades, e em seguida **Pequim restringiu a importação**. A queda da Nvidia na China tem um componente de proibição americana de vender e um componente de decisão política chinesa de não comprar. Nenhum dos dois é engenharia ganhando de engenharia.

Recomendação estrutural: mover para logo depois dos números, antes de qualquer argumento ser construído sobre eles.

### 1.6 Afirmação factualmente errada sobre política industrial ocidental

> "Quase nenhuma política industrial ocidental faz isso [compra direcionada]"

Falso, e verificável em cinco segundos. Buy American Act (1933) e Buy America (IIJA), EU Chips Act, aquisição do DoD e da DARPA, os *advance market commitments* da Operation Warp Speed. No Brasil, margem de preferência para produto nacional na Lei 14.133 e o histórico da Lei de Informática. Compra direcionada é um dos instrumentos ocidentais mais usados.

O que sobrevive, e é o ponto que você quer: no Ocidente ela raramente é **casada com disciplina de saída**. Compra-se o nacional, mas não se deixa quebrar quem não performa. Reescrever nessa direção.

### 1.7 A tensão que o artigo cria e não resolve: a campanha antinvolução é seleção

O texto diz que faltou "disciplina seletiva" na China. Depois descreve o Estado chinês, em julho de 2025, sob Xi, determinando saída ordenada de capacidade obsoleta e regulação da "competição desordenada de baixo preço".

Isso é disciplina seletiva. Imposta de cima, com dez anos de atraso, por decreto em vez de por mercado, mas é seleção. O artigo trata como sintoma de doença o que também é a correção da doença. Nomear essa tensão em vez de deixá-la implícita.

### 1.8 Marcadores de IA na estrutura (diagnóstico do humanizador)

- **Antídoto 8 violado de forma clássica.** A seção "O que este artigo não é" é literalmente três negações impessoais paralelas: "Não é defesa de protecionismo. / Não é elogio ao modelo chinês. / Não é argumento de que...". É o padrão que o GPTZero marca como *Impersonal Tone + Overly Formal + Contrast Phrasing* simultaneamente.
- **Antídoto 7 violado.** Contei 27 travessões em ~2.800 palavras. O limite do protocolo é 2 por 500 palavras, ou seja, ~11. Está a 2,5x.
- **Antídoto 5.** "As quatro condições" seguidas de "Três perguntas para levar" formam o sanduíche numerado clássico. Quatro condições limpas é uma tidiness que a evidência não sustenta (ver 1.2).
- **Baixa burstiness nas seções analíticas.** Os blocos de "Cinco explicações" e "O que o Estado chinês de fato fez" têm frases de comprimento quase uniforme, todas abrindo com negrito.
- **O que já está bom e deve ser preservado:** primeira pessoa, mudança de curso admitida no meio do texto, ancoragem em datas e nomes próprios, e a nota de verificação. Isso é fingerprint humano de verdade.

### 1.9 A nota de verificação vira pára-raios

Declarar incerteza no fim não autoriza abrir o texto com um número contestado. Ou o número sustenta o argumento, e aí precisa ser verificado; ou não sustenta, e aí não abre o texto. Hoje a nota funciona como licença retroativa.

---

## Parte 2 — Números

### 2.1 O erro de maior impacto: US$ 19 bilhões

> "A outra queimou dezenove bilhões de dólares sem entregar um chip."

O orçamento **anunciado** da HSMC era de ¥128 bi (~US$ 19-20 bi). O dinheiro público **efetivamente aportado** foi de ¥15,3 bi (~US$ 2,4 bi) até dezembro de 2019, pelo governo distrital.

A frase confunde promessa com desembolso, e é justamente a frase que carrega o peso retórico da seção. Corrigida, ela fica mais interessante: o escândalo não é o tamanho do buraco, é que **US$ 2,4 bilhões de dinheiro distrital foram suficientes para contratar o ex-CTO fundador da TSMC e comprar litografia da ASML** sem que ninguém checasse quem eram os sócios.

### 2.2 Três réguas diferentes empilhadas como se fossem uma

O artigo mistura três séries incompatíveis:

| Número no artigo | Fonte real | O que mede | Período |
|---|---|---|---|
| Nvidia 95% | Jensen Huang | Share de GPUs de IA na China antes dos controles | ~2022 |
| Nvidia ~8% | Bernstein, via The Economist | Share de **receita** do mercado chinês de chips de IA | 2026 (era ~39% em 2025) |
| 34% → 21% | TrendForce | Share de **chips para servidores de IA**, Nvidia + AMD | 2025 → 2026 |

Três metodologias, três recortes, três definições de "mercado". Encadeadas em dois parágrafos como se fossem uma trajetória.

Você é Master Black Belt. Isso tem nome: **falha de R&R**. Antes de comparar duas medidas, prova-se que o instrumento é o mesmo. Use uma régua por afirmação e diga qual é.

### 2.3 Erro de atribuição no share da Huawei

> "a Huawei saiu de praticamente zero para uma fatia estimada entre 50% e 60% desse mercado... Somando Huawei, Cambricon e os projetistas internos de ASIC, fornecedores domésticos devem controlar perto de 80%"

Os 56% da TrendForce são **Huawei + Cambricon juntas**. Somar a Cambricon de novo é dupla contagem.

Estrutura correta do mercado chinês de chips para servidores de IA em 2026, segundo a TrendForce (apresentado em Shenzhen, 25/06/2026):

- Huawei + Cambricon: **56%** (era 46% em 2025)
- ASICs internos de empresas chinesas de internet: **23%** (era 20%)
- Estrangeiros (Nvidia, AMD e outros): **21%** (era 34%)
- Total de silício projetado na China: **~79%**

A Bernstein, separadamente e com outro recorte, estima a Huawei sozinha em ~50%, com ~US$ 12,1 bi de vendas. Cite uma ou outra. Não some as duas.

### 2.4 "Mais de oitocentos mil chips despachados no ano"

Não encontrei fonte para esse número. Os dados públicos que existem:

- Meta de produção de **~750 mil unidades** do Ascend 950PR em 2026 (analistas citados pela Tom's Hardware, mai/2026)
- Plano da Huawei de **dobrar a produção em 2026, mirando ~1,6 milhão de *dies*** (set/2025)

*Die* não é chip embalado, e chip produzido não é chip despachado. Ou nomeie a fonte ou tire o número.

### 2.5 As séries de chips não saíram todas em 2019

> "No mesmo ano de 2019 saíram as séries Kirin, Balong, Kunpeng e Ascend."

Kirin existe desde 2009 (K3V1) e no formato moderno desde 2014. Balong desde 2010. Kunpeng 920 foi lançado em janeiro de 2019. Ascend 310 e 910 foram anunciados em outubro de 2018, com o 910 comercialmente disponível em agosto de 2019.

O fato verdadeiro é mais forte que o falso: **em 2019 a Huawei já tinha quatro famílias de chips em produção simultânea**, o que quase nenhuma empresa do mundo tem. Use esse.

### 2.6 Macaíba: valor, quantidade e uma armadilha de medição

O anúncio de 20 de agosto de 2026, feito por Lula no Parque Científico e Tecnológico Augusto Severo, em Macaíba:

| Artigo diz | Verificação |
|---|---|
| "dois supercomputadores" | **Um** supercomputador |
| "investimento acima de R$ 2 bilhões" | **R$ 1,06 bi** para a máquina (R$ 960 mi de equipamento + R$ 100 mi de infra e operação). O total >R$ 2 bi só aparece somando uma linha separada de ~R$ 1,276 bi para infraestrutura de nuvem e modelo de linguagem nacional, com a RNP, ao longo de 5 anos |
| "entre os dez mais potentes do mundo" | Alegação do governo, baseada em **7.200 petaflops em FP16** |
| "operação prevista para 2027" | Correto: fim de 2027, operado pelo LNCC |
| "PBIA R$ 23 bi entre 2024 e 2028" | Correto |

**E aqui está o presente que a verificação te deu.** O TOP500 ranqueia em **FP64**. O número brasileiro está em **FP16**. São precisões diferentes, e a diferença entre elas costuma ser de uma ordem de grandeza. A comparação com "os dez mais potentes do mundo" não é comparável ao ranking que ela invoca.

Isso é exatamente a sua tese, só que melhor: o entregável não é a máquina, é o número. E o número foi escolhido na régua que cita bem.

### 2.7 Big Fund: os números estão certos, uma afirmação não

Confirmados: Fase I (2014, US$ 21,8 bi), Fase II (2019, US$ 29,1 bi), Fase III (maio/2024, ¥344 bi = US$ 47,5 bi, com prazo de 15 anos, até 2039). Total ~US$ 98 bi. Investigação da Comissão Central de Inspeção Disciplinar em julho de 2022, com o ex-chefe Ding Wenwu entre os investigados. Confirmado.

**"distribuídos a mais de três mil entidades"**: não encontrei nenhuma fonte. A Fase I investiu em algo próximo de 70 projetos. Tirar ou substituir por fonte nomeada.

### 2.8 A declaração da NDRC é de 2020

O pedido de supervisão sobre "investimentos cegos" e a cobrança de responsabilização por projetos inacabados são de **outubro de 2020**. O artigo apresenta sem data, o que sugere admissão recente. Datar.

### 2.9 A quantificação da campanha antinvolução

"Metas de crescimento de produção reduzidas em dez indústrias-chave" mistura duas coisas: os **planos de estabilização de crescimento do MIIT para 10 indústrias-chave** (aço, metais não ferrosos, petroquímica, materiais de construção, máquinas, automóveis, equipamento elétrico, indústria leve, têxtil, eletrônicos), lançados a partir de janeiro de 2025 com metas para 2025-2026 abaixo das de 2024; e a **campanha antinvolução elevada pela Comissão Central de Assuntos Financeiros e Econômicos em julho de 2025**, presidida por Xi. São peças relacionadas, não a mesma peça. O caso concreto mais citado é a ordem para as siderúrgicas de Tangshan cortarem ~30% da produção.

---

## Parte 3 — Fontes

### 3.1 O que não é referência

> "Reportagem sobre zombie fabs e sobre a participação de mercado de Huawei e Nvidia em 2026, conforme listado na nota de verificação."

Isso é um espaço em branco com formatação de referência. Todos esses números têm fonte nomeável.

### 3.2 Referências reais que existem e deveriam estar lá

- HMAIDI, Antonia. *Huawei is Quietly Dominating China's Semiconductor Supply Chain*. MERICS, abril de 2024. (O artigo cita sem autor e sem data.)
- *Innovation under Pressure: China's Semiconductor Industry at a Crossroads*. American Affairs Journal, fev. 2026. **Existe, confirmado.**
- RUSI. *Huawei's 'Spare Tyre 2.0' and the Limits of US Sanctions*. **Existe.** Vale notar que o próprio RUSI atribui a fundação de 2004 à tentativa de aquisição pela Motorola em 2003, o que contradiz o uso que o artigo faz da fonte.
- TrendForce, apresentação em Shenzhen, 25/06/2026, via SCMP, para todos os números de share.
- Tom's Hardware, *Zombie fabs plague China's chipmaking ambitions*, para o intervalo de US$ 50-100 bi e a lista de projetos.
- Caixin, 12/07/2022, para a conclusão da recuperação judicial da Tsinghua Unigroup.
- Kevin Xu, *China's "Semiconductor Theranos": HSMC*, Interconnected, para a anatomia da fraude e os números de aporte distrital.
- SMITH, Noah. *What Studwell Got Wrong*. Noahpinion.

### 3.3 A crítica a Studwell está mal caracterizada

O artigo diz que Noah Smith é o crítico mais citado e sugere que a crítica atinge o núcleo da tese de condicionalidade. Não é o caso. Smith objeta a três coisas: a comparação Coreia versus Taiwan quando ajustada por PPC, o descarte da Malásia com base na Proton ignorando o sucesso em eletrônicos, e a generalização sobre o Sudeste Asiático diante de sinais recentes de convergência. Ele continua apoiando o arcabouço. A disciplina de exportação não é o alvo dele.

Isso é bom para você: significa que o núcleo que o artigo usa **sobrevive melhor** do que o texto admite. Mas a caracterização atual está errada.

### 3.4 Studwell e a Embraer

"A América Latina produziu essencialmente uma firma manufatureira globalmente competitiva. A Embraer." Isso é o enquadramento de Studwell e precisa ser atribuído como tal, não afirmado como fato. É contestável: Gerdau, WEG, Marcopolo, Braskem. Atribuir e deixar o leitor discordar de Studwell, não de você.

---

## Resumo executivo

**Sobrevive à verificação:**
- A carta de He Tingbo, a data e o conteúdo geral
- A fundação da HiSilicon em 2004
- Os números do Big Fund, incluindo o horizonte de 2039
- O intervalo de US$ 50-100 bi em fabs abandonadas
- A campanha antinvolução e o diagnóstico oficial chinês
- O núcleo de Studwell sobre condicionalidade
- A tese de capacidade absortiva de Cohen e Levinthal
- A observação central sobre a diferença entre subsidiar produção e garantir demanda

**Não sobrevive:**
- "Mesma proteção" entre Huawei e HSMC
- "US$ 19 bilhões queimados"
- Huawei sozinha com 50-60% de share
- A cadeia 95% → 8% como série única
- "Mais de oitocentos mil chips despachados"
- As quatro séries de chips lançadas em 2019
- Dois supercomputadores e mais de R$ 2 bi em Macaíba
- "Quase nenhuma política industrial ocidental faz compra direcionada"
- A Tsinghua Unigroup como falência
- A caracterização da crítica de Noah Smith

**O que a verificação entregou de graça, e que vale mais que o artigo original:**
1. A YMTC como anomalia viva dentro do próprio cemitério
2. A FDPR de setembro de 2020 como o choque que realmente construiu, contra a Entity List de 2019 que apenas revelou
3. FP16 versus FP64 em Macaíba, que é a sua tese sobre entregáveis compráveis em forma de erro de medição
4. A carta de 2019 como narrativa retroativa sobre 2004
