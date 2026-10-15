from comun import *

POSTS = [
dict(
id=1454, slug="infografia-10-diferencias-entre-inbound-y-outboung-marketing",
title="10 diferencias entre inbound y outbound marketing",
excerpt="Infografía con 10 diferencias entre inbound y outbound marketing: centrado en el usuario o en el producto, atraer o interrumpir, comunicación de dos vías, medios, público, presupuesto y medición.",
img_alt="Infografía de 10 diferencias entre inbound y outbound marketing",
credit="Infografía: @rosanarosas17.",
body=f"""
Hay dos formas de conseguir clientes: salir a buscarlos interrumpiendo, o atraerlos con algo que les sirva. Esta infografía compara el outbound (el marketing tradicional de salida) con el inbound.

{{IMG}}

## Las 10 diferencias

| Inbound marketing | Outbound marketing |
|---|---|
| Centrado en el usuario | Centrado en el producto |
| Atrae al cliente | Interrumpe al cliente |
| Comunicación de dos vías | Comunicación de una vía |
| Usa medios digitales | Usa medios tradicionales |
| Llega a un público específico | Llega a un público masivo |
| Busca entretener y educar | Busca vender |
| Requiere poco presupuesto | Requiere un presupuesto alto |
| Aporta valor | No aporta o aporta poco valor |
| Los clientes llegan por buscadores, redes, sitios y blogs | Se busca al cliente con anuncios en periódicos, TV, radio, llamadas en frío y banners |
| Los resultados se miden fácilmente | Es difícil medir el impacto |

## Un matiz

"Poco presupuesto" no significa gratis: el inbound requiere tiempo, constancia y talento para crear contenido. Y el outbound no está muerto; en ventas B2B, una llamada bien preparada a una cuenta que ya conoce tu contenido funciona muy bien. Lo más efectivo suele ser combinar: atraer con contenido y apoyar con publicidad y ventas bien dirigidas.

Profundiza en [qué es el inbound marketing]({GUIA}), [sus 4 fases]({FASES}) y [marketing tradicional vs. digital]({S}/infografia-marketing-tradicional-vs-marketing-digital/).
""",
faq=[
("¿Qué diferencia hay entre inbound y outbound marketing?", "El inbound atrae clientes con contenido útil y comunicación de dos vías; el outbound los busca con mensajes masivos que interrumpen, como anuncios o llamadas en frío."),
("¿El inbound marketing es gratis?", "No requiere grandes pagos en medios, pero sí tiempo, constancia y talento para crear y distribuir contenido."),
("¿Se pueden combinar inbound y outbound?", "Sí, y suele ser lo más efectivo: el contenido atrae y educa, y la publicidad o ventas dirigidas aceleran el proceso."),
],
related=[("Qué es el inbound marketing", GUIA), ("Marketing tradicional vs. digital", S + "/infografia-marketing-tradicional-vs-marketing-digital/")],
),

dict(
id=2225, slug="infografia-m2m-y-el-iot-en-cifras",
title="M2M vs. IoT: el internet de las cosas en cifras",
excerpt="Infografía de Telefónica que compara M2M (máquina a máquina) e IoT con cifras: de 5,000 a 27,000 millones de conexiones M2M, 75,400 millones de dispositivos en 2025 y crecimiento del gasto en la nube.",
img_alt="Infografía de M2M vs IoT en cifras",
credit="Infografía: Telefónica Business Solutions, con datos de Forbes, Machina Research, Statista y CCS Insight.",
body=f"""
M2M e IoT se usan casi como sinónimos, pero no son lo mismo. Esta infografía de Telefónica explica la diferencia y la acompaña con cifras.

{{IMG}}

## La diferencia

- **M2M (máquina a máquina):** sensores, datos e información que se comunican entre máquinas, como un camión que reporta su ubicación a un sistema.
- **IoT (internet de las cosas):** suma a las personas: usuarios finales, dispositivos, wearables y big data.

## Las cifras de M2M

- De **5,000 millones** de conexiones en 2014 a **27,000 millones** en 2024.
- **1.6 billones de dólares** en oportunidad de negocio para 2024 entre dispositivos, conectividad y aplicaciones, con un crecimiento anual de 12%. La mayoría de los beneficios vendría de los dispositivos.
- Las conexiones de corto alcance (Wi-Fi, Zigbee, PLC) pasarían de 72% a 69% en 2024.

## Las cifras de IoT

- El gasto mundial en la nube crecería de **70,000 millones de dólares en 2015 a más de 141,000 millones en 2019.**
- En 2020, la analítica predictiva y prescriptiva atraería el **40%** de las nuevas inversiones de las empresas.
- Dispositivos conectados: de **28,400 millones (2017)** a **30,700 millones** y hasta **75,400 millones en 2025**, según la proyección.
- Wearables: de **84 millones de unidades en 2015** a **245 millones en 2019.**
- El mercado pasaría de **900 millones de dólares (2015)** a **3,700 millones en 2020** (32.6% anual).
- El gasto en productos y servicios IoT crecería de **120,000 millones en 2016** a **253,000 millones en 2021.**

## Lo que pasó después

Las cifras más optimistas, como los 75,000 millones de dispositivos, resultaron altas; las estimaciones más recientes hablan de unas decenas de miles de millones. Aun así, la tendencia se cumplió: cada vez más objetos están conectados y generan datos.

Lee [sectores con más presencia del internet de las cosas]({S}/infografia-sectores-donde-tendra-mas-presencia-en-internet-de-las-cosas/) y [cloud computing e internet de las cosas]({S}/infografia-cloud-computing-e-internet-de-las-cosas-de-la-mano/).
""",
faq=[
("¿Qué diferencia hay entre M2M e IoT?", "M2M es la comunicación directa entre máquinas; IoT es más amplio e incluye a personas, dispositivos de consumo, wearables y análisis de datos."),
("¿Cuántos dispositivos IoT hay en el mundo?", "Las estimaciones recientes hablan de decenas de miles de millones; las proyecciones de 2017 resultaron algo optimistas."),
("¿Qué es un wearable?", "Un dispositivo que se lleva puesto, como un reloj inteligente o una pulsera de actividad."),
],
related=[("Sectores del internet de las cosas", S + "/infografia-sectores-donde-tendra-mas-presencia-en-internet-de-las-cosas/"), ("Cloud computing e internet de las cosas", S + "/infografia-cloud-computing-e-internet-de-las-cosas-de-la-mano/")],
),

dict(
id=1617, slug="infografia-mexico-el-consumidor-conectado",
title="México: el consumidor conectado (infografía)",
excerpt="Infografía de Google sobre el consumidor conectado en México en 2016: 70% usa internet, 81% de los internautas navega a diario, 66% usa smartphone y 91% lo usa mientras ve TV.",
img_alt="Infografía de México, el consumidor conectado",
credit="Infografía: Think with Google, con datos del Connected Consumer Study de Google y TNS (México, 2016).",
body=f"""
¿Cómo usan internet los mexicanos para informarse, entretenerse y comprar? Esta infografía de Google resume su estudio de 2016.

{{IMG}}

## Los datos

**Conectados**
- El **70%** de los mexicanos usa internet por motivos personales.
- El **81%** de los internautas navega a diario.
- El **80%** de los mayores de 35 se conecta todos los días.

**Buscan información**
- El **77%** dice que, cuando necesita información, internet es el primer lugar donde busca.
- El **40%** busca información de algún producto cada mes.

**Con el smartphone**
- El **66%** de los mexicanos usa smartphone; entre 18 y 35 años, el **83%.**
- El **54%** lo usa para ver video en línea cada semana.
- El **91%** usa el smartphone mientras ve televisión.

**Video**
- El **85%** de los internautas de 18 a 35 años ve video en línea al menos una vez a la semana, y el **78%** lo hace desde el smartphone.

## Lo que pasó después

Según la ENDUTIH del INEGI, la proporción de mexicanos que usan internet siguió subiendo y supera ya el 80% de la población de 6 años o más, casi siempre desde el celular. La foto de 2016 se volvió todavía más móvil.

## Lo que significa para tu negocio

Tu cliente investiga en el celular antes de comprar, incluso si compra en tienda. Asegúrate de aparecer en Google con información completa, de que tu sitio funcione en el celular y de tener video que responda sus dudas. Lee [Argentina: el consumidor conectado]({S}/infografia-argentina-el-consumidor-conectado/) y [el mundo es responsivo]({S}/infografia-el-mundo-es-responsive/).
""",
faq=[
("¿Cuántos mexicanos usaban internet en 2016?", "El 70%, según el Connected Consumer Study de Google y TNS."),
("¿Los mexicanos usan el celular mientras ven televisión?", "Sí: el 91% de los internautas lo hace, según el estudio."),
("¿Dónde buscan información los mexicanos antes de comprar?", "El 77% dice que internet es el primer lugar donde busca cuando necesita información."),
],
related=[("Argentina: el consumidor conectado", S + "/infografia-argentina-el-consumidor-conectado/"), ("El mundo es responsivo", S + "/infografia-el-mundo-es-responsive/")],
),

dict(
id=1671, slug="infografia-vuelve-la-peste",
title="Vuelve la peste: casos en el mundo (infografía)",
excerpt="Infografía con los casos de peste en humanos entre 2010 y 2015 según la OMS: Madagascar con 2,404 casos y 467 muertes, Congo, Uganda, Perú, Tanzania y Estados Unidos, y las zonas de riesgo.",
img_alt="Infografía vuelve la peste: casos registrados en el mundo entre 2010 y 2015",
credit="Infografía: Insider Pro con datos de la Organización Mundial de la Salud.",
body=f"""
La peste parece cosa de libros de historia, pero sigue existiendo. Esta infografía, con datos de la Organización Mundial de la Salud, muestra los casos en humanos entre 2010 y 2015.

{{IMG}}

## Casos y muertes (2010-2015)

| País | Casos | Muertes |
|---|---|---|
| Madagascar | 2,404 | 467 |
| Congo | 586 | 67 |
| Uganda | 72 | 12 |
| Perú | 66 | 7 |
| Tanzania | 61 | 7 |
| Estados Unidos | 39 | 5 |
| China | 10 | 5 |
| Mongolia | 5 | 2 |
| Bolivia | 3 | 2 |
| Kirguistán | 3 | 3 |
| Rusia | 1 | 0 |

El mapa marca también las zonas con mayor riesgo de infección, actualizadas a marzo de 2016.

## Lo que hay que saber

La peste es una infección bacteriana que transmiten sobre todo las pulgas de roedores. **Se trata con antibióticos**, y el diagnóstico temprano es clave. En 2017, Madagascar sufrió un brote importante, en gran parte de peste neumónica, que se contuvo con apoyo internacional.

Esta información es general; ante cualquier síntoma o duda, consulta a un profesional de la salud y sigue las indicaciones de las autoridades sanitarias.

## Por qué está en este blog

Es un buen ejemplo de cómo una infografía con mapa y círculos proporcionales comunica en segundos dónde está el problema. Lee [infografías: todo lo que debes saber]({S}/infografia-infografias-todo-lo-que-debes-de-saber/) y [algunos datos sobre el cerebro]({S}/infografia-algunos-datos-sobre-el-cerebro/).
""",
faq=[
("¿Todavía existe la peste?", "Sí. La OMS registra casos cada año, sobre todo en Madagascar y la República Democrática del Congo."),
("¿Cómo se transmite la peste?", "Principalmente por la picadura de pulgas de roedores infectados; la forma neumónica puede transmitirse entre personas."),
("¿La peste tiene cura?", "Sí, se trata con antibióticos, y el diagnóstico temprano es fundamental."),
],
related=[("Infografías: todo lo que debes saber", S + "/infografia-infografias-todo-lo-que-debes-de-saber/"), ("Algunos datos sobre el cerebro", S + "/infografia-algunos-datos-sobre-el-cerebro/")],
),

dict(
id=1683, slug="infografia-riesgos-de-seguridad-digital-para-establecimientos-medicos",
title="Riesgos de seguridad digital en clínicas y hospitales",
excerpt="Infografía de ESET sobre los riesgos de seguridad digital para establecimientos médicos: historias clínicas en riesgo, equipos sin antivirus, redes inseguras, personal negligente y medidas de protección.",
img_alt="Infografía de riesgos de seguridad para establecimientos médicos",
credit="Infografía: ESET Latinoamérica.",
body=f"""
Un expediente médico vale más en el mercado negro que una tarjeta de crédito. Por eso clínicas y hospitales son blanco frecuente de ataques. Esta infografía de ESET muestra dónde están los riesgos.

{{IMG}}

## Información en riesgo

- Historias clínicas y datos médicos.
- Datos personales y bancarios de pacientes y del personal.

## Los puntos débiles

- **Equipos sin antivirus** (área de resultados).
- **Equipos médicos vulnerables** (sala de estudios).
- **Equipos desactualizados.**
- **Personal negligente** que comparte datos de pacientes, por ejemplo por mensajería.
- **Redes inseguras** (recepción).
- **Servidores de correo desprotegidos** (administración).

## Medidas de seguridad

1. Antivirus.
2. Doble factor de autenticación.
3. Respaldos.
4. Cifrado.
5. Auditorías de seguridad.

## Para consultorios y clínicas en México

Los datos de salud son datos sensibles según la ley de protección de datos personales, y requieren cuidados especiales. Además de las medidas de la infografía: separa la red de pacientes de la red interna, capacita al personal para no compartir expedientes por WhatsApp personal y ten un plan para reaccionar ante un ataque de ransomware.

Lee [cómo proteger tu información del ransomware]({S}/infografia-protege-tu-informacion-del-ransomware/) y [111 consejos de ciberseguridad]({S}/infografia-111-consejos-para-elevar-la-ciberseguridad-de-tu-empresa/).
""",
faq=[
("¿Por qué los hospitales son blanco de ciberataques?", "Porque manejan datos médicos y financieros valiosos y no pueden detener su operación, lo que los vuelve vulnerables a la extorsión."),
("¿Qué medidas de seguridad necesita una clínica?", "Antivirus, verificación en dos pasos, respaldos, cifrado, auditorías, redes separadas y capacitación del personal."),
("¿Los datos de salud tienen protección especial?", "Sí; en México se consideran datos personales sensibles y requieren medidas de seguridad reforzadas."),
],
related=[("Cómo protegerte del ransomware", S + "/infografia-protege-tu-informacion-del-ransomware/"), ("111 consejos de ciberseguridad", S + "/infografia-111-consejos-para-elevar-la-ciberseguridad-de-tu-empresa/")],
),

dict(
id=1366, slug="infografia-las-necesidades-tecnologicas-de-las-empresas-del-siglo-xxi",
title="Los perfiles tecnológicos que necesitan las empresas",
excerpt="Infografía de ICEMD sobre las necesidades tecnológicas de las empresas del siglo XXI: perfiles en realidad virtual, nube, industria 4.0, ciencia de datos, ciberseguridad y hacking ético.",
img_alt="Infografía de las necesidades tecnológicas de las empresas del siglo XXI",
credit="Infografía: ICEMD, Instituto de la Economía Digital de ESIC.",
body=f"""
La transformación digital no la hacen las herramientas, la hacen las personas que saben usarlas. Esta infografía de ICEMD describe seis perfiles tecnológicos clave, qué aportan y por qué son necesarios.

{{IMG}}

## Los perfiles

**1. Realidad virtual y aumentada (Digital Solution Lead AR/VR)**
Desarrolla y adapta modelos y simulaciones, y apoya el diseño de soluciones avanzadas. Es clave para la experiencia de usuario y la simulación de productos.

**2. Nube y virtualización (soporte técnico de servicios cloud)**
Da soporte a la infraestructura en la nube (IaaS y SaaS) y asegura la continuidad de los servicios.

**3. Industria 4.0 (Expert Manufacturing e IoT Manager)**
Hace la fábrica más competitiva y eficiente con nuevas tecnologías y productos conectados. Es una posición estratégica.

**4. Ciencia de datos (Data Scientist Manager)**
Extrae información relevante con big data, machine learning e inteligencia de negocio. El dato es clave para decidir y para la productividad.

**5. Ciberseguridad y cumplimiento (Cybersecurity & Compliance Manager)**
Garantiza el cumplimiento de normas y protege a la empresa y sus productos de ataques. Sin este perfil no se puede digitalizar con seguridad.

**6. Hacking ético (Information Security Analyst)**
Busca vulnerabilidades antes que los atacantes y aporta soluciones de seguridad de la información.

## Lo que cambió

Todos siguen siendo demandados, y se sumaron perfiles de inteligencia artificial: ingenieros de machine learning, especialistas en IA generativa y responsables de gobernanza de datos. Para una pyme, no se trata de contratar a todos, sino de saber cuándo apoyarse en especialistas externos.

Lee [cómo será el trabajador del futuro]({S}/infografia-como-sera-el-trabajador-del-futuro/) y [5 desafíos de RR. HH. al implementar tecnología]({S}/infografia-5-desafios-de-rrhh-al-implementar-plataformas-tecnologicas/).
""",
faq=[
("¿Qué perfiles tecnológicos necesitan las empresas?", "Especialistas en nube, ciencia de datos, ciberseguridad, industria 4.0, realidad virtual y, cada vez más, inteligencia artificial."),
("¿Qué hace un data scientist?", "Analiza grandes volúmenes de datos con estadística y machine learning para generar información útil en la toma de decisiones."),
("¿Qué es el hacking ético?", "La práctica autorizada de buscar vulnerabilidades en sistemas para corregirlas antes de que las aprovechen atacantes."),
],
related=[("Cómo será el trabajador del futuro", S + "/infografia-como-sera-el-trabajador-del-futuro/"), ("5 desafíos de RR. HH. al implementar tecnología", S + "/infografia-5-desafios-de-rrhh-al-implementar-plataformas-tecnologicas/")],
),

dict(
id=1847, slug="infografia-guarda-y-clasifica-las-fotos-que-te-gusten-en-instagram",
title="Cómo guardar y clasificar fotos en Instagram",
excerpt="Infografía de cómo guardar y clasificar en colecciones las publicaciones que te gustan en Instagram, y cómo usar esta función para inspirarte y entender qué guarda tu audiencia.",
img_alt="Infografía de cómo guardar y clasificar las fotos que te gusten en Instagram",
body=f"""
¿Viste una publicación en Instagram que quieres consultar después? No necesitas hacer captura de pantalla. Esta infografía explica cómo guardarla y organizarla en colecciones.

{{IMG}}

## Los pasos

**1. Guarda las fotos que te gusten.** Toca el ícono de guardar que aparece debajo de la publicación. Si quieres quitarla, vuelve a tocarlo.

**2. Clasifícalas.** Mantén presionado el ícono de guardar hasta que aparezca la pantalla "Guardar en". Toca "+" para crear una colección nueva y darle nombre, o elige una colección existente.

La función sigue disponible: tus publicaciones guardadas están en tu perfil, en el menú, dentro de "Guardado". Solo tú puedes verlas, salvo que crees una colección compartida.

## Cómo usarlo en tu marca

- **Colecciones de inspiración:** ideas de contenido, competidores, diseños, tendencias.
- **Mide los guardados:** en las estadísticas de tus publicaciones, los "guardados" indican contenido útil que la gente quiere conservar. Es una de las señales más valiosas.
- **Crea contenido que se guarde:** guías, listas, tutoriales, plantillas e infografías suelen guardarse más.

Lee [8 estrategias de contenido para Instagram]({S}/infografia-8-estrategias-de-marketing-de-contenidos-para-instagram/) y [la historia de Instagram]({S}/infografia-historia-de-instagram/).
""",
faq=[
("¿Cómo guardar una publicación en Instagram?", "Toca el ícono de guardar debajo de la publicación; para organizarla, mantenlo presionado y elige o crea una colección."),
("¿Dónde veo mis publicaciones guardadas en Instagram?", "En tu perfil, en el menú, dentro de la opción Guardado."),
("¿Por qué importan los guardados para una marca?", "Porque indican que el contenido es útil y la gente quiere volver a él; suelen ser una buena señal de calidad."),
],
related=[("8 estrategias de contenido para Instagram", S + "/infografia-8-estrategias-de-marketing-de-contenidos-para-instagram/"), ("Historia de Instagram", S + "/infografia-historia-de-instagram/")],
),

dict(
id=1398, slug="infografia-el-auge-de-loa-videos-online-en-las-pantallas-de-tv",
title="El auge del video en línea en la pantalla de TV",
excerpt="Infografía de Think with Google sobre el auge de YouTube en el televisor: el tiempo de visualización en TV se duplicó, 2 de cada 3 espectadores lo ven ahí y es más probable verlo acompañado.",
img_alt="Infografía del auge de los videos online en las pantallas de TV",
credit="Infografía: Think with Google, con datos de YouTube.",
body=f"""
Durante años, YouTube se veía en la computadora o el celular. Esta infografía de Google mostraba que el video en línea estaba llegando a la sala, a la pantalla del televisor.

{{IMG}}

## Lo que muestra

- **El tiempo que se pasa viendo YouTube en la TV se duplicó** en un año.
- **2 de cada 3** espectadores de YouTube dicen verlo en una pantalla de TV.
- **Hay horarios de máxima audiencia,** igual que en la televisión tradicional.
- **El fin de semana sube** el tiempo de visualización en la TV.
- **Se ve en compañía:** es el doble de probable ver YouTube con otras personas en la TV que en el celular o la computadora.

Hace solo diez años, recuerda la infografía, las smart TV acababan de salir, Netflix empezaba con el streaming y Chromecast no existía.

## Lo que pasó después

La tendencia se consolidó: la TV conectada se volvió una de las pantallas principales para YouTube, y la publicidad en televisión conectada creció con fuerza. Muchas personas ya no distinguen entre "ver televisión" y "ver YouTube".

## Para tu marca

Si haces video, piensa también en cómo se verá en una pantalla grande y en grupo: buena calidad de imagen y sonido, y contenido que funcione para varios espectadores. Lee [la atención a los anuncios importa más que el alcance]({S}/infografia-la-atencion-a-los-anuncios-la-efectividad-no-solo-depende-de-la-cobertura/) y [datos que debes conocer sobre el video]({S}/infografia-algunos-datos-que-debes-conocer-sobre-el-video/).
""",
faq=[
("¿Cuánta gente ve YouTube en la televisión?", "Según la infografía, 2 de cada 3 espectadores de YouTube lo ven en una pantalla de TV."),
("¿Cuándo se ve más YouTube en la TV?", "En horarios de máxima audiencia y durante los fines de semana, como la televisión tradicional."),
("¿Qué es la TV conectada?", "Un televisor conectado a internet, directamente o mediante un dispositivo, que permite ver apps de video como YouTube o Netflix."),
],
related=[("La atención a los anuncios", S + "/infografia-la-atencion-a-los-anuncios-la-efectividad-no-solo-depende-de-la-cobertura/"), ("Datos que debes conocer sobre el video", S + "/infografia-algunos-datos-que-debes-conocer-sobre-el-video/")],
),

dict(
id=1659, slug="infografia-13-consejos-sencillos-para-posicionar-sin-saber-seo",
title="13 consejos sencillos para posicionar sin saber SEO",
excerpt="Infografía con 13 consejos sencillos para posicionar tu web sin ser experto en SEO: palabras clave, escribir para el usuario, titulares, contenido de calidad, responsive, velocidad, HTTPS e imágenes.",
img_alt="Infografía de 13 consejos facilitos para posicionar sin ser experto en SEO",
body=f"""
No necesitas ser experto para que Google te encuentre. Esta infografía resume trece consejos sencillos que cualquier persona puede aplicar.

{{IMG}}

## Los 13 consejos

1. **Elige tus palabras clave:** usa sinónimos, plurales y variaciones.
2. **Escribe para el usuario, no para Google.** Con naturalidad.
3. **Optimiza el titular:** incluye la palabra clave y no pases de 70 caracteres.
4. **Crea contenido de calidad,** de interés para tu público.
5. **Haz tu web responsive,** que se adapte a todos los dispositivos.
6. **Difunde tu contenido** en redes sociales.
7. **Usa Google+,** para que los bots te indexen más rápido.
8. **Usa URL amigables:** sin números raros ni símbolos.
9. **Cuida el tiempo de carga.**
10. **Enlaces de calidad, no cantidad.**
11. **Usa HTTPS** para la seguridad de tus usuarios y la autoridad de tu página.
12. **Longitud del contenido:** mejor más de 750 palabras, aunque la propia infografía advierte que es debatible.
13. **Nombra y etiqueta tus imágenes** con tus palabras clave.

## Lo que ajustaríamos hoy

- **Google+ cerró en 2019;** el consejo 7 ya no aplica. Para que Google descubra tus páginas, envía tu mapa del sitio en Google Search Console.
- **Titulares:** Google suele mostrar alrededor de 60 caracteres.
- **Longitud:** no hay un número mágico. La extensión correcta es la que responde por completo la pregunta.
- **Imágenes:** el texto ALT debe describir la imagen; usa la palabra clave solo si encaja.

Lo demás sigue siendo la base. Revisa el [checklist SEO antes de publicar]({S}/infografia-checklist-seo-antes-de-publicar-un-articulo/) y cómo funciona una [campaña en buscadores]({BUSCADORES}).
""",
faq=[
("¿Cómo posicionar mi web sin saber SEO?", "Eligiendo bien tus palabras clave, escribiendo contenido útil y natural, con buenos títulos, sitio rápido, adaptado al celular, seguro con HTTPS y con buenos enlaces."),
("¿Sigue sirviendo publicar en Google+ para SEO?", "No; Google+ cerró en 2019. Usa Google Search Console para que Google descubra tus páginas."),
("¿Cuántas palabras debe tener un artículo para posicionar?", "No hay una cifra fija; debe tener la extensión necesaria para responder bien la búsqueda."),
],
related=[("Checklist SEO antes de publicar", S + "/infografia-checklist-seo-antes-de-publicar-un-articulo/"), ("Campaña en buscadores", BUSCADORES)],
),

dict(
id=2025, slug="infografia-errores-seo-en-una-tienda-online",
title="3 errores SEO que hacen perder dinero a tu tienda en línea",
excerpt="Infografía con errores SEO que hacen perder dinero a una tienda en línea: no poner texto optimizado en la home y las categorías, descuidar el enlazado interno y no optimizar el peso de las imágenes.",
img_alt="Infografía de errores SEO que hacen perder dinero en una tienda online",
credit="Infografía: Zoping, agencia de marketing digital.",
body=f"""
Una tienda en línea vive de que la encuentren. Esta infografía señala tres errores SEO que se repiten en muchas tiendas y que, literalmente, cuestan ventas.

{{IMG}}

## Los 3 errores

**1. No poner texto en la página de inicio y en las categorías.**
Los buscadores necesitan texto para entender de qué trata cada página. Un buen texto optimizado en categorías y en la home ayuda a posicionar la palabra clave objetivo. Las tiendas grandes lo hacen.

**2. Descuidar el enlazado interno.**
Enlaza categorías relacionadas en sus descripciones. El enlazado interno da pistas a los buscadores sobre qué palabra clave quieres posicionar en cada URL y ayuda a que los rastreen más rápido.

**3. No optimizar el peso de las imágenes.**
Las imágenes pesadas hacen lenta la tienda. Busca el equilibrio entre peso y calidad para que cargue rápido sin perjudicar cómo se ven los productos.

## Tres más que vemos seguido

- **Fichas de producto con la descripción copiada del fabricante:** escribe la tuya.
- **Productos agotados que se eliminan** sin redirección y dejan errores 404.
- **Filtros que generan miles de URL** casi iguales; controla cuáles se indexan.

Lee [10 secretos del ecommerce rentable]({S}/infografia-secretos-del-comercio-electronico-rentable/) y [9 herramientas para comprimir imágenes]({S}/infografia-9-mejores-herramientas-online-para-comprimir-imagenes/).
""",
faq=[
("¿Por qué las categorías de una tienda necesitan texto?", "Porque los buscadores usan el texto para entender de qué trata la página y para qué búsquedas mostrarla."),
("¿Qué es el enlazado interno?", "Los enlaces entre páginas de tu propio sitio, que ayudan a usuarios y buscadores a navegar y entender la estructura."),
("¿Cómo afectan las imágenes al SEO de una tienda?", "Las imágenes pesadas hacen lenta la carga, lo que empeora la experiencia y puede afectar el posicionamiento."),
],
related=[("10 secretos del ecommerce rentable", S + "/infografia-secretos-del-comercio-electronico-rentable/"), ("9 herramientas para comprimir imágenes", S + "/infografia-9-mejores-herramientas-online-para-comprimir-imagenes/")],
),
]
