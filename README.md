# Whatplay · actualizaciones

Desde aquí se instala y se actualiza **Whatplay para Android**, un reproductor de listas de canales (M3U, W3U…) con guía de programación. El código de la app no está en este repositorio: solo lo que hace falta para instalarla y para que se actualice sola.

- **[`updates.json`](updates.json)**: lo que consulta la app para saber si hay una versión nueva: cuál es, sus novedades, de dónde descargarla y cómo comprobar que la descarga es la buena (tamaño, SHA-256 del APK y del certificado de firma).
- **[Releases](https://github.com/repotoolsapps/claqueta-updates/releases)**: cada versión, con su APK (`whatplay-<versión>.apk`) y sus novedades.

## Instalar Whatplay por primera vez

Whatplay no está en Google Play: se instala desde aquí una sola vez, en un móvil o una tablet Android (la versión mínima de Android aparece junto a la última versión, en [Novedades](#novedades)).

1. En el dispositivo, abre la **[última versión](https://github.com/repotoolsapps/claqueta-updates/releases/latest)** y, en **Assets**, toca `whatplay-<versión>.apk` para descargarlo.
2. Abre el archivo descargado, desde el aviso de descarga o desde la app de archivos (carpeta **Descargas**).
3. Android avisa de que, por seguridad, no deja instalar apps de esa fuente: toca **Ajustes**, activa **Permitir de esta fuente** (es el permiso «Instalar apps desconocidas») y vuelve atrás. En Android 7, el ajuste está en **Ajustes › Seguridad › Orígenes desconocidos**.
4. Toca **Instalar**. Si Play Protect avisa de que no conoce la app, elige instalarla igualmente.

A partir de ahí no hace falta volver por aquí: Whatplay avisa cuando hay una versión nueva, enseña sus novedades y la instala con un toque. La primera vez, Android pide el mismo permiso, esta vez para Whatplay. Si quieres, quítaselo después al navegador o a la app de archivos en **Ajustes › Aplicaciones › Acceso especial › Instalar apps desconocidas** (el camino cambia un poco de un fabricante a otro).

Para comprobar una descarga a mano, el SHA-256 de cada APK está en sus notas y en `updates.json`. En un ordenador: `shasum -a 256 whatplay-<versión>.apk` (macOS y Linux) o `certutil -hashfile whatplay-<versión>.apk SHA256` (Windows).

## Novedades

<!-- novedades:inicio -->
<!-- Este bloque lo escribe .github/workflows/publish.yml con cada versión: no lo edites a mano. -->

**Última versión para Android: 2.0.0-prueba83**, del 4 de noviembre de 2026 · Android 7.0 o superior · 46,6 MB

[Descargar whatplay-2.0.0-prueba83.apk](https://github.com/repotoolsapps/claqueta-updates/releases/download/v2.0.0-prueba83/whatplay-2.0.0-prueba83.apk) · SHA-256 `ea41d24913076d80b88d4c7debfa172a11438337ee91053c29b15d365aa4aa9e`

### 2.0.0-prueba83 · 4 de noviembre de 2026
- Whatplay, en español, inglés, francés y alemán: elige el idioma en Ajustes › Apariencia › Idioma, o deja el del móvil.
- La primera vez que abres Whatplay: una bienvenida con lo que puedes hacer (se puede saltar), las preguntas de los anuncios y de «Novedades», una guía rápida de dónde está cada cosa (se puede omitir) y la opción de quitar los anuncios con Whatplay Premium. Sale una sola vez; en la tele, solo la bienvenida.
- Whatplay se actualiza sola desde Google Play: la versión nueva se descarga mientras usas la app y «Reiniciar» la instala; si no lo pulsas, se instala al salir de la app o al volver a abrirla, nunca con un vídeo en marcha. Cuando una versión es imprescindible, te pide actualizar antes de seguir.
- Después de ver unos canales, al salir del reproductor, Google Play puede pedirte que valores Whatplay.
- El gesto de atrás hace lo mismo que el botón de atrás de cada pantalla, con la misma transición: en las listas, Favoritos, la guía, Ajustes, Sincronización y al añadir una lista, la página ya no encoge siguiendo al dedo. En las hojas de abajo, el gesto las cierra como tocar fuera.
- La guía rápida de la primera vez te enseña la app de verdad: unos bocadillos señalan Listas, «Añadir lista», Favoritos, Buscar y Ajustes, y el último cuenta el reproductor. «Omitir» o el gesto de atrás la cierran cuando quieras.
- Al enviar a la tele un canal en TS, la imagen ya no se queda parada cuando la emisión cambia por dentro (lo que pasa cuando el servidor del canal vuelve a arrancar): el móvil sigue dándole vídeo y, si el audio que convierte no llega a tiempo, sigue en silencio en vez de pararse.
- La cuenta de un proveedor (servidor, usuario y contraseña) se llama ahora «Cuenta de proveedor», en Añadir lista y en el filtro de Listas.
- Ajustes › Acerca de: la política de privacidad y los términos de uso.
- Menú lateral (el botón de tres rayas, arriba a la izquierda): Whatplay Premium, Ajustes, Sincronización, Novedades, la ayuda y el contacto con el soporte, valorar y compartir Whatplay, nuestras redes y lo legal. Y Ajustes, con un aspecto nuevo más limpio.
- Whatplay Premium, renovado: la tienda enseña lo que incluye y los dos planes, con lo que ahorras con el anual, y en el reproductor la pastilla «Quitar anuncios» (o el tiempo que te queda sin anuncios) abre una hoja para ver un vídeo y sumar 30 minutos, o hacerte Premium.
- Inicio enseña solo tus 5 últimos recientes (lo que dejaste a medias sigue en «Continuar viendo»), y con «Ocultar barras al desplazar» la cabecera ya no se queda escondida: vuelve sola al llegar arriba o cuando la lista cabe entera (por ejemplo, al filtrar o buscar) y al cambiar de lista o de pestaña.
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en Media (en su pestaña, con un buscador nuevo, y en Buscar) puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4».
- Los canales en directo cuya dirección no lleva extensión (como los de los paneles Xtream: servidor, puerto, usuario, contraseña y número) se ven aunque el servidor dé una lista HLS, redirija con un token a otro servidor, solo deje ver a reproductores como VLC o pida el vídeo por tramos; si el servidor corta el directo, se vuelve a conectar en vez de pasar al canal siguiente; el aviso de error dice por qué no se ve (con su código HTTP) o que la dirección es una lista de canales; y al pegar en «Servidor» la dirección de un canal así, salen solos el servidor, el usuario y la contraseña.
- Al abrir un canal o un vídeo, mientras carga solo se ve el círculo de carga: los botones del reproductor salen al tocar la pantalla. Y si no se puede ver, al tocar la pantalla salen también las barras de arriba y de abajo (volver, favoritos, la guía, las opciones, bloquear…), sin tapar el aviso. En vertical con la guía abierta, los botones del vídeo de arriba van en su centro, con el círculo de carga.
- En los canales en directo, el reproductor tiene abajo su barra, en el mismo sitio que la de un vídeo y con el tiempo donde siempre, y sin repetir «En directo» (ya está junto al nombre). En los que dejan volver atrás, llevar la barra al final vuelve al directo.
- Un vídeo de una web compartido desde el reproductor se abre a la primera en la otra Whatplay: se busca en su página, como lo encontró quien lo compartió (el enlace que encontró él iba con su sesión y en otro móvil no sirve).
- Recordatorios y grabaciones desde la guía, también con la app cerrada: toca un programa que aún no ha empezado (o mantén pulsado cualquiera) para que te avise antes, con la antelación que elijas y repitiendo el aviso si no lo ves, o para grabarlo, a él o a todos sus episodios. Avisa al empezar y al acabar cada grabación, y lo grabado se ve en «Recordatorios y grabaciones», en el menú lateral.
- Las letras se ven igual de gruesas en todos los móviles (en los Xiaomi salían muy finas), y la cuadrícula y «Ocultar barras al desplazar» vienen encendidos de serie.
- Al grabar puedes elegir tú el día, la hora a la que empieza y lo que dura, también en el reproductor (Opciones › «Grabar este canal», para cualquier canal aunque no tenga guía). Lo grabado sale en Inicio, en «Mis grabaciones», y la guía se llama ahora «Guía TV».
- Las estaciones web cuyo reproductor no se carga hasta tocarlo (solo enseñan su botón de reproducir) se abren solas, también al abrir un canal compartido.
- Si la web de una estación pide comprobar que eres una persona (un captcha o «pulsa para verificar que eres humano»), su página sale dentro del reproductor, sin ir al navegador: la pasas tú y el vídeo empieza ahí mismo.
- La nueva Whatplay: al actualizar, tus listas, tus favoritos y los marcadores del navegador de la versión anterior pasan solos (y si compraste quitar los anuncios, lo sigues teniendo).
- Whatplay Premium (mensual o anual) quita los anuncios; si pagaste la Whatplay de antes sin anuncios, la sigues teniendo así para siempre.
- Si sigues suscrito a Whatplay desde una versión anterior, tu suscripción también quita los anuncios mientras dure.
- Anuncios: de vez en cuando al abrir una lista, abajo del todo en el reproductor y al cambiar de canal; ver un vídeo da 30 minutos sin anuncios, acumulables.
- Ajustes › Actualizaciones › Novedades: notificaciones con las novedades de Whatplay, solo si las activas.
- Al abrir la app, las listas se actualizan en cuanto hay conexión (antes fallaban todas como si no hubiera internet), y todas aunque una no se pueda descargar.
- Con «Ocultar barras al desplazar», también se esconde la barra de arriba de las listas y de tus favoritos, y la página llega hasta abajo del todo, sin una franja negra.
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google (en tu Google Drive) o con Apple (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba82 · 4 de noviembre de 2026
- Whatplay, en español, inglés, francés y alemán: elige el idioma en Ajustes › Apariencia › Idioma, o deja el del móvil.
- La primera vez que abres Whatplay: una bienvenida con lo que puedes hacer (se puede saltar), las preguntas de los anuncios y de «Novedades», una guía rápida de dónde está cada cosa (se puede omitir) y la opción de quitar los anuncios con Whatplay Premium. Sale una sola vez; en la tele, solo la bienvenida.
- Whatplay se actualiza sola desde Google Play: la versión nueva se descarga mientras usas la app y «Reiniciar» la instala; si no lo pulsas, se instala al salir de la app o al volver a abrirla, nunca con un vídeo en marcha. Cuando una versión es imprescindible, te pide actualizar antes de seguir.
- Después de ver unos canales, al salir del reproductor, Google Play puede pedirte que valores Whatplay.
- El gesto de atrás hace lo mismo que el botón de atrás de cada pantalla, con la misma transición: en las listas, Favoritos, la guía, Ajustes, Sincronización y al añadir una lista, la página ya no encoge siguiendo al dedo. En las hojas de abajo, el gesto las cierra como tocar fuera.
- La guía rápida de la primera vez te enseña la app de verdad: unos bocadillos señalan Listas, «Añadir lista», Favoritos, Buscar y Ajustes, y el último cuenta el reproductor. «Omitir» o el gesto de atrás la cierran cuando quieras.
- Al enviar a la tele un canal en TS, la imagen ya no se queda parada cuando la emisión cambia por dentro (lo que pasa cuando el servidor del canal vuelve a arrancar): el móvil sigue dándole vídeo y, si el audio que convierte no llega a tiempo, sigue en silencio en vez de pararse.
- La cuenta de un proveedor (servidor, usuario y contraseña) se llama ahora «Cuenta de proveedor», en Añadir lista y en el filtro de Listas.
- Ajustes › Acerca de: la política de privacidad y los términos de uso.
- Menú lateral (el botón de tres rayas, arriba a la izquierda): Whatplay Premium, Ajustes, Sincronización, Novedades, la ayuda y el contacto con el soporte, valorar y compartir Whatplay, nuestras redes y lo legal. Y Ajustes, con un aspecto nuevo más limpio.
- Whatplay Premium, renovado: la tienda enseña lo que incluye y los dos planes, con lo que ahorras con el anual, y en el reproductor la pastilla «Quitar anuncios» (o el tiempo que te queda sin anuncios) abre una hoja para ver un vídeo y sumar 30 minutos, o hacerte Premium.
- Inicio enseña solo tus 5 últimos recientes (lo que dejaste a medias sigue en «Continuar viendo»), y con «Ocultar barras al desplazar» la cabecera ya no se queda escondida: vuelve sola al llegar arriba o cuando la lista cabe entera (por ejemplo, al filtrar o buscar) y al cambiar de lista o de pestaña.
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en Media (en su pestaña, con un buscador nuevo, y en Buscar) puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4».
- Los canales en directo cuya dirección no lleva extensión (como los de los paneles Xtream: servidor, puerto, usuario, contraseña y número) se ven aunque el servidor dé una lista HLS, redirija con un token a otro servidor, solo deje ver a reproductores como VLC o pida el vídeo por tramos; si el servidor corta el directo, se vuelve a conectar en vez de pasar al canal siguiente; el aviso de error dice por qué no se ve (con su código HTTP) o que la dirección es una lista de canales; y al pegar en «Servidor» la dirección de un canal así, salen solos el servidor, el usuario y la contraseña.
- Al abrir un canal o un vídeo, mientras carga solo se ve el círculo de carga: los botones del reproductor salen al tocar la pantalla. Y si no se puede ver, al tocar la pantalla salen también las barras de arriba y de abajo (volver, favoritos, la guía, las opciones, bloquear…), sin tapar el aviso. En vertical con la guía abierta, los botones del vídeo de arriba van en su centro, con el círculo de carga.
- En los canales en directo, el reproductor tiene abajo su barra, en el mismo sitio que la de un vídeo y con el tiempo donde siempre, y sin repetir «En directo» (ya está junto al nombre). En los que dejan volver atrás, llevar la barra al final vuelve al directo.
- Un vídeo de una web compartido desde el reproductor se abre a la primera en la otra Whatplay: se busca en su página, como lo encontró quien lo compartió (el enlace que encontró él iba con su sesión y en otro móvil no sirve).
- Recordatorios y grabaciones desde la guía, también con la app cerrada: toca un programa que aún no ha empezado (o mantén pulsado cualquiera) para que te avise antes, con la antelación que elijas y repitiendo el aviso si no lo ves, o para grabarlo, a él o a todos sus episodios. Avisa al empezar y al acabar cada grabación, y lo grabado se ve en «Recordatorios y grabaciones», en el menú lateral.
- Las letras se ven igual de gruesas en todos los móviles (en los Xiaomi salían muy finas), y la cuadrícula y «Ocultar barras al desplazar» vienen encendidos de serie.
- Al grabar puedes elegir tú el día, la hora a la que empieza y lo que dura, también en el reproductor (Opciones › «Grabar este canal», para cualquier canal aunque no tenga guía). Lo grabado sale en Inicio, en «Mis grabaciones», y la guía se llama ahora «Guía TV».
- Las estaciones web cuyo reproductor no se carga hasta tocarlo (solo enseñan su botón de reproducir) se abren solas, también al abrir un canal compartido.
- La nueva Whatplay: al actualizar, tus listas, tus favoritos y los marcadores del navegador de la versión anterior pasan solos (y si compraste quitar los anuncios, lo sigues teniendo).
- Whatplay Premium (mensual o anual) quita los anuncios; si pagaste la Whatplay de antes sin anuncios, la sigues teniendo así para siempre.
- Si sigues suscrito a Whatplay desde una versión anterior, tu suscripción también quita los anuncios mientras dure.
- Anuncios: de vez en cuando al abrir una lista, abajo del todo en el reproductor y al cambiar de canal; ver un vídeo da 30 minutos sin anuncios, acumulables.
- Ajustes › Actualizaciones › Novedades: notificaciones con las novedades de Whatplay, solo si las activas.
- Al abrir la app, las listas se actualizan en cuanto hay conexión (antes fallaban todas como si no hubiera internet), y todas aunque una no se pueda descargar.
- Con «Ocultar barras al desplazar», también se esconde la barra de arriba de las listas y de tus favoritos, y la página llega hasta abajo del todo, sin una franja negra.
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google (en tu Google Drive) o con Apple (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba69 · 4 de noviembre de 2026
- Whatplay, en español, inglés, francés y alemán: elige el idioma en Ajustes › Apariencia › Idioma, o deja el del móvil.
- La primera vez que abres Whatplay: una bienvenida con lo que puedes hacer (se puede saltar), las preguntas de los anuncios y de «Novedades», una guía rápida de dónde está cada cosa (se puede omitir) y la opción de quitar los anuncios con Whatplay Premium. Sale una sola vez; en la tele, solo la bienvenida.
- Whatplay se actualiza sola desde Google Play: la versión nueva se descarga mientras usas la app y «Reiniciar» la instala; si no lo pulsas, se instala al salir de la app o al volver a abrirla, nunca con un vídeo en marcha. Cuando una versión es imprescindible, te pide actualizar antes de seguir.
- Después de ver unos canales, al salir del reproductor, Google Play puede pedirte que valores Whatplay.
- El gesto de atrás hace lo mismo que el botón de atrás de cada pantalla, con la misma transición: en las listas, Favoritos, la guía, Ajustes, Sincronización y al añadir una lista, la página ya no encoge siguiendo al dedo. En las hojas de abajo, el gesto las cierra como tocar fuera.
- La guía rápida de la primera vez te enseña la app de verdad: unos bocadillos señalan Listas, «Añadir lista», Favoritos, Buscar y Ajustes, y el último cuenta el reproductor. «Omitir» o el gesto de atrás la cierran cuando quieras.
- Al enviar a la tele un canal en TS, la imagen ya no se queda parada cuando la emisión cambia por dentro (lo que pasa cuando el servidor del canal vuelve a arrancar): el móvil sigue dándole vídeo y, si el audio que convierte no llega a tiempo, sigue en silencio en vez de pararse.
- La cuenta de un proveedor (servidor, usuario y contraseña) se llama ahora «Cuenta de proveedor», en Añadir lista y en el filtro de Listas.
- Ajustes › Acerca de: la política de privacidad y los términos de uso.
- Menú lateral (el botón de tres rayas, arriba a la izquierda): Whatplay Premium, Ajustes, Sincronización, Novedades, la ayuda y el contacto con el soporte, valorar y compartir Whatplay, nuestras redes y lo legal. Y Ajustes, con un aspecto nuevo más limpio.
- Whatplay Premium, renovado: la tienda enseña lo que incluye y los dos planes, con lo que ahorras con el anual, y en el reproductor la pastilla «Quitar anuncios» (o el tiempo que te queda sin anuncios) abre una hoja para ver un vídeo y sumar 30 minutos, o hacerte Premium.
- Inicio enseña solo tus 5 últimos recientes (lo que dejaste a medias sigue en «Continuar viendo»), y con «Ocultar barras al desplazar» la cabecera ya no se queda escondida: vuelve sola al llegar arriba o cuando la lista cabe entera (por ejemplo, al filtrar o buscar) y al cambiar de lista o de pestaña.
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en Media (en su pestaña, con un buscador nuevo, y en Buscar) puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4».
- Los canales en directo cuya dirección no lleva extensión (como los de los paneles Xtream: servidor, puerto, usuario, contraseña y número) se ven aunque el servidor dé una lista HLS, redirija con un token a otro servidor, solo deje ver a reproductores como VLC o pida el vídeo por tramos; si el servidor corta el directo, se vuelve a conectar en vez de pasar al canal siguiente; el aviso de error dice por qué no se ve (con su código HTTP) o que la dirección es una lista de canales; y al pegar en «Servidor» la dirección de un canal así, salen solos el servidor, el usuario y la contraseña.
- La nueva Whatplay: al actualizar, tus listas, tus favoritos y los marcadores del navegador de la versión anterior pasan solos (y si compraste quitar los anuncios, lo sigues teniendo).
- Whatplay Premium (mensual o anual) quita los anuncios; si pagaste la Whatplay de antes sin anuncios, la sigues teniendo así para siempre.
- Si sigues suscrito a Whatplay desde una versión anterior, tu suscripción también quita los anuncios mientras dure.
- Anuncios: de vez en cuando al abrir una lista, abajo del todo en el reproductor y al cambiar de canal; ver un vídeo da 30 minutos sin anuncios, acumulables.
- Ajustes › Actualizaciones › Novedades: notificaciones con las novedades de Whatplay, solo si las activas.
- Al abrir la app, las listas se actualizan en cuanto hay conexión (antes fallaban todas como si no hubiera internet), y todas aunque una no se pueda descargar.
- Con «Ocultar barras al desplazar», también se esconde la barra de arriba de las listas y de tus favoritos, y la página llega hasta abajo del todo, sin una franja negra.
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google (en tu Google Drive) o con Apple (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba68 · 4 de noviembre de 2026
- Whatplay, en español, inglés, francés y alemán: elige el idioma en Ajustes › Apariencia › Idioma, o deja el del móvil.
- La primera vez que abres Whatplay: una bienvenida con lo que puedes hacer (se puede saltar), las preguntas de los anuncios y de «Novedades», una guía rápida de dónde está cada cosa (se puede omitir) y la opción de quitar los anuncios con Whatplay Premium. Sale una sola vez; en la tele, solo la bienvenida.
- Whatplay se actualiza sola desde Google Play: la versión nueva se descarga mientras usas la app y «Reiniciar» la instala; si no lo pulsas, se instala al salir de la app o al volver a abrirla, nunca con un vídeo en marcha. Cuando una versión es imprescindible, te pide actualizar antes de seguir.
- Después de ver unos canales, al salir del reproductor, Google Play puede pedirte que valores Whatplay.
- El gesto de atrás hace lo mismo que el botón de atrás de cada pantalla, con la misma transición: en las listas, Favoritos, la guía, Ajustes, Sincronización y al añadir una lista, la página ya no encoge siguiendo al dedo. En las hojas de abajo, el gesto las cierra como tocar fuera.
- La guía rápida de la primera vez te enseña la app de verdad: unos bocadillos señalan Listas, «Añadir lista», Favoritos, Buscar y Ajustes, y el último cuenta el reproductor. «Omitir» o el gesto de atrás la cierran cuando quieras.
- Al enviar a la tele un canal en TS, la imagen ya no se queda parada cuando la emisión cambia por dentro (lo que pasa cuando el servidor del canal vuelve a arrancar): el móvil sigue dándole vídeo y, si el audio que convierte no llega a tiempo, sigue en silencio en vez de pararse.
- La cuenta de un proveedor (servidor, usuario y contraseña) se llama ahora «Cuenta de proveedor», en Añadir lista y en el filtro de Listas.
- Ajustes › Acerca de: la política de privacidad y los términos de uso.
- Menú lateral (el botón de tres rayas, arriba a la izquierda): Whatplay Premium, Ajustes, Sincronización, Novedades, la ayuda y el contacto con el soporte, valorar y compartir Whatplay, nuestras redes y lo legal. Y Ajustes, con un aspecto nuevo más limpio.
- Whatplay Premium, renovado: la tienda enseña lo que incluye y los dos planes, con lo que ahorras con el anual, y en el reproductor la pastilla «Quitar anuncios» (o el tiempo que te queda sin anuncios) abre una hoja para ver un vídeo y sumar 30 minutos, o hacerte Premium.
- Inicio enseña solo tus 5 últimos recientes (lo que dejaste a medias sigue en «Continuar viendo»), y con «Ocultar barras al desplazar» la cabecera ya no se queda escondida: vuelve sola al llegar arriba o cuando la lista cabe entera (por ejemplo, al filtrar o buscar) y al cambiar de lista o de pestaña.
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en Media (en su pestaña, con un buscador nuevo, y en Buscar) puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4».
- La nueva Whatplay: al actualizar, tus listas, tus favoritos y los marcadores del navegador de la versión anterior pasan solos (y si compraste quitar los anuncios, lo sigues teniendo).
- Whatplay Premium (mensual o anual) quita los anuncios; si pagaste la Whatplay de antes sin anuncios, la sigues teniendo así para siempre.
- Si sigues suscrito a Whatplay desde una versión anterior, tu suscripción también quita los anuncios mientras dure.
- Anuncios: de vez en cuando al abrir una lista, abajo del todo en el reproductor y al cambiar de canal; ver un vídeo da 30 minutos sin anuncios, acumulables.
- Ajustes › Actualizaciones › Novedades: notificaciones con las novedades de Whatplay, solo si las activas.
- Al abrir la app, las listas se actualizan en cuanto hay conexión (antes fallaban todas como si no hubiera internet), y todas aunque una no se pueda descargar.
- Con «Ocultar barras al desplazar», también se esconde la barra de arriba de las listas y de tus favoritos, y la página llega hasta abajo del todo, sin una franja negra.
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google (en tu Google Drive) o con Apple (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba67 · 4 de noviembre de 2026
- Whatplay, en español, inglés, francés y alemán: elige el idioma en Ajustes › Apariencia › Idioma, o deja el del móvil.
- La primera vez que abres Whatplay: una bienvenida con lo que puedes hacer (se puede saltar), las preguntas de los anuncios y de «Novedades», una guía rápida de dónde está cada cosa (se puede omitir) y la opción de quitar los anuncios con Whatplay Premium. Sale una sola vez; en la tele, solo la bienvenida.
- Whatplay se actualiza sola desde Google Play: la versión nueva se descarga mientras usas la app y «Reiniciar» la instala; si no lo pulsas, se instala al salir de la app o al volver a abrirla, nunca con un vídeo en marcha. Cuando una versión es imprescindible, te pide actualizar antes de seguir.
- Después de ver unos canales, al salir del reproductor, Google Play puede pedirte que valores Whatplay.
- El gesto de atrás hace lo mismo que el botón de atrás de cada pantalla, con la misma transición: en las listas, Favoritos, la guía, Ajustes, Sincronización y al añadir una lista, la página ya no encoge siguiendo al dedo. En las hojas de abajo, el gesto las cierra como tocar fuera.
- La guía rápida de la primera vez te enseña la app de verdad: unos bocadillos señalan Listas, «Añadir lista», Favoritos, Buscar y Ajustes, y el último cuenta el reproductor. «Omitir» o el gesto de atrás la cierran cuando quieras.
- Al enviar a la tele un canal en TS, la imagen ya no se queda parada cuando la emisión cambia por dentro (lo que pasa cuando el servidor del canal vuelve a arrancar): el móvil sigue dándole vídeo y, si el audio que convierte no llega a tiempo, sigue en silencio en vez de pararse.
- La cuenta de un proveedor (servidor, usuario y contraseña) se llama ahora «Cuenta de proveedor», en Añadir lista y en el filtro de Listas.
- Ajustes › Acerca de: la política de privacidad y los términos de uso.
- Menú lateral (el botón de tres rayas, arriba a la izquierda): Whatplay Premium, Ajustes, Sincronización, Novedades, la ayuda y el contacto con el soporte, valorar y compartir Whatplay, nuestras redes y lo legal. Y Ajustes, con un aspecto nuevo más limpio.
- Whatplay Premium, renovado: la tienda enseña lo que incluye y los dos planes, con lo que ahorras con el anual, y en el reproductor la pastilla «Quitar anuncios» (o el tiempo que te queda sin anuncios) abre una hoja para ver un vídeo y sumar 30 minutos, o hacerte Premium.
- Inicio enseña solo tus 5 últimos recientes (lo que dejaste a medias sigue en «Continuar viendo»), y con «Ocultar barras al desplazar» la cabecera ya no se queda escondida: vuelve sola al llegar arriba o cuando la lista cabe entera (por ejemplo, al filtrar o buscar) y al cambiar de lista o de pestaña.
- La nueva Whatplay: al actualizar, tus listas, tus favoritos y los marcadores del navegador de la versión anterior pasan solos (y si compraste quitar los anuncios, lo sigues teniendo).
- Whatplay Premium (mensual o anual) quita los anuncios; si pagaste la Whatplay de antes sin anuncios, la sigues teniendo así para siempre.
- Si sigues suscrito a Whatplay desde una versión anterior, tu suscripción también quita los anuncios mientras dure.
- Anuncios: de vez en cuando al abrir una lista, abajo del todo en el reproductor y al cambiar de canal; ver un vídeo da 30 minutos sin anuncios, acumulables.
- Ajustes › Actualizaciones › Novedades: notificaciones con las novedades de Whatplay, solo si las activas.
- Al abrir la app, las listas se actualizan en cuanto hay conexión (antes fallaban todas como si no hubiera internet), y todas aunque una no se pueda descargar.
- Con «Ocultar barras al desplazar», también se esconde la barra de arriba de las listas y de tus favoritos, y la página llega hasta abajo del todo, sin una franja negra.
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google (en tu Google Drive) o con Apple (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 0.17.0-prueba15 · 3 de noviembre de 2026
- Versión de prueba.
- Enviar a la tele (Chromecast, Google TV y teles con Chromecast): lo que suena se ve en la tele y el reproductor la maneja. Lo que la tele no abre tal cual (MKV, AVI, FLV, vídeo Xvid, DivX, MPEG-2 o VC-1, audio AC-3, E-AC-3, MP2, DTS o TrueHD) se convierte en el móvil, también el audio de los canales en directo. En «Ajustes», «Convertir vídeo para la tele»: Preguntar, Siempre o Nunca.
- Mientras se envía, la tarjeta de «Continuar viendo» de Inicio maneja la tele: progreso, pausa, ±10 s y «Dejar de enviar».
- Listas Xtream Codes: añade tu cuenta con el servidor, el usuario y la contraseña, con sus canales, películas, series y guía.
- «Novedades» en Inicio: lo último que han añadido tus listas.
- FFmpeg vuelve para el audio que el móvil no sabe abrir (DTS, TrueHD, MP2, AC-3 donde falte).
- Los AVI de «Media» se ven con imagen y sonido.
- Navegador: ya no te lleva a la publicidad, los favoritos de vídeos de una web vuelven a buscar el vídeo al abrirlos (no caducan), carga reproductores que rechazaban a las apps y muestra los PDF.

### 0.16.5 · 29 de octubre de 2026
- La app pesa unos 15 MB menos.
- Por ahora, el motor FFmpeg usa los decodificadores del sistema por software: FFmpeg vuelve en la próxima versión.
- Los canales RTMP (rtmp://) ya no se reproducen: al abrirlos, la app lo dice.
- Ya no hay versión para aparatos con procesador x86 de 32 bits.

### 0.16.4 · 29 de octubre de 2026
- Torrents: los enlaces magnet y los archivos .torrent se ven en el reproductor mientras se descargan, desde tus listas, el navegador, otras apps o «Añadir lista» (desde Android 9). Mientras carga, se ve con cuántas fuentes y a qué velocidad.
- Lo descargado de un torrent se borra solo, y al dejar de verlo deja de compartirse. Con datos móviles, la app pregunta antes de empezar. Como en cualquier programa de torrents, quienes comparten el mismo ven tu dirección IP.
- En Android 17, para abrir canales, listas o páginas de tu red de casa (un NAS, un servidor o un descodificador), Claqueta necesita el permiso «Dispositivos cercanos»: lo pide al abrirlos y, si falta, lo dice enseguida con «Permitir», en vez de quedarse cargando.
- Mientras un canal carga, el botón central enseña pausa y la pone, y cerrar el reproductor mientras un vídeo aún carga lo para del todo, sin que suene después.

### 0.16.3 · 29 de octubre de 2026
- Cerrar la ventana flotante cierra el reproductor: el vídeo deja de sonar (en algunos móviles seguía de fondo) y lo que se buscaba termina.
- Mientras se busca el vídeo de una estación web, el reproductor está en pausa de verdad: no mantiene el móvil despierto ni la notificación dice que suena, y apagar la pantalla un momento ya no hace empezar de cero.
- Dos estaciones con la misma web, una tras otra, buscan cada una su vídeo; antes la segunda se quedaba girando.
- Con datos móviles, pasar a otro canal o darle a reproducir desde la notificación, unos auriculares o la ventana flotante ya no cuenta como aceptar, y la pregunta es siempre por lo que suena.
- La página de un canal que pasa al navegador solo se abre cuando se ve el reproductor; si se cierra antes, ya no se abre sola después.
- Reintentar vuelve a buscar en su web el vídeo que caducó, y al volver a la app durante una búsqueda ya no aparece un error antiguo.

### 0.16.2 · 29 de octubre de 2026
- Las estaciones web abren el reproductor al momento: mientras se busca su vídeo gira su círculo de carga, sin la pantalla negra de antes, y el vídeo empieza ahí mismo.
- Al cambiar a otra estación web con anterior, siguiente o la guía, solo gira el círculo del reproductor.
- Si un canal web no se puede abrir, el reproductor dice por qué y ofrece Reintentar, Otra opción o Siguiente.
- Si una web tarda más de lo normal, se puede ver su página; si pide elegir en su aviso de cookies, pasa al navegador y el vídeo se abre solo después.
- En la ventana flotante, la búsqueda sigue y el vídeo empieza en ella.

### 0.16.1 · 29 de octubre de 2026
- En vertical, el vídeo se ve centrado; al abrir la guía sube arriba y la guía aparece debajo, como en horizontal.
- Desde «Continuar viendo», el reproductor enseña esa lista para cambiar de canal.
- Con datos móviles, lo que suena se para y pregunta también con la pantalla apagada o en la ventana flotante, y los canales de internet de la cola no se cargan antes de aceptar.
- El candado del reproductor mantiene la orientación aunque se bloquee el móvil.
- Actualizaciones: avisos claros si el Bloqueador automático de Samsung, Play Protect o una protección del sistema no dejan instalar, y nunca se instalan con un vídeo en marcha.
- Avisos más cortos cuando un canal web no se puede abrir.

### 0.16.0 · 28 de octubre de 2026
- La app se actualiza sola: avisa cuando hay una versión nueva, enseña sus novedades y la instala con un toque.
- En Ajustes › Acerca de: la versión instalada, buscar actualizaciones y las novedades de cada versión.
- Desde Recientes y Favoritos, el reproductor enseña la guía de esos canales y cambia de canal sin salir de la lista.
- Con datos móviles, el reproductor pregunta antes de empezar un canal de internet.
- Las estaciones web cuentan como canales normales, también para anterior y siguiente; la etiqueta WEB queda solo para las páginas que se abren tal cual.
- La guía del reproductor enseña solo lo que hay: los canales, la programación, las dos o ninguna.
- «Continuar viendo» guarda cualquier vídeo que dejes a medias, aunque después cambies muchas veces de canal.
- Las películas de webs de vídeo se encuentran mejor con una conexión lenta, y si no se pueden abrir, la app dice por qué.
<!-- novedades:fin -->

## Cómo llegan aquí las versiones

Cada versión se compila y se firma en el repositorio privado de Whatplay, que la entrega en la rama `incoming` de este repositorio: el APK y un `release.json` que lo describe. Entonces [`publish.yml`](.github/workflows/publish.yml):

1. comprueba la entrega: el tamaño y el SHA-256 del APK, y que su `versionCode` sea mayor que el publicado;
2. crea la release `v<versión>` con el APK y sus novedades;
3. actualiza en `main` el archivo `updates.json` y estas novedades;
4. borra la rama `incoming`, para que el APK no se quede en el historial de git: solo vive en su release.

Si algo falla a medias, se puede volver a ejecutar sin miedo: lo que ya estaba hecho no cambia.

### updates.json

| Campo | Qué es |
|---|---|
| `schema` | La versión del formato: 1. Si una app no conoce el esquema, no lo usa. |
| `app` | `com.repotools.whatplay` |
| `updated` | Cuándo cambió el archivo por última vez (UTC). |
| `android` | La versión actual para Android, o `null` si aún no hay ninguna: `versionCode`, `versionName`, `date`, `minSdk`, `url` del APK, `size` en bytes, `sha256` del APK y `certSha256`, el SHA-256 del certificado con el que está firmado. |
| `ios` | Reservado para cuando haya versión para iPhone y iPad; mientras tanto, `null`. |
| `releases` | Las novedades de cada versión publicada, de la más nueva a la más antigua: `version`, `date`, `platforms` y `notes`. |

Quien lee el archivo ignora los campos que no conoce.
