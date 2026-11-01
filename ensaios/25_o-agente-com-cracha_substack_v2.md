# O agente com crachá

*A SK Telecom dá número de funcionário a agentes de IA, nomeia quem responde por eles, avalia cada um e desliga os que deixam de ser úteis. O desenho converge com o método de calibração que propus para gestores e acrescenta duas regras que o livro não tem. As duas fazem sentido, e as duas empurram para o mesmo canto o trabalho que não se mede*

---

"A SKT reconhece oficialmente o agente de IA com número de funcionário como uma nova força de trabalho." A frase está na página 29 do primeiro relatório de governança de IA da operadora sul-coreana, publicado em 26 de outubro. Logo abaixo, uma tabela diz o que fazer com a avaliação de desempenho desses agentes: no curto prazo, ligá-la à avaliação e à remuneração dos executivos e a prêmios para os empregados; no longo prazo, considerar levá-la aos indicadores de desempenho da organização.

O resto do documento, 40 páginas em coreano, trata do que se espera de um relatório assim: proteção de dados, avaliação de risco dos serviços ao cliente, a norma ISO/IEC 42001, que a empresa obteve em 2024 para os serviços ao público e em outubro estendeu à gestão dos agentes internos. Há um contexto que o relatório não menciona e que ajuda a lê-lo. Em agosto de 2025, a autoridade coreana de proteção de dados aplicou à SKT a maior multa da sua história, 134,8 bilhões de wons, pelo vazamento de dados de chips de cerca de 23 milhões de clientes, e entre as medidas corretivas mandou rever a governança para reforçar o papel do diretor de privacidade. É esse diretor, Cha Ho-beom, quem hoje responde também pela governança de IA. A empresa que escreve as regras mais detalhadas que encontrei para supervisionar agentes aprendeu, da forma mais cara, o que acontece quando o acesso a sistemas não tem dono.

O relatório descreve o sistema, não os resultados dele. Não sei quantos agentes têm número, se algum já foi desligado ou premiado, nem quanto pesa o desempenho de um agente na nota de um executivo. Tudo o que escrevo aqui é sobre o desenho publicado pela própria empresa, e as traduções do coreano são minhas.

## Como um agente ganha crachá

A ideia foi anunciada em junho, no programa que a empresa chama de AX Innovation 2.0, apresentado pelo CEO Jeong Jae-heon num fórum interno do grupo SK. No comunicado, a SKT disse que os agentes receberiam número, departamento, função e permissões e seriam geridos "por procedimentos semelhantes aos das pessoas, da contratação ao desligamento". O relatório de outubro mostra como isso foi posto para funcionar.

Um agente desenvolvido internamente recebe primeiro uma identificação básica, que só registra que ele existe. O número de funcionário vem depois de uma avaliação que verifica se ele cumpre os critérios da empresa. Com o número, ficam registrados a tarefa que executa, a área a que pertence, o seu estado de operação, o seu desempenho e um responsável humano. O princípio declarado é o "processamento autônomo e responsável do trabalho": quanto mais um agente faz sozinho, mais claro tem de estar quem o supervisiona, com que critério e em que escopo.

O responsável varia com o risco. Um agente que ajuda uma pessoa nas suas próprias tarefas pode ser gerido por quem o usa; um de maior impacto, ou mais autônomo, precisa "obrigatoriamente" ter como responsável um líder de equipe ou um executivo (página 27). E a empresa define, tarefa a tarefa, até onde o agente decide e executa sozinho e em que ponto o humano entra: revisão e aprovação antes de decisões importantes, monitoramento durante a execução, verificação depois.

Tudo passa por um sistema interno, o Agent OS, que registra cada etapa da execução, os modelos e ferramentas usados, as mudanças de configuração e o consumo de recursos. Se algo dá errado, o registro permite reconstruir o que aconteceu, e o sistema permite parar o agente na hora.

## O que o livro dizia, e o que a SKT fez

No capítulo 4 de *O Trabalho que Vem*, defendi que a adoção de agentes cria uma tarefa nova para o gestor: calibrar autonomia. Quem delega a uma pessoa recebe sinais que ajudam a calibrar (ela faz perguntas, tem histórico, cansa), e quem delega a um agente não recebe nenhum deles. Propus por isso quatro parâmetros para decidir quanta autonomia dar a um agente numa tarefa: a especificidade do contexto que a tarefa exige, a reversibilidade das ações, a frequência de casos fora do padrão e o custo do pior erro provável. E escrevi que eles não produzem uma fórmula, só uma conversa estruturada que o gestor precisa ter antes de ampliar a autonomia.

A SKT transformou a conversa em norma. Na página 28, o relatório lista três fatores que a empresa considera obrigatoriamente antes de dar número a um agente e definir o que ele pode fazer: se a tarefa tem um procedimento operacional padrão, se o desempenho pode ser medido objetivamente e se o agente consegue concluir a tarefa sem intervenção humana. A avaliação de risco soma o escopo e o impacto da tarefa, o tipo e a sensibilidade dos dados, o nível de automação e autonomia, o modelo usado e o ambiente de operação.

Três dos meus quatro parâmetros aparecem ali, quase sempre pelo avesso. Tarefa com procedimento padrão é tarefa de pouco contexto específico; tarefa que se conclui sem humano é tarefa com poucos casos fora do padrão; impacto e sensibilidade dos dados fazem o trabalho do custo do erro. O quarto falta: procurei no relatório inteiro os termos coreanos para reversibilidade e recuperação e não encontrei nenhum. Nisso a SKT está atrás de quem escreve as regras do setor. O marco de governança de agentes que Singapura publicou em janeiro, e revisou em maio, trata a reversibilidade como fator de risco próprio: um agente que marca reuniões consegue remarcá-las se errar, e um que manda e-mail para fora da empresa não tem como desmandar. Num dos casos documentados pelo marco, a Dayos classificou cada tipo de chamado de TI por gravidade, reversibilidade e viabilidade de supervisão humana, e deixou o nível mais alto fora do alcance do agente. Um artigo da Google DeepMind sobre delegação entre humanos e IA lista onze dimensões de uma tarefa, entre elas a verificabilidade, a reversibilidade e a contextualidade. A SKT ficou com a primeira; o livro, com as duas últimas.

Não tenho nenhum sinal de que um documento tenha influenciado o outro, e é isso que torna a coincidência interessante. Quando lugares sem contato entre si (um livro brasileiro, uma operadora coreana, um laboratório de IA) chegam aos mesmos eixos, a hipótese mais econômica é que os eixos estão no problema. A diferença é de estatuto: o que no livro era recomendação, na SKT virou regra escrita e auditada por terceiros.

## A primeira regra que o livro não tem

O fator que a SKT acrescenta é o segundo, a verificabilidade da lista da DeepMind: o desempenho pode ser medido objetivamente?

A regra é sensata. Se não dá para medir o que o agente entrega, não dá para saber se ele funciona, e dar autonomia a algo que ninguém avalia é imprudência. O efeito colateral é que ela orienta a autonomia para o trabalho mensurável e deixa com as pessoas o trabalho difícil de medir.

No mesmo capítulo do livro, separei três tipos de tarefa: as de execução, cujo critério de qualidade se define antes; as de julgamento, que lidam com informação ambígua e decisão sob incerteza; e as de cuidado, em que o valor está na presença humana. As de execução se medem bem, e as outras duas, quase por definição, se medem mal. A regra da SKT não diz que só as tarefas de execução vão para agentes, mas essa é a consequência provável, e ela não me parece ruim em si.

A economia descreveu o passo seguinte em 1991, quando Bengt Holmström e Paul Milgrom mostraram que, quando um trabalho tem uma parte fácil de medir e outra difícil, pagar forte pela parte medida desvia o esforço da outra, e às vezes o melhor contrato é o de incentivo fraco. O modelo deles trata de uma pessoa repartindo esforço entre tarefas. Se a lógica se estender a uma organização que reparte tarefas entre agentes e pessoas, a SKT montou as duas metades do problema: o agente é medido com precisão porque foi escolhido por ser mensurável, e o humano fica com o que não tem métrica clara e continua sendo avaliado por métricas que não o descrevem.

Em "Perguntar não mede", escrevi sobre escolas que tentam saber se a IA prejudica o aprendizado pela percepção dos professores, quando a medida confiável é a prova sem a ferramenta. Lá faltava medida para o humano. Aqui sobra medida para o agente, e o humano herda a falta.

## A segunda regra: o executivo e a nota do agente

A página 29 descreve a avaliação dos agentes em detalhe. Usuários e responsáveis fazem uma autoavaliação, explicando o efeito real do agente sobre o trabalho. Um comitê de especialistas em IA avalia competência e desempenho com base nos dados de operação e em indicadores definidos antes. Na página 30, a avaliação periódica inclui o custo de operação, e "o agente cuja necessidade diminuiu tem a operação encerrada".

No corpo do texto, o resultado é ligado ao desempenho da organização e contado como produtividade organizacional. Na tabela que fecha a página, o uso de curto prazo aparece como avaliação e remuneração dos executivos e prêmios para os empregados, e o relatório diz que a avaliação "tem um significado maior do que uma pontuação": serve de base para ampliar os agentes e "melhorar a distribuição do trabalho entre pessoas e agentes".

O relatório não especifica quais executivos, nem por qual regra a nota do agente entra na deles. A leitura que me parece mais natural, porque é o único elo entre executivos e agentes descrito no documento, é que o executivo responsável por um agente de alto impacto passe a ter parte da nota, e talvez do bônus, ligada ao desempenho desse agente. Pode ser outra coisa (uma meta geral de adoção de IA por área, por exemplo), e pode pesar pouco. Mas, se a leitura estiver certa, o desempenho do agente vira desempenho do humano que responde por ele.

No capítulo 5 do livro, escrevi que o contrato de trabalho precisa ser refeito: a empresa investe em formar julgamento nas pessoas, e o profissional investe em supervisionar agentes com ceticismo calibrado, que é a competência que vai valer na próxima década. A SKT chega perto disso por outro caminho. Em vez de remunerar a capacidade de supervisionar, remuneraria o resultado do supervisionado.

Ligar a remuneração do executivo ao agente que ele supervisiona é coerente com a ideia de responsabilidade, porque quem responde pelo agente deve ganhar ou perder com ele. É também um incentivo forte para escolher agentes que se medem bem, ampliar o que dá número e desligar o que dá custo, e o sistema estaria funcionando exatamente como foi desenhado. Não sei resolver essa tensão. Sei onde ela dói: na pessoa cuja contribuição é ajudar um agente a errar menos num caso que nenhum indicador captura.

O teatro tem um nome para esse trabalho: o ponto, que sopra o texto da coxia e faz a sua melhor noite quando a plateia sai sem saber que ele existia. A peça é avaliada pelo elenco; o ponto, pelo que não aconteceu.

## O que fazer com isso

Para quem está adotando agentes, o relatório da SKT é o modelo publicado de governança interna mais detalhado que encontrei. Vale lê-lo inteiro e copiar três coisas: o responsável humano proporcional ao risco, o registro de cada execução e o critério explícito de desligamento. Das empresas que conheço por dentro, quase nenhuma tem as três, e muitas têm agentes rodando sem nenhuma. Eu acrescentaria a quarta que falta à SKT e que o marco de Singapura já tem: a reversibilidade como critério à parte, avaliada antes do impacto.

Para quem desenha avaliação de desempenho, a pergunta que o caso coloca vem antes do indicador: o que estamos medindo nas pessoas que supervisionam agentes? Se a resposta for o desempenho do agente, convém medir também o que o agente não registra: os erros que o humano evitou, os casos fora do padrão que ele resolveu, o tempo que gastou ensinando o agente. O próprio registro de execução que a SKT exige já permite começar, contando quantas vezes o humano interveio e em que tipo de caso. É pouco perto do que se perde, mas é o que entra num painel.

E para quem pensa no trabalho que vem, a SKT oferece uma imagem concreta. O agente tem crachá, responsável, avaliação, prêmio indireto e desligamento, tudo escrito e certificado. Se a autonomia vai para o que se mede, e o humano passa a ser medido pelo agente, quem vai medir o ponto?

---

## Nota de verificação

**Lido na fonte primária.** O relatório de governança de IA da SK Telecom ("AI 거버넌스 리포트"), de outubro de 2026, em coreano (sktelecom.com/img/pds/persist_biz/2026/SKT_AI_Governance_Report.pdf). Conferi no original os três fatores para a concessão do número e os critérios de risco (p. 28), o reconhecimento do agente como força de trabalho e a ligação com a avaliação e a remuneração dos executivos (p. 29), o encerramento dos agentes cuja necessidade diminuiu (p. 30) e o responsável por nível de risco (p. 27). Para a ausência da reversibilidade, busquei no texto integral do PDF os termos 가역, 비가역, 되돌, 복구, 복원, 원복, 롤백, 취소, 철회 e 회복, sem nenhuma ocorrência. O comunicado da empresa de 26 de outubro de 2026, também em coreano. O marco de governança de agentes da IMDA, versão 1.5 de 20 de maio de 2026 (reversibilidade como fator de risco na p. 16; caso Dayos na p. 18; aprovação humana para ações irreversíveis na p. 29), e o comunicado da atualização. O artigo de Tomašev, Franklin e Osindero, da Google DeepMind (lista de dimensões da tarefa na seção 2.2). Todas as traduções são minhas e devem ser conferidas no original por quem for citar.

**Lido em reportagem original.** Financial News (파이낸셜뉴스), 26 de outubro de 2026, sobre o mesmo relatório. TelecomTV, Edaily, SBS Star e Aju News, de junho de 2026, sobre o AX Innovation 2.0; a frase "da contratação ao desligamento" é atribuída pela TelecomTV à empresa, não ao CEO. Korea Times e Light Reading, de 28 de agosto de 2025, sobre a multa da Comissão de Proteção de Informações Pessoais e as medidas corretivas.

**O que não consegui verificar.** O número de agentes com número de funcionário na SKT; se algum foi desligado ou deu origem a prêmio; quais executivos têm a avaliação ligada aos agentes e com que peso; e como a empresa avalia seus funcionários humanos, sobre o que o relatório não trata. A ligação entre a nota do agente e a do executivo que o supervisiona é leitura minha, marcada como tal no texto: o corpo da p. 29 fala em desempenho da organização, e só a tabela menciona executivos. A busca por reversibilidade foi textual; um conceito equivalente descrito com outras palavras escaparia dela, e por isso li também, por inteiro, as páginas 24 a 30.

**Sobre o livro.** Os trechos de *O Trabalho que Vem* (Marzagão, 2026) citados são do capítulo 4, seções 2 e 4, e do capítulo 5, seção 9, relidos para este texto.

---

## Referências

AJU NEWS (아주경제). SKT, AI 에이전트에 사번 부여…'AX 혁신 2.0' 추진. 16 jun. 2026.

EDAILY. SKT Assigns Employee Numbers to AI Agents: "Transitioning to an Organization That Works with AI". 16 jun. 2026.

FINANCIAL NEWS (파이낸셜뉴스). AI에이전트에 사번 부여하고 권한·책임 관리한다...SKT. 26 out. 2026.

HOLMSTRÖM, Bengt; MILGROM, Paul. Multitask Principal-Agent Analyses: Incentive Contracts, Asset Ownership, and Job Design. *Journal of Law, Economics, & Organization*, v. 7, número especial, p. 24-52, 1991.

IMDA (INFOCOMM MEDIA DEVELOPMENT AUTHORITY). *Model AI Governance Framework for Agentic AI*. Versão 1.5. Singapura, 20 maio 2026.

IMDA. Updated Model AI Governance Framework for Agentic AI. Factsheet, 20 maio 2026.

KOREA TIMES. SK Telecom fined $97 mil. over April data breach. 28 ago. 2025.

LIGHT READING. Privacy watchdog hits SKT with record $97M fine over data breach. 28 ago. 2025.

MARZAGÃO, Daniela. *O Trabalho que Vem: Como Você e Sua Empresa se Preparam para o Futuro*. 2026. Capítulos 4 e 5.

RCR WIRELESS. SK Telecom's plan to give every worker an AI agent. 18 jun. 2026.

SBS STAR. SK Telecom Assigns Employee IDs to AI, Ushering in the 'Era of AI Colleagues'. 16 jun. 2026.

SK TELECOM. AI 거버넌스 리포트 (Relatório de Governança de IA). Outubro de 2026.

SK TELECOM. SKT, 'AI 트러스트 경영' 강화… 「AI 거버넌스 리포트」 첫 발간. Comunicado, 26 out. 2026.

TELECOMTV. SK Telecom is building an agentic AI workforce. Junho de 2026.

TOMAŠEV, Nenad; FRANKLIN, Matija; OSINDERO, Simon. Intelligent AI Delegation. arXiv:2602.11865, 12 fev. 2026.

---

*Este artigo integra a série VibeCoding em Contexto. A calibração de autonomia está no capítulo 4 de* O Trabalho que Vem*. A medida sem ferramenta está em "Perguntar não mede".*
