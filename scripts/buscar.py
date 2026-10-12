#!/usr/bin/env python3
"""Busca términos (docs/buscar.txt) en widgets, redirecciones, formularios y contenido de WordPress. Solo lectura.

Deja el resultado en registro/busqueda.json.
"""
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)


def get(wp, url, params=None):
    r = wp.s.get(url, params=params or {}, timeout=60)
    try:
        return r.status_code, r.json()
    except ValueError:
        return r.status_code, r.text[:500]


def main():
    terms = [t.strip() for t in (ROOT / "docs" / "buscar.txt").read_text(encoding="utf-8").splitlines()
             if t.strip() and not t.startswith("#")]
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    base = wp.api.rsplit("/wp/v2", 1)[0]
    found = []

    def scan(source, obj):
        text = json.dumps(obj, ensure_ascii=False)
        for t in terms:
            if t.lower() in text.lower():
                i = text.lower().index(t.lower())
                found.append({"fuente": source, "termino": t, "contexto": text[max(0, i - 250): i + 250]})

    # Widgets y bloques reutilizables
    for path in ("widgets?context=edit&per_page=100", "blocks?context=edit&per_page=100&status=any",
                 "templates?context=edit", "template-parts?context=edit", "menu-items?context=edit&per_page=100",
                 "navigation?context=edit&per_page=100"):
        code, data = get(wp, f"{wp.api}/{path}")
        print(f"{path.split('?')[0]}: HTTP {code}, {len(data) if isinstance(data, list) else '-'} elementos")
        if isinstance(data, list):
            for item in data:
                scan(f"{path.split('?')[0]} {item.get('id')}", item)
    # Plugin Redirection
    code, data = get(wp, f"{base}/redirection/v1/redirect", {"per_page": 200})
    items = data.get("items", []) if isinstance(data, dict) else []
    print(f"redirection: HTTP {code}, {len(items)} redirecciones")
    for item in items:
        scan(f"redirection {item.get('id')}", item)
    # Entradas y páginas
    for t in terms:
        for kind in ("posts", "pages"):
            code, data = get(wp, f"{wp.api}/{kind}", {"search": t, "status": "any", "context": "edit", "per_page": 100})
            if isinstance(data, list):
                for item in data:
                    scan(f"{kind} {item.get('id')} {item.get('slug')}", {"content": (item.get("content") or {}).get("raw")})
    # Ajustes generales visibles por API
    code, data = get(wp, f"{wp.api}/settings")
    scan("settings", data)

    (ROOT / "registro" / "busqueda.json").write_text(json.dumps(found, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Coincidencias: {len(found)}")
    for f in found[:30]:
        print(f" - {f['fuente']}: {f['termino']}")


if __name__ == "__main__":
    main()
