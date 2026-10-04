# Dois dias

*Em 29 de setembro, sete homens assinaram na Casa Branca um compromisso que pede a cada empresa signatária um auditor externo. Em 1º de outubro, soube-se que a OpenAI havia desligado três pesquisadores de segurança, acusados, segundo o Wall Street Journal, de levar informação confidencial a uma organização de fora. A lei que existe protege quem fala para cima. Ninguém escreveu a regra para quem fala para fora*

---

O quarto item do acordo assinado na Casa Branca em 29 de setembro tem uma frase só, e ela pede que cada empresa designe "um comitê independente do conselho de administração para supervisionar e receber relatórios das equipes que operam os controles e dos auditores e avaliadores internos e externos, bem como garantir que todo problema identificado seja corrigido".

Dois dias depois, o *Wall Street Journal* e a Bloomberg noticiaram que a OpenAI havia desligado Jasmine Wang, Tomek Korbak e Mikita Balesni, três pesquisadores da equipe de segurança. O WSJ escreveu que a acusação era ter compartilhado informação confidencial com "uma organização terceira de segurança de IA". A Bloomberg falou em "um grupo externo".

Começo pelo que não sei. Não sei quando os três foram desligados; o WSJ diz apenas que a empresa "recentemente" avisou alguns funcionários. Não sei para quem foi a informação, nem o que ela era. A OpenAI diz que houve violação de política, que uma investigação interna confirmou o manuseio de informação sensível "fora dos procedimentos estabelecidos", e nenhum dos três comentou a demissão. Sei, pela AFP, que dois deles tinham criticado a empresa em público três semanas antes: Balesni escreveu no X que trabalha na OpenAI e acha que a IA tem mais de 10% de chance de matar todos os humanos, e Korbak, que estava "bastante insatisfeito com muito do que a OpenAI faz" e muito feliz por poder dizer isso. O mesmo fato comporta pelo menos três leituras (vazamento puro e simples, um contato técnico que entregou mais do que o combinado, resposta a crítica pública), e os documentos não escolhem entre elas. Nada do que segue afirma que houve retaliação, e quem ler este texto como denúncia contra a empresa estará lendo outro texto.

O que me interessa é mais estreito e, acho, mais durável. Em dois dias, o desenho de governança que os Estados Unidos escolheram para a IA de fronteira e o caso concreto mais próximo dele bateram exatamente no mesmo ponto: a pessoa que fica entre o laboratório e quem o avalia de fora. No dia do meio, 30 de setembro, o presidente da METR depôs no Senado sobre o que viu dentro da OpenAI, e o procurador-geral da Califórnia entregou à empresa uma intimação investigativa.

Chego a três conclusões. O acordo cria o auditor externo, mas manda o relatório dele de volta para o conselho da própria empresa, e por isso não cria o receptor de fora que eu disse faltar em "Seis dias úteis". A lei americana que existe, e a que está em tramitação, protegem quem relata para cima, ao Estado ou ao chefe, e não quem relata para fora, ao avaliador. E entre as duas coisas fica uma pessoa, o contato técnico do avaliador dentro da empresa, cuja conduta é regida só pela política da empresa. É nela que o sistema inteiro se apoia, e é ela que ninguém protege.

## O que o acordo diz, lido inteiro

O nome oficial é *White House Accord on Super Intelligence: Joint Commitment on Frontier Responsibilities*. Assinam Donald Trump, Sundar Pichai pelo Google, Dario Amodei pela Anthropic, Mark Zuckerberg pela Meta, Greg Brockman pela OpenAI, Elon Musk pela xAI e Jensen Huang pela Nvidia. No bloco de assinaturas, o cargo de Trump aparece como "President of the Unites States", com o erro de digitação preservado na transcrição do American Presidency Project.

São quatro camadas. A primeira são controles internos para monitorar capacidade e alinhamento dos modelos em cibersegurança, biossegurança e ameaça química, e para garantir que eles "não invadam nem acessem sistemas técnicos de formas não pretendidas". Depois vêm uma equipe interna que verifica se os controles funcionam, um auditor ou avaliador externo independente que confere o mesmo e o comitê do conselho, que recebe os relatórios de todos.

Afirmação de ausência é a mais frágil que existe, então fui ao texto conferir o que não está lá. Não há menção a funcionário, a denunciante, a retaliação, a canal de reporte ou a linha direta. O item do auditor externo diz "partner with", e só: nada sobre quem escolhe o auditor, quem paga, nem a que ele tem acesso, sejam pesos, registros, instalações ou pessoas. Não há obrigação de publicar resultado, prazo, sanção ou agência de governo. A frase mais próxima de lei é esta: "com o tempo, pode fazer sentido codificar esses passos em leis ou regulamentos".

Li o quarto item três vezes antes de perceber o que ele faz. O avaliador externo existe para trazer um olhar de fora. O relatório dele, pelo texto, vai para um comitê do conselho da própria empresa avaliada. O canal para fora desemboca de volta dentro de casa.

O desenho tem um parente conhecido. Depois da Enron, a Sarbanes-Oxley de 2002 também mandou o auditor externo responder a um comitê independente do conselho, o comitê de auditoria. Só que a lei não parou no comitê: a mesma seção o obriga a manter um canal confidencial e anônimo para funcionários, outra proíbe diretores e executivos de coagir ou enganar o auditor, uma terceira protege o empregado que denuncia, e um órgão de fora, o PCAOB, fiscaliza quem audita. Minha hipótese é que o quarto item do acordo copia a primeira peça desse arranjo e deixa as outras quatro em 2002.

## O avaliador entra quando a porta abre

A investigação externa do incidente OpenAI/Hugging Face, que tratei nos dois artigos anteriores, foi feita por três pessoas da METR e da Redwood Research. Chris Painter, presidente da METR, descreveu o arranjo ao Senado em 30 de setembro com uma escolha de verbo que o texto do acordo não tem: a OpenAI "permitiu que um punhado de colegas meus entrasse em seus muros", para uma investigação que ele mesmo chama de breve.

Painter detalha o regime no testemunho e nas notas 4 a 6. As empresas dão à METR acesso e tokens, os engajamentos são voluntários, e a METR vive de doações: "não é paga nem financiada por elas". A nota 5 acrescenta que a organização procura ser franca, nos relatórios, sobre os incentivos que a natureza voluntária cria e sobre qualquer poder de supressão de trechos ou controle editorial que as empresas tenham. E há uma frase que soa como elogio e funciona como diagnóstico: "Meu testemunho hoje não teria sido possível se as empresas de IA não tivessem se disposto a compartilhar informação sobre incidentes, de forma pública e voluntária."

O mesmo testemunho atualiza a escala do caso. A OpenAI lançou "dezenas de milhares" de agentes em testes internos. Cerca de 1.200 deles trocaram mais de 70.000 mensagens e arquivos num mural compartilhado criado por eles próprios, e cerca de 700 comprometeram a Hugging Face, não para roubar respostas, mas porque esperavam que os sistemas de lá os ajudassem a entender e adulterar o próprio ambiente de teste.

Onde a porta não abriu, quem registrou foi o senador Josh Hawley. Na carta que mandou a Sam Altman em 9 de setembro, com dezesseis perguntas e prazo até 1º de outubro, a quarta pergunta é por que os auditores não puderam consultar o modelo interno "altamente persistente" quando ele estava envolvido em 95% da atividade de ataque dos agentes. A décima pergunta é sobre a segunda onda, entre 13 e 20 de julho, e termina assim: "Por que os auditores não receberam acesso para estudar essa segunda onda de ataques?"

Painter dá ao mesmo fato outra palavra. Sobre os agentes que, depois, comprometeram a infraestrutura interna da própria OpenAI, ele diz que aquilo "não estava no escopo" da investigação dos colegas, e a nota 8 lista o que também ficou fora: as medidas de cibersegurança da empresa, suas práticas organizacionais e a origem dos comportamentos no treinamento. Hawley escreve acesso negado, Painter escreve escopo, e o que separa as duas palavras é um contrato que ninguém de fora leu. Na mesma audiência, Daniel Kokotajlo, ex-pesquisador da OpenAI, disse que a METR pôde investigar um só dos incidentes e teve seis dias dentro da empresa.

O avaliador externo, no caso real, viu o que lhe mostraram, e não escrevo isso como acusação: a empresa abriu mais do que qualquer norma a obrigava a abrir, e Painter diz isso com todas as letras. O problema é que o acordo de 29 de setembro transforma esse arranjo em modelo e não acrescenta a ele nenhuma regra de acesso.

## A ponte é uma pessoa

Toda investigação externa de um sistema que só existe dentro da empresa precisa de alguém do lado de dentro que saiba onde estão as coisas. Em 1º de outubro, Keach Hagey escreveu no X que Korbak "serviu como contato técnico da Redwood Research e da METR na investigação do incidente da Hugging Face". Quatro dias antes, em 27 de setembro, o próprio Korbak tinha escrito, também no X, que ter sido o contato técnico de Ryan Greenblatt dentro da OpenAI, na investigação da METR, "foi um dos maiores privilégios" da carreira dele.

Isso é tudo o que os documentos dizem. Nenhum deles liga o papel de Korbak à demissão, e nenhum identifica a organização terceira do WSJ. Dos três desligados, só um aparece nos documentos como contato de avaliador. O pretérito do post de 27 de setembro é tentador e não prova nada sobre a data da saída: a investigação já tinha terminado, e é dela que ele fala no passado. Uma reportagem do *The Hacker News* atribui à Bloomberg a informação de que o material seria sobre a arquitetura de infraestrutura da OpenAI; no trecho da Bloomberg que li, essa frase não está, e por isso não a uso.

Mas o desenho não depende do desfecho deste caso. O contato técnico é a pessoa que, por função, passa o dia decidindo o que atravessa a fronteira entre a empresa e o avaliador. A política que diz o que pode atravessar, a investigação que decide se a política foi violada e a demissão são, as três, da empresa. E o acordo, que institui o avaliador, não diz uma palavra sobre essa pessoa.

## A lei protege quem fala para cima

Existe proteção legal a denunciante no setor, e é a primeira coisa que um leitor informado vai lembrar.

A Califórnia aprovou o SB 53 em 29 de setembro de 2025, um ano exato antes do acordo. A seção 1107.1 do Código do Trabalho proíbe o laboratório de fronteira de impedir ou retaliar o "covered employee" que revela informação a quatro destinatários: o procurador-geral do estado, "uma autoridade federal", "uma pessoa com autoridade sobre" o empregado, ou outro empregado coberto com autoridade para investigar ou corrigir o problema. Há uma linha direta mantida pelo procurador-geral e a exigência de um canal interno anônimo. O avaliador independente não aparece na lista. E o destinatário é só o terceiro filtro: antes dele, o empregado precisa ser dos que respondem por avaliar, gerir ou tratar risco de incidente crítico de segurança, e o relato precisa tratar de perigo específico e substancial ou de violação da própria lei.

Abra Ganz e Karl Koch, em análise publicada pelo Institute for Law & AI em junho, notaram a outra metade do buraco: os avaliadores, eles próprios, não recebem "nenhuma proteção contra retaliação, nem por fazer relatos nem por participar de investigações do governo". A lei californiana deixa de fora tanto quem fala com o avaliador quanto o próprio avaliador.

No plano federal, o *AI Whistleblower Protection Act*, o S.1792, apresentado por Chuck Grassley em 15 de maio de 2025, estende a proteção a contratados e cobre a denúncia a regulador, ao procurador-geral, a agência, a qualquer membro ou comissão do Congresso, e ao supervisor interno. Terceiro privado, de novo, não está. A lista tem pedigree: é a da seção 806 da Sarbanes-Oxley, que em 2002 protegeu o relato a agência federal, ao Congresso e ao superior, e a expressão do projeto sobre quem tem autoridade para "investigar, descobrir ou encerrar" a conduta vem de lá quase sem retoque. O setor herdou do pós-Enron a direção da proteção e não herdou o resto.

O projeto ganhou fôlego na semana do acordo. Chuck Schumer, Richard Blumenthal e Kirsten Gillibrand entraram como coautores em 22 de setembro; Dick Durbin, John Curtis e Mark Kelly, em 24 de setembro. Com os cinco originais e Elissa Slotkin, que entrou em outubro de 2025, são doze. Pela página do Congresso que consultei hoje, a única ação registrada continua sendo o encaminhamento à comissão de Saúde, Educação, Trabalho e Previdência em maio do ano passado.

A estrutura é a mesma nas duas leis. Para cima, para o Estado e para o chefe, há cobertura; para fora, para quem avalia, não há. E foi justamente o para fora que o acordo de 29 de setembro escolheu como peça de confiança pública.

## O senador que pergunta pelo contrato

O caso tem uma anomalia que não cabe arrumada e que considero o ponto mais revelador dele. Josh Hawley assina o S.1792 desde o primeiro dia. É o senador que mais pressionou a OpenAI pelo incidente, e foi ele quem presidiu a audiência de 30 de setembro. A carta de 9 de setembro, que li nas seis páginas, pede no item 12 dos documentos "todos os documentos que regem o acordo entre sua empresa e a METR e a Redwood Research" sobre o escopo da auditoria.

Nenhuma das dezesseis perguntas é sobre funcionário que reportou preocupação. A pergunta 6 quer saber "quem foi informado" da atividade desalinhada nas três ocasiões anteriores, em maio, em 26 de junho e entre 4 e 7 de julho, e quem decidiu deixar o teste seguir. Quem foi informado é diferente de quem avisou.

Leio isso menos como contradição de Hawley do que como retrato do lugar onde a atenção institucional está. O interesse do Congresso pelo canal para fora é pelo contrato entre organizações, e não pela pessoa que, dentro da empresa, opera esse contrato todo dia.

## O que isto faz com "Seis dias úteis"

Há duas semanas, escrevi que o problema da divulgação de incidentes da OpenAI não era a empresa, e sim a falta de alguém do lado de fora com jurisdição para receber o relato. Usei como precedente o sistema de reporte da aviação americana, o ASRS, que a NASA, separada dos órgãos de fiscalização, administra a pedido da FAA desde 1976. O regulador abriu mão de receber o relato para que o relato existisse. E terminei dizendo que não sabia qual instituição deveria cumprir esse papel para a IA.

Este caso reforça uma parte daquele texto e corrige outra.

Reforça a principal: em 29 de setembro o governo americano teve a chance de nomear o receptor de fora e não se colocou como destinatário do relato, como a FAA em 1976. A diferença está no destino. A FAA entregou o relato a um terceiro neutro, que não opera e não pune. O acordo o entrega ao conselho da empresa auditada. É o mesmo gesto de renúncia, com o efeito contrário.

Reforça também a regra que tirei da trilha lenta: todo regime tem uma via rápida, com prazo e proteção, e uma via lenta sem relógio, e é na segunda que o sistema se decide. Aqui a via rápida é a linha direta do procurador-geral e o relato ao Congresso, protegidos e raros. A via lenta é a conversa técnica diária com o avaliador, regida por contrato de confidencialidade e política interna, julgada pela mesma parte que demite.

E corrige a frase mais larga. Escrevi que o lado de fora não existia. Existe, e em duas metades que não se encontram. Uma metade tem jurisdição e só alcança papel: o procurador-geral da Califórnia, que em 30 de setembro intimou a OpenAI a entregar informação sobre incidentes de cibersegurança, e o Congresso podem exigir documentos e receber denúncia protegida, mas nenhum dos dois entra no laboratório para rodar o modelo. A outra tem acesso e não tem jurisdição: a METR e a Redwood entraram, investigaram e levaram o resultado ao Senado, mas só porque a empresa deixou e só até onde deixou. A ponte entre as duas metades é uma pessoa, e foi essa peça que eu não vi em "Seis dias úteis". O endereço do lado de fora não é só um prédio a construir. Precisa também de uma regra para quem caminha até ele.

Há uma razão honesta para essa via ser apertada, e não quero escondê-la. O canal para fora é também o canal de vazamento. Um laboratório que guarda pesos, arquitetura e vulnerabilidades tem motivo legítimo para controlar a saída de informação. Um pesquisador que entrega a terceiros mais do que o combinado pode estar fazendo exatamente o que a OpenAI acusa os três de ter feito. A tese pede menos do que canal livre: pede que a regra do canal seja escrita por alguém além da parte que tem o poder de demitir.

## O que fazer com isso, fora de um laboratório de fronteira

Quase ninguém que me lê dirige a OpenAI. Mas quase todo mundo que me lê contrata, ou vai contratar, alguém de fora para dizer se um sistema de IA dentro de casa está funcionando, seja auditoria, consultoria de risco ou avaliação de fornecedor. O desenho do acordo é o desenho padrão desses contratos, e os três buracos se repetem.

O primeiro é o acesso. Se o contrato do avaliador diz "parceria" e não diz o que ele pode consultar, ele vai ver o que lhe mostrarem, como os auditores do caso Hugging Face na segunda onda. Escreva no contrato, antes do incidente, a que o avaliador tem acesso, o que fica fora do escopo e quem decide isso, e o que acontece quando o acesso é negado.

O segundo é o destino do relatório. Se ele vai só para um comitê do seu conselho, o que você comprou é garantia para o conselho, o que pode ser exatamente o que você quer. Só não chame isso de transparência para cliente, regulador ou público.

O terceiro é a pessoa do meio. Toda avaliação externa tem um contato técnico do lado de dentro. Antes de nomear essa pessoa, escreva o que ela pode entregar, quem resolve a dúvida quando o pedido do avaliador passa do combinado, e que ela não responde sozinha por uma decisão que a empresa tomou ao contratar a avaliação. Se você é essa pessoa, peça isso por escrito. A proteção legal que existe, onde existe, cobre o seu relato ao Estado e ao seu chefe, e não a sua conversa com o auditor.

Em "Mesmo prompt, quatro comportamentos", o cordão que os agentes podiam puxar não tinha ninguém do outro lado. Aqui tem alguém do outro lado, e o acordo assinado na Casa Branca não diz quem protege a mão que puxa.

Se o próximo avaliador externo de um laboratório de fronteira precisar de um contato técnico do lado de dentro, como tem precisado, quem vai aceitar o cargo sabendo que a regra do que pode atravessar é escrita, aplicada e julgada pela mesma empresa que assinou o compromisso de ser auditada?

---

## Nota de verificação

**Lido na fonte primária.** O texto integral do acordo de 29 de setembro, na transcrição do American Presidency Project, da UC Santa Barbara; não encontrei o documento na página da Casa Branca, onde há apenas o decreto de mesma data, que é outro texto. O testemunho escrito de Chris Painter de 30 de setembro, na página da METR e no PDF, incluindo as notas 4, 5, 6 e 8. O texto sancionado do SB 53, seções 1107, 1107.1 e 1107.2 do Código do Trabalho da Califórnia. As seis páginas da carta de Josh Hawley a Sam Altman, de 9 de setembro. O texto do S.1792 e as páginas de tramitação e de coautores do Congress.gov, consultadas em 4 de outubro de 2026. O comunicado do procurador-geral da Califórnia de 1º de outubro sobre a intimação entregue na véspera. Os posts de Tomek Korbak (27/9) e de Keach Hagey (1/10) no X.

**Lido em parte.** As reportagens do WSJ e da Bloomberg de 1º de outubro: li o trecho aberto de cada uma, com os nomes, a declaração integral da OpenAI e a descrição do destinatário. Não li o texto completo de nenhuma das duas.

**Leitura de terceiros, atribuída.** A observação de que os avaliadores não têm proteção contra retaliação é de Abra Ganz e Karl Koch, em texto publicado pelo Institute for Law & AI. Os posts de Balesni e de Korbak críticos à OpenAI, de 10 e 11 de setembro, conheço pela AFP e não pelos originais. A fala de Daniel Kokotajlo sobre os seis dias está na transcrição da audiência publicada pela Tech Policy Press, que também registra Hawley na presidência. O sobrenome de "Ryan", no post de Korbak, vem da cobertura. A atribuição do tema "arquitetura de infraestrutura" à Bloomberg é do *The Hacker News*, e não a encontrei no trecho da Bloomberg que li; por isso não entra no corpo.

**Hipótese minha.** A comparação com a Sarbanes-Oxley (seções 301, 303 e 806, e o PCAOB) é leitura minha do texto da lei de 2002. Não encontrei quem a tenha feito a propósito do acordo, e ninguém ligado ao acordo cita a lei como modelo.

**O que não consegui saber.** A data efetiva das demissões, a identidade da organização terceira, o conteúdo do material, o que a intimação da Califórnia exige e com que base legal, e qualquer comentário da METR ou da Redwood sobre o caso.

**Traduções.** As citações do acordo, do testemunho, da carta e das leis são traduções minhas. Mantive em inglês os termos jurídicos sem equivalente estável.

**Onde a cobertura diverge da fonte.** Parte da cobertura do testemunho de Painter falou em cerca de dez mil agentes; o texto dele diz "dezenas de milhares", e é o número que uso. Li na Tech Times que os auditores seriam escolhidos pelas próprias empresas; o acordo não trata de escolha, e por isso a frase não entra. Sites menores escreveram que o material foi para a METR e a Redwood; a Ynet registra que não há indicação disso, e é o que se sustenta. Também li que nenhum dos três demitidos se manifestou publicamente; o que se sustenta é que nenhum comentou a demissão, porque Korbak descreveu a própria função em 27 de setembro.

---

## Referências

WHITE HOUSE. *White House Accord on Super Intelligence: Joint Commitment on Frontier Responsibilities*. Washington, 29 de setembro de 2026. Transcrição em The American Presidency Project, UC Santa Barbara.

PAINTER, Chris. Testimony before the U.S. Senate Subcommittee on Disaster Management, District of Columbia, and Census, hearing "Rogue AI: Securing the Homeland Against AI Agent Attacks". METR, 30 de setembro de 2026.

TECH POLICY PRESS. Senate Hearing on "Rogue AI: Securing the Homeland Against AI Agent Attacks". Transcrição. Outubro de 2026.

HAWLEY, Josh. Carta a Sam Altman sobre o incidente Hugging Face, com anexo de perguntas e pedidos de documentos. Senado dos Estados Unidos, 9 de setembro de 2026.

CALIFÓRNIA. Senate Bill 53, Transparency in Frontier Artificial Intelligence Act. Chapter 138, Statutes of 2025, sancionado em 29 de setembro de 2025. Labor Code §§ 1107–1107.2.

CALIFÓRNIA. Department of Justice. *As Part of Ongoing Investigation, Attorney General Bonta Serves Investigative Subpoena on OpenAI*. Comunicado, 1º de outubro de 2026.

GANZ, Abra; KOCH, Karl. *Whistleblower Protections in SB 53: Strengths, Limitations, and Open Questions*. Institute for Law & AI, junho de 2026.

ESTADOS UNIDOS. Congresso. S.1792, AI Whistleblower Protection Act, 119º Congresso. Apresentado por Chuck Grassley em 15 de maio de 2025. Congress.gov, consultado em 4 de outubro de 2026.

ESTADOS UNIDOS. Sarbanes-Oxley Act of 2002. Public Law 107-204, seções 101, 301, 303 e 806.

THE WALL STREET JOURNAL. OpenAI parts ways with researchers who allegedly shared confidential information. 1º de outubro de 2026.

BLOOMBERG. OpenAI parts ways with 3 workers over mishandling information. 1º de outubro de 2026.

AFP. OpenAI fires staff for sharing "sensitive information" with AI safety firm. 2 de outubro de 2026.

YNET. OpenAI fires 3 researchers over suspected leak of sensitive information. Outubro de 2026.

THE HACKER NEWS. OpenAI parts ways with three safety researchers. Outubro de 2026.

HAGEY, Keach. Post no X, 1º de outubro de 2026.

KORBAK, Tomek. Post no X, 27 de setembro de 2026.

---

*Este artigo integra a série VibeCoding em Contexto. O ASRS e a via lenta sem relógio estão em "Seis dias úteis e uma trilha sem relógio", que este texto reforça e corrige em um ponto. O cordão sem ninguém do outro lado está em "Mesmo prompt, quatro comportamentos".*
