---
title: "Auditoría SEO técnica: checklist de 25 puntos para tu sitio"
slug: auditoria-seo-tecnica-checklist
type: post
status: draft
date: 2026-11-11 09:00
excerpt: "Checklist de auditoría SEO técnica en 25 puntos: rastreo, indexación, Core Web Vitals, móvil, seguridad y datos estructurados, con herramientas gratis."
categories: [seo]
tags: [auditoría seo técnica, seo técnico, core web vitals, search console, rastreo e indexación]
featured_image: images/auditoria-seo-tecnica-checklist.png
featured_alt: "Auditoría SEO técnica: checklist de 25 puntos para tu sitio web"
seo_title: "Auditoría SEO técnica: checklist de 25 puntos | INBOUND"
seo_description: "Checklist de auditoría SEO técnica en 25 puntos: rastreo, indexación, Core Web Vitals, móvil, HTTPS y datos estructurados, con herramientas gratis."
---

Una auditoría SEO técnica es la revisión de todo lo que permite que Google (y ahora también los motores de IA) encuentre, lea, entienda y muestre tu sitio: rastreo, indexación, velocidad, versión móvil, seguridad y datos estructurados. No toca el contenido ni los enlaces externos; revisa la tubería por la que pasa todo lo demás. Esta checklist es para dueños de negocio, responsables de marketing y desarrolladores de empresas mexicanas que quieren saber si su sitio tiene fugas técnicas antes de invertir más en contenido o publicidad.

<div class="pm-tldr" markdown="1">
**En resumen:** una auditoría SEO técnica revisa cinco bloques: **rastreo**, **indexación**, **rendimiento**, **móvil y seguridad**, y **datos estructurados**. Empieza por Search Console y PageSpeed Insights, que son gratis. El dato que explica por qué importa: solo **48%** de los sitios web aprueba los Core Web Vitals en móvil, según el Web Almanac 2025 de HTTP Archive. Si tu sitio está en el otro 52%, ningún artículo nuevo va a rendir lo que debería.
</div>

[TOC]

## Qué es una auditoría SEO técnica y qué no es

Es un diagnóstico de la infraestructura del sitio desde el punto de vista de los buscadores. Responde tres preguntas: ¿puede Google llegar a todas mis páginas importantes?, ¿las guarda en su índice tal como quiero?, y ¿cargarlas en un celular es una experiencia aceptable? No incluye la calidad del texto, la investigación de palabras clave ni la construcción de enlaces: eso es SEO de contenido y SEO off-page, y se revisa aparte.

La auditoría técnica va primero porque los otros dos dependen de ella. Un artículo excelente en una URL bloqueada por `robots.txt` no existe para Google. Una página de servicio que tarda seis segundos en cargar en un celular de gama media pierde al visitante antes de mostrar el precio. Y como los motores generativos leen el mismo índice que Google, los problemas técnicos también te sacan de las respuestas de ChatGPT o del Modo IA; lo explicamos en nuestra guía de [GEO](https://www.inbound.com.mx/geo-generative-engine-optimization/).

## Cuándo hacer una auditoría SEO técnica

Al menos una vez al año, y siempre alrededor de tres eventos: un rediseño o migración, una caída de tráfico orgánico que no se explica por estacionalidad, y el arranque de una inversión seria en contenido. En sitios con cambios frecuentes (tiendas en línea, portales inmobiliarios, medios) conviene además una revisión ligera trimestral de rastreo e indexación.

Dos herramientas gratuitas cubren el 80% del trabajo: Google Search Console (rastreo, indexación, Core Web Vitals reales, datos estructurados) y PageSpeed Insights (rendimiento con datos de campo y de laboratorio). Para sitios de más de cien páginas, suma un rastreador tipo Screaming Frog, cuya versión gratuita analiza hasta 500 URLs.

## Checklist de 25 puntos de auditoría SEO técnica

La tabla agrupa los 25 puntos en cinco bloques. La prioridad alta significa que el problema puede estar sacando páginas del índice o perdiendo visitantes hoy; media, que frena el rendimiento; baja, que es mejora incremental.

| # | Punto | Cómo revisarlo | Prioridad |
|---|---|---|---|
| 1 | `robots.txt` no bloquea secciones importantes ni CSS y JS | Abre tudominio.com/robots.txt; prueba URLs en Search Console | Alta |
| 2 | `robots.txt` responde 200 y pesa menos de 500 KiB | Inspecciona el código de respuesta con el navegador o curl | Alta |
| 3 | Sitemap XML enviado, sin errores y con `lastmod` real | Search Console, informe de sitemaps | Alta |
| 4 | Páginas importantes indexadas; nada basura indexado | Search Console, informe de indexación de páginas; `site:tudominio.com` | Alta |
| 5 | Sin `noindex` accidental en páginas que deben posicionar | Rastreador o inspección de URL | Alta |
| 6 | Sin cadenas ni bucles de redirección | Rastreador; redirecciones de dos o más saltos | Media |
| 7 | Errores 404 y soft 404 controlados | Search Console, informe de indexación | Media |
| 8 | Una sola versión del dominio (https, www o sin www) con 301 | Prueba las cuatro combinaciones en el navegador | Alta |
| 9 | Etiquetas canonical correctas y en el HTML inicial | Ver código fuente; rastreador | Alta |
| 10 | URLs limpias: cortas, con guiones, sin parámetros duplicados | Rastreador, lista de URLs | Media |
| 11 | Arquitectura plana: páginas clave a 3 clics o menos del inicio | Rastreador, profundidad de rastreo | Media |
| 12 | Enlazado interno sin páginas huérfanas ni enlaces rotos | Rastreador, informe de inlinks | Media |
| 13 | LCP de 2.5 s o menos en móvil (percentil 75) | PageSpeed Insights, datos de campo; Search Console | Alta |
| 14 | INP de 200 ms o menos | PageSpeed Insights; Search Console | Media |
| 15 | CLS de 0.1 o menos | PageSpeed Insights; Search Console | Media |
| 16 | Imágenes con dimensiones, formato moderno y sin lazy load en la imagen principal | PageSpeed Insights, diagnóstico de imágenes | Media |
| 17 | Servidor rápido: TTFB menor a 0.8 s y caché HTTP activa | PageSpeed Insights; cabeceras de respuesta | Media |
| 18 | Mismo contenido y navegación en móvil que en escritorio | Compara ambas versiones; inspección de URL en móvil | Alta |
| 19 | HTTPS en todo el sitio sin contenido mixto | Candado del navegador; consola de errores | Alta |
| 20 | HTML de páginas clave por debajo de 2 MB | Pestaña de red del navegador | Baja |
| 21 | Títulos y meta descripciones únicos, sin duplicados | Rastreador, informe de títulos | Media |
| 22 | Un solo H1 por página y jerarquía de encabezados lógica | Rastreador o extensión de navegador | Baja |
| 23 | Datos estructurados válidos (Organization, Article, Product, LocalBusiness) | Prueba de resultados enriquecidos; Search Console | Media |
| 24 | `hreflang` correcto si hay versiones por país o idioma | Rastreador; informe de Search Console | Baja |
| 25 | Rastreadores de IA permitidos o bloqueados de forma deliberada | `robots.txt`: GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot | Media |

Las secciones siguientes explican qué buscar en cada bloque y qué dicen las fuentes oficiales.

## Rastreo: ¿puede Google llegar a tus páginas? (puntos 1 a 7)

Si Google no puede rastrear una página, nada más importa. El archivo `robots.txt` es la primera parada, y tiene reglas más estrictas de lo que muchos creen. Según la [documentación de Google sobre cómo interpreta robots.txt](https://developers.google.com/search/reference/robots_txt?nav=true) (actualizada el 23 de octubre de 2026), el archivo tiene un límite de 500 KiB y todo lo que exceda se ignora; si responde un error 4xx, Google asume que no hay restricciones; y si responde 5xx, Google deja de rastrear el sitio durante las primeras 12 horas y puede usar la última versión válida hasta por 30 días. Un `robots.txt` roto durante una migración puede congelar tu rastreo un mes.

El error más común en WordPress y tiendas en línea es bloquear carpetas de CSS, JavaScript o imágenes "por seguridad". Google renderiza las páginas como un navegador; si no puede cargar los estilos, ve una página rota y la evalúa así.

Sobre el presupuesto de rastreo (crawl budget), conviene bajar la ansiedad. La [guía oficial de Google](https://developers.google.com/crawling/docs/crawl-budget), actualizada el 22 de julio de 2026, aclara que es un tema para sitios de más de un millón de páginas únicas, o de más de 10,000 páginas con contenido que cambia a diario. Para la mayoría de las empresas mexicanas el problema no es que Google rastree poco, sino que rastree basura: filtros de catálogo, versiones con parámetros, etiquetas vacías. Las recomendaciones de la guía aplican a todos: consolidar duplicados, devolver 404 o 410 en páginas eliminadas, mantener el sitemap con `lastmod` real y evitar cadenas de redirección. Google también advierte que `noindex` no ahorra rastreo, porque la página se sigue solicitando.

## Indexación y arquitectura: ¿Google guarda lo que quieres? (puntos 8 a 12)

Rastrear no es indexar. El informe de indexación de Search Console dice cuántas URLs están en el índice y por qué quedaron fuera las demás. Las dos categorías que más cuestan son "Rastreada: actualmente sin indexar" (Google la vio y la consideró poco valiosa o duplicada) y "Descubierta: actualmente sin indexar" (ni siquiera la ha rastreado, señal de problemas de arquitectura).

La etiqueta canonical debe apuntar a la versión que quieres posicionar y estar en el HTML inicial, no inyectada por JavaScript, para que Google no reciba señales contradictorias. En tiendas con variantes de color o talla, una canonical mal configurada reparte la autoridad entre veinte URLs casi iguales.

La arquitectura se mide en clics desde la portada: cualquier página que vende o convierte debe estar a tres clics o menos. Si tu página de "servicio de nómina en Querétaro" está a seis clics y sin enlaces internos, Google la trata como lo que parece: poco importante.

## Rendimiento y Core Web Vitals: ¿carga bien en un celular? (puntos 13 a 17)

Los Core Web Vitals son las tres métricas con las que Google mide la experiencia de carga, y los umbrales oficiales, medidos en el percentil 75 de visitas reales, son: LCP (tiempo en que aparece el elemento principal) de 2.5 segundos o menos, INP (respuesta a la interacción) de 200 milisegundos o menos y CLS (estabilidad visual) de 0.1 o menos. Entre esos valores y el doble, la página "necesita mejorar"; por encima, es "mala".

El panorama real no es alentador. El [capítulo de rendimiento del Web Almanac 2025](https://almanac.httparchive.org/en/2025/performance) de HTTP Archive, publicado en enero de 2026 con datos de julio de 2025, encontró que solo 48% de los sitios tiene buenos Core Web Vitals en móvil (44% en 2024) y 56% en escritorio. La métrica que más falla es LCP: solo 62% de los sitios la aprueba en móvil y 13% está en la zona "mala". INP la aprueba 77% en móvil y CLS 81%.

El mismo estudio apunta a dónde está el problema: en 76% de las páginas móviles el elemento LCP es una imagen, 62% tiene al menos una imagen sin dimensiones declaradas (la causa típica de saltos de diseño) y entre 16% y 17% aplica lazy loading a su imagen principal, lo que la retrasa en lugar de acelerarla. En la mayoría de los sitios, arreglar las imágenes de la parte superior de cada plantilla resuelve la mitad del problema.

Para medir, usa los datos de campo de PageSpeed Insights (vienen del Chrome UX Report, es decir, de usuarios reales) y el informe de Core Web Vitals de Search Console, que agrupa las URLs con problemas por plantilla. Los datos de laboratorio sirven para diagnosticar, no para calificar.

## Móvil y seguridad: ¿cumple lo básico? (puntos 18 a 20)

Google indexa la versión móvil de tu sitio, no la de escritorio. La transición a mobile-first indexing terminó el 5 de julio de 2024, [según reportó PPC Land](https://ppc.land/google-search-completes-transition-to-mobile-first-indexing-by-july-5-2024) a partir del anuncio de Google en junio de ese año, y los sitios cuyo contenido es inaccesible desde un celular pueden salir del índice. Revisa que la versión móvil tenga el mismo texto, los mismos enlaces de navegación y los mismos datos estructurados que la de escritorio; los menús "simplificados" que esconden la mitad de las secciones cortan el enlazado interno.

HTTPS ya no se discute: todo el sitio debe servirse cifrado, con redirección 301 desde http y sin contenido mixto (imágenes o scripts cargados por http dentro de una página https).

Un punto nuevo es el peso del HTML. [Search Engine Journal reportó en febrero de 2026](https://www.searchenginejournal.com/google-updates-googlebot-file-size-limit-docs/566485/) que la documentación de Google fija en 2 MB el límite de HTML y archivos de texto que Googlebot procesa por archivo (64 MB para PDF). Son muchos, pero algunos constructores visuales con CSS en línea se acercan; lo que quede después del límite no existe para Google.

## Datos estructurados y señales de página (puntos 21 a 25)

Los datos estructurados le dicen a Google qué es cada cosa en tu página: una empresa, un artículo, un producto con precio, una sucursal con horario. Se validan con la prueba de resultados enriquecidos de Google y se monitorean en Search Console. Las entidades que más valen para una empresa mexicana son `Organization` o `LocalBusiness` (con dirección, teléfono y horario), `Article` para el blog, `Product` con `Offer` para tiendas y `BreadcrumbList` para la navegación.

Un cambio importante de 2026 que muchas auditorías no reflejan: Google retiró los resultados enriquecidos de preguntas frecuentes. Su [documentación de datos estructurados](https://developers.google.com/search/docs/appearance/structured-data/faqpage) registra que la función dejó de mostrarse en Google Search a partir del 7 de mayo de 2026 y que la documentación se eliminó el 15 de junio. El marcado `FAQPage` no daña, pero ya no produce el acordeón de preguntas en los resultados; si tu plan de datos estructurados dependía de él, reasigna ese esfuerzo a `Product`, `LocalBusiness` y `Article`. Las preguntas frecuentes siguen valiendo como contenido, porque responden consultas conversacionales que los motores de IA citan.

El punto 25 es nuevo y deliberado: revisa qué rastreadores de inteligencia artificial permites. Bloquear `GPTBot` evita que tu contenido entrene modelos; bloquear `OAI-SearchBot` te saca de las respuestas con búsqueda de ChatGPT. La decisión debe ser consciente, no herencia de un plugin de seguridad.

## Cómo priorizar lo que encuentres

Una auditoría típica arroja entre 30 y 100 hallazgos, y el error es intentar arreglarlos todos. Ordénalos con dos preguntas: ¿cuánto tráfico o ingreso afecta? y ¿cuánto cuesta arreglarlo? Lo que afecta a plantillas completas va antes que lo que afecta a una URL; lo que saca páginas del índice (puntos 1, 4, 5, 8 y 9) va antes que lo que las hace lentas; y lo que se arregla con una configuración va antes que lo que requiere cambiar de tema o de servidor.

Un plan razonable para una pyme: semana uno, rastreo e indexación; semanas dos y tres, imágenes y Core Web Vitals de las tres plantillas principales; semana cuatro, datos estructurados y títulos. Después, una revisión mensual de Search Console de 30 minutos mantiene el sitio en forma. Si hace falta un cambio de fondo, la alternativa al rediseño de golpe es el [growth driven design](https://www.inbound.com.mx/growth-driven-design/), que mejora por ciclos sobre datos reales.

## Preguntas frecuentes

### ¿Qué es una auditoría SEO técnica?

Es la revisión de los elementos que permiten a los buscadores rastrear, indexar y mostrar un sitio: robots.txt, sitemap, redirecciones, canonicals, velocidad, versión móvil, HTTPS y datos estructurados. No evalúa la calidad del contenido ni los enlaces externos, que se auditan por separado.

### ¿Cada cuánto debo hacer una auditoría SEO técnica?

Una completa al año y una revisión ligera cada trimestre en sitios que cambian seguido, como tiendas en línea o portales inmobiliarios. También conviene hacerla antes y después de un rediseño o una migración, y cuando el tráfico orgánico cae sin explicación estacional.

### ¿Qué herramientas gratis sirven para una auditoría SEO técnica?

Google Search Console cubre rastreo, indexación, Core Web Vitals y datos estructurados. PageSpeed Insights mide rendimiento con datos reales de Chrome. La versión gratuita de Screaming Frog rastrea hasta 500 URLs, suficiente para la mayoría de los sitios de pymes.

### ¿Cuáles son los umbrales de los Core Web Vitals?

Medidos en el percentil 75 de visitas reales: LCP de 2.5 segundos o menos, INP de 200 milisegundos o menos y CLS de 0.1 o menos. Entre esos valores y el doble la página necesita mejorar; por encima se considera mala. Google los reporta en Search Console y PageSpeed Insights.

### ¿El marcado FAQPage todavía sirve en 2026?

Google dejó de mostrar los resultados enriquecidos de preguntas frecuentes el 7 de mayo de 2026, así que el marcado ya no genera el acordeón en los resultados. No daña, pero no debe ser prioridad. Las preguntas frecuentes como contenido siguen siendo útiles para búsquedas conversacionales y motores de IA.

### ¿Cuánto tarda en verse el efecto de una auditoría SEO técnica?

Los arreglos de rastreo e indexación se reflejan en Search Console en días o pocas semanas, conforme Google vuelve a rastrear las páginas. Los Core Web Vitals se calculan con datos de usuarios reales acumulados durante varias semanas, así que las mejoras de velocidad tardan alrededor de un mes en verse completas en los informes.

## Fuentes

- [How Google interprets the robots.txt specification, Google Search Central (actualizado el 23 de octubre de 2026)](https://developers.google.com/search/reference/robots_txt?nav=true)
- [Crawl budget management for large sites, Google Search Central (actualizado el 22 de julio de 2026)](https://developers.google.com/crawling/docs/crawl-budget)
- [Performance, Web Almanac 2025, HTTP Archive (15 de enero de 2026)](https://almanac.httparchive.org/en/2025/performance)
- [Google Search completes transition to mobile-first indexing by July 5, 2024, PPC Land (4 de junio de 2024)](https://ppc.land/google-search-completes-transition-to-mobile-first-indexing-by-july-5-2024)
- [Google updates Googlebot file size limit docs, Search Engine Journal (3 de febrero de 2026)](https://www.searchenginejournal.com/google-updates-googlebot-file-size-limit-docs/566485/)
- [FAQ structured data, historial de cambios, Google Search Central (mayo y junio de 2026)](https://developers.google.com/search/docs/appearance/structured-data/faqpage)

**Sigue leyendo:**

- [GEO: cómo aparecer en ChatGPT, Gemini y AI Overviews desde México](https://www.inbound.com.mx/geo-generative-engine-optimization/)
- [Growth driven design: qué es y por qué sustituye al rediseño tradicional](https://www.inbound.com.mx/growth-driven-design/)
- [Marketing digital en México que sí vende](https://www.inbound.com.mx/marketing/)

¿Quieres saber cuántos de estos 25 puntos falla tu sitio? [Pide un diagnóstico gratis](https://www.inbound.com.mx/contacto/) y te entregamos la auditoría con prioridades.

<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"¿Qué es una auditoría SEO técnica?","acceptedAnswer":{"@type":"Answer","text":"Es la revisión de los elementos que permiten a los buscadores rastrear, indexar y mostrar un sitio: robots.txt, sitemap, redirecciones, canonicals, velocidad, versión móvil, HTTPS y datos estructurados. No evalúa la calidad del contenido ni los enlaces externos, que se auditan por separado."}},{"@type":"Question","name":"¿Cada cuánto debo hacer una auditoría SEO técnica?","acceptedAnswer":{"@type":"Answer","text":"Una completa al año y una revisión ligera cada trimestre en sitios que cambian seguido, como tiendas en línea o portales inmobiliarios. También conviene hacerla antes y después de un rediseño o una migración, y cuando el tráfico orgánico cae sin explicación estacional."}},{"@type":"Question","name":"¿Qué herramientas gratis sirven para una auditoría SEO técnica?","acceptedAnswer":{"@type":"Answer","text":"Google Search Console cubre rastreo, indexación, Core Web Vitals y datos estructurados. PageSpeed Insights mide rendimiento con datos reales de Chrome. La versión gratuita de Screaming Frog rastrea hasta 500 URLs, suficiente para la mayoría de los sitios de pymes."}},{"@type":"Question","name":"¿Cuáles son los umbrales de los Core Web Vitals?","acceptedAnswer":{"@type":"Answer","text":"Medidos en el percentil 75 de visitas reales: LCP de 2.5 segundos o menos, INP de 200 milisegundos o menos y CLS de 0.1 o menos. Entre esos valores y el doble la página necesita mejorar; por encima se considera mala. Google los reporta en Search Console y PageSpeed Insights."}},{"@type":"Question","name":"¿El marcado FAQPage todavía sirve en 2026?","acceptedAnswer":{"@type":"Answer","text":"Google dejó de mostrar los resultados enriquecidos de preguntas frecuentes el 7 de mayo de 2026, así que el marcado ya no genera el acordeón en los resultados. No daña, pero no debe ser prioridad. Las preguntas frecuentes como contenido siguen siendo útiles para búsquedas conversacionales y motores de IA."}},{"@type":"Question","name":"¿Cuánto tarda en verse el efecto de una auditoría SEO técnica?","acceptedAnswer":{"@type":"Answer","text":"Los arreglos de rastreo e indexación se reflejan en Search Console en días o pocas semanas, conforme Google vuelve a rastrear las páginas. Los Core Web Vitals se calculan con datos de usuarios reales acumulados durante varias semanas, así que las mejoras de velocidad tardan alrededor de un mes en verse completas en los informes."}}]}</script>
