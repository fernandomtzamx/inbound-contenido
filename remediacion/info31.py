from comun import *

POSTS = [
dict(
id=5881, slug="infografia-snapcraft-para-desarrolladores",
title="Snapcraft para desarrolladores (infografía)",
excerpt="Infografía de Snapcraft, la tienda universal de apps para Linux: publicar una vez para escritorio, nube e IoT, más de 3 millones de instalaciones al mes y 42 distribuciones compatibles.",
img_alt="Infografía de Snapcraft, la tienda universal de aplicaciones para Linux",
credit="Infografía: Snapcraft (Canonical), febrero de 2019.",
body=f"""
Publicar una app para Linux solía significar empaquetarla para cada distribución por separado. Snapcraft, de Canonical (la empresa detrás de Ubuntu), propuso una sola tienda para todas. Esta infografía de 2019 resume su propuesta.

{{IMG}}

## Lo que muestra la infografía

**Una tienda universal para Linux:** distribuye y actualiza tu app en cualquier distribución, para escritorio, nube e internet de las cosas.

**Por qué publicar como snap**
- **Un solo paquete** para nube, escritorio y dispositivos IoT.
- **Visibilidad** ante millones de usuarios.
- **Métricas** de crecimiento y retención.

**Las cifras (febrero de 2019)**
- Más de 3 millones de instalaciones de snaps al mes.
- Más de 2,000 desarrolladores con snaps publicados.
- Apps oficiales de Spotify, Google, Amazon, Microsoft y Slack, entre otros.
- Comunidad: 32,300 publicaciones, 11,500 "me gusta" y 4,700 temas en el foro.

**Se integra con tu flujo de trabajo:** GitHub, GitLab, Travis, CircleCI, AppVeyor, Docker y Jenkins.

**Un paquete, 42 distribuciones de Linux,** como Ubuntu, Debian, Fedora, Arch Linux y Ubuntu MATE.

**Habla tu lenguaje:** Java, Node.js, Electron, Python, Ruby, Rust, ROS y ROS 2, además de apps precompiladas.

**Funciona donde corre Linux:** tarjetas de desarrollo, nube, PC, robótica, gateways y autos autónomos.

## Lo que cambió

Snap sigue siendo el formato preferido de Ubuntu, aunque convive con Flatpak, la alternativa que muchas otras distribuciones prefieren. Para un desarrollador, la decisión depende de dónde están sus usuarios.

## Lo que aprende cualquier producto digital

La propuesta de Snapcraft es un buen ejemplo de mensaje B2B: un dolor claro (empaquetar para cada distribución), una promesa simple (un solo paquete) y prueba social (marcas conocidas y cifras). Lee [inbound marketing para empresas B2B]({B2B}) y [cloud computing e internet de las cosas]({S}/infografia-cloud-computing-e-internet-de-las-cosas-de-la-mano/).
""",
faq=[
("¿Qué es Snapcraft?", "La tienda y el sistema de empaquetado de aplicaciones snap de Canonical, que permite distribuir una app en muchas distribuciones de Linux con un solo paquete."),
("¿Qué es un snap en Linux?", "Un paquete de software que incluye la app y sus dependencias, se actualiza automáticamente y funciona en distintas distribuciones."),
("¿Qué diferencia hay entre Snap y Flatpak?", "Ambos son formatos universales de apps para Linux; Snap es impulsado por Canonical y Ubuntu, y Flatpak es más usado por otras distribuciones."),
],
related=[("Inbound marketing para empresas B2B", B2B), ("Cloud computing e internet de las cosas", S + "/infografia-cloud-computing-e-internet-de-las-cosas-de-la-mano/")],
),

dict(
id=1981, slug="infografia-5-inesperadas-razones-por-las-que-el-engagement-de-tu-equipo-es-importante",
title="5 razones por las que importa el engagement de tu equipo",
excerpt="Infografía con 5 razones por las que importa el engagement de tu equipo: el 51% de los no comprometidos busca otro trabajo, 41% menos ausentismo y 17% más productividad.",
img_alt="Infografía de 5 inesperadas razones por las que el engagement de tu equipo es importante",
credit="Infografía: INVEX Banco, con datos de Officevibe (2017).",
body=f"""
Un equipo comprometido no es solo más feliz: falta menos, se queda más y produce más. Esta infografía resume cinco datos que lo demuestran.

{{IMG}}

## Las 5 razones

1. **El 51% de los colaboradores no comprometidos** busca constantemente otro trabajo.
2. **Los colaboradores no comprometidos** le cuestan a las empresas unos 550 millones de dólares al año, según la fuente citada.
3. **Las compañías que trabajan en el engagement** de su gente tienen 41% menos ausentismo.
4. **El 48% de los empleados** en el mundo dice ser infeliz en su trabajo.
5. **Las empresas con personal comprometido** ven un incremento de 17% en la productividad.

## Cómo medirlo y mejorarlo

- **Pregunta con frecuencia.** Encuestas breves y anónimas cada mes dicen más que una encuesta anual larga.
- **Actúa sobre lo que te dicen.** Preguntar y no hacer nada destruye la confianza.
- **Reconoce el trabajo** de forma específica y frecuente.
- **Da claridad:** que cada persona sepa qué se espera de ella y cómo su trabajo importa.
- **Cuida a los jefes directos.** Son el factor que más influye en el compromiso.

Lee [salario emocional, la clave para retener el talento]({S}/infografia-salario-emocional-la-clave-para-retener-el-talento/) y [las 13 características de un buen líder]({LIDER}).
""",
faq=[
("¿Qué es el engagement laboral?", "El nivel de compromiso emocional y motivación de una persona con su trabajo y su empresa."),
("¿Por qué es importante el engagement del equipo?", "Porque reduce la rotación y el ausentismo y aumenta la productividad, según los datos de la infografía."),
("¿Cómo mejorar el compromiso de los empleados?", "Preguntando con frecuencia, actuando sobre lo que dicen, reconociendo su trabajo, dando claridad y formando buenos jefes."),
],
related=[("Salario emocional", S + "/infografia-salario-emocional-la-clave-para-retener-el-talento/"), ("13 características de un buen líder", LIDER)],
),

dict(
id=1935, slug="infografia-estructura-de-la-declaracion-de-la-renta",
title="Estructura de la declaración de la renta en España",
excerpt="Infografía con la estructura básica de la declaración de la renta (IRPF) en España: renta general y del ahorro, reducciones, bases liquidables, cuota íntegra, deducciones y resultado.",
img_alt="Infografía de la estructura básica de la declaración de la renta en España",
credit="Infografía: Self Bank.",
body=f"""
La declaración de la renta en España (el IRPF) parece un laberinto, pero tiene una estructura lógica. Esta infografía la dibuja paso a paso. Ojo: es el sistema español; en México la declaración anual ante el SAT funciona distinto.

{{IMG}}

## La estructura

**1. Renta general**
- Rendimientos del trabajo (nóminas).
- Rendimientos del capital inmobiliario (alquileres).
- Rendimientos de actividades económicas (negocios propios y autónomos).

Todo suma la **base imponible general**. Se le aplican **reducciones**, como las aportaciones a planes de pensiones, y queda la **base liquidable general**, sobre la que se aplica la escala general del IRPF (del 19% al 45% cuando se hizo la infografía), descontando el mínimo personal y familiar.

**2. Renta del ahorro**
- Rendimientos del capital mobiliario: intereses de cuentas y depósitos, dividendos, seguros.
- Ganancias y pérdidas patrimoniales: compraventa de acciones y reembolso de fondos.

Se pueden compensar pérdidas de los cuatro ejercicios anteriores. Así se obtiene la **base imponible y liquidable del ahorro**, con su propio tipo de gravamen (19%, 21% y 23% por tramos cuando se hizo la infografía).

**3. Cuota íntegra, deducciones y resultado.** A la cuota se le restan deducciones (hipoteca, maternidad) y pagos a cuenta (retenciones). El resultado es una devolución o un pago.

## Lo que cambió

Los tramos y tipos del IRPF se han modificado varias veces desde entonces, sobre todo en la renta del ahorro, que hoy tiene más tramos y tipos más altos para las rentas grandes. Consulta siempre la información vigente de la Agencia Tributaria o a un asesor fiscal.

## Para emprendedores en México

Si tienes un negocio en México, la lógica es similar (ingresos, deducciones autorizadas, tarifa y pagos provisionales), pero las reglas son del SAT. Lee [qué hacer cuando un cliente no te paga]({NO_PAGA}) y [las características de un emprendedor exitoso]({EMPRENDEDOR}).
""",
faq=[
("¿Qué es el IRPF?", "El Impuesto sobre la Renta de las Personas Físicas de España, que grava los ingresos anuales de las personas."),
("¿Qué diferencia hay entre la renta general y la del ahorro?", "La general incluye trabajo, alquileres y actividades económicas; la del ahorro, intereses, dividendos y ganancias por venta de inversiones. Cada una tiene su propia escala."),
("¿Esta infografía aplica en México?", "No. Explica el sistema español; en México la declaración anual se presenta ante el SAT con reglas propias."),
],
related=[("Qué hacer cuando un cliente no te paga", NO_PAGA), ("Características de un emprendedor exitoso", EMPRENDEDOR)],
),

dict(
id=1462, slug="infografia-rutas-aereas-transpolares",
title="Rutas aéreas transpolares (infografía)",
excerpt="Infografía de las rutas aéreas transpolares: su historia desde 1952, por qué ahorran tiempo y combustible, y sus retos: congelación, radiación, comunicaciones y aeropuertos alternos.",
img_alt="Infografía de rutas aéreas transpolares, la mejor alternativa para ahorrar tiempo y combustible",
credit="Infografía: Aertec Solutions (2017).",
body=f"""
El camino más corto entre dos aeropuertos casi nunca es una línea recta en el mapa. Por eso muchos vuelos entre América del Norte y Asia cruzan cerca del Polo Norte. Esta infografía explica cómo funcionan las rutas transpolares.

{{IMG}}

## La historia

- **1952:** SAS hace el primer vuelo transpolar comercial con un DC-6B, de Los Ángeles a Copenhague, con escalas en Edmonton y Thule (Groenlandia).
- **1954:** se inauguran los vuelos regulares Copenhague-Los Ángeles.
- **1957:** un DC-7C de SAS abre la primera ruta polar al Lejano Oriente, de Copenhague a Tokio vía Anchorage.
- **1998:** Rusia autoriza cuatro rutas, Polar 1, 2, 3 y 4. Cathay Pacific es la primera en usarlas.
- **2001:** tras cientos de vuelos de prueba, entran oficialmente en servicio entre América del Norte y Asia.
- **2014:** se cierra la ruta austral Buenos Aires-Auckland-Sídney tras 30 años.
- **Actualmente:** Qantas y Air New Zealand operan las rutas polares más australes, hasta el paralelo 71° S.

## Por qué ahorran tiempo

En un mapa plano parece más corto ir en línea recta, pero en la esfera terrestre la ruta más corta pasa más cerca del polo. El ejemplo de la infografía: Nueva York-Hong Kong por ruta polar tarda 15 h 45 min, contra 19 h 50 min por la ruta convencional. United Airlines operaba más de 1,500 vuelos transpolares al año entre Estados Unidos y Asia.

## Los retos

- **Congelación del combustible:** la zona más fría del recorrido, sobre Siberia, llega a -65 °C. Los aviones llevan sistemas y sensores para evitarla.
- **Radiación:** la atmósfera es más delgada y el campo magnético distinto, así que se vigila la exposición.
- **Comunicaciones:** los satélites geoestacionarios no cubren más allá del paralelo 82° N, así que se usan otras frecuencias y satélites.
- **Navegación:** las brújulas magnéticas no son fiables cerca del polo.
- **Aeropuertos alternos** disponibles para garantizar la seguridad.

## Lo que pasó después

Desde 2022, el cierre del espacio aéreo ruso para muchas aerolíneas occidentales alargó varias rutas entre Europa y Asia y cambió el mapa de los vuelos polares. Lee [los 30 primeros años de Amadeus]({S}/infografia-30-primeros-anos-de-amadeus/) y [tendencias de viajes de verano]({S}/infografia-tendencias-sobre-los-viajes-de-verano-en-relacion-a-lo-que-buscan-en-internet/).
""",
faq=[
("¿Qué es una ruta aérea transpolar?", "Una ruta que cruza las regiones polares para acortar la distancia entre continentes, sobre todo entre América del Norte y Asia."),
("¿Por qué los vuelos pasan cerca del Polo Norte?", "Porque en la esfera terrestre la ruta más corta entre dos puntos lejanos suele pasar cerca del polo, aunque en un mapa plano no lo parezca."),
("¿Qué riesgos tienen los vuelos polares?", "Temperaturas extremas que pueden congelar el combustible, mayor radiación, comunicaciones limitadas y pocos aeropuertos alternos."),
],
related=[("Los 30 primeros años de Amadeus", S + "/infografia-30-primeros-anos-de-amadeus/"), ("Tendencias de viajes de verano", S + "/infografia-tendencias-sobre-los-viajes-de-verano-en-relacion-a-lo-que-buscan-en-internet/")],
),

dict(
id=1903, slug="infografia-clasificacion-de-las-motivaciones-sociales",
title="Las 3 motivaciones sociales: logro, poder y afiliación",
excerpt="Infografía de Pilar Jericó sobre la clasificación de las motivaciones sociales de David McClelland: logro, poder y afiliación, y cómo se comporta cada perfil en el trabajo.",
img_alt="Infografía de la clasificación de las motivaciones sociales: logro, poder y afiliación",
credit="Infografía: Pilar Jericó, con base en David McClelland.",
body=f"""
¿Qué mueve a cada persona de tu equipo? El psicólogo David McClelland propuso tres grandes motivaciones sociales. Esta infografía de Pilar Jericó describe cómo se comporta cada perfil.

{{IMG}}

## Las 3 motivaciones

**Logro**
- Se marcan objetivos ambiciosos.
- Asumen riesgos.
- Son resistentes al estrés.
- Buscan expertos en los que apoyarse.
- Se responsabilizan personalmente.

**Poder (influencia)**
- Influyen sobre los demás para que logren resultados.
- Son activos en las tramas de poder.
- Expresan sus emociones de forma abierta.

**Afiliación**
- Para trabajar, eligen antes a un amigo que a un experto.
- Crean buen clima.
- Conservan las amistades.
- Ayudan a los demás sin que se lo pidan.
- No les gusta estar solos.

## Cómo usarlo como líder

- **Al de logro,** dale retos medibles y retroalimentación frecuente.
- **Al de poder,** dale visibilidad, responsabilidad sobre personas y un propósito colectivo para que su influencia sume.
- **Al de afiliación,** dale trabajo en equipo y un ambiente de confianza; cuida que no evite conflictos necesarios.

Todos tenemos las tres en distinta medida. Conocer cuál predomina ayuda a asignar mejor las tareas. Lee [los miedos que frenan tu éxito en el trabajo]({S}/infografia-5-miedos-que-frenan-tu-exito-en-el-trabajo/) y [las 13 características de un buen líder]({LIDER}).
""",
faq=[
("¿Cuáles son las motivaciones sociales según McClelland?", "Logro, poder y afiliación."),
("¿Cómo es una persona motivada por el logro?", "Se marca objetivos ambiciosos, asume riesgos calculados, resiste el estrés y se responsabiliza de sus resultados."),
("¿Cómo motivar a alguien orientado a la afiliación?", "Con trabajo en equipo, buen clima y relaciones de confianza."),
],
related=[("Los miedos que frenan tu éxito en el trabajo", S + "/infografia-5-miedos-que-frenan-tu-exito-en-el-trabajo/"), ("13 características de un buen líder", LIDER)],
),

dict(
id=1302, slug="infografia-7-razones-por-las-que-pagar-a-los-becarios",
title="7 razones para pagar a tus becarios",
excerpt="Infografía con 7 razones para pagar a los becarios: atraer más candidatos, motivar, cumplir requisitos, demostrar seriedad, dar igualdad de oportunidades, cotizar y deducir.",
img_alt="Infografía de 7 razones para pagarle a tu becario",
credit="Infografía: Portal de Empleo de la Universidad de Sevilla (US Virtual Empleo).",
body=f"""
¿Pagar o no a quien hace prácticas en tu empresa? Esta infografía, pensada para empresas españolas, da siete razones para pagar. La mayoría aplican en cualquier país.

{{IMG}}

## Las 7 razones

1. **Atraer.** Más personas se interesarán en la beca, y podrás elegir entre más candidatos.
2. **Motivar.** Refuerza la implicación y el compromiso del becario.
3. **Cumplir.** Muchas universidades, centros de formación y programas de empleo exigen el pago, que a veces se complementa con una ayuda de la entidad promotora.
4. **Demostrar.** Proyectas una imagen seria, de empresa que reconoce el trabajo y se preocupa por atraer y desarrollar talento.
5. **Posibilitar.** Facilitas que personas con menos recursos accedan a las prácticas, lo que favorece la igualdad de oportunidades.
6. **Cotizar.** En España, la cotización es baja y fija, y permite que el becario cotice en la seguridad social.
7. **Deducir.** Las becas y cotizaciones pueden ser gastos deducibles.

## En México

Las prácticas profesionales y el servicio social tienen reglas propias, y muchas empresas otorgan un apoyo económico. Más allá de lo que exija la ley, la lógica es la misma: pagar atrae mejores candidatos y construye tu reputación como empleador. Consulta con tu área legal o contable las condiciones vigentes.

Lee [12 razones por las que el mejor talento no quiere trabajar en tu empresa]({S}/infografia-12-razones-por-las-que-el-mejor-talento-no-quiere-trabajar-en-tu-empresa/) y [salario emocional]({S}/infografia-salario-emocional-la-clave-para-retener-el-talento/).
""",
faq=[
("¿Por qué pagar a los becarios?", "Para atraer más y mejores candidatos, motivarlos, cumplir requisitos de las universidades, proyectar seriedad y favorecer la igualdad de oportunidades."),
("¿Pagar a un becario es deducible?", "En España, la infografía señala que las becas y cotizaciones pueden ser deducibles. En México conviene consultarlo con un contador."),
("¿Pagar a los becarios mejora la imagen de la empresa?", "Sí: proyecta una empresa que reconoce el trabajo y se preocupa por el talento."),
],
related=[("12 razones por las que el talento no te elige", S + "/infografia-12-razones-por-las-que-el-mejor-talento-no-quiere-trabajar-en-tu-empresa/"), ("Salario emocional", S + "/infografia-salario-emocional-la-clave-para-retener-el-talento/")],
),

dict(
id=1424, slug="infografia-10-herramientas-seo-gratis",
title="19 herramientas SEO gratis (infografía)",
excerpt="Infografía con 19 herramientas SEO gratis para keywords, SEO on page, SEO técnico, analítica y etiquetas: Google Trends, Search Console, Screaming Frog, PageSpeed Insights y más.",
img_alt="Infografía de las 19 mejores herramientas SEO gratis",
credit="Infografía: MainStreetHost.",
body=f"""
No necesitas pagar una suscripción cara para empezar a hacer SEO. Esta infografía reúne 19 herramientas gratuitas, ordenadas por tarea.

{{IMG}}

## Las herramientas

**Investigación de palabras clave**
- Google Trends.
- Google Keyword Planner.
- Keyworddit.
- Answer the Public.

**SEO on page**
- Open SEO Stats (extensión de Chrome).
- WooRank.
- Quicksprout.
- Check My Links.

**SEO técnico**
- Screaming Frog SEO Spider.
- Google PageSpeed Insights.
- Structured Data Testing Tool.
- Website Penalty Indicator.

**Analítica**
- Google Analytics.
- Google Search Console.
- Search Analytics for Sheets.

**Etiquetas de marketing**
- Google Tag Manager.
- Google Tag Assistant.
- Ghostery.
- GAChecker.

## Lo que cambió

- **Google Analytics** pasó a GA4 en 2023; la versión anterior dejó de registrar datos.
- **Structured Data Testing Tool** fue reemplazada por la Prueba de resultados enriquecidos de Google y el Schema Markup Validator.
- Algunas herramientas cambiaron de dueño, de nombre o dejaron de ser gratuitas, así que revisa cada una antes de usarla.

**El kit mínimo que sigue funcionando:** Google Search Console, GA4, PageSpeed Insights, Google Trends, Keyword Planner y la versión gratuita de Screaming Frog (hasta 500 URL).

Revisa [10 herramientas que deben formar parte de tu estrategia SEO]({S}/infografia-10-herramientas-que-deben-formar-parte-de-tu-estrategia-seo/) y [40 errores técnicos en SEO]({S}/infografia-40-errores-tecnicos-en-seo/).
""",
faq=[
("¿Cuáles son las mejores herramientas SEO gratis?", "Google Search Console, Google Analytics 4, PageSpeed Insights, Google Trends, Keyword Planner y la versión gratuita de Screaming Frog son una buena base."),
("¿Qué reemplazó a la Structured Data Testing Tool?", "La Prueba de resultados enriquecidos de Google y el Schema Markup Validator."),
("¿Para qué sirve Google Search Console?", "Para ver cómo aparece tu sitio en Google: búsquedas, clics, posiciones, errores de indexación y problemas técnicos."),
],
related=[("10 herramientas para tu estrategia SEO", S + "/infografia-10-herramientas-que-deben-formar-parte-de-tu-estrategia-seo/"), ("40 errores técnicos en SEO", S + "/infografia-40-errores-tecnicos-en-seo/")],
),

dict(
id=1755, slug="infografia-9-mejores-herramientas-online-para-comprimir-imagenes",
title="9 herramientas en línea para comprimir imágenes",
excerpt="Infografía con 9 herramientas en línea para comprimir imágenes: Compress JPEG, Compress Photos, Compressnow, Compressor.io, ConvertImage, Optimizilla, Resize Photos, ShortPixel y TinyJPG.",
img_alt="Infografía de las 9 mejores herramientas para comprimir imágenes en línea",
credit="Infografía: Web Services Pro (@webservicespro1).",
body=f"""
Las imágenes pesadas son una de las principales causas de que un sitio cargue lento. Esta infografía compara nueve herramientas gratuitas para comprimirlas sin registrarte.

{{IMG}}

## Las 9 herramientas

| # | Herramienta | Formatos | Subida | Compresión |
|---|---|---|---|---|
| 1 | Compress JPEG | JPEG, PNG | Individual o lotes de 20 | Automática, con ajuste manual |
| 2 | Compress Photos | JPEG, PNG | Individual o lotes de hasta 50 MB | Automática, con ajuste manual |
| 3 | Compressnow | JPEG, PNG, GIF | Individual, hasta 9 MB | Manual |
| 4 | Compressor.io | JPEG, PNG, GIF, SVG | Individual, hasta 10 MB | Dos tipos automáticos |
| 5 | ConvertImage | JPEG | Individual | Manual |
| 6 | Optimizilla | JPEG, PNG | Individual o lotes de 20 | Automática, con ajuste manual |
| 7 | Resize Photos | JPEG, PNG, GIF y otros | Individual | Manual, eligiendo píxeles |
| 8 | ShortPixel | JPEG, PNG, GIF | Individual o lotes de 50 | Tres tipos automáticos |
| 9 | TinyJPG | JPEG, PNG | Individual o lotes de 20 | Automática, sin vista previa |

Ninguna pide registro. Varias permiten descargar en lote como ZIP.

## Lo que cambió

Algunas de estas herramientas cambiaron sus límites, y hoy hay opciones como Squoosh, de Google, que convierte a formatos modernos como WebP y AVIF, mucho más ligeros. Si usas WordPress, un plugin de optimización puede comprimir y convertir automáticamente cada imagen que subes.

**Regla práctica:** redimensiona la imagen al tamaño en que se mostrará y después comprímela. Subir una foto de 4,000 píxeles para mostrarla a 800 es el error más común.

Revisa [herramientas de Google para optimizar tu página web]({S}/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/) y [SEO: la receta para que consuman tu contenido]({S}/infografia-seo-la-receta-ideal-para-que-consuman-tu-contenido/).
""",
faq=[
("¿Cómo comprimir imágenes sin perder calidad?", "Redimensionando al tamaño de uso y usando herramientas de compresión con vista previa, como Optimizilla, TinyJPG o Squoosh, o formatos modernos como WebP."),
("¿Qué formato de imagen pesa menos?", "WebP y AVIF suelen pesar bastante menos que JPEG y PNG con calidad similar."),
("¿Por qué comprimir las imágenes de mi sitio?", "Porque las imágenes pesadas hacen lenta la carga, empeoran la experiencia del usuario y afectan el SEO."),
],
related=[("Herramientas de Google para optimizar tu página web", S + "/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/"), ("SEO: la receta para tu contenido", S + "/infografia-seo-la-receta-ideal-para-que-consuman-tu-contenido/")],
),

dict(
id=2047, slug="infografia-la-importancia-del-color-en-el-branding",
title="La importancia del color en el branding",
excerpt="Infografía sobre el color en el branding: los colores que usan las marcas líderes por industria y lo que comunica cada uno, del rojo que despierta el apetito al azul de la confianza.",
img_alt="Infografía de la importancia del color en el branding por industria",
credit="Infografía: Towergate Insurance.",
body=f"""
Se dice que el 80% de la información visual que recibimos de un logo tiene que ver con sus colores. Por eso las marcas dedican tanto tiempo a elegirlos. Esta infografía analiza los colores de los logos de las 20 empresas principales en distintas industrias.

{{IMG}}

## Lo que muestra

**Los colores por industria.** La infografía compara 26 sectores, de restaurantes y bancos a aerolíneas, autos, software y mensajería, y muestra que muchas industrias se inclinan por ciertos colores.

**Lo que comunica cada color, con ejemplos:**
- **Rojo:** atención y energía; se cree que estimula el apetito (McDonald's). También pasión, fuerza y determinación.
- **Azul:** confianza, comunicación clara, calma y limpieza. Muy usado en bancos, tecnología, aerolíneas y salud.
- **Verde:** bienestar, salud, naturaleza.
- **Amarillo:** alegría y optimismo.
- **Naranja:** juventud, diversión, confianza y, en tonos brillantes, precio accesible.
- **Negro:** fuerza, seguridad y elegancia, sobre todo en moda.
- **Gris y plateado:** confiabilidad y calidad, frecuente en autos.

## Lo que sí y lo que no

La psicología del color es útil, pero no es una ciencia exacta: el significado cambia según la cultura, el contexto y la experiencia de cada persona. Lo que sí está claro es que la consistencia en el uso de tus colores hace que la gente reconozca tu marca más rápido.

**Para elegir los tuyos:** piensa en lo que quieres transmitir, revisa qué usa tu competencia (para no confundirte con ella) y prueba que tus colores funcionen en pantalla, impresión y con buen contraste para leer.

Lee [brand articulation: las bases de tu marca]({S}/infografia-brand-articulation-las-bases-para-solidificar-tu-marca-desde-cero/) y [28 términos de diseño que marketing debe conocer]({S}/infografia-28-terminos-de-diseno-que-marketing-debe-conocer/).
""",
faq=[
("¿Por qué es importante el color en una marca?", "Porque es de lo primero que se percibe y recuerda; usado con constancia, ayuda a que la gente reconozca tu marca."),
("¿Qué transmite el color azul en una marca?", "Confianza, seguridad y claridad, por eso es común en bancos, tecnología y salud."),
("¿Por qué tantos restaurantes usan rojo?", "Porque atrae la atención y se asocia con energía y apetito."),
],
related=[("Brand articulation", S + "/infografia-brand-articulation-las-bases-para-solidificar-tu-marca-desde-cero/"), ("28 términos de diseño", S + "/infografia-28-terminos-de-diseno-que-marketing-debe-conocer/")],
),

dict(
id=1919, slug="infografia-que-es-el-black-friday",
title="Qué es el Black Friday y cómo aprovecharlo",
excerpt="Infografía del Black Friday para el pequeño comercio: para qué sirve unirse, qué acciones poner en marcha y por qué definir el inventario. Y cómo se relaciona con El Buen Fin en México.",
img_alt="Infografía del Black Friday para el pequeño comercio",
credit="Infografía: Commerce360.",
body=f"""
El Black Friday, el viernes después del Día de Acción de Gracias en Estados Unidos, se volvió una fecha global de descuentos. Esta infografía explica cómo puede aprovecharlo un comercio pequeño.

{{IMG}}

## Para qué sirve unirte

- Deshacerte de inventario que no se ha vendido.
- Adelantar las compras de Navidad.
- Que te conozcan clientes nuevos, atraídos por el descuento.
- Usar los productos en promoción como gancho para vender otros a precio normal.

## Acciones que puede poner en marcha una tienda

- **2x1.**
- **Descuento especial** para socios y clientes fieles.
- **Oferta especial** para quienes te conozcan por redes sociales.
- **Trae a un amigo** y llévate una consumición gratis.
- **Bonificación** para compras futuras.

**Clave:** define bien el inventario y asegura su disponibilidad. La demanda es alta, y quedarte sin producto frustra a los clientes que atrajiste.

## En México

Aquí la gran fecha es **El Buen Fin**, a mediados de noviembre, que nació inspirado en el Black Friday. Muchas tiendas en línea participan en ambos, más el Cyber Monday y el Hot Sale de mayo.

## Cómo prepararte

- **Empieza semanas antes:** construye tu lista de correo y avisa a tus clientes.
- **No descuentes todo.** Elige productos gancho y protege tu margen.
- **Prepara tu sitio y tu atención** para el aumento de visitas y preguntas.
- **Da seguimiento después:** el cliente nuevo de noviembre puede ser el cliente fiel de todo el año.

Lee [cómo es el consumo en México por temporada]({S}/infografia-como-es-el-consumo-en-mexico/) y [cómo hacer que tus clientes te recomienden]({RECOMIENDEN}).
""",
faq=[
("¿Qué es el Black Friday?", "Un día de grandes descuentos que se celebra el viernes siguiente al Día de Acción de Gracias en Estados Unidos y que se extendió a muchos países."),
("¿Qué diferencia hay entre Black Friday y El Buen Fin?", "El Buen Fin es la versión mexicana, a mediados de noviembre, impulsada por gobierno y empresas; el Black Friday es la fecha estadounidense, que también se aprovecha en México."),
("¿Le conviene a un negocio pequeño participar en el Black Friday?", "Puede servirle para mover inventario, atraer clientes nuevos y adelantar ventas navideñas, siempre que cuide su margen y su inventario."),
],
related=[("Cómo es el consumo en México", S + "/infografia-como-es-el-consumo-en-mexico/"), ("Cómo hacer que tus clientes te recomienden", RECOMIENDEN)],
),
]
