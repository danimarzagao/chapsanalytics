# O agente com crachá

*A SK Telecom dá número de funcionário a agentes de IA, define quem responde por eles, avalia o desempenho de cada um e desliga os que deixam de ser necessários. O resultado entra na avaliação e na remuneração dos executivos que os supervisionam. É, quase ponto a ponto, o método de calibração que propus para gestores, posto em norma por uma empresa, com duas regras que eu não tinha previsto*

---

Em 26 de outubro, a operadora sul-coreana SK Telecom publicou seu primeiro relatório de governança de inteligência artificial. São 40 páginas, em coreano, e a maior parte trata do que se espera de um documento assim: proteção de dados, avaliação de risco dos serviços oferecidos aos clientes, a norma internacional ISO/IEC 42001, que a empresa já tinha para os serviços ao público e em outubro estendeu à gestão dos agentes que usa internamente.

A parte que me fez parar está na página 29. Ali a empresa escreve que "reconhece oficialmente o agente de IA com número de funcionário como uma nova força de trabalho". E descreve o que isso significa na prática: os agentes passam por avaliação de desempenho, e o resultado, no curto prazo, entra na avaliação e na remuneração dos executivos e em prêmios para os empregados. No longo prazo, a empresa considera incluí-lo nas metas da organização.

Começo pelo que não sei. O relatório descreve o sistema, não os resultados dele. Não sei quantos agentes têm número, se algum já foi desligado ou premiado, nem quanto pesa o desempenho de um agente na nota de um executivo. Tudo o que escrevo aqui é sobre o desenho, publicado pela própria empresa, e as traduções do coreano são minhas.

O desenho converge, quase ponto a ponto, com o método que propus no capítulo 4 de *O Trabalho que Vem* para calibrar a autonomia de agentes. E acrescenta duas regras que o livro não tem. A primeira dá autonomia ao trabalho que pode ser medido. A segunda faz o desempenho do agente pesar na avaliação de quem o supervisiona. As duas fazem sentido, e as duas empurram para o mesmo lugar o trabalho que não se mede.

## Como um agente ganha crachá

O projeto começou a ser anunciado em junho. No lançamento do programa que a empresa chama de AX Innovation 2.0, o presidente Jeong Jae-heon disse que os agentes seriam tratados como "funcionários digitais", com número, departamento, função e permissões, geridos "por procedimentos semelhantes aos das pessoas, da contratação ao desligamento", segundo a TelecomTV e a agência de notícias coreana Edaily. O relatório de outubro mostra como isso foi posto em funcionamento.

Um agente desenvolvido internamente recebe primeiro uma identificação básica, que serve para saber que ele existe. O número de funcionário só vem depois de uma avaliação que verifica se ele cumpre os critérios da empresa. Com o número, o agente passa a ter, registrados, a tarefa que executa, a área a que pertence, o seu estado de operação, o seu desempenho e um responsável humano. O relatório diz que o núcleo do sistema é o "processamento autônomo e responsável do trabalho": quanto mais um agente faz sozinho, mais claro tem de ser quem o supervisiona, com que critério e em que escopo.

O responsável varia com o risco. Um agente que ajuda uma pessoa nas suas próprias tarefas pode ser gerido por quem o usa. Um agente de maior impacto, ou mais autônomo, "deve obrigatoriamente" ter como responsável um líder de equipe ou um executivo. E a empresa define, tarefa a tarefa, "até onde o agente decide e executa sozinho, e em que ponto o humano intervém": revisão e aprovação antes de decisões importantes, monitoramento durante a execução, verificação depois.

Tudo isso passa por um sistema interno, o Agent OS, que registra cada etapa da execução, os modelos e ferramentas usados, as mudanças de configuração, o consumo de recursos e o custo. Se algo dá errado, o registro permite reconstruir o que aconteceu, e o sistema permite interromper o agente.

Cha Ho-beom, diretor de privacidade da SKT e responsável pela governança de IA, resumiu a lógica no comunicado de lançamento do relatório, em outubro: "Na era dos agentes de IA, a importância da governança de IA cresce ainda mais."

## O que o livro dizia, e o que a SKT fez

No capítulo 4 do livro, defendi que a adoção de agentes cria uma tarefa nova para o gestor: calibrar autonomia. Delegar a uma pessoa vem com sinais que ajudam a calibrar: ela faz perguntas, tem um histórico, cansa. Delegar a um agente não vem com nenhum desses sinais. Por isso propus quatro parâmetros para decidir quanta autonomia dar a um agente numa tarefa: a especificidade do contexto que a tarefa exige, a reversibilidade das ações, a frequência de casos fora do padrão e o custo do pior erro provável. E escrevi que eles não produzem uma fórmula, só uma conversa estruturada que o gestor precisa ter antes de ampliar a autonomia.

A SKT transformou a conversa em norma. Na página 28, o relatório lista três fatores que a empresa considera obrigatoriamente antes de dar número a um agente e definir o que ele pode fazer: se a tarefa tem um procedimento operacional padrão; se o desempenho pode ser medido objetivamente; e se o agente tem capacidade de concluir a tarefa sem intervenção humana. Esses três fatores, diz o texto, são a base para estimar a autonomia e o risco. A avaliação de risco considera ainda o impacto da tarefa, a sensibilidade dos dados e o nível de automação.

O procedimento padrão e a capacidade de concluir sem ajuda são, quase exatamente, o avesso de dois parâmetros do livro: tarefa com procedimento definido é tarefa de pouco contexto específico, e tarefa que se conclui sem humano é tarefa com poucos casos fora do padrão. O impacto e a sensibilidade dos dados fazem o trabalho do custo de erro. Fico contente de ver o método funcionando fora do livro, e mais contente ainda de ver que a empresa fez o que eu só recomendei: escreveu e pôs em auditoria.

## A primeira regra que eu não tinha previsto

O fator que a SKT acrescenta, e que o livro não tem, é o segundo: o desempenho pode ser medido objetivamente?

A regra é sensata: se não dá para medir o que o agente entrega, não dá para saber se ele está funcionando, e dar autonomia a algo que não se avalia é imprudência. Mas tem um efeito colateral. Ela orienta a autonomia para o trabalho mensurável. E o trabalho difícil de medir fica com as pessoas.

No mesmo capítulo do livro, separei três tipos de tarefa: as de execução, cujo critério de qualidade se define antes; as de julgamento, que lidam com informação ambígua e decisão sob incerteza; e as de cuidado, em que o valor está na presença humana. As de execução são as que se medem bem. As outras duas são, quase por definição, as que se medem mal. A regra da SKT não diz que só as tarefas de execução vão para agentes, mas a consequência provável é essa, e não me parece ruim. O problema aparece no passo seguinte.

Em "Perguntar não mede", escrevi sobre escolas que tentam saber se a IA está prejudicando o aprendizado pela percepção dos professores, quando a única medida confiável é a prova sem a ferramenta. Aqui o risco é o inverso. O agente é medido com precisão, porque foi escolhido justamente por ser mensurável. O humano fica com o trabalho que não tem métrica clara, e é avaliado por métricas que não o descrevem bem.

## A segunda regra: o executivo avaliado pelo agente

Na página 29, a avaliação dos agentes é descrita em detalhe. Usuários e responsáveis fazem uma autoavaliação, explicando o efeito real do agente sobre o trabalho. Um comitê de especialistas em IA avalia competência e desempenho, com base nos dados de operação e em indicadores definidos antes. Na página 30, a avaliação periódica inclui também o custo de operação, e "o agente cuja necessidade diminuiu tem a operação encerrada".

E então vem a ligação com as pessoas. O relatório diz que o resultado da avaliação, no curto prazo, se vincula à avaliação e à remuneração dos executivos e a prêmios para os empregados. E acrescenta que a avaliação "é mais do que uma pontuação": serve de base para ampliar os agentes e "melhorar a distribuição do trabalho entre pessoas e agentes".

Na prática, um executivo da SKT responsável por agentes de alto impacto passa a ter parte da nota, e talvez do bônus, definida pelo desempenho deles. O relatório não diz quanto. Pode ser pouco. Mas o desenho é claro: o desempenho do agente vira desempenho do humano que responde por ele.

No capítulo 5 do livro, escrevi que o contrato de trabalho precisa ser reformulado: a empresa investe em formar julgamento nas pessoas, e o profissional investe em desenvolver a capacidade de supervisionar agentes com ceticismo calibrado, que é a competência que vai valer na próxima década. A SKT fez algo próximo disso, por outro caminho. Em vez de remunerar a capacidade de supervisionar, remunera o resultado do supervisionado.

Há uma tensão aqui que não resolvo. Ligar a remuneração do executivo ao agente que ele supervisiona é coerente com a ideia de responsabilidade: se você responde pelo agente, deve ganhar ou perder com ele. Mas é também um incentivo forte para escolher agentes que se medem bem, ampliar o que dá número e desligar o que dá custo. O sistema estaria funcionando exatamente como foi desenhado. O que me pergunto é o que acontece com a pessoa cuja contribuição é ajudar um agente a errar menos num caso que nenhum indicador captura.

## O que fazer com isso

Para quem está adotando agentes, o relatório da SKT é o modelo publicado de governança interna mais detalhado que encontrei. Recomendo lê-lo inteiro e copiar três coisas: o responsável humano proporcional ao risco, o registro de cada execução e o critério explícito de desligamento. Quase nenhuma empresa que conheço tem as três, e muitas têm agentes rodando sem nenhuma.

Para quem desenha avaliação de desempenho, a pergunta que o caso coloca vem antes do indicador: o que estamos medindo nas pessoas que supervisionam agentes? Se a resposta for o desempenho do agente, convém medir também o que o agente não captura: os erros que o humano evitou, os casos fora do padrão que ele resolveu, o tempo que gastou ensinando o agente. São exatamente as coisas que não entram num painel.

E para quem pensa no trabalho que vem, a SKT oferece uma imagem concreta. O agente tem crachá, responsável, avaliação, prêmio indireto e desligamento, tudo escrito e certificado. Se a autonomia vai para o que se mede, e o humano passa a ser medido pelo agente, quem vai medir o trabalho que não se mede?

---

## Nota de verificação

**Lido na fonte primária.** O relatório de governança de IA da SK Telecom ("AI 거버넌스 리포트"), de outubro de 2026, em coreano; li a Parte 3, sobre o uso interno de IA, nas páginas 24 a 30, e consultei o restante para o contexto. O comunicado da empresa de 26 de outubro de 2026, também em coreano. Todas as traduções são minhas e devem ser conferidas no original por quem for citar.

**Lido em reportagem original.** Financial News (파이낸셜뉴스), Yoon Hong-jip, 26 de outubro de 2026, que descreve o mesmo relatório. TelecomTV e Edaily, de junho de 2026, sobre o lançamento do programa AX Innovation 2.0 e a fala do presidente Jeong Jae-heon. RCR Wireless e SBS Star, de junho, que confirmam o desenho.

**O que não consegui verificar.** O número de agentes com número de funcionário na SKT; se algum foi desligado ou deu origem a prêmio; o peso do desempenho dos agentes na avaliação de executivos; e como a empresa avalia seus funcionários humanos, sobre o que o relatório não trata. Por isso o texto não compara a avaliação dos agentes com a das pessoas na SKT, só com o que o livro propõe.

**Sobre o livro.** Os trechos de *O Trabalho que Vem* (Marzagão, 2026) citados são do capítulo 4, seções 2 e 4, e do capítulo 5, seção 9, relidos para este texto.

---

## Referências

EDAILY. SKT Assigns Employee Numbers to AI Agents: "Transitioning to an Organization That Works with AI". Junho de 2026.

FINANCIAL NEWS (파이낸셜뉴스). YOON, Hong-jip. AI에이전트에 사번 부여하고 권한·책임 관리한다...SKT. 26 out. 2026.

MARZAGÃO, Daniela. *O Trabalho que Vem: Como Você e Sua Empresa se Preparam para o Futuro*. 2026. Capítulos 4 e 5.

RCR WIRELESS. SK Telecom's plan to give every worker an AI agent. 18 jun. 2026.

SBS STAR. SK Telecom Assigns Employee IDs to AI, Ushering in the 'Era of AI Colleagues'. Junho de 2026.

SK TELECOM. AI 거버넌스 리포트 (Relatório de Governança de IA). Outubro de 2026.

SK TELECOM. SKT, 'AI 트러스트 경영' 강화… 「AI 거버넌스 리포트」 첫 발간. Comunicado, 26 out. 2026.

TELECOMTV. SK Telecom is building an agentic AI workforce. Junho de 2026.

---

*Este artigo integra a série VibeCoding em Contexto. A calibração de autonomia está no capítulo 4 de* O Trabalho que Vem*. A medida sem ferramenta está em "Perguntar não mede".*
