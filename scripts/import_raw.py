#!/usr/bin/env python3
"""Descarga el contenido original (raw) de entradas a registro/raw/<slug>.json. Solo lectura.

Lee los slugs de docs/importar.txt (uno por línea).
"""
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)


def main():
    slugs = [s.strip().strip("/") for s in (ROOT / "docs" / "importar.txt").read_text(encoding="utf-8").splitlines()
             if s.strip() and not s.startswith("#")]
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    out_dir = ROOT / "registro" / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        res = wp.req("GET", "posts", params={"slug": slug, "context": "edit", "status": "any"})
        if not res:
            print(f"no encontrado: {slug}")
            continue
        p = res[0]
        keep = {k: p.get(k) for k in ("id", "slug", "status", "date", "modified", "link", "featured_media",
                                      "categories", "tags", "template", "format")}
        keep["title"] = (p.get("title") or {}).get("raw")
        keep["excerpt"] = (p.get("excerpt") or {}).get("raw")
        keep["content"] = (p.get("content") or {}).get("raw")
        keep["yoast_head_json"] = {k: (p.get("yoast_head_json") or {}).get(k) for k in ("title", "description", "og_image")}
        if p.get("featured_media"):
            try:
                m = wp.req("GET", f"media/{p['featured_media']}", params={"context": "edit"})
                keep["featured"] = {"source_url": m.get("source_url"), "alt": m.get("alt_text"),
                                    "width": (m.get("media_details") or {}).get("width"),
                                    "height": (m.get("media_details") or {}).get("height")}
            except Exception as e:  # noqa: BLE001
                keep["featured"] = {"error": str(e)[:200]}
        (out_dir / f"{slug}.json").write_text(json.dumps(keep, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"descargado: {slug} (id {p['id']}, {len(keep['content'] or '')} caracteres)")


if __name__ == "__main__":
    main()
