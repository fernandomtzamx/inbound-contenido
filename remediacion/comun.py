"""Enlaces internos comunes para las fichas de remediación (todas existen en el sitio)."""
S = "https://www.inbound.com.mx"
HOME = S + "/"
HUB_FRASES = S + "/seccion/centro/frases-de-inbound-marketing/"
HUB_INFO = S + "/seccion/centro/infografias/"
GUIA = S + "/inbound-marketing/"
FASES = S + "/4-fases-del-inbound-marketing/"
BUYER = S + "/buyer-persona/"
PLAN_MC = S + "/desarrolla-un-plan-de-marketing-de-contenidos-para-tu-pagina-web/"
FORMATOS = S + "/formatos-contenido/"
EJEMPLOS = S + "/ejemplos-de-inbound-marketing-en-mexico/"
PYMES = S + "/inbound-marketing-para-pymes/"
B2B = S + "/inbound-marketing-para-empresas-b2b/"
EVALUA = S + "/evalua-tu-agencia-de-marketing-digital/"
RECOMIENDEN = S + "/como-hacer-que-mis-clientes-me-recomienden/"
BUSCADORES = S + "/campana-en-buscadores/"
KPIS = S + "/kpis-web/"
LIDER = S + "/infografia-13-caracteristicas-en-la-personalidad-de-un-buen-lider/"
EMOCIONES = S + "/infografia-como-controlar-tus-emociones/"
CULTURA = S + "/infografia-5-practicas-para-implementar-una-cultura-digital/"
EMPRENDEDOR = S + "/caracteristicas-de-un-emprendedor-exitoso/"
NO_PAGA = S + "/que-hacer-cuando-un-cliente-no-te-paga/"


def f(slug):
    return f"{S}/{slug}/"


# Frases del top 100 (slug completo) para enlazar entre sí
FR = {
    "patel": f("frases-de-inbound-marketing-neil-patel-tu-exito-esta-solo-parcialmente-dictado-por-cuanto-trafico-tienes-la-otra-parte-de-la-ecuacion-es-la-calidad-de-dicho-trafico"),
    "richards": f("frases-de-inbound-marketing-jef-richards-la-creatividad-sin-estrategia-se-llama-arte-la-creatividad-con-estrategia-se-llama-publicidad"),
    "handley1": f("frases-de-inbound-marketing-ann-handley-se-suficientemente-especifico-para-ser-creible-y-suficientemente-universal-para-ser-relevante"),
    "handley2": f("frases-de-inbound-marketing-ann-handley-convierte-al-cliente-en-el-heroe-de-tu-historia"),
    "dilorenzo": f("frases-de-inbound-marketing-mike-dilorenzo-las-redes-sociales-ya-no-son-sobre-sitios-webs-tratan-de-experiencias"),
    "kaushik": f("frases-de-inbound-marketing-avinash-kaushik-solo-podremos-tomar-decisiones-acertadas-si-sabemos-como-analizar-e-interpretar-los-datos"),
    "pulizzi": f("frases-de-inbound-marketing-joe-pulizzi-deja-de-escribir-de-todo-encuentra-tu-nicho-y-luego-busca-un-nicho-mas-pequeno-todavia"),
    "baer1": f("frases-de-inbound-marketing-jay-baer-el-social-media-es-un-ingrediente-no-un-platillo"),
    "kotler": f("frases-de-inbound-marketing-philip-kotler-no-vigile-el-ciclo-de-vida-del-producto-vigile-el-ciclo-de-vida-del-mercado"),
    "godin1": f("frases-de-inbound-marketing-seth-godin-no-encuentres-clientes-para-tus-productos-encuentra-productos-para-tus-clientes"),
    "qualman": f("frases-de-inbound-marketing-erik-qualman-no-tenemos-mas-opcion-que-hacer-social-media-la-cuestion-es-como-podemos-hacerlo-bien"),
    "goulart": f("frases-de-inbound-marketing-matt-goulart-social-media-es-acerca-de-personas-no-acerca-de-tu-negocio-cuida-de-la-gente-y-la-gente-cuidara-de-ti"),
    "barchetti": f("frases-de-inbound-marketing-katherine-barchetti-haz-un-cliente-no-una-venta"),
    "pennington": f("frases-de-inbound-marketing-trey-pennington-las-empresas-que-entienden-el-social-media-son-las-que-dicen-con-su-mensaje-te-veo-te-escucho-y-me-importas"),
    "ries_trout": f("frases-de-inbound-marketing-al-ries-y-jack-trout-el-marketing-no-es-una-batalla-de-productos-es-una-batalla-de-percepciones"),
    "ries": f("frases-de-inbound-marketing-al-ries-la-estrategia-el-sentido-de-la-oportunidad-y-el-momento-exacto-son-las-altas-cumbres-del-marketing-lo-demas-son-apenas-colinas"),
    "alcantara": f("frases-de-inbound-marketing-alfonso-alcantara-marca-es-el-perfume-que-usas-reputacion-es-el-olor-que-dejas"),
    "rapp": f("frases-de-inbound-marketing-stan-rapp-concretar-una-venta-es-importante-pero-lograr-la-fidelidad-de-los-clientes-es-vital"),
    "meerman": f("frases-de-inbound-marketing-david-meerman-scott-en-lugar-de-ser-una-interrupcion-unidireccional-el-marketing-online-suministra-al-comprador-contenido-util-en-el-momento-preciso-en-que-este-lo-nec"),
    "fishburne": f("frases-de-inbound-marketing-tom-fishburne-el-mejor-marketing-no-parece-marketing"),
    "wilson": f("frases-de-inbound-marketing-orvel-ray-wilson-los-clientes-compran-por-sus-razones-no-por-las-tuyas"),
    "bernbach": f("frases-de-inbound-marketing-william-bernbach-la-publicidad-es-basicamente-persuasion-y-la-persuasion-no-es-una-ciencia-sino-un-arte"),
    "hershey": f("frases-de-inbound-marketing-milton-hershey-dales-calidad-es-el-mejor-tipo-de-publicidad-que-existe"),
    "oliveros": f("frases-de-inbound-marketing-ana-garcia-oliveros-el-marketing-es-el-arte-de-la-persuasion-es-tambien-la-ciencia-que-combina-la-gestion-emocional-de-las-necesidades-sociales-y-la-creacion-de-valor"),
    "pallete": f("frases-de-inbound-marketing-alex-pallete-lo-que-construye-la-marca-no-es-el-mensaje-es-la-experiencia-que-se-vive-con-ella"),
    "pulizzi_barrett": f("frases-de-inbound-marketing-joe-pulizzi-y-newt-barrett-el-marketing-boca-a-boca-ha-sido-siempre-importante-hoy-es-mas-importante-que-nunca-debido-al-poder-de-internet"),
    "reeves": f("frases-de-inbound-marketing-rosser-reeves-quieres-textos-escritos-con-elegancia-quieres-obras-maestras-o-quieres-ver-como-las-malditas-ventas-empiezan-a-subir"),
    "kawasaki": f("frases-de-inbound-marketing-guy-kawasaki-cuando-hechizas-a-la-gente-tu-meta-no-es-hacer-dinero-con-ellos-y-conseguir-lo-que-ellos-quieren-sino-darles-satisfaccion"),
    "mejide": f("frases-de-inbound-marketing-risto-mejide-si-cuando-hablas-nadie-se-molesta-eso-es-que-no-has-dicho-absolutamente-nada"),
    "godin2": f("frases-de-inbound-marketing-seth-godin-si-no-tienes-tiempo-para-hacer-las-cosas-bien-que-te-hace-pensar-que-tendras-tiempo-para-hacerlo-de-nuevo"),
    "nunez": f("frases-de-inbound-marketing-vilma-nunez-mezclar-la-parte-personal-con-la-parte-profesional-tambien-genera-beneficios-desde-que-uso-instagram-en-este-sentido-he-notado-el-cambio"),
    "baer2": f("frases-de-inbound-marketing-jay-baer-el-contenido-es-fuego-y-el-social-media-gasolina"),
    "fernandez": f("frases-de-inbound-marketing-manuel-antonio-fernandez-nunca-fue-tan-facil-crear-una-marca-nunca-fue-tan-facil-que-una-marca-resultase-irrelevante"),
    "ogilvy": f("frases-de-inbound-marketing-david-ogilvy-la-publicidad-solo-es-mala-cuando-anuncia-cosas-malas"),
    "bard": f("frases-de-inbound-marketing-mirna-bard-el-branding-no-tiene-que-ver-con-el-slogan-o-logotipo-tiene-que-ver-con-la-personalidad-de-tu-marca"),
    "peretti": f("frases-de-inbound-marketing-jonas-peretti-el-contenido-es-el-rey-pero-la-distribucion-es-la-reina-y-ella-lleva-los-pantalones"),
    "branson": f("frases-de-inbound-marketing-richard-branson-por-encima-de-todo-tienes-que-crear-algo-de-lo-que-estes-orgulloso"),
    "sacks": f("frases-de-inbound-marketing-danielle-sacks-internet-ha-convertido-lo-que-solia-ser-un-mensaje-controlado-y-unidireccional-en-un-dialogo-en-tiempo-real-con-millones-de-personas"),
    "mcdonalds": f("frases-de-inbound-marketing-mcdonalds-nuestro-jefe-de-social-media-es-el-cliente"),
    "jefferson": f("frases-de-inbound-marketing-thomas-jefferson-el-hombre-que-deja-de-hacer-publicidad-para-ahorrar-dinero-es-como-el-hombre-que-para-el-reloj-para-ahorrar-tiempo"),
    "gates": f("frases-de-inbound-marketing-bill-gates-tus-clientes-mas-infelices-son-tu-mayor-fuente-de-aprendizaje"),
    "hsieh": f("frases-de-inbound-marketing-tony-hsieh-tu-cultura-es-tu-marca"),
    "minx": f("frases-de-inbound-marketing-heidi-minx-aprende-las-reglas-despues-aprende-como-cambiarlas-y-haz-que-los-demas-las-sigan"),
    "honda": f("frases-de-inbound-marketing-soichiro-honda-trabajemos-para-ser-una-compania-que-la-sociedad-quiera-que-exista"),
}


def cita(texto, autor):
    return f"> {texto}\n>\n> **{autor}**"
