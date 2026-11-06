# Arte y Tecnología -- Proyecto final

## Correr localmente

```sh
steam-run ./renpy.sh .
```

## Exportar a web

Este comando exporta el juego a `dists/web/` y `dists/web.zip`

```sh
steam-run ./renpy.sh launcher web_build "$PWD" --dest "$PWD/dists/web"
```
