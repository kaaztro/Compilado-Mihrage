################################################################
# MIHRAGE — PRÓLOGO + CAPÍTULO 1
# ==========================================
# Prólogo (2024): o coquetel do congresso, o instante em que o Daniel
# reconhece a Mirela. Eles se sentam num canto do saguão - e o resto
# do jogo é essa conversa.
#
# Capítulo 1 "Mihrela" (fases 1 a 6): ela conta 2014. A memória foi
# apagada à força, então ela RECONSTRÓI a lembrança enquanto fala, e
# cada módulo é a técnica que ela precisa pra trazer mais um pedaço.
# O Daniel, que estava lá, interrompe e completa.
#
#   Fase 0  (sem módulo)                escrita   (scene black)
#   Fase 1  tutorial_playing            escolha
#   Fase 2  tutorial_create             debug
#   Fase 3  tutorial_dialogue           debug  
#   Fase 4  tutorial_images             escolha   (checkpoint)
#   Fase 5  tutorial_simple_positions   escrita
#   Fase 6  tutorial_transitions        debug
################################################################


# ==========================================
# PRÓLOGO — o reencontro
# ==========================================
label prologo:

    $ vidas = VIDAS_INICIAIS
    $ checkpoint_atual = "prologo"
    $ nome_dela = "???"
    $ quando = "2024 · agora"

    show screen hud_vidas

    $ trilha("miragem", fade=3.0)

    scene black
    with dissolve

    centered "{size=+10}MIHRAGE{/size}"

    scene bg saguao tarde
    with dissolve

    $ ambiente("coquetel")

    "Congresso de automação e controle, fim do primeiro dia. Coquetel no saguão do hotel: taças de plástico, conversa de crachá."

    show mirela happy at right
    show daniel idle at left
    with dissolve

    m "...e aí o problema nem era o controlador, sabe? Era o encoder. Não sei como ninguém tinha olhado o encoder."

    "Ela parou no meio da frase. O homem do outro lado da mesa de café não tirava os olhos dela."

    m "Que foi? Tá branco."

    d "Mirela?"

    "O nome ficou pendurado no ar entre os dois, e passou muito mais tempo do que seria confortável antes de uma resposta."

    show mirela concerned at right

    $ nome_dela = "Mirela"

    m "...Faz dez anos que ninguém me chama assim."

    show daniel sad at left

    d "Você sumiu."

    m "Eu sei."

    d "Do nada. Sem tchau, sem falar nada. A gente ficou..."

    m "Eu sei, Daniel. Calma."

    "Ela olhou pro saguão cheio, pro relógio e depois pra porta. Depois de rodar um pouco pelo saguão, puxou duas cadeiras pro canto, longe da mesa do café."

    show mirela idle at right
    show daniel idle at left

    m "Senta. Se quiser que eu te conte o que aconteceu, vai ter que ouvir do começo. A não ser que esteja sem tempo, é claro."

    d "Do começo onde, Mirela?"

    m "Do pátio, a festa... Eu nem sei se ainda lembro direito, pra falar a verdade."

    sistema "O que você vai jogar a partir daqui é essa conversa."

    sistema "As falas em itálico são os dois conversando agora, nesse canto do saguão. O resto é a lembrança que eles estão montando."

    sistema "Pra montar cada lembrança, você usa o que aprender nos módulos do Ren'Py."

    jump cap1_checkpoint


# ==========================================
# CAPÍTULO 1 — Mihrela
# ==========================================
label cap1_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ ambiente(None)
    $ checkpoint_atual = "cap1_checkpoint"
    $ nome_dela = "Mirela"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 1 — Mihrela{/size}\nCEFET, 2014 · o que ela lembra"


# ---- FASE 0 — começando uma cena (escrita, sem módulo) ---------
# Antes de qualquer lembrança, o jogador aprende o comando que abre
# toda cena: scene. Ela "apaga" o saguão pra começar do escuro.
label cap1_fase0:

    $ quando = "2024 · agora"
    $ modulo_atual = "Antes dos módulos — Começando uma cena"

    scene bg saguao tarde
    show mirela idle at right
    show daniel idle at left
    with dissolve

    $ ambiente("coquetel")

    mh "Do começo, então. Mas eu não consigo lembrar de nada com esse saguão todo na minha frente."

    mh "Deixa eu fechar os olhos. Apagar tudo isso aqui e começar do escuro."

    call fase_escrita(
        "Apague o saguão inteiro e comece a lembrança do escuro. O fundo preto se chama black.",
        [
            "scene black",
            "re:scene black with \\w+",
            "re:scene black with Dissolve\\(\\d+(\\.\\d+)?\\)",
        ],
        "Ainda não. É a palavra scene seguida do nome do fundo: black.",
        "Antes: toda cena começa com scene. Ele limpa tudo o que está na tela, cenário e pessoas, e põe um fundo novo no lugar. Pro pátio da festa, por exemplo, seria: scene bg patio",
        "Comece a cena:")

    if not _return:
        jump game_over

    $ ambiente(None)

    scene black
    with Dissolve(2.0)

    $ quando = "2014 · lembrança dela"

    "Escuro. Um breu completo, a imagem do próprio vazio, como se o lugar imaginado não existisse mais."

    show screen reconstruindo

    mh "CEFET, 2014. É só isso que me vem à mente: o ano e o nome do lugar."

    mh "O resto eu apaguei da mente, ou pelo menos me fiz apagar. Ainda assim, com você aqui, não dá pra fingir que nada disso aconteceu."

    mh "Pra te contar, eu vou ter que montar tudo de novo, do zero. Não sei se ainda lembro como se monta."

    dh "Eu ajudo, Mih. Eu tava lá."

    hide screen reconstruindo


# ---- FASE 1 — tutorial_playing (múltipla escolha) ---------------
label cap1_fase1:

    mh "Primeiro as regras. Numa conversa dessas, o que é que dá pra fazer?"

    menu:
        sistema "O módulo 1 mostra os controles do jogo: salvar, carregar, pular, voltar. Quer ver?"

        "Quero ver os controles":
            call modulo("tutorial_playing", 1, "Jogando")

        "Já sei jogar, pode pular":
            $ modulo_atual = "Módulo 1 — Jogando"
            sistema "Resumo: clique ou Enter avança; a roda do mouse pra cima volta pras falas anteriores (o rollback); botão direito abre o menu, com salvar e carregar."

    call fase_escolha(
        "De tudo isso, uma coisa ela vai querer o tempo inteiro: voltar pro momento exato de uma fala e ver a cena de novo, do jeito que estava. Qual recurso faz isso?",
        [
            ("Rollback - volta pras falas anteriores", True,
             "Isso. O rollback volta a cena inteira pro momento daquela fala. Só não desfaz uma falha: o que deu errado fica registrado."),
            ("Histórico - mostra o texto que já passou", False,
             "Quase. O histórico mostra as falas escritas, mas a cena continua onde está. Quem volta no tempo, com imagem e tudo, é o rollback."),
            ("Skip - pula o texto que já foi lido", False,
             "Não. Pular só acelera o que já foi dito; não traz nada de volta."),
            ("Auto - avança sozinho sem clique", False,
             "Não. Isso só tira a mão dela do volante - não volta pra lugar nenhum."),
        ])

    if not _return:
        jump game_over

    call agora("sad", "idle")

    mh "Dá pra voltar e tentar ouvir de novo o que a gente diz. Apagar o que já foi dito é impossível."
    dh "Isso vale pra muita coisa."


# ---- FASE 2 — tutorial_create (debug) --------------------------
label cap1_fase2:

    mh "Antes de lembrar de qualquer coisa, eu preciso de um lugar onde tudo isso caiba. Um... um..."

    mh "...Como é que chama? É como se faltasse um espaço da minha própria memória."

    call modulo("tutorial_create", 2, "Criando um projeto")

    call agora("sad", "sad")

    dh "Um projeto. Um lugar vazio, pra caber o resto."
    mh "...Isso. Um projeto. Obrigada."
    dh "Mih, tá tudo bem?"
    mh "Tá sim. Vamos ao ponto de partida - o lugar onde a história começou a rodar."
    dh "E onde começou?"
    show mirela idle at right
    mh "Onde tudo começa. No start."

    call fase_debug(
        "PONTO DE PARTIDA — algo está errado",
        [
            "label start",
            "    \"CEFET, 2014.\"",
        ],
        "A primeira linha está incompleta. Escreve ela do jeito certo.",
        ["label start:"],
        "Quase. O nome está certo, falta só o dois-pontos no fim da linha.",
        "Antes: um bloco de roteiro sempre abre com a palavra label, o nome dele, e dois-pontos no fim da linha. É o dois-pontos que diz 'tudo que estiver indentado embaixo pertence a mim'. Um bloco chamado memoria ficaria: label memoria:")

    if not _return:
        jump game_over

    show mirela happy at right
    mh "Acho que assim a gente acaba chegando em algum lugar."

    $ ambiente(None)

    scene black
    with dissolve

    $ quando = "2014 · lembrança dela"


# ---- FASE 3 — tutorial_dialogue (debug) ----------------------
label cap1_fase3:

    show screen reconstruindo

    mh "A primeira coisa que volta pra mim não é nenhuma imagem. É uma voz."

    mh "Uma frase sozinha, sem ninguém dizendo, como se fosse a cena contando a si mesma."

    hide screen reconstruindo

    "Tá escuro demais aqui dentro."

    show screen reconstruindo

    mh "Essa era eu, naquela noite."

    mh "Agora ela, a Lucy."

    mh "Minha dupla desde o primeiro ano. Sentava do meu lado em todas as aulas, copiava meu caderno e me devolvia com aqueles desenhos na margem. Disso eu lembro."

    mh "Foi ela que inventou o \"Mih\"."

    mh "E foi a única pessoa que soube o que eu ia te falar lá em cima."

    dh "...A Lucy sabia?"

    mh "Disso a gente fala depois. Deixa eu remontar ela primeiro na minha memória."

    mh "Ela merece mais que uma frase solta da minha parte."

    hide screen reconstruindo

    call modulo("tutorial_dialogue", 3, "Escrevendo diálogo")

    call fase_debug(
        "A VOZ DA LUCY — falta o nome",
        [
            "define l = Character(____)",
            "",
            "l \"Cadê você, Mih?\"",
        ],
        "Falta o que vai no lugar do ____: o nome dela, Lucy, entre aspas. Escreve só isso, ou a linha inteira.",
        [
            "'Lucy'",
            "_('Lucy')",
            "l = Character('Lucy')",
            "l = Character(_('Lucy'))",
            "re:l=Character\\((_\\()?'Lucy'(\\))?,.+\\)",
        ],
        "Ainda não. É o nome Lucy entre aspas, com L maiúsculo, do jeito que vai aparecer na caixa de diálogo.",
        "Antes: definir uma personagem é escrever define, um apelido curto, o sinal de igual, e Character com o nome entre aspas. Maiúscula e minúscula contam. Pra uma personagem chamada Ana, com apelido a, ficaria: define a = Character('Ana')")

    if not _return:
        jump game_over

    l "Mih? Cadê você? Vem, a festa já começou."

    show screen reconstruindo
    mh "A voz dela. Eu sinto falta daquela voz."
    dh "\"Mih.\" Fazia anos que eu não ouvia ninguém te chamar assim."
    mh "Só ela me chamava assim. Pra todo o resto do CEFET eu era Mirela."
    hide screen reconstruindo


# ---- FASE 4 — tutorial_images (escolha) ------------------------
label cap1_fase4:

    $ checkpoint_atual = "cap1_fase4"
    $ quando = "2014 · lembrança dela"

    scene black

    show screen reconstruindo
    mh "Eu lembro da minha voz, eu lembro da Lucy... Tá faltando o lugar, e falta o rosto."
    hide screen reconstruindo

    call modulo("tutorial_images", 4, "Imagens")

    call fase_escolha(
        "A Lucy precisa aparecer de frente, bem no meio da tela, com o pátio da festa atrás dela. Qual sequência faz isso?",
        [
            ("scene bg patio  →  show lucy happy at center", True,
             "Isso. O scene troca o escuro pelo pátio; o show põe a Lucy por cima, e o at center deixa ela no meio."),
            ("show lucy happy at center  →  scene bg patio", False,
             "Não. O scene limpa tudo o que estava na tela: a Lucy some junto, e sobra só o pátio vazio."),
            ("scene bg patio  →  show lucy happy at left", False,
             "Não. O at left põe ela no canto esquerdo, não no meio da tela."),
            ("show bg patio  →  show lucy happy at center", False,
             "Não. O show não limpa o que já estava na tela: o pátio entra por cima do escuro em vez de começar uma cena nova."),
        ],
        "Antes: o scene limpa a tela e põe o fundo; o show põe alguém por cima dele. Quem diz onde a pessoa fica é o at: left, center ou right.")

    if not _return:
        jump game_over

    scene bg patio at memoria_surge

    $ ambiente("festa")

    "A festa... Aquela festa boba no meio do semestre, com a caixa de som alta demais pro tamanho do pátio, não que alguém ligasse pra isso."

    show lucy happy at center, memoria_surge

    pause 1.5

    show lucy mad

    l "Demorou, hein. Achei que tinha me largado sozinha aqui."

    mh "Ela vivia dizendo isso, que um dia eu ia largar ela sozinha. Não é que aconteceu?"

    dh "..."

    show lucy idle

    "O rosto da Lucy. Inteiro, do jeito que era."

    with vpunch

    "Atrás dela, no muro, um risco antigo de tinta que já estava ali muito antes de a turma delas entrar no CEFET."

    show daniel sombra at right, silhueta_pessoa
    with dissolve

    d "Vocês duas estão cochichando de novo. Um dia eu ainda descubro o que é tão engraçado."

    show lucy happy

    l "Nesse dia a gente vai parar de rir, Daniel."

    show screen reconstruindo

    mh "Por que eu não consigo remontar você?"

    mh "Sei o tamanho, sei de que lado você ficava, sei o jeito de falar. Mas... o rosto de 2014 não vem. Você mudou muito."

    mh "Você tá bem aqui na minha frente, e o único rosto que vem é o de agora."

    dh "É até melhor assim, hah. Eu tinha um bigodinho horrível."

    mh "Fica o contorno, então. É melhor do que nada."

    hide screen reconstruindo


# ---- FASE 5 — tutorial_simple_positions (escrita) --------------
label cap1_fase5:

    show screen reconstruindo
    mh "E... não era assim que a gente ficava. A Lucy no meio, eu em lugar nenhum. Tem algo errado."
    hide screen reconstruindo

    call modulo("tutorial_simple_positions", 5, "Posições simples")

    scene bg patio
    show lucy idle at center
    show daniel sombra at right, silhueta_pessoa
    with Dissolve(1.0)

    $ ambiente("festa")

    "A Lucy no meio, o contorno do Daniel do lado direito. E o lado esquerdo vazio."

    call fase_escrita(
        "Põe ela em cena à esquerda: a imagem é mirela happy, a posição é left.",
        [
            "show mirela happy at left",
            "re:show mirela happy at left with \\w+",
        ],
        "Ainda não. A ordem é: show, o nome da imagem com as duas partes, a palavra at, e o nome da posição.",
        "Antes: pra colocar uma imagem numa posição, escreve show, o nome da imagem, a palavra at, e a posição. As prontas são left, center e right. Por exemplo: show lucy mad at center",
        "Posicione a Mirela:")

    if not _return:
        jump game_over

    show mirela happy at left, memoria_surge

    "Os três nos lugares de sempre, quase por costume: ela de um lado, a Lucy no meio, o Daniel do outro."

    show screen reconstruindo

    mh "Aqui. Era exatamente aqui que eu ficava."

    mh "Não é engraçado como essas coisas não mudam? Se eu trocasse você por outra pessoa na minha memória, ela continuaria no mesmo lugar que você."

    hide screen reconstruindo

    show mirela vhappy at left

    "A noite foi esfriando. A caixa de som baixou sozinha, e o pátio começou a esvaziar."

    m "Vem comigo. Eu quero te mostrar uma coisa lá em cima."

    d "Lá em cima? Agora? Tá bom, mas se eu cair rolando a culpa é sua, viu."

    l "Vão lá. Eu fico aqui vendo as bolsas de vocês, como sempre."

    show lucy happy

    "A Lucy piscou pra ela quando o Daniel virou de costas. Só pra ela."

    dh "Ela piscou pra você?"

    mh "Você não perdia uma, né. A não ser que a sua vida dependesse disso; aí você perdia todas."

    hide lucy
    with dissolve

    dh "Eu lembro disso. Lembro de achar que você ia me mostrar o vira-lata que morava lá em cima."

    mh "O Parafuso?"

    dh "O Parafuso! Meu Deus. Quanto tempo que eu não vejo ele."


# ---- FASE 6 — tutorial_transitions (debug) ---------------------
label cap1_fase6:

    show screen reconstruindo

    mh "Agora o morro. É aqui que eu acho que a memória vai falhar."

    mh "Do jeito que eu penso, um lugar vira o outro de estalo, sem nada no meio... Mas não foi assim. No caminho teve aquela subida, o tempo que a gente levou. Você sofrendo com o esforço."

    dh "Vamos esquecer essa última parte, tudo bem?"

    hide screen reconstruindo

    call modulo("tutorial_transitions", 6, "Transições")

    call fase_debug(
        "A SUBIDA — o corte está seco demais",
        [
            "scene bg trilha",
            "show mirela happy",
            "with",
        ],
        "A última linha está pela metade. Escreve ela inteira, usando a dissolve.",
        [
            "with dissolve",
            "re:with Dissolve\\(\\d+(\\.\\d+)?\\)",
        ],
        "Ainda não. É a palavra with seguida do nome da transição, nada mais.",
        "Antes: depois de trocar a cena, uma linha com a palavra with e o nome de uma transição faz a passagem ser suave em vez de um corte seco. Com a fade, por exemplo, ficaria: with fade")

    if not _return:
        jump game_over

    # --- A subida ---
    scene bg trilha
    show mirela happy at center
    show daniel sombra at right, silhueta_pessoa
    with slowdissolve

    $ ambiente("morro")

    "O barulho da festa foi ficando pra trás, abafado pelo mato. Primeiro a música, depois as vozes. Depois mais nada."

    d "Se tiver cobra aqui, eu volto rolando."

    show mirela idle

    "Ela riu. Alto demais, nervosa demais. Ele não percebeu."

    mh "Eu contei os passos. Cento e oitenta e dois. Pra não pensar no que eu ia dizer lá em cima."

    # --- O topo ---
    scene bg morro
    show daniel sombra at right, silhueta_pessoa
    show mirela idle at center
    with Dissolve(2.0)

    "Lá de cima, a cidade inteira cabia na palma da mão. As luzes piscando lá embaixo, o vento frio no rosto."

    d "Tá. Valeu a subida. Admito."

    show mirela concerned at afastada

    "Ela deu dois passos à frente e ficou de costas pra ele, olhando as luzes."

    m "Daniel."

    d "Oi?"

    m "Eu preciso te falar uma coisa.{w=0.8} Faz tempo que eu..."

    # A revelação: o vento para, a música some, a lembrança congela.
    $ ambiente(None)
    $ trilha(None, fade=1.5)

    scene cg morro
    with Dissolve(1.5)

    "{cps=30}Ela guardava uma frase na cabeça fazia semanas. Tinha ensaiado no ônibus, no banho, na fila do bandejão. Tinha ensaiado com a Lucy.{/cps}"

    show screen reconstruindo

    mh "É aqui. Eu montei o lugar, montei a noite, o vento, você do meu lado. Remontei tudo."

    mh "Só falta a fala. Escreve você."

    hide screen reconstruindo

    # Uma "fase" sem resposta certa: o jogador tenta escrever a fala, e a
    # lembrança recusa. Não tira vida.
    $ _fala = renpy.input("A FALA DO MORRO\n\nm \"____\"\n\nEscreva o que ela disse:", length=120, screen="entrada_codigo").strip() or "..."

    show cg morro at memoria_trava

    m "{cps=12}[_fala!q]{/cps}{w=0.5}{nw}"

    show cg morro at memoria_trava
    with vpunch

    sistema "ERRO: essa linha não existe na lembrança."

    sistema "Dá pra montar um lugar, uma noite, uma pessoa. Não dá pra escrever uma fala que ninguém disse."

    mh "É como se fosse uma memória falsa. Eu tento escrever essa fala faz dez anos."

    # --- A desistência ---
    scene bg morro
    show daniel sombra at right, silhueta_pessoa
    show mirela concerned at afastada
    with Dissolve(1.2)

    d "Mirela? Faz tempo que você o quê?"

    "Ela ficou calada. Tempo demais."

    show mirela sad

    m "{cps=20}...Nada.{w=0.6} Deixa pra lá.{/cps}"

    d "Como assim, nada? A gente subiu até aqui só pra isso?"

    m "Foi bobagem minha, nada com que você precise se preocupar. Vamos descer, a Lucy tá sozinha com as bolsas."

    "Ele ainda esperou um pouco. Ela continuou olhando a cidade."

    # --- A descida ---
    scene bg patio
    show lucy idle at center
    with Dissolve(1.5)

    $ ambiente("festa", volume=0.35)

    "Lá embaixo, a festa continuava como se nada tivesse acontecido. E, pra todo mundo ali, nada tinha."

    show lucy happy

    l "E aí?"

    show mirela sad at left
    show daniel sombra at right, silhueta_pessoa
    with dissolve

    "A Mirela só balançou a cabeça. Uma vez, curto."

    show lucy sad

    l "...Ah, Mih."

    "A Lucy apertou a mão dela e não perguntou mais nada."

    dh "Eu vi isso. Achei que era coisa de vocês duas."

    $ ambiente(None)

    scene black
    with Dissolve(2.5)

    "{cps=26}Essa foi a última vez que alguém do CEFET viu a Mirela.{/cps}"

    "{cps=26}Na segunda, a cadeira dela ficou vazia.{w=0.8} Na terça também.{w=0.8} Na outra semana, ninguém guardava mais o lugar.{/cps}"

    # --- De volta ao saguão ---
    $ trilha("miragem", fade=4.0)
    $ quando = "2024 · agora"

    scene bg saguao tarde
    show mirela sad at right
    show daniel sad at left
    with Dissolve(2.0)

    $ ambiente("coquetel")

    dh "Dez anos. Eu passei dez anos tentando adivinhar o que você ia me falar naquela noite."

    dh "Fala agora, então."

    "Ela abriu a boca. Fechou. Baixou os olhos pro crachá pendurado no pescoço, como se ele pudesse responder por ela."

    mh "Eu ainda chego lá, Daniel. Prometo."

    mh "Daqui pra frente eu não sei nada do que aconteceu lá no CEFET. Afinal, eu não tava lá."

    dh "Foi tanta coisa, Mirela... Você não imagina."

    mh "Me conta você, então. O que aconteceu depois que eu sumi?"

    centered "{size=+8}Fim do Capítulo 1{/size}"

    jump cap2_checkpoint
