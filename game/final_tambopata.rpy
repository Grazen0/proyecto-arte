# Una ribera inspirada en el Tambopata: río ancho que se aleja hacia el fondo,
# selva continua en la orilla opuesta y vegetación cercana a los lados.
# Todas las variantes comparten la misma geometría; no hay 2^n imágenes.

init -1 python:
    orillas_tambopata = (
        (0, 358, 545), (180, 372, 560), (400, 391, 554),
        (620, 405, 536), (850, 413, 511), (1040, 402, 485),
        (1280, 382, 460),
    )

    def bordes_tambopata(x):
        """Bordes del mismo cauce usados por el agua y los tocones."""
        for (x0, arriba0, abajo0), (x1, arriba1, abajo1) in zip(
                orillas_tambopata, orillas_tambopata[1:]):
            if x <= x1:
                avance = float(x - x0) / (x1 - x0)
                return (int(arriba0 + (arriba1 - arriba0) * avance),
                        int(abajo0 + (abajo1 - abajo0) * avance))
        return orillas_tambopata[-1][1:]

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

    def tocones_perspectiva():
        """Llena ambas márgenes: pequeños al fondo, grandes en primer plano."""
        import random

        azar = random.Random(841)
        posiciones = []
        for fila, y in enumerate((294, 316, 342, 373, 411,
                                  456, 506, 561, 621, 674)):
            distancia = float(y - 265) / 410
            ancho = 17 + int(25 * distancia)
            alto = 18 + int(30 * distancia)
            paso = int(ancho * 2.2) + 9
            for x in range((fila * 17) % paso, 1280, paso):
                # Variaciones reproducibles para evitar una cuadrícula regular.
                px = max(0, x + azar.randint(-paso // 4, paso // 4))
                py = y + azar.randint(-paso // 4, paso // 4)
                if px >= 1280 or py + alto >= 720:
                    continue
                arriba, abajo = bordes_tambopata(px)
                if py + alto < arriba - 5 or py > abajo + 8:
                    posiciones.append((px, py, ancho, alto))
        return tocones_ribera(posiciones)

    def cauce_hacia_izquierda(superficie, profundidad, reflejo):
        """Un mismo cauce lateral para la escena con Bezout y todos los finales."""
        partes = []
        for x in range(0, 1280, 8):
            arriba, abajo = bordes_tambopata(x)
            partes.append(Solid(superficie, xpos=x, ypos=arriba,
                                xysize=(8, abajo - arriba)))
            partes.append(Solid(profundidad, xpos=x, ypos=arriba + (abajo - arriba) // 2,
                                xysize=(8, (abajo - arriba + 1) // 2)))

        for x, largo, altura in ((106, 100, 0.30), (390, 90, 0.58),
                                  (700, 85, 0.35), (974, 70, 0.50)):
            arriba, abajo = bordes_tambopata(x)
            partes.append(Solid(reflejo, xpos=x,
                                ypos=arriba + int((abajo - arriba) * altura),
                                xysize=(largo, 3)))
        return Fixed(*partes, xysize=(1280, 720))

    def rastros_petroleo():
        """Manchas irregulares sobre el agua, sin tocar las orillas."""
        partes = []
        for x, altura, largo in (
                (72, 0.36, 38), (158, 0.67, 25), (255, 0.46, 46),
                (349, 0.29, 30), (435, 0.73, 27), (522, 0.41, 43),
                (613, 0.62, 35), (701, 0.35, 27), (792, 0.70, 40),
                (877, 0.43, 28), (960, 0.65, 37), (1044, 0.32, 32),
                (1129, 0.68, 24), (1204, 0.48, 33)):
            arriba, abajo = bordes_tambopata(x)
            y = arriba + int((abajo - arriba) * altura)
            # Bordes oscuros y manchas amarillentas de distintos tamaños.
            partes.append(Solid("#81734f", xpos=x - 5, ypos=y - 2,
                                xysize=(largo + 7, 8)))
            partes.append(Solid("#baa259", xpos=x, ypos=y,
                                xysize=(largo - 10, 4)))
            partes.append(Solid("#c8ae6e", xpos=x + 7, ypos=y - 3,
                                xysize=(max(8, largo // 3), 3)))
            partes.append(Solid("#9b8953", xpos=x + largo - 6, ypos=y + 5,
                                xysize=(max(9, largo // 2), 3)))
        return Fixed(*partes, xysize=(1280, 720))


image final terreno = Fixed(
    # Cielo y orilla desnuda. No contiene vegetación: sirve también para la tala.
    Solid("#71b3c0"),
    Solid("#86bdc4", xpos=0, ypos=160, xysize=(1280, 67)),
    Solid("#558870", xpos=0, ypos=227, xysize=(1280, 59)),
    Solid("#426e55", xpos=0, ypos=286, xysize=(1280, 72)),
    Solid("#917557", xpos=0, ypos=358, xysize=(1280, 362)),
    # El sol queda alto y parcialmente cubierto por las copas del fondo.
    Text("●", size=115, color="#e5d48d", xpos=701, ypos=44),
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

image bosque arboles altos = copas_ribera([
    # Estrato alto compartido por la escena con Bezout y el final sin tala.
    (-35, 157, 139, "#2b6c49"), (54, 138, 154, "#347c50"),
    (157, 163, 124, "#286746"), (251, 137, 161, "#3a8152"),
    (355, 168, 134, "#2e704b"), (442, 141, 156, "#347d50"),
    (552, 171, 123, "#286747"), (639, 199, 100, "#367b50"),
    (738, 206, 91, "#2c704b"), (838, 167, 129, "#398153"),
    (932, 141, 157, "#2b6e48"), (1042, 160, 140, "#367b50"),
    (1147, 137, 157, "#2c714c"), (1225, 166, 125, "#3a8152"),
], 395)

image bosque arboles orilla = copas_ribera([
    # Vegetación tupida hasta la margen; el cauce oculta su parte sumergida.
    (-15, 278, 94, "#296b49"), (52, 304, 81, "#347a50"),
    (114, 291, 95, "#245e42"), (181, 318, 83, "#398456"),
    (247, 298, 99, "#286c49"), (327, 312, 87, "#357c51"),
    (397, 289, 100, "#296b49"), (481, 313, 86, "#398456"),
    (551, 300, 101, "#245e42"), (633, 318, 87, "#347a50"),
    (704, 297, 94, "#296b49"), (784, 311, 84, "#398456"),
    (851, 294, 98, "#245e42"), (934, 317, 81, "#347a50"),
    (997, 296, 97, "#286c49"), (1074, 312, 83, "#398456"),
    (1143, 291, 99, "#245e42"), (1220, 307, 90, "#347a50"),
], 450, troncos=False)

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

image final tocones orilla = tocones_ribera([
    # Las copas adicionales de la escena con Bezout también dejan bases taladas.
    (15, 320, 23, 27), (82, 333, 22, 24),
    (151, 326, 24, 28), (220, 339, 21, 24),
    (289, 340, 23, 28), (357, 350, 22, 25),
    (427, 350, 23, 29), (497, 363, 20, 25),
    (568, 362, 22, 27), (638, 373, 21, 25),
    (708, 372, 23, 27), (777, 377, 20, 25),
    (846, 373, 23, 29), (915, 362, 22, 26),
    (984, 360, 21, 26), (1054, 351, 22, 28),
    (1124, 346, 23, 27), (1194, 336, 20, 27),
])

image final tocones cerca = tocones_ribera([
    # Bases en la margen cercana del nuevo cauce, no sobre el agua.
    (20, 565, 40, 42), (60, 590, 33, 40), (110, 570, 36, 43),
    (150, 603, 38, 32), (220, 580, 32, 41), (280, 599, 30, 31),
    (340, 578, 34, 37), (395, 604, 29, 27), (460, 572, 31, 39),
    (525, 589, 32, 35), (590, 562, 27, 38), (650, 582, 28, 35),
    (720, 550, 27, 35), (780, 574, 25, 32), (840, 540, 24, 34),
    (900, 565, 23, 32), (960, 525, 22, 38), (1020, 557, 20, 34),
    (1080, 510, 19, 36), (1140, 542, 18, 34),
    (1190, 493, 22, 40), (1240, 524, 24, 32), (1260, 480, 17, 26),
])

image final tocones dispersos = tocones_perspectiva()

image final rio limpio = cauce_hacia_izquierda("#4a9bae", "#337e97", "#a2d2cf")
image final rio contaminado = Fixed(
    cauce_hacia_izquierda("#327b9c", "#2a5d80", "#73a0ac"),
    rastros_petroleo(),
    xysize=(1280, 720),
)
image bosque rio izquierda = "final rio limpio"

image final orilla = Fixed(
    # La ribera más cercana enmarca el agua sin ocultar su amplitud.
    Solid("#554532", xpos=0, ypos=641, xysize=(1280, 79)),
    Solid("#826a4c", xpos=0, ypos=635, xysize=(1280, 8)),
    xysize=(1280, 720),
)

image bg bosque = Fixed(
    "final terreno", "bosque arboles altos", "final arboles fondo",
    "bosque arboles orilla", "bosque rio izquierda",
    "final orilla", "final arboles cerca", xysize=(1280, 720),
)


init python:
    def paisaje_final(proyecto, despeje, mercurio):
        """Compone la ribera; cada decisión dañina resta saturación."""
        if not proyecto:
            despeje = mercurio = False

        capas = ["final terreno"]
        if despeje:
            capas.extend(("final tocones fondo", "final tocones orilla"))
        else:
            capas.extend(("bosque arboles altos", "final arboles fondo",
                          "bosque arboles orilla"))
        capas.append("final rio contaminado" if mercurio else "final rio limpio")
        capas.append("final orilla")
        if despeje:
            capas.extend(("final tocones cerca", "final tocones dispersos"))
        else:
            capas.append("final arboles cerca")

        imagen = Fixed(*capas, xysize=(1280, 720))
        if not proyecto:
            return imagen  # Rechazo definitivo: paisaje intacto, a todo color.

        danos = int(despeje) + int(mercurio)
        # Futuras consecuencias pueden seguir quitando color sin límite brusco.
        saturacion = 0.82 * (0.70 ** danos)
        return Transform(
            imagen,
            matrixcolor=TintMatrix("#f0e2d0") * SaturationMatrix(saturacion),
        )
