from comun import *

SHOP = "https://www.fernandomartinez.mx/enlaces-recomendados?task=weblink.go&id=100"
TIENDA = S + "/como-iniciar-una-tienda-online/"
COMO_SHOPIFY = S + "/como-funciona-shopify/"
CASOS_SHOPIFY = S + "/casos-de-exito-en-shopify/"
ABANDONAR = S + "/cuando-abandonar-un-cliente/"

POSTS = [
dict(
id=9737, slug="como-iniciar-una-tienda-online",
title="Cómo iniciar una tienda online en México paso a paso",
excerpt="Cómo iniciar una tienda online en México: elegir producto, validar demanda, escoger plataforma, resolver pagos, envíos y facturación, y conseguir tus primeras ventas.",
img_alt="Cómo iniciar una tienda online en México",
body=f"""
Muchos queremos emprender, pero pocos podemos renunciar mañana al sueldo fijo. Una tienda online es una buena forma de empezar sin apostar todo: puedes arrancar con poco, en tus tiempos libres, y crecer conforme haya ventas.

Eso sí: "abrir la tienda" es la parte fácil. Lo difícil es que alguien compre. Esta guía va en ese orden.

## 1. Decide qué vas a vender

Hay tres caminos comunes:

- **Lo haces tú:** jabones artesanales, ropa, muebles, cerámica.
- **Lo compras a mayoreo** y lo revendes con margen.
- **Dropshipping:** vendes y un proveedor envía directo al cliente. Arrancas sin inventario, pero el margen es menor y dependes mucho del proveedor.

Una pregunta útil: ¿qué problema resuelve tu producto, y para quién? "Velas aromáticas" es un producto. "Velas para regalar en fechas especiales, envueltas y listas" es una propuesta.

## 2. Valida que alguien lo quiere

Antes de invertir en inventario:

- Busca en Google y en marketplaces qué productos parecidos se venden y a qué precio.
- Pregunta a conocidos y en comunidades en línea. Mejor aún: intenta venderles.
- Haz un preventa o una prueba pequeña en redes sociales.

Si nadie te compra a ti en persona, una tienda online no lo va a arreglar.

## 3. Haz las cuentas

Suma costo del producto, empaque, envío, comisión de la pasarela de pago, comisión de la plataforma, publicidad e impuestos. Si después de todo eso el margen es muy delgado, ajusta el precio o el producto antes de lanzar.

## 4. Elige la plataforma

| Opción | Ventajas | Desventajas |
| --- | --- | --- |
| Plataforma de ecommerce (por ejemplo Shopify) | Rápida de montar, pagos y envíos integrados | Pago mensual y comisiones |
| WordPress con WooCommerce | Mucho control y flexibilidad | Requiere más mantenimiento técnico |
| Marketplaces (Mercado Libre, Amazon) | Tráfico desde el primer día | Comisiones altas y el cliente es del marketplace |
| Redes sociales y WhatsApp | Costo casi nulo para empezar | Difícil de escalar y de ordenar |

Muchas tiendas combinan una tienda propia con un marketplace. Si quieres probar Shopify, [aquí puedes empezar]({SHOP}), y en esta guía te explicamos [cómo funciona Shopify]({COMO_SHOPIFY}).

## 5. Resuelve pagos, envíos y facturación

- **Pagos:** tarjeta, transferencia, pago en tiendas de conveniencia y meses sin intereses si tu ticket lo permite.
- **Envíos:** compara paqueterías, define quién paga el envío y deja claros los tiempos.
- **Formalidad:** date de alta ante el SAT en el régimen que te corresponda y prepárate para emitir facturas. Un contador te ahorra muchos dolores de cabeza.
- **Políticas:** cambios, devoluciones y aviso de privacidad, visibles y en lenguaje claro.

## 6. Haz que tu tienda inspire confianza

Fotos reales y bien iluminadas, descripciones que respondan dudas (medidas, materiales, cuidados), datos de contacto visibles y un botón de WhatsApp. Las primeras reseñas pesan muchísimo: pídelas.

## 7. Consigue tus primeras ventas

1. Tu red cercana: amigos, familia, excompañeros.
2. Contenido en una o dos redes sociales donde esté tu cliente.
3. Contenido útil en tu blog que responda búsquedas reales.
4. Una lista de correo desde el primer día.
5. Publicidad pagada en cuanto sepas qué producto y qué mensaje funcionan.

Mira estos [casos de éxito en Shopify]({CASOS_SHOPIFY}) y las [características de un emprendedor exitoso]({EMPRENDEDOR}).
""",
faq=[
("¿Cómo iniciar una tienda online en México?", "Elige un producto, valida que hay demanda, calcula tus márgenes, escoge una plataforma, resuelve pagos, envíos y facturación, y consigue tus primeras ventas con tu red, contenido y una lista de correo."),
("¿Qué plataforma conviene para una tienda en línea?", "Depende de tu caso: plataformas como Shopify son rápidas de montar, WooCommerce da más control, los marketplaces aportan tráfico inmediato y las redes sociales sirven para probar con poca inversión."),
("¿Necesito darme de alta en el SAT para vender en línea?", "Sí. Vender en línea es una actividad económica, así que debes darte de alta en el régimen fiscal que te corresponda. Lo ideal es consultarlo con un contador."),
("¿Se puede vender en línea sin inventario?", "Sí, con dropshipping o fabricación bajo pedido, aunque normalmente implica márgenes menores y depender más de tus proveedores."),
],
related=[("Cómo funciona Shopify", COMO_SHOPIFY), ("Inbound marketing para pymes", PYMES)],
),

dict(
id=4080, slug="como-funciona-shopify",
title="Cómo funciona Shopify: guía para pymes y emprendedores",
excerpt="Cómo funciona Shopify para pymes y emprendedores en México: qué es, qué puedes vender, cómo crear tu tienda, cómo cobrar y enviar, y cuándo conviene otra opción.",
img_alt="Cómo funciona Shopify para pymes y emprendedores",
body=f"""
Quieres vender en línea, pero no quieres aprender a programar ni contratar a un desarrollador para cada cambio. Para eso existe Shopify.

En pocas palabras: Shopify es una plataforma que te renta todo lo necesario para tener una tienda en línea. Tú pones el producto y el negocio; ellos ponen el hosting, el carrito, los pagos y la seguridad.

## Qué es Shopify

Es una plataforma de comercio electrónico en la nube, fundada en Canadá en 2006. No instalas nada: creas una cuenta, eliges una plantilla, subes tus productos y empiezas a vender. Pagas una suscripción mensual, más comisiones por transacción según el plan y el método de pago.

Los planes y precios cambian con frecuencia, así que revisa los vigentes directamente en su sitio antes de decidir.

## Qué puedes vender

Prácticamente cualquier producto legal: físicos, digitales (cursos, ebooks), servicios, suscripciones y hasta productos bajo pedido. Si además tienes tienda física, su punto de venta (POS) te permite manejar inventario y ventas en un solo lugar.

## Cómo crear tu tienda en 7 pasos

1. **Crea tu cuenta** y define el nombre de tu tienda.
2. **Elige una plantilla.** Hay gratuitas y de pago. Prioriza que se vea bien en celular.
3. **Sube tus productos** con buenas fotos, descripción, precio, variantes (talla, color) e inventario.
4. **Configura pagos.** Tarjeta, transferencia y otros métodos según tu país.
5. **Configura envíos.** Zonas, tarifas y paqueterías.
6. **Conecta tu dominio.** tutienda.com.mx se ve más confiable que una dirección genérica.
7. **Revisa políticas y lanza.** Devoluciones, privacidad y términos, claros y visibles.

## Lo que más ayuda de Shopify

- **Apps:** miles de extensiones para reseñas, email marketing, programas de lealtad o facturación.
- **Canales de venta:** puedes conectar redes sociales, Google y marketplaces.
- **Reportes:** ventas, productos más vendidos y carritos abandonados.
- **Recuperación de carritos:** correos automáticos a quien dejó compras a medias.

## Cuándo NO conviene Shopify

- Si vendes muy poco y solo quieres probar: puedes empezar por redes sociales o un marketplace.
- Si necesitas un control técnico total del sitio o integraciones muy específicas: WooCommerce o un desarrollo a la medida pueden ajustarse mejor.
- Si tu margen es tan bajo que cada comisión duele: haz bien las cuentas antes.

## Tener la tienda no es tener ventas

Una tienda sin tráfico es un local en una calle sin gente. Necesitas atraer visitantes con contenido, redes sociales, buscadores y una lista de correo. Eso es [inbound marketing para pymes]({PYMES}).

Si quieres probar la plataforma, [crea tu tienda en Shopify aquí]({SHOP}). Y para el panorama completo, lee [cómo iniciar una tienda online en México]({TIENDA}).
""",
faq=[
("¿Qué es Shopify y cómo funciona?", "Es una plataforma de comercio electrónico en la nube: pagas una suscripción mensual, eliges una plantilla, subes tus productos y la plataforma te da carrito, pagos, hosting y seguridad."),
("¿Cuánto cuesta Shopify?", "Tiene varios planes con suscripción mensual, además de comisiones según el plan y el método de pago. Los precios cambian con frecuencia, así que conviene revisar los vigentes en su sitio oficial."),
("¿Qué se puede vender en Shopify?", "Casi cualquier producto legal: productos físicos, digitales, servicios y suscripciones. También puedes conectar tu tienda física con su sistema de punto de venta."),
("¿Shopify funciona en México?", "Sí. Puedes vender en pesos, configurar envíos nacionales y aceptar distintos métodos de pago disponibles en México."),
],
related=[("Cómo iniciar una tienda online en México", TIENDA), ("Casos de éxito en Shopify", CASOS_SHOPIFY)],
),

dict(
id=4053, slug="casos-de-exito-en-shopify",
title="Casos de éxito en Shopify: 3 tiendas y lo que puedes aprender",
excerpt="Casos de éxito en Shopify en Latinoamérica: Vorana, Mini Minu y Pet n'GO. Qué hicieron bien y qué lecciones puedes aplicar en tu propia tienda en línea.",
img_alt="Casos de éxito de tiendas en línea en Shopify",
body=f"""
Elegir plataforma para vender en línea da vértigo. Hay muchas opciones y todas prometen lo mismo.

Pero la plataforma es solo la mitad. Lo que separa a una tienda que vende de una que acumula polvo digital es lo que haces con ella. Por eso, en lugar de otra lista de funciones, aquí van tres historias de tiendas latinoamericanas en Shopify y lo que cada una enseña.

## Vorana: humanizar una tienda en línea

Vorana vende productos de belleza en tendencia. Sus fundadores no eran desarrolladores, así que se apoyaron en las herramientas de la plataforma para montar la tienda y dedicaron su energía a otra cosa: el servicio.

Su objetivo, en palabras de su equipo, fue "humanizar a Vorana": asesorar, acompañar y hacer sentir cerca al cliente.

**La lección:** en línea, el cliente no te ve. Cada respuesta rápida, cada recomendación personal y cada empaque cuidado reemplaza la sonrisa del mostrador.

## Mini Minu: saber exactamente a quién le hablas

Mini Minu vende muebles en línea. Su fundadora llegó a Panamá desde Argentina por el trabajo de su esposo y, como no podía ejercer su profesión de médica en ese país, empezó a explorar opciones. Así nació la tienda.

Lo que hizo la diferencia fue una segmentación clara: sabían a quién le hablaban y qué canales usar para llegar a esas personas.

**La lección:** no le vendas a "todo el mundo". Define tu [buyer persona]({BUYER}) y habla como si le escribieras a esa persona.

## Pet n'GO: nacer de una frustración propia

Pet n'GO empezó en 2011, cuando su fundador compró un perro y descubrió que no encontraba tiendas de mascotas con un servicio a la altura. Arrancó con unos 100 productos y una filosofía: que cada cliente se sintiera atendido y asesorado.

**La lección:** los mejores negocios suelen resolver un problema que el fundador vivió en carne propia. Esa experiencia se convierte en contenido, en servicio y en credibilidad.

## Lo que tienen en común

1. **Ninguno compite solo por precio.** Compiten por servicio, especialización y cercanía.
2. **Conocen a su cliente.** Su comunicación se nota pensada para alguien concreto.
3. **Usan la tecnología para liberar tiempo,** no como fin en sí misma.
4. **Empezaron pequeños.** Ninguno lanzó con un catálogo gigante ni una inversión enorme.

## Cómo aplicarlo en tu tienda

- Responde mensajes rápido y con nombre propio.
- Escribe descripciones que resuelvan dudas reales.
- Crea contenido sobre tu especialidad, no solo promociones.
- Pide reseñas y compártelas.
- Da seguimiento a quien compró para que vuelva.

Si quieres empezar, revisa [cómo funciona Shopify]({COMO_SHOPIFY}) o [crea tu tienda aquí]({SHOP}). Y para el proceso completo, lee [cómo iniciar una tienda online en México]({TIENDA}).
""",
faq=[
("¿Qué tiendas exitosas usan Shopify en Latinoamérica?", "Entre los casos que la propia plataforma ha difundido están Vorana (belleza), Mini Minu (muebles) y Pet n'GO (productos para mascotas), además de miles de marcas de todos los tamaños."),
("¿Qué tienen en común las tiendas exitosas en Shopify?", "Conocen bien a su cliente, compiten por servicio y especialización más que por precio, usan la tecnología para ahorrar tiempo y empezaron con un catálogo pequeño."),
("¿Shopify garantiza el éxito de una tienda en línea?", "No. La plataforma facilita la parte técnica, pero las ventas dependen del producto, el servicio, el contenido y la forma de atraer y cuidar a los clientes."),
],
related=[("Cómo funciona Shopify", COMO_SHOPIFY), ("Cómo iniciar una tienda online", TIENDA)],
),

dict(
id=4045, slug="que-hacer-cuando-un-cliente-no-te-paga",
title="Qué hacer cuando un cliente no te paga: 10 pasos",
excerpt="Qué hacer cuando un cliente no te paga: cómo prevenir, cobrar sin perder la relación, documentar el adeudo y cuándo acudir a un abogado en México.",
img_alt="Qué hacer cuando un cliente no te paga",
body=f"""
Terminaste el trabajo. Lo entregaste a tiempo. El cliente quedó contento.

Y luego… silencio. La factura venció hace tres semanas y tus correos tienen la tasa de respuesta de un formulario de quejas.

Si emprendes, tarde o temprano te va a pasar. La buena noticia es que buena parte del problema se previene, y la otra parte se maneja mejor con cabeza fría que con mensajes a medianoche.

## Antes: prevenir es más barato que cobrar

### 1. Pon todo por escrito

Alcance, precio, fechas de pago y qué pasa si hay retraso. Un contrato es ideal; un correo con la aceptación del cliente es mucho mejor que nada.

### 2. Pide anticipo

Un anticipo filtra a los clientes que no tienen intención (o capacidad) de pagar. Para proyectos largos, divide en entregas y cobra por avance.

### 3. Premia el pronto pago

Un pequeño descuento por pagar a tiempo suele funcionar mejor que amenazar con recargos que, siendo honestos, casi nadie cobra.

### 4. Factura bien

En México, si vas a cobrar en parcialidades o después de facturar, emite tu CFDI con método de pago PPD y, cuando recibas cada pago, el complemento de pago. Tener la facturación en orden te ayuda también si un día hay que reclamar.

## Durante: cobra sin quemar la relación

### 5. Recuerda antes de que venza

Un correo amable unos días antes de la fecha, y otro el día del vencimiento. Muchas veces el retraso es un descuido, no mala fe.

### 6. Habla con la persona correcta

Quien te contrató no siempre es quien paga. Pregunta cuál es el proceso de cuentas por pagar, qué fechas manejan y qué documentos necesitan.

### 7. Escala con calma

Correo, luego llamada, luego una reunión. Mantén el tono profesional y deja constancia por escrito de cada acuerdo.

### 8. Negocia un plan de pagos

Si el cliente tiene problemas reales de flujo, un calendario de pagos es mejor que nada. Documenta el acuerdo y, si es posible, respáldalo con un pagaré firmado.

### 9. Pausa el trabajo pendiente

Si tu contrato lo permite, detén entregas nuevas hasta regularizar los pagos. Avísalo con anticipación y por escrito.

## Después: cuando no hay de otra

### 10. Consulta a un abogado

Si el adeudo es importante, un abogado puede enviar un requerimiento formal y evaluar la vía adecuada. Si tienes un pagaré firmado, existe el juicio ejecutivo mercantil, que suele ser más directo. Cada caso es distinto, así que pide asesoría antes de actuar.

## Y aprende la lección

Si un cliente te hizo pasar por esto, revisa si vale la pena seguir trabajando con él. A veces la mejor decisión es [saber cuándo abandonar a un cliente]({ABANDONAR}).

Este artículo es informativo y no sustituye la asesoría de un abogado o contador.
""",
faq=[
("¿Qué hacer si un cliente no me paga?", "Envía recordatorios amables, habla con el área que paga, escala con calma, negocia un plan de pagos documentado, pausa el trabajo pendiente si el contrato lo permite y, si el adeudo es importante, consulta a un abogado."),
("¿Cómo evitar que un cliente no me pague?", "Pon el acuerdo por escrito, pide anticipo, cobra por avances en proyectos largos, ofrece descuento por pronto pago y factura correctamente."),
("¿Qué es el juicio ejecutivo mercantil?", "Es una vía legal en México para cobrar deudas respaldadas por documentos como un pagaré. Un abogado puede decirte si aplica en tu caso."),
("¿Qué es el complemento de pago?", "Es un CFDI que se emite cuando recibes el pago de una factura emitida con método de pago PPD (pago en parcialidades o diferido)."),
],
related=[("Cuándo abandonar a un cliente", ABANDONAR), ("Características de un emprendedor exitoso", EMPRENDEDOR)],
),

dict(
id=5895, slug="cuando-abandonar-un-cliente",
title="Cuándo abandonar a un cliente: 6 señales claras",
excerpt="Cuándo abandonar a un cliente: 6 señales de que una relación comercial ya no te conviene y cómo terminarla de forma profesional sin dañar tu reputación.",
img_alt="Cuándo abandonar a un cliente",
body=f"""
Nadie emprende para despedir clientes. Al principio, cada cliente se siente como un salvavidas.

Pero hay clientes que, en lugar de mantenerte a flote, te hunden: te quitan tiempo, dinero, energía y la posibilidad de atender a otros que sí valen la pena.

Como en una relación de pareja, a veces seguir juntos le hace daño a los dos. Aquí van seis señales de que llegó el momento.

## 1. El esfuerzo no tiene nada que ver con lo que pagan

Cambios infinitos, juntas que no estaban en el alcance, urgencias de todo y respuestas lentas de su lado. Si haces las cuentas de tus horas y el proyecto te sale a pérdida, no es un cliente: es un pasatiempo caro.

## 2. Te pide algo que no sabes (o no puedes) hacer

Aprender es parte de emprender. Pero si el proyecto requiere una capacidad o infraestructura que no tienes y no puedes conseguir a tiempo, decirlo es más profesional que entregar mal.

## 3. No respeta tu trabajo ni a tu equipo

Gritos, desprecio, mensajes a las 11 de la noche exigiendo respuesta inmediata. Ningún contrato vale la salud de tu equipo.

## 4. Te paga tarde (o no te paga)

Un retraso ocasional pasa. Un patrón de retrasos es una decisión del cliente. Si ya llegaste a ese punto, revisa [qué hacer cuando un cliente no te paga]({NO_PAGA}).

## 5. Te pide algo que va contra tus valores o la ley

Prácticas engañosas, información falsa, atajos legales. No hay factura que compense el daño a tu reputación.

## 6. Dependes demasiado de él

Si un solo cliente representa la mayor parte de tus ingresos, aunque sea bueno, estás en riesgo. No necesariamente hay que dejarlo, pero sí diversificar antes de que él decida por ti.

## Antes de terminar, intenta arreglarlo

Muchas relaciones se salvan con una conversación honesta: redefinir el alcance, ajustar precios o acordar nuevas reglas de comunicación. Si eso no funciona, entonces sí.

## Cómo terminar de forma profesional

1. **Revisa tu contrato:** plazos de aviso, entregables pendientes y penalizaciones.
2. **Avisa con anticipación,** de preferencia en persona o por llamada, y confírmalo por escrito.
3. **Entrega lo pendiente,** junto con accesos, archivos y documentación.
4. **Ofrece una transición,** incluso recomendar a otro proveedor si encaja mejor.
5. **No hables mal de él,** ni en público ni en privado. El mercado es más pequeño de lo que parece.

## El costo oculto de quedarte

Cada hora que le das a un mal cliente es una hora que no le das a encontrar uno bueno. Para tener de dónde escoger, necesitas un flujo constante de prospectos; eso es justo lo que resuelve el [inbound marketing para pymes]({PYMES}).
""",
faq=[
("¿Cuándo es momento de dejar a un cliente?", "Cuando el esfuerzo no corresponde a lo que paga, te pide algo que no puedes hacer bien, no respeta a tu equipo, paga tarde de forma recurrente, te pide algo contrario a tus valores o la ley, o dependes demasiado de él."),
("¿Cómo terminar la relación con un cliente de forma profesional?", "Revisa tu contrato, avisa con anticipación y por escrito, entrega lo pendiente con accesos y documentación, ofrece una transición y evita hablar mal de él."),
("¿Es mala idea depender de un solo cliente?", "Sí, aunque sea un buen cliente: si representa la mayor parte de tus ingresos, cualquier cambio de su lado pone en riesgo a tu negocio. Conviene diversificar."),
],
related=[("Qué hacer cuando un cliente no te paga", NO_PAGA), ("Cómo hacer que tus clientes te recomienden", RECOMIENDEN)],
),

dict(
id=3892, slug="employer-branding",
title="Employer branding: qué es y cómo atraer mejor talento",
excerpt="Qué es el employer branding o reclutamiento inbound, por qué importa para atraer y retener talento y cómo construir tu marca empleadora paso a paso.",
img_alt="Employer branding y reclutamiento inbound",
body=f"""
Durante años, reclutar funcionaba así: la empresa publicaba una vacante y los candidatos hacían fila.

Para muchos puestos, eso se acabó. Los buenos candidatos tienen opciones, investigan a la empresa antes de aplicar y leen lo que dicen los empleados actuales y anteriores. Ahora es la empresa la que tiene que convencer.

Eso es el **employer branding**: la reputación de tu empresa como lugar para trabajar. Y cuando lo trabajas con la lógica del inbound marketing, se llama reclutamiento inbound.

## Qué es el employer branding

Es la imagen que tienen de tu empresa los candidatos, los empleados y el mercado laboral en general. Existe aunque no la trabajes: si no la construyes tú, la construyen las reseñas en sitios de empleo y las conversaciones de pasillo.

## Por qué importa

- **Atraes mejores candidatos** y más rápido.
- **Reduces la rotación,** porque la gente llega sabiendo qué esperar.
- **Bajas el costo de contratación,** al depender menos de anuncios y headhunters.
- **Tus empleados recomiendan,** que es la fuente de candidatos más confiable.

## Reclutamiento inbound: el talento como buyer persona

La lógica es la misma que en ventas:

1. **Atraer:** contenido que muestre cómo es trabajar contigo.
2. **Convertir:** un proceso de aplicación claro y rápido.
3. **Cerrar:** entrevistas respetuosas, ofertas transparentes.
4. **Deleitar:** una buena integración y una experiencia que haga que tus empleados te recomienden.

Define tu candidato ideal como si fuera un [buyer persona]({BUYER}): qué busca, qué le preocupa, dónde se informa.

## Las bases que no se pueden fingir

### Políticas de recursos humanos justas

Cumplir con la ley laboral y fiscal, sueldos competitivos, prestaciones claras y oportunidades de crecimiento. Sin esto, ningún contenido bonito sirve.

### Una cultura que se vive

Flexibilidad, trabajo por objetivos, reconocimiento, buen liderazgo. La cultura es lo que pasa cuando el jefe no está viendo. Te puede servir esta [infografía de cultura digital]({CULTURA}) y la de [características de un buen líder]({LIDER}).

### Una experiencia de candidato respetuosa

Responde a todos, aunque sea para decir que no. Da fechas claras. No hagas cinco entrevistas para un puesto junior.

## Cómo comunicar tu marca empleadora

- **Una página de empleo real:** qué hacen, cómo trabajan, beneficios, proceso de selección y vacantes.
- **Historias de tu equipo:** en video o texto, con su permiso y en sus palabras.
- **Redes sociales,** sobre todo LinkedIn: logros del equipo, detrás de cámaras, aprendizajes.
- **Reseñas:** responde con respeto las opiniones en sitios de empleo, también las negativas.

## Cómo medirlo

Candidatos por vacante, tiempo para cubrir un puesto, costo por contratación, aceptación de ofertas, rotación en el primer año y porcentaje de contrataciones por recomendación.

Si quieres aplicar la metodología completa, lee [qué es el inbound marketing]({GUIA}).
""",
faq=[
("¿Qué es el employer branding?", "Es la reputación de una empresa como lugar para trabajar: la imagen que tienen de ella los candidatos, los empleados y el mercado laboral."),
("¿Qué es el reclutamiento inbound?", "Es aplicar la metodología inbound a la atracción de talento: atraer candidatos con contenido, facilitar la aplicación, ofrecer un proceso respetuoso y cuidar la experiencia de los empleados para que recomienden a la empresa."),
("¿Cómo mejorar la marca empleadora de una empresa?", "Con políticas de recursos humanos justas, una cultura real, una experiencia de candidato respetuosa, una página de empleo clara, historias del equipo y atención a las reseñas."),
("¿Cómo se mide el employer branding?", "Con indicadores como candidatos por vacante, tiempo y costo de contratación, aceptación de ofertas, rotación en el primer año y contrataciones por recomendación."),
],
related=[("Qué hacer ante la salida de un empleado clave", S + "/que-hacer-ante-la-salida-de-un-empleado-clave/"), ("Cultura digital en tu empresa", CULTURA)],
),

dict(
id=1185, slug="inbound-marketing-para-agencias-de-autos",
title="Inbound marketing para agencias de autos: 7 estrategias",
excerpt="Inbound marketing para agencias de autos: cómo atraer compradores que investigan en línea, dar seguimiento a cada prospecto y vender más sin depender del volanteo.",
img_alt="Inbound marketing para agencias de autos",
body=f"""
Imagina al vendedor de autos de las películas: corbata llamativa, sonrisa de comercial y un inflable gigante bailando en la entrada.

Ese modelo sigue vivo en muchas agencias. El problema es que el comprador cambió. Hoy llega a la agencia después de semanas de investigar en línea: comparó modelos, vio reseñas en video, revisó precios y quizá ya sabe más de la ficha técnica que el vendedor.

El inbound marketing para agencias de autos consiste en acompañar esa investigación y ser la agencia que el comprador quiere visitar.

## 1. Responde lo que el comprador busca

Las búsquedas del comprador son muy concretas: "SUV familiar con mejor consumo", "cuánto cuesta el servicio de los 20,000 km", "requisitos para crédito automotriz". Cada una es un tema de contenido.

## 2. Haz que cada auto tenga su página útil

Fotos reales, video corto, ficha técnica, versiones, precio de referencia y botón para agendar prueba de manejo. Una página así trabaja por ti las 24 horas.

## 3. Cuida tu perfil de Google y tus reseñas

"Agencia [marca] cerca de mí" es una búsqueda con intención de compra. Fotos actuales, horarios, reseñas respondidas con respeto y preguntas resueltas.

## 4. Da seguimiento a cada prospecto

Quien cotizó y no compró no es un caso perdido: probablemente sigue comparando. Un CRM y una secuencia de seguimiento (comparativo, invitación a prueba de manejo, opciones de financiamiento) hacen la diferencia. Y responde rápido: el que contesta primero suele llevarse la cita.

## 5. Usa tu base de clientes (sin bombardearla)

Ya tienes una lista de clientes valiosa. Úsala con contenido útil: recordatorios de servicio, consejos de mantenimiento por temporada, campañas de revisión. Así, cuando llegue el momento de cambiar de auto, piensan en ti.

## 6. Redes sociales para mostrar, no solo para promocionar

Entregas de autos (con permiso del cliente), recorridos por versiones, comparativos honestos, consejos de manejo. Responde comentarios rápido y con cortesía.

## 7. Conecta con la emoción detrás de la compra

Un auto no es solo transporte. Es el primer auto, el auto de la familia que creció, el premio después de años de trabajo. Las historias reales de tus clientes conectan más que cualquier lista de especificaciones.

## Mide lo que importa

Cotizaciones en línea, citas de prueba de manejo, tasa de cierre por canal, costo por venta y clientes que regresan a servicio. Estos [KPIs para tu sitio web]({KPIS}) son un buen punto de partida.

Lee también este análisis sobre [equipo interno o agencia externa en el sector automotriz](https://www.publi20.com/revista-publicidad-negocios-mexico/5408-equipo-interno-de-marketing-digital-o-agencia-externa-la-experiencia-del-sector-automotriz) y más [ejemplos de inbound marketing en México]({EJEMPLOS}).
""",
faq=[
("¿Qué es el inbound marketing para agencias de autos?", "Es atraer a compradores que investigan en línea con contenido útil sobre modelos, precios, financiamiento y servicio, y darles seguimiento hasta la prueba de manejo y la venta."),
("¿Cómo puede una agencia de autos conseguir más prospectos en línea?", "Con páginas útiles para cada modelo, contenido que responda búsquedas concretas, un perfil de Google bien cuidado, redes sociales activas y respuesta rápida a cada cotización."),
("¿Qué hacer con los prospectos que cotizan y no compran?", "Darles seguimiento con un CRM: comparativos, invitaciones a prueba de manejo y opciones de financiamiento. Muchos siguen comparando y deciden semanas después."),
],
related=[("Ejemplos de inbound marketing en México", EJEMPLOS), ("Por qué hacer campañas en buscadores", BUSCADORES)],
),

dict(
id=4072, slug="que-hacer-ante-la-salida-de-un-empleado-clave",
title="Qué hacer ante la salida de un empleado clave (infografía)",
excerpt="Qué hacer ante la salida de un empleado clave: cómo reaccionar, transferir el conocimiento, cuidar a clientes y equipo, y prepararte para que no vuelva a tomarte por sorpresa.",
img_alt="Qué hacer ante la salida de un empleado clave",
body=f"""
"¿Tienes un minuto? Quiero platicarte algo."

Pocas frases asustan tanto a un dueño de negocio, sobre todo cuando las dice la persona que sabe cómo funciona todo. La salida de un empleado clave duele: se va conocimiento, a veces relaciones con clientes, y el equipo se pone nervioso.

No puedes evitar que la gente se vaya. Sí puedes evitar que su salida descarrile a la empresa.

## Los primeros días: mantén la calma

1. **Escucha.** Entender por qué se va te da información valiosa, aunque no puedas retenerlo.
2. **Evalúa si vale la pena una contraoferta.** A veces funciona; muchas veces solo retrasa la salida. Si el motivo no es el dinero, el dinero no lo va a resolver.
3. **Acuerda la fecha de salida y el plan de transición.** Cuánto tiempo se queda, qué entrega y a quién.
4. **Cumple con lo legal.** Finiquito, documentos y procesos conforme a la ley laboral. Si tienes dudas, consulta a un especialista.

## Transfiere el conocimiento

Es lo más urgente:

- Lista de tareas recurrentes y cómo se hacen.
- Procesos documentados, aunque sea en una página cada uno.
- Contraseñas y accesos, que deben pasar a la empresa.
- Proyectos en curso: estado, pendientes y contactos.
- Relaciones clave: presentaciones en persona con clientes y proveedores.

## Comunica bien

**Al equipo:** pronto, con claridad y sin dramas. Explica quién asume qué y cómo será la transición. El silencio genera rumores.

**A los clientes:** si la persona era su contacto principal, preséntales a su nuevo enlace antes de la salida. Lo que más les preocupa es que el servicio no se caiga.

## Cubre la posición

- ¿Hay alguien interno que pueda crecer al puesto?
- ¿Conviene redistribuir funciones?
- ¿Hace falta contratar? Una buena [marca empleadora]({S}/employer-branding/) acorta mucho la búsqueda.

## Despídete bien

Una salida cordial deja la puerta abierta: el exempleado puede recomendarte, volver algún día o convertirse en cliente. Agradece su trabajo en público.

## Prepárate para la próxima vez

1. **Documenta los procesos clave** antes de que alguien se vaya.
2. **Evita que el conocimiento dependa de una sola persona:** rota tareas y forma respaldos.
3. **Haz entrevistas de permanencia,** no solo de salida: pregunta qué los haría quedarse.
4. **Cuida la cultura y el liderazgo.** Mucha gente no deja empresas, deja jefes. Revisa las [características de un buen líder]({LIDER}).
""",
faq=[
("¿Qué hacer cuando renuncia un empleado clave?", "Escucha sus motivos, evalúa si tiene sentido una contraoferta, acuerda un plan de transición, transfiere el conocimiento y los accesos, comunica bien al equipo y a los clientes, y define cómo cubrir el puesto."),
("¿Cómo evitar que el conocimiento se vaya con un empleado?", "Documentando procesos, haciendo que los accesos sean de la empresa, rotando tareas y formando respaldos para que nada dependa de una sola persona."),
("¿Conviene hacer una contraoferta a un empleado que renuncia?", "A veces sí, pero si el motivo de la salida no es económico, la contraoferta suele solo retrasar la renuncia. Primero entiende por qué se va."),
],
related=[("Employer branding", S + "/employer-branding/"), ("Características de un buen líder", LIDER)],
),
]
