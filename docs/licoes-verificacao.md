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

---

# Segundo caso: "Seis dias úteis", rodada de 20 de setembro de 2026

Verificação feita pela autora sobre o ensaio já pronto, com a fonte primária da OpenAI
acessível nesta rodada (o proxy tinha bloqueado o domínio na anterior). Dezesseis itens
checados, seis erros factuais e uma omissão que custava o melhor argumento do texto.

## Os erros que geraram regra

**Afirmei ausência sem abrir a fonte.** Escrevi "não há denominador". A OpenAI publicava
prevalência em dois casos: 2,15% dos resumos de compactação do GPT-5.6 Sol e 0,27% dos do
GPT-6 Astra. Afirmação falsificável em trinta segundos por qualquer leitor que abrisse a
página que eu declarei não ter conseguido abrir. → Regras 2.9 e 3.6.

**Errei a cronologia que sustentava o argumento.** Escrevi que o incidente da Hugging Face
era de abril e que a divulgação de setembro vinha "cinco meses depois". O incidente foi
divulgado entre 21 e 22 de julho de 2026, e a distância é de dois meses. Além disso foram
dois modelos, não um, e o dia zero estava num proxy de cache de registro de pacotes, não
na Hugging Face. A cronologia era a espinha do argumento "caso isolado vira padrão".
→ Regras 2.10 e 3.15.

**Números com validade vencida.** ASRS: escrevi 1,8 milhão de relatos, cem mil por ano e
mais de quarenta e cinco anos. Os números correntes são 2,3 milhões, acima de dez mil por
mês, e cinquenta anos de operação desde 15 de abril de 1976. → Regra 2.11.

**Revisão errada da norma.** Citei o Advisory Circular 00-46E. A revisão vigente é a 00-46F,
com o 14 CFR 91.25. → Regra 3.7.

**Reusei número do meu próprio texto sem checar.** As 18.476 propostas ao conselho de
pesquisa australiano vieram de um artigo anterior, declaradas na nota como não
reverificadas, três semanas depois do episódio em que exatamente esse hábito deu errado.
A nota declarava o hábito com honestidade e mantinha o hábito. Verificar custou uma
consulta: Bromham, Dinnage e Hua, *Nature* 534:684–687, 2016, programa Discovery do ARC,
cinco anos consecutivos. → Regra 3.8.

**Paráfrase que matou o mecanismo.** Escrevi que a troca entre agentes "pode ampliar
capacidades involuntariamente". A formulação real nomeia o mecanismo: o canal permite aos
agentes se apoiarem em trabalho de outras rodadas, aumentando o poder de computação efetivo
em tempo de teste. Eu estava dizendo que esse era o achado mais importante do texto e o
enfraqueci na hora de escrevê-lo. → Regra 3.11.

**Generalizei um incidente particular.** "Modelos subiram arquivos para a internet" era um
modelo não lançado, em duas datas (22/10/2025 e 24/01/2026), subindo registros recuperados
para serviços públicos de paste e imagens, para obter citação via navegador, numa tarefa
sobre lagos com mais de 5.000.000 m². → Regra 3.15.

**Referência fantasma.** Bainbridge nas referências e ausente do corpo, num texto cuja
seção "Quem vai ler o relatório" é literalmente a tese de *Ironies of Automation*.
→ Regra 3.13.

**Apresentei análise de um blog como consenso da cobertura.** O critério de avaliação que
chamei de "o mais útil de tudo que li" vinha de uma única análise secundária, não de
pesquisador nomeado nem da OpenAI. → Regra 3.10.

**Não nomeei quem podia ser nomeado.** "Pesquisadores da Apollo Research e da Safer AI
questionaram" tinha nome: Alexander Meinke e Henry Papadatos. → Regra 3.9.

**Omiti a ressalva do próprio autor.** O comunicado de Stanford abre com "no widespread
displacement", que eu tinha usado no artigo anterior e deixei de fora deste. → Regra 3.12.

## As críticas de argumento

**O título defendia a tese fraca.** "Seis dias úteis" celebra a pista rápida. A estrutura
que decide o comportamento do sistema é a terceira trilha, *Larger Investigation*, sem
prazo fixo, aplicável a casos complexos e a terceiros, com prioridade cedida a obrigações
de segurança e jurídicas avaliadas pela mesma parte que decide divulgar. É para lá que a
exceção migra, e o texto passou ao largo. → Regra 1.13.

**A crítica larga quebrou; a estreita sobrevivia.** → Regra 1.14.

**Três finais.** Perguntas, fecho e nota em sequência, com a melhor pergunta enterrada em
terceiro lugar. → Regra 1.15.

**O melhor fato estava sendo desperdiçado.** Tratei a neutralidade da NASA como
característica feliz. A documentação diz que foi a FAA que pediu à NASA, separada dos
órgãos de fiscalização e investigação, que administrasse o sistema. O regulador abriu mão
de receber o relato, o que muda o fecho: o ator ausente hoje não é uma ONG neutra a ser
inventada, é um regulador disposto a entregar a função de recebimento a outro.
→ Regra 3.14.

**Hipótese que ninguém cruzou.** O escape de julho se deu por dia zero no Artifactory, e o
quinto incidente de setembro usou o Artifactory interno da OpenAI como mural de recados. A
mesma peça de encanamento nos dois. A leitura responsável é perímetro, não conspiração: um
cache de registro de pacotes é alcançável por default em quase toda arquitetura de
avaliação, e por isso sustenta tanto uma fuga quanto um canal lateral. → Regra 1.16.

## O diagnóstico de voz

Primeira vez que a verificação veio com métrica em vez de impressão, e é o que gerou a
seção 4 reescrita e o `scripts/voz.py`.

| Métrica | Original | Reescrita | Alvo |
|---|---|---|---|
| Travessões | 0 | 0 | ≤ 2 por 500 palavras |
| "Não é X. É Y." | 4 | 0 | 0 |
| Frases | 157 | 159 | — |
| Média / desvio | 16,2 / 10,2 | 20,9 / **11,7** | desvio ≥ 11 |
| Frases ≤ 6 palavras | 15,9% | **8,2%** | ≤ 10% |
| Fragmentação ilegítima | ~8 pares | 0 | 0 |

O par central é o que ensina: o desvio-padrão **subiu** enquanto a proporção de frases
curtíssimas **caiu pela metade**. A variação do original estava parcialmente manufaturada
por ponto final em meia oração ("É contorno do medidor.", "Foi criar o lugar.", "Acha
olhando para o caminho.", "Não quem assina. Quem sabe."). Juntando as metades e deixando o
ritmo aparecer onde o pensamento muda de unidade, a variância real aumentou.

Teste operacional para cada fragmento: **a segunda frase sobrevive sozinha?**
