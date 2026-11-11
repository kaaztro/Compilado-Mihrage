################################################################
# MIHRAGE — CAPÍTULO 2 "Mihrage"
# 2014 · o que ele viveu — fases 7 a 13
# ==========================================
# Ainda no canto do saguão, em 2024: agora é o Daniel quem conta.
# Ela ouve pela primeira vez o que aconteceu do lado de cá depois do
# sumiço, e interrompe (falas em itálico).
#
#   Fase 7   tutorial_music      debug
#   Fase 8   tutorial_menus      escolha
#   Fase 9   tutorial_input      escrita
#   Fase 10  tutorial_video      escolha   (checkpoint)
#   Fase 11  tutorial_nvlmode    debug
#   Fase 12  director            escolha   (a cadeira vazia)
#   Fase 13  distribute          escolha   (lacrar a fita)
################################################################

label cap2_checkpoint:

    $ vidas = VIDAS_INICIAIS
    $ ambiente(None)
    $ checkpoint_atual = "cap2_checkpoint"
    $ nome_dela = "Mirela"

    show screen hud_vidas

    scene black
    with dissolve

    centered "{size=+10}CAPÍTULO 2 — Mihrage{/size}\n2014 · o que ele viveu"

    $ quando = "2014 · lembrança dele"

    scene bg sala_vazia
    with dissolve

    $ ambiente("sala")

    dh "Três semanas. Foi o tempo até alguém reparar de verdade."

    "Três semanas depois, a cadeira dela continuava vazia, e ninguém no CEFET sabia dizer desde quando."

    d "Cadê a Mirela? Alguém sabe alguma coisa?"

    "E como ninguém sabia, cada um inventou a sua: que fugiu de casa, que largou o curso, que arranjou alguém em outra cidade e sumiu sem avisar."

    "Piada é o que as pessoas fazem quando não têm a história de verdade."

    mh "Eu imaginava. Eu imaginava cada uma dessas."


# ---- FASE 7 — tutorial_music (debug) -------------------------
label cap2_fase7:

    scene bg quarto
    show daniel idle at center
    with dissolve

    $ ambiente("quarto")

    "O violão continuava encostado no canto do quarto, com a mesma corda desafinada de sempre."

    d "Ela pediu uma música. Eu enrolei, falei que era difícil, que eu tinha acabado de começar."

    d "Naquele dia eu tava tocando Hey Jude. De todas as músicas do mundo, Hey Jude."

    mh "Você tocava Hey Jude errado."

    dh "Eu tocava tudo errado. Mas aquela eu tocava errado com vontade."

    # Silêncio antes da fase: a música dele é que vai voltar a tocar.
    $ trilha(None, fade=2.0)

    call modulo("tutorial_music", 7, "Música e som")

    scene bg quarto
    show daniel idle at center
    with Dissolve(1.0)

    $ ambiente("quarto")

    "Ele apertou o play no computador velho pra tocar a base por cima. Nada. Só o chiado da caixa de som."

    call fase_debug(
        "O QUARTO — a música não toca",
        [
            "scene bg quarto",
            "ply music \"hey_jude.ogg\"",
        ],
        "Tem um erro de digitação no comando da segunda linha. Escreve ela certa.",
        [
            "play",
            "re:play music '(audio/)?hey_jude(\\.ogg)?'( fadein \\d+(\\.\\d+)?)?",
        ],
        "Ainda não. O comando que toca música se escreve p-l-a-y. O resto da linha fica igual.",
        "Antes: pra tocar uma música em loop, a linha é play, o canal music e o nome do arquivo entre aspas. Por exemplo: play music 'tower_clock.ogg'")

    if not _return:
        jump game_over

    scene bg quarto
    show daniel idle at center

    $ trilha("hey_jude", fade=2.0)

    "A base começou a tocar, e ele tocou por cima, errado do mesmo jeito de sempre."

    d "Se ela não vai me ouvir tocar, pelo menos vai existir uma música que é dela."


# ---- FASE 8 — tutorial_menus (escolha) -------------------------
label cap2_fase8:

    # A música dele fica pra trás; volta o tema do jogo.
    $ trilha("miragem", fade=4.0)

    "A lista de contatos tinha três nomes que talvez soubessem de alguma coisa. O cartão do orelhão tinha crédito pra uma ligação."

    dh "Uma ligação. Eu fiquei uma tarde inteira decidindo pra quem."

    call modulo("tutorial_menus", 8, "Menus e escolhas")

    scene bg orelhao
    show daniel idle at center
    with Dissolve(1.0)

    $ ambiente("rua")

    "O orelhão da esquina do CEFET, o cartão na mão, três nomes anotados no caderno."

    call fase_escolha(
        "Pra cada nome do caderno virar uma opção que ele pode apertar, como fica a linha de cada opção dentro do menu?",
        [
            ("\"Pra Lucy.\":", True,
             "Isso. O texto da opção entre aspas e dois-pontos no fim. Embaixo dela vem o que acontece se ele escolher."),
            ("\"Pra Lucy.\"", False,
             "Não. Sem os dois-pontos, o Ren'Py lê isso como uma fala solta, não como uma opção que dá pra apertar."),
            ("Pra Lucy:", False,
             "Não. Sem as aspas, o Ren'Py não sabe onde começa e onde termina o texto da opção."),
        ])

    if not _return:
        jump game_over

    scene bg orelhao
    show daniel idle at center

    menu:
        "Pra quem ele liga?"

        "Pra secretaria do CEFET.":
            $ primeira_ligacao = "escola"
            d "Alô, boa tarde. Eu queria saber de uma aluna do técnico de automação."
            "A moça da secretaria pediu pra ele esperar. Voltou dois minutos depois, com outra voz."
            "\"Não podemos passar informações sobre alunos.\""
            mh "Eles sabiam."

        "Pra casa dela.":
            $ primeira_ligacao = "casa"
            d "Alô? ...Alô?"
            "A ligação caiu antes da segunda palavra. Nas outras vezes, deu ocupado."
            mh "..."

        "Pra Lucy.":
            $ primeira_ligacao = "lucy"
            l "Ai, Daniel, deixa isso pra lá. Ela sumiu porque quis sumir."
            l "Ela vivia dizendo que um dia ia embora. Foi. Pronto."
            "E desligou antes que ele respondesse."
            mh "A Lucy disse isso?"
            dh "Com raiva. A voz tremendo. Na hora eu achei que era raiva de você."
            mh "Era medo. Ela tinha medo disso desde o primeiro ano."

    dh "Foi a única que eu consegui fazer."


# ---- FASE 9 — tutorial_input (escrita) -------------------------
label cap2_fase9:

    scene bg laboratorio
    show daniel idle at center
    with dissolve

    $ ambiente("laboratorio")

    "Sobrou a internet do laboratório: quinze minutos por aluno e uma caixa de busca piscando."

    dh "Eu digitei seu nome. Foi a única coisa que eu sabia fazer."

    call modulo("tutorial_input", 9, "Entrada de texto")

    # O nome digitado dentro do módulo (a pergunta "Quem ele estava
    # procurando?") é o que vai pra caixa de busca.
    python:
        busca = (store.name if isinstance(getattr(store, "name", None), str) else "") or "Mirela"
        busca = busca.strip().replace("{", "{{") or "Mirela"

    scene bg laboratorio
    show daniel idle at center
    with Dissolve(1.0)

    $ ambiente("laboratorio")

    "O que ele digitou ficou guardado numa variável chamada busca. Agora a tela precisa mostrar o que foi buscado."

    call fase_escrita(
        "Escreve a variável busca do jeito que ela entra no meio de uma fala, pra tela mostrar o que ele digitou.",
        [
            "[busca]",
            "re:.*\\[busca\\].*",
        ],
        "Ainda não. É o nome da variável entre colchetes, sem espaço: abre colchete, busca, fecha colchete.",
        "Antes: pra mostrar o valor de uma variável no meio de um texto, escreve o nome dela entre colchetes. Uma variável chamada cidade apareceria assim: [cidade]",
        "Mostre a busca:")

    if not _return:
        jump game_over

    scene bg laboratorio
    show daniel idle at center

    "Resultados para \"[busca]\": duas páginas de nomes parecidos. Nenhum deles ela."

    d "[busca]. Só isso. Nem sobrenome completo eu sabia direito."

    mh "Não ia achar. Não tinha nada meu em lugar nenhum. Nem foto deixaram."


# ---- FASE 10 — tutorial_video (escolha) ------------------------
label cap2_fase10:

    $ checkpoint_atual = "cap2_fase10"
    $ quando = "2014 · lembrança dele"

    scene bg quarto
    show daniel idle at center

    $ ambiente("quarto")

    "No fundo da gaveta, uma fita que alguém tinha gravado na festa de junho."

    dh "Eu nem lembrava que tinha isso. Achei procurando outra coisa."

    call modulo("tutorial_video", 10, "Vídeo")

    call fase_escolha(
        "Ele quer que a gravação tome a tela inteira e só devolva o controle quando acabar. O que serve?",
        [
            ("Uma cutscene de vídeo, que roda o arquivo e depois continua a história", True,
             "Isso. O vídeo ocupa tudo, roda até o fim, e a cena segue de onde parou."),
            ("Uma imagem parada do primeiro quadro", False,
             "Não. Uma foto não devolve a voz dela nem o movimento - e é justamente isso que ele foi procurar ali."),
            ("Um som tocando no canal de música", False,
             "Não. O som sozinho deixaria a tela vazia; ele quer ver a festa de novo."),
        ])

    if not _return:
        jump game_over

    scene bg quarto
    show daniel idle at center

    "Doze segundos de câmera tremida: a Lucy rindo perto da caixa de som, ele de costas, e num canto do quadro, por menos de um segundo, ela."

    show daniel sad at center

    d "É só isso que sobrou. Doze segundos, e ela aparece em um."

    mh "Eu nunca vi essa gravação."

    dh "Eu tirei um print do segundo em que você aparece. Tá no meu celular até hoje."


# ---- FASE 11 — tutorial_nvlmode (debug) ------------------------
label cap2_fase11:

    "A carta da direção chegou num envelope pardo, com o timbre do colégio no canto."

    call modulo("tutorial_nvlmode", 11, "Modo NVL")

    call fase_debug(
        "O COMUNICADO — a tela não limpa entre um bloco e outro",
        [
            "nvl",
            "\"A direção informa que entrou em contato com os responsáveis.\"",
        ],
        "A primeira linha está incompleta. Escreve ela inteira.",
        [
            "nvl clear",
        ],
        "Ainda não. É a palavra nvl seguida do comando que esvazia a tela.",
        "Antes: no modo de tela cheia, o texto vai se acumulando um embaixo do outro até alguém mandar limpar. Quem limpa é a palavra nvl seguida de clear.")

    if not _return:
        jump game_over

    scene cg carta
    with dissolve

    "A direção informa que entrou em contato com os responsáveis pela aluna."

    "A família solicitou que não sejam feitas novas tentativas de contato."

    "A aluna foi desligada do colégio a pedido dos responsáveis."

    "Não há mais informações a prestar."

    d "\"Não há mais informações a prestar.\""

    scene bg quarto
    show daniel sad at center
    with dissolve

    d "E acabou aí. Eu não tinha mais pra onde ligar, não tinha mais quem perguntar."

    mh "\"A pedido dos responsáveis.\" Que jeito educado de escrever aquilo."


# ---- FASE 12 — director (escolha) ------------------------------
label cap2_fase12:

    $ quando = "2014 · lembrança dele"

    scene bg sala_vazia
    show daniel sad at left
    show lucy sad at right
    with dissolve

    $ ambiente("sala")

    "A cadeira dela continuava no mesmo lugar: terceira fileira, do lado da janela. A Lucy sentava do lado."

    "Ele passava a aula inteira olhando pra ela. Pra cadeira."

    "Na terceira semana, a Lucy juntou o material e foi pro fundo da sala."

    hide lucy
    with moveoutright

    "Na quarta, o Rafael chegou atrasado, viu a cadeira livre e sentou. Ninguém falou nada. Tinha espaço."

    show colega at right
    with dissolve

    "Na quinta, o professor fez a chamada inteira e não leu o nome dela."

    dh "Ninguém tirou você de lá. Foram só colocando gente no lugar, um de cada vez."

    mh "Como se eu nunca tivesse sentado ali."

    call modulo("director", 12, "Ferramentas e o diretor")

    call fase_escolha(
        "Ninguém anunciou nada: a Lucy saiu do lugar, um colega entrou no vazio, um nome sumiu da chamada. No Ren'Py, o que decide quem está em cena - e é o que o diretor interativo escreve por você?",
        [
            ("show pra pôr alguém em cena e hide pra tirar, uma linha de cada vez", True,
             "Isso. Uma linha de show, uma de hide, e o lugar dela vai sendo ocupado sem que ninguém precise dizer nada."),
            ("Mudar a cor do nome dos personagens", False,
             "Não. A cor muda como alguém fala, não se a pessoa ainda está na sala."),
            ("Um menu de escolhas", False,
             "Não. O menu pergunta ao jogador. Aqui ninguém perguntou nada a ninguém."),
        ])

    if not _return:
        jump game_over

    scene bg sala_vazia
    show daniel sad at left
    show colega at right
    with dissolve

    "Em novembro, a carteira foi pra outra sala, porque faltava uma lá."

    hide colega
    with dissolve

    "Ficou só o espaço da janela."

    scene bg patio

    show lucy idle at right
    show daniel idle at left
    with dissolve

    $ ambiente("patio_dia")

    "No intervalo, a Lucy explicou por que tinha mudado de lugar: não conseguia sentar do lado da cadeira vazia."

    l "Você ainda pensa nisso, né?"

    show daniel sad at left

    d "Todo dia um pouco menos."

    show lucy sad at right

    l "Eu também penso. Ela era minha dupla, Daniel. Ela me contava tudo."

    l "...Quase tudo."

    d "Quase?"

    l "Esquece. Não é meu pra contar."

    show lucy idle at right

    l "Mas tá funcionando, né? Todo dia um pouco menos."

    "Eles começaram a namorar em outubro. No começo era só pra ter com quem sentir falta da mesma pessoa."

    mh "Você e a Lucy?"

    dh "Três anos. Acho que a gente se juntou pra sentir sua falta junto. Quando isso passou, acabou. Acabou bem."

    mh "Que bom. ...Sério. Que bom."


# ---- FASE 13 — distribute (escolha) ----------------------------
label cap2_fase13:

    scene bg quarto
    show daniel idle at center

    hide lucy
    with dissolve

    "A música ficou pronta num sábado de madrugada, com a mesma corda desafinada de sempre."

    "Gravou no gravador velho do pai, numa fita que já tinha sido de outra coisa. Era a única cópia."

    dh "Fita estica, mofa, apaga. Se eu não fechasse aquilo, em um ano não ia sobrar nem o chiado."

    "Antes de passar pro computador e lacrar o arquivo, ele botou o fone e ouviu a fita inteira uma última vez, procurando cada estalo e cada ruído."

    call modulo("distribute", 13, "Distribuindo o jogo")

    call fase_escolha(
        "Antes de lacrar o pacote, ele ouve a fita uma última vez caçando ruído. No Ren'Py, o que faz esse papel antes de gerar as distribuições?",
        [
            ("O Lint, que confere o jogo inteiro e aponta o que pode estar errado", True,
             "Isso. Primeiro o Lint, como quem escuta a fita até o fim; só depois o Build Distributions lacra o pacote."),
            ("O Build Distributions direto - se tiver erro, alguém acha depois", False,
             "Não. Isso é lacrar a fita sem ouvir: o estalo fica gravado pra sempre, e quem acha é quem escuta depois."),
            ("O autoreload com Shift+R", False,
             "Não. O autoreload recarrega o jogo enquanto você edita, como regravar por cima. Ele não confere nada."),
        ],
        "Antes: antes de gerar as versões pra Windows, Linux e Mac, o Ren'Py tem uma ferramenta que confere o jogo inteiro e lista o que pode estar errado. O módulo mostrou o nome dela logo no começo.")

    if not _return:
        jump game_over

    scene bg quarto
    show daniel idle at center

    "Nenhum estalo. Ele passou a música pro computador, salvou em três lugares diferentes e escreveu na etiqueta da fita a data e o nome dela."

    scene bg quarto
    show daniel idle at center

    $ trilha("miragem", fade=3.0)

    "Aí ele soltou no mundo: postou num site de música, numa conta com zero seguidores. No título, só o nome dela."

    show daniel happy at center

    d "Pronto. Existe."

    d "Não sei onde ela tá, não sei se um dia ela escuta. Mas agora existe uma música que é dela."

    mh "Você postou?"

    dh "Quarenta e três visualizações. Umas trinta são minhas."

    mh "...E depois?"

    $ quando = "2024 · agora"

    scene bg saguao anoitecer
    show mirela idle at right
    show daniel idle at left
    with dissolve

    $ ambiente("coquetel")

    "Lá fora tinha começado a escurecer. O coquetel já estava pela metade."

    dh "Depois foram dez anos. E hoje."

    scene black
    with dissolve

    centered "{size=+8}Fim do Capítulo 2{/size}"

    jump cap3_checkpoint
