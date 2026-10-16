<?php
/**
 * Plugin Name: Inbound: corrige URLs con la IP del servidor
 * Description: Sustituye http://3.145.105.128 por https://www.inbound.com.mx en las opciones guardadas (una sola vez) y en el HTML de salida. Corrige el logo móvil del tema Rehub y cualquier otra referencia a la IP.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'INBOUND_IP_VIEJA', 'http://3.145.105.128' );
define( 'INBOUND_HOST_NUEVO', 'https://www.inbound.com.mx' );

/**
 * Reemplazo recursivo en cadenas, arrays y objetos (opciones serializadas).
 */
function inbound_ip_reemplazar( $valor ) {
	if ( is_string( $valor ) ) {
		return str_replace( array( INBOUND_IP_VIEJA, 'https://3.145.105.128' ), INBOUND_HOST_NUEVO, $valor );
	}
	if ( is_array( $valor ) ) {
		foreach ( $valor as $k => $v ) {
			$valor[ $k ] = inbound_ip_reemplazar( $v );
		}
		return $valor;
	}
	if ( is_object( $valor ) ) {
		foreach ( get_object_vars( $valor ) as $k => $v ) {
			$valor->$k = inbound_ip_reemplazar( $v );
		}
	}
	return $valor;
}

/**
 * Corrección única de las opciones de la base de datos (theme options de Rehub,
 * theme_mods, widgets, etc.). Se ejecuta una vez; para repetirla, borrar la opción
 * inbound_ip_corregida.
 */
add_action( 'init', function () {
	if ( get_option( 'inbound_ip_corregida' ) ) {
		return;
	}
	global $wpdb;
	$nombres = $wpdb->get_col(
		$wpdb->prepare( "SELECT option_name FROM {$wpdb->options} WHERE option_value LIKE %s", '%3.145.105.128%' )
	);
	$corregidas = array();
	foreach ( $nombres as $nombre ) {
		$actual = get_option( $nombre );
		$nuevo  = inbound_ip_reemplazar( $actual );
		if ( $nuevo !== $actual && update_option( $nombre, $nuevo ) ) {
			$corregidas[] = $nombre;
		}
	}
	update_option( 'inbound_ip_corregida', array( 'fecha' => current_time( 'mysql' ), 'opciones' => $corregidas ), false );
}, 5 );

/**
 * Red de seguridad: reemplaza la IP en el HTML final del sitio público.
 */
add_action( 'template_redirect', function () {
	if ( is_admin() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) {
		return;
	}
	ob_start( function ( $html ) {
		return str_replace( array( INBOUND_IP_VIEJA, 'https://3.145.105.128' ), INBOUND_HOST_NUEVO, $html );
	} );
}, 0 );
