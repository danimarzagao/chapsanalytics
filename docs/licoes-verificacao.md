# Lições de verificação — caso de origem

Registro do caso que gerou as regras em `CLAUDE.md`. Serve para que o agente entenda a
origem de cada regra e reconheça o padrão quando ele reaparecer com outra roupa.

**Caso:** ensaio "O pneu sobressalente", série VibeCoding em Contexto, agosto de 2026.
Tema: controles de exportação americanos, ascensão da Huawei em chips de IA, e o
contraste com o anúncio de supercomputação em Macaíba.

**Resultado:** o texto foi reescrito duas vezes. A verificação derrubou a tese da
primeira versão e a evidência central da segunda. A versão final é melhor que as duas,
e é melhor **porque** perdeu material.

---

## O que não sobreviveu, e o que cada erro ensina

### O par que não era par

Escrito: "A Huawei e a HSMC operaram sob exatamente a mesma proteção. Mesmo Estado,
mesma política, mesmo bloqueio externo, mesmo acesso a subsídio."

As quatro afirmações eram falsas. A Huawei estava na Entity List desde maio de 2019 e
perdeu acesso à TSMC em setembro de 2020. A HSMC nunca foi sancionada, e por isso mesmo
comprou litografia da ASML. A Huawei recebeu subsídio central; a HSMC recebeu dinheiro
do distrito de Dongxihu e nunca viu recurso do Big Fund. A Huawei tinha duas décadas de
P&D; a HSMC tinha três sócios sem experiência no setor, um deles vindo de restaurantes.

Além de falso, o par era metodologicamente inválido: seleção pela variável dependente.
E o caso escolhido era uma fraude, o que faz dele o pior contraste possível, porque
qualquer variável explica a diferença.

→ Regras 1.1 e 1.2.

### O número que virou retórica

Escrito: "queimou dezenove bilhões de dólares sem entregar um chip."

Os US$ 19 bilhões eram orçamento anunciado. O aporte público efetivo foi de cerca de
US$ 2,4 bilhões. A frase que carregava o peso da seção confundia promessa com
desembolso.

A versão corrigida é pior para o Estado chinês e melhor para o texto: US$ 2,4 bilhões
de dinheiro distrital bastaram para contratar o ex-CTO fundador da TSMC e comprar
equipamento da ASML, sem que ninguém checasse quem eram os sócios.

→ Regra 2.2, e o princípio geral de que o fato verdadeiro costuma ser mais forte que o
falso.

### Três réguas empilhadas como uma

Escrito: Nvidia de 95% para 8%, e Nvidia mais AMD de 34% para 21%, encadeados como
trajetória.

Eram três séries incompatíveis: 95% era share de GPUs antes dos controles, dito pelo
CEO da Nvidia; 8% era share de receita estimado pela Bernstein; 34% para 21% era share
de chips para servidores, da TrendForce. Três metodologias, três recortes, três
definições de mercado.

→ Regra 2.1. O nome disso em processo é análise do sistema de medição, e a autora é
Master Black Belt. A regra existe justamente porque conhecimento do método não impede
o erro quando o dado vem de fora do domínio habitual.

### Dupla contagem

Escrito: Huawei sozinha com 50% a 60%, e depois "somando Huawei, Cambricon e ASICs
internos, perto de 80%".

Os 56% da TrendForce já eram Huawei mais Cambricon. Somar a Cambricon de novo é contá-la
duas vezes.

→ Regra 2.3.

### A anomalia enterrada

Escrito: Tsinghua Unigroup listada no cemitério, "a empresa foi à falência".

Não faliu: passou por recuperação judicial concluída em julho de 2022, com troca de
controle. E controlava a YMTC, única fabricante chinesa de 3D NAND, que sobreviveu à
reestruturação e à lista negra e segue expandindo.

A YMTC é o caso mais interessante da pesquisa inteira, porque **não** tinha o estoque
prévio de quinze anos que a tese exigia. Tinha dinheiro estatal, demanda cativa e
mercado protegido, exatamente a combinação que o texto dizia não bastar. Ela estava
enterrada em uma linha.

→ Regra 1.3. Anomalia enterrada é sempre sinal de que o modelo está sendo protegido do
dado.

### A espingarda mostrada no terceiro ato

O pivô inteiro do texto se apoiava na intenção fundadora da HiSilicon em 2004. A fonte
dessa intenção é uma carta de 2019, escrita pela parte interessada no dia seguinte à
sanção, viral em horas. O RUSI, citado como apoio no próprio artigo, atribui a fundação
de 2004 à tentativa frustrada de aquisição pela Motorola em 2003.

A fundação é fato. A intenção não é.

→ Regras 1.4 e 3.2. Note o agravante: a fonte citada como apoio continha a versão
concorrente.

### O falso dilema

O texto opunha "a sanção construiu" contra "a sanção encontrou estoque". As duas eram
verdadeiras em camadas diferentes. O pneu sobressalente de 2004 cobria projeto de chip;
a HiSilicon era fabless e dependia da TSMC. A regra que realmente machucou foi a Foreign
Direct Product Rule de setembro de 2020. Para essa não havia pneu, e o 7 nanômetros da
SMIC foi construído depois do choque.

A frase de fechamento, "restrição não constrói nada, apenas revela", era elegante e forte
demais para a evidência.

→ Regra 1.5. Frase bonita demais é sinal de checagem pendente.

### O defeater no lugar errado

A causalidade parcialmente reversa aparecia como quinta de cinco explicações
alternativas, perto do fim. Não era uma explicação entre outras: era um defeater do
número de abertura. Parte da queda da Nvidia é proibição americana de vender somada a
restrição chinesa de importar.

→ Regra 1.6.

### A afirmação que caía em cinco segundos

Escrito: "quase nenhuma política industrial ocidental faz compra direcionada."

Buy American existe desde 1933. EU Chips Act, DoD, DARPA, Operation Warp Speed, Lei
14.133 e Lei de Informática no Brasil. Compra direcionada é dos instrumentos ocidentais
mais comuns.

O que sobrevive, e era o ponto de verdade: o Ocidente raramente casa compra direcionada
com disciplina de saída.

→ Regra 1.9.

### A tensão não nomeada

O texto dizia que faltou disciplina seletiva na China e, páginas depois, descrevia a
campanha antinvolução de julho de 2025 determinando saída ordenada de capacidade
obsoleta. Isso é disciplina seletiva, imposta por decreto e com dez anos de atraso, mas
é seleção. O texto tratava como doença o que também era o remédio.

→ Regra 1.8.

### A crítica mal caracterizada

O texto dizia que Noah Smith era o crítico mais citado de Studwell e sugeria que a
crítica atingia o núcleo de condicionalidade. Smith objeta à comparação Coreia contra
Taiwan ajustada por paridade de poder de compra, ao descarte da Malásia com base na
Proton, e à generalização sobre o Sudeste Asiático. Ele não ataca a disciplina de
exportação e continua apoiando o arcabouço.

O núcleo usado sobrevivia melhor do que o texto admitia.

→ Regra 3.3.

### O presente que a verificação deu

Macaíba: um supercomputador, não dois. R$ 1,06 bilhão para a máquina, não mais de
R$ 2 bilhões. E os 7.200 petaflops são FP16, enquanto o TOP500 ranqueia em FP64. A
comparação com "os dez mais potentes do mundo" não é comparável ao ranking que ela
invoca.

Esse erro de medição é, ele mesmo, a tese do artigo sobre entregáveis compráveis. O que
se compra é a parte que se anuncia bem, e o que se anuncia bem escolhe a régua.

→ Regra 2.6, e o princípio de que erro de medição frequentemente é a melhor história
disponível.

---

## O que sobreviveu

Vale registrar, porque a lição não é "desconfie de tudo".

Sobreviveram: a carta de He Tingbo, data e conteúdo geral; a fundação da HiSilicon em
2004; todos os números do Big Fund, incluindo o horizonte de 2039; o intervalo de US$ 50
a 100 bilhões em fabs abandonadas, como ordem de grandeza; a campanha antinvolução e o
diagnóstico oficial chinês; o núcleo de Studwell sobre condicionalidade; Cohen e
Levinthal; e a distinção entre subsidiar produção e garantir demanda, que é o único item
que atravessou as três versões sem ressalva.

---

## A lição de processo

A nota de verificação da versão final foi escrita **antes** do artigo. Foi por isso que
o artigo mudou duas vezes antes de existir.

Nota escrita antes é projeto. Nota escrita depois é desculpa, e funciona como licença
retroativa para abrir o texto com número que não se checou.

→ Seção 5 do `CLAUDE.md`.
