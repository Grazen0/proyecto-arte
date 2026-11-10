"""Generate the flat-color aerial Tambopata illustration used by the main menu.

Run with `python3 tools/generate_title_river.py` (requires NumPy). The reference
is used for its broad river and dense forest, not embedded in the game.
"""

from pathlib import Path
import struct
import zlib

import numpy as np


WIDTH, HEIGHT = 1280, 720
OUTPUT = Path(__file__).resolve().parents[1] / "game/images/title_river.png"
rng = np.random.default_rng(2109)
rows, columns = np.mgrid[0:HEIGHT, 0:WIDTH]

# Dense dark canopy, with a little variation in its green rather than a flat fill.
grain = rng.normal(0, 3.0, (HEIGHT, WIDTH))
light = 7 * np.sin(columns / 160 + rows / 175)
canvas = np.empty((HEIGHT, WIDTH, 3), dtype=np.float32)
for channel, base in enumerate((13, 55, 43)):
    canvas[:, :, channel] = base + grain + light * (0.65 if channel == 0 else 1)


def oval(cx, cy, rx, ry, color):
    """Paint one overlapping, slightly shaded canopy viewed from above."""
    left, right = max(0, cx - rx), min(WIDTH, cx + rx + 1)
    top, bottom = max(0, cy - ry), min(HEIGHT, cy + ry + 1)
    if left >= right or top >= bottom:
        return
    yy, xx = np.mgrid[top:bottom, left:right]
    normalized = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
    mask = normalized <= 1
    highlight = (cx - xx) * 0.09 + (cy - yy) * 0.13
    shade = np.clip(highlight, -9, 11) - normalized * 7
    patch = canvas[top:bottom, left:right]
    patch[mask] = np.asarray(color) + shade[mask, None]


# Larger interlocking tree crowns: varied emerald, olive and blue-green tones.
palette = [
    (23, 74, 50), (30, 86, 57), (42, 103, 67), (27, 91, 72),
    (54, 107, 65), (30, 70, 55), (65, 116, 70), (42, 96, 70),
]
for _ in range(1550):
    x = int(rng.integers(-30, WIDTH + 30))
    y = int(rng.integers(-30, HEIGHT + 30))
    radius = int(rng.integers(13, 39))
    oval(x, y, radius, int(radius * rng.uniform(0.65, 1.1)), palette[rng.integers(len(palette))])

# Smaller leaf clusters close gaps and break the circular outlines.
for _ in range(2300):
    x = int(rng.integers(-15, WIDTH + 15))
    y = int(rng.integers(-15, HEIGHT + 15))
    radius = int(rng.integers(3, 11))
    oval(x, y, radius, radius, palette[rng.integers(len(palette))])

# A single S-shaped river: narrow upstream, wide downstream. Its banks are
# irregular, so it reads as an aerial view rather than a straight canal.
center = 770 - 0.24 * rows + 135 * np.sin((rows - 85) / 150) + 45 * np.sin(rows / 55)
half_width = 105 + rows * 0.135 + 7 * np.sin(rows / 35)
bank_roughness = 6 * np.sin(rows / 15) + 3 * np.sin(rows / 6)
distance = np.abs(columns - center)
bank = (distance < half_width + 15 + bank_roughness) & (distance >= half_width)
canvas[bank] = (133, 110, 71)
shore = (distance < half_width + 7) & (distance >= half_width - 4)
canvas[shore] = (76, 112, 91)

water = distance < half_width - 4
depth = np.clip(distance / half_width, 0, 1)
flow = 5 * np.sin(columns / 56 + rows / 42) + 3 * np.sin(columns / 25 - rows / 33)
water_color = np.stack((
    22 + flow - 4 * depth,
    108 + flow - 23 * depth,
    121 + flow - 19 * depth,
), axis=-1)
canvas[water] = water_color[water]

# Narrow light streaks follow the flow without turning the water into a grid.
for y, offset, length in ((46, -38, 95), (118, 29, 145), (195, -18, 115),
                          (266, 60, 130), (344, -42, 170), (430, 22, 140),
                          (517, -98, 125), (603, 58, 175), (676, -64, 145)):
    cx = int(center[y, 0] + offset)
    for shift in (0, 10, 19):
        x0 = max(0, cx - length // 2 + shift * 2)
        x1 = min(WIDTH, x0 + length - shift * 3)
        yy = y + shift
        if x0 < x1:
            visible = water[yy:yy + 2, x0:x1]
            patch = canvas[yy:yy + 2, x0:x1]
            patch[visible] = (90, 163, 158)

# Keep both the navigation area and the lower-right title legible. The menu's
# existing left overlay still provides its light-green border and contrast.
right_title = np.clip((columns - 880) / 380, 0, 1) * np.clip((rows - 430) / 250, 0, 1)
canvas *= (1 - 0.47 * right_title)[..., None]
pixels = np.uint8(np.clip(canvas, 0, 255))


def chunk(tag, data):
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data))


raw = b"".join(b"\0" + row.tobytes() for row in pixels)
png = (b"\x89PNG\r\n\x1a\n"
       + chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0))
       + chunk(b"IDAT", zlib.compress(raw, level=9))
       + chunk(b"IEND", b""))
OUTPUT.write_bytes(png)
print(f"Generated {OUTPUT}")
