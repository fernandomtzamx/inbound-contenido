# Inbound: contenido y pipeline de publicación

Repositorio fuente del blog de [inbound.com.mx](https://www.inbound.com.mx). Cada archivo Markdown en `content/` se publica en WordPress por la API REST cuando llega a `main`.

## Secretos (Settings > Secrets and variables > Actions)

| Secreto | Valor |
|---|---|
| `WP_URL` | `https://www.inbound.com.mx` |
| `WP_USER` | `aiagent` |
| `WP_APP_PASSWORD` | contraseña de aplicación del usuario |

## Archivos

- `scripts/publish.py`: Markdown con frontmatter a entradas o páginas; crea categorías y etiquetas si faltan; si el slug ya existe, actualiza.
- `.github/workflows/publish.yml`: publica lo que cambie en `content/` en cada push a `main`. Botón manual con modos `check`, `all` y `setup`.
- `scripts/site_setup.py` + `docs/sitio.yml`: autor, categorías y limpieza del sitio.
- `scripts/lint.py`, `scripts/cover.py`, `scripts/article.css`: control de calidad, portadas 1200x630 y estilos del artículo (ajustar colores a la marca).
- `wordpress/mu-plugins/inbound-auth.php`: subir a `wp-content/mu-plugins/` si el servidor borra el header `Authorization`.
- `registro/ultima-publicacion.log`: log del último run, para leerlo sin capturas.

## Frontmatter

```yaml
title: "Título"
slug: mi-slug
type: post            # post | page
status: draft         # draft | publish | pending | private
excerpt: "Descripción corta"
categories: [inbound-marketing]
tags: [hubspot, seo]
date: 2026-10-20 09:00   # opcional, hora de Ciudad de México; programa la entrada
featured_image: images/portada.png
```

## Errores típicos

- `401 rest_not_logged_in`: el header se pierde; sube el mu-plugin.
- `403`: firewall o plugin de seguridad bloqueando `/wp-json/`.
