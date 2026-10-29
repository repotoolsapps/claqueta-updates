# Claqueta · actualizaciones

Desde aquí se instala y se actualiza **Claqueta para Android**, un reproductor de listas de canales (M3U, W3U…) con guía de programación. El código de la app no está en este repositorio: solo lo que hace falta para instalarla y para que se actualice sola.

- **[`updates.json`](updates.json)**: lo que consulta la app para saber si hay una versión nueva: cuál es, sus novedades, de dónde descargarla y cómo comprobar que la descarga es la buena (tamaño, SHA-256 del APK y del certificado de firma).
- **[Releases](https://github.com/repotoolsapps/claqueta-updates/releases)**: cada versión, con su APK (`claqueta-<versión>.apk`) y sus novedades.

## Instalar Claqueta por primera vez

Claqueta no está en Google Play: se instala desde aquí una sola vez, en un móvil o una tablet Android (la versión mínima de Android aparece junto a la última versión, en [Novedades](#novedades)).

1. En el dispositivo, abre la **[última versión](https://github.com/repotoolsapps/claqueta-updates/releases/latest)** y, en **Assets**, toca `claqueta-<versión>.apk` para descargarlo.
2. Abre el archivo descargado, desde el aviso de descarga o desde la app de archivos (carpeta **Descargas**).
3. Android avisa de que, por seguridad, no deja instalar apps de esa fuente: toca **Ajustes**, activa **Permitir de esta fuente** (es el permiso «Instalar apps desconocidas») y vuelve atrás. En Android 7, el ajuste está en **Ajustes › Seguridad › Orígenes desconocidos**.
4. Toca **Instalar**. Si Play Protect avisa de que no conoce la app, elige instalarla igualmente.

A partir de ahí no hace falta volver por aquí: Claqueta avisa cuando hay una versión nueva, enseña sus novedades y la instala con un toque. La primera vez, Android pide el mismo permiso, esta vez para Claqueta. Si quieres, quítaselo después al navegador o a la app de archivos en **Ajustes › Aplicaciones › Acceso especial › Instalar apps desconocidas** (el camino cambia un poco de un fabricante a otro).

Para comprobar una descarga a mano, el SHA-256 de cada APK está en sus notas y en `updates.json`. En un ordenador: `shasum -a 256 claqueta-<versión>.apk` (macOS y Linux) o `certutil -hashfile claqueta-<versión>.apk SHA256` (Windows).

## Novedades

<!-- novedades:inicio -->
<!-- Este bloque lo escribe .github/workflows/publish.yml con cada versión: no lo edites a mano. -->

**Última versión para Android: 0.16.4**, del 29 de octubre de 2026 · Android 7.0 o superior · 37,4 MB

[Descargar claqueta-0.16.4.apk](https://github.com/repotoolsapps/claqueta-updates/releases/download/v0.16.4/claqueta-0.16.4.apk) · SHA-256 `0806d1800d78f01a1d6df70bfb792696c48f0f47a5a23e9f41dff8e52cdf9d24`

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

Cada versión se compila y se firma en el repositorio privado de Claqueta, que la entrega en la rama `incoming` de este repositorio: el APK y un `release.json` que lo describe. Entonces [`publish.yml`](.github/workflows/publish.yml):

1. comprueba la entrega: el tamaño y el SHA-256 del APK, y que su `versionCode` sea mayor que el publicado;
2. crea la release `v<versión>` con el APK y sus novedades;
3. actualiza en `main` el archivo `updates.json` y estas novedades;
4. borra la rama `incoming`, para que el APK no se quede en el historial de git: solo vive en su release.

Si algo falla a medias, se puede volver a ejecutar sin miedo: lo que ya estaba hecho no cambia.

### updates.json

| Campo | Qué es |
|---|---|
| `schema` | La versión del formato: 1. Si una app no conoce el esquema, no lo usa. |
| `app` | `com.repotools.claqueta` |
| `updated` | Cuándo cambió el archivo por última vez (UTC). |
| `android` | La versión actual para Android, o `null` si aún no hay ninguna: `versionCode`, `versionName`, `date`, `minSdk`, `url` del APK, `size` en bytes, `sha256` del APK y `certSha256`, el SHA-256 del certificado con el que está firmado. |
| `ios` | Reservado para cuando haya versión para iPhone y iPad; mientras tanto, `null`. |
| `releases` | Las novedades de cada versión publicada, de la más nueva a la más antigua: `version`, `date`, `platforms` y `notes`. |

Quien lee el archivo ignora los campos que no conoce.
