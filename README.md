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

**Última versión para Android: 0.16.0**, del 28 de octubre de 2026 · Android 7.0 o superior · 40,7 MB

[Descargar claqueta-0.16.0.apk](https://github.com/repotoolsapps/claqueta-updates/releases/download/v0.16.0/claqueta-0.16.0.apk) · SHA-256 `0e2864ebc960060c2b766c9ad4071cc34a5c598aed5dce5883c7d803d416610e`

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
