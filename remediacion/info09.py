from comun import *

POSTS = [
dict(
id=2171, slug="infografia-perfil-de-trabajador-peruano",
title="Perfil del trabajador peruano (infografía)",
excerpt="Infografía del perfil del trabajador peruano: edad, educación, ingreso promedio, informalidad, seguro de salud, pensiones y mercado laboral, con datos del INEI de 2017.",
img_alt="Infografía del perfil del trabajador peruano",
credit="Infografía: RPP Noticias (Estrella Contreras), con datos del INEI y el Ministerio de Trabajo, 2017.",
body=f"""
¿Cómo es el trabajador promedio en Perú? Esta infografía de RPP Noticias, con datos del INEI y el Ministerio de Trabajo de 2017, lo retrata en pocas cifras. Y muchas te van a sonar familiares si trabajas en México o en cualquier país de América Latina.

{{IMG}}

## Quién es

- **83%** tiene más de 25 años.
- **82%** tiene secundaria completa o educación superior.
- **81.7%** trabaja en un solo lugar.

## Ingreso y prestaciones

- **Ingreso promedio a nivel nacional:** S/1,366 (soles).
- **60%** no tiene tarjeta de ahorros ni de crédito.
- **75%** no recibe CTS (compensación por tiempo de servicio).
- **68%** no está afiliado a una AFP (administradora de fondos de pensiones).
- **75%** trabaja más de 48 horas a la semana.

## Condiciones de trabajo

- **77%** tiene algún seguro de salud (SIS, EsSalud o EPS).
- **75%** trabaja de manera informal.

## Mercado laboral

- **65%** labora en empresas de 1 a 10 trabajadores.
- **69%** trabaja en el sector comercio y servicios.
- **85%** son obreros o empleados.

## La lectura regional

La informalidad, las jornadas largas y el peso de las microempresas son rasgos comunes en América Latina. México comparte buena parte de ese panorama: más de la mitad de su población ocupada trabaja en la informalidad, según el INEGI.

Para una empresa, esto tiene dos lecturas:

1. **Ofrecer formalidad y prestaciones es una ventaja para atraer talento.** Lo vuelve parte de tu [marca empleadora]({S}/employer-branding/).
2. **Tu cliente probablemente es una microempresa** o trabaja en una. Productos simples, pagos flexibles y atención cercana suelen funcionar mejor que soluciones pensadas para corporativos.
""",
faq=[
("¿Cuál era el ingreso promedio del trabajador peruano?", "Según la infografía, con datos de 2017, el ingreso promedio a nivel nacional era de S/1,366."),
("¿Qué porcentaje de trabajadores peruanos es informal?", "La infografía indica que el 75% trabajaba de manera informal."),
("¿Dónde trabaja la mayoría de los peruanos?", "El 65% labora en empresas de 1 a 10 trabajadores y el 69% en el sector comercio y servicios."),
],
related=[("Employer branding", S + "/employer-branding/"), ("Barreras que frenan a las mipymes", S + "/infografia-barreras-culturales-legales-y-economicas-que-afectan-a-las-mipymes-infografia/")],
),

dict(
id=6924, slug="infografia-industria-de-videojuegos-en-mexico-2018",
title="La industria de videojuegos en México 2018 (infografía)",
excerpt="Infografía del mercado de videojuegos en México en 2018: valor de 27,032 millones de pesos, venta de consolas y juegos, eSports y juego en línea, con datos de The CIU.",
img_alt="Infografía de la industria de videojuegos en México en 2018",
credit="Infografía: Panda Ancha, con información de The CIU.",
body=f"""
Los videojuegos dejaron de ser cosa de niños hace mucho. En México son una industria de miles de millones de pesos, con jugadores de todas las edades y una audiencia que también consume torneos y transmisiones.

Esta infografía resume el mercado en 2018.

{{IMG}}

## Lo que muestra la infografía

La industria estaba en plena transformación: nuevas formas de jugar, de acceder a los juegos y de cobrar por ellos.

**Valor del mercado.** El sector gamer mexicano valió 27,032 millones de pesos, gracias a la estabilidad de precios y al aumento de jugadores.

**Segmento de consolas:** 23,220 millones de pesos en total, de los cuales 10,813 millones correspondieron a la venta de consolas y 12,408 millones a la venta de juegos.

**eSports.** El juego profesional ganaba relevancia:
- 10.6% de la audiencia ve canales de gaming en línea.
- 9% ha participado en algún torneo.
- 4.8% asiste a torneos como espectador.

**Videojuegos e internet.** 2 de cada 3 jugadores juegan en línea, y la mayoría descarga juegos gratuitos y de paga.

## Lo que pasó después

El mercado siguió creciendo, impulsado por el juego en celulares, las suscripciones y el modelo gratuito con compras dentro del juego. El juego en línea y las transmisiones en vivo se volvieron la norma.

## Oportunidades para marcas

- **Patrocinios y colaboraciones** con creadores de contenido de videojuegos, que tienen audiencias muy leales.
- **Publicidad dentro de juegos** y en plataformas de streaming.
- **Gamificación** de tus propias campañas o programas de lealtad.

Antes de entrar, define a tu público con un [buyer persona]({BUYER}): no es lo mismo un jugador casual de celular que un fanático de los eSports.
""",
faq=[
("¿Cuánto valía la industria de videojuegos en México en 2018?", "Según la infografía, con datos de The CIU, 27,032 millones de pesos."),
("¿Cuánto se vendió en consolas y juegos?", "El segmento de consolas sumó 23,220 millones de pesos: 10,813 millones por venta de consolas y 12,408 millones por venta de juegos."),
("¿Cuántos gamers mexicanos juegan en línea?", "Dos de cada tres jugadores juegan en línea, de acuerdo con la infografía."),
],
related=[("Videojuegos: beneficios vs. adicción", S + "/infografia-videojuegos-beneficios-vs-adiccion/"), ("Qué es un buyer persona", BUYER)],
),

dict(
id=5681, slug="infografia-el-papel-de-la-mujer-en-el-mundo",
title="El papel de la mujer en el mundo (infografía)",
excerpt="Infografía del papel de la mujer en el mundo: las mujeres más ricas, los países con más mujeres en el parlamento (México con 48.2%) y la persistencia del acoso sexual.",
img_alt="Infografía del papel de la mujer en el mundo",
credit="Infografía con datos de IPU, Forbes, Ipsos y Statista.",
body=f"""
Las mujeres ocupan cada vez más espacios en la política y la economía. Pero la violencia de género sigue siendo un problema global. Esta infografía, publicada en 2019, reúne ambos lados.

{{IMG}}

## Economía: las mujeres más ricas del mundo

En la lista de las 25 personas más ricas del mundo, el lugar 16 lo ocupaba Alice Walton, de Walmart. Las mujeres más ricas (en miles de millones de dólares):

1. Alice Walton (Estados Unidos): 46
2. Françoise Bettencourt Meyers (Francia): 42.2
3. Susanne Klatten (Alemania): 25
4. Jacqueline Mars (Estados Unidos): 23.6
5. Yang Huiyan (China): 21.9

## Política: países con más mujeres en el parlamento

- Ruanda: 61.3%
- Cuba: 53.2%
- Bolivia: 53.1%
- **México: 48.2%**
- Granada: 46.7%

México destacaba entre los países con mayor participación femenina en el Congreso. En los años siguientes alcanzó la paridad, y en 2024 eligió a la primera presidenta de su historia.

## La deuda pendiente: violencia y acoso

Mujeres de todo el mundo declaran haber sufrido acoso sexual desde los 15 años. Proporción por país según la infografía: Suecia 81%, Francia 75%, Gran Bretaña 68%, Estados Unidos 60% y Alemania 60%.

Los problemas más importantes que enfrentan las mujeres en México: acoso sexual (48%), violencia física (43%), violencia sexual (43%), estereotipos de género (22%) y abuso doméstico (14%).

## Qué pueden hacer las empresas

- Políticas claras contra el acoso, con canales de denuncia confiables.
- Igualdad salarial por el mismo puesto.
- Oportunidades reales de crecimiento y liderazgo.
- Flexibilidad que no penalice la maternidad ni los cuidados.

Revisa también [#MeToo en el periodismo mexicano]({S}/infografia-metoo-en-el-mundo-periodistico/).
""",
faq=[
("¿Qué país tiene más mujeres en el parlamento?", "Según la infografía, Ruanda, con 61.3%, seguido de Cuba (53.2%) y Bolivia (53.1%). México tenía 48.2%."),
("¿Quién era la mujer más rica del mundo según la infografía?", "Alice Walton, de Walmart, con 46 mil millones de dólares."),
("¿Cuáles son los principales problemas de las mujeres en México?", "Según la infografía: acoso sexual (48%), violencia física (43%), violencia sexual (43%), estereotipos de género (22%) y abuso doméstico (14%)."),
],
related=[("#MeToo en el periodismo mexicano", S + "/infografia-metoo-en-el-mundo-periodistico/"), ("Employer branding", S + "/employer-branding/")],
),

dict(
id=1549, slug="infografia-auge-y-caida-del-ipod",
title="Auge y caída del iPod (infografía)",
excerpt="Infografía del auge y caída del iPod: unidades vendidas de 2002 a 2014 y su peso en los ingresos de Apple. Por qué Apple dejó que el iPhone se comiera a su propio éxito.",
img_alt="Infografía del auge y caída del iPod, unidades vendidas y porcentaje de ingresos de Apple",
credit="Infografía: Statista, con datos de Apple.",
body=f"""
Hubo un tiempo en que el iPod era Apple. Esta gráfica cuenta cómo pasó de ser el producto estrella a desaparecer, y por qué esa caída fue en realidad una gran decisión de negocio.

{{IMG}}

## Lo que muestra la gráfica

**Unidades vendidas (millones):**
- 2002: 0.4 · 2003: 0.9 · 2004: 4.4 · 2005: 22.5
- 2006: 39.4 · 2007: 51.6 · **2008: 54.8 (máximo)** · 2009: 54.1
- 2010: 50.3 · 2011: 42.6 · 2012: 35.2 · 2013: 26.4 · 2014: 14.4

**Peso en los ingresos de Apple:** pasó de 2% en 2002 a cerca de 40% en 2006 y 2007, y cayó hasta 1% en 2014. Ese año Apple dejó de reportar las ventas del iPod por separado.

## Qué pasó

En 2007 llegó el iPhone, que hacía todo lo que hacía un iPod… y mucho más. A partir de 2008, las ventas del iPod empezaron a caer y su peso en los ingresos se desplomó. Apple dejó de vender el último iPod en 2022.

## La lección: canibalízate antes de que lo haga otro

Apple sabía que el teléfono acabaría con el reproductor de música. En lugar de proteger su producto estrella, lanzó el que lo iba a reemplazar. Si no lo hubiera hecho, lo habría hecho un competidor.

Para cualquier negocio:

- **Pregúntate qué podría volver obsoleto tu producto principal.**
- **Si puedes construirlo tú, hazlo** antes que otro.
- **No midas solo un producto:** mide la relación con el cliente. Apple perdió ventas de iPod, pero ganó clientes de iPhone.

Más sobre la marca en [Apple: ventas, ingresos y valor de marca]({S}/infografia-conoce-apple-ventas-ingresos-y-valor-de-marca-actual/).
""",
faq=[
("¿Cuándo vendió más el iPod?", "En 2008, con 54.8 millones de unidades, según la gráfica de Statista con datos de Apple."),
("¿Por qué cayeron las ventas del iPod?", "Principalmente por la llegada del iPhone en 2007, que incluía las funciones del iPod y muchas más."),
("¿Cuándo dejó Apple de vender el iPod?", "Apple dejó de reportar sus ventas en 2014 y descontinuó el último modelo, el iPod touch, en 2022."),
],
related=[("Apple: ventas y valor de marca", S + "/infografia-conoce-apple-ventas-ingresos-y-valor-de-marca-actual/"), ("Historia de Instagram", S + "/infografia-historia-de-instagram/")],
),

dict(
id=2011, slug="infografia-retrato-robot-del-comprador-online-en-europa",
title="Retrato del comprador en línea en Europa (infografía)",
excerpt="Infografía del comprador online en Europa: género, edad, sistema operativo y horas pico de compra en España, Reino Unido, Francia, Alemania, Austria e Italia.",
img_alt="Infografía del retrato robot de los consumidores online en Europa",
credit="Infografía: idealo, con datos de sus usuarios de enero a abril de 2017.",
body=f"""
¿Quién compra en línea en Europa? Esta infografía de idealo, un comparador de precios, retrata a los compradores de seis países con datos de 2017.

{{IMG}}

## Género

España era el país con mayor proporción de compradoras en línea: 46% mujeres y 54% hombres. En el resto, los hombres eran mayoría: Austria 61%, Francia 61%, Reino Unido 64%, Alemania 64% e Italia 66%.

## Edad

El grupo de 35 a 44 años era el más grande en casi todos los países (en España, 35%). Un dato curioso: en Reino Unido, los mayores de 65 compraban en línea tanto como los jóvenes de 18 a 24 (9% cada grupo).

## Sistema operativo

Android dominaba, con una excepción:
- España: 69% Android
- Italia: 64% Android
- Austria: 61% Android
- Francia: 60% Android
- Alemania: 58% Android
- **Reino Unido: 56% iOS**

## Horas pico

La infografía muestra cómo se reparten los clics a lo largo del día en cada país: la actividad crece desde la mañana, se mantiene por la tarde y en varios países alcanza su punto más alto por la noche.

## Lo que aplica a México

Aunque los datos son europeos, las preguntas son universales:

1. **¿Quién compra?** No asumas. Revisa los datos de tus clientes reales.
2. **¿Desde qué dispositivo?** En México, la mayoría compra desde el celular y con Android.
3. **¿A qué hora?** Programa tus campañas y correos para las horas en que tu cliente compra.

Revisa los [tipos de consumidor para tu tienda]({S}/infografia-tipos-de-consumidor-para-tu-tienda/) y [cómo iniciar una tienda online]({S}/como-iniciar-una-tienda-online/).
""",
faq=[
("¿Qué país europeo tiene más compradoras en línea?", "Según la infografía de idealo, España, donde el 46% de los compradores en línea eran mujeres."),
("¿Qué edad tienen los compradores en línea en Europa?", "El grupo más numeroso en casi todos los países era el de 35 a 44 años."),
("¿Android o iOS en las compras en línea?", "Android dominaba en España, Italia, Austria, Francia y Alemania; en Reino Unido predominaba iOS con 56%."),
],
related=[("Tipos de consumidor para tu tienda", S + "/infografia-tipos-de-consumidor-para-tu-tienda/"), ("Cómo iniciar una tienda online", S + "/como-iniciar-una-tienda-online/")],
),

dict(
id=1959, slug="infografia-diferencias-entre-el-diseno-web-responsive-y-el-diseno-web-adaptativo",
title="Diseño responsive vs. adaptativo (infografía)",
excerpt="Infografía de las diferencias entre diseño web responsive y adaptativo: flexibilidad, código, velocidad de carga y costo de desarrollo. Cuál conviene a tu sitio hoy.",
img_alt="Infografía de las diferencias entre diseño web responsive y diseño web adaptativo",
credit="Infografía: @RosanaRosas17. Hecha con Piktochart.",
body=f"""
Tu sitio se ve en celulares, tablets, laptops y pantallas enormes. Hay dos formas de lograr que se vea bien en todos: el diseño responsive y el adaptativo. Esta infografía las compara.

{{IMG}}

## Diseño responsive

- Un solo diseño para todos los dispositivos.
- Usa layouts flexibles y *media queries*.
- Los tamaños se definen en valores proporcionales.
- Es flexible: se redimensiona a cualquier resolución.
- El código es más complejo.
- Puede tardar más en cargar, sobre todo en celulares.
- El costo de desarrollo es menor.

## Diseño adaptativo

- Diseños distintos según el tamaño del dispositivo.
- Usa componentes de *progressive enhancement*.
- Tamaños de pantalla fijos y preestablecidos.
- Es menos flexible: no se ajusta exactamente a cualquier resolución.
- El código es más sencillo.
- La carga puede ser más rápida.
- El costo es mayor, porque pagas varios diseños.

## Cuál conviene hoy

Para la gran mayoría de los sitios, **responsive**. Es el estándar, lo que recomienda Google y lo que usan prácticamente todos los temas de WordPress y los constructores de sitios. Las técnicas actuales (imágenes adaptables, carga diferida, CSS moderno) resolvieron buena parte de los problemas de velocidad que menciona la infografía.

El adaptativo puede tener sentido en casos específicos, como aplicaciones web muy complejas que necesitan experiencias distintas en móvil y escritorio.

## Revisión rápida de tu sitio

1. Ábrelo en tu celular: ¿se lee sin hacer zoom?
2. ¿Los botones se pueden tocar con el dedo sin equivocarte?
3. ¿Carga rápido con datos móviles? Mídelo con PageSpeed Insights.
4. ¿El formulario o botón de WhatsApp está a la vista?

Más en [herramientas de Google para optimizar tu web]({S}/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/) y [accesibilidad web]({S}/infografia-accesibilidad-web/).
""",
faq=[
("¿Qué diferencia hay entre diseño responsive y adaptativo?", "El responsive usa un solo diseño flexible que se ajusta a cualquier pantalla; el adaptativo usa varios diseños fijos según el tamaño del dispositivo."),
("¿Qué es mejor, responsive o adaptativo?", "Para la mayoría de los sitios, el responsive: es el estándar actual, más económico y recomendado por Google."),
("¿Cómo saber si mi sitio es responsive?", "Ábrelo en distintos dispositivos o reduce la ventana del navegador: si el contenido se reacomoda sin necesidad de zoom ni desplazamiento lateral, es responsive."),
],
related=[("Herramientas de Google para tu web", S + "/infografia-herramientas-de-google-para-optimizar-tu-pagina-web/"), ("Accesibilidad web", S + "/infografia-accesibilidad-web/")],
),

dict(
id=7509, slug="infografia-dia-de-la-tierra",
title="Día de la Tierra: cuidemos nuestra casa (infografía)",
excerpt="Infografía del Día de la Tierra con acciones para cuidar el planeta: ahorrar agua y energía, reducir plásticos de un solo uso, reciclar y elegir empresas responsables.",
img_alt="Infografía del Día de la Tierra, cuidemos nuestra gran casa",
credit="Infografía: Perú21.",
body=f"""
Cada 22 de abril se celebra el Día de la Tierra. Esta infografía de Perú21 reúne acciones sencillas para cuidar el planeta desde casa y en el día a día.

{{IMG}}

## Las acciones

**Agua y energía**
- Que las duchas duren entre 5 y 10 minutos.
- Cierra la llave mientras te enjabonas o te lavas los dientes.
- Usa la lavadora y el lavavajillas solo con carga completa.
- Apaga las luces que no usas y elige focos ahorradores.

**Plásticos y residuos**
- Usa tu mochila o bolsa propia en lugar de bolsas desechables.
- Cambia rastrillos y cepillos de plástico desechables por alternativas de menor impacto.
- Di no a popotes, vasos y platos de un solo uso: según la infografía, el 50% de los residuos plásticos son de un solo uso.
- Lleva tu propio termo para el agua.
- Recicla papel, plástico y aluminio, y apuesta por productos de segunda mano como ropa y muebles.

**Hábitos y consumo**
- Usa bicicleta o transporte público.
- Pide tus facturas por correo electrónico.
- Comparte información útil sobre el cambio climático.
- Al comprar, fíjate si la empresa está comprometida con el medio ambiente.

La infografía también recuerda que el 70% de las emisiones de gases de efecto invernadero provienen de las ciudades, y que Lima y Callao generaban 886 toneladas de residuos plásticos al día, el 46% de todo Perú.

## Lo que puede hacer una empresa

- Facturación y documentos digitales.
- Menos empaques y materiales más responsables (revisa [packaging sustentable]({S}/infografia-packaging-sustentable/)).
- Políticas de ahorro de energía en oficinas.
- Comunicar lo que haces con datos concretos, sin exagerar.

Cada vez más clientes, como dice la infografía, eligen empresas comprometidas con el ambiente.
""",
faq=[
("¿Cuándo es el Día de la Tierra?", "Se celebra cada 22 de abril."),
("¿Qué puedo hacer para cuidar el planeta?", "Ahorrar agua y energía, evitar plásticos de un solo uso, reciclar, usar transporte público o bicicleta y preferir empresas comprometidas con el ambiente."),
("¿Qué pueden hacer las empresas por el medio ambiente?", "Digitalizar documentos, reducir empaques, ahorrar energía y comunicar con datos concretos sus acciones ambientales."),
],
related=[("Packaging sustentable", S + "/infografia-packaging-sustentable/"), ("Tecnologías de energía solar", S + "/infografia-tecnologias-de-energia-solar/")],
),

dict(
id=1390, slug="infografia-como-identificar-noticias-falsas-en-facebook",
title="Cómo identificar noticias falsas (infografía)",
excerpt="Infografía para identificar noticias falsas en Facebook: titulares, fuente, fotos, evidencia, URL, formato, fechas y otros reportes. 10 señales antes de compartir.",
img_alt="Infografía de cómo identificar noticias falsas en Facebook",
body=f"""
Antes de compartir esa noticia que te indignó, respira. Las noticias falsas están diseñadas justamente para eso: para que reacciones antes de pensar.

Esta infografía da diez consejos para identificarlas.

{{IMG}}

## Los 10 consejos

1. **Sé escéptico con los titulares.** Las noticias falsas suelen tener títulos llamativos. Si parece demasiado increíble, probablemente no es cierto.
2. **Investiga la fuente.** Asegúrate de que venga de un medio confiable. Revisa la sección "Acerca de".
3. **Considera las fotos.** Suelen usar imágenes o videos manipulados o fuera de contexto. Haz una búsqueda inversa de la imagen para saber de dónde viene.
4. **Revisa la evidencia.** La falta de pruebas o "expertos" no identificados son señales de alerta.
5. **¿Es una broma?** Muchos sitios publican sátira. Si notas ironía o burla, puede ser humor.
6. **Pon atención a la URL.** Muchos sitios falsos imitan los nombres de medios confiables.
7. **Fíjate en el formato.** Las faltas de ortografía y los diseños raros son una pista.
8. **Verifica las fechas.** Las cronologías que no cuadran delatan una nota falsa.
9. **Busca otros reportes.** Si ningún otro medio publica lo mismo, desconfía.
10. **Algunas historias son falsas a propósito.** Lee con sentido crítico y comparte solo lo que sabes que es confiable.

## Hoy es todavía más importante

Las imágenes, audios y videos generados con inteligencia artificial hacen más fácil fabricar "pruebas". Desconfía de lo que te llega por WhatsApp sin fuente y usa sitios de verificación de datos.

## Para marcas

Compartir información falsa, aunque sea por error, daña tu credibilidad. Verifica antes de publicar, cita tus fuentes y corrige rápido si te equivocas. Y prepárate por si alguien difunde algo falso sobre tu empresa: revisa [cómo hacer un manual de crisis]({S}/infografia-como-hacer-una-manual-de-crisis-de-reputacion/).
""",
faq=[
("¿Cómo saber si una noticia es falsa?", "Revisa la fuente, la URL, la evidencia, las fechas y las fotos, busca si otros medios confiables publican lo mismo y desconfía de titulares exagerados."),
("¿Cómo verificar una imagen?", "Con una búsqueda inversa de imágenes, que muestra dónde apareció antes y si fue sacada de contexto."),
("¿Qué hacer si mi empresa comparte una noticia falsa?", "Retirarla, aclarar el error con transparencia y revisar tu proceso para verificar fuentes antes de publicar."),
],
related=[("Cómo hacer un manual de crisis", S + "/infografia-como-hacer-una-manual-de-crisis-de-reputacion/"), ("Buenas prácticas para redes", S + "/infografia-guia-de-buenas-practicas-para-el-uso-y-gestion-de-redes-sociales/")],
),

dict(
id=2349, slug="infografia-9-consejos-para-vender-un-producto",
title="9 consejos para vender un producto (infografía)",
excerpt="Infografía con 9 consejos para vender un producto: cree en él, conócelo, explica beneficios, conoce a tu cliente, practica, sé honesto y cierra la venta con delicadeza.",
img_alt="Infografía de 9 consejos para vender un producto",
credit="Infografía: Panorama Anunciantes.",
body=f"""
Vender no es convencer a alguien de comprar algo que no necesita. Es ayudarle a decidir si lo que ofreces resuelve su problema. Esta infografía da nueve consejos para hacerlo bien.

{{IMG}}

## Los consejos

1. **Demuestra el amor por tu producto.** Si no crees en lo que vendes, el cliente lo nota. El entusiasmo se contagia.
2. **Conoce tu producto como a ti mismo.** Debes poder responder cualquier pregunta sobre sus características.
3. **Haz énfasis en las ventajas.** Explica cómo cada característica se convierte en un beneficio para el cliente.
4. **Explica las características a detalle.** En los detalles nacen los argumentos de venta.
5. **Conoce qué motiva a tus clientes.** Investiga sus necesidades, deseos e inquietudes para anticiparte.
6. **Practica cómo abordarlos.** Imagina los escenarios posibles: la práctica hace al maestro.
7. **La honestidad es clave.** Mintiendo quizás logres una venta, pero nunca la recompra. Nadie confía en una marca que lo engañó.
8. **No presiones.** El cliente no debe sentirse obligado a decidir.
9. **Cierra la venta.** Cuando ya diste la información y su espacio para pensarlo, impúlsalo con delicadeza a dar el último paso.

## Característica vs. beneficio

| Característica | Beneficio para el cliente |
| --- | --- |
| Batería de 20 horas | No te quedas sin celular en todo el día |
| Software en la nube | Trabajas desde cualquier lugar sin instalar nada |
| Entrega en 24 horas | Lo tienes mañana, sin esperar |

El cliente compra el beneficio. Tú tienes que traducir.

## Del vendedor al sistema

Estos consejos funcionan cara a cara, y también en tu sitio web: describe beneficios, responde objeciones con contenido y no presiones. Es lo que hace el [inbound marketing]({GUIA}). Más ideas en [10 frases para captar clientes]({S}/infografia-10-frases-para-captar-clientes/).
""",
faq=[
("¿Cómo vender mejor un producto?", "Creyendo en él, conociéndolo a fondo, explicando sus beneficios, entendiendo qué motiva al cliente, practicando, siendo honesto, sin presionar y cerrando con delicadeza."),
("¿Qué diferencia hay entre característica y beneficio?", "La característica describe el producto; el beneficio explica qué gana el cliente con ella. Los clientes compran beneficios."),
("¿Por qué es importante la honestidad en ventas?", "Porque un engaño puede conseguir una venta, pero destruye la confianza y la posibilidad de recompra y recomendación."),
],
related=[("Qué es el inbound marketing", GUIA), ("El arte de negociar", S + "/infografia-el-arte-de-negociar/")],
),

dict(
id=2111, slug="infografia-que-es-el-social-selling-index-ssi",
title="Qué es el Social Selling Index (SSI) de LinkedIn",
excerpt="Infografía del Social Selling Index (SSI) de LinkedIn: qué mide, cómo se calcula de 0 a 100, sus cuatro componentes y cómo mejorar tu puntuación para vender más.",
img_alt="Infografía de qué es el Social Selling Index (SSI)",
credit="Infografía: Vodafone Empresa (ideasparatuempresa.es).",
body=f"""
LinkedIn tiene un indicador que mide qué tan bien usas la red para vender: el Social Selling Index, o SSI. Esta infografía explica sus partes.

{{IMG}}

## Qué es el SSI

Es una puntuación de 0 a 100 que mide tu efectividad para vender a través de LinkedIn. Se actualiza a diario.

## Lo que muestra el panel, según la infografía

- **Índice diario:** tu puntuación sobre 100.
- **Clasificación SSI:** tu posición frente a profesionales de tu sector y frente a tu red de contactos.
- **Estado del perfil:** qué tan bien gestionas tu perfil, tus contactos y tus contenidos, en componentes con valores de 0 a 25.
- **Resumen semanal:** el detalle de tu índice en los últimos 7 días.
- **Estatus frente a la competencia:** compara tu perfil con el de tu sector y tu red.

## Los 4 componentes (25 puntos cada uno)

1. **Establecer tu marca profesional:** perfil completo y publicaciones de valor.
2. **Encontrar a las personas adecuadas:** búsqueda de prospectos con buenos filtros.
3. **Interactuar con información relevante:** compartir y comentar contenido útil.
4. **Construir relaciones:** conectar y conversar con tomadores de decisión.

Puedes consultar tu puntuación en la página de Social Selling Index de LinkedIn mientras tienes la sesión iniciada.

## Cómo mejorarlo

- Completa tu perfil con un título claro sobre a quién ayudas.
- Publica o comenta algo útil al menos dos veces por semana.
- Conecta con personas de tu mercado ideal, con un mensaje personal.
- Conversa antes de vender.

El SSI no es un fin en sí mismo: lo que importa son las conversaciones y oportunidades. Pero es una buena forma de medir hábitos. Más en [beneficios de la marca personal]({S}/infografia-beneficios-de-ls-marca-personal/).
""",
faq=[
("¿Qué es el Social Selling Index?", "Es una puntuación de 0 a 100 de LinkedIn que mide qué tan efectivo eres vendiendo a través de la red, con base en tu marca profesional, cómo encuentras personas, cómo interactúas y cómo construyes relaciones."),
("¿Cómo consulto mi SSI?", "En la página de Social Selling Index de LinkedIn, con tu sesión iniciada."),
("¿Cómo subir mi puntuación SSI?", "Completando tu perfil, publicando y comentando contenido útil con regularidad, conectando con tu público ideal y conversando con tus contactos."),
],
related=[("Beneficios de la marca personal", S + "/infografia-beneficios-de-ls-marca-personal/"), ("9 consejos para vender un producto", S + "/infografia-9-consejos-para-vender-un-producto/")],
),
]
