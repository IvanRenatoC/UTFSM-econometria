# Clase 4 · Regresión lineal múltiple en R

- [Abrir la clase](index.html)
- [Notebook con kernel R](clase-taller-4.ipynb)
- [Contenido en PDF](contenido-clase-4-taller.pdf)
- [Script completo en R](clase-taller-4.R)
- [Guía con explicaciones y código](guia-docente-taller-4.md)
- [Fuente teórica y orden de contenidos](https://hizocar.github.io/econometria-usm/clases/clase4/)

Horario: 18:50 a 21:25; descanso de 20:00 a 20:15. Son 140 minutos efectivos.

## Contenidos

La lámina inicial presenta Ŷ = Xβ̂, su versión por observación y los argumentos principales de lm(). Antes de comparar modelos se distinguen el plano de predicción y la proyección MCO.

14 láminas en cinco bloques. Comparamos modelos simples y múltiples, revisamos MCO y notación matricial, analizamos el modelo completo de wage2 y cerramos con un ejercicio en Colab sobre gpa2.

Los gráficos usan resultados calculados por el mismo código R del notebook. Se incluyen `wage2` (935 observaciones) y el ejemplo numérico de cinco personas de la cátedra. Los valores de educación 74 a 119 del ejemplo de cinco personas son valores didácticos; no se interpretan como años reales.

En Colab selecciona **R** como tipo de entorno y ejecuta de arriba hacia abajo. El primer bloque usa el paquete `wooldridge` si no encuentra el archivo local. Para ejecutar localmente, utiliza esta carpeta como directorio de trabajo. No requiere `rpy2` ni `%%R`.

## Regeneración y verificación

`contenido-clase-4.json` es la fuente común. No edites a mano la página o las celdas generadas.

```sh
# Requiere Node y el módulo webR 0.6.0 instalado fuera del repositorio.
WEBR_MODULE=/ruta/a/webr/dist/webr.mjs node clase-4-taller/herramientas/verificar_en_R.mjs
python3 clase-4-taller/herramientas/generar_web.py
```

El verificador ejecuta los 11 bloques de R de la clase y comprueba la muestra común, la selección de regresores y la comparación de R². Guarda salidas, datos de los gráficos y una huella del código; el generador exige esa huella antes de actualizar web, notebook, script y guía.

Fuentes técnicas: documentación oficial de R para [model.matrix](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/model.matrix.html), [solve](https://stat.ethz.ch/R-manual/R-devel/library/base/html/solve.html), [lm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html) y documentación de [wage2](https://justinmshea.github.io/wooldridge/reference/wage2.html).
