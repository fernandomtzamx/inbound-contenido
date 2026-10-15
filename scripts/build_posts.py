#!/usr/bin/env python3
"""Genera content/blog/<slug>.md a partir de fichas en remediacion/*.py.

Cada ficha es un dict en la lista POSTS con:
  id, slug, title, excerpt, body (markdown; {IMG} marca dónde va la imagen),
  img_alt, credit (opcional), faq [(pregunta, respuesta)], sources [(texto, url)],
  related [(texto, url)], toc (bool, por defecto True)
La imagen se toma del contenido original descargado en registro/raw/<slug>.json.
"""
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def first_image(slug):
    raw = ROOT / "registro" / "raw" / f"{slug}.json"
    if not raw.exists():
        return None
    d = json.loads(raw.read_text(encoding="utf-8"))
    m = re.search(r'<img[^>]+src="([^"]+)"', d.get("content") or "")
    src = m.group(1) if m else (d.get("featured") or {}).get("source_url")
    if not src:
        return None
    src = re.sub(r"^https?://www\.inbound\.com\.mx/+", "/", src)
    w = h = None
    f = d.get("featured") or {}
    if f.get("source_url") and f["source_url"].endswith(src.split("/")[-1]):
        w, h = f.get("width"), f.get("height")
    if not (w and h):
        for meta in sorted((ROOT / "registro" / "img" / slug).glob("*.txt")):
            lines = meta.read_text(encoding="utf-8").split()
            if len(lines) >= 2 and lines[0].endswith(src.split("/")[-1]) and "x" in lines[1]:
                w, h = lines[1].split("x")
                break
    return src, w, h


def render(p):
    body = p["body"].strip()
    img = p.get("img") or first_image(p["slug"])
    img_html = ""
    if img and p.get("img_alt"):
        src, w, h = img if isinstance(img, tuple) else (img, None, None)
        size = f' width="{w}" height="{h}"' if w and h else ""
        img_html = f'<img class="aligncenter" src="{src}" alt="{p["img_alt"]}"{size}>'
        if p.get("credit"):
            img_html += f'\n\n<p class="pm-nota">{p["credit"]}</p>'
    if "{IMG}" in body:
        body = body.replace("{IMG}", img_html)
    elif img_html:
        parts = body.split("\n\n", 1)
        body = parts[0] + "\n\n" + img_html + ("\n\n" + parts[1] if len(parts) > 1 else "")
    if p.get("toc", True) and "[TOC]" not in body:
        m = re.search(r"^## ", body, re.M)
        if m:
            body = body[:m.start()] + "[TOC]\n\n" + body[m.start():]
    out = [body]
    faq = p.get("faq") or []
    if faq:
        out.append("## Preguntas frecuentes")
        for q, a in faq:
            out.append(f"### {q}\n\n{a}")
    if p.get("sources"):
        out.append("## Fuentes\n\n" + "\n".join(f"- [{t}]({u})" for t, u in p["sources"]))
    if p.get("related"):
        out.append("**Sigue leyendo:**\n\n" + "\n".join(f"- [{t}]({u})" for t, u in p["related"]))
    if faq:
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer",
             "text": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a).replace("**", "")}} for q, a in faq]}
        out.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",", ":")) + "</script>")
    fm = {"title": p["title"], "id": p["id"], "slug": p["slug"], "type": "post", "status": "publish", "excerpt": p["excerpt"],
          "seo_title": p.get("seo_title", p["title"]), "seo_description": p.get("seo_description", p["excerpt"])}
    front = "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n\n"
    text = front + "\n\n".join(out) + "\n"
    bad = [c for c in ("—", "–") if c in text]
    if bad:
        raise ValueError(f"{p['slug']}: contiene guion largo o medio")
    if len(p["title"]) > 65:
        print(f"  aviso: title de {len(p['title'])} caracteres en {p['slug']}")
    return text


def main():
    for f in sys.argv[1:]:
        sys.path.insert(0, str(pathlib.Path(f).resolve().parent))
        spec = importlib.util.spec_from_file_location("ficha", f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for p in mod.POSTS:
            dest = ROOT / "content" / "blog" / f"{p['slug']}.md"
            dest.write_text(render(p), encoding="utf-8")
            words = len(re.sub(r"<[^>]+>|\[[^\]]*\]\([^)]*\)", " ", p["body"]).split())
            print(f"ok {p['id']} {p['slug'][:70]} ({words} palabras en el cuerpo)")


if __name__ == "__main__":
    main()
