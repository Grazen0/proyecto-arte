# Arte y Tecnología -- Proyecto final

Una novela visual sobre minería, socios y decisiones en Madre de Dios. Todos
los gráficos son formas y colores simples, así que todavía no hay assets de
imagen.

- `game/script.rpy` — la historia
- `game/options.rpy` — título, versión y configuración del build
- `game/gui.rpy`, `game/screens.rpy` — GUI por defecto generada
- `dists/web/` — último export web (artefacto generado, ignorado por Git)

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
