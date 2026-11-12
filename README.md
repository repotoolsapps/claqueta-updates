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

**Última versión para Android: 2.0.26**, del 12 de noviembre de 2026 · Android 7.0 o superior · 38,0 MB

[Descargar whatplay-2.0.26.apk](https://whatplay.es/apk/whatplay-2.0.26.apk) · SHA-256 `3c9821910d74e51c4acf0f9ca57dd19b958f1ae67c1ed5928f70efe52731bae3`

### 2.0.26 · 12 de noviembre de 2026
- La guía de TV que trae una lista se importa sola al añadirla o al actualizarla, como la de una cuenta Xtream, también en las listas que ya tenías. Las que desactives o elimines en «Editar guías» no vuelven solas.
- Envía tus guías de TV a la tele con Whatplay, como las listas: en «Editar guías», «Compartir» › «Enviar a una tele con Whatplay». Las teles con una versión de antes siguen recibiendo las listas como siempre.
- Android TV: cuando sale una versión nueva, y después de actualizar, el botón «Actualizar» o «Entendido» ya está elegido: con OK se actualiza o se cierra sin bajar por las novedades, que se siguen leyendo con la flecha arriba.
- Arreglo: en «Añadir lista», al importar, la página baja sola hasta «Abrir lista», que en las pantallas bajas quedaba detrás de la barra de abajo.

### 2.0.25 · 12 de noviembre de 2026
- Las guías de TV se comparten como las listas: en «Editar guías», cada una tiene su botón de compartir, con su código QR, su enlace o su archivo. Y se añaden igual que una lista: con su dirección, un archivo, un código QR o el portapapeles.
- Si lo que añades como lista, o lo que abres o compartes con Whatplay, es una guía de TV (también en .gz o .zip), se añade a la Guía TV en vez de dar error.

### 2.0.24 · 11 de noviembre de 2026
- Webs de vídeo: ya no se queda la pantalla en negro con «La web pide comprobar que eres una persona» cuando no hay nada que pulsar, y los saltos de la publicidad de la página (como en luluvid) ya no impiden encontrar el vídeo.
- Nunca se abre como vídeo del canal una pista de solo sonido, un anuncio ni un vídeo promocional en bucle: se espera a la lista completa de calidades y se abre el vídeo con su sonido. Un vídeo que se queda sin cargar se vuelve a pedir.

### 2.0.23 · 11 de noviembre de 2026
- Las webs de vídeo que hacen una comprobación invisible antes de dar el vídeo, como flyf.lat, ya se abren: Whatplay espera a que termine en vez de darlas por perdidas, y abre la calidad completa, con su sonido.

### 2.0.22 · 11 de noviembre de 2026
- El móvil como mando de la tele: con WebCast o TV Link, el botón «Mando» (en «Tus teles», en el minicontrol y en la tarjeta de Inicio) te deja moverte por Whatplay en la tele sin puntero, buscar escribiendo en el móvil y cambiar el volumen de la tele.
- Guía TV: la lupa de arriba busca por canal, por programa o por tipo (cine, noticias, deportes, series…) en la misma página. Ocupa el sitio del botón de grabar; «Recordatorios y grabaciones» se abre desde el menú y desde cada programa.
- La Guía TV, «Recordatorios y grabaciones», Descargas y Buscar pasan por debajo de la barra de abajo, como las demás páginas: ya no queda un bloque de fondo detrás de ella.
- Navegador: con «Ocultar barras al desplazar», la barra de abajo se esconde al bajar por la web (también en un PDF) y vuelve al subir.
- Favoritos: cada favorito cumple el control parental de su lista o carpeta de Favoritos en todas partes (Inicio, Favoritos, el reproductor, la Guía TV y la tele). El PIN del navegador ya no cuenta: lo que guardaste desde él deja de pedirlo si su lista no está restringida.
- Fire TV: el botón de comprar Premium abre la compra de la Amazon Appstore.
- Arreglos: la app ya no se cierra al abrirla en un móvil lento si WebCast se había cortado, y en Android 7 y 8 el navegador ya no saca el teclado al deslizar la página después de abrir una dirección.

### 2.0.20 · 10 de noviembre de 2026
- En el menú de una lista, «Mostrar en Inicio»: desmarcada, esa lista y sus canales no salen en Inicio (sí en Listas, Buscar y la guía).
- Recordatorios y grabaciones a mano, aunque no haya guía: eliges el canal, el día, la hora y la duración. Lo programado se cambia al tocarlo, y en el reproductor está también «Recordar este canal».
- Guía TV: el selector de listas también en «Ahora», y «Editar guías» con todas tus guías para activarlas, desactivarlas, añadirlas o eliminarlas.
- Los canales web ya no tienen el botón «Abrir en el navegador».

### 2.0.19 · 10 de noviembre de 2026
- Los canales web ya no piden el PIN del navegador: solo la pestaña Navegador. Siguen pidiendo el suyo si el canal o su lista están restringidos.
- En Favoritos, mantener pulsada una lista abre su menú: editarla, subirla o bajarla, restringirla o eliminarla entera. También en la tele.
- Dentro de una lista de favoritos, mantener pulsada una carpeta abre su menú, y en la tele también el de un canal.

### 2.0.18 · 10 de noviembre de 2026
- La pestaña Navegador va aparte: abrir un canal web ya no la cambia. El canal se abre en su propia pantalla y al cerrarlo no queda nada; con el globo, se lleva su página al navegador.
- El icono de web sale solo en los canales que se abren como web.
- Inicio se abre arriba del todo, con «Continuar viendo» a la vista.
- Si tras pasar la comprobación de humano la web no puede cargar su vídeo, se dice y se pasa a la siguiente opción, en vez de quedarse esperando.
- Una web que antes redirigía a una dirección que ya no existe se vuelve a pedir sin lo guardado, y se dice bien cuando la web de su reproductor ya no existe o no responde.

### 2.0.17 · 10 de noviembre de 2026
- Cada canal y carpeta lleva un iconito en la esquina de su logo para saber qué es: directo, web, carpeta o lista externa.
- En la tele, mantener pulsado OK abre el menú de una lista, carpeta o canal al soltarlo, y el menú ya no se cierra solo.
- En el navegador, Atrás ya no deja la página en blanco: va a la página de antes o al inicio del navegador.
- Cuando una web pide comprobar que eres una persona, se ve solo su comprobación, sobre fondo oscuro, y ningún anuncio puede ocupar su lugar.

### 2.0.16 · 10 de noviembre de 2026
- La lista de favoritos se ve como una lista: la misma cabecera, y carpetas y canales juntos, sin separarlos; y tiene su botón de buscar, que encuentra también lo que hay dentro de sus carpetas.
- Buscar tiene un botón para volver atrás.

### 2.0.15 · 8 de noviembre de 2026
- Las listas abiertas, también las de Favoritos, pasan por debajo de la barra de abajo como las pestañas: ya no queda un bloque de fondo que tapa la lista detrás de la barra.

### 2.0.14 · 8 de noviembre de 2026
- El navegador busca con DuckDuckGo de serie, en tu idioma y tu país, y las webs se ven con el tema claro u oscuro de la app; Google, si lo eliges, con el dominio de tu país.
- En el navegador, los enlaces que tocas se abren aunque vayan a otra web (también los resultados de los buscadores); solo se bloquea la publicidad. En las webs del reproductor, igual que antes.
- Sin hueco encima del teclado ni con la tele conectada sin enviar nada, y la barra de direcciones ya no devuelve el cursor al principio al escribir.

### 2.0.13 · 8 de noviembre de 2026
- Mantén pulsada una carpeta para abrir su menú: añadirla a favoritos o, si ya lo está, quitarla. En la tele, manteniendo pulsado OK.
- El reproductor: la carga es un solo círculo en medio del vídeo, que ya no parpadea ni se mueve al tocar la pantalla, y el botón de reproducir y los de alrededor son oscuros con el icono blanco.
- WebCast: la web de la tele se pone a pantalla completa con la primera pulsación del mando, y el vídeo ya no tiene las esquinas redondeadas.
- Al añadir una lista puedes ponerle nombre, también en la tele; se mantiene al actualizarla.
- Las listas Xtream con enlace get.php: si no dicen cuál es su guía, se usa la de su servidor (las que ya tienes la cogen al actualizarlas), y un enlace nuevo se añade como la cuenta Xtream que es, por categorías, así que las listas enormes ya se pueden añadir.

### 2.0.12 · 8 de noviembre de 2026
- Mantén pulsado un canal para añadirlo a favoritos, copiar su dirección o abrirlo con otra app; mantén pulsada una carpeta para guardarla entera en favoritos, y una lista para ver sus opciones. En la tele, manteniendo pulsado OK.
- Los menús de opciones llevan su icono a la izquierda.
- El reproductor enseña la carga dentro del botón de reproducir, como en la tele, y ya no salen dos círculos a la vez.
- Los vídeos de las webs: se puede pasar la comprobación de que eres una persona aunque la tape un anuncio invisible, se ven los directos que la web reproduce ella misma, no se abre un anuncio como si fuera la película, y si no hay vídeo se dice por qué: que lo han borrado, que la dirección no existe o que el servidor de la web da error.
- Si una opción de un canal no funciona, se prueba sola la siguiente antes de dar el error («La opción 1 no funciona: probando la 2…»), también enviando a la tele. El error sale solo cuando han fallado todas.

### 2.0.11 · 8 de noviembre de 2026
- Mejoras internas en los anuncios del móvil.

### 2.0.10 · 8 de noviembre de 2026
- Las listas de los paneles Xtream que se añaden con su enlace get.php ya se ordenan por sus carpetas (por países), con sus logos, también en Android TV, WebCast y TV Link. Las que ya tenías se ordenan solas la próxima vez que se actualicen.

### 2.0.9 · 7 de noviembre de 2026
- Cuando haya una actualización importante, la app te pedirá instalarla al abrirla.

### 2.0.8 · 7 de noviembre de 2026
- Descargas: ya no se ofrece descargar los vídeos de las webs que no lo permiten en sus condiciones de uso (YouTube, las redes sociales y las plataformas de pago); se siguen viendo igual.

### 2.0.7 · 7 de noviembre de 2026
- Los vídeos encontrados en una web (las estaciones web y lo que abres desde el navegador) ya se pueden descargar, en el móvil, en WebCast y en TV Link.

### 2.0.6 · 7 de noviembre de 2026
- Descarga lo que no es en directo (películas, series, vídeos) desde el reproductor para verlo sin conexión: eliges la calidad, sigue aunque cierres el reproductor y se pausa o se cancela desde la notificación. Con Whatplay Premium o con tiempo sin anuncios; en Android TV, con Premium.
- Nueva pantalla Descargas y la fila «Mis descargas» en Inicio; en Android TV, «Descargas» en el menú lateral. En WebCast y TV Link, «Descargar en el móvil» desde la tele.
- En Ajustes › Whatplay Premium puedes canjear un código de Premium o de descuento.
- Chromecast: con la tele conectada y sin nada sonando, o si un canal no se puede reproducir, la tele enseña una pantalla de Whatplay en vez del símbolo de Cast.
- Android TV: «Añadir lista › Archivo» en todas las teles; si la tele no tiene con qué elegir archivos, sale un QR para enviarlo desde el móvil o el ordenador.
- La app sigue funcionando con total normalidad aunque el servidor de Whatplay no responda o conteste mal, y la app TV Link de la tele ya no se queda en una página de error.
- Android TV: Ajustes ya no ofrece «Avisar si uso datos móviles», la última fila se ve entera y el teclado de la pantalla solo lleva la «ñ» en español. En la ficha de un programa, «Ver recordatorios y grabaciones» se ve en todos los idiomas.

### 2.0.2 · 6 de noviembre de 2026
- Whatplay ya está también en italiano y en portugués de Brasil (la app, la de Android TV y WebCast).
- Android TV: todo se maneja con el mando, con el foco siempre a la vista («Importar lista», «Solo reproducir», menús y reproductor), y la tele ya no pide cámara, compartir ni permiso de notificaciones.
- Android TV con el aspecto de WebCast: menú arriba, Inicio con cartel, listas, guía, reproductor, Añadir lista y Ajustes, y Premium también se compra desde la tele.
- En Android TV se usa gratis viendo anuncios de vídeo, igual que en el móvil (un vídeo da tiempo sin anuncios y Premium los quita).
- El navegador de Android TV tiene un puntero que mueves con las flechas del mando: OK pulsa, en los bordes se desplaza la página y con Atrás o arriba del todo vuelves a la barra.
- Envía una lista del móvil a tu Android TV por la misma wifi: abre «Añadir lista» en la tele y en el móvil pulsa «Compartir» › «Enviar a una tele con Whatplay». Va cifrada y se confirma con el mismo código en las dos pantallas.
- La sincronización con Drive ya no se queja de que tus listas «ocupan demasiado»: las listas enormes que tienen dirección viajan por su dirección y cada aparato las descarga.
- Con el motor «Automático» suenan las pistas AC-3 y E-AC-3 que el móvil no decodifica, aunque vayan junto a otra AAC, y dos pistas con el mismo nombre se distinguen.
- «Abrir» en los avisos del navegador ya no cierra la app en los WebView antiguos, y avisa si ninguna app puede abrir la página.
- WebCast vuelve a arrancar solo si Android cierra la app mientras estaba en marcha, y la tele sale de «Reconectando…».
- Los errores al descargar una lista o una guía se explican claros y en tu idioma, y la hora sale en el idioma de la app y con el reloj de 12 o 24 horas del sistema.
- Retoques en la Guía, Favoritos, Premium y en los textos largos en francés y alemán o con letra grande.

### 2.0.1 · 5 de noviembre de 2026
- La Guía vuelve a abrirse en «Ahora»: en la 2.0.0 cerraba la app al abrirla con una guía importada.

### 2.0.0 · 5 de noviembre de 2026
- Al actualizar desde la Whatplay de antes se pasan todas tus listas (las muy grandes, en cuanto hay conexión), con el nombre que les pusiste y sus bloqueos, y los de tus favoritos. Si tenías algo bloqueado con la huella, Whatplay te pide una vez crear un PIN para que siga protegido.
- El nombre que le pones a una lista ya no cambia al actualizarse, y lo que cambias mientras se descarga (el nombre o el control parental) ya no se pierde.
- La sincronización ya no borra listas en tus otros aparatos cuando la copia de Drive es muy grande, y una lista ya no se queda a medias si la app se cierra o el móvil se llena mientras se guarda.
- Más estable: ya no se cierra con la app en otro idioma que el del sistema, con canales repetidos en la Guía, sin sitio en el móvil ni al compartir sin apps; y en Android 7 se abren los ajustes de notificaciones y vuelven a funcionar los anuncios, la tele y las novedades.
- El reproductor no se cierra con canales Smooth Streaming ni con un WebView que falte o se esté actualizando, el temporizador para la radio con la pantalla apagada (y sigue contando aunque cierres el reproductor) y, al volver tras cerrarlo Android, sigue en el canal que sonaba.
- Enviar a la tele ya no cierra la app al emparejar una LG o una Samsung en Android 7 a 12, ni al poner un directo en un Chromecast en Android 13; WebCast vuelve a enseñar imágenes y avisos en la tele con Android 7 a 12, y su PIN sale siempre con cifras normales.
- La Guía ya no cierra la app con listas muy grandes (las de un panel con miles de películas y series): solo tiene en cuenta los canales que están en la guía, y se abre el doble de rápido.
- WebCast, más claro: la hoja explica en tres pasos cómo abrir Whatplay en el navegador de cualquier aparato (tele, ordenador o tablet), WebCast tiene su tarjeta propia en «Tus teles» y las teles LG y Samsung recordadas se pueden olvidar desde allí.
- Sincronización: ahora solo con tu cuenta de Google. Tus listas, favoritos y ajustes se guardan en tu Google Drive, en una carpeta que solo ve Whatplay.
- El soporte de Whatplay es ahora el de Veltrix Studios (contacto@veltrixstudios.net), y la ayuda, la privacidad y los términos se abren en whatplay.es.
- Una LG o Samsung con Chromecast integrado sale dos veces en «Tus teles», una por Cast y otra por TV Link, cada una con su etiqueta (antes podía salir tres veces).
- WebCast y TV Link ya no se mezclan: activar WebCast no conecta sola la app de tu LG o Samsung, y la app solo se conecta cuando eliges esa tele en «Tus teles».
- WebCast es ahora una tele más en «Tus teles»: ves si está esperando (con la dirección para escribir en la tele) o conectado, y lo desconectas como las demás.
- Solo hay una conexión a la vez: al elegir un Chromecast, una tele LG o Samsung, o WebCast, lo de antes se desconecta al momento y lo que estaba sonando sigue en la nueva. En cada camino solo cabe una tele: si se conecta otra, la anterior se desconecta del todo.
- Al desconectar, la tele deja de esperar: el Chromecast vuelve a su pantalla y la app de la LG o Samsung se cierra sola.
- Las LG nuevas salen en «Tus teles» con su nombre y su modelo limpios.
- «Tus teles» vuelve a encontrar las LG y Samsung y a encenderlas aunque tengas una VPN activa en el móvil, y mientras busca se ve el radar.
- En la guía de la tele ya puedes poner avisos y grabaciones como en el móvil: pulsa OK en un programa y elige «Avisarme» o «Grabar» (o quítalos). Si al móvil le falta un permiso, la tele te lo dice y el móvil te enseña dónde darlo.
- La Guía se abre al momento con lo guardado; las guías nuevas se descargan en segundo plano, con su avance, y se van viendo según llegan. Importar una guía grande es unas 4 veces más rápido, y si no ha cambiado ya no se vuelve a descargar.
- Al quitar un canal de favoritos (en el móvil, en la tele, borrando su lista o desde otro aparato sincronizado) desaparece también de «Últimos favoritos» al momento.
- Las actualizaciones se instalan siempre, aunque estés viendo algo o enviándolo a la tele; luego sigues por donde ibas desde «Continuar viendo».
- Al enviar un canal web al Chromecast, si su web pide demostrar que eres una persona, la verificación se abre sola en el móvil si estás en Whatplay; si no, te llega un aviso que la abre al tocarlo.
- Al enviar al Chromecast, «La tele no llega al móvil» ya no sale cuando la wifi solo va lenta, y tras un corte la tele sigue con lo mismo en vez de volver a empezar.
- Cuando el servidor del canal tarda tanto que no da nada, se dice «El servidor del canal no responde».
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google, en tu Google Drive (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba94 · 5 de noviembre de 2026
- La Guía ya no cierra la app con listas muy grandes (las de un panel con miles de películas y series): solo tiene en cuenta los canales que están en la guía, y se abre el doble de rápido.
- WebCast, más claro: la hoja explica en tres pasos cómo abrir Whatplay en el navegador de cualquier aparato (tele, ordenador o tablet), WebCast tiene su tarjeta propia en «Tus teles» y las teles LG y Samsung recordadas se pueden olvidar desde allí.
- Sincronización: ahora solo con tu cuenta de Google. Tus listas, favoritos y ajustes se guardan en tu Google Drive, en una carpeta que solo ve Whatplay.
- El soporte de Whatplay es ahora el de Veltrix Studios (contacto@veltrixstudios.net), y la ayuda, la privacidad y los términos se abren en whatplay.es.
- Una LG o Samsung con Chromecast integrado sale dos veces en «Tus teles», una por Cast y otra por TV Link, cada una con su etiqueta (antes podía salir tres veces).
- WebCast y TV Link ya no se mezclan: activar WebCast no conecta sola la app de tu LG o Samsung, y la app solo se conecta cuando eliges esa tele en «Tus teles».
- WebCast es ahora una tele más en «Tus teles»: ves si está esperando (con la dirección para escribir en la tele) o conectado, y lo desconectas como las demás.
- Solo hay una conexión a la vez: al elegir un Chromecast, una tele LG o Samsung, o WebCast, lo de antes se desconecta al momento y lo que estaba sonando sigue en la nueva. En cada camino solo cabe una tele: si se conecta otra, la anterior se desconecta del todo.
- Al desconectar, la tele deja de esperar: el Chromecast vuelve a su pantalla y la app de la LG o Samsung se cierra sola.
- Las LG nuevas salen en «Tus teles» con su nombre y su modelo limpios.
- «Tus teles» vuelve a encontrar las LG y Samsung y a encenderlas aunque tengas una VPN activa en el móvil, y mientras busca se ve el radar.
- En la guía de la tele ya puedes poner avisos y grabaciones como en el móvil: pulsa OK en un programa y elige «Avisarme» o «Grabar» (o quítalos). Si al móvil le falta un permiso, la tele te lo dice y el móvil te enseña dónde darlo.
- La Guía se abre al momento con lo guardado; las guías nuevas se descargan en segundo plano, con su avance, y se van viendo según llegan. Importar una guía grande es unas 4 veces más rápido, y si no ha cambiado ya no se vuelve a descargar.
- Al quitar un canal de favoritos (en el móvil, en la tele, borrando su lista o desde otro aparato sincronizado) desaparece también de «Últimos favoritos» al momento.
- Las actualizaciones se instalan siempre, aunque estés viendo algo o enviándolo a la tele; luego sigues por donde ibas desde «Continuar viendo».
- Al enviar un canal web al Chromecast, si su web pide demostrar que eres una persona, la verificación se abre sola en el móvil si estás en Whatplay; si no, te llega un aviso que la abre al tocarlo.
- Al enviar al Chromecast, «La tele no llega al móvil» ya no sale cuando la wifi solo va lenta, y tras un corte la tele sigue con lo mismo en vez de volver a empezar.
- Cuando el servidor del canal tarda tanto que no da nada, se dice «El servidor del canal no responde».
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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
- Sincronización: tus listas, favoritos y ajustes en todos tus dispositivos, iniciando sesión con Google, en tu Google Drive (Ajustes › Sincronización).
- En el reproductor, el sombreado de los controles llega hasta arriba del todo, también bajo la barra de estado.
- «Abrir en la web» abre la página a pantalla completa, como un canal embed, sin la barra de la dirección.

### 2.0.0-prueba93 · 5 de noviembre de 2026
- Una LG o Samsung con Chromecast integrado sale dos veces en «Tus teles», una por Cast y otra por TV Link, cada una con su etiqueta (antes podía salir tres veces).
- WebCast y TV Link ya no se mezclan: activar WebCast no conecta sola la app de tu LG o Samsung, y la app solo se conecta cuando eliges esa tele en «Tus teles».
- WebCast es ahora una tele más en «Tus teles»: ves si está esperando (con la dirección para escribir en la tele) o conectado, y lo desconectas como las demás.
- Solo hay una conexión a la vez: al elegir un Chromecast, una tele LG o Samsung, o WebCast, lo de antes se desconecta al momento y lo que estaba sonando sigue en la nueva. En cada camino solo cabe una tele: si se conecta otra, la anterior se desconecta del todo.
- Al desconectar, la tele deja de esperar: el Chromecast vuelve a su pantalla y la app de la LG o Samsung se cierra sola.
- Las LG nuevas salen en «Tus teles» con su nombre y su modelo limpios.
- «Tus teles» vuelve a encontrar las LG y Samsung y a encenderlas aunque tengas una VPN activa en el móvil, y mientras busca se ve el radar.
- En la guía de la tele ya puedes poner avisos y grabaciones como en el móvil: pulsa OK en un programa y elige «Avisarme» o «Grabar» (o quítalos). Si al móvil le falta un permiso, la tele te lo dice y el móvil te enseña dónde darlo.
- La Guía se abre al momento con lo guardado; las guías nuevas se descargan en segundo plano, con su avance, y se van viendo según llegan. Importar una guía grande es unas 4 veces más rápido, y si no ha cambiado ya no se vuelve a descargar.
- Al quitar un canal de favoritos (en el móvil, en la tele, borrando su lista o desde otro aparato sincronizado) desaparece también de «Últimos favoritos» al momento.
- Las actualizaciones se instalan siempre, aunque estés viendo algo o enviándolo a la tele; luego sigues por donde ibas desde «Continuar viendo».
- Al enviar un canal web al Chromecast, si su web pide demostrar que eres una persona, la verificación se abre sola en el móvil si estás en Whatplay; si no, te llega un aviso que la abre al tocarlo.
- Al enviar al Chromecast, «La tele no llega al móvil» ya no sale cuando la wifi solo va lenta, y tras un corte la tele sigue con lo mismo en vez de volver a empezar.
- Cuando el servidor del canal tarda tanto que no da nada, se dice «El servidor del canal no responde».
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba92 · 5 de noviembre de 2026
- WebCast y TV Link ya no se mezclan: activar WebCast no conecta sola la app de tu LG o Samsung, y la app solo se conecta cuando eliges esa tele en «Tus teles».
- WebCast es ahora una tele más en «Tus teles»: ves si está esperando (con la dirección para escribir en la tele) o conectado, y lo desconectas como las demás.
- Solo hay una conexión a la vez: al elegir un Chromecast, una tele LG o Samsung, o WebCast, lo de antes se desconecta al momento y lo que estaba sonando sigue en la nueva. En cada camino solo cabe una tele: si se conecta otra, la anterior se desconecta del todo.
- Al desconectar, la tele deja de esperar: el Chromecast vuelve a su pantalla y la app de la LG o Samsung se cierra sola.
- Una LG o Samsung con Chromecast integrado sale una sola vez en «Tus teles», y puedes elegir el camino con «O por Cast» o «O con la app TV Link»; las LG nuevas salen con su nombre y su modelo limpios.
- «Tus teles» vuelve a encontrar las LG y Samsung y a encenderlas aunque tengas una VPN activa en el móvil, y mientras busca se ve el radar.
- En la guía de la tele ya puedes poner avisos y grabaciones como en el móvil: pulsa OK en un programa y elige «Avisarme» o «Grabar» (o quítalos). Si al móvil le falta un permiso, la tele te lo dice y el móvil te enseña dónde darlo.
- La Guía se abre al momento con lo guardado; las guías nuevas se descargan en segundo plano, con su avance, y se van viendo según llegan. Importar una guía grande es unas 4 veces más rápido, y si no ha cambiado ya no se vuelve a descargar.
- Al quitar un canal de favoritos (en el móvil, en la tele, borrando su lista o desde otro aparato sincronizado) desaparece también de «Últimos favoritos» al momento.
- Las actualizaciones se instalan siempre, aunque estés viendo algo o enviándolo a la tele; luego sigues por donde ibas desde «Continuar viendo».
- Al enviar un canal web al Chromecast, si su web pide demostrar que eres una persona, la verificación se abre sola en el móvil si estás en Whatplay; si no, te llega un aviso que la abre al tocarlo.
- Al enviar al Chromecast, «La tele no llega al móvil» ya no sale cuando la wifi solo va lenta, y tras un corte la tele sigue con lo mismo en vez de volver a empezar.
- Cuando el servidor del canal tarda tanto que no da nada, se dice «El servidor del canal no responde».
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba91 · 5 de noviembre de 2026
- Al enviar al Chromecast, «La tele no llega al móvil» ya no sale cuando la wifi solo va lenta, y tras un corte la tele sigue con lo mismo en vez de volver a empezar.
- Cuando el servidor del canal tarda tanto que no da nada, se dice «El servidor del canal no responde».
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba90 · 5 de noviembre de 2026
- En la tele, el botón Favorito del reproductor ya guarda el canal o el vídeo (antes decía «Algo ha fallado en el móvil»), y el corazón sale lleno en lo que ya es favorito.
- Al desconectar la tele desde el móvil, la tele lo dice al momento y no vuelve a conectarse sola; para volver, pulsa «Conectar otra vez» en la tele o envía algo desde el móvil.
- Lo restringido por el control parental pide ahora el PIN también en la tele, por cualquier camino (al cambiar de canal también), y la pantalla del PIN cabe entera en las teles LG.
- El reproductor de la tele, más pequeño y recogido; sus botones salen siempre igual, y debajo del título solo va lo que echan ahora.
- Cambiar de canal desde el móvil ya no cierra y vuelve a abrir el reproductor de la tele.
- Con la tele conectada, el móvil enseña siempre la misma imagen que la tele: en el minicontrol, en el reproductor (también al cambiar de canal desde la tele), en el mando de Inicio, en la notificación y en la pantalla de bloqueo.
- La tele se llama igual en toda la app, con el nombre que le diste; y si cierras la app de la tele o la apagas, TV Link deja de darla por conectada.
- El icono de las notificaciones se ve más grande y claro en la barra de estado.
- Textos de enviar a la tele corregidos en inglés, francés y alemán.
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba89 · 4 de noviembre de 2026
- Los canales en directo con sonido Dolby (AC-3 / E-AC-3) vuelven a verse y oírse en la tele: en algunos Samsung el audio convertido salía vacío y la tele no llegaba a abrir el canal.
- En la tele, cuando se acaba el tiempo sin anuncios, «Ver un vídeo (+30 min)» abre el vídeo con premio en el móvil (pidiendo desbloquearlo si hace falta) y, al verlo entero, lo que estabas viendo sigue solo.
- En el reproductor de la tele, los mandos se esconden solos también cuando el canal tarda en arrancar, y «Cargando…» y «Preparando…» ya no salen cortados.
- Con una VPN activa en el móvil, la hoja de WebCast avisa de que, si el código no encuentra la tele, puedes usar la dirección y el PIN.
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba88 · 4 de noviembre de 2026
- En el reproductor de la tele, con los mandos a la vista, las flechas y OK mueven por los botones y los pulsan (ya se llega a «De la lista» y Favorito); con ellos ocultos, izquierda y derecha retroceden y avanzan enseñando solo la barra, y OK pausa. Atrás oculta los mandos y, si ya están ocultos, sale.
- Cambiar de canal en la tele (desde «De la lista», anterior y siguiente, P+ y P− o «A continuación») ya no cierra el reproductor: pone el canal nuevo al momento, y anterior y siguiente salen siempre.
- En la tele, el título y «A continuación» van más abajo, junto a la barra, y la carga y los errores arriba, sin tapar nada; el título es algo más pequeño y sin la línea de encima.
- En la tele, los canales que son páginas web ya no salen como «Película» si no se sabe que lo son.

### 2.0.0-prueba87 · 4 de noviembre de 2026
- Con una tele conectada (WebCast, TV Link o Chromecast) ya nunca se abre el reproductor del móvil: el vídeo de una estación web se busca sin pantalla y suena en la tele, también al elegirla desde la tele. Con un Chromecast, si la web pide demostrar que eres una persona, una notificación te pide abrirla en el móvil.
- En la app de la tele: Atrás en Inicio la cierra, y al volver a abrirla, si el móvil ha cambiado de wifi, busca su dirección nueva en vez de quedarse colgada. El móvil avisa enseguida de su IP nueva.
- En el reproductor de la tele, arriba y abajo solo mueven por los botones: el canal se cambia con P+ y P−, «A continuación», el panel de canales o los botones anterior y siguiente. La carga y el título ya no se pisan, y las letras tienen tamaños coherentes.
- «Tus teles» ya no enseña la misma tele dos veces.
- En la tienda, «Ver un vídeo» es una tarjeta que se toca entera y se lee bien también mientras se prepara.
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba86 · 4 de noviembre de 2026
- Con una tele conectada (Chromecast, WebCast o TV Link), lo que tocas va directo a ella sin abrir el reproductor; el minicontrol trae anterior y siguiente y al tocarlo abre el reproductor, donde la imagen ocupa toda la pantalla y el botón de enviar se ve conectado.
- Enviar a la tele con el móvil bloqueado: con Whatplay abierto, WebCast y TV Link siguen con la pantalla apagada, y el vídeo de una estación web se busca en el móvil sin pedirte que lo abras. Si su web pide demostrar que eres una persona (un reCAPTCHA, Cloudflare…), la pasas tú en la tele con el mando, viendo la página del móvil casi en directo. Ajustes › Tele explica cómo poner Whatplay en «Sin restricciones».
- Si el móvil y la tele están en redes distintas, los dos lo dicen (con las dos redes) en vez de quedarse conectando.
- En la tele: las flechas recorren las filas de Inicio, el título del reproductor es más pequeño, las imágenes llenan la tarjeta, las listas llevan su imagen, el indicador de carga es nuevo y EN VIVO solo sale en los directos.
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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

### 2.0.0-prueba85 · 4 de noviembre de 2026
- Enviar a la tele: el botón de la cabecera y el del reproductor abren «Tus teles», con tus Chromecast, las teles LG y Samsung con la app Whatplay TV Link y WebCast, que lleva Whatplay al navegador de cualquier tele u ordenador. Para vincular la tele, escribe en el móvil el código que ves en ella (sin internet, la dirección y el PIN); lo que ves va siempre por la wifi de casa. Sin Premium, WebCast y las teles LG funcionan mientras te quede tiempo sin anuncios.
- Si un bloqueador (un DNS privado, una app o VPN, el filtro del router) no deja llegar los anuncios, Whatplay te explica cómo quitarlo o te ofrece Premium; y donde hay que dar el consentimiento de los anuncios, si se activa, te pide aceptarlos o hacerte Premium. Si estabas enviando a la tele, sigue sonando y puedes dejar de enviar desde esa misma ventana.
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
- Ajustes está ahora en el menú lateral, y la cabecera queda más despejada; en el Navegador no hay cabecera: solo su barra, con más sitio para la web. Whatplay sale en el idioma de tu móvil (en inglés si no es español, inglés, francés ni alemán; en español con el catalán, el gallego o el euskera), y lo puedes cambiar en Ajustes › Idioma, que ahora está en la página principal.
- Listas enseña solo las listas que añades tú (por su dirección, de un archivo, de otra app o con una cuenta de proveedor); tus listas de favoritos están solo en Favoritos, y «Eliminar todas las listas» ya no las borra. Fuera la pastilla «Locales». En Buscar, dos pastillas nuevas: «Favoritos», si tienes alguno, y «Media», si hay vídeos en el móvil y Whatplay puede verlos. Y en la pastilla «Media» de Buscar puedes buscar también por formato: «.avi», «mkv» o «vacaciones .mp4» (la pestaña Media ya no lleva su propio buscador: está la lupa de arriba).
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
