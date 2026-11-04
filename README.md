# Proyecto Arte — Ren'Py web-export demo

A tiny visual novel made to test Ren'Py web exports. All graphics are flat
colors and text, so there are no image assets to worry about.

- `game/script.rpy` — the story
- `game/options.rpy` — game title, version, and build settings
- `game/gui.rpy`, `game/screens.rpy` — generated default GUI
- `dist/web/` — latest web export (built artifact, git-ignored)

## Run locally

The Ren'Py SDK lives in this same folder, so point it at the project root:

```sh
steam-run ./renpy.sh .
```

## Build the web export

```sh
steam-run ./renpy.sh launcher web_build "$PWD" --dest "$PWD/dists/web"
```

This writes the playable site to `dists/web/` and a zip to `dists/web.zip`.

## Test the web export

Web builds must be served over HTTP — opening `index.html` directly from the
filesystem will not work.

```sh
cd dists/web
python3 -m http.server 8042
```

Then open <http://127.0.0.1:8042/>.

## Note about this layout

This project sits inside the Ren'Py SDK folder. `game/options.rpy` has a
build-file whitelist that packages only `game/**`; without it, web builds would
also include the launcher, tutorial, docs, and the rest of the SDK.
