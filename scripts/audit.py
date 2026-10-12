#!/usr/bin/env python3
"""Audita entradas publicadas y deja el resultado en registro/auditoria.json.

Lee los slugs (uno por línea) de docs/auditoria.txt. Solo lee: no modifica nada en WordPress.
"""
import html as htmllib
import importlib.util
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)

HOSTS = ("inbound.com.mx",)


def analyze(post):
    raw = (post.get("content") or {}).get("raw") or ""
    rendered = (post.get("content") or {}).get("rendered") or ""
    body = re.sub(r"<(script|style)\b.*?</\1>", " ", rendered, flags=re.S | re.I)
    text = htmllib.unescape(re.sub(r"<[^>]+>", " ", body))
    imgs = re.findall(r"<img\b[^>]*>", rendered, re.I)
    srcs = [re.search(r'\bsrc="([^"]+)"', i).group(1) for i in imgs if re.search(r'\bsrc="([^"]+)"', i)]
    links = re.findall(r'<a\b[^>]*href="([^"]+)"', rendered, re.I)
    internal = [l for l in links if l.startswith("/") or any(h in l for h in HOSTS)]
    yo = post.get("yoast_head_json") or {}
    return {
        "id": post["id"],
        "slug": post["slug"],
        "link": post.get("link"),
        "title": htmllib.unescape((post.get("title") or {}).get("rendered", "")),
        "date": post.get("date"),
        "modified": post.get("modified"),
        "words": len(text.split()),
        "h2": len(re.findall(r"<h2\b", rendered, re.I)),
        "h3": len(re.findall(r"<h3\b", rendered, re.I)),
        "images": len(imgs),
        "images_sin_alt": sum(1 for i in imgs if not re.search(r'\balt="[^"]+"', i)),
        "imagenes_http_o_ip": [s for s in srcs if s.startswith("http://") or re.match(r"https?://\d+\.\d+\.\d+\.\d+", s)],
        "imagenes_ejemplo": srcs[:3],
        "enlaces_internos": len(internal),
        "enlaces_externos": len(links) - len(internal),
        "featured_media": post.get("featured_media"),
        "categories": post.get("categories"),
        "tags": post.get("tags"),
        "excerpt": htmllib.unescape(re.sub(r"<[^>]+>", "", (post.get("excerpt") or {}).get("rendered", ""))).strip()[:300],
        "yoast_title": yo.get("title"),
        "yoast_description": yo.get("description"),
        "yoast_robots": yo.get("robots"),
        "yoast_canonical": yo.get("canonical"),
        "schema_types": sorted({str(g.get("@type")) for g in (yo.get("schema") or {}).get("@graph", [])}),
        "texto_inicio": " ".join(text.split())[:400],
        "usa_bloques": "<!-- wp:" in raw,
    }


def main():
    slugs = [s.strip().strip("/") for s in (ROOT / "docs" / "auditoria.txt").read_text(encoding="utf-8").splitlines()
             if s.strip() and not s.startswith("#")]
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    out = []
    for slug in slugs:
        try:
            res = wp.req("GET", "posts", params={"slug": slug, "context": "edit", "status": "any"})
            if not res:
                res = wp.req("GET", "pages", params={"slug": slug, "context": "edit", "status": "any"})
            if not res:
                out.append({"slug": slug, "error": "no encontrado"})
                print(f"no encontrado: {slug}")
                continue
            out.append(analyze(res[0]))
            print(f"ok: {slug} ({out[-1]['words']} palabras)")
        except Exception as e:  # noqa: BLE001
            out.append({"slug": slug, "error": str(e)[:300]})
            print(f"ERROR {slug}: {e}")
    dest = ROOT / "registro" / "auditoria.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Auditoría guardada en {dest.relative_to(ROOT)}: {len(out)} URLs")


if __name__ == "__main__":
    main()
