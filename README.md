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
- `wordpress/mu-plugins/inbound-yoast-rest.php`: subir a `wp-content/mu-plugins/` para que `seo_title` y `seo_description` se guarden en Yoast.
- `wordpress/mu-plugins/inbound-host-canonico.php`: subir a `wp-content/mu-plugins/`. Redirige con 301 a https://www.inbound.com.mx todo lo que llegue por otro host (mail.inbound.com.mx, la IP, etc.) para que Google no indexe el sitio duplicado.
- `scripts/build_posts.py` + `remediacion/*.py`: fichas de las entradas remediadas; generan `content/blog/<slug>.md`.
- `scripts/audit.py` (`docs/auditoria.txt`) e `scripts/import_raw.py` (`docs/importar.txt`): auditoría y descarga del contenido original, solo lectura; se ejecutan al cambiar esos archivos.
- `registro/ultima-publicacion.log`: log del último run, para leerlo sin capturas.
- `scripts/calendario.py` + `docs/calendario-editorial.md` (y `.csv`): calendario de tres entradas por semana hasta junio de 2027. Cada entrada se escribe en `content/blog/<slug>.md` con `status: draft` y su `date`; al cambiarla a `status: publish` WordPress la programa y la publica solo. `python scripts/calendario.py` regenera la tabla con el estado real de cada archivo.

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
id: 1234                 # opcional: actualiza esa entrada aunque cambie el slug
seo_title: "Title de Yoast"
seo_description: "Meta description de Yoast"
```

Todas las entradas se publican con el autor del usuario conectado (soporte, Fernando Arturo Martinez Aguilar). Las imágenes citadas como `src="images/..."` se suben solas a Medios.

## Errores típicos

- `401 rest_not_logged_in`: el header se pierde; sube el mu-plugin.
- `403`: firewall o plugin de seguridad bloqueando `/wp-json/`.
