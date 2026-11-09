# El final se compone por capas para que nuevas decisiones puedan añadir
# consecuencias visuales sin crear una imagen por cada combinación.

image final terreno = Fixed(
    # Cielo, lomas y ribera desnuda; no hay árboles en esta capa.
    Solid("#83b9aa"),
    Solid("#acd4bb", xpos=0, ypos=155, xysize=(1280, 155)),
    Solid("#6da779", xpos=0, ypos=257, xysize=(1280, 100)),
    Solid("#568966", xpos=0, ypos=335, xysize=(1280, 114)),
    Text("●", size=120, color="#e5db85", xpos=932, ypos=54),
    Solid("#947455", xpos=0, ypos=426, xysize=(1280, 24)),
    xysize=(1280, 720),
)

image final arboles = Fixed(
    # Selva intacta en ambas orillas. Esta capa desaparece si se tala.
    Solid("#20533d", xpos=65, ypos=250, xysize=(28, 200)),
    Text("●", size=172, color="#317b51", xpos=0, ypos=177),
    Text("●", size=130, color="#3d8e5c", xpos=80, ypos=220),
    Solid("#20533d", xpos=286, ypos=242, xysize=(30, 208)),
    Text("●", size=164, color="#2e7550", xpos=215, ypos=158),
    Solid("#214d39", xpos=494, ypos=249, xysize=(33, 201)),
    Text("●", size=153, color="#398357", xpos=427, ypos=175),
    Solid("#214d39", xpos=747, ypos=240, xysize=(33, 210)),
    Text("●", size=171, color="#286b4a", xpos=677, ypos=147),
    Solid("#214d39", xpos=996, ypos=252, xysize=(35, 198)),
    Text("●", size=180, color="#317b51", xpos=918, ypos=166),
    Solid("#20533d", xpos=1183, ypos=257, xysize=(30, 193)),
    Text("●", size=146, color="#398357", xpos=1115, ypos=190),
    xysize=(1280, 720),
)

image final tocones = Fixed(
    # Solo quedan las bases de los troncos: no se reutiliza la capa de árboles.
    Solid("#6d503a", xpos=70, ypos=403, xysize=(37, 46)),
    Solid("#b1956b", xpos=65, ypos=401, xysize=(47, 9)),
    Solid("#6d503a", xpos=279, ypos=413, xysize=(43, 36)),
    Solid("#b1956b", xpos=274, ypos=410, xysize=(53, 9)),
    Solid("#6d503a", xpos=488, ypos=406, xysize=(40, 43)),
    Solid("#b1956b", xpos=483, ypos=403, xysize=(50, 9)),
    Solid("#6d503a", xpos=742, ypos=413, xysize=(43, 36)),
    Solid("#b1956b", xpos=737, ypos=410, xysize=(53, 9)),
    Solid("#6d503a", xpos=985, ypos=405, xysize=(45, 44)),
    Solid("#b1956b", xpos=980, ypos=402, xysize=(55, 9)),
    Solid("#6d503a", xpos=1177, ypos=414, xysize=(38, 35)),
    Solid("#b1956b", xpos=1172, ypos=411, xysize=(48, 9)),
    xysize=(1280, 720),
)

image final rio limpio = Fixed(
    Solid("#4c9eb0", xpos=0, ypos=450, xysize=(1280, 124)),
    Solid("#3d889d", xpos=0, ypos=518, xysize=(1280, 56)),
    Solid("#b8ded0", xpos=90, ypos=477, xysize=(160, 6)),
    Solid("#b8ded0", xpos=378, ypos=535, xysize=(205, 6)),
    Solid("#b8ded0", xpos=782, ypos=475, xysize=(200, 6)),
    Solid("#b8ded0", xpos=1060, ypos=531, xysize=(145, 6)),
    xysize=(1280, 720),
)

image final rio contaminado = Fixed(
    # Agua opaca y decolorada; sustituye por completo el río limpio.
    Solid("#363d3b", xpos=0, ypos=450, xysize=(1280, 124)),
    Solid("#303433", xpos=0, ypos=518, xysize=(1280, 56)),
    Solid("#69706a", xpos=90, ypos=477, xysize=(160, 5)),
    Solid("#69706a", xpos=378, ypos=535, xysize=(205, 5)),
    Solid("#69706a", xpos=782, ypos=475, xysize=(200, 5)),
    Solid("#69706a", xpos=1060, ypos=531, xysize=(145, 5)),
    xysize=(1280, 720),
)

image final orilla = Fixed(
    Solid("#5c4934", xpos=0, ypos=574, xysize=(1280, 146)),
    Solid("#547d4d", xpos=0, ypos=574, xysize=(1280, 18)),
    Solid("#856c4d", xpos=285, ypos=554, xysize=(86, 20)),
    Solid("#856c4d", xpos=953, ypos=548, xysize=(110, 26)),
    xysize=(1280, 720),
)

init python:
    def paisaje_final(proyecto, despeje, mercurio):
        """Compone la ribera; cada decisión dañina resta saturación."""
        if not proyecto:
            despeje = mercurio = False

        capas = ["final terreno"]
        capas.append("final tocones" if despeje else "final arboles")
        capas.append("final rio contaminado" if mercurio else "final rio limpio")
        capas.append("final orilla")

        imagen = Fixed(*capas, xysize=(1280, 720))
        if not proyecto:
            return imagen  # Rechazo definitivo: paisaje intacto, a todo color.

        danos = int(despeje) + int(mercurio)
        # La progresión no se agota con estas dos decisiones: futuras
        # consecuencias pueden seguir quitando color sin un límite brusco.
        saturacion = 0.72 * (0.57 ** danos)
        return Transform(
            imagen,
            matrixcolor=TintMatrix("#f0e2d0") * SaturationMatrix(saturacion),
        )
