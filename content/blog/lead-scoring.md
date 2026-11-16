---
title: "Lead scoring: cómo calificar prospectos sin complicarte"
slug: lead-scoring
type: post
status: draft
date: 2026-11-16 09:00
excerpt: "Qué es el lead scoring, cómo armar un modelo de puntos con dos tablas (ajuste e interés) y cómo usarlo para que ventas llame primero a quien sí va a comprar."
categories: [crm]
tags: [lead scoring, crm, inbound sales, hubspot, prospectos]
featured_image: images/lead-scoring.png
featured_alt: "Lead scoring: cómo calificar prospectos sin complicarte"
seo_title: "Lead scoring: califica prospectos sin complicarte | INBOUND"
seo_description: "Guía práctica de lead scoring para empresas en México: criterios de ajuste e interés, puntos, umbrales, errores comunes y cómo configurarlo en tu CRM."
---

El lead scoring es un sistema de puntos para ordenar a tus prospectos según qué tan probable es que compren. Cada dato que sabes de una persona (su puesto, el tamaño de su empresa, qué páginas visitó, si pidió una cotización) suma o resta puntos, y el total le dice a ventas a quién llamar primero. Es para cualquier empresa que recibe más prospectos de los que puede atender bien, o que atiende a todos por igual y por eso llega tarde con los que sí iban a comprar.

Esta guía explica cómo armar un modelo de lead scoring sencillo, con dos tablas y una hoja de cálculo, antes de pensar en inteligencia artificial o en herramientas caras. Si ya tienes un CRM, al final verás cómo configurarlo.

<div class="pm-tldr" markdown="1">
**En resumen:** un lead scoring útil mide dos cosas por separado: **ajuste** (¿se parece a tu cliente ideal?) e **interés** (¿está haciendo algo que indica que quiere comprar?). Asigna puntos a cinco o seis criterios de cada tipo, define un umbral a partir del cual el prospecto pasa a ventas y revisa el modelo cada trimestre con los cierres reales. La velocidad importa: responder en la primera hora multiplica por siete la probabilidad de calificar a un prospecto, según un estudio citado por Harvard Business Review.
</div>

[TOC]

## Qué es el lead scoring y qué problema resuelve

El lead scoring es la calificación numérica de un prospecto a partir de sus características y de su comportamiento, para decidir qué atención merece y cuándo. Resuelve un problema concreto: el tiempo de ventas es limitado y la mayoría de los prospectos que entran por un formulario no están listos para comprar. Sin un criterio compartido, cada vendedor elige a quién llamar por intuición, y los prospectos buenos se enfrían mientras se atienden los malos.

El costo de ese desorden es alto. Según el [State of Sales 2024 de Salesforce](https://diginomica.com/state-sales-ai-incoming-there-are-caveats-according-salesforce-data), una encuesta a 5,500 profesionales de ventas en 27 países publicada en agosto de 2024, los vendedores calculan que el 70% de su jornada se va en tareas que no son vender: capturar datos, administración, preparación y juntas internas. Con tan poco tiempo real de venta, gastarlo en el prospecto equivocado es el error más caro que puede cometer un equipo comercial.

Y el reloj corre desde el primer minuto. Un estudio de 2011 de James Oldroyd, Kristina McElheran y David Elkington, publicado en [Harvard Business Review](https://hbr.org/2011/03/the-short-life-of-online-sales-leads) y [resumido por HubSpot](https://blog.hubspot.com/sales/how-to-handle-the-ticking-time-bomb-that-is-an-inbound-lead), encontró que responder a un prospecto en la primera hora hace siete veces más probable calificarlo, y que las empresas que tardaban un día o más tenían 60 veces menos probabilidad de generar un cliente. El lead scoring no acelera la llamada por sí mismo, pero decide cuál llamada se hace primero.

Dentro de la [metodología inbound](https://www.inbound.com.mx/metodologia-inbound/), el lead scoring vive en la etapa de interactuar: es el puente entre el contenido que atrajo al prospecto y el vendedor que va a ayudarlo a decidir.

## Los dos tipos de puntos: ajuste e interés

Un modelo de lead scoring que funciona separa dos preguntas distintas, porque un prospecto puede ser perfecto en una y pésimo en la otra.

**Ajuste (fit).** ¿Esta persona y su empresa se parecen a tus mejores clientes? Se califica con datos que no cambian con el tiempo: giro, tamaño, ubicación, puesto, presupuesto declarado. Un director de operaciones de una planta en Querétaro con 200 empleados tiene alto ajuste para un proveedor industrial; un estudiante que descargó tu guía para una tarea, no.

**Interés (engagement).** ¿Está haciendo algo que indica intención de compra? Se califica con comportamiento: visitas a la página de precios, solicitud de demostración, respuesta a correos, asistencia a un webinar, número de visitas en la última semana. El interés sube y baja; el ajuste casi nunca.

Esta separación es la misma que usan las herramientas profesionales. En la [documentación de HubSpot sobre calificación de leads](https://knowledge.hubspot.com/es/scoring/understand-the-lead-scoring-tool), las puntuaciones se dividen en calificaciones de adecuación (propiedades como cargo, tamaño de empresa o ingresos) y calificaciones de interacción (visitas, clics, aperturas, formularios), y las combinadas producen tres propiedades: una de ajuste, una de interacción y un total.

La ventaja de separarlas se ve en una matriz de dos por dos:

| | Interés alto | Interés bajo |
|---|---|---|
| **Ajuste alto** | Pasa a ventas hoy. Llamada en menos de una hora | Nutrir con contenido y revisar en 30 días |
| **Ajuste bajo** | Responder con recursos de autoservicio; no invertir tiempo de vendedor | Descartar o dejar en el boletín |

## Cómo definir los criterios con tu buyer persona

Los criterios salen de tus clientes actuales, no de una lista genérica. Antes de asignar un solo punto, haz dos ejercicios con el CRM abierto (o con la hoja de cálculo donde registras ventas):

1. **Saca a tus 20 mejores clientes del último año** (por margen, por permanencia o por facilidad de implementación) y anota qué tienen en común: giro, tamaño, ciudad, puesto de quien firmó, por dónde llegaron. Eso define el ajuste.
2. **Revisa el historial de los últimos 20 cierres** y anota qué hicieron antes de comprar: qué páginas vieron, qué descargaron, cuántas veces volvieron, si pidieron cotización. Eso define el interés.

Si ya tienes un [buyer persona](https://www.inbound.com.mx/buyer-persona/) documentado, el primer ejercicio está casi hecho. Si no, este es el momento de hacerlo, porque sin persona el lead scoring califica contra una idea vaga de "cliente".

Un detalle para empresas en México: el tamaño de la empresa importa más de lo que parece. Según los [Censos Económicos 2024 del INEGI](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def_RR.pdf), publicados en julio de 2025, el 95.4% de las unidades económicas del país son micronegocios de hasta 10 personas, así que si vendes a empresas medianas, el tamaño es el filtro que más tiempo le ahorra a ventas. Y el canal de contacto también dice algo: el mismo censo indica que solo el 5.6% de las unidades económicas vendió por internet en 2023 (28.7% entre las pymes), de modo que una empresa que te encontró y te escribió por tu sitio web ya muestra un nivel de madurez digital por encima del promedio.

## Cómo asignar los puntos

Empieza con una escala simple de 0 a 100 y repártela en dos mitades: hasta 50 puntos de ajuste y hasta 50 de interés. Dentro de cada mitad, da más puntos a los criterios que más separan a los clientes de los no clientes.

Un modelo de arranque para una empresa B2B de servicios en México podría verse así:

| Tipo | Criterio | Puntos |
|---|---|---|
| Ajuste | Giro dentro de tus tres industrias objetivo | +15 |
| Ajuste | Empresa de 11 a 250 empleados | +15 |
| Ajuste | Puesto de dirección o gerencia | +10 |
| Ajuste | Ubicación dentro de tu zona de cobertura | +10 |
| Ajuste | Correo personal (gmail, hotmail) en lugar de corporativo | -10 |
| Ajuste | Puesto de estudiante, becario o "otro" | -20 |
| Interés | Solicitó cotización, demostración o diagnóstico | +25 |
| Interés | Visitó la página de precios o de servicios | +10 |
| Interés | Abrió un correo y dio clic en el enlace | +5 |
| Interés | Descargó una guía o plantilla | +5 |
| Interés | Tres o más visitas al sitio en siete días | +5 |
| Interés | Sin actividad en 60 días | -15 |

Tres reglas para que no se te desborde:

- **Los puntos negativos son tan importantes como los positivos.** Restar por correo personal, por puesto irrelevante o por inactividad es lo que evita que ventas reciba basura con puntuación alta.
- **La acción con intención de compra vale más que diez acciones de curiosidad.** Pedir una cotización debe pesar más que leer cinco artículos. Si tu modelo premia el volumen de clics, va a premiar a los curiosos.
- **El interés caduca.** Una visita a la página de precios de hace cuatro meses no dice nada de hoy. HubSpot, por ejemplo, permite configurar un decaimiento lineal de los puntos de interacción en intervalos de 1, 3, 6 o 12 meses; si tu herramienta no lo hace sola, resta puntos por inactividad como en la tabla.

## Qué umbral usar y qué pasa cuando se cruza

El umbral es la puntuación a partir de la cual un prospecto deja de ser responsabilidad de marketing y pasa a ventas. No hay un número universal; lo que hay es un método para encontrarlo: califica con tu modelo a los últimos 50 prospectos que ya sabes si compraron o no, ordénalos por puntuación y busca el corte donde la mayoría de los que están arriba compraron y la mayoría de los que están abajo no. Ese es tu umbral inicial. Suele caer entre 50 y 70 en una escala de 100.

Lo que ocurre al cruzarlo tiene que estar escrito, no sobreentendido:

1. El CRM asigna automáticamente al prospecto a un vendedor (por zona, por industria o por turno).
2. El vendedor recibe una notificación inmediata, no un reporte al día siguiente.
3. El vendedor tiene un tiempo máximo de primer contacto. Dada la evidencia sobre la primera hora, apunta a minutos.
4. Si el vendedor no lo trabaja en ese plazo, el prospecto se reasigna.
5. El vendedor registra el resultado del primer contacto en el CRM, aunque sea "no contestó".

Este acuerdo entre marketing y ventas (el SLA) es la parte del lead scoring que más se olvida y la que más resultados cambia. En la guía de [inbound marketing para empresas B2B](https://www.inbound.com.mx/inbound-marketing-para-empresas-b2b/) explicamos cómo redactar ese acuerdo cuando el ciclo de venta es largo.

Para los prospectos con alto ajuste pero bajo interés, el camino es la nutrición: una secuencia de correos alineada con el [buyer's journey](https://www.inbound.com.mx/buyer-journey-etapas-contenido/), que les acerque el contenido de la etapa en la que están y los mantenga sumando puntos hasta cruzar el umbral.

## Cómo configurarlo en el CRM

Un modelo de lead scoring se puede operar en una hoja de cálculo durante un par de meses, mientras lo calibras. Después conviene llevarlo al CRM, porque las señales de interés (visitas, clics, aperturas) solo las captura una herramienta conectada a tu sitio y a tu correo. Tomando HubSpot como referencia, según su propia documentación:

- La herramienta de calificación de leads está disponible en los planes Pro y Enterprise de Marketing Hub y Sales Hub; la calificación de contactos requiere Marketing Hub y la de negocios, Sales Hub.
- Cada calificación se guarda como una propiedad que puedes usar en vistas, segmentos, flujos de trabajo e informes, que es justamente lo que permite automatizar la asignación y la notificación al vendedor.
- Se pueden crear varias calificaciones por objeto, por ejemplo una por línea de negocio o una por región.
- Las calificaciones con inteligencia artificial requieren Marketing Hub Enterprise y una muestra mínima de 50 contactos, 25 que convirtieron y 25 que no, para detectar patrones.

Ese último punto es la respuesta a una pregunta frecuente: ¿conviene empezar con lead scoring predictivo? Solo si ya tienes historial suficiente y limpio. Para la mayoría de las pymes mexicanas el modelo manual de dos tablas es el punto de partida correcto, y la IA llega cuando hay datos para alimentarla. Si estás evaluando herramientas, en [HubSpot en México](https://www.inbound.com.mx/hubspot-mexico/) comparamos qué incluye cada plan.

Si tu presupuesto no alcanza para un plan de paga, las versiones gratuitas de varios CRM permiten registrar el ajuste al crear el contacto y marcar a mano las dos o tres acciones de interés que más pesan. Es menos elegante y funciona.

## Errores comunes al implementar lead scoring

- **Demasiados criterios.** Un modelo de 40 reglas es imposible de explicar a ventas y de calibrar. Empieza con cinco o seis por tipo.
- **Calificar sin datos.** Si tu formulario solo pide nombre y correo, no tienes con qué medir el ajuste. Agrega empresa, puesto y tamaño; los formularios cortos convierten más, pero un campo extra bien elegido vale la pérdida. Hay [consejos para que tus formularios generen leads](https://www.inbound.com.mx/infografia-5-consejos-para-que-tus-formularios-generen-leads/) sin volverse interrogatorios.
- **Puntuar la curiosidad como intención.** Diez visitas al blog no equivalen a una solicitud de cotización.
- **Nunca restar puntos.** Sin negativos, todo prospecto termina cruzando el umbral tarde o temprano.
- **No cerrar el ciclo con ventas.** Si el vendedor no registra qué pasó con cada prospecto calificado, no hay forma de saber si el modelo acierta.
- **Dejarlo fijo.** Revisa cada trimestre: ¿qué porcentaje de los prospectos que cruzaron el umbral se convirtió en cliente? ¿Qué criterios tenían en común los que no? Ajusta los puntos con esa información.

## Cómo saber si tu lead scoring funciona

Mide tres cosas, una vez al mes, con los mismos [KPIs](https://www.inbound.com.mx/kpis-web/) que ya revisas:

1. **Tasa de conversión de prospecto calificado a cliente.** Si sube con el tiempo, el modelo está filtrando bien.
2. **Tiempo de primer contacto de los prospectos calificados.** Si no baja, el problema no es el modelo sino el SLA.
3. **Porcentaje de prospectos calificados que ventas rechaza.** Si ventas devuelve más del 20% o 30% como "no sirven", hay criterios de ajuste mal puestos o un umbral demasiado bajo.

Cuando marketing y ventas dejan de discutir sobre la calidad de los prospectos y empiezan a discutir sobre los números del modelo, el lead scoring está funcionando.

## Preguntas frecuentes

### ¿Qué es el lead scoring en pocas palabras?

Es un sistema de puntos que califica a cada prospecto según qué tanto se parece a tu cliente ideal (ajuste) y qué tanto interés muestra en comprar (comportamiento). El total ordena a quién debe atender ventas primero.

### ¿Cuántos puntos necesita un prospecto para pasar a ventas?

Depende de tu modelo, pero en una escala de 0 a 100 el umbral suele caer entre 50 y 70. La forma correcta de fijarlo es calificar a prospectos pasados de los que ya conoces el resultado y buscar el corte que mejor separa a los que compraron de los que no.

### ¿Necesito un CRM de paga para hacer lead scoring?

No para empezar. Puedes calificar en una hoja de cálculo durante uno o dos meses mientras calibras el modelo. La puntuación automática por comportamiento sí requiere una herramienta conectada a tu sitio y tu correo, que en HubSpot, por ejemplo, está en los planes Pro y Enterprise.

### ¿Qué diferencia hay entre lead scoring manual y predictivo?

En el manual tú decides los criterios y los puntos. En el predictivo, un algoritmo encuentra los patrones en tu historial de conversiones. El predictivo necesita datos suficientes y limpios; HubSpot, por ejemplo, pide al menos 50 contactos con 25 convertidos y 25 no convertidos. Para la mayoría de las pymes el manual es el punto de partida.

### ¿Cada cuánto debo revisar el modelo?

Cada trimestre. Compara la puntuación que tenían los prospectos con su resultado real (compró o no compró), revisa qué criterios tenían en común los falsos positivos y ajusta los puntos. Un modelo que no se revisa pierde precisión conforme cambia tu mercado.

### ¿El lead scoring sirve para empresas que venden a consumidores?

Sí, con criterios distintos. En B2C el ajuste suele medirse con ubicación, rango de edad o tipo de producto que le interesa, y el interés con acciones como agregar al carrito, pedir una cita o volver varias veces a la misma página. El principio es el mismo: separar quién puede comprar de quién está a punto de hacerlo.

## Fuentes

- [Comprender la herramienta de calificación de leads, Base de conocimientos de HubSpot](https://knowledge.hubspot.com/es/scoring/understand-the-lead-scoring-tool)
- [The Short Life of Online Sales Leads, Harvard Business Review, marzo de 2011](https://hbr.org/2011/03/the-short-life-of-online-sales-leads)
- [How to Handle the Ticking Time Bomb That Is an Inbound Lead, HubSpot](https://blog.hubspot.com/sales/how-to-handle-the-ticking-time-bomb-that-is-an-inbound-lead)
- [State of Sales 2024 de Salesforce, resumen en Diginomica, agosto de 2024](https://diginomica.com/state-sales-ai-incoming-there-are-caveats-according-salesforce-data)
- [Censos Económicos 2024, resultados definitivos, INEGI, julio de 2025](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def_RR.pdf)

**Sigue leyendo:**

- [Buyer's journey: qué contenido necesita cada etapa](https://www.inbound.com.mx/buyer-journey-etapas-contenido/)
- [Cómo crear un buyer persona](https://www.inbound.com.mx/buyer-persona/)
- [Inbound marketing para empresas B2B](https://www.inbound.com.mx/inbound-marketing-para-empresas-b2b/)

¿Quieres saber si tus prospectos están llegando a ventas en el orden correcto? [Pide un diagnóstico gratis](https://www.inbound.com.mx/contacto/) y revisamos contigo tu modelo de calificación.

<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"¿Qué es el lead scoring en pocas palabras?","acceptedAnswer":{"@type":"Answer","text":"Es un sistema de puntos que califica a cada prospecto según qué tanto se parece a tu cliente ideal (ajuste) y qué tanto interés muestra en comprar (comportamiento). El total ordena a quién debe atender ventas primero."}},{"@type":"Question","name":"¿Cuántos puntos necesita un prospecto para pasar a ventas?","acceptedAnswer":{"@type":"Answer","text":"Depende de tu modelo, pero en una escala de 0 a 100 el umbral suele caer entre 50 y 70. La forma correcta de fijarlo es calificar a prospectos pasados de los que ya conoces el resultado y buscar el corte que mejor separa a los que compraron de los que no."}},{"@type":"Question","name":"¿Necesito un CRM de paga para hacer lead scoring?","acceptedAnswer":{"@type":"Answer","text":"No para empezar. Puedes calificar en una hoja de cálculo durante uno o dos meses mientras calibras el modelo. La puntuación automática por comportamiento sí requiere una herramienta conectada a tu sitio y tu correo, que en HubSpot, por ejemplo, está en los planes Pro y Enterprise."}},{"@type":"Question","name":"¿Qué diferencia hay entre lead scoring manual y predictivo?","acceptedAnswer":{"@type":"Answer","text":"En el manual tú decides los criterios y los puntos. En el predictivo, un algoritmo encuentra los patrones en tu historial de conversiones. El predictivo necesita datos suficientes y limpios; HubSpot, por ejemplo, pide al menos 50 contactos con 25 convertidos y 25 no convertidos. Para la mayoría de las pymes el manual es el punto de partida."}},{"@type":"Question","name":"¿Cada cuánto debo revisar el modelo?","acceptedAnswer":{"@type":"Answer","text":"Cada trimestre. Compara la puntuación que tenían los prospectos con su resultado real (compró o no compró), revisa qué criterios tenían en común los falsos positivos y ajusta los puntos. Un modelo que no se revisa pierde precisión conforme cambia tu mercado."}},{"@type":"Question","name":"¿El lead scoring sirve para empresas que venden a consumidores?","acceptedAnswer":{"@type":"Answer","text":"Sí, con criterios distintos. En B2C el ajuste suele medirse con ubicación, rango de edad o tipo de producto que le interesa, y el interés con acciones como agregar al carrito, pedir una cita o volver varias veces a la misma página. El principio es el mismo: separar quién puede comprar de quién está a punto de hacerlo."}}]}</script>
