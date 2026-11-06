# The script of the game goes in this file.

# --- Characters --------------------------------------------------------------

define bz = Character("Bezout", color="#d9a441")

# --- Story flags -------------------------------------------------------------
# These are here so later scenes can react to the player's decisions.

default proyecto_iniciado = False
default zona_despejada = False
default metodo_extraccion = None


# --- Placeholder graphics ----------------------------------------------------
# Flat colors and simple shapes. Replace these with real backgrounds and
# sprites later; the script does not depend on the art.

image bg cuarto = Fixed(
    Solid("#2a2530"),
    Solid("#1c1820", xpos=0, ypos=560, xysize=(1280, 160)),

    # Ventana con luz de mañana.
    Solid("#3a2f42", xpos=760, ypos=100, xysize=(360, 280)),
    Solid("#9fc7d9", xpos=778, ypos=118, xysize=(324, 244)),
    Text("\u25cf", size=100, color="#ffe9a8", xpos=980, ypos=130),

    # Cama.
    Solid("#4a3f52", xpos=70, ypos=380, xysize=(520, 260)),
    Solid("#e8dcc8", xpos=100, ypos=400, xysize=(180, 100)),
    Solid("#5d5068", xpos=70, ypos=520, xysize=(520, 40)),

    # Velador y celular.
    Solid("#3a2f42", xpos=620, ypos=470, xysize=(90, 90)),
    Solid("#e8a87c", xpos=635, ypos=430, xysize=(60, 40)),
    Solid("#1b1b22", xpos=640, ypos=395, xysize=(50, 35)),
)

image bg ventana = Fixed(
    Solid("#1f1a26"),

    # Marco de la ventana.
    Solid("#3a2f42", xpos=240, ypos=70, xysize=(800, 430)),

    # Bosque y río vistos desde adentro.
    Solid("#2e6b4a", xpos=260, ypos=90, xysize=(760, 390)),
    Solid("#1d4a33", xpos=260, ypos=330, xysize=(760, 150)),
    Solid("#3f8fa8", xpos=260, ypos=400, xysize=(760, 40)),
    Solid("#163b27", xpos=320, ypos=150, xysize=(50, 260)),
    Solid("#1b4a30", xpos=450, ypos=110, xysize=(60, 300)),
    Solid("#163b27", xpos=610, ypos=170, xysize=(45, 240)),
    Solid("#1b4a30", xpos=760, ypos=120, xysize=(70, 290)),
    Solid("#163b27", xpos=900, ypos=160, xysize=(55, 250)),

    # Cruz del marco.
    Solid("#3a2f42", xpos=630, ypos=90, xysize=(20, 390)),
    Solid("#3a2f42", xpos=260, ypos=270, xysize=(760, 20)),

    # Luz y borde inferior del interior.
    Text("\u25cf", size=90, color="#d8e8a8", xpos=850, ypos=130),
    Solid("#15111a", xpos=0, ypos=500, xysize=(1280, 220)),
)

image bg bosque = Fixed(
    Solid("#2f7a4a"),
    Solid("#1d4f32", xpos=0, ypos=0, xysize=(1280, 140)),

    # Árboles.
    Solid("#245c3b", xpos=50, ypos=130, xysize=(100, 300)),
    Solid("#1b4a30", xpos=200, ypos=90, xysize=(120, 340)),
    Solid("#245c3b", xpos=390, ypos=150, xysize=(85, 280)),
    Solid("#1b4a30", xpos=560, ypos=100, xysize=(110, 330)),
    Solid("#245c3b", xpos=760, ypos=140, xysize=(90, 290)),
    Solid("#1b4a30", xpos=930, ypos=80, xysize=(130, 350)),
    Solid("#245c3b", xpos=1130, ypos=150, xysize=(100, 280)),

    # Río Tambopata.
    Solid("#3f9bb5", xpos=0, ypos=430, xysize=(1280, 130)),
    Solid("#2f7f9e", xpos=0, ypos=470, xysize=(1280, 90)),
    Solid("#9fd4e0", xpos=120, ypos=500, xysize=(160, 8)),
    Solid("#9fd4e0", xpos=420, ypos=540, xysize=(220, 8)),
    Solid("#9fd4e0", xpos=820, ypos=490, xysize=(180, 8)),

    # Orilla cercana.
    Solid("#6b4b2f", xpos=0, ypos=560, xysize=(1280, 160)),
)

image bezout = Fixed(
    Solid("#d9a441", xysize=(250, 430)),
    Text("B", size=190, color="#2a2530", xalign=0.5, yalign=0.5),
    xysize=(250, 430),
)


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

    show bezout at right with dissolve

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
