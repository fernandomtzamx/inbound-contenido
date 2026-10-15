from comun import *

POSTS = [
dict(
id=1817, slug="infografia-7-motivos-para-instalar-un-antivirus-para-android",
title="7 motivos para instalar un antivirus en Android",
excerpt="Infografía con 7 motivos para instalar un antivirus en Android: navegación móvil, privacidad, localizar el teléfono, batería, archivos basura y más virus.",
img_alt="Infografía de 7 motivos para instalar un antivirus para Android",
body=f"""
Tu celular sabe más de ti que tu familia: contraseñas, fotos, conversaciones, la app del banco y los accesos de tu empresa. Y aun así, mucha gente lo protege menos que su computadora.

Esta infografía da siete motivos para instalar un antivirus en Android.

{{IMG}}

## Los 7 motivos

1. **Cada vez navegamos más desde el celular,** y con ello aumenta la exposición a sitios y descargas maliciosas.
2. **El celular ya es parte de nuestra vida:** ahí está nuestra información personal y de trabajo.
3. **Permite localizar tu smartphone** en caso de pérdida o robo.
4. **Optimiza el uso y gasto de la batería.**
5. **Elimina archivos basura** que ocupan espacio.
6. **Evita compartir nuestra privacidad** con aplicaciones que piden más permisos de los necesarios.
7. **Crece el número de virus para Android.**

## Lo que cambió desde entonces

Android hoy incluye protecciones de fábrica como Google Play Protect, y la función "Encontrar mi dispositivo" permite localizar o borrar el teléfono sin instalar nada. Un antivirus adicional puede sumar, pero lo que más protege es el hábito:

- Descarga apps solo de Google Play y revisa los permisos que piden.
- Mantén el sistema y las apps actualizados.
- Activa el bloqueo de pantalla y la verificación en dos pasos en tus cuentas.
- Desconfía de enlaces por SMS o WhatsApp que piden datos o te apuran.

## Si usas el celular para trabajar

Para una empresa, un celular robado puede ser una fuga de datos de clientes. Define reglas mínimas para el equipo: bloqueo de pantalla, cuentas con verificación en dos pasos y la posibilidad de cerrar sesiones de forma remota. Más en estas [buenas prácticas de seguridad en redes sociales]({S}/infografia-buenas-practicas-para-la-seguridad-de-la-informacion-en-la-gestion-de-redes-sociales/).
""",
faq=[
("¿Es necesario un antivirus en Android?", "Android incluye protecciones como Google Play Protect, pero un antivirus puede sumar seguridad. Lo más importante es descargar apps solo de fuentes oficiales, actualizar el sistema y revisar permisos."),
("¿Cómo localizar un celular Android perdido?", "Con la función Encontrar mi dispositivo de Google, que permite ubicarlo, hacerlo sonar o borrar sus datos de forma remota."),
("¿Qué riesgos tiene usar el celular para trabajar?", "Si se pierde o lo roban sin protección, puede exponer datos de clientes y accesos de la empresa. Conviene usar bloqueo de pantalla, verificación en dos pasos y cierre remoto de sesiones."),
],
related=[("Seguridad en redes sociales", S + "/infografia-buenas-practicas-para-la-seguridad-de-la-informacion-en-la-gestion-de-redes-sociales/"), ("Más infografías", HUB_INFO)],
),

dict(
id=2048, slug="infografia-como-implementar-big-data-en-tu-empresa",
title="Cómo implementar big data en tu empresa (infografía)",
excerpt="Infografía de cómo implementar big data en tu empresa en 7 pasos: conocer sus posibilidades, modelos analíticos, KPIs, limpieza de datos, fuentes y herramientas.",
img_alt="Infografía de cómo implementar big data en tu empresa",
credit="Infografía: Sage.",
body=f"""
"Big data" suena a algo para Amazon o los bancos. Pero cualquier empresa genera datos todos los días: ventas, clientes, visitas al sitio, cotizaciones. La pregunta es si los usas para decidir o solo los acumulas.

Esta infografía propone siete pasos para implementar big data sin complicarte.

{{IMG}}

## Los 7 pasos

1. **Conoce sus posibilidades.** Directivos y empleados deben entender qué es y cómo puede ayudar a los objetivos del negocio.
2. **Modelos analíticos.** Aprende a analizar los datos para encontrar patrones de comportamiento y adelantarte a lo que buscan tus clientes.
3. **Define nuevos KPIs.** ¿Qué necesitas saber para actuar en función de tus objetivos?
4. **Haz una buena limpieza.** Quédate con los datos útiles y descarta los duplicados, incompletos o inexistentes.
5. **Piensa dónde recopilarás los datos.** Además de tu operación diaria, hay fuentes que quizá no consideras: intranet, repositorios, etc. Haz una lista y conéctalas.
6. **Elige la herramienta.** Necesitas un software para recopilar, analizar y reportar. La infografía, elaborada por Sage, menciona su solución Sage Live integrada con Salesforce.
7. **No rompas el banco.** Hay alternativas para cualquier tamaño y presupuesto, incluso con pago mensual.

## Versión pyme

No necesitas un equipo de científicos de datos para empezar:

- **Un CRM** como fuente única de clientes y oportunidades.
- **Google Analytics 4** para tu sitio.
- **Una hoja de cálculo o un tablero** que reúna 5 a 10 indicadores.
- **Una revisión mensual** en la que cada dato lleve a una decisión.

El error más común no es tener pocos datos. Es tener muchos y no saber qué pregunta responden. Empieza por estos [KPIs para tu sitio web]({KPIS}) y por ordenar tus [operaciones de marketing]({S}/por-que-implementar-procesos-de-marketing-dentro-de-tu-empresa/).
""",
faq=[
("¿Cómo implementar big data en una empresa?", "Entendiendo sus posibilidades, definiendo qué indicadores necesitas, limpiando los datos, identificando todas las fuentes, eligiendo una herramienta adecuada y empezando con un presupuesto acorde a tu tamaño."),
("¿Una pyme puede usar big data?", "Sí, a su escala: con un CRM, analítica web y un tablero de indicadores que se revise periódicamente para tomar decisiones."),
("¿Por qué es importante limpiar los datos?", "Porque los datos duplicados, incompletos o erróneos llevan a conclusiones equivocadas."),
],
related=[("KPIs para tu sitio web", KPIS), ("Operaciones de marketing", S + "/por-que-implementar-procesos-de-marketing-dentro-de-tu-empresa/")],
),

dict(
id=1452, slug="infografia-puesto-de-trabajo-compartido-germenes-compartidos",
title="Puesto de trabajo compartido: gérmenes compartidos",
excerpt="Infografía sobre gérmenes en el puesto de trabajo: cuántas bacterias hay en un escritorio, cómo se transmiten las infecciones y cómo mantener limpia la oficina.",
img_alt="Infografía sobre gérmenes y bacterias en el puesto de trabajo compartido",
body=f"""
Tu escritorio puede tener más bacterias de las que te imaginas. Y si lo compartes con otros turnos o compañeros, compartes también lo que dejan ahí.

Esta infografía muestra por qué la limpieza del puesto de trabajo importa más de lo que parece.

{{IMG}}

## Lo que dice la infografía

- **El 80% de las infecciones puede transmitirse por contacto.**
- **Los trabajadores entran en contacto con millones de bacterias al día.**
- **Los puestos de trabajo son grandes almacenes de gérmenes:** los restos que se acumulan en las mesas son un entorno ideal para bacterias y hongos.
- **Hay miles de gérmenes por centímetro cuadrado** en superficies de uso diario como el teclado.
- **El 39% de los trabajadores no se lava las manos** después de estornudar, toser o sonarse.
- **Los agentes antimicrobianos** son cada vez más relevantes para reducir gérmenes en las superficies que más se tocan.

## Medidas sencillas para la oficina

1. **Limpia teclado, mouse, teléfono y escritorio** con regularidad, sobre todo si se comparten.
2. **Pon gel antibacterial** a la vista en áreas comunes.
3. **No comas sobre el teclado.** Las migajas son alimento para bacterias.
4. **Si estás enfermo, quédate en casa** o trabaja a distancia si es posible.
5. **Ventila los espacios.**

## Para quien dirige equipos

Un equipo enfermo es un equipo que no entrega. Facilitar la limpieza, permitir el trabajo remoto cuando alguien está enfermo y cuidar los espacios comunes es parte de una buena cultura laboral, y también de tu [marca empleadora]({S}/employer-branding/).
""",
faq=[
("¿Cuántas bacterias hay en un escritorio de oficina?", "Según la infografía, miles de gérmenes por centímetro cuadrado en superficies de uso diario como el teclado, y los trabajadores entran en contacto con millones de bacterias al día."),
("¿Cómo se transmiten las infecciones en la oficina?", "Principalmente por contacto: la infografía señala que hasta el 80% de las infecciones puede transmitirse así, por ejemplo al tocar superficies compartidas."),
("¿Cómo mantener limpio un puesto de trabajo compartido?", "Limpiando teclado, mouse, teléfono y escritorio con regularidad, usando gel antibacterial, evitando comer sobre el teclado y quedándose en casa cuando se está enfermo."),
],
related=[("Employer branding", S + "/employer-branding/"), ("Más infografías", HUB_INFO)],
),

dict(
id=2267, slug="infografia-paso-a-paso-de-una-campana-publicitaria-en-google",
title="Campaña en Google Ads paso a paso (infografía)",
excerpt="Infografía con el paso a paso de una campaña publicitaria en Google: objetivos, tipos de anuncio, palabras clave, página de aterrizaje, presupuesto, medición y optimización.",
img_alt="Infografía del paso a paso de una campaña publicitaria en Google",
credit="Infografía: Publicar.",
body=f"""
Google Ads puede ser la mejor inversión de tu marketing o la forma más rápida de quemar dinero. La diferencia casi siempre está en el proceso.

Esta infografía resume los pasos de una campaña publicitaria en Google (cuando se hizo, la plataforma se llamaba Google AdWords).

{{IMG}}

## Los pasos de la infografía

1. **Definir objetivos.** Traducir los intereses del negocio en objetivos claros y alcanzables.
2. **Elegir el tipo de anuncio:** en resultados de búsqueda, en sitios de internet (red de display) o en videos de YouTube.
3. **Seleccionar las palabras clave.** Es todo un arte: de ellas depende gran parte del éxito o fracaso de la inversión, así que hay que investigar a fondo.
4. **Analizar y optimizar la página de aterrizaje.** ¿Tiene contenido relacionado con el anuncio? ¿Se ve bien en celular y computadora? ¿Su diseño es atractivo?
5. **Definir el presupuesto.** Dependiendo de él, llegarás a más o menos personas.
6. **Medir.** Los primeros resultados significativos llegan alrededor de un mes después: cuántos clics, quiénes lo vieron, qué días y horas rinden más.
7. **Optimizar.** Ajustar con base en los resultados para mejorarlos.

## Consejos actualizados

- **Mide conversiones, no clics.** Configura el seguimiento de formularios, llamadas y clics a WhatsApp antes de gastar el primer peso.
- **Empieza con búsqueda.** Captas a quien ya busca lo que vendes. Display y YouTube funcionan mejor para dar a conocer o recordar.
- **Usa palabras clave negativas** para no pagar por búsquedas que no te sirven.
- **Una página de aterrizaje por intención.** Si el anuncio habla de "contabilidad para pymes", la página también.

Si quieres entender cuándo conviene invertir en anuncios, lee [por qué hacer campañas en buscadores]({BUSCADORES}).
""",
faq=[
("¿Cuáles son los pasos para crear una campaña en Google Ads?", "Definir objetivos, elegir el tipo de anuncio, seleccionar palabras clave, optimizar la página de aterrizaje, establecer el presupuesto, medir resultados y optimizar."),
("¿Cuánto tarda en dar resultados una campaña en Google?", "Los anuncios se muestran casi de inmediato, pero según la infografía los datos significativos para optimizar llegan alrededor de un mes después."),
("¿Google AdWords es lo mismo que Google Ads?", "Sí. Google AdWords cambió su nombre a Google Ads en 2018."),
],
related=[("Por qué hacer campañas en buscadores", BUSCADORES), ("Herramientas de Google para tu web", S + "/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/")],
),

dict(
id=1637, slug="infografia-outbound-marketing-vs-inbound-marketing",
title="Outbound vs. inbound marketing: diferencias (infografía)",
excerpt="Infografía outbound marketing vs inbound marketing: interrumpir o atraer, medios tradicionales o contenido, presupuesto o creatividad. Cuál le conviene a tu empresa.",
img_alt="Infografía de outbound marketing vs inbound marketing",
body=f"""
Hay dos formas de conseguir clientes: ir a buscarlos interrumpiendo lo que hacen, o lograr que ellos te encuentren cuando lo necesitan.

La primera es outbound marketing. La segunda, inbound. Esta infografía las compara.

{{IMG}}

## Las diferencias según la infografía

**Outbound marketing**
- Interrumpe al usuario.
- Usa medios tradicionales.
- Se centra en el cliente potencial al que quiere llegar, lo busque o no.

**Inbound marketing**
- Atrae y enamora al cliente.
- Se dirige al público interesado.
- Usa menos presupuesto y más creatividad.

## Cómo se ve en la práctica

| | Outbound | Inbound |
| --- | --- | --- |
| Ejemplos | Anuncios en TV y radio, llamadas en frío, volantes, espectaculares | Blog, SEO, guías descargables, redes sociales, email con permiso |
| Quién inicia | La marca | El cliente |
| Costo en el tiempo | Pagas cada vez que quieres exposición | El contenido sigue atrayendo visitas mucho después |
| Medición | Difícil en medios tradicionales | Detallada: visitas, prospectos, ventas |

## ¿Hay que elegir uno?

No necesariamente. El outbound bien enfocado (por ejemplo, prospección a cuentas específicas en B2B o anuncios en buscadores) puede acelerar resultados. El inbound construye un activo que trabaja para ti a largo plazo y reduce tu costo por cliente.

La combinación más común en pymes: contenido y SEO como base, y publicidad pagada para acelerar lo que ya funciona.

Para entender la metodología completa, lee [qué es el inbound marketing]({GUIA}) y [las 4 fases del inbound marketing]({FASES}).
""",
faq=[
("¿Qué diferencia hay entre outbound e inbound marketing?", "El outbound interrumpe al usuario con mensajes en medios tradicionales; el inbound atrae a personas interesadas con contenido útil para que ellas encuentren a la marca."),
("¿Cuál es más barato, inbound u outbound?", "El inbound suele requerir menos presupuesto y más creatividad, y su contenido sigue generando resultados con el tiempo, mientras que en outbound pagas por cada exposición."),
("¿Se pueden combinar inbound y outbound?", "Sí. Muchas empresas usan contenido y SEO como base y publicidad o prospección directa para acelerar resultados."),
],
related=[("Qué es el inbound marketing", GUIA), ("Las 4 fases del inbound marketing", FASES)],
),

dict(
id=6814, slug="infografia-metoo-en-el-mundo-periodistico",
title="#MeToo en el periodismo mexicano (infografía)",
excerpt="Infografía #MeToo en el mundo periodístico: resultados del sondeo de Periodistas Unidas Mexicanas sobre acoso sexual en los medios y qué deben hacer las empresas.",
img_alt="Infografía #MeToo en el mundo periodístico, acoso en los medios de comunicación",
credit="Infografía con datos del sondeo del colectivo Periodistas Unidas Mexicanas.",
body=f"""
En 2019, el movimiento #MeToo llegó con fuerza a México, y el periodismo fue uno de los gremios donde más testimonios salieron a la luz.

Esta infografía resume un sondeo sobre acoso en los medios de comunicación.

{{IMG}}

## Lo que muestra la infografía

El colectivo Periodistas Unidas Mexicanas realizó un sondeo con 392 mujeres entre el 6 y el 22 de febrero.

- **60%** respondió que sí ha vivido o está viviendo una situación de acoso, hostigamiento o agresión sexual en su trabajo, dentro o fuera de las instalaciones.

Las tres formas de violencia más señaladas fueron:

1. Comentarios sobre la vestimenta o sobre cómo luce en el día a día (71%).
2. Miradas lascivas (64%).
3. Comentarios sexuales sobre su persona o en doble sentido que incomodan (52%).

## Lo que deben hacer las empresas

El acoso no es un problema de un gremio, y prevenirlo es también una obligación. En México, la NOM-035 de la Secretaría del Trabajo y Previsión Social obliga a identificar y prevenir factores de riesgo psicosocial, y la Ley Federal del Trabajo prohíbe el hostigamiento y el acoso sexual.

Medidas básicas:

1. **Una política clara** contra el acoso, conocida por todos.
2. **Canales de denuncia confiables,** que protejan a quien denuncia.
3. **Investigación y sanciones reales.** Una política que no se aplica comunica lo contrario.
4. **Capacitación,** sobre todo para quienes dirigen equipos.

Un lugar de trabajo seguro es la base de cualquier cultura sana y de una buena [marca empleadora]({S}/employer-branding/).
""",
faq=[
("¿Qué reveló el sondeo de Periodistas Unidas Mexicanas?", "Que el 60% de las 392 mujeres encuestadas había vivido o vivía una situación de acoso, hostigamiento o agresión sexual en su trabajo."),
("¿Cuáles fueron las formas de acoso más señaladas?", "Comentarios sobre la vestimenta o la apariencia (71%), miradas lascivas (64%) y comentarios sexuales o en doble sentido (52%)."),
("¿Qué obligaciones tienen las empresas en México frente al acoso?", "La Ley Federal del Trabajo prohíbe el hostigamiento y el acoso sexual, y la NOM-035 obliga a identificar y prevenir factores de riesgo psicosocial. Conviene tener una política, canales de denuncia y sanciones claras."),
],
related=[("Employer branding", S + "/employer-branding/"), ("Más infografías", HUB_INFO)],
),

dict(
id=4433, slug="infografia-gestion-de-proyectos-en-el-pasado-y-en-la-actualidad",
title="Gestión de proyectos: antes y ahora (infografía)",
excerpt="Infografía de la gestión de proyectos en el pasado y la actualidad: de cascada a ágil, de herramientas de escritorio a la nube y de equipos locales a equipos remotos.",
img_alt="Infografía de la gestión de proyectos en el pasado y en la actualidad",
body=f"""
Los pasos para planear y ejecutar un proyecto no cambiaron mucho desde las pirámides. Lo que sí cambió, y mucho, son las herramientas, los equipos y la forma de trabajar.

Esta infografía compara la gestión de proyectos de antes con la de ahora.

{{IMG}}

## Antes vs. ahora

| Antes | Ahora |
| --- | --- |
| La gestión de proyectos era una responsabilidad extra de empleados de tiempo completo | Es un cargo distintivo: las empresas contratan gestores especializados |
| Los gestores simplemente ejecutaban lo que recibían | Son estrategas: llevan el proyecto desde la justificación de negocio hasta la entrega |
| Era una ciencia: cuadrar programas y presupuestos | Es ciencia y arte: liderazgo, colaboración y flexibilidad |
| Proceso en cascada, secuencial | Procesos ágiles e iterativos que se adaptan al cliente |
| Herramientas de escritorio caras y técnicas | Herramientas en la nube, multiplataforma y fáciles de usar |
| Equipos en un mismo lugar y horario | Equipos remotos, con distintos idiomas, culturas y zonas horarias |
| Juntas de estado programadas | Actualizaciones virtuales en tiempo real |
| Gestión en solitario | Colaboración constante |
| Éxito = cumplir requisitos, tiempo y presupuesto | Éxito = valor para el negocio y el cliente |

## Lo que puedes aplicar mañana

1. **Un tablero visible** (Trello, Asana, Monday o similar) donde todos vean qué sigue y quién lo hace.
2. **Entregas cortas.** Mejor algo pequeño cada dos semanas que todo al final.
3. **Juntas breves y frecuentes** en lugar de reportes largos.
4. **Un dueño por tarea,** con fecha.

Los proyectos de marketing también se benefician de esto. Revisa cómo ordenar tus [operaciones de marketing]({S}/por-que-implementar-procesos-de-marketing-dentro-de-tu-empresa/).
""",
faq=[
("¿Cómo ha cambiado la gestión de proyectos?", "Pasó de ser una tarea extra a un cargo especializado, de procesos en cascada a métodos ágiles, de herramientas de escritorio a la nube y de equipos locales a equipos remotos que colaboran en tiempo real."),
("¿Qué diferencia hay entre metodología en cascada y ágil?", "La cascada avanza por fases secuenciales con entregables definidos desde el inicio; la ágil trabaja en ciclos cortos e iterativos que se ajustan a las necesidades cambiantes del cliente."),
("¿Qué herramientas se usan hoy para gestionar proyectos?", "Herramientas en la nube como Trello, Asana, Monday, Jira o ClickUp, que permiten ver tareas, responsables y avances en tiempo real."),
],
related=[("Operaciones de marketing", S + "/por-que-implementar-procesos-de-marketing-dentro-de-tu-empresa/"), ("Liderazgo situacional", S + "/infografia-liderazgo-situacional/")],
),

dict(
id=2113, slug="infografia-alojamiento-en-hostales-guia-de-supervivencia",
title="Hostales: guía de supervivencia para viajeros",
excerpt="Infografía con una guía para elegir hostal: eventos diarios, áreas comunes, ubicación céntrica, habitaciones femeninas, lockers y wifi, más lo que enseña a los negocios turísticos.",
img_alt="Infografía de alojamiento en hostales, guía de supervivencia",
credit="Infografía: Genis Viajera.",
body=f"""
Un hostal puede ser la mejor parte de tu viaje o la anécdota que cuentas para que nadie repita tu error. Todo depende de cómo lo eliges.

Esta infografía resume qué buscar.

{{IMG}}

## Qué buscar en un hostal

- **Eventos diarios.** Noches temáticas, música en vivo, recorridos: cualquier evento es buena excusa para conocer gente.
- **Área común.** Un espacio para compartir una comida, planear el día o platicar. Si es una alberca, mejor.
- **Ubicación céntrica.** Facilita moverte y tener cerca tiendas y restaurantes; si está cerca de una estación de tren o autobús, todavía mejor.
- **Habitaciones femeninas.** Las mixtas funcionan, pero tener la opción es importante para quien no se siente cómoda compartiendo con desconocidos.
- **Lockers.** Seguridad ante todo: guarda bajo llave pasaporte, documentos y objetos de valor.
- **Wifi.** Para quien no compra chip local, sobran explicaciones.

La infografía también recomienda algunos hostales en ciudades como Río de Janeiro, Lisboa, Sídney, Chile, Ciudad del Cabo y Vietnam.

## Lo que aprende un negocio turístico de esta lista

Si tienes un hostal, hotel o cualquier hospedaje, esta lista es literalmente lo que tu cliente busca. Úsala así:

1. **Pon estos atributos en tus fotos y descripciones,** no escondidos en el texto.
2. **Muestra la experiencia, no solo la cama.** Los eventos y áreas comunes venden.
3. **Responde reseñas** que mencionen seguridad y limpieza: son las que más pesan.
4. **Facilita la reserva directa** con algún beneficio extra.

Más ideas en [inbound marketing para hoteles]({S}/inbound-marketing-para-hoteles/).
""",
faq=[
("¿Qué debo buscar al elegir un hostal?", "Ubicación céntrica, áreas comunes, eventos para conocer gente, lockers para tus pertenencias, wifi y, si lo prefieres, habitaciones femeninas."),
("¿Los hostales son seguros?", "Pueden serlo si eliges uno con buenas reseñas, lockers para guardar documentos y objetos de valor, y opciones de habitación que te hagan sentir cómodo."),
("¿Cómo puede un hostal atraer más huéspedes?", "Mostrando en fotos y descripciones lo que los viajeros buscan (ubicación, áreas comunes, eventos, seguridad), respondiendo reseñas y facilitando la reserva directa."),
],
related=[("Inbound marketing para hoteles", S + "/inbound-marketing-para-hoteles/"), ("Turismo y transformación digital", S + "/infografia-turismo-y-transformacion-digital/")],
),

dict(
id=2219, slug="infografia-que-es-un-influencer-en-medios-sociales",
title="Qué es un influencer en redes sociales (infografía)",
excerpt="Infografía de qué es un influencer en redes sociales: quiénes son, qué hacen, cómo ganan dinero, qué buscar en uno y cómo conectar con influencers para tu marca.",
img_alt="Infografía de qué es un influencer en medios sociales",
credit="Infografía en inglés: IZEA.",
body=f"""
Mientras los anuncios tradicionales en TV y radio perdían terreno, una opción más joven empezó a crecer: el marketing de influencers.

Esta infografía (en inglés, elaborada por IZEA) explica qué es un influencer en redes sociales y cómo trabajar con uno. Aquí la tienes resumida en español.

{{IMG}}

## Qué es el marketing de influencers

Consiste en unir a marcas con personas que tienen audiencias grandes y confiables en redes como Facebook, Instagram, X (antes Twitter) o Pinterest, para promover productos ante clientes nuevos y actuales a través de los canales del influencer.

## Quiénes son

Íconos de redes sociales con muchos seguidores y credibilidad en un nicho: youtubers, blogueros, expertos de la industria, activistas, celebridades y entusiastas.

## Qué hacen

Colaboran con marcas en campañas para aumentar el conocimiento de marca y las ventas:

- Contenido sobre un producto o servicio para sus lectores o seguidores.
- Reseñas, concursos, sorteos, cupones, historias personales y videos.
- Difusión en varios canales a la vez.

## Cómo ganan dinero

Las marcas les pagan con dinero, con productos gratuitos o con ambos.

## Qué buscar en un influencer

- **Alto engagement:** que su audiencia esté activa.
- **Contenido de calidad:** que no sea uno más del montón.
- **Afinidad con tu marca:** que su estilo y su público encajen contigo.

## Cómo conectar con ellos

La infografía sugiere usar marketplaces de creadores para encontrar a los indicados. También puedes trabajar con agencias de influencers o contactarlos directamente.

Antes de contratar, define a quién quieres llegar con tu [buyer persona]({BUYER}) y conoce los [6 tipos de influencers]({S}/infografia-6-tipos-de-influencers/).
""",
faq=[
("¿Qué es un influencer en redes sociales?", "Es una persona con muchos seguidores y credibilidad en un nicho, que colabora con marcas para promover productos o servicios entre su audiencia."),
("¿Cómo ganan dinero los influencers?", "Las marcas les pagan con dinero, con productos gratuitos o con ambos, a cambio de contenido, reseñas, concursos o cupones."),
("¿Qué buscar en un influencer para mi marca?", "Que tenga una audiencia activa, contenido de calidad y afinidad con tu marca y con tu cliente ideal."),
],
related=[("6 tipos de influencers", S + "/infografia-6-tipos-de-influencers/"), ("Qué es un buyer persona", BUYER)],
),

dict(
id=1661, slug="infografia-tecnologias-de-energia-solar",
title="Tecnologías de energía solar: cómo funcionan (infografía)",
excerpt="Infografía de tecnologías de energía solar: cómo se obtiene, cómo funciona un sistema en casa, grandes proyectos y gadgets solares, con ideas para empresas.",
img_alt="Infografía de tecnologías de energía solar",
body=f"""
El sol ha sido fuente de energía desde que alguien encendió la primera fogata. Hoy alimenta casas, empresas, satélites y hasta mochilas.

Esta infografía explica cómo funciona la energía solar y algunos usos curiosos.

{{IMG}}

## Dos formas de obtener energía solar

1. **Con espejos** que concentran los rayos en un receptor de calor; este genera vapor que mueve una turbina y produce electricidad.
2. **Con paneles fotovoltaicos,** formados por celdas que transforman la luz (fotones) en energía eléctrica (electrones).

## Cómo funciona en una casa

1. Los paneles captan los rayos solares.
2. Generan corriente directa (DC) que pasa al controlador de carga.
3. La energía se almacena en un banco de baterías.
4. Un inversor convierte la corriente directa en alterna (AC).
5. La energía se distribuye por toda la casa.
6. Si hace falta, se complementa con la red eléctrica tradicional.

Muchos sistemas actuales se conectan directamente a la red y usan medición neta, sin baterías.

## Proyectos y gadgets de la infografía

- Una gran planta solar en Arizona que se extiende por miles de hectáreas.
- Los proyectos solares de Google en California y Project Sunroof, que calcula cuánta energía puede generar tu techo.
- Gadgets como un candado inteligente para bicicleta, un teclado solar de Logitech, una bocina Bluetooth recargable con sol, una mochila solar y linternas solares.

## Para empresas

Para muchos negocios, la energía solar es una forma de bajar costos fijos, y también un mensaje de marca. Si la instalas, cuéntalo con datos concretos (cuánto ahorras, cuánto CO₂ evitas). Y si vendes paneles, esta es la clase de contenido educativo que atrae clientes: explica, compara y responde dudas antes de vender. Eso es [inbound marketing]({GUIA}).
""",
faq=[
("¿Cómo se obtiene la energía solar?", "Con espejos que concentran los rayos para generar vapor y mover una turbina, o con paneles fotovoltaicos que transforman la luz en electricidad."),
("¿Cómo funciona un sistema de energía solar en casa?", "Los paneles generan corriente directa, que pasa por un controlador de carga, puede almacenarse en baterías y un inversor la convierte en corriente alterna para usarla en la casa."),
("¿Conviene la energía solar a una empresa?", "Puede reducir costos fijos de electricidad y mejorar la imagen de marca. Conviene evaluar consumo, inversión y tiempo de recuperación con un proveedor."),
],
related=[("Qué es el inbound marketing", GUIA), ("Más infografías", HUB_INFO)],
),
]
