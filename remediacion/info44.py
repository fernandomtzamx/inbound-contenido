from comun import *

POSTS = [
dict(
id=1663, slug="infografia-ramsonware-lo-que-debes-saber",
title="Ransomware: lo que debes saber (infografía)",
excerpt="Infografía de Wellness Telecom sobre el ransomware: qué es, cómo se propaga, sus tipos (cifrado, bloqueo de pantalla y dispositivos) y cómo protegerse en una empresa.",
img_alt="Infografía de ransomware: qué es, cómo se propaga y cómo protegerse",
credit="Infografía: Wellness Telecom.",
body=f"""
El ransomware es uno de los ataques que más daño hace a empresas de cualquier tamaño. Esta infografía de Wellness Telecom explica lo esencial.

{{IMG}}

## Qué es

Un software que restringe el acceso a tus archivos, aplicaciones o sistema, secuestra tus datos y pide un rescate para liberarlos.

## Cómo se propaga

Por correo electrónico, almacenamiento externo (memorias USB, discos), aplicaciones y la red.

## Tipos de ransomware

- **De cifrado de datos:** cifra tus archivos.
- **De bloqueo de pantalla:** impide usar el equipo.
- **De dispositivos:** ataca celulares y otros equipos.

## Cómo protegerse

- **Educa al personal** para prevenir y actuar ante posibles infecciones.
- **Haz copias de seguridad** con una política adecuada.
- **Actualiza el software de seguridad** (antivirus).
- **No abras ni ejecutes archivos sospechosos.**
- **Descarga aplicaciones solo de sitios seguros.**
- **Cambia las contraseñas** con frecuencia.

## Lo que agregaríamos hoy

- **Verificación en dos pasos** en correo, nube y accesos remotos.
- **Respaldos desconectados** o que no se puedan modificar, porque el ransomware moderno busca y cifra también los respaldos.
- **Un plan de respuesta:** a quién llamar, cómo aislar equipos y cómo restaurar.

Lee [cómo proteger tu información del ransomware]({S}/infografia-protege-tu-informacion-del-ransomware/) y [111 consejos de ciberseguridad]({S}/infografia-111-consejos-para-elevar-la-ciberseguridad-de-tu-empresa/).
""",
faq=[
("¿Qué es el ransomware?", "Un software malicioso que bloquea o cifra tus datos y exige un rescate para devolverlos."),
("¿Cómo entra el ransomware a una empresa?", "Sobre todo por correos con archivos o enlaces maliciosos, memorias externas, aplicaciones no confiables y accesos remotos mal protegidos."),
("¿Cuál es la mejor defensa contra el ransomware?", "Respaldos frecuentes y desconectados, actualizaciones al día, verificación en dos pasos y capacitación del personal."),
],
related=[("Cómo proteger tu información del ransomware", S + "/infografia-protege-tu-informacion-del-ransomware/"), ("111 consejos de ciberseguridad", S + "/infografia-111-consejos-para-elevar-la-ciberseguridad-de-tu-empresa/")],
),

dict(
id=1493, slug="infografia-ad-verification-para-publicidad-programatica",
title="Ad verification en publicidad programática",
excerpt="Infografía de Tradelab y Adloox sobre la verificación de anuncios en programática: antifraude, visibilidad y seguridad de marca, cómo funciona y resultados como 10% de tráfico inválido sin herramienta.",
img_alt="Infografía de ad verification para publicidad programática",
credit="Infografía: Tradelab y Adloox.",
body=f"""
En publicidad programática, no todo lo que se cobra lo ve una persona real ni aparece en un lugar adecuado. La verificación de anuncios (ad verification) existe para eso. Esta infografía explica cómo funciona.

{{IMG}}

## Para qué sirve

Proteger la inversión publicitaria y la imagen de la marca, asegurar una difusión de calidad y optimizar la eficiencia de los medios.

## Cómo opera

- **Antifraude:** listas blancas y negras de sitios.
- **Visibilidad (viewability):** criterios de visibilidad personalizados en todos los formatos.
- **Seguridad de marca (brand safety):** bloqueo de grupos de palabras clave inadecuadas.

**El filtro antifraude** trabaja con un doble enfoque durante las pujas: por usuario (seguimiento del tráfico inválido, como bots) y por oferta (detección de tráfico dañado a nivel del medio).

## Cómo funciona

Los medios ofrecen sus espacios; la solución de verificación se integra en la plataforma de compra; se excluyen sitios, usuarios y ubicaciones no calificados; se evalúa cada oportunidad y se puja solo por las que valen la pena.

## Los resultados que reporta

- Sin herramienta, en promedio el **10%** del tráfico es inválido; con la solución, **0.8%.**
- **60%** de reducción del CPM al abrir la difusión a sitios de nicho con inventario limpio.
- **70%** de visibilidad media.
- **44%** de reducción del costo por clic.

Son cifras del propio proveedor, promedio de más de 100 campañas.

## Para tu marca

Si inviertes en display o video programático, pregunta a tu agencia o plataforma qué verificación usan, qué porcentaje de tráfico inválido detectan y en qué sitios aparecen tus anuncios. Lee [8 razones para elegir la publicidad programática]({S}/infografia-8-razones-para-elegir-programatica/) y [tendencias en publicidad digital]({S}/infografia-tendencias-en-publicidad-digital/).
""",
faq=[
("¿Qué es ad verification?", "El conjunto de herramientas que verifica que los anuncios se muestren a personas reales, en lugares adecuados y con visibilidad suficiente."),
("¿Qué es el tráfico inválido en publicidad?", "Impresiones o clics generados por bots o actividad fraudulenta, que no corresponden a personas reales."),
("¿Qué es brand safety?", "Las medidas para evitar que los anuncios de una marca aparezcan junto a contenido inapropiado o dañino."),
],
related=[("8 razones para elegir la publicidad programática", S + "/infografia-8-razones-para-elegir-programatica/"), ("Tendencias en publicidad digital", S + "/infografia-tendencias-en-publicidad-digital/")],
),

dict(
id=2143, slug="infografia-cuantos-anuncios-retira-google-al-ano",
title="Cuántos anuncios retira Google al año (infografía)",
excerpt="Infografía con los anuncios que Google retiró en 2016: 1,700 millones por infringir sus políticas, 112 millones por inducir a descargar software dañino y 80 millones por engañar con productos milagro.",
img_alt="Infografía de cuántos anuncios retira Google al año",
credit="Infografía: Vodafone (Ideas para tu empresa), con datos del informe anual de Google sobre malos anuncios de 2016.",
body=f"""
No todo anuncio que se publica en Google llega a verse. Esta infografía resume cuántos retiró Google en 2016, según su informe anual sobre anuncios maliciosos.

{{IMG}}

## Los anuncios retirados en 2016

- **1,700 millones** por infringir las políticas de Google.
- **112 millones** por inducir a descargar software dañino.
- **80 millones** por engañar con productos como dietas milagro.
- **68 millones** por infringir normas sanitarias.
- **17 millones** por anunciar apuestas ilegales.

## Lo que pasó después

Las cifras crecieron: en años recientes, Google ha reportado que bloquea o retira más de 5,000 millones de anuncios al año y suspende millones de cuentas de anunciantes, con ayuda de inteligencia artificial.

## Lo que significa para tu negocio

- **Conoce las políticas** antes de anunciarte, sobre todo si estás en salud, finanzas, alcohol o apuestas.
- **Cuida tu página de destino:** muchas veces lo que se rechaza no es el anuncio, sino el sitio al que lleva.
- **No prometas lo imposible.** Además de que Google lo retira, destruye la confianza.

Lee [ingresos de Google vs. gasto publicitario por país]({S}/infografia-ingresos-de-google-por-publicidad-vs-gasto-publicitario-principales-paises/) y cómo funciona una [campaña en buscadores]({BUSCADORES}).
""",
faq=[
("¿Cuántos anuncios retiró Google en 2016?", "Unos 1,700 millones por infringir sus políticas, según su informe anual."),
("¿Por qué Google retira anuncios?", "Por engañar a los usuarios, promover software dañino, infringir normas sanitarias, anunciar apuestas ilegales u otras violaciones de sus políticas."),
("¿Cómo evitar que Google rechace mis anuncios?", "Conociendo sus políticas, evitando promesas exageradas y cuidando que la página de destino sea clara y confiable."),
],
related=[("Ingresos de Google vs. gasto publicitario", S + "/infografia-ingresos-de-google-por-publicidad-vs-gasto-publicitario-principales-paises/"), ("Campaña en buscadores", BUSCADORES)],
),

dict(
id=2039, slug="infografia-usuarios-de-tecnologias-de-la-informacion-en-mexico",
title="Usuarios de internet y tecnología en México (2016)",
excerpt="Infografía con datos de la ENDUTIH 2016 del INEGI: 65.5 millones de usuarios de internet en México (59.5%), uso por edad y escolaridad, actividades en línea, celulares y estados más conectados.",
img_alt="Infografía de usuarios de tecnologías de la información en México",
credit="Infografía con datos de la ENDUTIH 2016 del INEGI.",
body=f"""
¿Cuántos mexicanos usaban internet en 2016 y para qué? Esta infografía resume la Encuesta Nacional sobre Disponibilidad y Uso de Tecnologías de la Información en los Hogares (ENDUTIH) del INEGI.

{{IMG}}

## Los datos (2016)

- **65.5 millones** de personas de 6 años o más usaban internet: el **59.5%** de esa población.
- **Por edad:** el uso cae conforme aumenta la edad. Lo usaba el 60.3% de las personas de 35 a 44 años, el 45.5% de las de 45 a 54 y solo el 21.6% de los mayores de 54.
- **Por escolaridad:** nueve de cada diez personas con estudios superiores lo usaban, cuatro de cada cinco con nivel medio superior y menos de la mitad con educación básica.
- **Frecuencia:** el 96% de los usuarios navegaba al menos una vez a la semana.
- **Actividades principales:** comunicarse, buscar información y consumir contenidos audiovisuales; crecía la interacción con el gobierno.
- **Celular:** unos 81 millones de usuarios, el 73.6% de la población de 6 años o más.
- **Hogares:** el 45.6% tenía computadora, el 52.1% televisión de paga y el 47% conexión a internet.
- **Por estado:** Baja California Sur, Sonora y Baja California tenían la mayor disponibilidad de internet; Tlaxcala, Oaxaca y Chiapas, la menor.

## Lo que pasó después

En la ENDUTIH más reciente, los usuarios de internet superan el 80% de la población de 6 años o más, casi siempre desde el celular. La brecha entre estados y entre edades se redujo, pero sigue existiendo.

## Para tu negocio

Tu cliente probablemente está en línea y en el celular, pero no asumas que todos lo están igual: revisa la edad, la región y la escolaridad de tu público antes de decidir canales. Lee [México: el consumidor conectado]({S}/infografia-mexico-el-consumidor-conectado/) y [cómo compran los mexicanos en línea]({S}/infografia-asi-compran-los-mexicanos-en-linea/).
""",
faq=[
("¿Cuántos mexicanos usaban internet en 2016?", "65.5 millones de personas de 6 años o más, el 59.5% de esa población, según la ENDUTIH 2016 del INEGI."),
("¿Qué estados tenían más acceso a internet?", "Baja California Sur, Sonora y Baja California; los de menor acceso eran Tlaxcala, Oaxaca y Chiapas."),
("¿Cuántos mexicanos usan internet hoy?", "Las encuestas más recientes del INEGI reportan más del 80% de la población de 6 años o más."),
],
related=[("México: el consumidor conectado", S + "/infografia-mexico-el-consumidor-conectado/"), ("Así compran los mexicanos en línea", S + "/infografia-asi-compran-los-mexicanos-en-linea/")],
),

dict(
id=2221, slug="infografia-plan-de-inbound-marketing",
title="Plan de inbound marketing paso a paso (infografía)",
excerpt="Infografía con el plan de inbound marketing paso a paso: objetivos SMART, buyer persona, oferta de valor, calendario editorial, blog, landing pages, llamados a la acción, email marketing y análisis.",
img_alt="Infografía del plan de inbound marketing paso a paso",
credit="Infografía con base en la metodología de HubSpot.",
body=f"""
El inbound marketing funciona cuando sigue un plan, no cuando se publica por publicar. Esta infografía lo ordena en ocho pasos más el análisis.

{{IMG}}

## Los pasos

1. **Define objetivos SMART:** específicos, medibles, alcanzables, relevantes y con tiempo definido.
2. **Crea tu buyer persona:** sus iniciativas, criterios de decisión, barreras y proceso de compra.
3. **Crea una oferta de valor** para cada etapa del recorrido del comprador. Contenido más contexto.
4. **Crea un calendario editorial.**
5. **Actualiza tu blog** con frecuencia y usa palabras clave de cola larga, que traen menos tráfico pero convierten más.
6. **Crea una landing page** para cada oferta: sin menú que distraiga, con al menos dos párrafos que expliquen su valor, listas para lo más importante y formularios cortos (menos de cinco campos), y una página de agradecimiento.
7. **Diseña llamados a la acción** claros: que el botón diga el beneficio, por ejemplo "Descargar mi ebook de...".
8. **Usa el email marketing** para nutrir a tus contactos.

**Analiza y mejora:** de dónde vienen tus visitas, por qué landing llegaron, qué canal funciona mejor, qué contenido recibieron y qué palabra clave usaron.

La infografía cierra recomendando una herramienta que integre todo: blog, páginas de destino, correo, automatización, CRM, SEO, redes sociales y analítica.

## Cómo empezar sin abrumarte

No necesitas todo el primer mes. Un buen orden es: buyer persona, una oferta útil, su landing page, un correo de seguimiento y medición. Después agregas contenido y automatización.

Profundiza en [qué es el inbound marketing]({GUIA}), [las 4 fases]({FASES}) y [cómo crear campañas de inbound marketing]({S}/infografia-como-crear-campanas-de-inbound-marketing/).
""",
faq=[
("¿Qué incluye un plan de inbound marketing?", "Objetivos, buyer persona, ofertas de valor, calendario editorial, blog, landing pages, llamados a la acción, email marketing y análisis de resultados."),
("¿Qué son los objetivos SMART?", "Objetivos específicos, medibles, alcanzables, relevantes y con un plazo definido."),
("¿Qué debe tener una buena landing page?", "Un solo objetivo, sin menú que distraiga, texto claro sobre el valor de la oferta, un formulario corto y un botón que diga el beneficio."),
],
related=[("Qué es el inbound marketing", GUIA), ("Cómo crear campañas de inbound marketing", S + "/infografia-como-crear-campanas-de-inbound-marketing/")],
),

dict(
id=2367, slug="infografia-guia-practica-para-elegir-medio-para-campana-publicitaria",
title="Cómo elegir el medio para tu campaña publicitaria",
excerpt="Infografía con una guía práctica para elegir medio publicitario: cómo funcionan, por qué son útiles y cuándo convienen Google Ads, Facebook, Twitter, Instagram y los directorios en línea.",
img_alt="Infografía guía práctica para saber en qué medio hacer una campaña publicitaria",
credit="Infografía: Publicar.",
body=f"""
¿Tienes que hacer una campaña y no sabes en qué medio? Esta guía compara las plataformas más usadas: cómo funcionan, cuándo convienen y cuál es la clave del éxito en cada una.

{{IMG}}

## Las plataformas

**Google Ads (antes AdWords)**
- **Cómo funciona:** tu anuncio aparece según las palabras clave en resultados de búsqueda, blogs y videos de YouTube.
- **Cuándo conviene:** si quieres aprovechar las búsquedas de clientes que ya buscan lo que vendes, sobre todo si tu marca aún no es conocida.
- **La clave:** elegir bien las palabras clave y controlar el presupuesto para no pagar de más en la subasta.

**Facebook**
- **Cómo funciona:** anuncios en el feed y otros espacios, segmentados por edad, sexo, ubicación, intereses y comportamientos.
- **Cuándo conviene:** si tu público es activo ahí y quieres generar interacción y conversación sobre tu marca.
- **La clave:** elegir bien el objetivo del anuncio (interacción, "me gusta", tráfico o conversiones).

**Twitter (hoy X)**
- **La clave:** aprovechar la inmediatez y espontaneidad de la red para crear un vínculo más cercano.

**Instagram**
- **Cómo funciona:** anuncios como publicaciones, administrados desde Facebook.
- **Cuándo conviene:** para productos muy visuales, público joven o estrategias en el celular.

**Directorios en línea y guías comerciales**
- **Cómo funciona:** presencia en versión impresa, portal web o ambos.
- **Por qué son útiles:** llegan a compradores que ya decidieron comprar y buscan algo concreto.

## Lo que cambió

Facebook e Instagram se gestionan juntos en Meta Ads, TikTok se sumó como opción relevante para públicos jóvenes, y los directorios impresos perdieron peso frente a Google Maps y las reseñas. La regla de fondo sigue: **elige el medio según dónde está tu cliente y en qué momento de la compra está.** Quien ya busca, está en Google; quien todavía no sabe que te necesita, está en redes.

Lee [consejos de publicidad en redes sociales]({S}/infografia-consejos-sobre-publicidad-en-las-redes-sociales/) y cómo funciona una [campaña en buscadores]({BUSCADORES}).
""",
faq=[
("¿Qué es mejor, Google Ads o Facebook Ads?", "Depende: Google Ads capta a quien ya busca tu producto; Facebook e Instagram sirven para llegar a públicos por intereses y generar demanda."),
("¿Cuándo conviene anunciarse en Instagram?", "Cuando vendes productos muy visuales o tu público es joven y usa mucho el celular."),
("¿Cómo elegir el medio publicitario?", "Según dónde está tu cliente, en qué etapa de compra se encuentra, tu presupuesto y lo que quieres lograr."),
],
related=[("Consejos de publicidad en redes sociales", S + "/infografia-consejos-sobre-publicidad-en-las-redes-sociales/"), ("Campaña en buscadores", BUSCADORES)],
),

dict(
id=1979, slug="infografia-en-que-crean-empleo-las-pymes-espanolas",
title="En qué crean empleo las pymes españolas",
excerpt="Infografía de Cinco Días con las actividades que más empleo crearon en las pymes españolas a inicios de 2017 por tamaño de empresa: restaurantes, construcción, comercio y servicios.",
img_alt="Infografía de las actividades más dinámicas en las pymes españolas",
credit="Infografía: Cinco Días, con datos del Boletín trimestral de empleo en las pymes de Cepyme y Randstad.",
body=f"""
¿En qué sectores crean empleo las pequeñas y medianas empresas? Esta infografía muestra las actividades más dinámicas en las pymes de España, según las afiliaciones a la seguridad social del primer trimestre de 2017 frente al año anterior.

{{IMG}}

## Por tamaño de empresa (miles de afiliaciones, variación anual)

**De 1 a 9 trabajadores**
- Servicios de comidas y bebidas.
- Construcción especializada (6,845).
- Construcción de edificios (6,774).
- Comercio al por menor (5,521).
- Otros servicios personales (4,620).

**De 10 a 49 trabajadores**
- Servicios de comidas y bebidas (22,208).
- Construcción especializada (11,493).
- Comercio al por mayor (10,393).
- Comercio al por menor (9,733).
- Construcción de edificios (9,577).

**De 50 a 249 trabajadores**
- Comercio al por mayor (10,620).
- Servicios de comidas y bebidas (9,244).
- Asistencia en establecimientos residenciales (6,955).
- Servicios a edificios y jardinería (6,834).

## Lo que muestra

Restaurantes, construcción y comercio concentraban la creación de empleo en las pymes, en plena recuperación tras la crisis.

## Para pymes en México

El patrón es parecido: en México, las micro, pequeñas y medianas empresas generan la mayor parte del empleo, y los servicios de comida y el comercio están entre los sectores con más negocios. Para crecer, muchas necesitan lo mismo: que más clientes las encuentren. Lee [inbound marketing para pymes]({PYMES}) y [por qué tu empresa necesita una página web]({S}/infografia-por-que-tu-empresa-necesita-tener-una-web/).
""",
faq=[
("¿Qué sectores generan más empleo en las pymes españolas?", "Según la infografía de 2017: servicios de comidas y bebidas, construcción y comercio."),
("¿Las pymes generan mucho empleo?", "Sí; en España y en México, las micro, pequeñas y medianas empresas generan la mayor parte del empleo."),
("¿Qué es una pyme?", "Una pequeña o mediana empresa; en esta infografía, las que tienen de 1 a 249 trabajadores."),
],
related=[("Inbound marketing para pymes", PYMES), ("Por qué tu empresa necesita una página web", S + "/infografia-por-que-tu-empresa-necesita-tener-una-web/")],
),

dict(
id=1767, slug="infografia-desmontando-los-mitos-negativos-del-cloud-computing",
title="5 mitos de la nube que no son ciertos",
excerpt="Infografía de Sage que desmonta 5 mitos del cloud computing: costos, seguridad, utilidad, obsolescencia y dependencia de internet, con datos del sector en España y Europa.",
img_alt="Infografía desmontando los mitos negativos del cloud computing",
credit="Infografía: Sage.",
body=f"""
"La nube es cara, insegura y no la necesito." Esta infografía de Sage responde a esos y otros mitos con datos.

{{IMG}}

## Los 5 mitos

**1. "Los costos son inabarcables."** La nube puede reducir costos hasta 40%: ahorro en software y hardware, menos mantenimiento técnico (lo hace el proveedor), menos renovación de equipos y pago por uso.

**2. "Falta seguridad y privacidad."** Se puede navegar seguro: claves largas con letras y números, verificación en dos pasos, cifrado de archivos, respaldos frecuentes, conexiones seguras y no dar más datos de los necesarios.

**3. "No es necesaria para trabajar."** Permite compartir archivos desde cualquier lugar y dispositivo, evita instalar y actualizar programas en cada equipo, ayuda ante caídas y respaldos, y comparte recursos de forma eficiente.

**4. "Se puede quedar obsoleta."** Es escalable: se adapta a las necesidades de cada momento, con actualizaciones casi en tiempo real, a distancia y sin costo.

**5. "Si se corta internet, no hay servicio."** Bastan dispositivos con alternativas de conexión.

## La nube en datos

- Se esperaba que para 2019 más de la mitad de los datos críticos estuvieran en la nube: información de clientes (53%) y datos financieros (51%).
- Según la Comisión Europea, su adopción podría aportar 160,000 millones de euros al año al PIB de la UE y crear unos 3.5 millones de empleos.
- **Top 5 mundial en cloud computing:** Japón, Estados Unidos, Alemania, Canadá y Francia. España ocupaba el lugar 11 en 2016.
- El 43% de las compañías optaba por nube privada, el 23% por pública y el 33% por soluciones híbridas.

## Hoy

El debate de si usar la nube ya casi no existe: correo, documentos, facturación y CRM viven ahí. El reto actual es usarla bien: controlar accesos, no acumular suscripciones y respaldar lo importante. Lee [el futuro de las empresas está en la nube]({S}/infografia-el-futuro-de-las-empresas-esta-en-la-nube/) y [cómo contratar servicios en la nube con seguridad]({S}/infografia-contrata-en-la-nube-con-seguridad/).
""",
faq=[
("¿La nube es segura?", "Puede serlo tanto o más que un servidor propio si usas contraseñas fuertes, verificación en dos pasos, cifrado y respaldos."),
("¿Cuánto se ahorra con la nube?", "La infografía habla de hasta 40% de reducción de costos por menos inversión en equipos, software y mantenimiento."),
("¿Qué es una nube híbrida?", "Una combinación de nube privada y pública, que permite elegir dónde guardar cada tipo de información."),
],
related=[("El futuro de las empresas está en la nube", S + "/infografia-el-futuro-de-las-empresas-esta-en-la-nube/"), ("Contratar en la nube con seguridad", S + "/infografia-contrata-en-la-nube-con-seguridad/")],
),

dict(
id=2253, slug="infografia-las-cifras-de-la-hoteleria-en-2016",
title="Las cifras de la hotelería en 2016 (infografía)",
excerpt="Infografía de las cifras de la hotelería en 2016: precio por habitación en Europa y España, 330 millones de pernoctaciones, inversión de 2,155 millones de euros, redes sociales y cadenas con más habitaciones.",
img_alt="Infografía de las cifras de la hotelería en 2016",
credit="Infografía: Lahotelista.net y Hostelco, con datos de la OMT, INE, Trivago, Statista, JLL y Hosteltur.",
body=f"""
2016 fue un gran año para la hotelería en España. Esta infografía resume precios, ocupación, inversión y presencia en redes de las principales cadenas.

{{IMG}}

## Precio por habitación

**Europa:** Montecarlo (320 euros), Ginebra (231), Berna (184), Londres (182) y Copenhague (179), frente a Kiev (57) y Belgrado (61).

**España:** Palma (148 euros), Barcelona (141), San Sebastián (125) y Madrid (106), frente a Lleida (59), Lugo (60) y Murcia (62).

**Facturación media por habitación:** 82.3 euros; 181.4 en hoteles de cinco estrellas, 88.6 en cuatro y 66.8 en tres.

## Pernoctaciones

- **330 millones** de estancias (+7.1%) y **75.6 millones** de turistas (+10.3%).
- El 50% de las estancias fue de 4 a 7 noches.
- Crecieron los visitantes de Reino Unido (+11%) y Alemania (+6.6%).

## Inversión en el sector

**2,155 millones de euros,** 18.6% menos que en 2015. Por destino: Madrid (28%), Barcelona (16%), Málaga y Fuerteventura (7.4%), Valencia (7%) y Mallorca (6.1%).

## Redes sociales

- **Twitter:** Paladium (237,003 seguidores), Barceló (209,144), NH (148,905), Meliá (145,952) y Riu (82,799).
- **Facebook:** Meliá (2,542,745), Barceló (1,466,583), Paladium (1,190,944), Riu (892,434) y Catalonia (439,071).
- **Hoteles más fotografiados en Instagram:** encabezados por el MGM Grand de Las Vegas.

## Habitaciones

Meliá (83,252 en el mundo; 34,867 en España), NH (58,714; 17,588), Riu (42,291) y Barceló (13,858 en España).

## Lo que aprende cualquier hotel

Las grandes cadenas invierten en redes, pero un hotel independiente puede competir con algo que ellas no tienen: cercanía y experiencias locales. Lee [inbound marketing para hoteles]({S}/inbound-marketing-para-hoteles/) y [el sector de la hostelería en España y Europa]({S}/infografia-el-sector-de-la-hosteleria-en-europa/).
""",
faq=[
("¿Cuál era la ciudad más cara de Europa para hospedarse en 2016?", "Montecarlo, con un precio medio de 320 euros por habitación, según la infografía."),
("¿Cuántas pernoctaciones tuvo España en 2016?", "330 millones de estancias, un 7.1% más que el año anterior."),
("¿Qué cadena hotelera española tenía más habitaciones?", "Meliá, con 83,252 habitaciones en el mundo."),
],
related=[("Inbound marketing para hoteles", S + "/inbound-marketing-para-hoteles/"), ("El sector de la hostelería en España y Europa", S + "/infografia-el-sector-de-la-hosteleria-en-europa/")],
),

dict(
id=2075, slug="infografia-telefonos-que-mas-fidelizan-a-sus-usuarios",
title="Las marcas de celular con clientes más fieles",
excerpt="Infografía de lealtad a las marcas de celular en Estados Unidos en 2017: el 92% de los usuarios de iPhone volvería a comprar Apple, frente a 77% de Samsung, 59% de LG, 56% de Motorola y 42% de Nokia.",
img_alt="Infografía de los teléfonos que más fidelizan a sus usuarios",
credit="Infografía: Insider Pro con datos de Morgan Stanley.",
body=f"""
Quien prueba el iPhone casi nunca se cambia. Esta infografía, con una encuesta de Morgan Stanley de 2017 en Estados Unidos, mide qué tan fieles son los usuarios de cada marca.

{{IMG}}

## Usuarios que volverían a comprar la misma marca

| Marca | Lealtad |
|---|---|
| Apple | 92% |
| Samsung | 77% |
| LG | 59% |
| Motorola | 56% |
| Nokia | 42% |

Encuesta a 1,000 estadounidenses que pensaban cambiar de teléfono en los siguientes 12 meses.

## Por qué Apple retiene tanto

No es solo el teléfono: es el ecosistema. Apps compradas, fotos en iCloud, Apple Watch, AirPods, iMessage. Cambiar de marca significa perder o migrar todo eso, y la experiencia es consistente año con año.

## Lo que pasó después

LG salió del negocio de celulares en 2021, y en Latinoamérica marcas como Xiaomi y Motorola ganaron participación. Apple y Samsung siguen dominando la lealtad.

## La lección para cualquier negocio

La retención se construye haciendo que quedarse sea más fácil y valioso que irse: buena experiencia, servicios conectados y beneficios que se acumulan. Lee [¿comprarías un Galaxy Note 8 tras el Note 7?]({S}/infografia-te-planteas-comprar-un-samsung-galaxy-note-8/) y [cómo hacer que tus clientes te recomienden]({RECOMIENDEN}).
""",
faq=[
("¿Qué marca de celular tiene los clientes más leales?", "Apple: el 92% de sus usuarios volvería a comprar un iPhone, según Morgan Stanley (2017)."),
("¿Por qué los usuarios de iPhone no cambian de marca?", "Por el ecosistema de apps, servicios y dispositivos conectados, además de una experiencia consistente."),
("¿Cómo aumentar la lealtad de los clientes?", "Ofreciendo buena experiencia, servicios que se integran entre sí y beneficios que crecen con el tiempo."),
],
related=[("¿Comprarías un Galaxy Note 8 tras el Note 7?", S + "/infografia-te-planteas-comprar-un-samsung-galaxy-note-8/"), ("Cómo hacer que tus clientes te recomienden", RECOMIENDEN)],
),
]
