# As quatro evidências críticas: o que as fontes dizem

*Pesquisa de 15/11/2026 sobre as evidências E1 a E4 de `crescimento-pinha-patrone-livro.md`. Para cada uma: o que foi lido, o que a fonte diz, o que isso faz com o argumento e o que ainda falta. As razões entre percentuais foram refeitas em Python.*

---

## Síntese

1. **Pinha tem razão no diagnóstico e erra a dicotomia (E1).** No estudo da PwC, as empresas que lideram em IA apontam a tecnologia para crescimento e reinvenção, e a convergência entre setores é o fator mais forte. Só que 48% dessas líderes também esperam cortar pelo menos 5% do quadro. Elas crescem *e* cortam, e o estudo não separa a receita da eficiência.
2. **A régua aparece dentro do próprio estudo da PwC.** As líderes têm 80% mais chance de acompanhar de forma sistemática o impacto de negócio da IA. Quem mede melhor é quem captura mais valor. A PwC não testa causalidade, mas é o dado mais próximo da tese do "Contar cabeças" que encontrei.
3. **A elasticidade da demanda está confirmada como mecanismo (E2).** Bessen mostra, com dois séculos de dados de têxteis, aço e automóveis nos Estados Unidos, que a elasticidade da demanda decide o sinal do efeito da automação sobre o emprego. A velocidade da produtividade só decide o ritmo. Ele mesmo trata a aplicação a hoje como questão empírica, setor a setor.
4. **A evidência por empresa enfraquece tanto o "teto" de Pinha quanto a explicação cultural do livro (E3).** O Brasil tem dispersão grande de qualidade de gestão entre empresas, com uma cauda longa de empresas mal geridas. Em empresas familiares, a sucessão para um CEO da família reduz a adoção de práticas estruturadas em cerca de 0,8 a 0,96 desvio-padrão. A habilidade do CEO explica só parte dessa diferença. O mecanismo principal proposto é o compromisso implícito com os empregados, que torna caro disciplinar e demitir. É quase o inverso da pergunta "quantas pessoas eliminar".
5. **No Brasil, a indústria declara eficiência quase sempre e mercado novo com menos frequência (E4).** Na PINTEC Semestral 2024, 90,3% das indústrias com 100 ou mais pessoas citam aumento de eficiência como benefício das tecnologias digitais avançadas, 74,7% citam maior capacidade de desenvolver produtos novos e 43,8% citam entrada em novos mercados. A pergunta vale para o conjunto das tecnologias, não só para a IA. A pergunta de Pinha que tem menos resposta empírica no Brasil é a dos mercados nunca alcançados.
6. **Há uma correção a fazer no livro.** O capítulo 1, §5, diz que "a maioria das organizações que investe em IA não está gerando retorno mensurável". O estudo da PwC mede o desempenho relativo à mediana do setor, então não permite afirmar nada sobre retorno absoluto. Ver seção 5.

---

## E1. O que distingue os 20% que capturam 74% (PwC, 2026)

**Fonte lida:** PwC, *Want ROI from AI? Go for growth*, relatório completo em PDF (pwc.com/gx/en/so-you-can/2026/content/roi-from-ai.pdf). Também consultados os releases de PwC Global, Austrália e Tailândia.

**Metodologia (p. 28).**
- 1.217 executivos de nível diretor ou acima, de 25 setores e seis regiões.
- 91% de empresas de capital aberto, 76% com receita de US$ 1 bilhão ou mais.
- Campo em outubro e novembro de 2025.
- O "desempenho atribuído à IA" combina ganhos de receita e de eficiência ou custo atribuídos à IA, ajustados pela mediana do setor.
- O índice de "AI fitness" soma nove fatores avaliados em 60 práticas. Seis são fundações: estratégia, investimento, dados e tecnologia, força de trabalho, governança e risco, inovação. Três medem o uso: amplitude e profundidade, sofisticação, e captura de valor pela convergência entre setores.

**O que as líderes fazem.**

| Prática | Líderes contra demais | Página |
|---|---|---|
| Relatam que a IA melhorou a capacidade de reinventar o modelo de negócio | 2,6x | p. 11 |
| Usam IA para identificar *value pools* emergentes | 1,8x | p. 11 |
| Colaboram com empresas de fora do setor | 3x (50% contra 17%) | p. 12 |
| Acompanham sistematicamente o impacto de negócio da IA | +80% | p. 13 |
| Investem em IA como percentual da receita | 2,5x | p. 15 |
| Têm aprendizado contínuo e por função | 1,7x (62% contra 36%) | p. 18 |
| Confiam nos insights da IA e agem sobre eles | 2,1x (60% contra 29%) | p. 18 |
| Têm incentivos de desempenho que estimulam o uso de IA | 1,8x (59% contra 32%) | p. 18 |

O relatório chama a convergência entre setores de "the single strongest AI fitness factor influencing AI-driven financial performance" (p. 11).

**Emprego (p. 26).** 48% das líderes esperam reduzir o quadro em pelo menos 5% por causa da IA, e 49% esperam pouca mudança ou aumento. O próprio relatório diz que "the immediate shift is not the removal of people".

**Limites que o relatório tem ou admite.**
- É um corte transversal com escalas de concordância respondidas por executivos. O índice está "positively and significantly linked" ao desempenho, mas isso é correlação, e o texto usa linguagem de efeito.
- O 74%/20% é afirmado sem que o cálculo seja explicado.
- O 7,2x é a razão entre 15,7 e 2,2 pontos percentuais acima da mediana. A conta dá 7,1 com os valores publicados. Uma razão entre diferenças em relação à mediana, com um denominador perto de zero, é instável.
- Receita e eficiência não aparecem separadas nos multiplicadores, de modo que não dá para dizer quanto do desempenho das líderes vem de crescimento.
- A amostra é de empresas grandes e listadas. Os casos são de clientes da PwC, que vende serviços de IA.

**O que isso faz com o argumento.**
- *A favor de Pinha:* as líderes declaram usar IA para reinventar o modelo e entrar em novos espaços de valor.
- *Contra a dicotomia de Pinha:* quase metade das líderes também espera cortar. Crescimento e corte aparecem juntos nas mesmas empresas. A pergunta "quantas pessoas eliminar" convive com as perguntas de crescimento, e o problema é quando ela é a única.
- *A favor da tese da régua:* o +80% em acompanhamento sistemático do impacto é a evidência mais próxima de que medir bem anda junto com capturar valor.
- *A favor do livro:* o aprendizado contínuo (1,7x) conversa com os capítulos 5 e 6, sempre como correlação.

**O que falta.** Ver se há anexo com os dados de receita separados dos de eficiência. Ler o gráfico da p. 9, sobre novos produtos e velocidade de lançamento, direto no PDF, porque a extração em texto não permitiu associar cada multiplicador à linha certa.

---

## E2. Elasticidade da demanda e emprego (Bessen, 2019)

**Fonte lida:** resumo do artigo em IPUMS e RePEc; coluna do autor no VoxEU/CEPR, republicada pelo Fórum Econômico Mundial. O artigo completo está em *Economic Policy*, vol. 34, nº 100, pp. 589–626 (2019), com versão de trabalho aberta na BU Law (SSRN 2935003).

**O que a fonte diz.**
- Com dados de dois séculos das indústrias têxtil, siderúrgica e automobilística nos Estados Unidos, Bessen mostra que a automação primeiro fez o emprego crescer porque a demanda era muito elástica. Depois a demanda saturou, e o emprego caiu.
- A produtividade cresceu a ritmo parecido nas duas fases. O que mudou foi a resposta da demanda: muito elástica no início, muito inelástica depois.
- A formulação central da coluna: a taxa de crescimento da produtividade define o ritmo da mudança, e a elasticidade da demanda define o sinal.
- O exemplo do tecido: no começo do século XIX o adulto médio tinha uma muda de roupa. A queda de preço liberou uma demanda reprimida grande. Em meados do século XX os armários estavam cheios, e novas quedas de preço já não aumentavam muito a demanda.
- Implicação proposta por ele: setores com muita demanda não atendida tendem a responder à automação com mais emprego. A principal consequência pode ser uma grande realocação de empregos, e não perda em massa.
- Ressalva do próprio autor: a elasticidade de resposta é uma questão empírica, e os estudos recentes sobre robôs e TI divergem. Alguns encontram efeito positivo sobre o emprego, outros nenhum, outros negativo.

**O que isso faz com o argumento.** A hipótese H-A se sustenta como mecanismo. A pergunta de crescimento de Pinha faz sentido onde há demanda reprimida, e a pergunta do corte é a conta certa onde a demanda está saturada. Isso troca uma discussão de caráter por uma pergunta empírica, que é o movimento do artigo.

**Cuidados.**
- A evidência é de bens industriais, nos Estados Unidos, numa escala de décadas. A aplicação a serviços com IA é extensão, e o texto precisa marcar isso como extensão.
- O caso Airbnb, com custo por noite caindo e reservas subindo, é *compatível* com demanda elástica, mas não a demonstra. As reservas não crescem por causa do custo de atendimento.
- Bessen cita Baumol (1967), "Macroeconomics of unbalanced growth", na mesma coluna. Isso dá uma ponte com a fonte original para a hipótese H-B, a do quarteto de cordas, que se apoia em Baumol e Bowen (1966).

**O que falta.** Ler o artigo completo para a especificação econométrica e o modelo. Procurar estimativas de elasticidade em serviços no Brasil, como atendimento, crédito e varejo digital.

---

## E3. Qualidade de gestão por empresa e empresas familiares

**Fontes lidas.**
- Bloom, Genakos, Sadun e Van Reenen, "Management Practices Across Firms and Countries", *Academy of Management Perspectives* 26(1), 2012; versão NBER WP 17850.
- PEDL Policy Insights nº 1 (Bloom, Lemos, Sadun, Scur e Van Reenen), no site do World Management Survey.
- Lemos e Scur, "The ties that bind", rascunho de março de 2019 (NBER) e CEPR Discussion Paper 13794, junho de 2019.
- Versão anterior: "All in the family? CEO choice and firm organization", CEP Discussion Paper 1528, janeiro de 2018.

**O que as fontes dizem.**
- Empresas de países em desenvolvimento, como Brasil, China e Índia, são em média menos bem geridas. Dentro de cada país, a dispersão é grande, e no Brasil e na Índia ela é particularmente notável, com uma cauda longa de empresas mal geridas (Bloom et al., 2012).
- Empresas de propriedade familiar e gestão familiar têm, em média, escores de gestão muito piores. As de propriedade familiar com gestão externa pontuam bem mais alto (PEDL).
- Segundo uma estimativa citada no PEDL (Bloom, Sadun e Van Reenen, 2016), a gestão responde, em média, por cerca de um quarto das diferenças de produtividade total dos fatores entre os Estados Unidos e outros países.
- **Lemos e Scur:**
  - *Amostra:* mais de 800 a 900 empresas na América Latina e na Europa, conforme a versão.
  - *Identificação:* a variável instrumental é o sexo dos filhos do CEO que sai. Ter pelo menos um filho homem aumenta em cerca de 30 pontos percentuais a chance de a sucessão ficar na família.
  - *Efeito:* a sucessão dinástica reduz a adoção de práticas estruturadas de gestão em cerca de 0,8 desvio-padrão (versão de 2018) ou 0,96 (versão de 2019). A queda implícita de produtividade é de 5% a 10%, por inferência e não por estimativa direta.
  - *Brasil:* mais de 500 empresas da onda de 2008 do WMS, pareadas com a PIA do IBGE (1999 a 2014). Um desvio-padrão a mais em gestão está associado a cerca de 12% mais valor adicionado nas empresas familiares e 18% nas não familiares (OLS).
  - *Mecanismo:* habilidade e conhecimento do CEO explicam parte da diferença, mas não a maior parte. O mecanismo proposto é o compromisso implícito com os empregados: o CEO da família não consegue se comprometer de forma crível a demitir sem um custo de reputação. Empresas que levam o nome da família adotam menos práticas de gestão de pessoas.

**O que isso faz com o argumento.**
- *Com Pinha:* a dispersão entre empresas brasileiras é o dado que faltava para a objeção do artigo. Uma explicação que vale para todo o empresariado não explica a cauda longa. E, onde o preparo foi medido (a habilidade do CEO familiar), ele explica só parte da diferença.
- *Com o livro:* a mesma dispersão é a autocrítica ao capítulo 2, §5. Hofstede dá a média nacional, e a variação que importa está entre empresas.
- *Hipótese nova, a mais provocadora desta rodada:* a evidência sugere que as empresas familiares com CEO da família ficam para trás na gestão em parte porque *não querem* demitir. O compromisso implícito com quem trabalha lá é um ativo relacional, no sentido do capítulo 9, §5, e é também um freio à adoção de práticas estruturadas. O livro trata os ativos relacionais como o que a transformação deve preservar. Lemos e Scur mostram que eles também têm custo. O Padrão 3 do capítulo 9 ganha uma tensão real: preservar o vínculo sem que ele bloqueie a gestão. Essa é uma extensão minha, e não um achado das autoras sobre IA.

**Cuidados.**
- Lemos e Scur aparecem como working paper (CEPR DP 13794). Não encontrei versão publicada em periódico com revisão por pares.
- O coeficiente muda entre versões (0,8 e 0,96 desvio-padrão). Citar como "cerca de 0,8 a 1 desvio-padrão", com a versão indicada.
- Os dados brasileiros do WMS são de 2008 e cobrem só a indústria de transformação de porte médio.
- O WMS mede práticas de gestão, e não "preparo intelectual". A ponte com Pinha é minha.

**O que falta.** Conferir se há dados mais recentes do WMS para o Brasil, ou a pesquisa equivalente do IBGE com o Banco Mundial, se existir. Verificar se "The ties that bind" saiu em periódico depois de 2021.

---

## E4. Finalidade da adoção no Brasil (PINTEC Semestral 2024 e TIC Empresas 2024)

**Fontes lidas.**
- Agência IBGE Notícias, release da PINTEC Semestral 2024, pelo trecho indexado; a página não abriu na consulta direta.
- Reportagem da Agência Brasil, reproduzida pelo *Diário de Pernambuco* em 24/9/2025, com a lista de benefícios e obstáculos.
- Cetic.br, TIC Empresas 2024, tabela H10.

**PINTEC Semestral 2024.**
- **População:** 10.167 empresas das indústrias extrativas e de transformação com 100 ou mais pessoas ocupadas. Parceria do IBGE com ABDI e UFRJ; é uma estatística experimental.
- **Uso de IA:** 41,9% em 2024, contra 16,9% em 2022. As áreas que mais usam IA são Administração (87,9%), Comercialização (75,2%) e Desenvolvimento de projetos de produtos, processos e serviços (73,1%).

**Benefícios das tecnologias digitais avançadas** (o conjunto das tecnologias, não só IA; respostas múltiplas):

| Benefício | % das empresas |
|---|---|
| Aumento da eficiência | 90,3% |
| Maior flexibilidade em processos administrativos, produtivos e organizacionais | 89,5% |
| Melhoria no relacionamento com clientes ou fornecedores | 85,6% |
| Maior eficácia no atendimento ao mercado | 82,9% |
| Maior capacidade de desenvolver produtos ou serviços novos | 74,7% |
| Redução do impacto ambiental | 74,1% |
| Entrada em novos mercados | 43,8% |

**Obstáculos.** Entre as que usam: custo alto (78,6%) e falta de pessoal qualificado (54,2%). Entre as que não usam: custo alto (74,3%) e falta de pessoal qualificado (60,6%).

**TIC Empresas 2024** (Cetic.br, empresas com 10 ou mais pessoas que usaram IA; 13% do total em 2024, segundo a cobertura da *Forbes Brasil*). Finalidades da IA:

| Finalidade | Total | 250 ou mais pessoas |
|---|---|---|
| Marketing ou vendas | 37% | 28% |
| Segurança digital | 36% | 39% |
| Gestão de empresas | 35% | 24% |
| Organização de processos de administração | 33% | 29% |
| Gestão de RH ou recrutamento | 28% | 27% |
| Processos de produção | 24% | 22% |
| Logística | 24% | 23% |

A tabela não tem categoria de novos produtos nem de P&D.

**O que isso faz com o argumento.**
- A leitura de Pinha, de que a IA no Brasil vira só corte, não se confirma nos dados declarados da indústria. Três em cada quatro citam maior capacidade de desenvolver produtos novos.
- A lacuna está em mercado: menos da metade cita entrada em novos mercados. É a pergunta de Pinha com menos resposta empírica, e coincide com a lacuna do livro ("regional para global").
- O obstáculo mais citado depois do custo é a falta de pessoal qualificado, o que conversa com a armadilha de Becker do capítulo 5.

**Cuidados.**
- Os benefícios valem para todas as tecnologias digitais avançadas, não para a IA isolada.
- São benefícios declarados, com respostas múltiplas. Citar 74,7% como "capacidade de desenvolver produtos novos" é diferente de dizer que a empresa lançou produtos novos.
- Ainda não li as tabelas no IBGE; os percentuais vêm da reportagem da Agência Brasil. Conferir no SIDRA ou na publicação da PINTEC Semestral antes de publicar.
- A TIC Empresas 2025 (divulgada em junho de 2026) registra adoção média de 17%, segundo a cobertura. Vale trocar pela edição mais recente se a tabela de finalidades for repetida.

---

## 5. Correção proposta para o livro (cap. 1, §5)

**Trecho atual:** "74% do valor econômico gerado por IA é capturado por apenas 20% das empresas. A maioria das organizações que investe em IA não está gerando retorno mensurável. Uma minoria está gerando retorno desproporcional."

**Problema:** o estudo mede o desempenho em pontos percentuais em relação à mediana do setor. Os quintis vão de −2,6 a 15,7, e três dos cinco estão acima da mediana. Uma medida relativa não diz quantas empresas têm retorno absoluto. A frase do meio não decorre do estudo. Talvez venha da *Global CEO Survey* de 2026, em que a maioria dos CEOs declarou ainda não ver retorno, segundo a cobertura; essa fonte não foi conferida.

**Redação proposta:**
> No estudo de desempenho em IA da PwC de 2026, com 1.217 executivos de empresas grandes, sobretudo de capital aberto, 20% das empresas capturam 74% dos ganhos atribuídos à IA. As que lideram não se distinguem por usar mais IA, mas por apontá-la para crescimento e reinvenção do modelo de negócio, e por medir de forma sistemática o que ela entrega.[^nota]

**Nota proposta:** PwC (2026). *Want ROI from AI? Go for growth*. Pesquisa com 1.217 executivos de nível diretor ou acima, em 25 setores e seis regiões, de outubro a novembro de 2025; 91% de empresas de capital aberto. O desempenho é medido em relação à mediana do setor e combina receita e eficiência atribuídas à IA. Correlação em corte transversal, com dados declarados pelos executivos.

---

## 6. Como as quatro evidências reorganizam o próximo artigo

| Explicação | Evidência desta rodada | Situação |
|---|---|---|
| Preparo das lideranças (Pinha) | Em empresas familiares, a habilidade do CEO explica parte, mas não a maior parte, do déficit de gestão (Lemos e Scur) | Parcial: existe, mas não é o mecanismo principal medido |
| Cultura nacional (livro, cap. 2) | Dispersão grande entre empresas brasileiras (Bloom et al., 2012) | Fraca para explicar a variação entre empresas |
| A régua (artigo "Contar cabeças") | Líderes têm 80% mais chance de medir o impacto de forma sistemática (PwC) | Compatível, sem teste causal |
| Elasticidade da demanda | Bessen: a elasticidade decide o sinal do efeito sobre o emprego | Forte como mecanismo histórico; extensão para IA a marcar |
| Compromisso implícito (novo) | Lemos e Scur: custo de reputação ao demitir freia a gestão estruturada | Hipótese nova para o livro e para o artigo |

A espinha "três explicações para a mesma pergunta" ganha uma quarta e uma quinta. O fecho mais forte talvez seja o de Lemos e Scur: em parte das empresas brasileiras, o problema de gestão vem menos de quererem cortar gente demais e mais de não conseguirem cortar nada, nem pessoas nem práticas. As duas coisas cabem no mesmo país, e uma régua de cabeças não distingue uma da outra.

---

## Fontes

- [PwC, *Want ROI from AI? Go for growth* (PDF)](https://www.pwc.com/gx/en/so-you-can/2026/content/roi-from-ai.pdf)
- [PwC, página do estudo](https://www.pwc.com/gx/en/1/issues/tech-data-ai/ai-roi.html)
- [PwC Austrália, release de 20/4/2026](https://www.pwc.com.au/media/2026/pwc-ai-performance-study-australian-companies-lead-on-ai-security.html)
- [Bessen (2019), RePEc, *Economic Policy* 34(100)](https://econpapers.repec.org/RePEc:oup:ecpoli:v:34:y:2019:i:100:p:589-626.)
- [Bessen, resumo em IPUMS](https://bibliography.ipums.org/citations/show/4b433b5a-f17c-3b9a-a979-c23145d75d97)
- [Bessen, coluna no VoxEU/CEPR](https://cepr.org/voxeu/columns/automation-and-jobs-when-technology-boosts-employment)
- [Bloom, Genakos, Sadun e Van Reenen (2012), Harvard DASH](https://dash.harvard.edu/server/api/core/bitstreams/fcd005f8-68ee-41f4-8789-9415919a6faa/content)
- [PEDL Policy Insights nº 1, World Management Survey](https://worldmanagementsurvey.org/wp-content/uploads/2017/10/PEDL-Policy-Insights-Series-No.-1.pdf)
- [Lemos e Scur (2019), "The ties that bind", rascunho NBER](https://conference.nber.org/conf_papers/f118307.pdf)
- [Scur e Lemos (2019), CEPR DP 13794](https://econpapers.repec.org/RePEc:cpr:ceprdp:13794)
- [Lemos e Scur (2018), CEP DP 1528, LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/88679)
- [Agência IBGE Notícias, PINTEC Semestral 2024](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-noticias/noticias/44551-de-2022-a-2024-percentual-de-empresas-industriais-utilizando-inteligencia-artificial-subiu-de-16-9-para-41-9)
- [Agência Brasil via *Diário de Pernambuco*, 24/9/2025](https://www.diariodepernambuco.com.br/brasil/2025/09/11696571-numero-de-empresas-industriais-que-usam-ia-cresce-163-em-dois-anos.html)
- [Cetic.br, TIC Empresas 2024, tabela H10](https://cetic.br/en/tics/pesquisa/2024/empresas/H10/)
