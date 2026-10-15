from comun import *

POSTS = [
dict(
id=2054, slug="infografia-25-personas-mas-ricas-del-mundo",
title="Las 25 personas más ricas del mundo (2017)",
excerpt="Infografía con las 25 personas más ricas del mundo en 2017 según Forbes, por edad, país y patrimonio: Bill Gates a la cabeza, Carlos Slim como el mexicano de la lista, y lo que cambió desde entonces.",
img_alt="Infografía de las 25 personas más ricas del mundo por edad, país y patrimonio",
credit="Infografía: Insider Pro con datos de Forbes.",
body=f"""
¿Quiénes eran las personas más ricas del mundo en 2017, de dónde venían y qué edad tenían? Esta infografía las ubica en una gráfica de edad contra patrimonio.

{{IMG}}

## Los primeros lugares (miles de millones de dólares, aproximado)

1. **Bill Gates** (Estados Unidos): unos 86.
2. **Warren Buffett** (Estados Unidos): unos 76.
3. **Jeff Bezos** (Estados Unidos): unos 73.
4. **Amancio Ortega** (España): unos 70.
5. **Mark Zuckerberg** (Estados Unidos): unos 56.
6. **Carlos Slim Helú** (México): unos 54.
7. **Larry Ellison** (Estados Unidos): unos 53.

Completan la lista Charles y David Koch, Michael Bloomberg, Larry Page, Sergey Brin, Bernard Arnault, Liliane Bettencourt, Alice, Jim y S. Robson Walton, Wang Jianlin, Li Ka-shing, Sheldon Adelson, Steve Ballmer, Jorge Paulo Lemann, Jack Ma, David Thompson y Karl Albrecht Jr.

**Lo que se ve:** la mayoría eran estadounidenses, la mayoría tenía más de 60 años y Zuckerberg, con poco más de 30, era la gran excepción.

## Lo que cambió

La lista se transformó por completo: Elon Musk, que no aparecía, llegó al primer lugar; Bezos, Bernard Arnault y los fundadores de empresas de tecnología e inteligencia artificial subieron con fuerza. Varios de los nombres de 2017 fallecieron, como Liliane Bettencourt, Sheldon Adelson y David Koch. Carlos Slim sigue siendo la persona más rica de México.

## La lección

Casi todas estas fortunas vienen de construir empresas que resolvieron algo a gran escala, y de reinvertir durante décadas. Lee [cómo Jeff Bezos llegó a ser el más rico]({S}/infografia-evolucion-de-las-5-personas-mas-ricas-del-mundo/) y [las ciudades con más multimillonarios]({S}/infografia-las-ciudades-con-mayor-cantidad-de-habitantes-multimillonarios/).
""",
faq=[
("¿Quién era la persona más rica del mundo en 2017?", "Bill Gates, con unos 86,000 millones de dólares, según Forbes."),
("¿Qué mexicano aparecía entre los más ricos del mundo?", "Carlos Slim Helú, con unos 54,000 millones de dólares en 2017."),
("¿Quién era el más joven de la lista?", "Mark Zuckerberg, con poco más de 30 años."),
],
related=[("Cómo Jeff Bezos llegó a ser el más rico", S + "/infografia-evolucion-de-las-5-personas-mas-ricas-del-mundo/"), ("Ciudades con más multimillonarios", S + "/infografia-las-ciudades-con-mayor-cantidad-de-habitantes-multimillonarios/")],
),

dict(
id=1685, slug="infografia-tomar-decisiones-por-que-es-tan-dificil",
title="Tomar decisiones: ¿por qué es tan difícil?",
excerpt="Infografía de Área Humana sobre por qué nos cuesta tomar decisiones: los pensamientos que nos bloquean, las 4 esferas de la decisión y 10 peligros, del perfeccionismo al miedo a fallar.",
img_alt="Infografía de por qué es tan difícil tomar decisiones",
credit="Infografía: Área Humana, investigación e innovación en psicología.",
body=f"""
"¿Y si me equivoco?" Esa pregunta puede paralizarnos ante decisiones grandes y pequeñas. Esta infografía de Área Humana explica por qué decidir cuesta tanto y qué trampas evitar.

{{IMG}}

## Los pensamientos que nos bloquean

- "Si me equivoco, las consecuencias serán irreparables."
- "No estoy a la altura de tanta responsabilidad."
- "¿Qué pensarán de mí si no tomo la decisión correcta?"
- "No puedo equivocarme, tengo que prever todas las posibilidades."

## Las 4 esferas de la decisión

La infografía relaciona la decisión con la autoconfianza, la autoestima, los estilos de pensamiento y los peligros que la rodean.

## Los 10 peligros

1. Perfeccionismo.
2. Creer que "siempre" tomamos malas decisiones.
3. Intentar controlar todas las alternativas.
4. Necesidad de aceptación.
5. Decidir por impulso para quitarnos el malestar.
6. Delegar las decisiones en otros.
7. Negarnos el derecho a equivocarnos.
8. Precipitarnos.
9. Miedo a fallar a los demás.
10. Inflexibilidad o visión reducida.

**Dos ideas para quedarte:** "Las decisiones no son correctas o incorrectas, son más o menos adecuadas a los objetivos, el contexto y las circunstancias". Y: "Tenemos derecho a equivocarnos".

## En el trabajo

- **Define qué es suficiente:** no toda decisión necesita toda la información.
- **Pregunta si es reversible.** Las que se pueden corregir se toman rápido; las irreversibles merecen más tiempo.
- **Pon fecha límite** a la decisión.

Si la indecisión te genera angustia constante, puede ayudarte hablar con un profesional de la psicología. Lee [los miedos que frenan tu éxito en el trabajo]({S}/infografia-5-miedos-que-frenan-tu-exito-en-el-trabajo/) y [cómo controlar tus emociones]({EMOCIONES}).
""",
faq=[
("¿Por qué me cuesta tanto tomar decisiones?", "Con frecuencia por perfeccionismo, miedo a equivocarte o a fallar a otros, necesidad de aceptación o el intento de controlar todas las alternativas."),
("¿Cómo tomar mejores decisiones?", "Aceptando que no hay decisiones perfectas, distinguiendo las reversibles de las irreversibles, poniendo fecha límite y evaluando según tus objetivos y contexto."),
("¿Es malo delegar las decisiones?", "Delegar puede ser útil, pero hacerlo siempre para evitar la responsabilidad es uno de los peligros que señala la infografía."),
],
related=[("Los miedos que frenan tu éxito en el trabajo", S + "/infografia-5-miedos-que-frenan-tu-exito-en-el-trabajo/"), ("Cómo controlar tus emociones", EMOCIONES)],
),

dict(
id=2083, slug="infografia-7-tendencias-en-elearning",
title="7 tendencias en e-learning (infografía)",
excerpt="Infografía con 7 tendencias de 2017 en e-learning: aprendizaje adaptativo, big data, cápsulas de formación, social learning, aprendizaje experiencial, gamificación y mobile learning.",
img_alt="Infografía de 7 tendencias 2017 en e-learning",
credit="Infografía: Entrena (MHP Servicios de Control).",
body=f"""
La formación en línea dejó de ser un PDF con un examen al final. Esta infografía resumió siete tendencias que marcaban el e-learning en 2017.

{{IMG}}

## Las 7 tendencias

1. **Personalización progresiva y aprendizaje adaptativo.** Cada persona aprende a partir de lo que ya sabe; personalizar es el gran reto y el objetivo de todas las demás tendencias.
2. **Big data.** Cada acción formativa genera datos valiosos para decidir mejor.
3. **Autoaprendizaje y cápsulas de formación.** Tú eliges cuándo, cómo, dónde y cuánto tiempo, con cápsulas de contenido de libre acceso.
4. **Social learning.** Asimilamos un conocimiento cuando lo compartimos; los propios empleados son una fuente inagotable de conocimiento.
5. **Aprendizaje experiencial.** La mejor forma de aprender es haciendo, experimentando y equivocándonos.
6. **Gamificación.** No solo por "aprender jugando", sino por la emoción que hace que el aprendizaje perdure.
7. **Mobile learning e internet de las cosas.** Facilitar el acceso desde cualquier dispositivo reduce el abandono.

## Lo que pasó después

La pandemia aceleró todas estas tendencias, y la inteligencia artificial hizo realidad la primera: tutores que adaptan el contenido y responden dudas al momento. El microaprendizaje en video corto también se volvió estándar.

## Para capacitar a tu equipo

Combina cápsulas cortas en el celular con práctica real y espacios para que tu gente comparta lo que sabe. Y mide si lo aprendido se aplica, no solo si se completó el curso. Lee [gestión del talento en equipos de e-learning]({S}/infografia-gestion-del-talento-en-equipos-de-elearning/) y [BYOD y MOOC en las aulas]({S}/infografia-byod-y-mooc-en-las-aulas/).
""",
faq=[
("¿Cuáles son las tendencias del e-learning?", "Aprendizaje adaptativo, analítica de datos, microaprendizaje, aprendizaje social, aprendizaje práctico, gamificación y formación desde el celular, hoy potenciadas por la IA."),
("¿Qué es el aprendizaje adaptativo?", "Un modelo en el que el contenido se ajusta al nivel, ritmo y necesidades de cada persona."),
("¿Qué es la gamificación en la formación?", "Usar elementos de juego, como puntos, retos o niveles, para motivar y hacer que el aprendizaje perdure."),
],
related=[("Gestión del talento en equipos de e-learning", S + "/infografia-gestion-del-talento-en-equipos-de-elearning/"), ("BYOD y MOOC en las aulas", S + "/infografia-byod-y-mooc-en-las-aulas/")],
),

dict(
id=1985, slug="infografia-como-indexa-google-el-contenido",
title="Cómo indexa Google el contenido (infografía)",
excerpt="Infografía de cómo indexa Google el contenido: participación de los buscadores en PC y móvil, y el proceso de rastreo, indexación, base de datos, algoritmo y lista de resultados.",
img_alt="Infografía de cómo indexa Google el contenido",
credit="Infografía: JACN Creative Network, con datos de Alexa Rank.",
body=f"""
¿Qué pasa entre que publicas una página y que aparece en Google? Esta infografía explica el proceso en pocos pasos.

{{IMG}}

## Los principales buscadores (según Alexa Rank)

| Computadora | Móvil |
|---|---|
| Google 68.54% | Google 92.71% |
| Baidu 10.18% | Yahoo 4.83% |
| Bing 9.86% | Bing 1.97% |
| Yahoo 9.26% | Baidu 0.20% |
| AOL 0.47% | Ask 0.06% |
| Ask 0.27% | AOL 0.002% |

## El proceso

1. **Rastreo:** un robot (también llamado spider o crawler) recorre los sitios web y **recopila los datos.**
2. **Indexación:** la información se guarda en una **base de datos.**
3. **Algoritmo:** **ordena los datos** según su relevancia.
4. **Buscador:** muestra la **lista de resultados.**

Todo empieza con una búsqueda del usuario, que puede ser de navegación (ir a un sitio), de información o de transacción (comprar o contratar).

## Cómo ayudar a Google a indexarte

- **Da de alta tu sitio en Google Search Console** y envía tu mapa del sitio.
- **Enlaza tus páginas entre sí** para que el robot las encuentre.
- **Revisa el informe de indexación:** te dice qué páginas están dentro y por qué otras no.
- **Evita bloquear por error** páginas importantes en el archivo robots.txt o con etiquetas noindex.

Hoy, además, Google muestra resúmenes generados con IA en muchas búsquedas. Estar bien indexado y ser una fuente clara y confiable es la base para aparecer ahí también.

Lee [qué es RankBrain]({S}/infografia-que-es-rankbrain-y-como-influye-en-el-seo/) y [13 consejos para posicionar sin saber SEO]({S}/infografia-13-consejos-sencillos-para-posicionar-sin-saber-seo/).
""",
faq=[
("¿Cómo indexa Google una página?", "Un robot rastrea la web, guarda la información en su índice, el algoritmo la ordena por relevancia y la muestra en los resultados cuando alguien busca."),
("¿Cuánto tarda Google en indexar una página?", "Puede tardar de horas a semanas; enviar el mapa del sitio y enlazar la página desde otras ayuda a acelerarlo."),
("¿Cómo saber si mi página está indexada?", "En Google Search Console, con el informe de indexación o la herramienta de inspección de URL."),
],
related=[("Qué es RankBrain", S + "/infografia-que-es-rankbrain-y-como-influye-en-el-seo/"), ("13 consejos para posicionar sin saber SEO", S + "/infografia-13-consejos-sencillos-para-posicionar-sin-saber-seo/")],
),

dict(
id=2189, slug="infografia-como-atraer-mas-visitas-a-tu-perfil-de-linkedln",
title="Cómo atraer más visitas a tu perfil de LinkedIn",
excerpt="Infografía con 8 formas de atraer más visitas a tu perfil de LinkedIn: compartir y publicar contenido, comentar, visitar perfiles, invitaciones personalizadas, validaciones, firma de correo y perfil optimizado.",
img_alt="Infografía de cómo atraer más visitas a tu perfil de LinkedIn",
credit="Infografía: Luz Grango (luzgrango.com).",
body=f"""
Un perfil de LinkedIn que nadie visita no genera oportunidades. Esta infografía propone ocho acciones sencillas para que más personas lleguen al tuyo.

{{IMG}}

## Las 8 acciones

1. **Comparte contenido de valor** en tu perfil y en grupos de tu interés.
2. **Publica contenido original;** te dará visitas y autoridad profesional.
3. **Recomienda y comenta** publicaciones de profesionales de tu sector.
4. **Visita perfiles** de personas de tu interés; algunas te devolverán la visita.
5. **Envía invitaciones personalizadas** a conectar.
6. **Valida las aptitudes de tus contactos;** les llega el aviso y muchos visitan tu perfil.
7. **Incluye el enlace a tu perfil en tu firma de correo.**
8. **Optimiza tu perfil** para aparecer en las búsquedas de los reclutadores.

**Ten tu perfil impecable** para que la visita valga la pena.

## Lo que más funciona hoy

- **Comentar con aportes reales** en publicaciones de tu sector suele darte más visibilidad que publicar poco y en solitario.
- **Tu titular** es lo primero que ven en comentarios y búsquedas: di a quién ayudas y cómo.
- **Activa el modo creador** si publicas con frecuencia, para destacar tus temas.

Lee [cómo optimizar tu perfil de LinkedIn]({S}/infografia-como-optimizar-tu-perfil-de-linkedin-para-generar-oportunidades/) y [10 maneras de usar LinkedIn para hacer networking]({S}/infografia-10-maneras-de-usar-linkedin-para-generar-networking/).
""",
faq=[
("¿Cómo conseguir más visitas en mi perfil de LinkedIn?", "Publicando y comentando contenido útil, visitando perfiles relevantes, enviando invitaciones personalizadas y teniendo un perfil optimizado."),
("¿Sirve validar aptitudes de mis contactos?", "Sí; les llega una notificación y muchos visitan tu perfil en respuesta."),
("¿Qué debe decir mi titular de LinkedIn?", "A quién ayudas y cómo, con palabras que usarían quienes te buscan."),
],
related=[("Cómo optimizar tu perfil de LinkedIn", S + "/infografia-como-optimizar-tu-perfil-de-linkedin-para-generar-oportunidades/"), ("10 maneras de usar LinkedIn para hacer networking", S + "/infografia-10-maneras-de-usar-linkedin-para-generar-networking/")],
),

dict(
id=1687, slug="infografia-el-coste-de-una-mala-contratacion",
title="El costo real de una mala contratación",
excerpt="Infografía de Talentier sobre el costo de una mala contratación: el 70% de los directores de RR. HH. ha contratado a alguien que no cumplió, la prisa es la causa principal y puede costar más de 50,000 dólares.",
img_alt="Infografía de cuál es el coste real de una mala contratación",
credit="Infografía: Talentier, con datos de Robert Half, CareerBuilder y Harvard Business Review.",
body=f"""
Contratar mal sale caro: no solo en sueldo, también en tiempo, moral del equipo y clientes. Esta infografía de Talentier pone cifras al problema.

{{IMG}}

## Un problema extendido

- Al **91%** de los directores de recursos humanos les cuesta identificar y reclutar profesionales calificados.
- El **70%** ha contratado a alguien que no cumplió las expectativas.

## La prisa, mala consejera

- El **38%** de las empresas señala la urgencia por cubrir la vacante como la principal causa de sus malas contrataciones.

## Las consecuencias

- El **80%** de la rotación de personal se debe a malas decisiones de contratación.
- Además: más costos de capacitación, impacto en la moral del equipo, pérdida de productividad, costos de despido, ventas perdidas y tiempo y recursos desperdiciados.

## El costo en dinero (Estados Unidos)

- El **41%** de las empresas estima que una mala contratación cuesta más de **25,000 dólares**, y el **25%**, más de **50,000.**
- En puestos con sueldos altos (110,000 a 130,000 dólares), el costo llega a **220,000 dólares;** en puestos con sueldos bajos, a unos **25,000.**

## Cómo evitarlo

- **Define el perfil** antes de publicar: resultados esperados, no solo requisitos.
- **No te saltes pasos por prisa;** una vacante abierta unas semanas más cuesta menos que un mal ingreso.
- **Usa pruebas prácticas** y referencias.
- **Cuida la integración:** muchos ingresos fallan por una mala bienvenida.

Lee [5 habilidades del reclutador de hoy]({S}/infografia-5-habilidades-del-reclutador-actual/) y [10 razones por las que no te contratarían]({S}/infografia-10-razones-por-las-que-no-te-contratarian-version-2/).
""",
faq=[
("¿Cuánto cuesta una mala contratación?", "Según la infografía, el 41% de las empresas estima más de 25,000 dólares y el 25%, más de 50,000; en puestos altos puede llegar a 220,000."),
("¿Cuál es la principal causa de las malas contrataciones?", "La urgencia por cubrir la vacante, señalada por el 38% de las empresas."),
("¿Cómo evitar una mala contratación?", "Definiendo bien el perfil, sin saltar pasos por prisa, con pruebas prácticas, referencias y una buena integración."),
],
related=[("5 habilidades del reclutador de hoy", S + "/infografia-5-habilidades-del-reclutador-actual/"), ("10 razones por las que no te contratarían", S + "/infografia-10-razones-por-las-que-no-te-contratarian-version-2/")],
),

dict(
id=2101, slug="infografia-por-que-tu-empresa-necesita-tener-una-web",
title="Por qué tu empresa necesita una página web",
excerpt="Infografía con las ventajas de tener una página web para cualquier negocio: te encuentran en Google Maps, vende 24 horas, es tu mejor catálogo, y cómo optimizarla con anuncios, SEO y medición.",
img_alt="Infografía de por qué a cualquier negocio le conviene una página web",
credit="Infografía: Fontamadrid.",
body=f"""
"Ya tengo Facebook, ¿para qué quiero página web?" Esta infografía responde con las ventajas de tener sitio propio y cómo sacarle provecho.

{{IMG}}

## Las ventajas

- **Apareces en Google Maps** y te encuentran clientes.
- **Adiós al volanteo:** la web reemplaza buena parte de la publicidad impresa.
- **La web vende** las 24 horas, los 365 días.
- **Recibes llamadas directas** desde el celular cuando ven tu teléfono.
- **Es una inversión,** no un gasto: más visibilidad, más clientes, más facturación.
- **Es tu mejor catálogo.**

## Si ya tienes web, optimízala

- **Anúnciate en Google** para aparecer en búsquedas de clientes cercanos.
- **Trabaja el SEO** para posicionarte.
- **Mide los resultados** de tus anuncios para mejorar la conversión.
- **Asegúrate de que sea accesible** desde el celular.
- **Crea un video de presentación** de no más de un minuto.
- **Incluye tus redes sociales** y un sistema de recomendaciones.
- **Facilita el contacto.**
- **Crea contenidos útiles,** como trucos y consejos.
- **Vigila que funcione** y contrata soporte técnico profesional.

## Nuestra opinión

Las redes sociales son terreno prestado: cambian sus reglas y su alcance. Tu sitio es tuyo. Para una pyme en México, una web sencilla, rápida en el celular, con botón de WhatsApp y una ficha de Google Business Profile bien llena da más resultados que muchos esfuerzos dispersos.

Lee [cómo debe ser tu página web]({S}/infografia-como-debe-ser-tu-pagina-web/) y [inbound marketing para pymes]({PYMES}).
""",
faq=[
("¿Por qué un negocio necesita página web si ya tiene redes sociales?", "Porque la web es tuya, aparece en Google, funciona como catálogo las 24 horas y no depende de los cambios de las redes."),
("¿Qué debe tener la página web de una pyme?", "Información clara de lo que haces, contacto visible, botón de WhatsApp, ubicación, testimonios y diseño adaptado al celular."),
("¿Qué es Google Business Profile?", "La ficha gratuita de tu negocio en Google y Google Maps, con horario, ubicación, fotos y reseñas."),
],
related=[("Cómo debe ser tu página web", S + "/infografia-como-debe-ser-tu-pagina-web/"), ("Inbound marketing para pymes", PYMES)],
),

dict(
id=1515, slug="infografia-coches-conectados-mediante-5g",
title="Autos conectados mediante 5G (infografía)",
excerpt="Infografía de los autos conectados mediante 5G: qué cambia del 4G al 5G, casos de uso como evitar colisiones, proyecciones de vehículos conectados y del mercado del auto conectado.",
img_alt="Infografía de coches conectados mediante 5G",
credit="Infografía con datos de 5GAA, 5G Forum, ABI Research, TrendForce y Statista.",
body=f"""
Los autos se están convirtiendo en computadoras con ruedas, y el 5G es la red que les permitirá hablar entre ellos y con la ciudad. Esta infografía explica qué cambia y qué se esperaba.

{{IMG}}

## Del 4G al 5G

- Latencia muy baja.
- Más velocidad.
- Más bandas de frecuencia, y más altas.
- Más conexiones simultáneas.

## Casos de uso

Asesor en intersecciones sin visibilidad, advertencias en tiempo real, prevención de colisiones, señales de tráfico, control de velocidad y control de prioridad, además de posicionamiento e itinerario GPS, análisis del comportamiento al volante y analítica.

## Las proyecciones

Para 2020, la infografía preveía:
- Que el 75% de los autos nuevos estuvieran conectados.
- Unos 250 millones de vehículos conectados en las carreteras.
- Millones de suscripciones 5G en autos y miles de millones de sensores conectados.
- Un mercado del auto conectado creciendo de unos 4,283 millones de dólares a más de 16,000 millones.

## Lo que pasó después

El auto conectado sí se volvió normal: la mayoría de los autos nuevos tienen conexión, actualizaciones a distancia y apps. El 5G en autos y la comunicación entre vehículos (V2X) avanzaron más lento de lo previsto, y los autos totalmente autónomos siguen limitados a servicios en algunas ciudades.

Lee [quién tiene más patentes del coche autónomo]({S}/infografia-que-fabricantes-tienen-mas-patentes-sobre-el-coche-autonomo/) y [redes LTE-A en América Latina]({S}/infografia-redes-lte-a-despego-en-paises-latinoamericanos-2018/).
""",
faq=[
("¿Qué es un auto conectado?", "Un vehículo con conexión a internet que puede recibir actualizaciones, ofrecer servicios en línea y comunicarse con otros sistemas."),
("¿Por qué importa el 5G para los autos?", "Por su baja latencia y capacidad para muchas conexiones simultáneas, clave para advertencias en tiempo real y comunicación entre vehículos."),
("¿Qué es V2X?", "La comunicación del vehículo con todo su entorno: otros autos, semáforos, peatones y la red."),
],
related=[("Quién tiene más patentes del coche autónomo", S + "/infografia-que-fabricantes-tienen-mas-patentes-sobre-el-coche-autonomo/"), ("Redes LTE-A en América Latina", S + "/infografia-redes-lte-a-despego-en-paises-latinoamericanos-2018/")],
),

dict(
id=1635, slug="infografia-malos-tiempos-para-el-dolar",
title="Malos tiempos para el dólar en 2017 (infografía)",
excerpt="Infografía del rendimiento del dólar frente a las principales monedas del 1 de enero al 18 de julio de 2017: el peso mexicano fue la moneda frente a la que más cayó, con 15.3%.",
img_alt="Infografía de tiempos difíciles para el dólar estadounidense frente a otras monedas",
credit="Infografía: Insider Pro con datos de FactSet.",
body=f"""
A principios de 2017, muchos esperaban un dólar fuerte. Pasó lo contrario. Esta infografía muestra cómo le fue al dólar frente a las principales monedas entre el 1 de enero y el 18 de julio de 2017.

{{IMG}}

## Rendimiento del dólar frente a cada moneda

| Moneda | Variación del dólar |
|---|---|
| Dólar de Hong Kong | +0.6% |
| Lira turca | +0.4% |
| Rand sudafricano | 0% |
| Real brasileño | -2.2% |
| Renminbi chino | -2.8% |
| Rublo ruso | -2.9% |
| Yen japonés | -4.1% |
| Libra esterlina | -5.2% |
| Rupia india | -5.3% |
| Dólar de Singapur | -5.5% |
| Dólar neozelandés | -5.8% |
| Dólar canadiense | -6.2% |
| Franco suizo | -6.3% |
| Corona noruega | -6.4% |
| Won coreano | -6.9% |
| Euro | -9% |
| Corona sueca | -9% |
| Dólar australiano | -9.2% |
| **Peso mexicano** | **-15.3%** |

El peso mexicano fue la moneda frente a la que más se debilitó el dólar, tras la fuerte caída del peso a finales de 2016.

## Lo que pasó después

El tipo de cambio siguió subiendo y bajando con la política, las tasas de interés y la economía mundial. En los años siguientes hubo etapas de "superpeso" y otras de depreciación. Lo único constante es la volatilidad.

## Para tu negocio

Si importas, exportas o vendes en dólares, el tipo de cambio afecta tus márgenes. Considera precios con margen para la variación, coberturas cambiarias con tu banco y, cuando sea posible, costos y precios en la misma moneda. Esto no es una recomendación de inversión. Lee [la paradoja del índice Big Mac y el índice iPhone]({S}/infografia-la-paradoja-entre-el-indice-big-mac-y-el-indice-iphone/) y [todo el dinero del mundo en perspectiva]({S}/infografia-todo-el-dinero-del-mundo-en-perspectiva/).
""",
faq=[
("¿Frente a qué moneda cayó más el dólar en la primera mitad de 2017?", "Frente al peso mexicano, con una baja de 15.3% entre enero y julio de 2017."),
("¿Qué mueve el tipo de cambio peso-dólar?", "Las tasas de interés, la inflación, la economía, el comercio y la percepción de riesgo político, entre otros factores."),
("¿Cómo protege una empresa sus márgenes del tipo de cambio?", "Con precios que consideren la variación, coberturas cambiarias y, cuando es posible, costos e ingresos en la misma moneda."),
],
related=[("Índice Big Mac e índice iPhone", S + "/infografia-la-paradoja-entre-el-indice-big-mac-y-el-indice-iphone/"), ("Todo el dinero del mundo en perspectiva", S + "/infografia-todo-el-dinero-del-mundo-en-perspectiva/")],
),

dict(
id=9511, slug="infografia-home-office-en-mexico",
title="Home office en México: lo que cambió con la ley",
excerpt="Infografía sobre el home office en México: lo que aprobó el Senado en 2019, ventajas y desventajas del trabajo remoto con datos, y el ABC para un home office efectivo. Con la reforma de teletrabajo de 2021.",
img_alt="Infografía de México da un paso más hacia el home office",
body=f"""
En junio de 2019, el Senado mexicano avaló reformas para reconocer y promover el trabajo remoto. Esta infografía resume qué se aprobó, las ventajas y desventajas del home office y cómo hacerlo bien.

{{IMG}}

## Lo que aprobó el Senado (2019)

- Reconocer al teletrabajador como la persona que usa la tecnología para trabajar sin estar físicamente en una oficina.
- Que el empleador ofrezca el equipo necesario.
- Igualdad de pago, capacitación y condiciones entre quienes trabajan a distancia y en la oficina.
- El empleador es responsable de la salud, seguridad y prevención de riesgos del teletrabajo.
- Una red nacional para asesorar, promover y fomentar el home office.

## A favor del home office

- El **80%** de las personas prefiere hacer home office que ganar más.
- El **23%** de quienes trabajan en casa eleva su productividad.
- Los gastos de las empresas con trabajo remoto se reducen **18%.**
- El ausentismo baja **19%** cuando la gente controla sus horarios.
- La rotación baja **40%.**

## Lo negativo

- El **41%** de los teletrabajadores tiene altos niveles de estrés.
- Un empleado remoto trabaja **1.9 horas** más a la semana que uno presencial.
- El **45%** hace tareas domésticas mientras trabaja.
- El **36%** empieza más temprano o termina más tarde.
- El **66%** de los empleadores prefiere contratar a alguien presencial.

**El futuro, según la infografía:** el 50% de los trabajadores del mundo trabajaría a distancia en 2020.

## ABC para un home office efectivo

- Trabajar con objetivos claros y cumplirlos.
- Comunicación constante con el equipo.
- Un lugar adecuado para trabajar.
- El equipo y software necesarios.
- Una rutina, aunque estés fuera de la oficina.

## Lo que pasó después

La pandemia de 2020 convirtió el home office en realidad para millones. En enero de 2021 se publicó la reforma a la Ley Federal del Trabajo sobre teletrabajo, que obliga al empleador a dar equipo, a ayudar con gastos de internet y luz, y reconoce el derecho a la desconexión. Después, muchas empresas adoptaron esquemas híbridos.

Lee [los países que más desconectan en vacaciones]({S}/infografia-los-paises-que-mas-desconectan-en-vacaciones/) y [qué hay en el corazón de una empresa saludable]({S}/infografia-que-hay-en-el-corazon-de-una-empresa-saludable/).
""",
faq=[
("¿Qué dice la ley sobre el home office en México?", "Desde la reforma de 2021, el empleador debe proporcionar equipo, apoyar con gastos de internet y luz, cuidar la salud y seguridad del teletrabajador y respetar su derecho a la desconexión."),
("¿El home office aumenta la productividad?", "Según la infografía, el 23% de quienes trabajan en casa eleva su productividad, aunque también aumentan el estrés y las horas trabajadas."),
("¿Cómo hacer home office de forma efectiva?", "Con objetivos claros, comunicación constante, un espacio adecuado, buen equipo y una rutina."),
],
related=[("Los países que más desconectan en vacaciones", S + "/infografia-los-paises-que-mas-desconectan-en-vacaciones/"), ("Qué hay en el corazón de una empresa saludable", S + "/infografia-que-hay-en-el-corazon-de-una-empresa-saludable/")],
),
]
