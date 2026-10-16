#!/usr/bin/env python3
"""Inventario de plugins y temas instalados; deja el resultado en registro/inventario.json.

Solo lee: no modifica nada en WordPress. Se ejecuta cuando cambia docs/inventario.txt.
"""
import importlib.util
import json
import pathlib
import re

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)


def main():
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    out = {"plugins": [], "temas": [], "wordpress": {}, "servidor": {}}

    try:
        for p in wp.req("GET", "plugins", params={"context": "edit"}):
            out["plugins"].append({k: p.get(k) for k in (
                "plugin", "name", "status", "version", "requires_wp", "requires_php",
                "author", "plugin_uri", "textdomain", "network_only")})
            print(f"plugin: {p.get('name')} {p.get('version')} [{p.get('status')}] PHP>={p.get('requires_php') or '?'}")
    except Exception as e:  # noqa: BLE001
        out["plugins_error"] = str(e)[:300]
        print(f"ERROR plugins: {e}")

    try:
        for t in wp.req("GET", "themes", params={"context": "edit"}):
            out["temas"].append({k: t.get(k) for k in (
                "stylesheet", "template", "status", "version", "requires_wp", "requires_php",
                "theme_uri", "author", "textdomain")} | {
                "name": (t.get("name") or {}).get("raw") or (t.get("name") or {}).get("rendered")})
            print(f"tema: {out['temas'][-1]['name']} {t.get('version')} [{t.get('status')}] PHP>={t.get('requires_php') or '?'}")
    except Exception as e:  # noqa: BLE001
        out["temas_error"] = str(e)[:300]
        print(f"ERROR temas: {e}")

    base = wp.api.split("/wp-json")[0]
    # Versión de WordPress: el feed RSS incluye <generator>.
    try:
        r = wp.s.get(base + "/feed/", timeout=30)
        m = re.search(r"wordpress\.org/\?v=([\d.]+)", r.text)
        out["wordpress"]["version"] = m.group(1) if m else None
        print(f"WordPress: {out['wordpress']['version']}")
    except Exception as e:  # noqa: BLE001
        out["wordpress"]["error"] = str(e)[:300]

    # Encabezados del servidor (versión de PHP si el servidor la expone).
    try:
        r = wp.s.get(base + "/wp-json/", timeout=30)
        hdr = {k: v for k, v in r.headers.items() if k.lower() in (
            "server", "x-powered-by", "x-litespeed-cache", "cf-cache-status", "x-turbo-charged-by")}
        out["servidor"]["headers"] = hdr
        print(f"Encabezados: {hdr}")
    except Exception as e:  # noqa: BLE001
        out["servidor"]["error"] = str(e)[:300]

    # Site Health (si el usuario tiene permiso): pruebas directas.
    for test in ("background-updates", "loopback-requests", "https-status", "dotorg-communication", "page-cache"):
        try:
            r = wp.s.get(f"{base}/wp-json/wp-site-health/v1/tests/{test}", timeout=60)
            if r.status_code == 200:
                d = r.json()
                out["servidor"][test] = {"status": d.get("status"), "label": d.get("label")}
                print(f"site-health {test}: {d.get('status')} - {d.get('label')}")
        except Exception:  # noqa: BLE001
            pass

    (ROOT / "registro").mkdir(exist_ok=True)
    (ROOT / "registro" / "inventario.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Inventario: {len(out['plugins'])} plugins, {len(out['temas'])} temas -> registro/inventario.json")


if __name__ == "__main__":
    main()
