# The script of the game goes in this file.

# --- Characters --------------------------------------------------------------

init python:
    def bezout_habla(event, interact=True, **kwargs):
        """Anima la boca durante el scroll y la detiene al terminar el texto."""
        if event == "begin":
            renpy.show("bezout hablando", at_list=[renpy.store.bezout_grande])
        elif event in ("slow_done", "end"):
            renpy.show("bezout neutral", at_list=[renpy.store.bezout_grande])

define bz = Character("Bezout", color="#d9a441", callback=bezout_habla)
define fin_juego = Character(
    None,
    what_style="game_over_text",
    window_style="game_over_window",
    statement_name="say-centered",
)

# --- Story flags -------------------------------------------------------------
# These are here so later scenes can react to the player's decisions.

default proyecto_iniciado = False
default zona_despejada = False
default metodo_extraccion = None       # "mercurio" o "gravimetrico"
default uso_mercurio = False
default plan_cierre = False
default negaciones_finales = 0


# --- Minimalist artwork ------------------------------------------------------
# A shared palette keeps the room, travel view, forest, and character cohesive:
# deep jungle greens, blue-green water, warm wood, and a muted gold accent.

init -1 python:
    def rio_por_ventana(ancho, alto, orillas):
        """El mismo cauce curvo, estrechándose suavemente hacia la derecha."""
        def bordes(posicion):
            for (x0, arriba0, abajo0), (x1, arriba1, abajo1) in zip(orillas, orillas[1:]):
                if posicion <= x1:
                    avance = float(posicion - x0) / (x1 - x0)
                    return (int(arriba0 + (arriba1 - arriba0) * avance),
                            int(abajo0 + (abajo1 - abajo0) * avance))
            return orillas[-1][1:]

        partes = []
        for x in range(0, ancho, 8):
            arriba, abajo = bordes(x)
            tramo = min(8, ancho - x)
            partes.append(Solid("#5b9875", xpos=x, ypos=arriba - 4, xysize=(tramo, 4)))
            partes.append(Solid("#4a9bad", xpos=x, ypos=arriba,
                                xysize=(tramo, abajo - arriba)))
            partes.append(Solid("#3d889d", xpos=x, ypos=abajo - (abajo - arriba) // 3,
                                xysize=(tramo, (abajo - arriba) // 3)))

        for indice, (fraccion, largo) in enumerate(((0.11, 0.13), (0.38, 0.11), (0.70, 0.13))):
            x = int(ancho * fraccion)
            arriba, abajo = bordes(x)
            partes.append(Solid("#acd4c8", xpos=x,
                                ypos=arriba + int((abajo - arriba) * (0.65 if indice == 1 else 0.30)),
                                xysize=(int(ancho * largo), 3)))
        return Fixed(*partes, xysize=(ancho, alto))


image cuarto rio pampa = rio_por_ventana(340, 262, (
    (0, 183, 241), (85, 188, 249), (170, 195, 244),
    (245, 192, 236), (340, 182, 227),
))

image ventana rio pampa = rio_por_ventana(820, 404, (
    (0, 259, 370), (180, 269, 378), (390, 283, 368),
    (590, 273, 350), (820, 256, 326),
))

image cuarto vista pampa = Fixed(
    # Vista desde la habitación: cielo y selva continua de Madre de Dios.
    Solid("#82b8be"),
    Solid("#9bc9c0", xpos=0, ypos=80, xysize=(340, 50)),
    Text("●", size=37, color="#e0e8df", xpos=34, ypos=29),
    Text("●", size=47, color="#e0e8df", xpos=54, ypos=18),
    Text("●", size=31, color="#e0e8df", xpos=83, ypos=31),
    # Sol alto, parcialmente cubierto por las copas de la orilla opuesta.
    Text("●", size=78, color="#e5d48d", xpos=243, ypos=12),
    Solid("#4a825d", xpos=0, ypos=124, xysize=(340, 138)),
    Solid("#305f47", xpos=0, ypos=157, xysize=(340, 105)),
    # Copas cercanas entre sí y de diferentes alturas: no hay una hilera vacía.
    Text("●", size=60, color="#397c55", xpos=-14, ypos=95),
    Text("●", size=52, color="#286b4b", xpos=25, ypos=108),
    Text("●", size=62, color="#347451", xpos=54, ypos=91),
    Text("●", size=49, color="#448a60", xpos=91, ypos=106),
    Text("●", size=65, color="#286b4b", xpos=116, ypos=91),
    Text("●", size=52, color="#398159", xpos=156, ypos=106),
    Text("●", size=59, color="#2b6b4c", xpos=186, ypos=88),
    Text("●", size=53, color="#448a60", xpos=225, ypos=104),
    Text("●", size=61, color="#296b4b", xpos=255, ypos=92),
    Text("●", size=54, color="#398159", xpos=298, ypos=106),
    Text("●", size=48, color="#286b4b", xpos=322, ypos=99),
    Text("●", size=42, color="#266145", xpos=11, ypos=137),
    Text("●", size=44, color="#397c55", xpos=74, ypos=137),
    Text("●", size=42, color="#286b4b", xpos=140, ypos=135),
    Text("●", size=45, color="#397c55", xpos=277, ypos=137),

    # El Tambopata recorre la vista hacia la derecha, no hacia el observador.
    "cuarto rio pampa",
    # Vegetación cercana que enmarca ambas márgenes.
    Text("●", size=91, color="#245d41", xpos=-33, ypos=159),
    Text("●", size=72, color="#30714d", xpos=2, ypos=202),
    Text("●", size=85, color="#245d41", xpos=292, ypos=162),
    Text("●", size=65, color="#347b52", xpos=309, ypos=207),
    xysize=(340, 262),
)

image bg cuarto = Fixed(
    # Habitación: pared, zócalo y piso de madera oscura.
    Solid("#18382d"),
    Solid("#245344", xpos=0, ypos=0, xysize=(1280, 88)),
    Solid("#10261f", xpos=0, ypos=510, xysize=(1280, 210)),
    Solid("#0b1a16", xpos=0, ypos=560, xysize=(1280, 160)),
    Solid("#315f4d", xpos=0, ypos=505, xysize=(1280, 8)),

    # Ventana con vista al río y a la selva de Madre de Dios.
    Solid("#805e3d", xpos=754, ypos=76, xysize=(392, 314)),
    Solid("#102c27", xpos=766, ypos=88, xysize=(368, 290)),
    # Recorta las copas a los límites del vidrio: Fixed no recorta sus hijos.
    Transform("cuarto vista pampa", crop=(0, 0, 340, 262), xpos=780, ypos=102),
    # El marco siempre queda por delante del paisaje.
    Solid("#805e3d", xpos=754, ypos=76, xysize=(392, 12)),
    Solid("#805e3d", xpos=754, ypos=378, xysize=(392, 12)),
    Solid("#805e3d", xpos=754, ypos=88, xysize=(12, 290)),
    Solid("#805e3d", xpos=1134, ypos=88, xysize=(12, 290)),
    Solid("#805e3d", xpos=940, ypos=88, xysize=(14, 276)),
    Solid("#805e3d", xpos=780, ypos=220, xysize=(340, 13)),

    # Cama con manta verde y una franja dorada.
    Solid("#674a32", xpos=58, ypos=348, xysize=(555, 238)),
    Solid("#d6d2b5", xpos=84, ypos=368, xysize=(204, 95)),
    Solid("#b9c4aa", xpos=295, ypos=368, xysize=(155, 95)),
    Solid("#2f6851", xpos=72, ypos=455, xysize=(528, 130)),
    Solid("#275942", xpos=72, ypos=530, xysize=(528, 55)),
    Solid("#c8a758", xpos=72, ypos=507, xysize=(528, 15)),
    Solid("#4d3527", xpos=78, ypos=585, xysize=(22, 78)),
    Solid("#4d3527", xpos=570, ypos=585, xysize=(22, 78)),

    # Velador, lámpara cálida, celular y una planta pequeña.
    Solid("#62442e", xpos=642, ypos=422, xysize=(98, 110)),
    Solid("#805e3d", xpos=654, ypos=532, xysize=(74, 36)),
    Solid("#e1c667", xpos=670, ypos=350, xysize=(42, 45)),
    Solid("#c59f52", xpos=678, ypos=395, xysize=(26, 28)),
    Solid("#091614", xpos=665, ypos=428, xysize=(42, 69)),
    Solid("#73b8ae", xpos=670, ypos=435, xysize=(32, 48)),
    Solid("#a66d45", xpos=1180, ypos=432, xysize=(48, 70)),
    Text("●", size=58, color="#73a66a", xpos=1155, ypos=372),
    Text("●", size=48, color="#4d8b5d", xpos=1197, ypos=360),
)

image bg cuarto periodico = Fixed(
    "bg cuarto",

    # Mesa auxiliar con el periódico del día.
    Solid("#0b1a16a0", xpos=742, ypos=564, xysize=(330, 18)),
    Solid("#62442e", xpos=748, ypos=430, xysize=(318, 26)),
    Solid("#4d3527", xpos=760, ypos=456, xysize=(294, 104)),
    Solid("#4d3527", xpos=768, ypos=560, xysize=(18, 88)),
    Solid("#4d3527", xpos=1026, ypos=560, xysize=(18, 88)),

    # Periódico doblado sobre la mesa.
    Solid("#d8d8d4", xpos=778, ypos=422, xysize=(248, 40)),
    Solid("#f2f2f0", xpos=770, ypos=418, xysize=(248, 40)),
    Solid("#3a3a38", xpos=792, ypos=426, xysize=(92, 5)),
    Solid("#9a9a96", xpos=792, ypos=436, xysize=(200, 4)),
    Solid("#8a8a86", xpos=792, ypos=444, xysize=(70, 10)),
    Solid("#9a9a96", xpos=872, ypos=444, xysize=(90, 3)),
    Solid("#9a9a96", xpos=872, ypos=449, xysize=(78, 3)),
    Solid("#9a9a96", xpos=872, ypos=454, xysize=(84, 3)),

    # Taza de café.
    Solid("#d8d8d4", xpos=1016, ypos=426, xysize=(44, 8)),
    Solid("#2f6851", xpos=1022, ypos=398, xysize=(28, 30)),
    Solid("#2f6851", xpos=1048, ypos=406, xysize=(10, 12)),
    Solid("#e1c667", xpos=1026, ypos=402, xysize=(20, 20)),
)

image ventana vista pampa = Fixed(
    # Acercamiento a la misma ribera de Madre de Dios visible desde el cuarto.
    Solid("#82b8be"),
    Solid("#9bc9c0", xpos=0, ypos=132, xysize=(820, 85)),
    Text("●", size=69, color="#e0e8df", xpos=100, ypos=39),
    Text("●", size=91, color="#e0e8df", xpos=135, ypos=23),
    Text("●", size=61, color="#e0e8df", xpos=197, ypos=48),
    Text("●", size=49, color="#dce5db", xpos=362, ypos=66),
    Text("●", size=63, color="#dce5db", xpos=391, ypos=52),
    # Sol alto: la orilla boscosa lo cubre parcialmente.
    Text("●", size=133, color="#e5d48d", xpos=612, ypos=58),
    Solid("#4a825d", xpos=0, ypos=202, xysize=(820, 202)),
    Solid("#305f47", xpos=0, ypos=256, xysize=(820, 148)),

    # Muchas copas superpuestas, con diferentes alturas y tonos.
    Text("●", size=104, color="#397c55", xpos=-24, ypos=149),
    Text("●", size=93, color="#286b4b", xpos=29, ypos=169),
    Text("●", size=113, color="#347451", xpos=77, ypos=147),
    Text("●", size=90, color="#448a60", xpos=141, ypos=170),
    Text("●", size=116, color="#286b4b", xpos=190, ypos=142),
    Text("●", size=93, color="#398159", xpos=264, ypos=167),
    Text("●", size=105, color="#2b6b4c", xpos=314, ypos=140),
    Text("●", size=93, color="#448a60", xpos=384, ypos=162),
    Text("●", size=105, color="#296b4b", xpos=439, ypos=145),
    Text("●", size=95, color="#398159", xpos=504, ypos=166),
    Text("●", size=112, color="#286b4b", xpos=567, ypos=137),
    Text("●", size=91, color="#397c55", xpos=638, ypos=158),
    Text("●", size=106, color="#286b4b", xpos=692, ypos=145),
    Text("●", size=100, color="#398159", xpos=758, ypos=161),
    Text("●", size=65, color="#286b4b", xpos=21, ypos=222),
    Text("●", size=76, color="#397c55", xpos=118, ypos=219),
    Text("●", size=67, color="#286b4b", xpos=229, ypos=226),
    Text("●", size=75, color="#397c55", xpos=351, ypos=216),
    Text("●", size=74, color="#286b4b", xpos=711, ypos=218),

    # Una vista más amplia del mismo río, curvándose hacia la derecha.
    "ventana rio pampa",

    # Árboles de la orilla cercana enmarcan el río sin ocultarlo.
    Text("●", size=164, color="#245d41", xpos=-62, ypos=270),
    Text("●", size=129, color="#30714d", xpos=20, ypos=323),
    Text("●", size=150, color="#245d41", xpos=699, ypos=267),
    Text("●", size=115, color="#347b52", xpos=745, ypos=330),
    xysize=(820, 404),
)

image periodico_manu = Fixed(
    # Fotografía aérea del río Manu, ya en blanco y negro.
    Transform("manu.jpg", zoom=1.5),

    # Marco de impresión.
    Solid("#4a4a46", xpos=0, ypos=0, xysize=(720, 3)),
    Solid("#4a4a46", xpos=0, ypos=402, xysize=(720, 3)),
    Solid("#4a4a46", xpos=0, ypos=0, xysize=(3, 405)),
    Solid("#4a4a46", xpos=717, ypos=0, xysize=(3, 405)),

    xysize=(720, 405),
)

image periodico_puente = Fixed(
    # Fotografía aérea en blanco y negro del puente Billinghurst.
    Transform("puente.jpg", zoom=0.4286),

    # Marco de impresión.
    Solid("#4a4a46", xpos=0, ypos=0, xysize=(330, 3)),
    Solid("#4a4a46", xpos=0, ypos=164, xysize=(330, 3)),
    Solid("#4a4a46", xpos=0, ypos=0, xysize=(3, 167)),
    Solid("#4a4a46", xpos=327, ypos=0, xysize=(3, 167)),

    xysize=(330, 167),
)

image periodico base = Fixed(
    # Escritorio oscuro y periódico en blanco y negro.
    Solid("#142c25"),
    Solid("#1d3b31", xpos=0, ypos=0, xysize=(1280, 70)),
    Solid("#0c1d18", xpos=0, ypos=610, xysize=(1280, 110)),

    # Hoja de periódico.
    Solid("#0a1512", xpos=66, ypos=42, xysize=(1186, 700)),
    Solid("#d8d8d4", xpos=48, ypos=24, xysize=(1188, 700)),
    Solid("#f2f2f0", xpos=36, ypos=12, xysize=(1188, 700)),

    # Cabecera.
    Text("Madre de Dios", size=22, color="#161616", xpos=524, ypos=56),
    Text("El Noticiero", size=40, bold=True, color="#161616", xpos=80, ypos=38),
    Solid("#2a2a2a", xpos=80, ypos=96, xysize=(600, 3)),
    Solid("#9a9a96", xpos=760, ypos=44, xysize=(160, 5)),
    Solid("#9a9a96", xpos=940, ypos=44, xysize=(100, 5)),
    Solid("#9a9a96", xpos=760, ypos=56, xysize=(230, 5)),
    Solid("#9a9a96", xpos=760, ypos=68, xysize=(190, 5)),

    # Las fotografías se añaden según la portada: inicial o epílogo.
    Solid("#9a9a96", xpos=840, ypos=424, xysize=(220, 5)),
    Solid("#9a9a96", xpos=840, ypos=436, xysize=(190, 5)),

    # Columna de texto no especificado.
    Solid("#3a3a38", xpos=840, ypos=218, xysize=(220, 8)),
    Solid("#9a9a96", xpos=840, ypos=452, xysize=(300, 5)),
    Solid("#9a9a96", xpos=840, ypos=464, xysize=(280, 5)),
    Solid("#9a9a96", xpos=840, ypos=476, xysize=(310, 5)),
    Solid("#9a9a96", xpos=840, ypos=488, xysize=(260, 5)),
    Solid("#9a9a96", xpos=840, ypos=500, xysize=(290, 5)),
    Solid("#9a9a96", xpos=840, ypos=512, xysize=(240, 5)),
    Solid("#9a9a96", xpos=840, ypos=524, xysize=(300, 5)),

)

image bg periodico = Fixed(
    "periodico base",
    Text(
        "Índice de mercurio en la atmósfera\nsobre Manu aumenta en un 40%",
        size=36,
        bold=True,
        color="#111111",
        xpos=80,
        ypos=120,
        xmaximum=740,
        line_spacing=-2,
    ),
    Solid("#9a9a96", xpos=80, ypos=222, xysize=(620, 6)),
    Solid("#9a9a96", xpos=80, ypos=236, xysize=(560, 6)),
    Transform("periodico_manu", xpos=80, ypos=252),
    Transform("periodico_puente", xpos=840, ypos=252),
)

image bg ventana = Fixed(
    # Acercamiento a la ventana del cuarto, no a un vehículo distinto.
    Solid("#18382d"),
    Solid("#245344", xpos=0, ypos=0, xysize=(1280, 82)),
    Solid("#315f4d", xpos=0, ypos=545, xysize=(1280, 8)),
    Solid("#10261f", xpos=0, ypos=553, xysize=(1280, 167)),
    Solid("#805e3d", xpos=196, ypos=55, xysize=(888, 472)),
    Solid("#102c27", xpos=214, ypos=73, xysize=(852, 436)),
    Transform("ventana vista pampa", crop=(0, 0, 820, 404), xpos=230, ypos=89),
    # Marco delante de las copas, como en la ventana pequeña.
    Solid("#805e3d", xpos=196, ypos=55, xysize=(888, 18)),
    Solid("#805e3d", xpos=196, ypos=509, xysize=(888, 18)),
    Solid("#805e3d", xpos=196, ypos=73, xysize=(18, 436)),
    Solid("#805e3d", xpos=1066, ypos=73, xysize=(18, 436)),
    Solid("#805e3d", xpos=628, ypos=73, xysize=(17, 420)),
    Solid("#805e3d", xpos=230, ypos=286, xysize=(820, 16)),
)

image bezout cuerpo = Fixed(
    # Sombra y piernas.
    Solid("#0b1b17a0", xpos=28, ypos=416, xysize=(196, 12)),
    Solid("#182d2c", xpos=73, ypos=338, xysize=(47, 85)),
    Solid("#182d2c", xpos=133, ypos=338, xysize=(47, 85)),
    Solid("#0a1715", xpos=65, ypos=407, xysize=(62, 17)),
    Solid("#0a1715", xpos=128, ypos=407, xysize=(62, 17)),

    # Chaqueta azul verdosa, camisa y corbata dorada.
    Solid("#162b2b", xpos=43, ypos=187, xysize=(164, 161)),
    Solid("#224140", xpos=52, ypos=196, xysize=(31, 144)),
    Solid("#224140", xpos=167, ypos=196, xysize=(31, 144)),
    Solid("#dde2d0", xpos=108, ypos=202, xysize=(35, 118)),
    Solid("#c49c4f", xpos=121, ypos=208, xysize=(10, 100)),
    Solid("#b58b42", xpos=115, ypos=199, xysize=(22, 15)),
    Solid("#cbd4bd", xpos=91, ypos=202, xysize=(18, 23)),
    Solid("#cbd4bd", xpos=143, ypos=202, xysize=(18, 23)),
    Solid("#162b2b", xpos=25, ypos=202, xysize=(27, 129)),
    Solid("#162b2b", xpos=198, ypos=202, xysize=(27, 129)),
    Solid("#b57855", xpos=25, ypos=323, xysize=(27, 22)),
    Solid("#b57855", xpos=198, ypos=323, xysize=(27, 22)),

    # Cabeza, pelo y cuello: una silueta humana deliberadamente simple.
    Solid("#b57855", xpos=104, ypos=164, xysize=(39, 34)),
    Text("●", size=112, color="#b57855", xpos=69, ypos=59),
    # El pelo se construye con mechones, no con otro círculo sobre la cara.
    Solid("#25322b", xpos=72, ypos=81, xysize=(96, 28)),
    Solid("#25322b", xpos=69, ypos=101, xysize=(23, 35)),
    Solid("#25322b", xpos=148, ypos=101, xysize=(21, 30)),
    Solid("#8f5c43", xpos=93, ypos=137, xysize=(15, 7)),
    Solid("#8f5c43", xpos=143, ypos=137, xysize=(15, 7)),

    # Pañuelo de bolsillo: el mismo acento dorado de la escena.
    Solid("#c49c4f", xpos=171, ypos=235, xysize=(18, 11)),
    xysize=(250, 430),
)

# Dos bocas y una animación corta. El callback de bz selecciona esta imagen
# sólo durante sus líneas; al terminar, vuelve a la expresión neutral.
image bezout boca cerrada = LiveComposite(
    (250, 430),
    (0, 0), "bezout cuerpo",
    (117, 147), Solid("#653c35", xysize=(18, 4)),
)

image bezout boca abierta = LiveComposite(
    (250, 430),
    (0, 0), "bezout cuerpo",
    (119, 145), Solid("#653c35", xysize=(14, 9)),
)

image bezout neutral = "bezout boca cerrada"

image bezout hablando:
    "bezout boca cerrada"
    pause 0.10
    "bezout boca abierta"
    pause 0.10
    repeat

transform bezout_grande:
    # Un plano medio: más grande, con las piernas ocultas por el cuadro de diálogo
    # y desplazado un poco hacia el centro sin invadir la vista del jugador.
    xpos 0.92
    xanchor 1.0
    yalign 1.0
    zoom 1.55


init python:
    def foto_recortada_periodico(foto, ancho, alto):
        """Recorta una foto al marco sin deformarla ni dejar que se desborde."""
        borde = 3
        interior_ancho = ancho - borde * 2
        interior_alto = alto - borde * 2
        ancho_original, alto_original = renpy.image_size(foto)
        proporcion_foto = float(ancho_original) / alto_original
        proporcion_panel = float(interior_ancho) / interior_alto

        if proporcion_foto > proporcion_panel:
            ancho_recorte = int(alto_original * proporcion_panel)
            recorte = ((ancho_original - ancho_recorte) // 2, 0,
                       ancho_recorte, alto_original)
        else:
            alto_recorte = int(ancho_original / proporcion_panel)
            recorte = (0, (alto_original - alto_recorte) // 2,
                       ancho_original, alto_recorte)

        return Fixed(
            Transform(foto, crop=recorte, xpos=borde, ypos=borde,
                      xysize=(interior_ancho, interior_alto)),
            Solid("#4a4a46", xpos=0, ypos=0, xysize=(ancho, borde)),
            Solid("#4a4a46", xpos=0, ypos=alto - borde, xysize=(ancho, borde)),
            Solid("#4a4a46", xpos=0, ypos=0, xysize=(borde, alto)),
            Solid("#4a4a46", xpos=ancho - borde, ypos=0, xysize=(borde, alto)),
            xysize=(ancho, alto),
        )

    def periodico_con_titular(titular, foto):
        """Periódico final con titular y foto elegidos por las decisiones."""
        return Fixed(
            "periodico base",
            Transform(foto_recortada_periodico(foto, 720, 405), xpos=80, ypos=252),
            Transform(
                foto_recortada_periodico("images/puerto_maldonado.jpg", 330, 167),
                xpos=840,
                ypos=252,
            ),
            Text(
                titular,
                xpos=80,
                ypos=116,
                xmaximum=730,
                size=31,
                bold=True,
                color="#111111",
                line_spacing=-2,
            ),
            xysize=(1280, 720),
        )


# --- Story -------------------------------------------------------------------

label start:

    play music "audio/sounds.mp3"

    scene bg cuarto periodico with fade

    "Es un día nuevo."
    "Te levantas y revisas tu celular."
    "Te ha contactado Bezout, uno de tus socios más confiables."
    "Dice que tiene algo muy interesante que mostrarte, y que vayas ahora mismo a donde está ubicado en este momento."
    "Comienzas a alistarte."

    scene bg ventana with fade

    "Eres empresario en minería desde hace unos 10 años. El negocio nunca ha dejado de ser fructífero."
    "Aunque has gestionado sitios de extracción en otros lugares, estos últimos años has estado en Madre de Dios."
    "Ha mostrado ser la región más rentable, después de todo."
    "Sin embargo, todo lo que has logrado no ha sido exactamente gracias a trabajar siguiendo la ley."
    "Has tenido que pasar por alto una que otra regla en múltiples ocasiones."
    "\"Ilícito\" llamarían algunos al tipo de minería del que te encargas."
    "Conociste a Bezout allá por tus primeros años involucrados en minería."
    "Es empresario, como tú, y juntos han levantado múltiples operativos mineros aquí en la selva."
    "Es gracias a Bezout y sus contactos que has podido evadir la ley múltiples veces."
    "Por suerte, habías viajado hace poco a Madre de Dios para supervisar uno de los sitios que gestionas."

    scene bg cuarto periodico with fade

    "Te fijas en el periódico que trajiste el otro día."

    play sound "audio/newspaper.mp3"
    scene bg periodico with dissolve

    "..."
    "Es verdad, tus minas vienen causando estos efectos, y lo sabes desde hace muchos años."
    "Pero el negocio es extremadamente rentable."
    "\"Algún sacrificio se tiene que hacer\", piensas."

    scene bg cuarto periodico with fade

    "Sin mayor demora, terminas de alistarte y vas a donde Bezout."

    scene bg bosque with fade

    "Llegas a la ubicación que te envió Bezout."
    "Es un lugar con mucho bosque, cerca de un río. Según tu celular, es el río Tambopata."

    show bezout neutral at bezout_grande with dissolve

    bz "¡Hola, socio! Qué bueno encontrarte. ¿Cómo estás?"

    menu:
        "¿Qué le respondes?"

        "Todo bien por acá.":
            bz "Uy, qué bueno, socio. Veo que el negocio te ha estado tratando bien, ¿eh?"

        "Bien. ¡A los años!":
            bz "¡A los años, socio! Hace rato que no te veía."

    bz "Sabes, te contacté porque encontré este terreno que ves aquí. ¿Bonito, no?"
    bz "Nuestras mediciones han detectado que esta zona está llena de mineral nuevo para extraer. ¡Sería un excelente lugar para abrir un nuevo sitio de extracción!"
    bz "Veo un gran potencial. Estoy seguro de que este proyecto sería de mucho interés para nuestros socios y clientes."
    bz "Pero tú eres el jefe, mi estimado."

    "El proyecto te parece una gran oportunidad. ¿Decides iniciarlo?"

    menu:
        "¿Inicias el proyecto?"

        "Sí, iniciemos con el proyecto.":
            $ proyecto_iniciado = True
            jump proyecto_aceptado

        "No, no prosigamos.":
            $ proyecto_iniciado = False
            jump final_rechazo


label proyecto_aceptado:

    bz "¡Genial, socio! Vas a ver que esta operación va a dar muchos frutos."
    bz "Pero primero hay que decidir algunos temas. Ya sabes, cosas de la chamba."
    bz "Como puedes ver, la zona todavía no está muy preparada para el operativo."
    bz "Es buena idea que despejemos el área. Necesitamos que los carros y toda la maquinaria pasen fácil."

    "Lo que dice Bezout tiene sentido. ¿Programas el despeje de la zona para el operativo?"

    menu:
        "¿Despejas la zona?"

        "Sí, despejemos.":
            $ zona_despejada = True
            bz "¡Bien! Luego contacto a los otros chicos para el despeje."

        "No, no lo hagamos.":
            $ zona_despejada = False
            "Algo te hace pensar que despejar el área no es buena idea."
            bz "Uy, ¿cómo que no, socio? Bueno, podemos intentar no hacerlo esta vez…"

    "Bezout lo anota un momento en su celular."
    bz "¡Listo! poco a poco vamos avanzando."
    "Bezout guarda su celular y mira alrededor."
    bz "¿Qué te parece el lugar? Bastante bonito, ¿no?"
    bz "La verdad, cuando vine por primera vez, no esperaba encontrarme con un paisaje así."
    bz "Aunque bueno, ya sabes cómo es esto. No podemos quedarnos admirando el paisaje todo el día."
    bz "Hablando de trabajar, hay algo que todavía tenemos que definir. ¿Ya pensaste cómo vamos a separar el mineral del resto del material?"
    bz "Tenemos un par de alternativas para hacerlo. ¿Qué te parece si revisamos?"

    "El mercurio y el método gravimétrico son dos métodos de separar el oro en la extracción."
    "Históricamente, el mercurio te ha servido mucho mejor. El método gravimétrico, cuando lo has probado, ha producido resultados más lentos y mucho más caros."

    menu:
        "¿Qué método escoges?"

        "Usemos mercurio.":
            $ metodo_extraccion = "mercurio"
            $ uso_mercurio = True
            bz "Me parece bien, como siempre lo hemos trabajado."

        "Usemos el gravimétrico.":
            $ metodo_extraccion = "gravimetrico"
            $ uso_mercurio = False
            bz "¿Seguro? Nos costará mucho más, pero está bien."

    bz "Por último, pero no menos importante: el cierre de mina."
    bz "Los operativos no duran para siempre, ya sabes."
    bz "Siempre podemos gastar un poco en reparar y monitorear el área luego de que termine el proyecto."
    bz "En teoría, ayudaría a cuidar mejor lo que quede y nos podría ahorrar uno que otro problema con el Estado..."
    bz "...pero es un montón de chamba."

    "Es verdad, en tus proyectos nunca ha habido plan de cierre. De todas formas, nunca te ha causado problemas."

    menu:
        "¿Hacen un plan de cierre?"

        "Hagamos un plan de cierre.":
            $ plan_cierre = True
            bz "Saldrá caro, ojo. Pero podemos hacerlo."

        "Sin plan de cierre.":
            $ plan_cierre = False
            bz "Bien, será como siempre."

    bz "Bueno, socio, me parece que eso es lo más importante que había que decidir."
    bz "¡Este sitio será un éxito! Pronto llamo a todo el equipo a chambear."
    bz "Te avisaré para iniciar la gestión."
    bz "Un gusto hacer negocios, como siempre."

    hide bezout with dissolve

    "Te despides de Bezout."
    "Ha sido un encuentro muy fructífero, a tu parecer."
    "Vuelves a tu cuarto."

    scene bg cuarto with fade

    "Pese a todo, algo te tiene pensativo."
    "Meditas sobre lo que acaba de suceder."
    "¿Tomaste la decisión correcta?"
    "Solo tú puedes determinar eso."

    scene black with fade
    centered "Muchos años después…"

    scene bg cuarto periodico with fade
    play sound "audio/newspaper.mp3"

    if not plan_cierre:
        $ titular_final = "Puntos de minería ilegal abandonados quedan inhóspitos. Hectáreas de bosque perdidas."
        $ foto_final = "images/sitio_abandonado.jpg"
    elif zona_despejada and uso_mercurio:
        $ titular_final = "Hectáreas de bosque perdidas y derrames de mercurio por la minería ilegal."
        $ foto_final = "images/rio_contaminado.jpg"
    elif uso_mercurio:
        $ titular_final = "Derrames masivos de mercurio en Tambopata por la minería ilegal."
        $ foto_final = "images/rio_contaminado.jpg"
    elif zona_despejada:
        $ titular_final = "Cientas de hectáreas de bosque perdidas por la minería ilegal."
        $ foto_final = "images/tala.png"
    else:
        $ titular_final = "Bosques se ven afectados por avance de la minería ilegal."
        $ foto_final = "images/bosques_afectados.jpg"

    scene expression periodico_con_titular(titular_final, foto_final) with dissolve

    "..."

    scene expression paisaje_final(proyecto_iniciado, zona_despejada, uso_mercurio) with Fade(1.5, 0.5, 2.5)

    fin_juego "Fin del juego"

    stop music fadeout 1.0

    return


label final_rechazo:

    bz "¿En serio? Pero si los resultados son mejores de lo que esperábamos. No todos los días encontramos algo así."
    bz "Piénsalo un momento. Ya tenemos buena parte del trabajo hecho. ¿Por qué no dar el siguiente paso?"

    menu:
        "Tienes razón, deberíamos continuar.":
            $ proyecto_iniciado = True
            jump proyecto_aceptado

        "No creo que sea buena idea...":
            pass

    bz "Vamos, no seas tan pesimista. ¿Qué es lo que te hace dudar? Tenemos información favorable y una oportunidad que vale la pena explorar."
    bz "Además, si no nos atrevemos a intentarlo, nunca sabremos hasta dónde podríamos llegar."

    menu:
        "Está bien, tienes razón.":
            $ proyecto_iniciado = True
            jump proyecto_aceptado

        "Sigo pensando que no...":
            pass

    bz "¡Pero vamos! ¿Después de todo lo que hemos investigado, vamos a echarlo todo por la borda?"
    bz "Los resultados están ahí. Al menos deberíamos darle una oportunidad."
    bz "Y no olvides algo: si nosotros no actuamos, alguien más podría adelantarse."

    menu:
        "De acuerdo, hagamos la extracción.":
            $ proyecto_iniciado = True
            jump proyecto_aceptado

        "Mi respuesta sigue siendo no.":
            pass

    bz "¿Todavía no estás convencido? ¡No puedo creerlo! Te he mostrado los resultados, hemos revisado las posibilidades y seguimos teniendo una excelente oportunidad frente a nosotros."
    bz "Mira, no quiero presionarte, pero sería frustrante descubrir más adelante que dejamos escapar algo que pudo haber sido extraordinario."

    menu:
        "Está bien, hagámoslo.":
            $ proyecto_iniciado = True
            jump proyecto_aceptado

        "No. Definitivamente no.":
            pass

    "Bezout da un suspiro."

    bz "Bueno… parece que ya tomaste una decisión."
    bz "He intentado convencerte de todas las maneras posibles, pero veo que no hay forma de hacerte cambiar de opinión."
    bz "Está bien, no insistiré más."

    "Bezout escribe algo en su celular."

    bz "Veo que no tengo nada que hacer contigo, socio. Yo me iré retirando."

    hide bezout with dissolve

    "..."

    scene bg ventana with fade

    "Meditas sobre lo que acaba de suceder."
    "¿Tomaste la decisión correcta?"
    "Solo tú puedes determinar eso."

    scene expression paisaje_final(proyecto_iniciado, zona_despejada, uso_mercurio) with fade

    fin_juego "Fin del juego"

    stop music fadeout 1.0

    return
