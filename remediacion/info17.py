from comun import *

POSTS = [
dict(
id=2283, slug="infografia-etapas-del-desarrollo-cognitivo",
title="Desarrollo cognitivo: Piaget, Vygotsky y Gardner",
excerpt="Infografía del desarrollo cognitivo: las 4 etapas de Piaget, la teoría sociocultural de Vygotsky y las 9 inteligencias múltiples de Gardner, con ideas para aplicarlas.",
img_alt="Infografía de las etapas del desarrollo cognitivo según Piaget, Vygotsky y Gardner",
body=f"""
¿Cómo aprende una persona? Tres pensadores dieron respuestas que siguen guiando la educación: Jean Piaget, Lev Vygotsky y Howard Gardner. Esta infografía resume sus teorías.

{{IMG}}

## Jean Piaget: las etapas del desarrollo cognitivo

Piaget estudió cómo piensan los niños y propuso cuatro etapas:

1. **Sensoriomotora (0 a 2 años).** El niño se relaciona con el mundo a través de los sentidos y la acción. *Estimulación:* aprendizaje por ensayo y error, juegos de esconder objetos.
2. **Preoperacional (2 a 7 años).** Aparece la función simbólica (imágenes y palabras), el pensamiento es egocéntrico y aún no comprende que ciertas características se conservan. *Estimulación:* adaptarse a su pensamiento, permitir la experimentación y usar símbolos en los juegos.
3. **Operaciones concretas (7 a 12 años).** El pensamiento se vuelve lógico y reversible; puede ponerse en el lugar del otro y ordenar objetos por categorías. *Estimulación:* ayudarle a plantear preguntas y razonar sobre hechos concretos.
4. **Operaciones formales (12 años en adelante).** Pensamiento abstracto, hipótesis y deducciones. *Estimulación:* debates, análisis de problemas éticos y paso de lo concreto a lo abstracto.

La infografía también recoge críticas: Piaget habría subestimado a los niños, sus etapas serían demasiado rígidas y no tomó en cuenta las influencias sociales y culturales.

## Lev Vygotsky: la teoría sociocultural

Pone la cultura en primer plano. Los procesos mentales se construyen en la interacción social. Sus cinco elementos: funciones mentales, herramientas del pensamiento (como el lenguaje), mediación, habilidades psicológicas y la **zona de desarrollo próximo**: lo que una persona aún no puede hacer sola, pero sí con ayuda.

## Howard Gardner: las inteligencias múltiples

Propone nueve tipos de inteligencia: espacial, lingüística, lógico-matemática, kinestésica, musical, interpersonal, intrapersonal, naturalista y existencial. Todos las tenemos en distinta medida.

## Fuera del salón

Estas ideas también sirven para capacitar equipos: aprender con otros (Vygotsky), explicar con ejemplos concretos antes de lo abstracto (Piaget) y usar distintos formatos para distintas personas (Gardner). Revisa los [consejos para maestros]({S}/infografia-7-consejos-para-maestros-al-inicio-del-ciclo-escolar/).
""",
faq=[
("¿Cuáles son las etapas del desarrollo cognitivo de Piaget?", "Sensoriomotora (0 a 2 años), preoperacional (2 a 7), operaciones concretas (7 a 12) y operaciones formales (12 en adelante)."),
("¿Qué es la zona de desarrollo próximo?", "Es un concepto de Vygotsky: la distancia entre lo que una persona puede hacer sola y lo que puede lograr con la ayuda de otra más experimentada."),
("¿Cuáles son las inteligencias múltiples de Gardner?", "Espacial, lingüística, lógico-matemática, kinestésica, musical, interpersonal, intrapersonal, naturalista y existencial."),
],
related=[("7 consejos para maestros", S + "/infografia-7-consejos-para-maestros-al-inicio-del-ciclo-escolar/"), ("5 factores de la inteligencia emocional", S + "/infografia-5-factores-de-inteligencia-emocional/")],
),

dict(
id=2241, slug="infografia-metodo-canvas",
title="Modelo Canvas: qué es y cómo usarlo (infografía)",
excerpt="Infografía del modelo Canvas para validar modelos de negocio: sus 9 bloques, desde segmentos de clientes y propuesta de valor hasta fuentes de ingresos y estructura de costos.",
img_alt="Infografía del modelo Canvas para modelos de negocio",
credit="Infografía: marketingyfinanzas.net.",
body=f"""
Un plan de negocio de 40 páginas que nadie lee, o una sola hoja que todo tu equipo entiende. El modelo Canvas, creado por Alexander Osterwalder, es la segunda opción: una herramienta para diseñar, probar y validar modelos de negocio.

{{IMG}}

## Los 9 bloques del Canvas

1. **Segmento de clientes.** A quién te diriges, qué problemas y necesidades tiene.
2. **Propuesta de valor.** Qué tienes tú que no tengan los demás y por lo que la gente está dispuesta a pagar.
3. **Canales.** Cómo llega tu propuesta de valor a tus clientes.
4. **Relación con clientes.** Tu cliente es lo más importante: define qué tipo de relación tendrás con él.
5. **Fuentes de ingresos.** Cuál es la rentabilidad; cómo y por dónde llegarán tus ingresos.
6. **Recursos clave.** Qué necesitas para que el modelo funcione.
7. **Actividades clave.** Lo que tienes que hacer bien para que el negocio tenga éxito.
8. **Socios clave.** La gente con la que debes trabajar para que la propuesta de valor suceda.
9. **Estructura de costos.** La inversión, costos fijos y variables.

La infografía cierra con un recordatorio: tu producto o servicio debe incluir creatividad e innovación.

## Cómo usarlo

1. **Empieza por la derecha:** clientes y propuesta de valor. Si eso no está claro, lo demás no importa.
2. **Escribe en notas adhesivas.** El Canvas está hecho para cambiar.
3. **Marca qué es hipótesis** y qué ya validaste con clientes.
4. **Haz versiones.** Compara escenarios: otro segmento, otro canal, otro modelo de precio.

Para el bloque de clientes, apóyate en tu [buyer persona]({BUYER}) y el [mapa de empatía]({S}/infografia-mapa-de-la-empatia/). Para el resto, revisa [cómo hacer un plan de empresa]({S}/infografia-como-hacer-un-plan-de-empresa/).
""",
faq=[
("¿Qué es el modelo Canvas?", "Es una herramienta creada por Alexander Osterwalder para describir, diseñar y validar modelos de negocio en una sola hoja con nueve bloques."),
("¿Cuáles son los 9 bloques del Canvas?", "Segmento de clientes, propuesta de valor, canales, relación con clientes, fuentes de ingresos, recursos clave, actividades clave, socios clave y estructura de costos."),
("¿Por dónde empezar a llenar el Canvas?", "Por el segmento de clientes y la propuesta de valor, porque el resto del modelo depende de ellos."),
],
related=[("Cómo hacer un plan de empresa", S + "/infografia-como-hacer-un-plan-de-empresa/"), ("Mapa de empatía", S + "/infografia-mapa-de-la-empatia/")],
),

dict(
id=1633, slug="infografia-como-conseguir-una-insignia-de-verificacion-en-redes-sociales",
title="Cómo verificar tu cuenta en redes sociales",
excerpt="Infografía de cómo conseguir la insignia de verificación en Facebook, Twitter, Instagram y YouTube, con los requisitos de entonces y cómo funciona hoy la verificación de pago.",
img_alt="Infografía de cómo conseguir una insignia de verificación en redes sociales",
credit="Infografía: Adveischool.",
body=f"""
La palomita azul junto al nombre da confianza: confirma que esa cuenta es realmente de quien dice ser. Esta infografía explicaba cómo se obtenía en cada red. Las reglas cambiaron mucho, así que aquí tienes las dos versiones.

{{IMG}}

## Lo que decía la infografía

- **Facebook:** había dos insignias, azul para perfiles muy conocidos y gris para empresas.
- **Twitter:** habilitaba la verificación para cuentas de música, cine, moda, política, religión, medios, deportes, negocios y otras áreas de interés.
- **Instagram:** la plataforma la concedía a perfiles con riesgo de suplantación, como personajes famosos.
- **YouTube:** la reservaba para canales con más de 100,000 suscriptores.

## Cómo funciona hoy

- **Meta (Facebook e Instagram):** además de la verificación por notoriedad, existe **Meta Verified**, una suscripción de pago que verifica la identidad y da la insignia a perfiles y empresas que cumplen requisitos.
- **X (antes Twitter):** la insignia azul se obtiene con la suscripción de pago; las organizaciones tienen una insignia dorada y los gobiernos, gris.
- **YouTube:** mantiene el umbral de 100,000 suscriptores para solicitarla, entre otros requisitos.
- **LinkedIn:** permite verificar identidad y lugar de trabajo.

Los requisitos y precios cambian con frecuencia; consúltalos en el centro de ayuda de cada red.

## ¿Le conviene a tu empresa?

La verificación ayuda cuando hay riesgo de cuentas falsas que se hagan pasar por ti, o cuando atiendes clientes por mensajes y quieres que confíen en que hablan con la cuenta oficial. Pero no sustituye lo básico: contenido útil, respuestas rápidas y una buena [reputación online]({S}/infografia-por-que-debes-de-proteger-tu-reputacion-online/).
""",
faq=[
("¿Cómo verificar una cuenta de Instagram o Facebook?", "Hoy, además de la verificación por notoriedad, Meta ofrece Meta Verified, una suscripción de pago que verifica la identidad del perfil o la empresa si cumple los requisitos."),
("¿Cuántos suscriptores necesito para verificar un canal de YouTube?", "YouTube pide al menos 100,000 suscriptores para solicitar la insignia de verificación, entre otros requisitos."),
("¿Cómo se obtiene la palomita azul en X (Twitter)?", "Con la suscripción de pago de la plataforma, sujeta a requisitos; las organizaciones verificadas tienen una insignia dorada."),
],
related=[("Por qué proteger tu reputación online", S + "/infografia-por-que-debes-de-proteger-tu-reputacion-online/"), ("Seguridad en redes sociales", S + "/infografia-buenas-practicas-para-la-seguridad-de-la-informacion-en-la-gestion-de-redes-sociales/")],
),

dict(
id=2149, slug="infografia-algunos-cambios-de-nombre-de-empresas-muy-conocidas",
title="Nombres originales de empresas famosas (infografía)",
excerpt="Infografía de cambios de nombre de empresas famosas: BackRub se volvió Google, Brad's Drink fue Pepsi y Confinity pasó a PayPal. Qué enseñan sobre naming y marca.",
img_alt="Infografía de cambios de nombre de empresas muy conocidas",
body=f"""
¿Le comprarías un refresco a Brad's Drink? ¿Buscarías algo en BackRub? Muchas de las marcas más conocidas del mundo empezaron con nombres muy distintos. Esta infografía reúne algunos de los cambios más sonados.

{{IMG}}

## Los cambios

| Nombre original | Nombre actual | Desde |
| --- | --- | --- |
| BackRub | Google | 1998 |
| Lucky Goldstar | LG | 1995 |
| Marufuku Co. Ltd. | Nintendo | 1963 |
| America Online | AOL | 2006 |
| Brad's Drink | Pepsi | 1961 |
| Jerry's Guide to the World Wide Web | Yahoo! | 1994 |
| Sound of Music | Best Buy | 1983 |
| Research In Motion | BlackBerry | 2013 |
| Blue Ribbon Sports | Nike | 1971 |
| AuctionWeb | eBay | 1997 |
| Pete's Super Submarines | Subway | 1968 |
| Confinity | PayPal | 1999 |

## Por qué cambian de nombre

- **El nombre original era demasiado largo o difícil** (Jerry's Guide to the World Wide Web).
- **El negocio creció más allá de su origen** (Sound of Music vendía equipos de audio; Best Buy vende de todo).
- **El producto estrella se volvió la marca** (Research In Motion pasó a BlackBerry).
- **Para simplificar y globalizar** (Lucky Goldstar a LG).

Y en tiempos recientes: Facebook pasó a llamarse Meta en 2021 y Twitter se convirtió en X en 2023.

## Si estás nombrando tu negocio

1. **Fácil de decir, escribir y recordar.**
2. **Que no te encierre:** piensa si seguirá funcionando si creces.
3. **Revisa disponibilidad** del dominio, las redes y el registro de marca ante el IMPI.
4. **Pruébalo en voz alta** con clientes potenciales.

Cambiar de nombre es posible, pero cuesta. Revisa también [colores y su relación con la publicidad]({S}/infografia-los-colores-y-su-relacion-con-la-publicidad/).
""",
faq=[
("¿Cuál era el nombre original de Google?", "BackRub. Cambió a Google en 1998."),
("¿Cómo se llamaba Pepsi originalmente?", "Brad's Drink; adoptó el nombre Pepsi-Cola y después Pepsi."),
("¿Qué revisar antes de elegir el nombre de un negocio?", "Que sea fácil de recordar, que no limite el crecimiento y que estén disponibles el dominio, las redes sociales y el registro de marca."),
],
related=[("Los colores y la publicidad", S + "/infografia-los-colores-y-su-relacion-con-la-publicidad/"), ("Historia de Instagram", S + "/infografia-historia-de-instagram/")],
),

dict(
id=2181, slug="infografia-la-sociedad-de-la-informacion-en-el-mundo",
title="La sociedad de la información en el mundo",
excerpt="Infografía de la sociedad de la información: penetración de telefonía fija, móvil e internet por región, cuota de usuarios por continente y crecimiento del tráfico de datos.",
img_alt="Infografía de la sociedad de la información en el mundo",
credit="Infografía con datos de la UIT (ICT Facts and Figures 2016) y Cisco Visual Networking Index.",
body=f"""
En 2016 se cruzó una línea simbólica: más de la mitad de los hogares del mundo ya tenía internet. Esta infografía muestra cómo estaba repartido el acceso a las comunicaciones por región.

{{IMG}}

## Lo que muestra la infografía

**Penetración por región.** Compara telefonía fija, telefonía móvil e internet en Norteamérica, América Latina, la Unión Europea, el resto de Europa, los países árabes, África, Asia (China, las grandes economías, Oriente Medio y el resto) y Oceanía. Las diferencias son enormes, sobre todo en internet.

**Usuarios de telefonía móvil por región.** Asia concentra la mayor parte, con China como el país con más usuarios; África representa una proporción importante, por encima de América Latina y el Caribe.

**Usuarios de internet por región.** También dominados por Asia, con China a la cabeza y el resto de Asia y Oceanía con una gran parte; Norteamérica, Europa, América Latina y África completan el reparto.

**Tráfico de datos.** En 2016, el tráfico IP creció 22.5% frente a 2015, hasta 88.7 exabytes al mes. Para 2020 se esperaba que dos terceras partes vinieran de dispositivos inalámbricos y móviles.

## Lo que pasó después

La conectividad siguió creciendo y hoy la mayoría de la población mundial usa internet, casi siempre desde el celular. En México, según las encuestas del INEGI, más de tres cuartas partes de la población de 6 años o más usa internet.

## Lo que significa para tu negocio

- **Tu cliente está en el celular.** Sitio, anuncios y atención deben pensarse para móvil.
- **El video y los datos móviles crecen sin parar.** Optimiza el peso de tus páginas e imágenes.
- **Todavía hay brechas.** Si atiendes zonas rurales o públicos mayores, combina canales digitales con teléfono y atención presencial.

Revisa [5 tendencias tecnológicas]({S}/infografia-5-tendencias-tecnologicas-que-cambiaran-el-mundo/).
""",
faq=[
("¿Cuántos hogares tenían internet en 2016?", "Según la infografía, más de la mitad de los hogares del mundo ya contaba con conexión a internet."),
("¿Qué región concentra más usuarios de internet?", "Asia, con China como el país con más usuarios."),
("¿Cuánto creció el tráfico de datos en 2016?", "El tráfico IP creció 22.5% respecto a 2015, hasta 88.7 exabytes al mes, de acuerdo con la infografía."),
],
related=[("5 tendencias tecnológicas", S + "/infografia-5-tendencias-tecnologicas-que-cambiaran-el-mundo/"), ("Chile: el consumidor conectado", S + "/infografia-chile-el-consumidor-conectado/")],
),

dict(
id=2105, slug="infografia-posicionamiento-seo-una-estrategia-que-debe-tener-siempre-objetivos",
title="Cómo medir cada objetivo de tu estrategia SEO",
excerpt="Infografía de los objetivos de una estrategia SEO y cómo medir cada uno: visibilidad, tráfico, posicionamiento de marca, conversiones, contenido y ventas en línea.",
img_alt="Infografía de posicionamiento SEO, una estrategia que debe tener siempre objetivos",
credit="Infografía: JACN Creative Network.",
body=f"""
Definir objetivos SEO es el primer paso; el segundo es saber si los estás cumpliendo. Esta infografía repasa los objetivos de una estrategia de posicionamiento. Aquí nos enfocamos en cómo medir cada uno.

{{IMG}}

## Los objetivos y cómo medirlos

| Objetivo | Qué medir | Dónde |
| --- | --- | --- |
| Visibilidad | Impresiones y posición promedio de tus páginas | Google Search Console |
| Tráfico | Clics orgánicos y sesiones desde buscadores | Search Console y Google Analytics 4 |
| Popularidad y marca | Búsquedas de tu marca y enlaces de otros sitios | Search Console (consultas de marca) y herramientas de enlaces |
| Conversión | Formularios, descargas, suscripciones, llamadas y clics a WhatsApp desde tráfico orgánico | Google Analytics 4 con eventos configurados |
| Contenido | Visitas por artículo, tiempo de lectura y conversiones asistidas | Google Analytics 4 |
| Venta en línea | Ingresos e ingresos por visita del canal orgánico | Analytics de comercio electrónico o tu plataforma de tienda |

## Lo que recuerda la infografía

- **El posicionamiento de marca** busca recordación, popularidad y mayor interés de búsqueda.
- **La conversión es responsabilidad compartida:** el SEO trae prospectos, pero cerrar la venta depende también del equipo comercial y del servicio.
- **El marketing de contenidos** alimenta la visibilidad con contenido original y relevante.
- **El SEO para venta en línea** se apoya en herramientas como Google Shopping y en las valoraciones de los compradores.

## Una rutina mensual de 30 minutos

1. Revisa en Search Console las páginas que más crecieron y las que más cayeron.
2. Identifica consultas con muchas impresiones y pocos clics: mejora título y descripción.
3. Revisa conversiones orgánicas en Analytics.
4. Elige una página para actualizar ese mes.

Para el contexto completo, lee [posicionamiento SEO: define tus objetivos]({S}/infografia-posicionamiento-seo-una-estrategia-de-debe-tener-objetivos/) y estos [KPIs para tu sitio]({KPIS}).
""",
faq=[
("¿Cómo medir los resultados de una estrategia SEO?", "Con Google Search Console para impresiones, clics y posiciones, y con Google Analytics 4 para tráfico, conversiones e ingresos del canal orgánico."),
("¿Qué es una conversión orgánica?", "Es una acción valiosa, como enviar un formulario o comprar, realizada por un visitante que llegó desde buscadores sin anuncios pagados."),
("¿Cada cuánto revisar el SEO de un sitio?", "Una revisión mensual de indicadores y páginas clave suele ser suficiente para detectar oportunidades y caídas a tiempo."),
],
related=[("Posicionamiento SEO: define tus objetivos", S + "/infografia-posicionamiento-seo-una-estrategia-de-debe-tener-objetivos/"), ("KPIs para tu sitio web", KPIS)],
),

dict(
id=1933, slug="infografia-community-manager-vs-social-media-strategist",
title="Community manager vs. social media strategist",
excerpt="Infografía de las funciones del community manager y del social media strategist: quién ejecuta y conversa con la comunidad, y quién define la estrategia y mide resultados.",
img_alt="Infografía de funciones del community manager y el social media strategist",
credit="Infografía: @RosanaRosas17. Hecha con Piktochart.",
body=f"""
Muchas empresas contratan "a alguien para redes" y esperan que haga estrategia, contenido, atención, publicidad y reportes. Son dos roles distintos. Esta infografía explica la diferencia.

{{IMG}}

## Community manager: la voz de la marca

Es el intermediario entre la marca y su público: comunica el mensaje de la empresa y, a la vez, lleva a la empresa las necesidades y propuestas de la audiencia.

**Sus funciones:**
- Analizar las comunidades: identificar, localizar, medir y comprender.
- Interactuar con la audiencia y atender preguntas, comentarios y quejas.
- Manejar y actualizar el contenido en los distintos medios sociales.
- Aportar creatividad y buen contenido.
- Escuchar y analizar a los usuarios.
- Identificar oportunidades de colaboración.
- Resolver crisis puntuales y responder a críticas.
- Atraer nuevos seguidores y convertir a los críticos en seguidores.
- Preparar informes para el social media strategist.

## Social media strategist: el que define el rumbo

Establece las estrategias de la marca en medios sociales: planes de acción, planes de crisis, reputación en línea y marketing de contenidos.

**Sus funciones:**
- Desarrollar estrategias innovadoras y efectivas en redes.
- Definir la estrategia de contenido, el estilo de comunicación y el calendario.
- Comunicar el mensaje de la empresa en la red.
- Definir campañas: promociones, concursos, publicidad, eventos y lanzamientos.
- Monitorear tendencias y herramientas.
- Medir el impacto de las acciones de marketing en redes.
- Buscar oportunidades de negocio e innovación.
- Crear estrategias de crisis y de fidelización.
- Dar seguimiento a la reputación en línea.
- Analizar los reportes del community manager.

## ¿Necesitas los dos?

En una pyme, a veces una persona hace ambos. Funciona si sabe dónde está cada sombrero y tiene tiempo para los dos. Si no, lo común es que la ejecución diaria se coma la estrategia. Una opción: estrategia externa (una agencia o consultor) y ejecución interna. Revisa las [8 tareas de un community manager]({S}/infografia-8-tareas-de-un-community-manager-en-una-empresa/) y [cómo hacer un presupuesto de redes]({S}/infografia-como-hacer-un-presupuesto-de-marketing-en-redes-sociales/).
""",
faq=[
("¿Qué diferencia hay entre community manager y social media strategist?", "El community manager ejecuta y conversa con la comunidad día a día; el social media strategist define la estrategia, las campañas y mide los resultados."),
("¿Qué hace un social media strategist?", "Diseña la estrategia de redes, define contenido y calendario, planea campañas, prepara planes de crisis, mide el impacto y analiza los reportes del community manager."),
("¿Una pyme necesita ambos roles?", "Puede combinarlos en una persona si tiene tiempo para la estrategia, o apoyarse en una agencia para la estrategia y mantener la ejecución interna."),
],
related=[("8 tareas de un community manager", S + "/infografia-8-tareas-de-un-community-manager-en-una-empresa/"), ("Presupuesto de redes sociales", S + "/infografia-como-hacer-un-presupuesto-de-marketing-en-redes-sociales/")],
),

dict(
id=2117, slug="infografia-snapchat-tiene-muchos-usuarios-que-no-utilizan-otras-redes",
title="Snapchat y su público exclusivo (infografía)",
excerpt="Infografía del público exclusivo de Snapchat: qué porcentaje de sus usuarios no usa Facebook, Instagram, Messenger, YouTube, Twitter o WhatsApp en un día cualquiera.",
img_alt="Infografía de Snapchat y su público exclusivo",
credit="Infografía: Business Insider, con datos de App Annie.",
body=f"""
Si una marca está en Facebook e Instagram, ¿ya llega a todos? Esta gráfica sugería que no: muchos usuarios diarios de Snapchat en Estados Unidos no usaban otras plataformas ese mismo día.

{{IMG}}

## Lo que muestra la gráfica

Porcentaje de usuarios diarios de Snapchat en EE. UU. que **no** usaban otra plataforma en un día cualquiera (público exclusivo) frente a los que sí la usaban (público compartido):

| Plataforma | Exclusivo de Snapchat | Compartido |
| --- | --- | --- |
| Facebook | 35% | 65% |
| Instagram | 46% | 54% |
| Messenger | 58% | 42% |
| YouTube | 61% | 39% |
| Twitter | 81% | 19% |
| WhatsApp | 93% | 7% |

Datos de usuarios mayores de 13 años en iPhone y Android, según App Annie.

## La lección

**Cada red tiene un público parcialmente propio.** Estar en una no garantiza llegar a quienes usan otra. Por eso conviene:

1. **Saber dónde está tu cliente ideal,** no dónde están "todos".
2. **No duplicar todo en todas las redes:** elige las que tu público usa a diario.
3. **Revisar datos de tu propio mercado.** Estas cifras son de EE. UU.; en México, por ejemplo, WhatsApp tiene un uso mucho más amplio.

Snapchat perdió relevancia en muchos mercados frente a Instagram Stories y TikTok, pero la idea de fondo sigue vigente. Revisa la [demografía de las redes sociales]({S}/infografia-demografia-de-las-redes-sociales/).
""",
faq=[
("¿Qué porcentaje de usuarios de Snapchat no usa Facebook?", "Según la gráfica, 35% de los usuarios diarios de Snapchat en EE. UU. no usaba Facebook ese mismo día."),
("¿Qué significa público exclusivo de una red social?", "Son los usuarios de una red que no usan otra plataforma determinada, por lo que solo se les puede alcanzar en esa red."),
("¿Una marca debe estar en todas las redes sociales?", "No necesariamente. Conviene estar donde está su cliente ideal y entender que cada red tiene un público en parte propio."),
],
related=[("Demografía de las redes sociales", S + "/infografia-demografia-de-las-redes-sociales/"), ("Redes sociales en cifras", S + "/infografia-redes-sociales-en-cifras/")],
),

dict(
id=2291, slug="infografia-8-reglas-de-oro-para-invertir-en-bolsa",
title="8 reglas de oro para invertir en bolsa (infografía)",
excerpt="Infografía con 8 reglas de oro para invertir en bolsa: fórmate, invierte dinero que no necesitas, analiza, sigue la tendencia, controla el riesgo, diversifica y fija objetivos.",
img_alt="Infografía de 8 reglas de oro para invertir en bolsa",
body=f"""
Invertir en bolsa ya no es solo para expertos: hoy cualquiera puede abrir una cuenta desde el celular. Justo por eso conviene tener reglas claras antes de empezar. Esta infografía propone ocho.

{{IMG}}

## Las reglas

1. **Fórmate e infórmate.** Domina lo básico: comisiones, tipos de órdenes, cómo funciona el mercado.
2. **Invierte dinero ocioso.** No arriesgues el dinero que vas a necesitar a corto plazo.
3. **Analiza y selecciona tus inversiones.** Nunca compres por impulso o intuición; apóyate en el análisis técnico o fundamental.
4. **Si no la ves clara, no inviertas.** No hacer una operación también es una decisión de inversión.
5. **Ponte a favor de la tendencia.** Detecta si el mercado es alcista o bajista y opera a su favor.
6. **Controla el riesgo.** Usa un *stop loss* que limite tu pérdida máxima. Cuando pierdas, pierde poco.
7. **Diversifica.** No pongas todos los huevos en la misma canasta: distintas empresas, sectores y países.
8. **Márcate un objetivo.** No cortes las ganancias por ansiedad, pero define una meta realista.

## Antes de tu primera inversión

- **Ten un fondo de emergencia** de varios meses de gastos.
- **Paga deudas caras** (tarjetas de crédito) antes de invertir.
- **Define tu horizonte:** ¿cuándo vas a necesitar ese dinero?
- **Empieza con instrumentos diversificados,** como fondos indexados, si no tienes tiempo para analizar empresas.
- **Usa casas de bolsa y plataformas reguladas** por la CNBV.

Este contenido es informativo y no es una recomendación de inversión. Consulta a un asesor financiero antes de invertir. Revisa también [los mercados de valores más caros del mundo]({S}/infografia-los-mercados-de-valores-mas-caros-del-mundo/).
""",
faq=[
("¿Qué reglas seguir para invertir en bolsa?", "Formarte, invertir solo dinero que no necesitas a corto plazo, analizar antes de comprar, operar a favor de la tendencia, controlar el riesgo, diversificar y fijar objetivos."),
("¿Qué es un stop loss?", "Es una orden que vende automáticamente una inversión si cae a cierto precio, para limitar la pérdida máxima."),
("¿Qué es diversificar una inversión?", "Repartir el dinero entre distintas empresas, sectores, países o instrumentos para reducir el riesgo."),
],
related=[("Los mercados de valores más caros", S + "/infografia-los-mercados-de-valores-mas-caros-del-mundo/"), ("Bitcoin no es la única criptomoneda", S + "/infografia-el-bitcoin-no-es-la-unica-criptomoneda/")],
),

dict(
id=2279, slug="infografia-7-pautas-para-crear-tu-estrategia-de-experiencia-del-cliente",
title="7 pautas para tu estrategia de experiencia del cliente",
excerpt="Infografía con 7 pautas para crear tu estrategia de experiencia del cliente: principios, personajes, conexión emocional, encuestas, formación, escucha al equipo y NPS.",
img_alt="Infografía de 7 pautas para crear tu estrategia de experiencia del cliente",
credit="Infografía con base en un artículo de Adriana González (Marketeros de Hoy). Hecha con Piktochart.",
body=f"""
Tu cliente no recuerda tu producto en abstracto. Recuerda cómo se sintió al comprarlo, al pedir ayuda y al resolver un problema. Esa es la experiencia del cliente, y esta infografía da siete pautas para diseñarla.

{{IMG}}

## Las 7 pautas

1. **Define principios.** Establece cómo quieres que se sienta el cliente al interactuar con tu marca. Todo el equipo debe conocerlos y aplicarlos.
2. **Crea personajes.** Ayuda al equipo a ponerse en los zapatos del cliente. Por ejemplo: María, 20 años, ama la tecnología y prefiere redes sociales; Beatriz, 50 años, prefiere el teléfono y que la atienda una persona.
3. **Conecta emocionalmente.** Haz sentir al cliente especial; así se construye la lealtad.
4. **Pregunta después de cada interacción.** Una encuesta breve al cerrar la atención.
5. **Detecta necesidades de formación** del equipo y monitorea la calidad del servicio.
6. **Escucha a tu equipo.** La información que tiene la gente de primera línea sirve para mejorar.
7. **Mide con NPS.** El Net Promoter Score pregunta: "¿Recomendarías esta empresa a un amigo o familiar?".

## Cómo empezar esta semana

- **Recorre tu propio proceso** como cliente: cotiza, compra, pide soporte. Anota cada fricción.
- **Lee tus últimas 20 reseñas** y agrupa los temas que se repiten.
- **Elige una mejora** y hazla.

La experiencia es lo que hace que tus clientes vuelvan y te recomienden. Revisa [cómo hacer que tus clientes te recomienden]({RECOMIENDEN}) y el [mapa de empatía]({S}/infografia-mapa-de-la-empatia/).
""",
faq=[
("¿Qué es la experiencia del cliente?", "Es la percepción que tiene el cliente de todas sus interacciones con una marca, desde que la conoce hasta después de comprar."),
("¿Qué es el NPS?", "El Net Promoter Score es un indicador que mide la probabilidad de que un cliente recomiende la empresa a un amigo o familiar."),
("¿Cómo mejorar la experiencia del cliente?", "Definiendo principios de servicio, entendiendo a distintos tipos de clientes, conectando emocionalmente, preguntando su opinión después de cada interacción, capacitando al equipo y midiendo con indicadores como el NPS."),
],
related=[("Cómo hacer que tus clientes te recomienden", RECOMIENDEN), ("Mapa de empatía", S + "/infografia-mapa-de-la-empatia/")],
),
]
