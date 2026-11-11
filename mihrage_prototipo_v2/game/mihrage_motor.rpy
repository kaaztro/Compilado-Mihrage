################################################################
# MIHRAGE — MOTOR
# ==========================================
# Personagens, imagens, estado de jogo (vidas/checkpoints), HUD,
# caderno, a moldura dos módulos e as três dinâmicas de fase.
# Nada de narrativa aqui: a história fica em mihrage_cap1.rpy,
# mihrage_cap2.rpy e mihrage_cap3.rpy.
#
# MOLDURA DA HISTÓRIA
# O jogo inteiro é a conversa de Daniel e Mirela no reencontro, em
# 2024, no coquetel de um congresso. O prólogo mostra o momento em que
# ele a reconhece; os capítulos 1 e 2 são os dois montando o passado
# juntos; o capítulo 3 alcança o prólogo e segue até o fim da conversa.
#
#   fala normal   -> a cena sendo montada (2014, ou hoje cedo)
#   fala itálica  -> os dois conversando AGORA, no canto do saguão
################################################################


# ==========================================
# 1. PERSONAGENS
# ==========================================

# Quem apresenta os módulos (o tutorial oficial fala por `e`) é a
# própria Mirela de agora, explicando enquanto monta a lembrança.
# O nome acompanha o dela (Mirela -> Mihlena no fim).
define e = Character("[nome_dela]", color="#c8ffc8")

# `l` (Lucy) já vem definida em tutorial_quickstart.rpy.

# O nome dela muda ao longo do jogo ("???" -> "Mirela" -> "Mihlena").
# Fica numa variável `default` pra entrar no save e no rollback.
default nome_dela = "Mirela"
define NOME_NOVO = "Mihlena"

define m = Character("[nome_dela]", color="#c8ffc8")
define d = Character("Daniel", color="#a3c9ff")

# As vozes de AGORA: os dois contando um pro outro, em itálico.
define mh = Character("[nome_dela]", who_color="#ffe08a",
                      what_color="#ffe08a", what_italic=True)
define dh = Character("Daniel", who_color="#a3c9ff",
                      what_color="#cfe2ff", what_italic=True)

# A Lucy do outro lado da linha, em 2024: voz pequena, cinza, sem cor.
define l_tel = Character("Lucy (telefone)", who_color="#9aa3ad",
                         what_color="#a7adb5", what_size=22)

# A voz do jogo (módulos, falhas, vidas).
define sistema = Character("SISTEMA", who_color="#ff6b6b", what_color="#ffb3b3")


# ==========================================
# 2. IMAGENS (placeholders do tutorial)
# ==========================================
# Quando a arte final chegar, basta trocar o arquivo à direita.

# --- Tom de lembrança ----------------------------------------------
# Tudo que é 2014 aparece um pouco mais quente e desbotado; o presente
# (2024) e os módulos ficam com a cor normal. Os sprites trocam de tom
# sozinhos conforme o "quando" (ConditionSwitch confere a cada fala).
init -5 python:
    MAT_LEMBRANCA = TintMatrix("#fff0dc") * SaturationMatrix(0.78)

    # Os PNGs estão em 2x (720x1082): zoom 0.6 = tamanho de retrato na
    # tela de 1280x720, e em tela cheia o Ren'Py usa os pixels extras.
    # (O tom de 2014 fica só nos cenários: tingir os sprites também
    # travava as transições na versão web.)
    def sprite(arquivo):
        return Transform(arquivo, zoom=0.6)

    # Cenários em 1920x1080, encaixados na tela de 1280x720.
    def fundo(arquivo):
        return Transform(arquivo, xysize=(1280, 720))

    def fundo_2014(arquivo):
        return Transform(arquivo, xysize=(1280, 720), matrixcolor=MAT_LEMBRANCA)

# --- Cenários ------------------------------------------------------
# Arte final em game/images/cenarios/ (1920x1080). Pra trocar um, ponha o
# arquivo em game/images/cenarios/ e mude só o lado direito da linha.
# Prompts de cada um: no art bible (Design System) e no fim deste bloco.

# O canto do saguão do congresso, onde a conversa inteira acontece.
# Ele vai esvaziando: tarde (prólogo) -> anoitecer -> noite (fim).
image bg saguao tarde = fundo("images/cenarios/saguao_tarde.jpg")
image bg saguao anoitecer = Transform("images/cenarios/saguao_tarde.jpg", xysize=(1280, 720), matrixcolor=TintMatrix("#f0b48a") * BrightnessMatrix(-0.08))
image bg saguao noite = Transform("images/cenarios/saguao_tarde.jpg", xysize=(1280, 720), matrixcolor=TintMatrix("#7d8ab8") * BrightnessMatrix(-0.22))
# O congresso por dentro: ar-condicionado, luz fria, crachá azul.
image bg congresso = fundo("images/cenarios/congresso.jpg")

# 2014
image bg patio = fundo_2014("images/cenarios/patio.jpg")
image bg trilha = fundo_2014("images/cenarios/trilha.jpg")
image bg morro = fundo_2014("images/cenarios/morro.jpg")
image bg sala_vazia = fundo_2014("images/cenarios/sala_vazia.jpg")
image bg quarto = fundo_2014("images/cenarios/quarto.jpg")
image bg orelhao = fundo_2014("images/cenarios/orelhao.jpg")
image bg laboratorio = fundo_2014("images/cenarios/laboratorio.jpg")

# 2024
image bg aeroporto = fundo("images/cenarios/aeroporto.jpg")
# A rua em Salvador, três da tarde: calor estourado.
image bg rua_salvador = fundo("images/cenarios/rua_salvador.jpg")

# O ping-pong que eles montaram na tela do osciloscópio (fase 25).
image osciloscopio = Transform("bg pong field.png", matrixcolor=TintMatrix("#6dff95") * BrightnessMatrix(-0.25))

# Colegas sem rosto que vão ocupando o lugar dela na sala (fase 12).
image colega = Transform("lucy mad", matrixcolor=BrightnessMatrix(0.16) * TintMatrix("#000000"), alpha=0.85)

# --- Ilustrações de momentos-chave (CG) ------------------------------
# Tela cheia. Por enquanto um cartão com a descrição da cena.
init python:
    def cg_provisorio(descricao, fundo):
        return Fixed(
            Solid(fundo),
            Text("[[ " + descricao + " ]", size=34, color="#f6f1ea",
                 xalign=0.5, yalign=0.45, textalign=0.5, xmaximum=900),
            )

image cg carta = cg_provisorio("CG: a carta da direção, envelope pardo aberto", "#5b4a33")
# A ilustração do morro. Enquanto a arte final não chega (salve como
# game/images/cgs/cg_morro.jpg que ela entra sozinha), a cena é montada
# com o próprio cenário: a câmera se aproxima devagar e os dois viram
# vultos contra as luzes da cidade.
transform cg_respira:
    align (0.5, 0.5)
    zoom 1.0
    linear 14.0 zoom 1.08

init 10 python:
    if renpy.loadable("images/cgs/cg_morro.jpg"):
        renpy.image(("cg", "morro"), "images/cgs/cg_morro.jpg")
    else:
        _vulto = ColorizeMatrix("#070a16", "#151c36")
        renpy.image(("cg", "morro"), Fixed(
            At("bg morro", cg_respira),
            Solid("#0a0f2a40"),
            Transform("images/personagens/mih_idle.png", zoom=0.275, matrixcolor=_vulto, xcenter=0.45, ypos=0.84, yanchor=1.0),
            Transform("images/personagens/daniel_idle.png", zoom=0.285, matrixcolor=_vulto, xcenter=0.56, ypos=0.84, yanchor=1.0),
            ))
image cg print = cg_provisorio("CG: o print da fita no celular, ela cortada no canto do quadro", "#2b2b33")
image cg final = cg_provisorio("CG: o celular na mesa entre duas taças vazias, a música tocando", "#2a2236")

# Sprites dos personagens: game/images/personagens/ (720x1082, remake
# visual em 2x, cortados no quadril). Ver sprite() acima.
image mirela idle = sprite("images/personagens/mih_idle.png")
image mirela happy = sprite("images/personagens/mih_happy.png")
image mirela sad = sprite("images/personagens/mih_sad.png")
# Ainda não existem versões "muito feliz" e "preocupada": usam as mais
# próximas. Quando a arte chegar, é só trocar o arquivo aqui.
image mirela vhappy = sprite("images/personagens/mih_happy.png")
image mirela concerned = sprite("images/personagens/mih_sad.png")

image daniel idle = sprite("images/personagens/daniel_idle.png")
image daniel happy = sprite("images/personagens/daniel_happy.png")
image daniel sad = sprite("images/personagens/daniel_sad.png")

# O Daniel de 2014 ela não consegue montar: só o contorno dele.
image daniel sombra = sprite("images/personagens/daniel_idle.png")

# Os tutoriais oficiais mostram a "eileen". Aqui quem aparece é a Mih:
# as três expressões usadas nos tutoriais apontam pros sprites dela.
# (init 999 roda depois da leitura automática da pasta images/.)
init 999 python:
    # Fundo dos módulos: o próprio saguão, escurecido. Os tutoriais
    # oficiais chamam "bg washington"; aqui ele vira o saguão.
    renpy.image(("bg", "washington"), Transform("images/cenarios/saguao_tarde.jpg", xysize=(1280, 720), matrixcolor=BrightnessMatrix(-0.18) * SaturationMatrix(0.6)))

    renpy.image(("eileen", "happy"), sprite("images/personagens/mih_happy.png"))
    renpy.image(("eileen", "vhappy"), sprite("images/personagens/mih_happy.png"))
    renpy.image(("eileen", "concerned"), sprite("images/personagens/mih_sad.png"))

    # A Lucy do Mihrage (mesmo traço da Mih e do Daniel) no lugar da
    # Lucy padrão do Ren'Py, inclusive dentro dos tutoriais.
    for _expr in ("happy", "mad", "sad", "idle"):
        renpy.image(("lucy", _expr), sprite("images/personagens/lucy_%s.png" % _expr))

image exclamation = "exclamation.png"
image reconstrucao_icone = "logo solid.png"

# O Daniel de 2014 que ela não consegue montar: um vulto azul-escuro,
# meio apagado, em vez de um recorte preto chapado.
transform silhueta_pessoa:
    matrixcolor ColorizeMatrix("#10162c", "#26315a")
    alpha 0.88

# Fase 16: a pressão cai e o chão desnivela por um segundo.
transform vertigem:
    subpixel True
    align (0.5, 0.5)
    zoom 1.0 rotate 0
    ease 0.35 zoom 1.7 rotate 14
    ease 0.6 rotate -7
    ease 1.4 zoom 1.0 rotate 0

# Fase 17: do calor da rua pro ar gelado - um clarão, não uma passagem.
define choque_termico = Fade(0.08, 0.0, 0.9, color="#ffffff")

# Uma lembrança "se formando": entra transparente e um pouco maior e
# vai assentando no lugar. (O desfoque travava junto com o tom de 2014.) Usada quando o jogador monta uma parte da cena.
transform memoria_surge:
    alpha 0.0 zoom 1.03
    easein 1.4 alpha 1.0 zoom 1.0

# A lembrança "engasga" quando chega no que não foi dito: tremida curta
# e piscadas, sem desfoque (desfoque trava na web).
transform memoria_trava:
    xoffset 0 alpha 1.0
    linear 0.05 xoffset -9 alpha 0.75
    linear 0.05 xoffset 7 alpha 1.0
    linear 0.04 xoffset -4 alpha 0.6
    linear 0.06 xoffset 0 alpha 1.0
    pause 0.5
    linear 0.04 xoffset 5 alpha 0.8
    linear 0.06 xoffset 0 alpha 1.0

# A câmera chegando perto dela, devagar, no morro.
transform aproxima:
    subpixel True
    xalign 0.5 yalign 1.0
    zoom 1.3
    linear 6.0 zoom 1.42

# Ela de costas pro Daniel, olhando a cidade: um pouco à frente e menor.
transform afastada:
    subpixel True
    xcenter 0.38 yalign 1.0
    zoom 1.0
    easein 2.0 xcenter 0.3

transform icone_canto:
    xalign 1.0
    yalign 0.0
    alpha 0.9


# ==========================================
# 3. ESTADO DE JOGO
# ==========================================

define VIDAS_INICIAIS = 3
define config.default_language = "portuguese"

default vidas = 3
default checkpoint_atual = "prologo"

# Rótulo de tempo no HUD: quando é a cena que está na tela.
default quando = ""

# Módulo em andamento (vai pro caderno junto com a lição).
default modulo_atual = ""
default quando_antes = ""

# Som ambiente da cena atual (volta depois de cada módulo).
default ambiente_atual = None

# Trilha sonora tocando agora (volta sozinha depois de cada módulo).
default trilha_atual = None

# Caderno: lista de (módulo, lição) já vistas.
default caderno = []
default caderno_avisado = False
default vidas_avisado = False

# Estado narrativo do Capítulo 2 (usado de novo no Capítulo 3).
default primeira_ligacao = ""
default busca = "Mirela"

init python:

    import re

    def normaliza(s):
        """
        Sanitiza o que o jogador digitou SEM mexer em maiúsculas -
        no Ren'Py `L` e `l` são nomes diferentes, e o jogo ensina isso.

        - tira espaços das pontas e colapsa espaços repetidos;
        - aspas duplas e simples contam igual;
        - descarta os prefixos `$ ` e `define `;
        - ignora espaço em volta de = , ( );
        - 2.0 vale o mesmo que 2.
        """
        s = s.strip().replace('"', "'")
        s = " ".join(s.split())

        if s.startswith("$"):
            s = s[1:].strip()

        if s.startswith("define "):
            s = s[len("define "):].strip()

        s = re.sub(r"\s*([=,()])\s*", r"\1", s)
        s = re.sub(r"\b(\d+)\.0+\b", r"\1", s)

        return s

    def confere(resposta, aceitas):
        """
        True se a resposta bate com alguma das formas aceitas.

        Cada forma pode ser:
          "texto"        -> comparado depois de normalizar os dois lados
          "re:padrão"    -> expressão regular sobre a resposta normalizada
          "rei:padrão"   -> idem, sem diferenciar maiúsculas (cores hex)
        """
        r = normaliza(resposta)

        for a in aceitas:
            if a.startswith("re:"):
                if re.fullmatch(a[3:], r):
                    return True
            elif a.startswith("rei:"):
                if re.fullmatch(a[4:], r, re.IGNORECASE):
                    return True
            elif r == normaliza(a):
                return True

        return False

    # Som ambiente: põe um .ogg em game/audio/ambiente/<nome>.ogg e ele
    # toca em loop. Se o arquivo ainda não existir, só não toca nada.
    renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

    # Trilha sonora (canal music, em loop). "miragem" é o tema do jogo; a
    # fase do Hey Jude troca pela música do Daniel. Volume da trilha um
    # pouco abaixo pra não brigar com o som ambiente e as falas.
    TRILHAS = {
        "miragem": ("audio/miragem.ogg", 0.55),
        "hey_jude": ("audio/hey_jude.ogg", 0.9),
    }

    def trilha(nome=None, fade=2.0):
        store.trilha_atual = nome
        if not nome:
            renpy.music.stop(channel="music", fadeout=fade)
            return
        arquivo, vol = TRILHAS[nome]
        if renpy.loadable(arquivo):
            renpy.music.play(arquivo, channel="music", loop=True, fadein=fade,
                             fadeout=fade, if_changed=True, relative_volume=vol)

    def ambiente(nome=None, guardar=True, volume=1.0):
        if guardar:
            store.ambiente_atual = nome
        if not nome:
            renpy.music.stop(channel="ambiente", fadeout=1.0)
            return
        arquivo = "audio/ambiente/" + nome + ".ogg"
        if renpy.loadable(arquivo):
            renpy.music.play(arquivo, channel="ambiente", fadein=1.0, if_changed=True, relative_volume=volume)
        else:
            renpy.music.stop(channel="ambiente", fadeout=1.0)

    # Lembranças (2014) ganham um tom quente e desbotado na tela inteira;
    # o presente (2024) e os módulos ficam com a cor normal. Assim dá pra
    # saber "quando" estamos só de olhar.
    def anota(licao):
        """Guarda a lição no caderno (uma vez só por módulo+lição)."""
        item = (modulo_atual, licao)
        if licao and item not in caderno:
            caderno.append(item)


# ==========================================
# 4. HUD, CADERNO E TELAS DE APOIO
# ==========================================

# HUD sem caixas: uma sombra suave no topo, as vidas como três pontos
# de luz (o último pisca quando é o que sobrou) e o "quando" em itálico,
# quente nas lembranças e frio no presente.
transform hud_entra:
    alpha 0.0
    easein 0.8 alpha 1.0

transform vida_ultima:
    alpha 1.0
    ease 0.8 alpha 0.3
    ease 0.8 alpha 1.0
    repeat

transform vida_perdida:
    alpha 0.35

screen hud_vidas():
    zorder 50

    $ _lembranca = quando.startswith("2014")
    $ _cor_tempo = "#ffd9a8" if _lembranca else "#cfe2ff"
    $ _cor_vida = "#ffc9a3" if _lembranca else "#ffb3b3"

    add "gui/hud_sombra.png" at hud_entra

    hbox at hud_entra:
        xpos 58
        ypos 16
        spacing 26

        hbox:
            spacing 7
            yalign 0.5
            for _i in range(VIDAS_INICIAIS):
                if _i >= vidas:
                    text "○" size 19 color "#ffffff" outlines [(2, "#00000070", 0, 0)] at vida_perdida
                elif vidas == 1:
                    text "●" size 19 color "#ff8a7a" outlines [(2, "#00000070", 0, 0)] at vida_ultima
                else:
                    text "●" size 19 color _cor_vida outlines [(2, "#00000070", 0, 0)]

        if quando:
            text "[quando]" size 17 italic True color _cor_tempo yalign 0.5 outlines [(2, "#00000080", 0, 0)]

        if caderno:
            textbutton "✎ caderno":
                yalign 0.5
                background None
                padding (0, 0)
                text_size 17
                text_color "#ffe08acc"
                text_hover_color "#ffffff"
                text_outlines [(2, "#00000080", 0, 0)]
                action Show("caderno_tela")


# Um pulso vermelho nas bordas quando uma vida cai.
transform dano_pulsa:
    alpha 0.0
    linear 0.08 alpha 1.0
    easeout 0.9 alpha 0.0

screen dano():
    zorder 55
    add "gui/dano.png" at dano_pulsa
    timer 1.0 action Hide("dano")


screen caderno_tela():
    modal True
    zorder 100

    # Clicar fora do caderno também fecha.
    button:
        xfill True
        yfill True
        background "#000000cc"
        action Hide("caderno_tela")

    # Fica na metade de cima da tela: na versão web a caixa de
    # digitação ocupa a parte de baixo, e cobria o botão Fechar.
    frame:
        xalign 0.5
        ypos 40
        xsize 1000
        ysize 470
        background "#f6f1ea"
        padding (36, 24)

        vbox:
            spacing 14
            xfill True

            hbox:
                xfill True
                text "Caderno de anotações" size 30 color "#1f1a24" yalign 0.5
                textbutton "Fechar ✕":
                    xalign 1.0
                    yalign 0.5
                    text_size 22
                    text_color "#5f5866"
                    text_hover_color "#1f1a24"
                    action Hide("caderno_tela")

            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 360

                vbox:
                    spacing 18
                    xsize 900

                    for titulo, licao in caderno:
                        vbox:
                            spacing 4
                            text titulo size 18 color "#a0522d" bold True
                            text licao size 20 color "#1f1a24" substitute False

    key "game_menu" action Hide("caderno_tela")


# Antes mostrava um ícone no canto enquanto ela "remontava" a
# lembrança. Saiu: confundia mais do que ajudava. A tela continua
# existindo (vazia) pra não precisar mexer em cada chamada.
screen reconstruindo():
    zorder 45


# Caixa de digitação das fases. A padrão do Ren'Py fica presa na
# caixa de diálogo, lá embaixo, e com o enunciado junto ela descia
# pra fora da tela. Esta fica no meio, logo abaixo do trecho de código.
screen entrada_codigo(prompt):
    zorder 60

    frame:
        xalign 0.5
        ypos 250
        xsize 980
        background "#0d1117f2"
        padding (32, 24)

        vbox:
            spacing 14
            xfill True

            text prompt size 22 color "#f6f1ea" substitute False

            frame:
                xfill True
                background "#1f2733"
                padding (16, 10)

                input id "input" size 26 color "#b7f5c0"

            text "Enter pra confirmar · o caderno (✎) continua no canto da tela" size 15 color "#8b949e"


screen trecho_codigo(titulo, linhas):
    zorder 40

    frame:
        xalign 0.5
        ypos 60
        xsize 940
        background "#0d1117ee"
        padding (24, 18)

        vbox:
            spacing 6
            xsize 890

            text titulo size 19 color "#ffcc00"
            text "- - - - - - - - - - - - - - - - - - - -" size 15 color "#586069"

            for linha in linhas:
                text linha size 17 color "#b7f5c0" substitute False


# ==========================================
# 5. A MOLDURA DOS MÓDULOS
# ==========================================
# Todo trecho do tutorial oficial entra por aqui: a conversa "pausa",
# o módulo roda, e a tela volta pro preto pra fase remontar a cena.
# `com_menu`: o módulo tem um menu de tópicos - avisa como sair dele.

# Volta pro presente: os dois sentados no saguão, conversando.
label agora(mih="idle", dan="idle"):
    $ quando = "2024 · agora"
    $ ambiente("coquetel")
    scene bg saguao tarde
    $ renpy.show("mirela " + mih, at_list=[right])
    $ renpy.show("daniel " + dan, at_list=[left])
    with dissolve
    return


label modulo(tutorial, numero, titulo, com_menu=False):

    hide screen reconstruindo

    $ quando_antes = quando
    $ quando = "módulo " + str(numero) + "/26"
    $ modulo_atual = "Módulo " + str(numero) + " — " + titulo

    $ ambiente(None, guardar=False)

    # Entrada mais suave: escurece devagar, mostra o título sozinho
    # por um instante, e abre na Mirela explicando.
    scene black
    with Dissolve(0.8)

    show screen titulo_modulo(numero, titulo)
    with Dissolve(0.6)
    $ renpy.pause(1.8)
    hide screen titulo_modulo
    with Dissolve(0.6)

    scene bg washington
    show eileen happy at center
    with Dissolve(1.0)

    if com_menu:
        sistema "Esse módulo tem um menu de tópicos. Vê quantos quiser; a última opção do menu te devolve pra conversa."

    $ reset_example()
    call expression tutorial

    hide example
    scene black
    with Dissolve(0.8)

    $ ambiente(ambiente_atual)
    $ trilha(trilha_atual)

    $ quando = quando_antes

    return


screen titulo_modulo(numero, titulo):
    zorder 50
    vbox:
        align (0.5, 0.45)
        spacing 10
        text "MÓDULO [numero]" size 22 color "#ffb3b3" xalign 0.5
        text "[titulo]" size 40 color "#f6f1ea" xalign 0.5


# ==========================================
# 6. VIDAS, FALHA E CHECKPOINT
# ==========================================

# Tira uma vida e devolve True se ainda sobrou alguma. Só RETORNA,
# nunca salta - assim a pilha de call fica limpa.
# Bloqueia o rollback: dá pra voltar e reler a conversa, mas não dá
# pra desdizer uma resposta errada.
label perder_vida:

    $ vidas -= 1
    $ renpy.block_rollback()
    show screen dano

    if vidas > 0:
        with vpunch
        sistema "A lembrança falhou. Vidas restantes: [vidas]."
        if not vidas_avisado:
            $ vidas_avisado = True
            sistema "São três vidas por capítulo. Perdendo todas, a conversa volta pro último ponto estável."
        return True

    with vpunch
    sistema "Falha crítica. Nenhuma vida restante."
    return False


label game_over:

    hide screen reconstruindo
    hide screen trecho_codigo
    hide screen caderno_tela

    scene black
    with dissolve

    sistema "A CONVERSA SE PERDEU."

    sistema "Fragmentos demais de uma vez. Os dois precisam voltar um pouco e recomeçar dali."

    $ vidas = VIDAS_INICIAIS

    sistema "Vidas: [vidas]/[VIDAS_INICIAIS]. Voltando pro último ponto estável."

    jump expression checkpoint_atual


# ==========================================
# 7. AS TRÊS DINÂMICAS DE FASE
# ==========================================
# Regra geral: nenhuma fase cobra algo que não tenha sido ensinado
# antes. Quem chama passa `licao` com a regra e o formato, e só
# depois vem a pergunta. Toda lição vai pro caderno.

# --- Dinâmica 1: múltipla escolha -------------------------------
# opcoes: lista de (texto_da_opcao, é_a_correta, feedback)
# A ordem das opções é embaralhada a cada tentativa.
label fase_escolha(pergunta, opcoes, licao=""):

    if licao:
        $ anota(licao)
        sistema "[licao]"
        if not caderno_avisado:
            $ caderno_avisado = True
            sistema "Essa regra foi pro caderno (✎), no canto de cima da tela. Dá pra abrir a qualquer hora, inclusive na hora de responder."

    while True:

        python:
            _ordem = list(range(len(opcoes)))
            renpy.random.shuffle(_ordem)
            _itens = [(opcoes[i][0], i) for i in _ordem]
            # A pergunta fica na caixa de texto enquanto as opções
            # aparecem (antes ela sumia quando o menu abria).
            sistema(pergunta, interact=False)
            _escolhido = renpy.display_menu(_itens)
            _texto, _acertou, _feedback = opcoes[_escolhido]

        sistema "[_feedback]"

        if _acertou:
            return True

        call perder_vida

        if not _return:
            return False


# --- Dinâmica 2: escrita de código ------------------------------
# aceitas: formas válidas (ver confere: texto, "re:" ou "rei:")
label fase_escrita(instrucao, aceitas, dica, licao="", prompt="Digite o comando:"):

    if licao:
        $ anota(licao)
        sistema "[licao]"
        if not caderno_avisado:
            $ caderno_avisado = True
            sistema "Essa regra foi pro caderno (✎), no canto de cima da tela. Dá pra abrir a qualquer hora, inclusive na hora de responder."

    while True:

        sistema "[instrucao]"

        # A instrução vai junto na caixa de digitação: na versão web a
        # caixa cobre o texto do SISTEMA, e o jogador perdia o enunciado.
        $ _resposta = renpy.input(instrucao + "\n\n" + prompt, length=160, screen="entrada_codigo")

        if confere(_resposta, aceitas):
            sistema "Comando aceito."
            return True

        sistema "[dica]"

        call perder_vida

        if not _return:
            return False


# --- Dinâmica 3: correção de código (debug) ---------------------
# O trecho quebrado aparece ANTES da lição e fica visível enquanto o
# jogador corrige.
label fase_debug(titulo, linhas, instrucao, aceitas, dica, licao=""):

    show screen trecho_codigo(titulo, linhas)

    sistema "Tem um trecho quebrado aí em cima. Olha ele com calma."

    if licao:
        $ anota(licao)
        sistema "[licao]"
        if not caderno_avisado:
            $ caderno_avisado = True
            sistema "Essa regra foi pro caderno (✎), no canto de cima da tela. Dá pra abrir a qualquer hora, inclusive na hora de responder."

    while True:

        sistema "[instrucao]"

        $ _resposta = renpy.input(instrucao + "\n\nEscreva a linha corrigida:", length=160, screen="entrada_codigo")

        if confere(_resposta, aceitas):
            sistema "Corrigido."
            hide screen trecho_codigo
            return True

        sistema "[dica]"

        call perder_vida

        if not _return:
            hide screen trecho_codigo
            return False
