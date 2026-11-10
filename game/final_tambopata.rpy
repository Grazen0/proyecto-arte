# Una ribera inspirada en el Tambopata: río ancho que se aleja hacia el fondo,
# selva continua en la orilla opuesta y vegetación cercana a los lados.
# Todas las variantes comparten la misma geometría; no hay 2^n imágenes.

init -1 python:
    def copas_ribera(puntos, base, troncos=True):
        """Dibuja árboles superpuestos con alturas, tamaños y tonos variados."""
        partes = []
        for indice, (x, y, tamano, color) in enumerate(puntos):
            if troncos:
                inicio_tronco = y + tamano // 2
                partes.append(Solid("#1e4a38", xpos=x + tamano // 3,
                                    ypos=inicio_tronco,
                                    xysize=(max(9, tamano // 7),
                                            max(1, base - inicio_tronco))))
            # Variar el borde de cada copa evita una hilera de círculos idénticos.
            if indice % 3 == 0:
                partes.append(Text("●", size=tamano * 2 // 3, color=color,
                                   xpos=x - tamano // 4, ypos=y + tamano // 5))
            partes.append(Text("●", size=tamano, color=color, xpos=x, ypos=y))
            if indice % 2 == 0:
                partes.append(Text("●", size=tamano * 3 // 5, color=color,
                                   xpos=x + tamano // 2, ypos=y + tamano // 4))
        return Fixed(*partes, xysize=(1280, 720))

    def tocones_ribera(puntos):
        """Cada base conserva su corte claro y una sombra lateral."""
        partes = []
        for x, y, ancho, alto in puntos:
            partes.append(Solid("#604b38", xpos=x, ypos=y,
                                xysize=(ancho, alto)))
            partes.append(Solid("#503f32", xpos=x + ancho - 4, ypos=y + 5,
                                xysize=(4, alto - 5)))
            partes.append(Solid("#aa906b", xpos=x - 3, ypos=y - 3,
                                xysize=(ancho + 6, 7)))
        return Fixed(*partes, xysize=(1280, 720))

    def cauce_tambopata(superficie, profundidad, reflejo):
        """Un solo cauce en perspectiva para el agua limpia y la contaminada."""
        bordes = (
            (272, 948, 1190), (310, 838, 1225), (360, 688, 1255),
            (425, 437, 1280), (490, 142, 1280), (555, 0, 1280),
            (720, 0, 1280),
        )

        def limites(y):
            for (y0, izq0, der0), (y1, izq1, der1) in zip(bordes, bordes[1:]):
                if y <= y1:
                    avance = float(y - y0) / (y1 - y0)
                    return (int(izq0 + (izq1 - izq0) * avance),
                            int(der0 + (der1 - der0) * avance))
            return (0, 1280)

        partes = []
        for y in range(272, 720, 4):
            izq, der = limites(y)
            partes.append(Solid(superficie if y < 430 else profundidad,
                                xpos=izq, ypos=y, xysize=(der - izq, 4)))

        # Reflejos breves y separados, como los claros sobre agua en movimiento.
        for x, y, largo in ((812, 307, 77), (725, 343, 120),
                            (615, 390, 85), (445, 445, 155),
                            (250, 493, 105), (720, 481, 180),
                            (980, 530, 120), (85, 555, 170)):
            partes.append(Solid(reflejo, xpos=x, ypos=y, xysize=(largo, 4)))
        return Fixed(*partes, xysize=(1280, 720))


image final terreno = Fixed(
    # Cielo y orilla desnuda. No contiene vegetación: sirve también para la tala.
    Solid("#71b3c0"),
    Solid("#86bdc4", xpos=0, ypos=160, xysize=(1280, 67)),
    Solid("#558870", xpos=0, ypos=227, xysize=(1280, 59)),
    Solid("#426e55", xpos=0, ypos=286, xysize=(1280, 72)),
    Solid("#917557", xpos=0, ypos=358, xysize=(1280, 362)),
    # El sol queda alto y parcialmente cubierto por las copas del fondo.
    Text("●", size=115, color="#e5d48d", xpos=701, ypos=144),
    # Nubes claras y desiguales, sin tapar la línea del bosque.
    Text("●", size=68, color="#e4e9dd", xpos=177, ypos=54),
    Text("●", size=91, color="#e4e9dd", xpos=204, ypos=27),
    Text("●", size=61, color="#e4e9dd", xpos=258, ypos=63),
    Text("●", size=62, color="#dae6e0", xpos=763, ypos=72),
    Text("●", size=77, color="#dae6e0", xpos=799, ypos=48),
    Text("●", size=55, color="#dae6e0", xpos=850, ypos=78),
    xysize=(1280, 720),
)

image final arboles fondo = copas_ribera([
    (-32, 207, 108, "#35774c"), (7, 189, 98, "#448758"),
    (55, 206, 113, "#286847"), (98, 179, 121, "#3d8153"),
    (149, 203, 97, "#286847"), (186, 188, 108, "#36764c"),
    (228, 172, 131, "#2e7048"), (277, 199, 101, "#448758"),
    (315, 184, 115, "#32744c"), (365, 208, 104, "#266443"),
    (408, 182, 119, "#448758"), (460, 198, 105, "#2e7048"),
    (503, 173, 134, "#367b4e"), (556, 206, 102, "#296947"),
    (599, 192, 113, "#438357"), (649, 206, 104, "#32744c"),
    (687, 182, 121, "#266443"), (744, 209, 102, "#3b8053"),
    (787, 187, 109, "#296947"), (835, 206, 100, "#438357"),
    (873, 185, 107, "#32744c"), (927, 205, 99, "#296947"),
    (974, 198, 92, "#367b4e"), (1021, 205, 88, "#266443"),
    (1064, 207, 83, "#438357"), (1112, 210, 80, "#32744c"),
    (1161, 207, 77, "#296947"), (1205, 210, 80, "#438357"),
    (1246, 204, 84, "#286847"),
], 335)

image final arboles cerca = copas_ribera([
    # Vegetación cercana en las esquinas, dejando el centro libre para el río.
    (-58, 338, 209, "#245f41"), (30, 365, 143, "#2c7049"),
    (93, 415, 116, "#367b50"), (-44, 490, 149, "#357b51"),
    (1120, 322, 149, "#245f41"), (1187, 347, 185, "#2e704b"),
    (1079, 410, 117, "#397f54"), (1231, 481, 147, "#245f41"),
], 630, troncos=False)

image final tocones fondo = tocones_ribera([
    # Una base por cada árbol del fondo; tamaños irregulares, como la selva.
    (10, 259, 19, 23), (55, 252, 17, 28), (100, 263, 21, 24),
    (145, 255, 18, 26), (190, 262, 20, 25), (235, 250, 22, 29),
    (280, 260, 17, 23), (325, 253, 21, 27), (370, 265, 18, 21),
    (415, 254, 20, 27), (460, 261, 19, 23), (505, 250, 23, 30),
    (550, 262, 18, 23), (595, 254, 20, 27), (640, 264, 18, 22),
    (685, 252, 21, 28), (730, 260, 19, 24), (775, 255, 20, 25),
    (820, 263, 18, 22), (865, 251, 21, 28), (910, 260, 19, 24),
    (955, 254, 18, 26), (1000, 263, 20, 23), (1045, 256, 18, 26),
    (1090, 263, 19, 22), (1135, 253, 20, 27), (1180, 261, 18, 24),
    (1225, 255, 19, 26), (1260, 261, 18, 23),
])

image final tocones cerca = tocones_ribera([
    # Más troncos en la orilla cercana; ninguno nace dentro del agua.
    (20, 495, 40, 45), (55, 475, 33, 41), (90, 455, 36, 43),
    (130, 480, 38, 46), (170, 443, 32, 38), (205, 455, 30, 39),
    (239, 427, 34, 38), (273, 415, 29, 36), (310, 403, 31, 39),
    (349, 389, 32, 38), (388, 377, 27, 35), (430, 364, 28, 34),
    (470, 350, 27, 33), (515, 341, 25, 31), (557, 329, 24, 30),
    (603, 320, 23, 28), (645, 310, 22, 26), (686, 299, 20, 25),
    (730, 289, 19, 23), (768, 279, 18, 21),
    (1236, 299, 25, 30), (1255, 338, 24, 34), (1263, 362, 17, 29),
])

image final rio limpio = cauce_tambopata("#4a9bae", "#337e97", "#a2d2cf")
image final rio contaminado = cauce_tambopata("#464743", "#303432", "#787b72")

image final orilla = Fixed(
    # La ribera más cercana enmarca el agua sin ocultar su amplitud.
    Solid("#554532", xpos=0, ypos=641, xysize=(1280, 79)),
    Solid("#826a4c", xpos=0, ypos=635, xysize=(1280, 8)),
    xysize=(1280, 720),
)

image bg bosque = Fixed(
    "final terreno", "final arboles fondo", "final rio limpio",
    "final orilla", "final arboles cerca", xysize=(1280, 720),
)


init python:
    def paisaje_final(proyecto, despeje, mercurio):
        """Compone la ribera; cada decisión dañina resta saturación."""
        if not proyecto:
            despeje = mercurio = False

        capas = ["final terreno"]
        capas.append("final tocones fondo" if despeje else "final arboles fondo")
        if despeje:
            # El agua tapa los tocones que llegan al borde: ninguno flota.
            capas.append("final tocones cerca")
        capas.append("final rio contaminado" if mercurio else "final rio limpio")
        capas.append("final orilla")
        if not despeje:
            capas.append("final arboles cerca")

        imagen = Fixed(*capas, xysize=(1280, 720))
        if not proyecto:
            return imagen  # Rechazo definitivo: paisaje intacto, a todo color.

        danos = int(despeje) + int(mercurio)
        # Futuras consecuencias pueden seguir quitando color sin límite brusco.
        saturacion = 0.72 * (0.57 ** danos)
        return Transform(
            imagen,
            matrixcolor=TintMatrix("#f0e2d0") * SaturationMatrix(saturacion),
        )
