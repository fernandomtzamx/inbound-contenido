#!/usr/bin/env python3
"""Descarga el contenido original (raw) de entradas a registro/raw/<slug>.json. Solo lectura.

Lee los slugs de docs/importar.txt (uno por línea). Líneas especiales:
  categoria:<slug>   importa todas las entradas publicadas de esa categoría
  buscar:<texto>     importa todas las entradas que coinciden con la búsqueda
  imagenes:si        además descarga las imágenes del contenido a registro/img/<slug>/
  solo-lista         solo guarda las listas en registro/listas/, sin descargar entradas
  minutos:<n>        detiene la descarga después de n minutos (lo ya bajado se guarda)
"""
import time
import io
import re
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)


def listar(wp, params):
    out, page = [], 1
    while True:
        r = wp.s.get(f"{wp.api}/posts", params={**params, "per_page": 100, "page": page,
                                                "_fields": "id,slug,title,link,categories"}, timeout=30)
        if r.status_code >= 400:
            break
        data = r.json()
        out += data
        if page >= int(r.headers.get("X-WP-TotalPages", 1)):
            break
        page += 1
    return out


def bajar_imagenes(wp, slug, content, featured):
    srcs = re.findall(r'<img[^>]+src="([^"]+)"', content or "")
    if featured:
        srcs.append(featured)
    base = wp.api.split("/wp-json")[0]
    d = ROOT / "registro" / "img" / slug
    d.mkdir(parents=True, exist_ok=True)
    seen = []
    for src in srcs:
        url = src if src.startswith("http") else base + "/" + src.lstrip("/")
        url = url.replace("http://", "https://")
        if url in seen:
            continue
        seen.append(url)
        try:
            r = wp.s.get(url, timeout=(10, 40))
            r.raise_for_status()
            from PIL import Image
            im = Image.open(io.BytesIO(r.content)).convert("RGB")
            w, h = im.size
            if w > 1100:
                im = im.resize((1100, int(h * 1100 / w)))
            name = f"{len(seen)}.jpg"
            im.save(d / name, "JPEG", quality=82)
            (d / f"{len(seen)}.txt").write_text(f"{src}\n{w}x{h}\n", encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"  imagen no descargada {url}: {str(e)[:120]}")


def main():
    lines = [s.strip() for s in (ROOT / "docs" / "importar.txt").read_text(encoding="utf-8").splitlines()
             if s.strip() and not s.startswith("#")]
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    con_img = "imagenes:si" in lines
    solo_lista = "solo-lista" in lines
    limite = next((int(l.split(":")[1]) for l in lines if l.startswith("minutos:")), 25) * 60
    t0 = time.time()
    slugs = []
    listas = ROOT / "registro" / "listas"
    for ln in lines:
        if ln in ("imagenes:si", "solo-lista") or ln.startswith("minutos:"):
            continue
        if ln.startswith("categoria:"):
            cs = ln.split(":", 1)[1]
            cat = wp.req("GET", "categories", params={"slug": cs})
            if not cat:
                print(f"categoría no encontrada: {cs}")
                continue
            posts = listar(wp, {"categories": cat[0]["id"]})
        elif ln.startswith("buscar:"):
            cs = "buscar-" + re.sub(r"\W+", "-", ln.split(":", 1)[1]).strip("-")
            posts = listar(wp, {"search": ln.split(":", 1)[1]})
        else:
            slugs.append(ln.strip("/"))
            continue
        listas.mkdir(parents=True, exist_ok=True)
        (listas / f"{cs}.json").write_text(json.dumps([{"id": p["id"], "slug": p["slug"], "title": p["title"]["rendered"],
                                                         "link": p["link"], "categories": p["categories"]} for p in posts],
                                                       ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"lista {cs}: {len(posts)} entradas")
        slugs += [p["slug"] for p in posts]
    slugs = list(dict.fromkeys(slugs))
    if solo_lista:
        return
    out_dir = ROOT / "registro" / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        if time.time() - t0 > limite:
            print(f"límite de tiempo: faltaron {len(slugs) - slugs.index(slug)} entradas", flush=True)
            break
        if con_img and (ROOT / "registro" / "img" / slug).exists():
            continue
        res = wp.req("GET", "posts", params={"slug": slug, "context": "edit", "status": "any"})
        tipo = "posts"
        if not res:
            res = wp.req("GET", "pages", params={"slug": slug, "context": "edit", "status": "any"})
            tipo = "pages"
        if not res:
            print(f"no encontrado: {slug}")
            continue
        p = res[0]
        keep = {k: p.get(k) for k in ("id", "slug", "status", "date", "modified", "link", "featured_media",
                                      "categories", "tags", "template", "format")}
        keep["title"] = (p.get("title") or {}).get("raw")
        keep["excerpt"] = (p.get("excerpt") or {}).get("raw")
        keep["content"] = (p.get("content") or {}).get("raw")
        keep["tipo"] = tipo
        if tipo == "pages":
            keep["parent"] = p.get("parent")
            keep["rendered"] = (p.get("content") or {}).get("rendered")
            keep["meta"] = p.get("meta")
        keep["yoast_head_json"] = {k: (p.get("yoast_head_json") or {}).get(k) for k in ("title", "description", "og_image")}
        if p.get("featured_media"):
            try:
                m = wp.req("GET", f"media/{p['featured_media']}", params={"context": "edit"})
                keep["featured"] = {"source_url": m.get("source_url"), "alt": m.get("alt_text"),
                                    "width": (m.get("media_details") or {}).get("width"),
                                    "height": (m.get("media_details") or {}).get("height")}
            except Exception as e:  # noqa: BLE001
                keep["featured"] = {"error": str(e)[:200]}
        if con_img:
            bajar_imagenes(wp, slug, keep["content"], (keep.get("featured") or {}).get("source_url"))
        (out_dir / f"{slug}.json").write_text(json.dumps(keep, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"descargado: {slug} (id {p['id']}, {len(keep['content'] or '')} caracteres)")


if __name__ == "__main__":
    main()
