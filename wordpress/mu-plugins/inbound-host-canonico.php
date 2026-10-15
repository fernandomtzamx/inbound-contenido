<?php
/**
 * Plugin Name: Inbound: host canónico
 * Description: Redirige con 301 cualquier petición que llegue por un host distinto de
 *              www.inbound.com.mx (mail.inbound.com.mx, inbound.com.mx, la IP del servidor, etc.)
 *              a la misma ruta en https://www.inbound.com.mx. Evita que Google indexe el sitio
 *              duplicado bajo otros hosts. Cuando el host no es el canónico también manda
 *              X-Robots-Tag: noindex por si algo impide la redirección.
 *
 * Instalación: subir este archivo a wp-content/mu-plugins/ (se activa solo).
 */

if (PHP_SAPI === 'cli' || (defined('WP_CLI') && WP_CLI)) {
    return;
}

$inbound_host_canonico = 'www.inbound.com.mx';

$inbound_host_actual = isset($_SERVER['HTTP_HOST']) ? strtolower(trim($_SERVER['HTTP_HOST'])) : '';
$inbound_host_actual = preg_replace('/:\d+$/', '', $inbound_host_actual);

if ($inbound_host_actual === '' || $inbound_host_actual === $inbound_host_canonico) {
    return;
}

// Hosts internos que no deben redirigirse (cron, pruebas locales).
if (in_array($inbound_host_actual, array('localhost', '127.0.0.1'), true)) {
    return;
}

$inbound_ruta = isset($_SERVER['REQUEST_URI']) ? $_SERVER['REQUEST_URI'] : '/';
if ($inbound_ruta === '' || $inbound_ruta[0] !== '/') {
    $inbound_ruta = '/' . ltrim($inbound_ruta, '/');
}

// Sin cabeceras de caché: LiteSpeed/Cloudflare no deben servir la copia duplicada.
header('X-Robots-Tag: noindex, nofollow', true);
header('Cache-Control: no-store, max-age=0', true);
header('Location: https://' . $inbound_host_canonico . $inbound_ruta, true, 301);
exit;
