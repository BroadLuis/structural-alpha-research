# Structural Alpha Research — manual de publicación de artículos y estudios

Este documento es la referencia obligatoria para preparar, revisar, publicar y mantener artículos en Structural Alpha Research. Consolida las reglas existentes de rankings y analítica con las normas editoriales y el procedimiento de publicación descritos en el README del repositorio. Las comprobaciones editoriales adicionales son normas de trabajo; no debe suponerse que el validador automático ya las verifica.

## 1. Principios editoriales

1. Publicar investigación original, independiente y basada en datos verificables. No presentar hipótesis, interpretaciones o escenarios como hechos confirmados.
2. Usar títulos precisos y descriptivos, coherentes con las cifras y las conclusiones del artículo. Evitar afirmaciones categóricas que los datos no sustenten.
3. Escribir los artículos públicos en inglés claro y natural, con tono analítico, sobrio y comprensible. Mantener consistencia terminológica y evitar exageraciones.
4. Distinguir explícitamente entre **observaciones medidas**, **interpretación** y **escenarios o riesgos**. No confundir fortaleza relativa con recuperación confirmada ni mejora semanal con cambio de tendencia estructural.
5. Indicar fecha de corte de los datos, fecha de publicación, universo examinado, tamaño de muestra, metodología y limitaciones relevantes.
6. Comprobar todas las cifras, unidades, fechas, denominadores, porcentajes y afirmaciones comparativas contra los archivos fuente. No inventar datos faltantes ni extrapolar conclusiones sin advertirlo.
7. Respetar la confidencialidad: nunca publicar bases privadas, scripts internos, claves, información de cuentas, señales propietarias de trading ni datos personales.

## 2. Estructura recomendada del artículo

Adaptar las secciones a la naturaleza del estudio; no introducir apartados vacíos ni indicadores que no existan en los datos.

1. **Cabecera:** título, mercado o universo, fecha de publicación y fecha de observación.
2. **Entradilla o resumen:** tesis central sustentada en los datos, sin adelantar conclusiones no probadas.
3. **Indicadores principales:** tamaño del universo y métricas pertinentes (por ejemplo, amplitud sobre MA200, rentabilidades, drawdowns y volumen relativo).
4. **Desarrollo analítico:** qué ha cambiado, dónde se concentra la fortaleza o debilidad y qué divergencias muestran los indicadores.
5. **Gráficos:** visualizaciones relevantes, explicadas y vinculadas a afirmaciones concretas del texto.
6. **Ranking completo de compañías**, cuando el estudio sea por valores, conforme a la sección 4.
7. **Interpretación, escenarios y limitaciones:** diferenciar señales preliminares de confirmaciones.
8. **Datos del ranking y metodología:** tabla interactiva basada en JSON, copia completa del ranking y otros materiales públicos cuando proceda, con enlaces comprobados.

No es obligatorio que todos los estudios incluyan los mismos indicadores; sí es obligatorio que la narrativa refleje fielmente los datos disponibles.

## 3. Gráficos, imágenes y tablas analíticas

1. Comprobar que títulos, ejes, fechas, leyendas, unidades, escalas y series coinciden con los datos originales.
2. Mantener los gráficos legibles en ordenador y móvil, sin cortes, solapamientos ni texto ilegible.
3. Evitar escalas engañosas y explicar las comparaciones entre universos o períodos no equivalentes.
4. Utilizar solamente imágenes, gráficos y datos cuya publicación esté autorizada; no incluir información privada ni marcas o firmas ajenas al estilo aprobado.
5. No modificar gráficos o rankings que ya funcionen al introducir cambios en otra parte del artículo.

## 4. Rankings completos — reglas obligatorias

El estudio ASX del 16/10/2026 (`studies/2026-10-16-asx/index.html`) es la referencia del nuevo formato JSON de rankings; los estudios anteriores conservan su formato histórico.

1. Publicar **todos** los valores del universo, nunca solo una selección de mejores o peores.
2. Mostrar, cuando estén disponibles, **Weekly Rank, Global Rank, Ticker, Company, Last Close, 1W, 4W, 3M y YTD**.
3. Rentabilidades positivas: fondo verde; negativas: rojo/rosa; cero: neutro. Usar porcentajes con signo de manera consistente.
4. **Ordenador:** tabla completa, legible, con búsqueda visible encima de la tabla y ordenación funcional. **Cada encabezado de las nueve columnas debe ser pulsable**, mostrar flechas y alternar entre orden ascendente y descendente; los valores numéricos se ordenan numéricamente y los textos alfabéticamente.
5. **Móvil:** fichas verticales etiquetadas, con los mismos datos y sin desplazamiento horizontal; buscador propio y ordenación funcional.
6. **Ambos buscadores** deben filtrar por ticker o nombre de empresa mientras se escribe, recuperar todos los valores al borrar el texto y seguir funcionando después de ordenar o cargar datos dinámicamente. El buscador móvil **no sustituye** al de escritorio.
7. Mostrar recuento total de empresas y un botón funcional **Copy complete ranking** que copie las nueve columnas y todas las filas, con encabezados, separadas por tabuladores y filas por saltos de línea, aptas para pegar en Excel. No es obligatorio ofrecer Excel público en estudios nuevos.
8. En los nuevos estudios, publicar el JSON generado por Weekly Analysis y mantenerlo sincronizado con el Excel privado de trabajo, el HTML y el tamaño real del universo. Verificar **todas las filas**, las nueve columnas, el orden, los nulos y las rentabilidades.
9. Mantener los estilos compartidos cuando corresponda, especialmente `assets/structural-alpha-ranking.css`. No sustituir una tabla que funciona por otra implementación sin verificarla.
10. Al ordenar desde los encabezados, actualizar la indicación visual de dirección y el atributo accesible `aria-sort`, manteniendo búsqueda y tarjetas móviles sincronizadas.
11. Cargar el JSON directamente con `fetch` y comprobar `schema_version`, `universe`, `columns` y `rows`; no depender de XLSX.js para las nuevas tablas. Conservar buscadores y ordenación independientes en escritorio y móvil.

## 5. Organización de archivos y catálogo

1. Cada estudio debe tener su carpeta propia, por ejemplo `studies/AAAA-MM-DD-mercado/`, con su `index.html` y los recursos públicos necesarios.
2. La portada pública es `index.html` (raíz). El catálogo maestro es `reports.json`.
3. Registrar cada estudio en `reports.json` con **title, date, universe, summary y url**; incluir **download** cuando exista un archivo descargable.
4. El campo `universe` debe coincidir **exactamente** con una opción del filtro de la portada (por ejemplo, `ENERGY`).
5. El resumen del catálogo debe ser breve y basado en datos: objetivo editorial de **30–65 palabras**; el validador actual rechaza más de **85 palabras**.
6. Sincronizar el bloque `// BEGIN GENERATED REPORT SNAPSHOT` / `// END GENERATED REPORT SNAPSHOT` de `index.html` con `reports.json`, conservando contenido y orden.
7. Verificar rutas relativas, acceso público sin autenticación, lectura JSON, botón de copia y descargas únicamente cuando existan.
8. Usar GitHub Releases para archivos ZIP de gran tamaño cuando corresponda; no subir archivos innecesarios o privados al repositorio.

## 6. Metadatos y presentación web

1. Mantener la identidad visual del sitio y la navegación coherente con el resto de estudios.
2. Cada página debe tener título HTML, descripción y metadatos para compartir en redes (Open Graph y Twitter/X) acordes con el artículo. Revisar sus enlaces e imagen de vista previa.
3. **Obligatorio en todas las páginas publicadas:** tema claro y oscuro funcionales, con cambio y persistencia coherentes entre páginas; verificar escritorio y móvil. No basta con que el CSS contenga reglas de tema oscuro: el documento debe activarlas realmente y el contenido debe resultar legible.
4. Comprobar que no hay texto provisional, mensajes de «archivo pendiente», enlaces rotos ni controles sin función una vez publicada la página.
5. Mantener la accesibilidad básica: jerarquía de encabezados, texto alternativo para imágenes informativas, etiquetas de buscadores y controles utilizables.

## 7. Cloudflare Web Analytics y privacidad

**Obligatorio en cada nueva página HTML** (portada, estudios y páginas auxiliares): insertar **exactamente una vez dentro de `<head>`** este código:

```html
<!-- Cloudflare Web Analytics -->
<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token":"7337e081de4249b9bc3b0afc3b1d2e88"}'></script>
<!-- End Cloudflare Web Analytics -->
```

- **Prohibidos los contadores públicos de visitas**, incluidos hits.sh, en todas las páginas y artículos.
- No introducir mecanismos nuevos de seguimiento de clics o descargas sin aprobación expresa.
- Confirmar que el beacon aparece exactamente una vez por página.

## 8. Validación obligatoria antes de publicar

**Revisión editorial y de datos:**
- [ ] Título, tesis, fechas, tamaño del universo y cifras cotejados con los originales.
- [ ] Observaciones, interpretación y escenarios claramente diferenciados; limitaciones incluidas.
- [ ] Gráficos legibles, con leyendas y unidades correctas.
- [ ] JSON público contrastado con el Excel local; sin datos privados, claves, señales propietarias o información personal.

**Revisión del ranking (si existe):**
- [ ] Número de filas igual al universo completo; columnas y rentabilidades correctas.
- [ ] Colores positivos/negativos/neutros y signos verificados.
- [ ] Buscador y ordenación probados **por separado** en escritorio y móvil; flechas de **todas** las columnas probadas en ambos sentidos.
- [ ] Fichas móviles legibles, sin scroll horizontal, y botón «Copy complete ranking» probado.
- [ ] Carga dinámica, borrado del filtro y reordenación probados.

**Revisión técnica:**
- [ ] Entrada de `reports.json` completa, filtro `universe` correcto y snapshot de portada idéntico.
- [ ] Ejecutado `python scripts/validate_research.py` **sin errores**.
- [ ] Todos los enlaces, imágenes, archivos JSON, botones de copia, descargas existentes y metadatos revisados.
- [ ] Beacon de Cloudflare exactamente una vez; ningún contador público.
- [ ] Modo claro y oscuro comprobados en cabecera, cuerpo, tarjetas KPI, tablas completas, celdas positivas/negativas, filtros, fichas móviles y navegación; preferencia persistente al abrir otro estudio.
- [ ] Verificado el despliegue de GitHub Pages y la página real desde navegador de escritorio y móvil.

**Importante:** `scripts/validate_research.py` valida actualmente catálogo, filtros, enlaces locales y snapshot de portada. **No certifica** por sí solo buscadores, renderizado, recuentos de filas cargadas, gráficos, analítica o funcionamiento móvil; esas pruebas requieren revisión adicional.

## 9. Publicación y verificación final

1. Revisar los datos y redactar el artículo según las secciones anteriores.
2. Preparar y comprobar Excel, gráficos, HTML y rankings.
3. Añadir el estudio a `reports.json` y sincronizar el snapshot de `index.html`.
4. Ejecutar el validador y corregir los errores antes del commit.
5. Publicar en la rama `main` conforme al flujo de GitHub Pages del repositorio.
6. Confirmar el resultado de la validación y del despliegue; abrir la URL pública y probar buscadores, tabla, fichas, enlaces y descargas.
7. **No anunciar la publicación como completada hasta verificar el funcionamiento real**. Si una comprobación no se ha podido realizar, indicarlo expresamente.

### Programación de publicaciones — comprobación obligatoria

Cuando un artículo tenga una fecha y hora futuras de publicación:

1. Incorporar el estudio y su enlace de descarga (si existe) a `reports.json` y sincronizar el snapshot de `index.html`.
2. Añadir la fecha y hora exactas, **convertidas correctamente a UTC desde la hora de Nueva York (ET)** para ese día, al objeto `publicationTimes` de `index.html`. Tener en cuenta los cambios de horario de verano de Nueva York y Madrid.
3. **Comprobar también `PUBLICATION_SCHEDULE.md`**: el artículo debe figurar en **Upcoming releases**, con fecha, hora de Madrid, hora de Nueva York, universo y título correctos. No basta con actualizar `index.html` y `reports.json`.
4. El calendario se genera desde `publicationTimes` y `reports.json` mediante `scripts/update_publication_schedule.py`; ejecutar el script o lanzar manualmente el workflow `.github/workflows/update-publication-schedule.yml` (GitHub Actions → Run workflow) cuando deba reflejarse inmediatamente. El workflow también se ejecuta periódicamente, pero puede retrasarse.
5. Confirmar en GitHub que `PUBLICATION_SCHEDULE.md` refleja efectivamente la nueva publicación y que el artículo pasa a **Earlier scheduled releases** tras la hora programada. Verificar igualmente el comportamiento de la portada pública.
6. **No afirmar que la publicación está programada y verificada** si no se ha comprobado la entrada en el calendario y su horario; explicar claramente cualquier comprobación pendiente. La ocultación en la portada no impide necesariamente acceder al artículo mediante su URL directa.


## 10. Mantenimiento y control de cambios

- Usar este documento como checklist en todos los estudios futuros.
- Mantener el formato ASX como referencia visual, sin copiar errores ni sobrescribir funcionalidades que ya funcionen.
- Si se detecta una nueva necesidad general, actualizar primero estas normas y aplicar la mejora a los artículos afectados cuando proceda.
- No afirmar que un requisito está automatizado si solo se revisa manualmente.
- Conservar las instrucciones editoriales del `README.md` como documentación complementaria; ante una diferencia, revisar y armonizar ambos documentos antes de publicar.


## Transparencia metodológica y protección de métodos propios

- Mantener una página pública `methodology.html` que explique la finalidad, interpretación y limitaciones de amplitud, drawdown, volumen relativo y rankings.
- Cada artículo debe enlazar a la guía pública, sin sustituir las notas específicas necesarias para interpretar sus cifras, denominadores, horizontes temporales y fuentes.
- No publicar fórmulas propietarias, ponderaciones, parámetros internos, filtros de clasificación, algoritmos de ranking ni reglas de trading.
- Los indicadores convencionales pueden describirse con el detalle necesario para evitar interpretaciones engañosas; la transparencia no debe sacrificarse para ocultar el significado de los datos publicados.
- Revisar los Excel y otros archivos descargables antes de publicarlos: no deben contener por descuido hojas internas, fórmulas protegidas, reglas o modelos propietarios. No retirar información ya publicada sin revisión expresa.
- Distinguir entre observaciones cuantitativas, interpretación y escenarios. No presentar un ranking como recomendación personalizada ni afirmar que la metodología es imposible de reconstruir.


## 11. SEO, descubrimiento e indexación — obligatorio en nuevas publicaciones

**Objetivo:** facilitar que inversores interesados en mineras y análisis cuantitativo encuentren estudios originales desde buscadores, sin sacrificar precisión editorial ni convertir el artículo en publicidad. El SEO no garantiza indexación, posicionamiento ni tráfico.

### 11.1 Intención de búsqueda, título y descripción

1. Definir antes de redactar una **consulta principal** plausible en inglés y 2–4 consultas secundarias relacionadas con el universo y los datos reales. Ejemplos orientativos: `ASX mining stocks analysis`, `gold miners market breadth`, `junior copper miners relative strength`. No afirmar volúmenes de búsqueda sin datos.
2. Escribir un `<title>` HTML **único, descriptivo y específico**, que combine el mercado, el hallazgo principal y, cuando aporte valor, el período. Priorizar claridad sobre una longitud rígida; evitar repetir mecánicamente el nombre del sitio o usar titulares sensacionalistas.
3. Escribir una `<meta name="description">` **única**, natural y verificable, que resuma la aportación del estudio (universo, evidencia, ranking, fecha o descarga). Orientación editorial de 140–160 caracteres, sin truncar ideas para cumplir una cifra exacta; Google puede mostrar otro fragmento.
4. Mantener **un único H1** representativo del contenido y usar H2/H3 en orden lógico para el análisis, el ranking y la metodología. No utilizar encabezados exclusivamente decorativos.
5. Introducir en el primer párrafo el universo analizado, fecha de corte, alcance y conclusión principal. Usar términos buscables solo cuando resulten naturales; prohibido el relleno de palabras clave y los títulos que prometan recomendaciones que el estudio no ofrece.
6. Conservar los datos y matices del análisis: no sustituir la tesis real por expresiones como «best stocks to buy» si no se han identificado oportunidades de compra.

### 11.2 Metadatos técnicos y páginas accesibles

1. Cada estudio público debe tener `<html lang="en">`, `<meta name="viewport">`, título, descripción y **canonical absoluta autorreferente** en `<head>`, usando `https://structuralalpharesearch.net/` y la URL pública real.
2. Mantener coherencia entre `canonical`, `og:url`, `og:title`, `og:description`, etiquetas Twitter/X y contenido visible. Las imágenes de vista previa deben existir, ser accesibles y tener proporciones adecuadas.
3. No insertar `noindex` ni bloquear el rastreo de artículos públicos. Las páginas futuras, borradores y publicaciones todavía no liberadas **no deben figurar en el sitemap** ni enlazarse como disponibles; si es imprescindible mantenerlas accesibles antes de tiempo, revisar expresamente su exposición y la política de indexación.
4. Mantener HTML legible para buscadores: el cuerpo del análisis, el título y los enlaces principales deben existir en el HTML inicial; no depender exclusivamente de JavaScript para que Google descubra el texto o los enlaces.
5. Comprobar ausencia de enlaces rotos, errores 404, redirecciones innecesarias y duplicados entre rutas con/sin `index.html`. La URL canónica debe ser consistente en el sitio.
6. Si se incorporan datos estructurados (`Article`, `BreadcrumbList`), deben representar contenido visible, fechas y autoría verdaderas; nunca inventar valoraciones, reseñas ni resultados.

### 11.3 Enlaces internos y páginas permanentes por universo

1. Desde cada estudio enlazar, cuando existan, a la página permanente del universo, al estudio anterior comparable y a `/methodology.html`. Incluir enlaces contextuales a otros mercados solo cuando aporten valor analítico.
2. Utilizar textos de enlace descriptivos (p. ej. «ASX miners weekly analysis»), no repetir únicamente «click here».
3. **Propuesta de implantación gradual, pendiente de aprobación y desarrollo:** páginas estables como `/asx/` y `/gdx-gdxj/`, con introducción original al universo, último estudio publicado, histórico de estudios, metodología y enlaces a rankings. No crearlas como páginas vacías o duplicados del artículo semanal.
4. Cada página permanente tendría canonical propia y navegación visible desde la portada y desde los artículos correspondientes. Los estudios fechados conservarían sus URLs, contenido y canonical individuales.
5. No añadir nuevas páginas al sitemap ni a la navegación hasta que existan, estén publicadas y se haya probado su utilidad en escritorio y móvil.

### 11.4 Sitemap, automatización y Search Console

1. Registrar todo nuevo estudio en `reports.json` con su URL real y fecha de publicación, según la sección 5.
2. Mantener `/sitemap.xml` y `/robots.txt` accesibles. El sitemap debe incluir solo páginas públicas, canónicas, con respuesta correcta y ya publicadas.
3. La generación prevista usa `scripts/generate_sitemap.py` y `.github/workflows/update-sitemap.yml`. **Verificar la ejecución efectiva de GitHub Actions y el contenido del XML** tras cada publicación; no dar por hecho que la automatización funcionó por existir el workflow.
4. Revisar que la nueva URL figure en `https://structuralalpharesearch.net/sitemap.xml` después del despliegue. Las publicaciones programadas no deben aparecer anticipadamente.
5. Search Console es la fuente para evaluar descubrimiento, cobertura, impresiones, consultas, clics y posición media. El envío del sitemap y la solicitud de indexación **no garantizan** indexación ni clasificación.
6. Revisar periódicamente errores de rastreo e indexación. No solicitar indexación manual repetidamente de cada estudio si el sistema de descubrimiento funciona.

### 11.5 Distribución y evaluación

1. Redactar el post de X con una conclusión relevante y una razón concreta para visitar el estudio completo (gráficos, ranking íntegro, datos o metodología), sin ocultar información de forma engañosa.
2. No modificar la tesis, cifras, niveles ni conclusiones para mejorar el CTR. Mantener Structural Alpha Research gratuito y sin mecanismos de monetización añadidos.
3. Evaluar mensualmente por separado: impresiones y clics orgánicos de Search Console; visitantes y páginas vistas de Cloudflare; y alcance y clics de X. No confundir impresiones, visitantes únicos y visitas.
4. Evaluar páginas permanentes solo después de disponer de un período razonable de observación. No atribuir automáticamente aumentos o caídas de tráfico a un cambio SEO aislado.

### 11.6 Checklist SEO antes y después de publicar

- [ ] Consulta principal e intención del lector definidas; título y descripción únicos y fieles a los datos.
- [ ] Un H1 claro, encabezados jerárquicos, entradilla informativa y contenido principal legible sin JavaScript.
- [ ] Canonical absoluta correcta; metadatos Open Graph y X coherentes; enlaces e imágenes operativos.
- [ ] Enlaces internos a metodología, estudio anterior y página de universo si ya existe.
- [ ] Estudio publicado y accesible; no incluido anticipadamente en el sitemap.
- [ ] `reports.json`, portada, URL pública y sitemap sincronizados; workflow comprobado.
- [ ] Tras el despliegue, verificar la URL real y, posteriormente, su estado en Search Console.


## 12. Formato JSON obligatorio para nuevos rankings (desde 16/10/2026)

1. **Producción local:** Weekly Analysis genera el Excel completo para el autor y un JSON de publicación. El Excel local no se elimina ni es necesario subirlo a GitHub.
2. **Ruta recomendada:** guardar el archivo público como `studies/AAAA-MM-DD-mercado/assets/ranking.json`, con una ruta relativa comprobada desde el HTML del artículo. El ejemplo validado es `studies/2026-10-16-asx/assets/ranking.json`.
3. **Esquema v1:** objeto con `schema_version: 1`, `universe`, `start_date`, `as_of_date`, `columns` y `rows`. Orden exacto de columnas: `rank_weekly`, `rank_global`, `ticker`, `name`, `last_close`, `return_week_pct`, `return_4w_pct`, `return_3m_pct`, `return_ytd_pct`. Las filas son arrays de nueve elementos, y los campos sin dato se representan mediante `null`.
4. **Formato numérico:** las rentabilidades del JSON son porcentajes numéricos (por ejemplo, `9.5` significa `+9.50%`), no fracciones ni cadenas formateadas. Los decimales se redondean únicamente al presentarlos en pantalla. No cambiar ni recalcular rankings al exportar.
5. **Interfaz:** conservar buscadores, ordenación, colores y tarjetas móviles; el botón `Copy complete ranking` debe copiar todas las filas, incluso si hay un filtro activo, con encabezados y tabuladores para pegar en hojas de cálculo. Deshabilitar la copia o informar claramente cuando el JSON aún no se haya cargado.
6. **Publicación:** para nuevos estudios, subir el JSON y no el Excel. No incluir un botón de descarga Excel ni un campo `download` en `reports.json` cuando no exista descarga pública. Evitar frases que prometan un Excel en el título, resumen o metadatos.
7. **Histórico:** no borrar Excel ni romper enlaces de estudios antiguos. La migración de un artículo existente debe validarse antes de cambiarlo, manteniendo su URL, canonical y contenido editorial.
8. **Verificación:** comprobar la ordenación ascendente y descendente de cada encabezado, además del recuento exacto del universo, los nueve campos, valores nulos, búsquedas de escritorio/móvil, ordenaciones, signos/colores, copia y navegación. Probar el HTML desplegado, no solo el JSON local.
9. **SEO:** mantener el texto analítico y enlaces en HTML inicial; la tabla JSON dinámica no debe ser el único contenido útil para los buscadores.

## 13. Legibilidad de rankings en móviles (18/10/2026)

- Aplicar el CSS compartido `assets/structural-alpha-ranking.css` en las páginas con rankings.
- En las fichas móviles, reservar una columna estable para las etiquetas y otra para los valores. Referencia: `grid-template-columns:minmax(100px,36%) minmax(0,1fr)`.
- No dividir palabras de etiquetas como Weekly rank, Global rank, Ticker, Company o Last close. Evitar `overflow-wrap:anywhere` en las etiquetas.
- Permitir que los nombres largos de empresas se ajusten entre palabras, sin desplazar las etiquetas ni provocar scroll horizontal.
- Mantener los números y porcentajes alineados a la derecha y los colores de rentabilidades.
- Verificar una ficha con nombre largo, por ejemplo Brown Forman Ord Shs Class B, en pantallas de 320 a 390 px y en temas claro y oscuro.
- Probar después del despliegue un ranking histórico con Excel y otro nuevo con JSON, sin alterar la experiencia de escritorio. No considerar validado el cambio hasta comprobar la web publicada.


## 14. Identidad visual y modo claro/oscuro — obligatorio (21/10/2026)

1. **Identidad gráfica unificada:** todos los artículos y estudios, incluidos los históricos, deben mantener la paleta grafito y dorado de Structural Alpha Research, cabeceras proporcionadas, tipografía legible y una jerarquía visual sobria. Evitar encabezados gigantes o bloques que ocupen una pantalla sin aportar información. No alterar cifras ni gráficos al corregir estilos.
2. **Ambos temas son obligatorios:** el modo claro y el modo oscuro deben funcionar en todo el documento, no solo en el encabezado. La cabecera, el fondo exterior, el contenedor principal, los paneles de análisis, las tarjetas KPI, notas, enlaces, gráficos, tablas y rankings deben conservar contraste suficiente.
3. **Inicialización real del tema:** establecer `data-theme="light"` o `data-theme="dark"` en `document.documentElement` antes de renderizar el contenido. Respetar primero `localStorage.getItem("structural-alpha-theme")` si contiene `light` o `dark`; en su defecto, usar `prefers-color-scheme`. `document.documentElement.dataset.theme` es equivalente. **No considerar que una página soporta modo oscuro por el simple hecho de contener selectores CSS `[data-theme="dark"]`.** Comprobar que el valor se asigna y que los selectores se aplican efectivamente.
4. **Estilos compartidos:** las páginas con ranking deben cargar `assets/structural-alpha-ranking.css` y las páginas de investigación deben cargar `assets/structural-alpha-dark-legibility.css` con la ruta relativa correcta. La hoja compartida es un refuerzo, **no sustituye** la adaptación de clases específicas del artículo. Revisar la cascada CSS, la especificidad, el orden de carga, los estilos `inline` y las reglas con `!important`; evitar parches indiscriminados que perjudiquen otras páginas.
5. **Referencias cromáticas para temas:** en oscuro, fondo exterior aproximado `#171b1e`, paneles `#242a2e`, texto principal `#f0eae0`, cabeceras de tabla `#37424b`. En claro, fondo general `#f5f3ef`, paneles blancos y texto `#20272d`. Mantener acentos dorados discretos. Los valores son referencias: el criterio decisivo es la legibilidad de todos los elementos.
6. **Rankings en ambos temas:** las filas alternas y celdas no coloreadas deben tener contraste entre texto y fondo. Positivos: verde con texto legible; negativos: rojo/rosa con texto legible; neutros o nulos, claramente visibles. Conservar búsqueda, ordenación, encabezados clicables, copia íntegra y diseño de fichas móviles. No confiar en que la tabla se vea bien solo por comprobar la cabecera.
7. **Gráficos y componentes especiales:** revisar fondos propios, títulos, ejes, leyendas y textos que utilicen colores codificados, así como `<canvas>`, SVG y estilos `inline` cuando existan. Los gráficos con fondo claro intencionado deben mantener texto oscuro y contraste suficiente dentro de su propia superficie; nunca imponer texto claro sobre fondo blanco.
8. **Prueba funcional y visual antes de publicar:** abrir el HTML **desplegado**, establecer explícitamente modo claro y modo oscuro, recargar, cambiar de artículo y confirmar que se conserva la elección. Revisar comienzo, mitad y final de la página; en un ranking, comprobar filas pares/impares, las nueve columnas, colores y buscadores. Repetir en escritorio y móvil (incluyendo 320–390 px). Hacer capturas o una inspección visual equivalente: una revisión estática del CSS no acredita que la página se vea correctamente.
9. **Control de cambios y caché:** cuando cambie una hoja CSS compartida, revisar todas las páginas dependientes y actualizar su referencia de versión si es necesario para evitar una copia antigua en caché. No afirmar «corregido visualmente» hasta probar el resultado público; distinguir confirmación del commit en GitHub, despliegue y verificación de interfaz.
10. **Enlaces de continuidad editorial:** al final de cada artículo publicado, incluir cuando proceda un bloque discreto «Continue exploring» con 2–3 estudios relacionados ya disponibles y enlace al archivo o página permanente del universo. No recomendar estudios bajo embargo ni romper el calendario de publicación. Usar títulos descriptivos, enlaces reales y diseño adaptable; no introducir seguimiento adicional sin autorización.

**Incidencia histórica de referencia:** en octubre de 2026, algunas publicaciones antiguas incluían estilos `[data-theme="dark"]` pero no activaban el atributo del tema; en otras, las filas alternas del ranking mostraban fondo claro con texto claro. Es obligatorio comprobar tanto la **activación** como el **contraste efectivo** para evitar reproducir esos fallos.

## 15. Market Perspectives: catálogo visible, contenedores y pruebas integrales (22/10/2026)

1. **Dos registros distintos de publicación:** incluir los nuevos artículos editoriales en `reports.json` (y sincronizar el bloque `BEGIN/END GENERATED REPORT SNAPSHOT` de `index.html`) **y también en la lista HTML `#market-perspectives .perspectives-list` de la portada**. La inclusión en el catálogo general no implica que aparezcan en la sección visual Market Perspectives.
2. **Tres artículos visibles y calendario:** la portada selecciona los tres artículos editoriales más recientes cuya fecha `data-release` (UTC) ya haya transcurrido. Añadir a cada `.perspective-row` el enlace, título, resumen y `data-release` correctos. Verificar orden, ocultación de publicaciones futuras, sustitución automática de la tercera entrada y enlace real. No saltarse la programación editorial ni adelantar artículos pendientes.
3. **Prohibido el marco blanco en modo oscuro:** los artículos históricos pueden contener CSS fijo como `main{background:white}` o `main{background:#fff}`, aunque el texto ya sea claro. Revisar expresamente `body`, `main`, `article`, `section` y los contenedores exteriores; en modo oscuro deben compartir superficies coherentes (exterior grafito, paneles oscuros) sin grandes márgenes ni marcos blancos accidentales.
4. **Corregir la causa y no solo los síntomas:** inspeccionar el orden efectivo de las reglas, hojas compartidas, reglas inline y especificidad; aplicar selectores de tema dirigidos al contenedor afectado sin sustituir indiscriminadamente fondos de gráficos, tablas o componentes que necesiten estilos propios. No alterar texto, datos, cálculos ni imágenes al corregir la presentación.
5. **Consistencia en artículos antiguos y nuevos:** usar paleta grafito/dorado, encabezados proporcionados y superficies continuas en los artículos de Market Perspectives, incluso los que estén bajo `studies/` en lugar de `perspectives/`. No suponer que todos los artículos editoriales residen en la misma carpeta.
6. **Verificación visual obligatoria:** revisar la página realmente desplegada, desde cabecera hasta pie, en claro y oscuro, para escritorio y móvil. Confirmar que el panel principal no queda blanco, que no existe texto claro sobre fondo claro, que los gráficos conservan contraste y que el enlace de vuelta y «Continue exploring» funcionan. Si no se puede abrir el sitio publicado, indicar que la corrección solo está confirmada en GitHub.
7. **Rastreo y descubrimiento:** después de publicar comprobar registro editorial, catálogo general, canonical, sitemap (solo URLs ya liberadas) y acceso público; no dar por terminada una publicación solo porque el HTML y el JSON estén en el repositorio.
8. **Rankings de propósito específico:** los estudios de rentabilidad y drawdown pueden utilizar un esquema de columnas diferente del ranking semanal de nueve campos, siempre que coincida con el Excel fuente y que `columns`, cada fila de `rows` y las columnas/etiquetas del HTML estén sincronizadas. Al retirar campos públicos, actualizar conjuntamente JSON, encabezados, buscadores, ordenación y «Copy complete ranking», verificar el mismo número de filas y no modificar silenciosamente las medidas.
9. **Regresión tras modificaciones:** comprobar que la corrección de un artículo no desconfigura otros artículos editoriales, ni los de publicación programada. Registrar cada intervención y evitar CSS global nuevo sin pruebas de contraste y de funcionamiento en las páginas afectadas.

**Casos de control (22/10/2026):** `studies/2026-10-12-silver-bull-market/index.html` y `perspectives/2026-10-19-gold-silver-miners-leadership/index.html` presentaron contenedor exterior blanco y contenido interior oscuro. El artículo `perspectives/2026-10-22-mining-divergence/index.html` se añadió al catálogo, pero hubo que registrarlo también en la lista editorial visible de la portada. Estos antecedentes son pruebas de regresión obligatorias; los cambios de código no sustituyen la comprobación visual de GitHub Pages.
