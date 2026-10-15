from comun import *

POSTS = [
dict(
id=1773, slug="infografia-indicadores-economicos-paises-del-g20",
title="Indicadores económicos de los países del G20 (infografía)",
excerpt="Infografía de indicadores económicos del G20: PIB per cápita, población y PIB total de cada país, con México comparado frente a las mayores economías del mundo.",
img_alt="Infografía de indicadores económicos de los países del G20",
credit="Infografía: Business Insider, con datos de 2016.",
body=f"""
¿Qué tan grande es la economía mexicana comparada con las demás del G20? ¿Y qué tan rico es, en promedio, cada mexicano frente a un alemán o un brasileño?

Esta infografía pone tres indicadores lado a lado para los países del G20, con datos de 2016.

{{IMG}}

## Los tres indicadores

- **PIB per cápita** en paridad de poder adquisitivo (dólares): cuánto produce cada habitante, ajustado por lo que cuesta vivir en cada país.
- **Población** en millones.
- **PIB total** en miles de millones de dólares.

## Lo que destaca

- **Estados Unidos** encabezaba el PIB per cápita (57,467 dólares) y el PIB total (18,569 miles de millones), con 323 millones de habitantes.
- **Arabia Saudita y Alemania** seguían en PIB per cápita (54,431 y 48,730).
- **China** tenía la mayor población (1,380 millones) y el segundo PIB total (11,199 miles de millones), pero un PIB per cápita de 15,535.
- **India** tenía 1,320 millones de habitantes y el PIB per cápita más bajo de la lista (6,572).
- **México** registraba un PIB per cápita de 17,862 dólares, 128 millones de habitantes y un PIB total de 1,046 miles de millones, cerca de Corea del Sur, Rusia e Indonesia en tamaño de economía.

Las cifras han cambiado desde entonces, pero el panorama general se mantiene: economías grandes no siempre significan ingresos altos por persona.

## Por qué le importa a un negocio

- **Tamaño de mercado no es poder de compra.** Un país con mucha población puede tener un ingreso por persona bajo; tu precio y tu oferta deben ajustarse a eso.
- **México es una economía grande,** con un mercado interno amplio y cercano a Estados Unidos, algo clave para exportar o atender clientes internacionales.

Si estás pensando en vender fuera, empieza por definir a tu [buyer persona]({BUYER}) en cada mercado: no compra igual un cliente en Monterrey que uno en Madrid.
""",
faq=[
("¿Qué indicadores muestra la infografía del G20?", "PIB per cápita en paridad de poder adquisitivo, población y PIB total de cada país del G20, con datos de 2016."),
("¿Cuál era el PIB per cápita de México según la infografía?", "Alrededor de 17,862 dólares en paridad de poder adquisitivo, con 128 millones de habitantes y un PIB total de 1,046 miles de millones de dólares."),
("¿Qué diferencia hay entre PIB total y PIB per cápita?", "El PIB total mide el tamaño de toda la economía; el per cápita lo divide entre la población para estimar cuánto produce, en promedio, cada habitante."),
],
related=[("Qué es un buyer persona", BUYER), ("Más infografías", HUB_INFO)],
),

dict(
id=5609, slug="infografia-5-claves-sobre-la-poblacion-mundial-que-debes-dominar",
title="5 claves sobre la población mundial (infografía)",
excerpt="Infografía con 5 claves sobre la población mundial: edades, distribución por continente, países más urbanizados, población joven y grandes ciudades del mundo.",
img_alt="Infografía de 5 claves sobre la población mundial",
body=f"""
Entender cómo está repartida la población del mundo ayuda a entender hacia dónde van los mercados: dónde hay más jóvenes, dónde la gente vive en ciudades y dónde se concentra el consumo.

Esta infografía resume cinco claves.

{{IMG}}

## Las 5 claves

**1. La edad de la población.** A nivel mundial, alrededor del 26% de las personas tiene menos de 15 años y cerca del 9% más de 64. En Europa la brecha es mucho más estrecha: 16% menores de 15 y 18% mayores de 64.

**2. La distribución por continente.** Asia concentra la gran mayoría de la población mundial, seguida de África, Europa, América Latina y el Caribe y América del Norte.

**3. Los países con más población urbana.** China e India encabezan la lista, seguidas de Estados Unidos, Brasil, Indonesia, Japón, Rusia y México, con más de 100 millones de personas viviendo en ciudades.

**4. Los continentes con más población joven.** África destaca con una proporción muy alta de menores de 15 años (alrededor del 41%), muy por encima de otras regiones.

**5. Las ciudades más pobladas.** La infografía cierra con las mayores aglomeraciones urbanas del mundo.

## Lo que significa para los negocios

- **El consumo se urbaniza.** Más gente en ciudades significa más demanda de servicios, comercio en línea y entregas rápidas.
- **Mercados jóvenes y mercados que envejecen** requieren productos y mensajes distintos.
- **México es un mercado urbano grande,** con más de 100 millones de personas en ciudades según la infografía.

Conocer a tu mercado empieza por los datos, pero se vuelve útil cuando lo aterrizas en una persona concreta: tu [buyer persona]({BUYER}).
""",
faq=[
("¿Qué porcentaje de la población mundial es menor de 15 años?", "Según la infografía, alrededor del 26%, mientras que cerca del 9% tiene más de 64 años."),
("¿Qué países tienen más población urbana?", "China e India encabezan la lista, seguidas de Estados Unidos, Brasil, Indonesia, Japón, Rusia y México."),
("¿Qué continente tiene la población más joven?", "África, con alrededor del 41% de su población menor de 15 años según la infografía."),
],
related=[("Indicadores económicos del G20", S + "/infografia-indicadores-economicos-paises-del-g20/"), ("Qué es un buyer persona", BUYER)],
),

dict(
id=1356, slug="infografia-los-mercados-de-valores-mas-caros-del-mundo",
title="Los mercados de valores más caros del mundo",
excerpt="Infografía de los mercados de valores más caros del mundo según la relación CAPE: qué mide este indicador, qué países destacaban y cómo interpretarlo.",
img_alt="Infografía de los mercados de valores más caros del mundo según la relación CAPE",
credit="Infografía: Business Insider, con datos de StarCapital.",
body=f"""
¿Cómo saber si una bolsa de valores está "cara" o "barata"? Una de las formas más usadas es la relación CAPE, y esta infografía la muestra para decenas de mercados del mundo.

{{IMG}}

## Qué es la relación CAPE

La CAPE (también conocida como PER de Shiller, por el economista Robert Shiller) se define como el precio de mercado dividido entre el promedio de las utilidades de los últimos diez años, ajustado por inflación.

Usar diez años suaviza los altibajos de un año bueno o malo. En términos simples: cuanto más alta la CAPE, más pagan los inversionistas por cada peso de utilidades, es decir, más "caro" está el mercado.

## Lo que muestra la infografía

El mapa compara la CAPE estimada de mercados de América, Europa y Asia con datos de StarCapital de esa época. Entre los valores que se leen:

- **Los más caros:** Dinamarca (36.4), Irlanda (33.8), Estados Unidos (28.5) y Japón (26.3).
- **México** marcaba 23.3, por encima de Canadá (20.5), China (16.6) o Hong Kong (17.3).
- **Los más baratos:** Rusia (5), República Checa (9.1) y Brasil (11).
- **En Europa** había mucha variación: de Suiza (24.3) y Bélgica (24) a Turquía (11.8) y Polonia (12.5).

Estos valores cambian constantemente con el precio de las acciones y las utilidades de las empresas.

## Cómo leerlo

- **No es una señal para comprar o vender mañana.** La CAPE funciona mejor como referencia de largo plazo.
- **Un mercado caro puede seguir subiendo,** y uno barato puede seguir barato por buenas razones.
- **Compara con la historia del propio mercado,** no solo con otros países.

Este contenido es informativo y no es una recomendación de inversión. Antes de invertir, consulta a un asesor financiero.
""",
faq=[
("¿Qué es la relación CAPE?", "Es el precio de mercado dividido entre el promedio de las utilidades de los últimos diez años, ajustado por inflación. También se conoce como PER de Shiller."),
("¿Qué significa una CAPE alta?", "Que los inversionistas pagan mucho por cada peso de utilidades, lo que suele interpretarse como un mercado caro en términos históricos."),
("¿Sirve la CAPE para saber cuándo invertir?", "Es una referencia de largo plazo, no una señal de corto plazo. Conviene usarla junto con otros indicadores y con asesoría profesional."),
],
related=[("Indicadores económicos del G20", S + "/infografia-indicadores-economicos-paises-del-g20/"), ("Más infografías", HUB_INFO)],
),

dict(
id=2063, slug="infografia-guia-para-mejorar-tus-reuniones-uno-a-uno",
title="Reuniones uno a uno: guía para mejorarlas (infografía)",
excerpt="Infografía con una guía para mejorar tus reuniones uno a uno: frecuencia, preguntas clave, agenda de 60 minutos y consejos para escuchar más a tu equipo.",
img_alt="Infografía de guía para mejorar tus reuniones uno a uno",
credit="Infografía: INVEX Banco, con base en una guía de Officevibe.",
body=f"""
Muchos líderes creen que hablan con su equipo todos los días. Pero hablar de pendientes no es lo mismo que hablar con la persona.

Para eso existen las reuniones uno a uno. Esta infografía explica cómo sacarles provecho.

{{IMG}}

## Qué es una reunión uno a uno

Es exactamente lo que su nombre dice: el líder se reúne con un colaborador para tener una plática privada sobre cualquier inquietud.

## Claves

- Una sesión al mes, de una hora, con cada miembro del equipo.
- Prepara preguntas clave: "¿Qué te inquieta?", "¿Cómo te sientes con tu trabajo?".
- Toma nota siempre.
- Habla poco, escucha más.
- No es una reunión de estatus. No la trates como tal.

## Agenda sugerida de 60 minutos

| Tiempo | Para qué |
| --- | --- |
| 10 minutos | Ponerse al día |
| 20 minutos | Escuchar a tu colaborador |
| 20 minutos | Discutir las notas que tomaste |
| 10 minutos | Proponer un plan de acción |

## Consejos

- Recuerda que la reunión es para tu equipo, no para ti.
- Pide retroalimentación sobre tu propio liderazgo.
- Pide a tu colaborador una lista de temas 24 horas antes.
- Escribe todo lo que te comente.

## Por qué vale la pena

Muchas renuncias se pueden ver venir… si alguien pregunta a tiempo. Una buena uno a uno detecta frustraciones, ideas y señales de desgaste antes de que se conviertan en problemas. Revisa también [qué hacer ante la salida de un empleado clave]({S}/que-hacer-ante-la-salida-de-un-empleado-clave/) y las [características de un buen líder]({LIDER}).
""",
faq=[
("¿Qué es una reunión uno a uno?", "Es una conversación privada y periódica entre un líder y un colaborador para hablar de sus inquietudes, su desarrollo y su trabajo, no del estatus de los proyectos."),
("¿Cada cuánto hacer reuniones uno a uno?", "La infografía recomienda una sesión al mes de una hora con cada miembro del equipo; muchos equipos las hacen cada dos semanas en formatos más cortos."),
("¿Qué preguntar en una reunión uno a uno?", "Qué le inquieta, cómo se siente con su trabajo, qué obstáculos tiene, qué le gustaría aprender y qué podrías hacer mejor como líder."),
],
related=[("Las 13 características de un buen líder", LIDER), ("Liderazgo situacional", S + "/infografia-liderazgo-situacional/")],
),

dict(
id=1565, slug="infografia-a-que-personaje-publico-les-gustaria-parecerse-a-los-jovenes-espanoles-de-mayor",
title="¿A quién quieren parecerse los jóvenes? (infografía)",
excerpt="Infografía: a qué personaje público les gustaría parecerse a los jóvenes españoles de 16 a 19 años. Empresarios, científicos, deportistas y sus propios padres.",
img_alt="Infografía de a qué personaje público les gustaría parecerse a los jóvenes españoles",
credit="Infografía: Kiko Llaneras para El País, con datos de Educa 20.20 y GAD3.",
body=f"""
Cuando les preguntaron a jóvenes españoles de 16 a 19 años a qué personaje público les gustaría parecerse de mayores, las respuestas sorprendieron: en lo alto de la lista aparecieron empresarios, científicos y… sus propios padres.

{{IMG}}

## Lo que respondieron

**Chicas.** Entre los nombres más mencionados estuvieron Amancio Ortega (fundador de Inditex), su madre, Emma Watson, Steve Jobs, su padre, algún profesor o profesora, Marie Curie, Michelle Obama, Barack Obama, Bill Gates y la influencer Dulceida.

**Chicos.** Entre los más mencionados estuvieron Bill Gates, Steve Jobs, Amancio Ortega, su padre, Elon Musk, Cristiano Ronaldo, Donald Trump, Rafael Nadal, Albert Einstein, Leo Messi y algún profesor.

Los datos provienen de un estudio de Educa 20.20 y GAD3, publicado por El País.

## Lo que llama la atención

- **Los emprendedores son referentes.** Gates, Jobs, Ortega y Musk aparecen en ambas listas o muy arriba.
- **La familia pesa.** Mamá, papá y los maestros compiten con celebridades.
- **Los influencers no dominan,** aunque aparecen.

## Lo que aprende una marca

Si tu cliente es joven, la autenticidad y el mérito pesan. Las historias de esfuerzo, de construir algo desde cero, conectan más que la fama por sí sola. Y los referentes cercanos (familia, maestros) influyen tanto como las figuras públicas.

Si emprendes, tu historia también puede inspirar. Revisa las [características de un emprendedor exitoso]({EMPRENDEDOR}).
""",
faq=[
("¿A quién quieren parecerse los jóvenes españoles según la encuesta?", "Entre los más mencionados están Bill Gates, Steve Jobs y Amancio Ortega, además de sus propios padres, profesores, científicos como Marie Curie y Albert Einstein y deportistas como Rafael Nadal."),
("¿De dónde vienen los datos?", "De un estudio de Educa 20.20 y GAD3 con jóvenes de 16 a 19 años, publicado por El País."),
("¿Qué indica la encuesta sobre los referentes juveniles?", "Que los emprendedores y la familia pesan tanto o más que las celebridades y los influencers."),
],
related=[("Características de un emprendedor exitoso", EMPRENDEDOR), ("Más infografías", HUB_INFO)],
),

dict(
id=1871, slug="infografia-que-paises-tiene-las-mayores-reservas-de-litio",
title="Países con las mayores reservas de litio (infografía)",
excerpt="Infografía de los países con mayores reservas de litio: el triángulo de Argentina, Bolivia y Chile, la producción de Australia y por qué el litio es clave.",
img_alt="Infografía de los países con las mayores reservas de litio",
credit="Infografía: Business Insider, con datos del Servicio Geológico de Estados Unidos, Roskill, Comibol, Banco Mundial y Transparencia Internacional.",
body=f"""
El litio está en la batería de tu celular, tu laptop y cada vez más autos eléctricos. Por eso se le ha llamado "el petróleo blanco".

Esta infografía, con datos de enero de 2017, muestra dónde están las mayores reservas y quién las aprovecha.

{{IMG}}

## Lo que muestra la infografía

**Argentina, Bolivia y Chile tienen más de la mitad de las reservas mundiales de litio,** en la región conocida como el triángulo del litio.

Pero, según la infografía, estos países no habían sabido aprovechar la oportunidad. Para explicarlo, compara a los países productores en cuatro indicadores:

- Producción de litio en 2016 (en equivalente de carbonato de litio).
- Inversión extranjera directa como porcentaje del PIB.
- Lugar en el ranking de facilidad para hacer negocios del Banco Mundial.
- Índice de Percepción de la Corrupción de Transparencia Internacional.

Australia, con reservas menores, aparecía como gran productor gracias a un entorno más favorable para la inversión. Bolivia, con enormes reservas, apenas registraba ventas.

## Lo que pasó después

La demanda de litio creció con fuerza por los autos eléctricos y el almacenamiento de energía. México también entró a la conversación: en 2022 declaró el litio de utilidad pública y creó una empresa estatal para su explotación.

## La lección de negocio

Tener el recurso no basta. Lo que convierte una ventaja natural en riqueza son las reglas claras, la inversión y la capacidad de ejecutar. Aplica igual a una empresa: tener el mejor producto no sirve si nadie lo conoce o si no puedes entregarlo.
""",
faq=[
("¿Qué países tienen las mayores reservas de litio?", "Argentina, Bolivia y Chile, el llamado triángulo del litio, concentran más de la mitad de las reservas mundiales según la infografía."),
("¿Por qué Australia produce tanto litio?", "Porque, aunque tiene menos reservas, ofrecía un entorno más favorable para la inversión y para hacer negocios."),
("¿Para qué se usa el litio?", "Principalmente en baterías de celulares, computadoras, autos eléctricos y sistemas de almacenamiento de energía."),
],
related=[("Tecnologías de energía solar", S + "/infografia-tecnologias-de-energia-solar/"), ("Más infografías", HUB_INFO)],
),

dict(
id=1346, slug="infografia-accesibilidad-web",
title="Accesibilidad web: los 4 principios (infografía)",
excerpt="Infografía de accesibilidad web: los cuatro principios (perceptible, operable, comprensible y robusto) explicados con ejemplos para que tu sitio lo use todo el mundo.",
img_alt="Infografía de accesibilidad web con los principios perceptible, operable, comprensible y robusto",
credit="Infografía: AENOR. Ilustración de J.C. Esteban y R. Quirosa.",
body=f"""
Si tu sitio web no se puede usar sin mouse, si tus imágenes no tienen texto alternativo o si tus enlaces solo se distinguen por el color, hay personas que no pueden comprarte. Y también es probable que Google te entienda peor.

Esta infografía de AENOR explica los cuatro principios de la accesibilidad web.

{{IMG}}

## Por qué importa

La infografía recuerda que el 17 de mayo es el Día Mundial de Internet, una fecha para impulsar el acceso de todos a la sociedad de la información. Normas como la UNE 139803 (en España) establecen las características que deben cumplir los contenidos web para que los use el mayor número de personas posible. Hoy la referencia internacional son las pautas WCAG del W3C.

## Los 4 principios

**Perceptible**
- El contenido debe estar disponible para los sentidos (vista, oído, tacto).
- Las fotografías que transmiten información deben tener una descripción textual alternativa.
- Los enlaces deben distinguirse visualmente, no solo por el color, con textos breves y significativos.

**Operable**
- Formularios, controles y navegación deben permitir la interacción.
- Toda la funcionalidad debe poder usarse con el teclado.
- Los usuarios deben tener tiempo suficiente para leer y usar el contenido.
- No deben usarse contenidos que destellen más de tres veces por segundo, porque pueden provocar convulsiones.

**Comprensible**
- El contenido y la interfaz deben entenderse fácilmente.
- Debe indicarse el idioma de la página y de los textos cuando cambie.
- Los formularios deben indicar qué campos son obligatorios.

**Robusto**
- El contenido debe ser lo bastante consistente para funcionar con distintos navegadores, ayudas técnicas y tecnologías futuras.

## Revisión rápida para tu sitio

1. ¿Todas tus imágenes informativas tienen texto alternativo?
2. ¿Puedes recorrer tu sitio y enviar tu formulario solo con el teclado?
3. ¿El contraste entre texto y fondo es suficiente?
4. ¿Tus enlaces dicen a dónde llevan, en lugar de "clic aquí"?

Un sitio accesible convierte más y se posiciona mejor. Revisa también estos [KPIs para tu sitio web]({KPIS}).
""",
faq=[
("¿Cuáles son los principios de la accesibilidad web?", "Perceptible, operable, comprensible y robusto."),
("¿Qué es el texto alternativo de una imagen?", "Es una descripción textual que leen los lectores de pantalla y que se muestra si la imagen no carga. Es clave para la accesibilidad y también ayuda al SEO."),
("¿Qué normas regulan la accesibilidad web?", "La referencia internacional son las pautas WCAG del W3C; en España, la infografía menciona la norma UNE 139803."),
],
related=[("KPIs para tu sitio web", KPIS), ("Herramientas de Google para tu web", S + "/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/")],
),

dict(
id=2023, slug="infografia-el-bitcoin-no-es-la-unica-criptomoneda",
title="Bitcoin no es la única criptomoneda (infografía)",
excerpt="Infografía: el bitcoin no es la única criptomoneda. Ethereum, Ripple, Litecoin, Dash, Monero y otras, su origen y capitalización en 2017, con contexto actual.",
img_alt="Infografía: el bitcoin no es la única criptomoneda",
credit="Infografía: Business Insider, con datos de CoinDesk y CoinMarketCap.",
body=f"""
Cuando se habla de criptomonedas, casi todos piensan en bitcoin. Pero ya en 2017 existían cientos de alternativas.

Esta infografía muestra las principales, su año de origen y su capitalización de mercado en 2017.

{{IMG}}

## Lo que muestra la infografía

- **Bitcoin (2009)** era la moneda más grande por capitalización de mercado.
- **Otras criptomonedas** como Litecoin y Dogecoin se basan en el mismo código fuente.
- **Ethereum (2015)** y **Ripple** eran las alternativas más grandes, con capitalizaciones de varios miles de millones de dólares.
- **Aparecen también** Ethereum Classic, Dash, Monero, Bytecoin, NEM, Stellar Lumens y más de 800 monedas alternativas.
- **El precio venía creciendo:** todas las principales criptomonedas registraron ganancias en 2016, y su capitalización total ya podía compararse con la de grandes empresas estadounidenses.

## Qué pasó después

El mercado cripto vivió subidas y caídas extremas. Muchas monedas desaparecieron; bitcoin y ethereum se consolidaron como las más grandes, y surgieron las *stablecoins*, ligadas al valor de monedas como el dólar.

## Lo que conviene saber

- **Son activos muy volátiles.** Su precio puede subir o caer con fuerza en días.
- **No todas son iguales.** Algunas son plataformas para aplicaciones (como Ethereum), otras buscan pagos rápidos, otras privacidad.
- **Cuidado con las estafas:** promesas de rendimientos garantizados son una señal de alerta.

Este contenido es informativo y no es una recomendación de inversión. Antes de invertir, consulta a un asesor financiero.
""",
faq=[
("¿Qué otras criptomonedas existen además de bitcoin?", "Entre las que muestra la infografía están Ethereum, Ripple, Litecoin, Dogecoin, Dash, Monero, NEM, Stellar Lumens y Ethereum Classic, además de cientos de monedas alternativas."),
("¿Cuándo se creó bitcoin?", "En 2009. Es la primera criptomoneda y la más grande por capitalización de mercado."),
("¿Es seguro invertir en criptomonedas?", "Son activos muy volátiles y con riesgo de fraudes. Conviene informarse bien, desconfiar de rendimientos garantizados y consultar a un asesor."),
],
related=[("5 tendencias tecnológicas", S + "/infografia-5-tendencias-tecnologicas-que-cambiaran-el-mundo/"), ("Más infografías", HUB_INFO)],
),

dict(
id=2169, slug="infografia-los-gigantes-tecnologicos-de-estados-unidos-siguen-creciendo",
title="Los gigantes tecnológicos siguen creciendo (infografía)",
excerpt="Infografía del crecimiento de los gigantes tecnológicos de Estados Unidos: capitalización de Apple, Alphabet, Microsoft, Amazon y Facebook desde 2006.",
img_alt="Infografía del crecimiento de los gigantes tecnológicos de Estados Unidos",
credit="Infografía: Business Insider, con datos de Yahoo! Finance.",
body=f"""
En una década, un puñado de empresas tecnológicas se volvió más valioso que economías enteras. Esta infografía muestra cómo creció su capitalización de mercado desde 2006.

{{IMG}}

## Lo que muestra la infografía

La gráfica sigue la capitalización de mercado (en miles de millones de dólares) de las grandes tecnológicas y de internet de Estados Unidos, entre ellas **Apple, Google/Alphabet, Microsoft y Facebook**.

La tendencia es clara: crecimiento sostenido, con Apple a la cabeza en el periodo que cubre la infografía (hasta 2017), cuando varias de estas empresas ya superaban los 500 mil millones de dólares.

## Lo que pasó después

El crecimiento continuó. Apple, Microsoft y otras superaron el billón de dólares de valor, y nuevas empresas, como las de chips para inteligencia artificial, se sumaron al grupo de las más valiosas del mundo. Facebook cambió su nombre corporativo a Meta en 2021.

## Lo que significa para tu negocio

Estas empresas controlan buena parte de los canales por los que llegas a tus clientes: búsqueda, redes sociales, tiendas de aplicaciones y publicidad. Eso tiene dos lecturas:

1. **Aprovecha sus herramientas,** muchas gratuitas, para atraer clientes.
2. **No dependas solo de ellas.** Un cambio de algoritmo puede reducir tu alcance de un día para otro. Construye activos propios: tu sitio web, tu lista de correo y tu base de clientes.

Eso es justo lo que propone el [inbound marketing]({GUIA}): tener canales propios que nadie te puede quitar.
""",
faq=[
("¿Qué empresas tecnológicas muestra la infografía?", "Las grandes tecnológicas y de internet de Estados Unidos, entre ellas Apple, Google/Alphabet, Microsoft y Facebook (hoy Meta)."),
("¿Qué es la capitalización de mercado?", "Es el valor total de una empresa en bolsa: el precio de su acción multiplicado por el número de acciones en circulación."),
("¿Por qué no depender solo de las grandes plataformas?", "Porque un cambio en sus algoritmos o reglas puede reducir tu alcance de golpe. Conviene construir canales propios como tu sitio web y tu lista de correo."),
],
related=[("Qué es el inbound marketing", GUIA), ("Apple: ventas y valor de marca", S + "/infografia-conoce-apple-ventas-ingresos-y-valor-de-marca-actual/")],
),

dict(
id=2095, slug="infografia-por-que-wordpress-es-el-cms-mas-usado-del-mundo",
title="Por qué WordPress es el CMS más usado (infografía)",
excerpt="Infografía de por qué WordPress es el CMS más usado del mundo: cuota de mercado, plugins, idiomas y comunidad, con datos actualizados y cuándo conviene usarlo.",
img_alt="Infografía de por qué WordPress es el CMS más usado del mundo",
credit="Infografía: miguelvalero.com.",
body=f"""
Si alguna vez te preguntaste en qué está hecho un sitio web, hay muchas probabilidades de que la respuesta sea WordPress.

Esta infografía explica por qué se volvió el gestor de contenidos (CMS) más usado del mundo.

{{IMG}}

## Lo que dice la infografía

Con datos de esa época:

- Más del 60% de los sitios hechos con un CMS usaban WordPress.
- El 24% de todos los sitios web estaban creados con WordPress.
- Unos 76 millones de sitios en el mundo lo usaban.
- Una buena parte de los nuevos dominios registrados en Estados Unidos lo utilizaba.
- Había más de 30,000 plugins disponibles.
- Estaba traducido a 51 idiomas.

## Cómo está hoy

WordPress siguió creciendo: hoy impulsa alrededor de 4 de cada 10 sitios web del mundo, tiene decenas de miles de plugins gratuitos y está disponible en más de 200 idiomas y variantes.

## Por qué tanta gente lo elige

- **Es de código abierto y gratuito.** Pagas hosting, dominio y, si quieres, temas o plugins premium.
- **Es flexible:** sirve para un blog, un sitio corporativo o una tienda con WooCommerce.
- **Tiene una comunidad enorme:** casi cualquier problema ya lo resolvió alguien.
- **Es amigable con el SEO,** sobre todo con plugins como Yoast.

## Cuándo pensarlo dos veces

Requiere mantenimiento: actualizaciones, seguridad y respaldos. Si no quieres ocuparte de nada técnico, una plataforma administrada puede convenirte más. Compara opciones en [HubSpot CMS vs. WordPress]({S}/hubspot-cos-vs-wordpress-cms/).
""",
faq=[
("¿Por qué WordPress es el CMS más usado?", "Porque es gratuito y de código abierto, muy flexible, tiene miles de plugins y temas, una comunidad enorme y buenas herramientas para SEO."),
("¿Qué porcentaje de sitios web usa WordPress?", "La infografía hablaba de 24% en su momento; hoy WordPress impulsa alrededor de 4 de cada 10 sitios web del mundo."),
("¿WordPress es gratis?", "El software es gratuito, pero necesitas pagar hosting y dominio, y opcionalmente temas o plugins premium."),
],
related=[("HubSpot CMS vs. WordPress", S + "/hubspot-cos-vs-wordpress-cms/"), ("Accesibilidad web", S + "/infografia-accesibilidad-web/")],
),
]
