# O decreto sem crédito: revisão de voz, fatos e argumento

*Revisão de 8 nov. 2026 sobre o rascunho enviado. Versão revisada: `26_o-decreto-sem-credito_vozDani.md`.*

## 1. Síntese

O rascunho já cumpria as regras duras de voz. O problema principal estava nos fatos e no argumento: uma premissa factual estava errada (a auditoria tinha prazo público), e a "segunda leitura" era mais forte do que o texto admitia. Uma conta feita só com as proporções publicadas mostra que os 36% de Abbott saem quase inteiros da composição partidária. A tese do título continua de pé, e agora tem mais base.

## 2. Diagnóstico quantitativo

| Métrica | Original | Revisado |
|---|---|---|
| Travessões | 0 | 0 |
| Negrito no corpo | 0 | 0 |
| Palavras (corpo) | 1.851 | ~2.170 |
| Frases | 94 | 103 |
| Média palavras/frase | 19,7 | 21,1 |
| Desvio-padrão | 10,1 | 9,9 |
| Frases ≤ 8 palavras | 13% | 11% |
| Frases com 3+ "que" | 1 | 0 |

## 3. Correções de fato (mudam o argumento)

| # | Original | Problema | Correção | Fonte |
|---|---|---|---|---|
| F1 | "ninguém sabe quando ela acaba" | Em 20 ago. o ERCOT anunciou à PUCT a entrega do relatório em 10 dez., cinco semanas depois da eleição | Data incluída; ela passa a sustentar a leitura de credibilidade | TPR / Houston Public Media; Utility Dive; DCD |
| F2 | "não tinha como verificar se a auditoria terminaria antes ou depois de 2027" | Mesma premissa | Reescrito: 10 dez. é data de entrega de relatório, sem decisão marcada para depois | mgrid.org; Gibson Dunn |
| F3 | "terceira medida … em dois meses" | Correto em 3 ago., mas incompleto | Acrescentada a diretiva de 21 set. (pausa das licenças ambientais da TCEQ) | DLA Piper, 25 set. |
| F4 | Berkeley como "a régua que mais me convenceu", sem contraponto | Há evidência contrária: George Mason (2025) não acha efeito negativo no norte da Virgínia | Contraponto incluído, mais a heterogeneidade (efeito maior no primeiro data center da comunidade), segundo a Newsweek | Bisnow; The Close; Newsweek |

## 4. Mudança de argumento: a leitura partidária

**Antes.** "Os dados admitem duas leituras, e não consigo escolher entre elas", e a segunda leitura dependia de uma tabela que não está publicada.

**Agora.** A conta foi feita em Python e só usa a boca de urna (R = 48%, Abbott 90% entre R, 75% contrários, Abbott 36% entre contrários):
- quase metade dos republicanos (≥ 47,9%) está necessariamente entre os contrários;
- nos cenários que fecham, Abbott tem de 82% a 99% dos republicanos contrários, perto da média partidária de 90%.

Conclusão: os 36% são quase todos composição partidária. O decreto não rendeu voto, e o número também não mostra que o eleitor tenha punido Abbott pelo passado. Isso bate com a comparação com a Geórgia, que já estava no texto.

**Reforço pré-eleição.** A pesquisa UT/Texas Politics Project de agosto mostrava 75% dos democratas contra um data center na própria comunidade, contra 43% dos republicanos (45% dos republicanos eram a favor).

**Âncora teórica (polímata).** Achen & Bartels, *Democracy for Realists* (2016): a identidade partidária forma a posição sobre os temas, e o caminho inverso é raro. A referência entra com marcação de extensão ("Se a lógica deles vale aqui…"), como pede a disciplina de atribuição.

**Efeito na seção final.** A frase "Uma posição adotada tarde, por quem construiu o problema, rende pouco" afirmava uma causa que os dados não permitem afirmar. Ela virou uma lição mais modesta: "adotar a posição do eleitor não comprou o voto dele", e as duas causas possíveis ficam declaradas como não separáveis.

## 5. Edições de voz (cirúrgicas)

| Antes | Depois | Regra |
|---|---|---|
| "O levantamento é um só. … uma medição só, citada sete vezes." | "Por trás de todos os números há um levantamento só… O que aparece em sete veículos é uma medição citada sete vezes." | Redundância ("um só" duas vezes) |
| "…para 48%. Na Geórgia, 27% contra 50%." | "…para 48%; na Geórgia, para 27% e 50%." | Fragmentação ilegítima (elipse) |
| "O achado que importa aqui está no meio do artigo." | Removida | Metafrase de sinalização |
| "…deixa de ser se o eleitor puniu… Passa a ser outra, mais precisa:" | "…muda de objeto: em vez de saber se…, quero saber…" | Molde "deixa de ser X. Passa a ser Y" + sujeito elíptico |
| "calculou que … e acrescentou que acredita que…" | "…e apostou que elas durariam pouco" | Frase-contêiner (3 "que") |
| "O comunicado não marca prazo. O ERCOT adiou…" | Unidas por vírgula + "e" | Par curto sem virada real |
| "a política certa" | "a política que pedia" | Juízo avaliativo sem base no texto |

O que ficou como estava, porque passa no teste da fragmentação legítima: "A frase circulou." "Ohio tem 21." "Ele foi dois pontos pior." "A primeira é de credibilidade."

## 6. O que não verifiquei e fica sob sua responsabilidade

- A frase de Aidan Yao e as quedas de Core Scientific (−11,6%) e Iren (−12,5%): não achei a matéria da Reuters. A cobertura secundária cita outras quedas no mesmo dia (CoreWeave −9,5%, Vistra −15,4%).
- Os números da boca de urna NBC (62/36, 61/38, 48%, 90%) e Rick Jackson como candidato na Geórgia: não reabri as tabelas.
- Ballotpedia, 50/47/46: a CNBC noticiou "40 de 41" para as medidas da cédula de 3 nov. (21 delas em Ohio). Isso é compatível com a contagem do ano inteiro, mas convém reconferir a página.

## 7. Sugestão opcional (não aplicada)

No dia seguinte à eleição, segundo a Reuters via cobertura secundária, Amazon e Microsoft subiram cerca de 6% enquanto as operadoras de data center caíram. A leitura possível é que o mercado premiou quem compra capacidade e puniu quem a constrói. Isso daria um gancho para a seção final sobre quem paga a conta, mas exige ler a Reuters no original antes de entrar no texto.
