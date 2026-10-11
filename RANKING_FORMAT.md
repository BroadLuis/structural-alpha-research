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
8. **Descargas y metodología:** Excel revisado y otros materiales públicos cuando proceda, con enlaces comprobados.

No es obligatorio que todos los estudios incluyan los mismos indicadores; sí es obligatorio que la narrativa refleje fielmente los datos disponibles.

## 3. Gráficos, imágenes y tablas analíticas

1. Comprobar que títulos, ejes, fechas, leyendas, unidades, escalas y series coinciden con los datos originales.
2. Mantener los gráficos legibles en ordenador y móvil, sin cortes, solapamientos ni texto ilegible.
3. Evitar escalas engañosas y explicar las comparaciones entre universos o períodos no equivalentes.
4. Utilizar solamente imágenes, gráficos y datos cuya publicación esté autorizada; no incluir información privada ni marcas o firmas ajenas al estilo aprobado.
5. No modificar gráficos o rankings que ya funcionen al introducir cambios en otra parte del artículo.

## 4. Rankings completos — reglas obligatorias

El estudio ASX (`studies/2026-10-09-asx/index.html`) es la referencia canónica del formato de rankings.

1. Publicar **todos** los valores del universo, nunca solo una selección de mejores o peores.
2. Mostrar, cuando estén disponibles, **Weekly Rank, Global Rank, Ticker, Company, Last Close, 1W, 4W, 3M y YTD**.
3. Rentabilidades positivas: fondo verde; negativas: rojo/rosa; cero: neutro. Usar porcentajes con signo de manera consistente.
4. **Ordenador:** tabla completa, legible, con búsqueda visible encima de la tabla y ordenación funcional.
5. **Móvil:** fichas verticales etiquetadas, con los mismos datos y sin desplazamiento horizontal; buscador propio y ordenación funcional.
6. **Ambos buscadores** deben filtrar por ticker o nombre de empresa mientras se escribe, recuperar todos los valores al borrar el texto y seguir funcionando después de ordenar o cargar datos dinámicamente. El buscador móvil **no sustituye** al de escritorio.
7. Mostrar recuento total de empresas y proporcionar descarga operativa del Excel original revisado.
8. Mantener sincronizados Excel, JSON (si procede) y referencias HTML; verificar que se cargan **todas las filas** y que el número coincide con el universo.
9. Utilizar `assets/structural-alpha-ranking.css` para la presentación compartida. No sustituir una tabla que funciona por otra implementación sin verificarla.

## 5. Organización de archivos y catálogo

1. Cada estudio debe tener su carpeta propia, por ejemplo `studies/AAAA-MM-DD-mercado/`, con su `index.html` y los recursos públicos necesarios.
2. La portada pública es `index.html` (raíz). El catálogo maestro es `reports.json`.
3. Registrar cada estudio en `reports.json` con **title, date, universe, summary y url**; incluir **download** cuando exista un archivo descargable.
4. El campo `universe` debe coincidir **exactamente** con una opción del filtro de la portada (por ejemplo, `ENERGY`).
5. El resumen del catálogo debe ser breve y basado en datos: objetivo editorial de **30–65 palabras**; el validador actual rechaza más de **85 palabras**.
6. Sincronizar el bloque `// BEGIN GENERATED REPORT SNAPSHOT` / `// END GENERATED REPORT SNAPSHOT` de `index.html` con `reports.json`, conservando contenido y orden.
7. Verificar rutas relativas, enlaces a recursos, descarga de Excel y acceso público sin autenticación.
8. Usar GitHub Releases para archivos ZIP de gran tamaño cuando corresponda; no subir archivos innecesarios o privados al repositorio.

## 6. Metadatos y presentación web

1. Mantener la identidad visual del sitio y la navegación coherente con el resto de estudios.
2. Cada página debe tener título HTML, descripción y metadatos para compartir en redes (Open Graph y Twitter/X) acordes con el artículo. Revisar sus enlaces e imagen de vista previa.
3. Verificar visualización en escritorio y móvil, incluidos tema claro/oscuro cuando la página lo implemente.
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
- [ ] Excel público revisado; sin datos privados, claves, señales propietarias o información personal.

**Revisión del ranking (si existe):**
- [ ] Número de filas igual al universo completo; columnas y rentabilidades correctas.
- [ ] Colores positivos/negativos/neutros y signos verificados.
- [ ] Buscador y ordenación probados **por separado** en escritorio y móvil.
- [ ] Fichas móviles legibles, sin scroll horizontal, y Excel descargable.
- [ ] Carga dinámica, borrado del filtro y reordenación probados.

**Revisión técnica:**
- [ ] Entrada de `reports.json` completa, filtro `universe` correcto y snapshot de portada idéntico.
- [ ] Ejecutado `python scripts/validate_research.py` **sin errores**.
- [ ] Todos los enlaces, imágenes, descargas y metadatos revisados.
- [ ] Beacon de Cloudflare exactamente una vez; ningún contador público.
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

## 10. Mantenimiento y control de cambios

- Usar este documento como checklist en todos los estudios futuros.
- Mantener el formato ASX como referencia visual, sin copiar errores ni sobrescribir funcionalidades que ya funcionen.
- Si se detecta una nueva necesidad general, actualizar primero estas normas y aplicar la mejora a los artículos afectados cuando proceda.
- No afirmar que un requisito está automatizado si solo se revisa manualmente.
- Conservar las instrucciones editoriales del `README.md` como documentación complementaria; ante una diferencia, revisar y armonizar ambos documentos antes de publicar.
