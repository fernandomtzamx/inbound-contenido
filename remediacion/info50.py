from comun import *

POSTS = [
dict(
id=1841, slug="infografia-desglose-de-una-nomina-de-un-trabajador-temporal",
title="Desglose de la nómina de un trabajador temporal",
excerpt="Infografía de Wolters Kluwer que desglosa una nómina temporal en España: con 1,500 euros brutos, la empresa paga 2,019 y el trabajador recibe 1,269 netos.",
img_alt="Infografía de la nómina: el salario bruto y el salario neto",
credit="Infografía: Wolters Kluwer (España).",
body=f"""
¿Por qué tu sueldo neto es menor que el bruto, y por qué a la empresa le cuesta más que el bruto? Esta infografía de Wolters Kluwer lo desglosa con un ejemplo de España.

{{IMG}}

## El caso

Salario bruto de 1,500 euros al mes, contrato temporal, trabajador soltero y sin hijos.

## Lo que paga la empresa: 2,019 euros

Al bruto se suman **519 euros** de Seguridad Social a cargo de la empresa:
- Contingencias comunes (pensiones): 354 euros (23.6%).
- Desempleo: 100.5 euros (6.7%).
- Accidentes de trabajo y enfermedad profesional: 52.5 euros (3.5%, depende del puesto).
- Formación profesional: 9 euros (0.6%).
- Fogasa (cobertura de despidos en empresas en quiebra): 3 euros (0.2%).

## Lo que recibe el trabajador: 1,269 euros

Del bruto se restan **231 euros**:
- IRPF (anticipo del impuesto sobre la renta): 135 euros (9%), según la situación personal y el tipo de contrato.
- Cotización a la Seguridad Social: 96 euros, que incluyen contingencias comunes, 70.5 euros (4.7%); desempleo, 24 euros (1.6%); y formación profesional, 1.5 euros (0.1%).

## ¿Y en México?

La lógica es la misma, con otros conceptos: al trabajador se le retiene el ISR y su cuota del IMSS, y el patrón paga además sus cuotas del IMSS, el Infonavit, el SAR y el impuesto estatal sobre nómina. Por eso, al calcular cuánto cuesta contratar, el sueldo bruto nunca es la cifra completa. Consulta a tu contador para tu caso concreto.

Lee [el desglose de la nómina de un trabajador indefinido]({S}/infografia-desglose-de-una-nomina-de-un-trabajador-indefinido/) y [el salario emocional para retener talento]({S}/infografia-salario-emocional-la-clave-para-retener-el-talento/).
""",
faq=[
("¿Qué diferencia hay entre salario bruto y neto?", "El bruto es lo pactado antes de impuestos y cotizaciones; el neto es lo que el trabajador recibe después de las retenciones."),
("¿Cuánto le cuesta a la empresa un trabajador?", "Más que el sueldo bruto: en el ejemplo español, 1,500 euros brutos le cuestan 2,019 a la empresa."),
("¿Qué se le descuenta a un trabajador en México?", "Principalmente el ISR y su cuota del IMSS; el patrón paga además sus propias cuotas y el impuesto estatal sobre nómina."),
],
related=[("Nómina de un trabajador indefinido", S + "/infografia-desglose-de-una-nomina-de-un-trabajador-indefinido/"), ("Salario emocional", S + "/infografia-salario-emocional-la-clave-para-retener-el-talento/")],
),

dict(
id=1501, slug="infografia-el-desafio-de-la-ciberseguridad-en-el-iot",
title="El desafío de la ciberseguridad en el IoT",
excerpt="Infografía de Telefónica sobre el reto de la ciberseguridad en el internet de las cosas: el costo del cibercrimen pasaría de 100,000 millones de dólares en 2014 a más de 6 billones en 2021.",
img_alt="Infografía del desafío de la ciberseguridad en el IoT",
credit="Infografía: Telefónica IoT, con datos de Lookout, Cisco, Juniper Research, Forbes y Cybersecurity Ventures.",
body=f"""
Cada dispositivo conectado es una puerta más para los atacantes. Esta infografía de Telefónica muestra el tamaño del reto.

{{IMG}}

## El costo del cibercrimen crece cada año

| Año | Costo estimado |
|---|---|
| 2014 | 100,000 millones de dólares |
| 2015 | 400,000 millones |
| 2016 | 1.2 billones (millones de millones) |
| 2017 | 2.9 billones |
| 2018 | 3.8 billones |
| 2019 | 4.7 billones |
| 2020 | 5.5 billones |
| 2021 | Más de 6 billones |

## Más cifras

- Habría **3.5 millones** de puestos de ciberseguridad sin cubrir en 2021: el triple que antes.
- El gasto en ciberseguridad superaría **1 billón de dólares** entre 2017 y 2021; en 2016 ya pasaba de 80,000 millones.
- Dispositivos conectados: **28,400 millones** en 2017, **30,700 millones** en 2020 y **75,400 millones** previstos para 2025.
- Habría más de **600 millones** de wearables.
- Una filtración de datos móviles podía poner en riesgo **26.4 millones de dólares** a una empresa.
- El daño global por ransomware superaría **5,000 millones** en 2017.

## Lo que pasó después

El ransomware se volvió la principal amenaza para empresas de todos los tamaños, incluidas pymes, hospitales y gobiernos en México. Y la falta de especialistas en ciberseguridad sigue siendo un problema mundial. Para una pyme, lo básico ya protege mucho: respaldos fuera de línea, actualizaciones, verificación en dos pasos y redes separadas para los dispositivos IoT.

Lee [ciberseguridad del IoT en la empresa]({S}/infografia-ciberseguridad-del-internet-de-las-cosas-en-la-empresa/) y [cómo detectar sitios web y correos falsos]({S}/infografia-como-detectar-webs-y-emails-falsos/).
""",
faq=[
("¿Por qué el internet de las cosas es un riesgo de seguridad?", "Porque hay miles de millones de dispositivos conectados, muchos con contraseñas débiles o sin actualizaciones, que pueden usarse para entrar a una red."),
("¿Cuánto cuesta el cibercrimen?", "Las estimaciones citadas pasaban de 100,000 millones de dólares en 2014 a más de 6 billones en 2021."),
("¿Cómo puede protegerse una pyme?", "Con respaldos fuera de línea, actualizaciones constantes, verificación en dos pasos, contraseñas fuertes y redes separadas para los dispositivos conectados."),
],
related=[("Ciberseguridad del IoT en la empresa", S + "/infografia-ciberseguridad-del-internet-de-las-cosas-en-la-empresa/"), ("Cómo detectar webs y correos falsos", S + "/infografia-como-detectar-webs-y-emails-falsos/")],
),

dict(
id=2311, slug="infografia-smartcars-los-coches-del-futuro",
title="Smart cars: los autos del futuro",
excerpt="Infografía de IDAT sobre los autos inteligentes: la evolución de 2013 a 2017, cómo funcionan los autónomos, su impacto en la seguridad vial y sus beneficios.",
img_alt="Infografía de smart cars, los autos del futuro",
credit="Infografía: IDAT.",
body=f"""
Desde la invención del automóvil en 1885, la industria no ha dejado de agregar mejoras para reducir errores y hacer más fácil manejar. Esta infografía de IDAT explica hacia dónde iban los autos inteligentes en 2017.

{{IMG}}

## Línea de tiempo

- **2013:** control de distancia, con láser y radar.
- **2014:** conexión a internet 4G en los autos.
- **2015:** combustible de hidrógeno (Toyota, Honda y Nissan).
- **2016:** encendido a distancia desde el celular.
- **2017:** el smart car, sin volante, palanca ni pedales, controlado por computadora y sensores.

## Cómo funcionaban los prototipos autónomos

Con batería y botón de arranque y paro; sensores de 360 grados para evitar puntos ciegos; manejados por completo por una computadora; velocidad máxima de 40 km/h; capacidad para dos personas.

## Impacto en la sociedad

- Más del **90%** de los accidentes son causados por errores humanos.
- Se podrían prevenir **30,000 muertes y 2 millones de lesiones**.
- El **81%** de los accidentes podría evitarse con un uso eficiente del vehículo y sus sistemas de comunicación.
- La computadora reacciona mucho más rápido que una persona y no se distrae.
- Reducirían el tiempo en el tráfico (2.4 años de vida por persona) y la contaminación.

**Distracciones más frecuentes al volante:** conversar con pasajeros (80%), ajustar el radio (65%), comer o beber (45%), hacer o contestar llamadas (40%), usar dispositivos (30%) e interactuar con niños en el asiento de atrás (27%).

**Datos importantes:** 1.2 millones de personas morían al año en accidentes de tránsito; se esperaba que para 2020 estos autos se produjeran en masa; la tecnología costaba más de 250,000 dólares por auto.

**Beneficios:** eliminan factores humanos como cansancio, alcohol o distracciones; alivian el tráfico y ahorran combustible; ayudan a personas con problemas de visión; y reducen la necesidad de estacionamiento.

## Lo que pasó después

La producción masiva no llegó en 2020. Hoy existen servicios de robotaxi en algunas ciudades de Estados Unidos y China, y muchos autos nuevos traen asistencias (frenado automático, control de carril, crucero adaptativo), pero el auto 100% autónomo para uso personal todavía no es común. Lee [coches conectados mediante 5G]({S}/infografia-coches-conectados-mediante-5g/) y [qué fabricantes tienen más patentes sobre el coche autónomo]({S}/infografia-que-fabricantes-tienen-mas-patentes-sobre-el-coche-autonomo/).
""",
faq=[
("¿Qué es un smart car?", "Un auto con sensores, conectividad y computadoras que asisten o sustituyen al conductor."),
("¿Ya existen autos autónomos?", "Hay servicios de robotaxi en algunas ciudades, pero los autos totalmente autónomos para uso personal todavía no son comunes."),
("¿Por qué los autos autónomos serían más seguros?", "Porque la mayoría de los accidentes se deben a errores humanos, y una computadora reacciona más rápido y no se distrae."),
],
related=[("Coches conectados mediante 5G", S + "/infografia-coches-conectados-mediante-5g/"), ("Patentes del coche autónomo", S + "/infografia-que-fabricantes-tienen-mas-patentes-sobre-el-coche-autonomo/")],
),

dict(
id=1482, slug="infografia-que-buscan-los-consumidores-en-un-commerce",
title="Qué buscan los consumidores en una tienda online",
excerpt="Infografía de RodrigoHM con lo que buscan los consumidores en un ecommerce: un sitio rápido y fácil, información detallada, buenas imágenes, reseñas confiables y un buen buscador.",
img_alt="Infografía de qué buscan los consumidores en sitios de ecommerce",
credit="Infografía: RodrigoHM.com.",
body=f"""
Una tienda online compite contra todas las demás a un clic de distancia. Esta infografía de RodrigoHM resume lo que más valoran los compradores.

{{IMG}}

## 1. Un sitio fácil de usar y que cargue rápido

- El **47%** dice que la funcionalidad y el diseño responsivo son lo más importante.
- La navegación es lo que más pesa al juzgar si un sitio es fácil de usar.
- **3 de cada 4** compradores abandonarían un sitio lento.
- El **51%** ya compra desde el celular, y el **77%** de quienes tienen entre 18 y 29 años.

## 2. Información precisa y detallada

- El **68%** quiere conocer a detalle el producto, y al **77%** el contenido del producto le influye en la compra.
- El **40%** espera encontrar preguntas y respuestas, y el **83%** valora poder preguntar.
- El **42%** ha devuelto una compra porque el producto no coincidía con la descripción. (La infografía dice además que el 86% "volvería" a comprar en un sitio con información imprecisa; por el contexto, parece un error y el dato se refiere a quienes no volverían.)

## 3. Imágenes grandes, claras y con detalles

- El **26%** ha abandonado una compra por imágenes malas o insuficientes.
- El **50%** quiere imágenes de alta calidad en general, y el **67%** en las páginas de producto.
- El **71%** usa el zoom con regularidad.
- El **39%** deja un sitio si las imágenes no cargan rápido.

## 4. Reseñas y calificaciones variadas y confiables

- El **73%** quiere ver qué dicen otros compradores antes de decidir, y el **50%** quiere reseñas de expertos.
- Las reseñas les dan seguridad, hacen al sitio más serio y ayudan a asegurar la calidad.
- Pero el **48%** no sabe si las reseñas en internet son reales.

## 5. Un buscador rápido y útil

- El **71%** usa el buscador del sitio con regularidad, y el **70%** valora poder filtrar resultados.
- Haz visible la barra de búsqueda, agrega autocompletado, usa búsqueda semántica, incluye migas de pan (breadcrumbs) y muestra imágenes y calificaciones en los resultados.

## Para tu tienda

Revisa tu sitio desde un celular, con datos móviles, como lo haría tu cliente: ¿carga rápido?, ¿encuentras un producto en dos búsquedas?, ¿las fotos se ven bien?, ¿hay reseñas? Lee [los secretos del comercio electrónico rentable]({S}/infografia-secretos-del-comercio-electronico-rentable/) y [errores SEO en una tienda online]({S}/infografia-errores-seo-en-una-tienda-online/).
""",
faq=[
("¿Qué valoran más los compradores en una tienda online?", "Que sea rápida y fácil de usar, con información detallada, buenas imágenes, reseñas confiables y un buen buscador."),
("¿Por qué importan las fotos en un ecommerce?", "Porque el cliente no puede tocar el producto; el 26% ha abandonado compras por imágenes malas o insuficientes."),
("¿Conviene mostrar reseñas en mi tienda?", "Sí: el 73% quiere leer opiniones de otros compradores antes de decidir."),
],
related=[("Secretos del comercio electrónico rentable", S + "/infografia-secretos-del-comercio-electronico-rentable/"), ("Errores SEO en una tienda online", S + "/infografia-errores-seo-en-una-tienda-online/")],
),

dict(
id=1478, slug="infografia-con-quien-pasamos-el-tiempo",
title="¿Con quién pasamos el tiempo según la edad?",
excerpt="Infografía de Insider Pro con datos de The Atlas: cómo cambia, a lo largo de la vida, el tiempo diario que pasamos con amigos, familia, compañeros, hijos, pareja y solos.",
img_alt="Infografía de con quién pasamos el tiempo según la edad",
credit="Infografía: Insider Pro, con datos de The Atlas.",
body=f"""
¿Con quién pasas tus horas a los 20, a los 40 y a los 80? Esta infografía de Insider Pro, con datos de The Atlas, muestra cómo cambia a lo largo de la vida.

{{IMG}}

## Lo que muestran las gráficas (horas al día, por edad)

- **Amigos:** más de 2 horas en la adolescencia; baja rápido después de los 20 y se queda en menos de una hora.
- **Familia:** más de 4 horas a los 15 años; cae en la juventud y se mantiene cerca de una hora.
- **Compañeros de trabajo:** suben desde los 20 y se mantienen en 3 a 4 horas hasta los 60; luego casi desaparecen.
- **Hijos:** crecen desde los 20, con un máximo de más de 4 horas cerca de los 35 a 40 años, y bajan después.
- **Pareja:** suben desde los 20, se mantienen en unas 3 horas y alcanzan un máximo cerca de los 70.
- **Solos:** es la única curva que crece casi toda la vida: de unas 3 a 4 horas en la juventud a más de 8 a los 80.

## Lo que significa

Pasamos cada vez más tiempo solos conforme envejecemos, y los amigos pierden espacio muy pronto. Para las empresas, esto explica por qué el trabajo es una de las principales fuentes de relaciones en la vida adulta, y por qué una buena cultura laboral importa tanto.

Para las marcas, también es una pista: cada etapa de la vida tiene con quién y para quién se compra (los hijos, la pareja, uno mismo). Lee [cómo será el trabajador del futuro]({S}/infografia-como-sera-el-trabajador-del-futuro/) y [habilidades sociales]({S}/infografia-habilidades-sociales/).
""",
faq=[
("¿Con quién pasamos más tiempo en la vida adulta?", "Según los datos, con compañeros de trabajo, hijos y pareja; y el tiempo a solas crece con la edad."),
("¿A qué edad pasamos más tiempo con amigos?", "En la adolescencia, con más de dos horas diarias; después de los 20 baja a menos de una hora."),
("¿De dónde vienen los datos?", "De The Atlas, publicados por Insider Pro, con base en encuestas de uso del tiempo en Estados Unidos."),
],
related=[("Cómo será el trabajador del futuro", S + "/infografia-como-sera-el-trabajador-del-futuro/"), ("Habilidades sociales", S + "/infografia-habilidades-sociales/")],
),

dict(
id=1464, slug="infografia-inbound-sales-vs-otbound-sales",
title="Inbound sales vs. outbound sales",
excerpt="Infografía de Postedin que compara las ventas inbound (centradas en el cliente, con contenido relevante y resultados medibles) con las outbound (intrusivas, masivas y difíciles de medir).",
img_alt="Infografía de inbound sales vs outbound sales",
credit="Infografía: Postedin.",
body=f"""
Vender interrumpiendo o vender ayudando: esa es la diferencia de fondo. Esta infografía de Postedin compara las ventas inbound con las outbound.

{{IMG}}

## La comparación

| Inbound sales | Outbound sales |
|---|---|
| Se centra en el usuario y el prospecto, con contenido relevante | Se centra en mostrar las características del producto, interrumpiendo al cliente cuando no busca información |
| Atrae antes de invadir; gana atención y confianza | Busca al cliente en medios tradicionales para ganar su atención |
| Comunicación interactiva, que permite conocer necesidades y opiniones reales | Acciones a menudo intrusivas; sin planeación, pueden resultar molestas |
| Llega a un público segmentado y realmente interesado | Suele dirigirse a gente que no necesariamente está interesada |
| Resultados medibles, que permiten mejorar continuamente | Resultados difíciles de medir |
| Comunicación bidireccional en un entorno casi totalmente digital | Comunicación unidireccional y masiva, sin canales personalizados |

## ¿Uno u otro?

En la práctica, muchas empresas combinan ambos: el inbound atrae y educa a prospectos, y un outbound bien segmentado (una llamada o un correo personalizado a una empresa que encaja con tu cliente ideal) acelera las ventas. La clave es que el contacto sea relevante para quien lo recibe.

Lee [outbound marketing vs. inbound marketing]({S}/infografia-outbound-marketing-vs-inbound-marketing/) y [qué es el inbound marketing]({GUIA}).
""",
faq=[
("¿Qué son las inbound sales?", "Una forma de vender centrada en el prospecto: lo atrae con contenido útil y lo acompaña según sus necesidades, sin interrumpirlo."),
("¿Qué son las outbound sales?", "La venta tradicional que sale a buscar al cliente, con llamadas en frío, publicidad masiva o correos no solicitados."),
("¿Se pueden combinar inbound y outbound?", "Sí: muchas empresas atraen prospectos con inbound y usan outbound personalizado para cuentas bien seleccionadas."),
],
related=[("Outbound vs. inbound marketing", S + "/infografia-outbound-marketing-vs-inbound-marketing/"), ("Qué es el inbound marketing", GUIA)],
),

dict(
id=1961, slug="infografia-guia-para-hacer-un-podcast",
title="Guía para hacer un podcast en 8 pasos",
excerpt="Infografía de Rosana Rosas con 8 pasos para hacer un podcast: elegir el tema, diseñar la portada, escribir el guion, reunir el equipo, grabar, editar, publicar y difundir.",
img_alt="Infografía de guía para hacer un podcast",
credit="Infografía: Rosana Rosas (@rosanarosas17).",
body=f"""
Un podcast es barato, lo puedes hacer tú mismo y te acerca a tu audiencia. Esta infografía de Rosana Rosas explica cómo hacerlo en ocho pasos.

{{IMG}}

## Los 8 pasos

1. **Escoge el tema:** relacionado con tu nicho o sector, y que le interese a tu audiencia.
2. **Diseña la portada:** una imagen atractiva que identifique el tema.
3. **Escribe tu guion:** con introducción, desarrollo y cierre.
4. **Reúne el equipo:** una computadora, un micrófono, audífonos y, para grabar en exteriores, una grabadora o un smartphone.
5. **Graba:** cuida el volumen y cambia la entonación para no sonar monótono.
6. **Edita:** corta silencios y errores, y agrega efectos y música.
7. **Publica:** súbelo a una plataforma de podcasts con descripción y etiquetas.
8. **Difunde:** intégralo a tu blog y compártelo en tus redes.

**Software de grabación y edición:** Audacity, Adobe Audition y Sound Forge.
**Plataformas:** iTunes, SoundCloud, Spreaker e iVoox.

## Lo que cambió

Hoy los podcasts se escuchan sobre todo en Spotify, Apple Podcasts y YouTube, y cada vez más se graban en video. Hay herramientas que simplifican todo, como Spotify for Creators para publicar y editores con inteligencia artificial que eliminan muletillas y ruido. Lo que no cambió: la constancia y un tema claro son lo que hace crecer un podcast.

Lee [la evolución del audiolibro en español]({S}/infografia-evolucion-del-audiolibro-en-espanol/) y [formatos de contenido para tu estrategia]({FORMATOS}).
""",
faq=[
("¿Qué necesito para hacer un podcast?", "Un tema claro, un guion, un micrófono, audífonos, una computadora o celular, un programa de edición y una plataforma para publicarlo."),
("¿Dónde publicar un podcast?", "En plataformas como Spotify, Apple Podcasts y YouTube; desde un solo servicio de alojamiento puedes distribuirlo a varias."),
("¿Cuánto cuesta hacer un podcast?", "Puede ser muy barato: con un buen micrófono y software gratuito como Audacity puedes empezar."),
],
related=[("Evolución del audiolibro en español", S + "/infografia-evolucion-del-audiolibro-en-espanol/"), ("Formatos de contenido", FORMATOS)],
),

dict(
id=1376, slug="infografia-juego-de-tronos-el-mercado-que-mueve",
title="Juego de Tronos: el mercado que mueve",
excerpt="Infografía de idealo sobre el mercado de Juego de Tronos: búsquedas en Google, personajes favoritos, productos más buscados (61% DVD y Blu-ray) y la temporada preferida.",
img_alt="Infografía de Juego de Tronos y el mercado que mueve",
credit="Infografía: idealo, con datos de Google Trends y del comparador idealo (junio 2016 a julio 2017).",
body=f"""
Una serie exitosa no solo vende suscripciones: mueve juguetes, juegos y colecciones. Esta infografía del comparador idealo analiza el mercado de Juego de Tronos.

{{IMG}}

## La popularidad no paraba de crecer

Las búsquedas en Google subían con cada estreno de temporada, y cada pico era más alto que el anterior, de 2011 a 2017.

## Los personajes favoritos (más buscados en figuras)

| # | Hombres | Mujeres |
|---|---|---|
| 1 | Robb Stark | Daenerys Targaryen |
| 2 | Jon Nieve | Arya Stark |
| 3 | Tyrion Lannister | Sansa Stark |
| 4 | Eddard "Ned" Stark | Brienne de Tarth |

## Productos más buscados por categoría

DVD y Blu-ray 61.2%, juegos de mesa 29.98%, figuras 4.26%, videojuegos 3.02%, otros 1.08% y estampas 0.46%.

## Temporadas preferidas (DVD y Blu-ray)

Temporada 6: 50%. Temporada 5: 18%. Temporada 4: 16%. Temporadas 1 y 3: 6%. Temporada 2: 4%.

## Lo más buscado

- **Juegos de mesa:** Monopoly (edición coleccionista), Risk y Cluedo de Game of Thrones.
- **Figuras:** Funko Pop! TV y Vinyl de Game of Thrones, y Dark Horse Comics.
- **Videojuegos:** Game of Thrones: A Telltale Games Series, A Song of Ice and Fire y A Game of Thrones: Genesis.

## Para las marcas

Una historia fuerte crea un ecosistema de productos. La serie terminó en 2019 y sigue viva con precuelas como La casa del dragón. Para cualquier marca, la lección es la misma: si tu comunidad se emociona con algo, hay productos y contenidos alrededor que puedes ofrecer. Lee [la industria del videojuego]({S}/infografia-la-industria-del-videojuego/) y [ventas de productos icónicos]({S}/infografia-ventas-mundiales-de-productos-iconicos-desde-su-lanzamiento/).
""",
faq=[
("¿Qué productos de Juego de Tronos se buscaban más?", "DVD y Blu-ray (61.2%), seguidos de juegos de mesa (29.98%)."),
("¿Cuál era la temporada favorita?", "La sexta, con 50% del interés de compra en DVD y Blu-ray."),
("¿Quiénes eran los personajes más buscados?", "Robb Stark y Daenerys Targaryen encabezaban las búsquedas de figuras."),
],
related=[("La industria del videojuego", S + "/infografia-la-industria-del-videojuego/"), ("Ventas de productos icónicos", S + "/infografia-ventas-mundiales-de-productos-iconicos-desde-su-lanzamiento/")],
),

dict(
id=1997, slug="infografia-las-primeras-ciudades-que-seran-afectadas-por-el-cambio-climatico-son-%c2%85",
title="Las primeras ciudades que sufrirán el cambio climático",
excerpt="Infografía de Insider Pro con datos de The Washington Post: el año en que cada ciudad viviría un cambio climático drástico si no se reducen las emisiones. Ciudad de México: 2031.",
img_alt="Infografía de las primeras ciudades en sufrir el cambio climático",
credit="Infografía: Insider Pro, con datos de Leonard Bernstein y Gene Thorp (The Washington Post).",
body=f"""
¿Cuándo dejaría de ser "normal" el clima de tu ciudad? Esta infografía muestra el año estimado en que distintas ciudades vivirían un cambio climático drástico si no se reducen las emisiones de dióxido de carbono.

{{IMG}}

## Qué significa la fecha

Es el año a partir del cual la temperatura media del año más frío sería mayor que la de los años más calientes registrados entre 1860 y 2005 en ese lugar. Es decir: a partir de entonces, hasta el año más fresco sería más caliente que cualquiera del pasado.

## Algunas ciudades

- **Primero, en zonas tropicales:** Manokwari (2020), Kingston y Ngerulmud (2023), Lagos y Georgetown (2029), Yakarta (2029), Singapur (2028).
- **América Latina:** Ciudad de México (2031), Bogotá (2033), Lima (2038), Santiago (2043), Río de Janeiro (2050).
- **Estados Unidos:** Fénix y Honolulu (2043), Nueva York y Washington (2047), Los Ángeles (2048), Chicago (2052), Seattle (2055), Anchorage (2071).
- **Europa y Asia:** Roma (2044), Pekín y Bangkok (2046), Londres (2056), Moscú (2063), San Petersburgo (2064), Reikiavik (2066), Tokio (2041).

El patrón es claro: los trópicos, donde el clima varía poco, serían los primeros en salir de su rango histórico.

## Lo que pasó después

Las fechas corresponden a un escenario de emisiones altas. Los últimos años han roto récords de temperatura, y los acuerdos climáticos buscan evitar ese escenario. Para las empresas, el tema ya es de negocio: consumidores, inversionistas y reguladores piden medir y reducir emisiones. Lee [qué es el packaging sustentable]({S}/infografia-packaging-sustentable/) y [tecnologías de energía solar]({S}/infografia-tecnologias-de-energia-solar/).
""",
faq=[
("¿Cuándo afectaría el cambio climático a la Ciudad de México?", "Según la proyección, hacia 2031 su año más frío sería más cálido que cualquier año del periodo 1860-2005, si no se reducen las emisiones."),
("¿Por qué los trópicos serían los primeros afectados?", "Porque su clima varía poco de un año a otro, así que un aumento pequeño de temperatura los saca más rápido de su rango histórico."),
("¿Estas fechas son seguras?", "No; son proyecciones bajo un escenario de emisiones altas, y pueden cambiar si se reducen las emisiones."),
],
related=[("Packaging sustentable", S + "/infografia-packaging-sustentable/"), ("Tecnologías de energía solar", S + "/infografia-tecnologias-de-energia-solar/")],
),

dict(
id=1378, slug="infografia-5-datos-clave-sobre-los-empleos-del-futuro",
title="5 datos clave sobre los empleos del futuro",
excerpt="Infografía del Banco Mundial con 5 datos sobre los empleos del futuro: 600 millones de empleos por crear para 2030, automatización, nuevas habilidades y brechas en América Latina.",
img_alt="Infografía de 5 datos clave sobre los empleos del futuro",
credit="Infografía: Banco Mundial.",
body=f"""
El trabajo está cambiando más rápido que la escuela. Esta infografía del Banco Mundial reúne cinco datos clave sobre los empleos del futuro.

{{IMG}}

## Los 5 datos

1. **600 millones de empleos** deben crearse en el mundo para 2030, según los expertos.
2. **77% de los empleos en China** están amenazados por la automatización, y América Latina también empieza a sentir el impacto.
3. **Los empleos del futuro requieren nuevas habilidades:** menos memorización y más pensamiento crítico.
4. **36% de las empresas en América Latina** dice que es muy difícil encontrar trabajadores capacitados y con la educación adecuada.
5. **Solo 47% de las mujeres participa en la fuerza laboral de Argentina,** frente a 75% de los hombres.

## Lo que pasó después

La inteligencia artificial generativa aceleró el debate: ya no solo se automatizan tareas manuales y repetitivas, también tareas de oficina como redactar, resumir o programar. Por eso pesan cada vez más las habilidades que la tecnología complementa pero no sustituye: pensamiento crítico, comunicación, aprendizaje constante y saber usar estas herramientas.

## Para tu empresa

Invierte en capacitar a tu equipo: es más barato que buscar talento que no existe en el mercado. Lee [cómo será el trabajador del futuro]({S}/infografia-como-sera-el-trabajador-del-futuro/) y [las estrategias de los directivos ante la escasez de talento]({S}/infografia-estrategias-de-los-directivos-para-afrontar-la-escasez-de-talento/).
""",
faq=[
("¿Qué habilidades pedirán los empleos del futuro?", "Pensamiento crítico, resolución de problemas, comunicación, aprendizaje constante y manejo de tecnología."),
("¿La automatización eliminará empleos?", "Transformará muchos: algunas tareas desaparecen y surgen otras, por eso la capacitación es clave."),
("¿Es difícil encontrar talento en América Latina?", "Según el Banco Mundial, el 36% de las empresas de la región dice que es muy difícil encontrar trabajadores capacitados."),
],
related=[("Cómo será el trabajador del futuro", S + "/infografia-como-sera-el-trabajador-del-futuro/"), ("Escasez de talento", S + "/infografia-estrategias-de-los-directivos-para-afrontar-la-escasez-de-talento/")],
),
]
