# Um número sem dono (artigo 23): análise, crítica e registro das melhorias

Data: 18 out. 2026. Original: `23_um-numero-sem-dono_substack.md`. Versão revisada: `23_um-numero-sem-dono_substack_v2.md`.

## 1. Síntese

A tese resiste, e sai mais forte. O artigo dizia que a régua contábil explica "só uma parte" da diferença de US$ 20 bilhões; a conta corrigida mostra que ela explica entre US$ 3 e 6 bilhões, e uma hipótese aritmética nova (40 × 1,7 = 68) oferece o primeiro mecanismo que fecha o número. Três problemas exigiram intervenção:

1. **Aritmética assimétrica.** O original comparava uma queda (6% a 10%, bruto para líquido) com um acréscimo (40%, líquido para bruto). Bases diferentes, comparação indevida.
2. **Contradição interna.** O texto prova que a régua não explica o salto e depois chama o gatilho de "diferença de método contábil" duas vezes.
3. **Causalidade e datas mais fortes do que a evidência.** "Provocado", "dois meses e meio", "escrito em julho" e "se preparam para abrir capital" não se sustentam como estavam.

A voz já estava limpa (zero travessões, zero negrito, zero molde "Não é X. É Y."). As intervenções de voz foram poucas e cirúrgicas.

## 2. Verificação de fatos

| # | No original | O que encontrei | Ação |
|---|---|---|---|
| 1 | O exemplo dos US$ 100 atribuído à própria Axios | Na matéria de 8/10, o exemplo é da professora de contabilidade Francine McKenna, ouvida pela Axios, e o verbo é "pode registrar" | Atribuição corrigida no corpo e na nota |
| 2 | "As duas formas seguem as regras contábeis americanas" | Correto. A Axios acrescenta o critério: depende de quem controla o cliente e entrega o produto. É o teste de principal versus agente da ASC 606 | Nome da norma e critério incluídos |
| 3 | Quatro versões da origem | A Axios de 8/10 tem uma quinta formulação, próxima da do FT: informação que a OpenAI compartilhou com investidores, "grossed up" | Incluída numa oração ao lado do FT, mantendo "quatro origens" |
| 4 | "Duas empresas que se preparam para abrir capital" | A Axios de 8/10 não fala em IPO; só diz que investidores de mercado aberto preferem receita efetiva. Nenhuma fonte listada sustenta o plano de IPO | Afirmação retirada do fecho |
| 5 | "Dois meses e meio de antecedência" | Reunião em 29/7, queda em 8/10: 71 dias, cerca de 2,3 meses. E a ata sai três semanas após a reunião (meados de agosto) | "Dez semanas antes"; "discutido em julho e público desde agosto" |
| 6 | "É o roteiro da semana, escrito em julho" | Discutido em julho, publicado em agosto | Corrigido |
| 7 | "Somando US$ 1,64 trilhão" ligado ao índice da Filadélfia | O US$ 1,64 trilhão é a soma da Reuters para ações de chips americanas, não a perda do SOX | Atribuição separada |
| 8 | Subtítulo: "Seis pregões depois" | De 8 a 15/10 inclusive são seis pregões; "depois" sugere seis pregões além do dia 8 | "Em seis pregões" |
| 9 | "Cinco meses depois" (memorando de abril → 29/9) | Domingo de abril mais provável: 12/4 (Implicator é de 13/4). Até 29/9: 5,6 meses | "Menos de seis meses depois" |
| 10 | "Nobel de economia" | Nome oficial: prêmio de ciências econômicas em memória de Alfred Nobel. Hall e Woodford confirmados como laureados em 12/10 | Nome completo uma vez no corpo; título da seção mantido |
| 11 | "Ninguém publica a conversão" | Afirmação de ausência, não verificável em sentido forte | "Não encontrei, de nenhum dos dois, a conversão" |
| 12 | "As duas maiores empresas do setor" | O "setor" do artigo é ambíguo: a queda foi de chips. OpenAI e Anthropic não são as maiores empresas desse setor | "Os dois maiores laboratórios de IA" |

Datas e intervalos conferidos por código: 3/9 → 29/9 = 26 dias (correto); 8/10 é quinta e 12/10 é segunda (quatro dias, correto); 8 a 15/10 = seis pregões (correto).

## 3. Aritmética da "conta que não fecha"

Cálculos em Python. Premissas: queda de 6% a 10% (fonte anônima, Axios, 3/9); US$ 50 bi líquido e US$ 70 bi bruto (Axios, 8/10).

| Grandeza | Valor |
|---|---|
| Anthropic: queda bruto → líquido | 6% a 10% (dado) |
| Anthropic: mesmo efeito como acréscimo líquido → bruto | 6,4% a 11,1% |
| Proporção da Anthropic aplicada aos US$ 50 bi da OpenAI | US$ 53,2 a 55,6 bi |
| Parte da diferença que a régua explicaria | US$ 3,2 a 5,6 bi, de 20 |
| OpenAI implícita: acréscimo líquido → bruto | 40,0% |
| OpenAI implícita: fatia da receita bruta repassada a parceiros | 28,6% |
| Razão entre a fatia implícita da OpenAI e a da Anthropic | 2,9 a 4,8 vezes |

O original comparava 6% a 10% com 40%. A comparação correta é 6,4% a 11,1% contra 40% (como acréscimo) ou 6% a 10% contra 28,6% (como queda). A conclusão do artigo se mantém e fica quantificada.

## 4. Lógica do argumento

1. **Contradição com a seção 2.** O texto demonstra que a régua cobre no máximo um quarto da diferença e, adiante, diz que o gatilho foi "uma diferença de método contábil" e que "uma diferença de método virou notícia de demanda". Trocado por "um número cuja régua ninguém conferiu" e "um número sem conferência", o que é coerente com o título.
2. **Causalidade calibrada.** "O dia que abriu a queda foi provocado por" afirma causa única, e a própria seção "Há uma tensão" admite que a régua pode ter sido faísca. Trocado por "teve como gatilho imediato", que é o que a sequência de datas sustenta.
3. **Moldura do Nobel enfraquecida pela premissa "a taxa é a taxa".** A premissa é falsa no ponto que interessa: o Fed também trabalha com duas réguas de inflação (CPI e PCE). O que diferencia o caso é que existe ponte publicada entre elas. O argumento fica mais preciso: o problema é a falta de ponte, e não a existência de duas réguas. Reescrito.
4. **Comunicado de 28 de janeiro.** Aparece em "Lido na fonte primária" e nas referências, mas nenhuma frase do corpo o usa. Mantido porque é registro de leitura seu; vale cortar ou dizer para que serviu.

## 5. Voz

| Métrica | Original | v2 |
|---|---|---|
| Palavras no corpo | 2.438 | 2.796 |
| Frases | 104 | 113 |
| Média de palavras por frase | 22,8 | 24,1 |
| Desvio-padrão | 12,9 | 12,2 |
| Frases curtas (até 6 palavras) | 9% | 7% |
| Frases acima de 40 palavras | 11 | 13 |
| Travessões | 0 | 0 |
| Negrito no corpo | 0 | 0 |
| Molde "Não é X. É Y." | 0 | 0 |
| "próprio/própria" | 12 | 6 |
| "mesma repórter" | 3 | 2 |

O aumento de palavras vem dos dois acréscimos (seção 6). A queda de frases curtas é efeito de uma junção e de duas meta-frases retiradas; todas as curtas restantes passam no teste da fragmentação legítima.

**Trocas de voz, antes e depois**

| Antes | Depois | Motivo |
|---|---|---|
| "Começo pelo limite do que posso afirmar." | Retirada; o parágrafo entra direto nas outras causas | Meta-frase |
| "Chego a três conclusões." | Retirada; as três conclusões entram sem anúncio | Arquitetura anunciada (Antídoto 5) |
| "Vou dizer uma coisa mais estreita" | "O que tenho a dizer é mais estreito" | Evita o par espelhado "Não vou dizer… Vou dizer…" |
| "A parte que me fez escrever este texto é outra." | "O que me fez escrever este texto foi outra coisa." | Mais oral, menos anúncio |
| "Na edição de 8 de outubro, a OpenAI 'decepcionou'. Na de 9…" | Unidas por ponto e vírgula | A segunda frase completa a comparação (marca 3 da fragmentação) |
| "segundo a CNBC e o The Verge, que leram o documento, conforme relatou o Implicator" | "um memorando… que a CNBC e o The Verge leram, segundo o Implicator" | Três atribuições encadeadas viraram duas |
| "A própria Axios tinha avisado." | "A Axios tinha avisado." | Excesso de "própria" (12 ocorrências) |
| "Para quem decide… Para quem lê… Para quem dirige…" | Três aberturas diferentes | Paralelismo de template |
| Pergunta final com 49 palavras | Uma frase afirmativa e uma pergunta | A pergunta perde força sob três subordinadas |

Mantidas de propósito, por carregarem proposição própria: "Nenhum cliente deixou de pagar. A explicação que circulou foi contábil." / "Sozinha, a régua explica um dia ruim. A semana precisou de mais." / "O resto continua sem autor." / "Os juros pesaram a semana inteira. Por pesarem o tempo todo, não explicam…".

## 6. Acréscimos ao conteúdo (podem ser cortados)

São as duas únicas intervenções que acrescentam argumento. Ambas estão marcadas no texto como hipótese ou moldura.

**6.1 A hipótese 40 × 1,7.** Os US$ 40 bi de agosto (que, segundo o The Information, ainda incluíam receita da Microsoft via Azure) multiplicados pelo crescimento de 70% anunciado por Friar dão US$ 68 bi, exatamente o número da CNBC. E 50 ÷ 1,7 ≈ US$ 29,4 bi no fim de junho. Se for essa a conta do investidor anônimo, o erro foi de base, não de régua: crescimento correto aplicado a uma base velha. Em metrologia é um erro de offset propagado por multiplicação. A hipótese depende da data de referência dos US$ 40 bi, que não consegui confirmar, e o texto diz isso.

**6.2 Ponte e rastreabilidade.** Dois parágrafos novos na seção do Nobel:
- CPI (BLS) e PCE (BEA) divergem por fórmula, peso e cobertura, e o governo americano publica a reconciliação. Este dado vem de conhecimento geral, não de leitura feita nesta revisão: confira a tabela de reconciliação no site do BEA antes de publicar.
- Rastreabilidade metrológica (VIM): um resultado só é rastreável se puder ser ligado a uma referência por cadeia ininterrupta e documentada de calibrações. Dá ao título "Um número sem dono" uma tradução técnica exata.

## 7. Hipóteses que ficaram fora do texto

- **Telefone sem fio com amplificação.** Em epidemiologia de rumores, a repetição sem fonte nova não acrescenta evidência, mas acrescenta confiança. O número de US$ 70 bi é um caso de reprodutibilidade aparente: n citações, n_efetivo = 1.
- **Contabilidade como dramaturgia.** Principal ou agente é, na ASC 606, a pergunta sobre quem está em cena e quem está na coxia. Anthropic se declara protagonista; OpenAI se declara coadjuvante na venda pela Microsoft. A régua é um papel escolhido, e o mercado leu o elenco como bilheteria.
- **Bioequivalência.** Na farmacêutica, dois medicamentos só são intercambiáveis com estudo de bioequivalência contra o referência. Duas receitas de IA só são comparáveis com o "estudo" que nenhuma empresa fez.

## 8. Pendências antes de publicar

1. Confirmar a data de referência dos US$ 40 bi de agosto (sustenta a hipótese 6.1).
2. Conferir no BEA a reconciliação CPI–PCE (sustenta 6.2).
3. Verificar o título da Reuters (US$ 2 tri) contra o corpo (US$ 1,64 tri) e explicar a diferença na nota, se houver.
4. Conferir no comunicado da Oracle se os US$ 20 bi em ações foram venda, emissão ou programa de oferta. O verbo "vendeu" pode estar impreciso.
5. Guerra EUA–Irã "no oitavo mês" e Brent acima de US$ 104 vêm só da CNBC; vale uma segunda fonte.
6. Decidir sobre o comunicado do Fed de 28 de janeiro (citado, não usado).

## Fontes consultadas nesta revisão

- [Axios, 8 out. 2026](https://axios.com/2026/10/08/openai-50-billion-arr-anthropic-revenue-accounting)
- [NBER: Robert Hall and Michael Woodford Awarded 2026 Nobel Prize](https://www.nber.org/news/robert-hall-and-michael-woodford-awarded-2026-nobel-prize)
- [Al Jazeera, 12 out. 2026](https://www.aljazeera.com/news/2026/10/12/nobel-economics-prize-awarded-to-robert-hall-and-michael-⁠woodford)
- [Investinglive: How a (negative!) $20 billion gap opened up](https://investinglive.com/stocks/how-a-negative-20-billion-gap-opened-up-in-openai-s-revenue-figures/)
