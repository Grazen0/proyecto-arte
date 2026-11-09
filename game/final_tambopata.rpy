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
    # Árboles pequeños y copas entrelazadas al fondo de la ribera.
    Solid("#346e4d", xpos=21, ypos=338, xysize=(12, 112)),
    Text("●", size=74, color="#4a9667", xpos=-6, ypos=302),
    Solid("#346e4d", xpos=122, ypos=326, xysize=(11, 124)),
    Text("●", size=79, color="#438d5e", xpos=90, ypos=287),
    Solid("#346e4d", xpos=207, ypos=342, xysize=(11, 108)),
    Text("●", size=70, color="#4a9667", xpos=182, ypos=307),
    Solid("#346e4d", xpos=365, ypos=330, xysize=(12, 120)),
    Text("●", size=78, color="#438d5e", xpos=336, ypos=291),
    Solid("#346e4d", xpos=438, ypos=342, xysize=(11, 108)),
    Text("●", size=74, color="#4a9667", xpos=411, ypos=305),
    Solid("#346e4d", xpos=563, ypos=324, xysize=(11, 126)),
    Text("●", size=84, color="#438d5e", xpos=529, ypos=281),
    Solid("#346e4d", xpos=647, ypos=339, xysize=(12, 111)),
    Text("●", size=75, color="#4a9667", xpos=619, ypos=302),
    Solid("#346e4d", xpos=823, ypos=329, xysize=(11, 121)),
    Text("●", size=82, color="#438d5e", xpos=791, ypos=288),
    Solid("#346e4d", xpos=908, ypos=343, xysize=(12, 107)),
    Text("●", size=73, color="#4a9667", xpos=880, ypos=307),
    Solid("#346e4d", xpos=1082, ypos=333, xysize=(12, 117)),
    Text("●", size=80, color="#438d5e", xpos=1050, ypos=292),
    Solid("#346e4d", xpos=1241, ypos=338, xysize=(12, 112)),
    Text("●", size=76, color="#4a9667", xpos=1212, ypos=299),

    # Árboles grandes delante de la línea de vegetación.
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
    Text("●", size=98, color="#347c53", xpos=144, ypos=314),
    Text("●", size=91, color="#2d704d", xpos=373, ypos=308),
    Text("●", size=102, color="#347c53", xpos=580, ypos=303),
    Text("●", size=95, color="#2d704d", xpos=810, ypos=306),
    Text("●", size=103, color="#347c53", xpos=1053, ypos=303),
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
