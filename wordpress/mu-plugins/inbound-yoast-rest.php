<?php
/**
 * Plugin Name: Inbound: campos de Yoast en la API REST
 * Description: Permite leer y escribir el title y la meta description de Yoast por la API REST
 *              (solo usuarios que pueden editar entradas). Lo usa el pipeline de inbound-contenido.
 *
 * Instalación: subir este archivo a wp-content/mu-plugins/ (se activa solo).
 */

add_action('init', function () {
    $keys = array('_yoast_wpseo_title', '_yoast_wpseo_metadesc');
    foreach (array('post', 'page') as $type) {
        foreach ($keys as $key) {
            register_post_meta($type, $key, array(
                'type'              => 'string',
                'single'            => true,
                'show_in_rest'      => true,
                'sanitize_callback' => 'sanitize_text_field',
                'auth_callback'     => function () {
                    return current_user_can('edit_posts');
                },
            ));
        }
    }
});
