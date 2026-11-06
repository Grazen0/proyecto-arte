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

# --- Story flags -------------------------------------------------------------
# These are here so later scenes can react to the player's decisions.

default proyecto_iniciado = False
default zona_despejada = False
default metodo_extraccion = None


# --- Minimalist artwork ------------------------------------------------------
# A shared palette keeps the room, travel view, forest, and character cohesive:
# deep jungle greens, blue-green water, warm wood, and a muted gold accent.

image bg cuarto = Fixed(
    # Habitación: pared, zócalo y piso de madera oscura.
    Solid("#18382d"),
    Solid("#245344", xpos=0, ypos=0, xysize=(1280, 88)),
    Solid("#10261f", xpos=0, ypos=510, xysize=(1280, 210)),
    Solid("#0b1a16", xpos=0, ypos=560, xysize=(1280, 160)),
    Solid("#315f4d", xpos=0, ypos=505, xysize=(1280, 8)),

    # Ventana: cielo, sol, cerros y una línea de árboles.
    Solid("#805e3d", xpos=754, ypos=76, xysize=(392, 314)),
    Solid("#102c27", xpos=766, ypos=88, xysize=(368, 290)),
    Solid("#78a99d", xpos=780, ypos=102, xysize=(340, 262)),
    Text("●", size=84, color="#ead77c", xpos=995, ypos=120),
    Solid("#5f9a76", xpos=780, ypos=255, xysize=(340, 109)),
    Solid("#347154", xpos=780, ypos=290, xysize=(340, 74)),
    Solid("#1d4b38", xpos=803, ypos=202, xysize=(22, 162)),
    Solid("#1d4b38", xpos=875, ypos=230, xysize=(28, 134)),
    Solid("#1d4b38", xpos=1050, ypos=210, xysize=(25, 154)),
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

image bg ventana = Fixed(
    # Interior de vehículo/cabaña durante el trayecto.
    Solid("#10251f"),
    Solid("#17362c", xpos=0, ypos=0, xysize=(1280, 82)),
    Solid("#0a1713", xpos=0, ypos=512, xysize=(1280, 208)),

    # Gran ventana panorámica hacia el bosque.
    Solid("#735237", xpos=196, ypos=55, xysize=(888, 472)),
    Solid("#0b1c18", xpos=214, ypos=73, xysize=(852, 436)),
    Solid("#86b5a6", xpos=230, ypos=89, xysize=(820, 404)),
    Text("●", size=104, color="#e7d67f", xpos=822, ypos=112),
    Solid("#78a879", xpos=230, ypos=255, xysize=(820, 238)),
    Solid("#4c8662", xpos=230, ypos=304, xysize=(820, 189)),
    Solid("#2c674a", xpos=230, ypos=356, xysize=(820, 137)),
    Solid("#4d9bad", xpos=230, ypos=423, xysize=(820, 70)),
    Solid("#3e8498", xpos=230, ypos=461, xysize=(820, 32)),

    # Árboles en diferentes planos para dar profundidad.
    Solid("#285c43", xpos=282, ypos=184, xysize=(29, 239)),
    Text("●", size=116, color="#397957", xpos=240, ypos=130),
    Solid("#285c43", xpos=456, ypos=211, xysize=(25, 212)),
    Text("●", size=94, color="#397957", xpos=423, ypos=156),
    Solid("#214d39", xpos=630, ypos=156, xysize=(34, 268)),
    Text("●", size=132, color="#2f6c4e", xpos=582, ypos=92),
    Solid("#214d39", xpos=908, ypos=185, xysize=(30, 239)),
    Text("●", size=118, color="#2f6c4e", xpos=868, ypos=120),
    Solid("#735237", xpos=628, ypos=73, xysize=(17, 420)),
    Solid("#735237", xpos=230, ypos=286, xysize=(820, 16)),

    # Reflejos sobre el agua, tablero y asiento en primer plano.
    Solid("#afd3c9", xpos=395, ypos=447, xysize=(130, 5)),
    Solid("#afd3c9", xpos=715, ypos=468, xysize=(180, 5)),
    Solid("#243f35", xpos=0, ypos=500, xysize=(1280, 54)),
    Solid("#0d1d18", xpos=0, ypos=552, xysize=(1280, 168)),
    Solid("#1d4034", xpos=70, ypos=470, xysize=(180, 140)),
    Solid("#285243", xpos=88, ypos=490, xysize=(145, 96)),
)

image bg bosque = Fixed(
    # Cielo de selva, copa de árboles y vegetación a distintas distancias.
    Solid("#6fa590"),
    # Solid("#2d6d4d", xpos=0, ypos=104, xysize=(1280, 360)),
    Solid("#22583f", xpos=0, ypos=190, xysize=(1280, 275)),
    Solid("#173e30", xpos=0, ypos=330, xysize=(1280, 155)),
    # Sol alto, al fondo y entre claros de la copa de los árboles.
    Text("●", size=162, color="#e2d77b", xpos=327, ypos=-38),

    # Árboles lejanos y follaje en capas.
    Solid("#1b4a36", xpos=78, ypos=112, xysize=(34, 355)),
    Text("●", size=160, color="#2e7550", xpos=6, ypos=55),
    Text("●", size=130, color="#367e58", xpos=102, ypos=88),
    Solid("#1b4a36", xpos=290, ypos=160, xysize=(30, 307)),
    Text("●", size=140, color="#2c704f", xpos=220, ypos=88),
    Solid("#1b4a36", xpos=520, ypos=125, xysize=(37, 342)),
    Text("●", size=180, color="#286847", xpos=436, ypos=35),
    Solid("#173e30", xpos=770, ypos=151, xysize=(39, 316)),
    Text("●", size=170, color="#245f43", xpos=688, ypos=65),
    Solid("#173e30", xpos=1027, ypos=105, xysize=(45, 362)),
    Text("●", size=195, color="#245f43", xpos=932, ypos=10),
    Solid("#173e30", xpos=1191, ypos=174, xysize=(34, 293)),
    Text("●", size=150, color="#2b704d", xpos=1120, ypos=98),

    # Río Tambopata y reflejos suaves.
    Solid("#4d9bad", xpos=0, ypos=448, xysize=(1280, 126)),
    Solid("#3e8498", xpos=0, ypos=505, xysize=(1280, 69)),
    Solid("#b5d8ca", xpos=90, ypos=475, xysize=(166, 7)),
    Solid("#b5d8ca", xpos=370, ypos=528, xysize=(214, 7)),
    Solid("#b5d8ca", xpos=785, ypos=470, xysize=(190, 7)),
    Solid("#b5d8ca", xpos=1060, ypos=535, xysize=(130, 7)),

    # Orilla, rocas, hojas cercanas y luciérnagas.
    Solid("#553d2c", xpos=0, ypos=574, xysize=(1280, 146)),
    Solid("#365f3e", xpos=0, ypos=562, xysize=(1280, 22)),
    Solid("#806347", xpos=270, ypos=543, xysize=(92, 31)),
    Solid("#806347", xpos=940, ypos=536, xysize=(124, 38)),
    Text("●", size=42, color="#75a965", xpos=34, ypos=507),
    Text("●", size=54, color="#4f9258", xpos=112, ypos=520),
    Text("●", size=50, color="#4f9258", xpos=1150, ypos=503),
    Text("•", size=30, color="#e8dc85", xpos=410, ypos=391),
    Text("•", size=24, color="#e8dc85", xpos=700, ypos=432),
    Text("•", size=28, color="#e8dc85", xpos=1090, ypos=365),
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


# --- Story -------------------------------------------------------------------

label start:

    scene bg cuarto with fade

    "Es un día nuevo."
    "Te levantas y revisas tu celular."
    "Te ha contactado Bezout, uno de tus socios más confiables."
    "Dice que tiene algo muy interesante que mostrarte, y que vayas ahora mismo a donde está ubicado en este momento."
    "Comienzas a alistarte."

    scene bg ventana with fade

    "Eres empresario en minería desde hace unos 10 años. El negocio nunca ha dejado de ser fructífero."
    "Aunque has gestionado sitios de extracción en otros lugares, estos últimos años has estado en Madre de Dios. Ha mostrado ser la región más rentable, después de todo."
    "Sin embargo, todo lo que has logrado no ha sido exactamente gracias a trabajar junto al Estado. Has tenido que pasar por alto una que otra regla en múltiples ocasiones."
    "«Ilícito» llamarían algunos al tipo de minería del que te encargas, pero «así es la vida» sueles decir."
    "Conociste a Bezout en tus primeros años en la minería. Es empresario, como tú."
    "Por suerte, habías viajado hace poco a Madre de Dios para supervisar uno de los sitios que gestionas."
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

    bz "Ahora, otra cosa en la lista: el proceso de extracción. ¿Usaremos mercurio, o el gravimétrico?"
    bz "Es importante eso. De mi experiencia, es de lo que más determina el beneficio que sacaremos del proyecto."

    "El mercurio y el método gravimétrico son dos métodos de separar el oro en la extracción."
    "Históricamente, el mercurio te ha servido mucho mejor. El método gravimétrico, cuando lo has probado, ha producido resultados más lentos y mucho más caros."

    menu:
        "¿Qué método escoges?"

        "Usemos mercurio.":
            $ metodo_extraccion = "mercurio"
            bz "Me parece bien, como siempre lo hemos trabajado."

        "Usemos el gravimétrico.":
            $ metodo_extraccion = "gravimetrico"
            bz "¿Seguro? Nos costará mucho más, pero está bien."

    jump continuara


label final_rechazo:

    bz "..."
    bz "¿En serio, socio? Bueno. Tú mandas."
    "Bezout guarda el celular y contempla el terreno en silencio."
    "Decides volver al campamento. El proyecto no se lleva a cabo."

    hide bezout with dissolve

    centered "{size=+16}Fin{/size}\n\nRechazaste el proyecto."

    return


label continuara:

    hide bezout with dissolve

    centered "{size=+16}Continuará…{/size}\n\nFin de la demo."

    return
