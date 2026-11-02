# Clase 3 · Causalidad y variable omitida en R

Taller presencial de Iván Canales, para 8–10 estudiantes. Duración: 18:50–21:25; descanso 20:00–20:15 (140 minutos de trabajo).

[Página de la clase](https://ivanrenatoc.github.io/UTFSM-econometria/clase-3-taller/) · [Cátedra de referencia](https://hizocar.github.io/econometria-usm/clases/clase3/).

## Contenido y secuencia

16 láminas, en el orden de los ocho temas de la cátedra: asociación y contrafactual; resultados potenciales; selección; aleatorización; variable omitida; signo del sesgo; controles; variables irrelevantes. El cierre aplica lo aprendido a `wage2`.

- `contenido-clase-3.json`: fuente común de consignas, código, interpretación, explicaciones y resultados de referencia.
- `clase-taller-3.ipynb`: notebook con kernel R. Ejecutar las celdas en orden. La práctica final se puede ejecutar independientemente.
- `clase-taller-3.R`: mismo código, como script.
- `guia-actividades-taller-3.md`: secuencia completa en Markdown.
- `guia-docente-taller-3.md`: tiempos, metodología y precauciones de interpretación.
- `datos/`: copias de apoyo y datos/resultados reproducibles de las figuras.
- `herramientas/`: generadores, estilos y controles interactivos.

Desde la raíz del repositorio: `python3 clase-3-taller/herramientas/generar_web.py`. Este comando regenera web, notebook, script y guía sin modificar las clases 1 y 2. Las láminas y soluciones comienzan plegadas. Se conservan búsqueda, modo presentación, tema oscuro, copia de código y navegación accesible.

## Datos y verificación

`wage1` (526 personas, CPS 1976) usa salario por hora; `wage2` (935 observaciones, 1980) usa ingresos mensuales. No son la misma muestra ni la misma unidad de salario. Fuentes: documentación del paquete [wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html) y [wage2](https://justinmshea.github.io/wooldridge/reference/wage2.html). Copias obtenidas del paquete Wooldridge; `wage2` proviene de los datos utilizados por Blackburn y Neumark (1992), según la documentación del paquete.

Las cinco personas, alarmas, asignaciones, omisiones y ejemplo de fumar son **simulaciones didácticas**; los contrafactuales se conocen porque se construyeron. El ejemplo de fumar no reproduce datos clínicos ni probabilidades de muerte. Las figuras usan las observaciones exportadas por R en `datos/resultados-interactivos.json`, no puntos aleatorios nuevos creados en el navegador.

Todos los códigos fueron ejecutados en webR 0.6.0. Salidas: `datos/salidas-verificadas-r.json`. Verificación reproducible con Node y el paquete npm `webr@0.6.0`:

```sh
WEBR_MODULE=/ruta/a/node_modules/webr/dist/webr.mjs node clase-3-taller/herramientas/verificar_en_R.mjs
```

La verificación usa los CSV locales, no instala paquetes R ni modifica las fuentes. Regenera las salidas y los datos de las figuras; después ejecutar el generador web para sincronizar los artefactos.

## Apoyo para las láminas 02–07

La notación explicativa utiliza $Y^{NT}$ y $Y^{T}$; los identificadores `Y_NT` y `Y_T` se conservan solo en el código y en sus salidas. Los contrafactuales de las cinco personas se construyen fijando efectos supuestos, nunca se deducen de las observaciones. La lámina 03 incluye tabla y fórmulas para la pizarra. Las viñetas 02–07 contienen código independiente, comprobado también en entornos R sin acceso a los objetos de las otras láminas. El notebook incorpora esas celdas y el reto de Juan por separado.
