#!/usr/bin/env python3
"""Calendario editorial de inbound.com.mx: tres entradas por semana hasta junio de 2027.

Genera docs/calendario-editorial.md y docs/calendario-editorial.csv a partir de las listas de abajo.
Lunes: estrategia (inbound marketing, metodología, inbound sales, CRM, marketing digital).
Miércoles: SEO, GEO y desarrollo web con growth driven design.
Viernes: inbound marketing por industria o mercado.

Uso: python scripts/calendario.py
"""
import csv
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INICIO = datetime.date(2026, 10, 26)  # lunes de la semana 1
SEMANAS = 36                           # hasta el lunes 28 de junio de 2027
HORA = "09:00"
# Días festivos: la entrada se adelanta al jueves.
MOVER = {datetime.date(2026, 12, 25): datetime.date(2026, 12, 24),
         datetime.date(2027, 1, 1): datetime.date(2026, 12, 31)}

# (categoría, título, keyword principal, slug)
LUNES = [
    ("inbound-marketing", "Metodología inbound: cómo funciona el flywheel en 2026", "metodología inbound", "metodologia-inbound"),
    ("inbound-marketing", "Inbound marketing vs outbound: costos, plazos y cuándo combinarlos", "inbound marketing vs outbound", "inbound-marketing-vs-outbound"),
    ("inbound-marketing", "Buyer's journey: qué contenido necesita cada etapa", "buyer's journey", "buyer-journey-etapas-contenido"),
    ("crm", "Lead scoring: cómo calificar prospectos sin complicarte", "lead scoring", "lead-scoring"),
    ("inbound-sales", "Inbound sales: qué es y cómo cambia tu proceso de ventas", "inbound sales", "inbound-sales"),
    ("crm", "Qué CRM elegir para una pyme en México: HubSpot, Zoho o Salesforce", "crm para pymes", "que-crm-elegir-pyme-mexico"),
    ("inbound-marketing", "Lead nurturing: secuencias de correo que sí convierten", "lead nurturing", "lead-nurturing"),
    ("marketing-digital", "Plan de marketing de contenidos 2027: calendario y recursos", "plan de marketing de contenidos", "plan-marketing-de-contenidos-2027"),
    ("inbound-sales", "Smarketing: cómo alinear marketing y ventas con un SLA", "smarketing", "smarketing-alinear-marketing-y-ventas"),
    ("marketing-digital", "Automatización de marketing: los 5 flujos con los que empezar", "automatización de marketing", "automatizacion-de-marketing-flujos"),
    ("inbound-marketing", "KPIs de inbound marketing: qué medir cada mes y por qué", "kpis de inbound marketing", "kpis-de-inbound-marketing"),
    ("marketing-digital", "Costo por lead en México: referencias por canal e industria", "costo por lead", "costo-por-lead-mexico"),
    ("inbound-sales", "Llamada de descubrimiento: guion para vender sin presionar", "llamada de descubrimiento", "llamada-de-descubrimiento-ventas"),
    ("crm", "Cómo implementar un CRM en 30 días sin perder la operación", "implementar un crm", "implementar-crm-30-dias"),
    ("inbound-marketing", "Account based marketing e inbound: cómo combinarlos en B2B", "account based marketing", "account-based-marketing-inbound"),
    ("marketing-digital", "Email marketing en México: entregabilidad, consentimiento y ley de datos", "email marketing méxico", "email-marketing-mexico-entregabilidad"),
    ("marketing-digital", "Presupuesto de marketing digital 2027: cuánto invertir y en qué", "presupuesto de marketing digital", "presupuesto-marketing-digital-2027"),
    ("inbound-marketing", "Webinars que generan prospectos: formato, promoción y seguimiento", "webinars para generar leads", "webinars-para-generar-leads"),
    ("inbound-sales", "Objeciones de precio: cómo responderlas con inbound sales", "objeciones de precio", "objeciones-de-precio-ventas"),
    ("crm", "Pipeline de ventas: etapas, probabilidades y pronóstico", "pipeline de ventas", "pipeline-de-ventas"),
    ("marketing-digital", "Marketing conversacional: WhatsApp Business y chatbots con sentido", "marketing conversacional", "marketing-conversacional-whatsapp"),
    ("inbound-marketing", "Casos de éxito y testimonios: cómo producirlos y dónde usarlos", "casos de éxito marketing", "casos-de-exito-testimonios"),
    ("marketing-digital", "Remarketing y pauta: cómo acelerar el inbound sin depender de ella", "remarketing", "remarketing-y-pauta-inbound"),
    ("inbound-marketing", "Deleitar: retención, NPS y clientes que recomiendan", "retención de clientes", "retencion-de-clientes-nps"),
    ("inbound-sales", "Social selling en LinkedIn: prospección que no parece spam", "social selling linkedin", "social-selling-linkedin"),
    ("crm", "Datos limpios en el CRM: duplicados, campos y reportes confiables", "limpieza de datos crm", "limpieza-de-datos-crm"),
    ("marketing-digital", "Video marketing: YouTube y shorts para generar demanda", "video marketing", "video-marketing-youtube"),
    ("marketing-digital", "Atribución de marketing: modelos y cómo leerlos con GA4 y CRM", "atribución de marketing", "atribucion-de-marketing-ga4-crm"),
    ("inbound-marketing", "Contenido pilar y clusters: cómo organizar el blog por temas", "contenido pilar", "contenido-pilar-y-clusters"),
    ("inbound-sales", "Propuestas comerciales que cierran: estructura y errores", "propuesta comercial", "propuestas-comerciales-que-cierran"),
    ("crm", "Automatización de ventas: secuencias, tareas y recordatorios", "automatización de ventas", "automatizacion-de-ventas-crm"),
    ("marketing-digital", "IA en marketing: dónde ayuda, dónde estorba y cómo usarla", "ia en marketing", "ia-en-marketing"),
    ("inbound-marketing", "Customer marketing: upsell y cross-sell con contenido", "customer marketing", "customer-marketing-upsell-cross-sell"),
    ("inbound-sales", "Speed to lead: por qué responder en 5 minutos multiplica cierres", "speed to lead", "speed-to-lead"),
    ("crm", "CRM y servicio al cliente: tickets, base de conocimiento y encuestas", "crm servicio al cliente", "crm-servicio-al-cliente"),
    ("inbound-marketing", "Plan de inbound marketing para el segundo semestre de 2027", "plan de inbound marketing", "plan-inbound-marketing-segundo-semestre-2027"),
]

MIERCOLES = [
    ("seo", "GEO: cómo aparecer en ChatGPT, Gemini y AI Overviews desde México", "geo generative engine optimization", "geo-generative-engine-optimization"),
    ("desarrollo-web", "Growth driven design: qué es y por qué sustituye al rediseño tradicional", "growth driven design", "growth-driven-design"),
    ("seo", "Auditoría SEO técnica: checklist de 25 puntos para tu sitio", "auditoría seo técnica", "auditoria-seo-tecnica-checklist"),
    ("seo", "Investigación de keywords en español de México: método y herramientas", "investigación de keywords", "investigacion-de-keywords-mexico"),
    ("desarrollo-web", "Launch pad: cómo lanzar un sitio en 60 días con growth driven design", "launch pad website", "launch-pad-website-growth-driven-design"),
    ("seo", "SEO local: Google Business Profile paso a paso", "seo local", "seo-local-google-business-profile"),
    ("seo", "Schema markup: qué datos estructurados agregar y cómo", "schema markup", "schema-markup-datos-estructurados"),
    ("desarrollo-web", "Core Web Vitals en WordPress: cómo medir y mejorar la velocidad", "core web vitals wordpress", "core-web-vitals-wordpress"),
    ("desarrollo-web", "Ciclo de mejora continua: hipótesis, wishlist y sprints en GDD", "mejora continua sitio web", "mejora-continua-growth-driven-design"),
    ("seo", "Contenido que citan los LLM: estructura para AI Overviews y ChatGPT", "contenido para ai overviews", "contenido-para-ai-overviews"),
    ("seo", "Link building en México: tácticas que no te penalizan", "link building", "link-building-mexico"),
    ("seo", "Arquitectura web y enlazado interno: cómo repartir autoridad", "enlazado interno", "arquitectura-web-enlazado-interno"),
    ("desarrollo-web", "Anatomía de una landing page que convierte (con ejemplos)", "landing page que convierte", "landing-page-que-convierte"),
    ("seo", "SEO para ecommerce: categorías, fichas y búsquedas de compra", "seo para ecommerce", "seo-para-ecommerce"),
    ("seo", "llms.txt, robots.txt y rastreadores de IA: qué permitir y qué no", "llms.txt", "llms-txt-robots-rastreadores-ia"),
    ("seo", "Search Console: cómo leerlo cada mes y qué decisiones tomar", "google search console", "google-search-console-como-leerlo"),
    ("desarrollo-web", "Pruebas A/B y mapas de calor: cómo decidir cambios con datos", "pruebas a/b sitio web", "pruebas-ab-mapas-de-calor"),
    ("seo", "Canibalización de keywords: cómo detectarla y consolidar con 301", "canibalización de keywords", "canibalizacion-de-keywords"),
    ("seo", "Cómo medir tu visibilidad en motores de IA: métricas y herramientas", "visibilidad en motores de ia", "medir-visibilidad-motores-de-ia"),
    ("seo", "SEO para Latinoamérica: hreflang, dominios y variantes de español", "seo internacional latinoamérica", "seo-latinoamerica-hreflang"),
    ("desarrollo-web", "Formularios que convierten: campos, fricción y seguimiento", "formularios que convierten", "formularios-que-convierten"),
    ("seo", "Content refresh: cómo actualizar entradas viejas y recuperar tráfico", "actualizar contenido antiguo", "content-refresh-actualizar-contenido"),
    ("seo", "E-E-A-T: experiencia, autoría y confianza en tu contenido", "e-e-a-t", "eeat-experiencia-autoridad-confianza"),
    ("desarrollo-web", "WordPress, HubSpot CMS o Webflow: qué plataforma usar para inbound", "cms para inbound marketing", "wordpress-hubspot-cms-webflow"),
    ("seo", "GEO fuera de tu sitio: reseñas, foros y menciones que leen los LLM", "menciones de marca ia", "geo-menciones-resenas-foros"),
    ("seo", "SEO para video: YouTube y resultados enriquecidos", "seo para youtube", "seo-para-video-youtube"),
    ("desarrollo-web", "Accesibilidad web y mobile first: lo mínimo que debe cumplir tu sitio", "accesibilidad web", "accesibilidad-web-mobile-first"),
    ("seo", "Migrar un sitio sin perder SEO: plan de redirecciones", "migración seo", "migrar-sitio-sin-perder-seo"),
    ("seo", "Búsqueda conversacional: cómo cambian las consultas con IA y voz", "búsqueda conversacional", "busqueda-conversacional-ia-voz"),
    ("seo", "GEO local: cómo aparecer cuando preguntan a la IA por negocios cerca", "geo local", "geo-local-negocios-cerca"),
    ("desarrollo-web", "Dashboard de rendimiento web: las 10 métricas que importan", "métricas de sitio web", "dashboard-rendimiento-sitio-web"),
    ("seo", "Páginas por ciudad y servicio: cómo hacerlas sin contenido duplicado", "páginas de ubicación seo", "paginas-por-ciudad-y-servicio-seo"),
    ("seo", "SEO en 2027: qué cambió en el último año y qué hacer", "seo 2027", "seo-2027-que-cambio"),
    ("desarrollo-web", "Conectar tu sitio con el CRM: rastreo de formularios y atribución", "integrar sitio web con crm", "conectar-sitio-web-con-crm"),
    ("seo", "Imágenes y SEO: WebP, texto alternativo y Google Imágenes", "seo de imágenes", "seo-de-imagenes-webp"),
    ("seo", "SEO y GEO juntos: plan para el segundo semestre de 2027", "plan seo y geo", "plan-seo-geo-segundo-semestre-2027"),
]

VIERNES = [
    ("industrias", "Inbound marketing para manufactura: cómo vender a plantas y compradores", "inbound marketing para manufactura", "inbound-marketing-para-manufactura"),
    ("industrias", "Inbound marketing para inmobiliarias: prospectos antes de la visita", "inbound marketing para inmobiliarias", "inbound-marketing-para-inmobiliarias"),
    ("industrias", "Marketing digital para el Buen Fin 2026: plan de 30 días", "marketing digital buen fin", "marketing-digital-buen-fin"),
    ("industrias", "Inbound marketing para clínicas y hospitales: confianza antes de la cita", "inbound marketing para clínicas", "inbound-marketing-para-clinicas"),
    ("industrias", "Inbound marketing para universidades y escuelas: captación 2027", "inbound marketing para universidades", "inbound-marketing-para-universidades"),
    ("industrias", "Inbound marketing para empresas de software y SaaS en México", "inbound marketing para saas", "inbound-marketing-para-saas"),
    ("industrias", "Inbound marketing para capacitación corporativa y e-learning B2B", "marketing para capacitación empresarial", "inbound-marketing-para-capacitacion-corporativa"),
    ("industrias", "Inbound marketing para despachos legales: contenido que da confianza", "inbound marketing para abogados", "inbound-marketing-para-despachos-legales"),
    ("industrias", "Inbound marketing para contadores y despachos fiscales", "inbound marketing para contadores", "inbound-marketing-para-contadores"),
    ("industrias", "Marketing digital para restaurantes: reservas y pedidos sin comisión", "marketing digital para restaurantes", "marketing-digital-para-restaurantes"),
    ("industrias", "Inbound marketing para fintech: confianza, regulación y contenido", "inbound marketing para fintech", "inbound-marketing-para-fintech"),
    ("industrias", "Inbound marketing para maquinaria y equipo industrial", "marketing para maquinaria industrial", "inbound-marketing-para-maquinaria-industrial"),
    ("industrias", "Inbound marketing para constructoras y desarrolladores", "inbound marketing para constructoras", "inbound-marketing-para-constructoras"),
    ("industrias", "Inbound marketing para logística y transporte", "inbound marketing para logística", "inbound-marketing-para-logistica"),
    ("industrias", "Inbound marketing para consultorías: vender conocimiento", "inbound marketing para consultorías", "inbound-marketing-para-consultorias"),
    ("industrias", "Inbound marketing para energía solar: ciclo largo y objeciones", "inbound marketing energía solar", "inbound-marketing-para-energia-solar"),
    ("industrias", "Inbound marketing para seguros y agentes", "inbound marketing para seguros", "inbound-marketing-para-seguros"),
    ("industrias", "Inbound marketing para parques industriales y nearshoring", "marketing nearshoring méxico", "inbound-marketing-nearshoring-parques-industriales"),
    ("industrias", "Inbound marketing para clínicas dentales", "marketing para dentistas", "inbound-marketing-para-clinicas-dentales"),
    ("industrias", "Inbound marketing para franquicias: captar franquiciatarios", "marketing para franquicias", "inbound-marketing-para-franquicias"),
    ("industrias", "Inbound marketing para startups: crecer sin quemar presupuesto", "inbound marketing para startups", "inbound-marketing-para-startups"),
    ("industrias", "Inbound marketing para gimnasios y estudios de fitness", "marketing para gimnasios", "inbound-marketing-para-gimnasios"),
    ("industrias", "Inbound marketing para agroindustria y alimentos", "marketing agroindustria", "inbound-marketing-para-agroindustria"),
    ("industrias", "Inbound marketing para reclutadoras y recursos humanos", "marketing para reclutadoras", "inbound-marketing-para-reclutadoras"),
    ("industrias", "Inbound marketing para arquitectos y despachos de diseño", "marketing para arquitectos", "inbound-marketing-para-arquitectos"),
    ("industrias", "Inbound marketing para veterinarias y mascotas", "marketing para veterinarias", "inbound-marketing-para-veterinarias"),
    ("industrias", "Inbound marketing para distribuidores y mayoristas B2B", "marketing para distribuidores", "inbound-marketing-para-distribuidores"),
    ("industrias", "Inbound marketing para ONG y causas: donantes recurrentes", "marketing para ong", "inbound-marketing-para-ong"),
    ("industrias", "Marketing digital para el Hot Sale 2027: plan de 45 días", "marketing digital hot sale", "marketing-digital-hot-sale"),
    ("industrias", "Inbound marketing para escuelas de idiomas y cursos en línea", "marketing para cursos en línea", "inbound-marketing-para-cursos-en-linea"),
    ("industrias", "Inbound marketing para empresas de eventos y experiencias", "marketing para eventos", "inbound-marketing-para-empresas-de-eventos"),
    ("industrias", "Inbound marketing para telecomunicaciones e internet local", "marketing para telecomunicaciones", "inbound-marketing-para-telecomunicaciones"),
    ("industrias", "Inbound marketing para muebles y decoración", "marketing para mueblerías", "inbound-marketing-para-muebles"),
    ("industrias", "Inbound marketing para servicios de TI y ciberseguridad", "marketing para empresas de ti", "inbound-marketing-para-servicios-de-ti"),
    ("industrias", "Inbound marketing para moda y marcas de ropa", "marketing para marcas de ropa", "inbound-marketing-para-moda"),
    ("industrias", "Inbound marketing para el sector público y proveedores de gobierno", "marketing para proveedores de gobierno", "inbound-marketing-proveedores-gobierno"),
]

PILAR = {"inbound-marketing": "Inbound marketing", "marketing-digital": "Marketing digital", "seo": "SEO y GEO",
         "desarrollo-web": "Desarrollo web (GDD)", "inbound-sales": "Inbound sales", "crm": "CRM", "industrias": "Industrias"}
DIA = {0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves", 4: "viernes"}
MES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def filas():
    assert len(LUNES) == len(MIERCOLES) == len(VIERNES) == SEMANAS
    n = 0
    for w in range(SEMANAS):
        lunes = INICIO + datetime.timedelta(weeks=w)
        for offset, lista in ((0, LUNES), (2, MIERCOLES), (4, VIERNES)):
            fecha = lunes + datetime.timedelta(days=offset)
            fecha = MOVER.get(fecha, fecha)
            cat, titulo, kw, slug = lista[w]
            n += 1
            archivo = ROOT / "content" / "blog" / f"{slug}.md"
            estado = "pendiente"
            if archivo.exists():
                fm = archivo.read_text(encoding="utf-8").split("---", 2)[1]
                estado = "borrador" if "status: draft" in fm else "programada"
            yield {"n": n, "semana": w + 1, "fecha": fecha.isoformat(), "dia": DIA[fecha.weekday()], "pilar": PILAR[cat],
                   "categoria": cat, "titulo": titulo, "keyword": kw, "slug": slug, "estado": estado}


def main():
    rows = list(filas())
    with (ROOT / "docs" / "calendario-editorial.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    out = ["# Calendario editorial de inbound.com.mx (octubre 2026 a junio 2027)", "",
           f"{len(rows)} entradas: tres por semana durante {SEMANAS} semanas, del 26 de octubre de 2026 al 2 de julio de 2027, a las {HORA} hora de Ciudad de México.", "",
           "- **Lunes:** estrategia (inbound marketing, metodología, inbound sales, CRM, marketing digital).",
           "- **Miércoles:** SEO, GEO y desarrollo web con growth driven design.",
           "- **Viernes:** inbound marketing por industria o mercado.",
           "- Las entradas del 25 de diciembre y del 1 de enero se adelantan al jueves.", "",
           "## Cómo se publica sola", "",
           "Cada entrada es un archivo `content/blog/<slug>.md`. Con `status: publish` y `date: AAAA-MM-DD 09:00` en el frontmatter, el push a `main` la manda a WordPress como **programada** (estado `future`) y WordPress la publica solo a esa hora; no hace falta tocar nada ese día. Mientras se revisa, se deja `status: draft` (queda como borrador en WordPress con la misma fecha) y para aprobarla basta cambiar a `publish` y hacer push.", "",
           "Regenerar esta tabla: `python scripts/calendario.py` (lee el estado real de cada archivo).", ""]
    mes_actual = None
    for r in rows:
        d = datetime.date.fromisoformat(r["fecha"])
        m = f"{MES[d.month - 1].capitalize()} {d.year}"
        if m != mes_actual:
            mes_actual = m
            out += [f"## {m}", "", "| # | Fecha | Pilar | Título | Keyword | Slug | Estado |", "|---|---|---|---|---|---|---|"]
        out.append(f"| {r['n']} | {r['dia']} {d.day} | {r['pilar']} | {r['titulo']} | {r['keyword']} | `{r['slug']}` | {r['estado']} |")
    out.append("")
    (ROOT / "docs" / "calendario-editorial.md").write_text("\n".join(out), encoding="utf-8")
    print(f"ok {len(rows)} entradas; estados:", {e: sum(r['estado'] == e for r in rows) for e in ('pendiente', 'borrador', 'programada')})


if __name__ == "__main__":
    main()
