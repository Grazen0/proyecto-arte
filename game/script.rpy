# The script of the game goes in this file.

# --- Characters --------------------------------------------------------------

define maya = Character("Maya", color="#e8a87c")
define leo = Character("Leo", color="#7cc7c0")

# Tracks which advice the player gave. Used in the ending.
default inspiration = 0


# --- Bare-minimum graphics ---------------------------------------------------
# Everything below is drawn from flat colored rectangles and text, so the demo
# needs no image assets at all.

image bg studio = Fixed(
    Solid("#241d2b"),
    Solid("#1a1420", xpos=0, ypos=560, xysize=(1280, 160)),
    Solid("#3a2f42", xpos=760, ypos=100, xysize=(440, 340)),
    Solid("#e9ddc6", xpos=778, ypos=118, xysize=(404, 304)),
    Solid("#e8a87c", xpos=810, ypos=300, xysize=(150, 46)),
    Solid("#7cc7c0", xpos=900, ypos=360, xysize=(90, 24)),
    Solid("#b06a5c", xpos=1030, ypos=200, xysize=(44, 44)),
)

image bg night = Fixed(
    Solid("#0d1422"),
    Text("\u25cf", size=220, color="#f4e7c3", xpos=900, ypos=40),
    Solid("#161f31", xpos=0, ypos=500, xysize=(1280, 220)),
    Solid("#1d2942", xpos=80, ypos=400, xysize=(120, 320)),
    Solid("#1d2942", xpos=260, ypos=460, xysize=(90, 260)),
    Solid("#1d2942", xpos=420, ypos=350, xysize=(140, 370)),
    Solid("#1d2942", xpos=760, ypos=430, xysize=(110, 290)),
)

image maya = Fixed(
    Solid("#e8a87c", xysize=(250, 430)),
    Text("M", size=190, color="#241d2b", xalign=0.5, yalign=0.5),
    xysize=(250, 430),
)

image leo = Fixed(
    Solid("#7cc7c0", xysize=(250, 430)),
    Text("L", size=190, color="#241d2b", xalign=0.5, yalign=0.5),
    xysize=(250, 430),
)


# --- The demo ----------------------------------------------------------------

label start:

    scene bg studio with fade

    "A small studio. A half-finished canvas. Two cups of cold coffee."

    show maya at left with dissolve

    maya "I've been staring at this canvas for three hours."
    maya "Every color looks wrong. Every line feels like an apology."

    "Maya steps back from the easel and looks at you."

    menu:
        "What do you tell her?"

        "Trust the first version.":
            $ inspiration += 1
            maya "The first version..."
            maya "You know, that one was messy. But it had teeth."

        "Take a break. The painting will wait.":
            $ inspiration += 2
            maya "Maybe you're right. The painting isn't going anywhere."
            "She sets down the brush."

    show leo at right with moveinright

    leo "Am I interrupting an art emergency?"
    maya "Yes. But a small one."
    leo "Good. Small emergencies are my specialty."

    hide maya with dissolve
    hide leo with dissolve

    scene bg night with fade

    "Later, the city turns the window into a second canvas."

    if inspiration >= 2:
        "Maya texts you a photo of the painting. She has added one bold, impossible color."
    else:
        "Maya texts you a photo of the painting. It is exactly the same, but she sounds lighter."

    "It's enough. For tonight, it's enough."

    centered "{size=+12}proyecto-arte{/size}\n\nA demo visual novel.\n\nThanks for playing."

    return
