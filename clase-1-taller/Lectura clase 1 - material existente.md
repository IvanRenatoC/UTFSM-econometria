# Lectura clase 1 - material existente

Fecha de revisión: 17 de octubre de 2026.

Esta lectura explica la página principal del curso y la página de clase 1, y las compara con los materiales de la carpeta `clase-1-pasado`. La comparación muestra una continuidad amplia de contenidos: la página de clase 1 conserva la secuencia de las tres presentaciones locales y agrega recursos para estudiar, practicar y visualizar los conceptos. La página principal aporta la organización del curso vigente.

## 1. Fuentes y alcance

Se consultaron directamente estas dos páginas:

- [Página principal de Econometría ICS-294](https://hizocar.github.io/econometria-usm/).
- [Clase 1: Introducción y repaso de estadística](https://hizocar.github.io/econometria-usm/clases/clase1/).

En el material local se revisaron los tres archivos `.tex` y se extrajo el texto de los tres PDF. Los PDF tienen 21, 11 y 35 páginas, respectivamente. Los archivos fuente tienen el mismo número de cuadros activos, contando la portada. Esta revisión compara contenidos y organización; no certifica identidad visual ni equivalencia exacta entre las versiones PDF y LaTeX.

| Material local | Contenido | Correspondencia en la web |
|---|---|---|
| `clase1.tex` y `clase1.pdf` | Introducción a la econometría, datos y muestreo | Parte 1: cátedra; 20 láminas de contenido |
| `clase1-repaso-estadistica-ayudantia.tex` y su PDF | Estadística descriptiva | Parte 2: ayudantía; 10 láminas de contenido |
| `clase1-repaso-estadistica-ii.tex` y su PDF | Estadística inferencial e intervalos de confianza | Parte 3: ayudantía; 34 láminas de contenido |
| `image.png`, `hist.png`, `box_plot.png` | Figuras de muestreo, histograma y boxplot usadas por los fuentes | La web presenta figuras de esos mismos temas, además de recursos adicionales |

La web identifica los fuentes como `sem1/clase1.tex`, `sem1/repaso_ayudantia.tex` y `sem1/repaso_estadistica.tex`. Los nombres de los dos repasos difieren de los locales; la correspondencia se establece por sus temas, ejemplos y orden. La diferencia de una lámina por presentación se explica por la portada local, excluida de la numeración de contenido web.

## 2. Qué explica la página principal

La [página principal](https://hizocar.github.io/econometria-usm/) presenta Econometría ICS-294 para Ingeniería Comercial de la Universidad Técnica Federico Santa María. Enuncia tres propósitos que orientan la asignatura:

- **Describir relaciones:** estudiar cómo varía el promedio de una variable al cambiar otra. Por ejemplo, comparar salarios según educación.
- **Identificar causas:** determinar si una variable produce cambios en otra, considerando los demás factores relevantes.
- **Predecir:** anticipar valores futuros, como ventas, inflación o tipo de cambio.

Estas preguntas requieren objetivos y supuestos diferentes. Observar que las personas con más educación ganan más describe una relación; atribuir esa diferencia a la educación exige justificar una interpretación causal.

La portada organiza el trabajo en cátedra los viernes, de 18:40 a 21:25, taller los lunes y un proyecto grupal con datos reales. Identifica a Sebastián Azócar en cátedra y a Iván en taller. Señala 6 créditos SCT, MAT-033 como prerrequisito y un período entre el 12 de octubre de 2026 y el 22 de enero de 2027.

La evaluación publicada se distribuye así:

| Evaluación | Ponderación | Fecha o distribución publicada |
|---|---:|---|
| Certamen 1 | 20% | 16 de noviembre de 2026 |
| Certamen 2 | 20% | 14 de diciembre de 2026 |
| Certamen 3 | 20% | 18 de enero de 2027 |
| Dos controles y tres talleres | 15% | Controles: semanas 2 y 9; talleres: semanas 4, 8 y 12 |
| Trabajo práctico | 25% | Primera entrega: 5%; informe final: 10%; presentación: 10%. La portada sitúa el cierre en semana 14 |
| Recuperativa | Sin ponderación propia indicada | 22 de enero de 2027 |

Las fechas y condiciones corresponden a lo publicado al revisar el sitio. La portada remite al programa para los requisitos completos de aprobación y al calendario para la planificación semanal. Esas páginas enlazadas no forman parte de esta comparación.

## 3. Qué explica la página de clase 1

La [clase 1](https://hizocar.github.io/econometria-usm/clases/clase1/) está fechada el viernes 16 de octubre de 2026. Reúne el material introductorio y dos repasos, pero distingue expresamente su uso: la Parte 1 corresponde a cátedra y las Partes 2 y 3 a ayudantía, en otra sesión.

### 3.1. Parte 1: introducción a la econometría

La econometría combina teoría económica, estadística y datos para estudiar preguntas económicas. El método comienza con una pregunta, propone un modelo económico y lo convierte en un modelo que pueda estimarse y contrastarse. El término de error representa factores que el modelo no recoge explícitamente.

Un eje central es la distinción entre correlación y causalidad. El ejemplo compartido con el material local considera personas de 35 años en Chile: quienes completaron la universidad ganan un 30% más. Esa comparación, por sí sola, no permite concluir que la universidad causó toda la diferencia, porque los grupos también pueden diferir en habilidad, recursos familiares y otras características.

Se presentan aplicaciones sobre desparasitación escolar y consultoría de gestión, así como dos maneras de clasificar los datos. Una clasificación considera cómo se determina la exposición o tratamiento: experimental, pseudoexperimental y observacional. Otra considera la estructura de las observaciones: corte transversal, serie de tiempo y panel. Son dimensiones distintas: unos datos pueden ser, por ejemplo, observacionales y de panel.

El bloque de muestreo distingue población, unidad de observación, muestra, parámetro y estadístico. Explica por qué se trabaja con muestras y presenta los métodos aleatorio simple, sistemático, estratificado, por conglomerados y no probabilístico. Termina diferenciando el resumen de los datos observados de la inferencia hacia una población.

### 3.2. Parte 2: repaso de estadística descriptiva

El segundo bloque organiza herramientas para resumir una muestra:

- La media y la mediana describen su centro; la mediana se obtiene ordenando los datos.
- Los percentiles y cuartiles describen posiciones dentro de la distribución.
- El rango intercuartílico, la varianza muestral y la desviación estándar describen dispersión.
- El histograma muestra frecuencias por intervalos y el boxplot resume posición, dispersión y posibles valores atípicos.

La varianza muestral presentada utiliza el denominador `n - 1`. La desviación estándar es su raíz cuadrada y conserva las unidades de la variable. El ejemplo adicional del multimillonario que entra a un bar permite apreciar por qué un valor extremo puede alterar mucho la media y bastante menos la mediana.

### 3.3. Parte 3: repaso de estadística inferencial

El tercer bloque explica cómo utilizar una muestra para estimar parámetros poblacionales y expresar incertidumbre. Introduce el teorema central del límite (TCL), la distribución del promedio muestral y los intervalos de confianza para medias, proporciones y diferencias de medias independientes.

Para una media con desviación poblacional conocida, el intervalo combina la media muestral con un margen de error. Ese margen aumenta al exigir mayor confianza y disminuye al aumentar el tamaño de la muestra. El material también despeja el tamaño muestral necesario para una precisión deseada y exige redondearlo hacia arriba.

Los ejemplos centrales coinciden con los archivos locales:

| Ejemplo | Datos principales | Resultado presentado en ambos materiales |
|---|---|---|
| Ventas mensuales | Media 200, desviación poblacional 60 y muestra de 36 | IC de 95%: `(180,4; 219,6)` |
| Ventas con mayor confianza | Mismos datos, confianza de 99% | IC presentado: `(174,3; 225,7)`, usando 2,57 como valor crítico aproximado |
| Productos defectuosos | 19 defectuosos de 200; afirmación del proveedor: 5% | IC aproximado: `(0,05433; 0,1356)`; el 5% queda fuera |
| Chips aceptables | 26 de 30 en la muestra piloto; longitud máxima del intervalo: 0,05 | Tamaño requerido presentado: 711 chips |
| Salarios de dos carreras | Medias 800.000 y 680.000; muestras de 144 y 121 | IC de la diferencia: aproximadamente `(106.756; 133.244)` pesos; excluye cero |

La web añade una explicación especialmente útil de la confianza: el 95% describe la cobertura del procedimiento al repetir el muestreo. Un intervalo ya calculado contiene al parámetro fijo o no lo contiene.

## 4. Coincidencias con el material existente

La coincidencia temática y de secuencia es alta. La introducción conserva la definición de econometría, las tres preguntas de la econometría moderna, el método, la discusión causal, los ejemplos aplicados, los tipos de datos y el muestreo. El repaso descriptivo conserva las medidas de centro, posición y dispersión, además del histograma y boxplot. El inferencial conserva el TCL, los intervalos, el vínculo entre confianza y precisión y los ejemplos numéricos.

La web declara que reproduce las diapositivas en orden. La revisión de títulos, temas, datos y soluciones plegadas respalda esa correspondencia sustantiva. Algunas respuestas que aparecen directamente en las diapositivas están ocultas inicialmente en la web bajo controles desplegables; siguen disponibles para su lectura.

Los archivos locales ya incluyen enlaces a Colab y, en el repaso inferencial, a una hoja de cálculo. Por tanto, el uso de recursos digitales externos tiene un antecedente en las presentaciones. La ampliación web consiste especialmente en incorporar actividades dentro de la propia página.

## 5. Aspectos diferentes

### 5.1. Organización, autoría y presentación

La portada web aporta equipo docente vigente, horarios, evaluaciones, créditos y enlaces de navegación. Las presentaciones locales se concentran en los contenidos académicos y atribuyen su autoría a Jocelyn Tapia Stefanoni. Conviene conservar esa distinción entre autoría del material previo y equipo que organiza el curso actual.

En dos fuentes locales, el título principal indica ICS-294, mientras el título corto conserva ICS-162. La web utiliza ICS-294. Es una diferencia de identificación que sería conveniente unificar en una futura edición.

El formato local es una secuencia de diapositivas. La web reúne los tres bloques en una lectura continua con índice, objetivos, agenda horaria, respuestas plegadas y cierre. Su agenda reserva el viernes para la introducción, datos y muestreo; el repaso estadístico se asigna a ayudantía.

### 5.2. Recursos adicionales de la web

| Tema | Ampliación observada en la web |
|---|---|
| Correlación y causalidad | Caso de helados, tiburones y temperatura; referencia ilustrativa a chocolate y premios Nobel |
| Universidad y salarios | Visualización de factores no observados asociados a la diferencia salarial |
| Estudios aplicados | Recorridos por la pregunta, comparación, diseño y resultados de los casos de Kenia e India |
| Tipos de datos | Grilla de unidades por períodos y preguntas de clasificación |
| Muestreo | Analogía de la sopa, casos por método y simulador de muestras de hogares |
| Sesgos de selección de muestras | Encuesta de Instagram y caso histórico del Literary Digest |
| Media y mediana | Caso del multimillonario en el bar y simulador de estadísticos, histograma y boxplot |
| TCL | Máquina de Galton y simulador que acumula promedios muestrales de distintas poblaciones |
| Intervalos de confianza | Analogía de aros y estaca, simulación de cobertura y calculadora de intervalos y tamaño muestral |
| Estudio autónomo | Autoevaluaciones y lectura de Wooldridge: capítulo 1 y apéndice C; anuncio de regresión lineal simple como siguiente clase |

Estos recursos se identificaron mediante la lectura de la página y de sus controles. No se realizó una auditoría del código ni de la exactitud de todos los simuladores. Sus cifras generadas al azar no deben tratarse como resultados fijos del curso.

## 6. Precisiones para acompañar la lectura

Hay formulaciones heredadas que conviene explicar con cuidado al enseñar. Las observaciones siguientes son aclaraciones conceptuales de esta lectura; no representan cambios ya realizados en las fuentes.

**Muestreo y representatividad.** La selección con probabilidades conocidas permite formular inferencias basadas en el diseño, pero una muestra concreta puede diferir de la población. También influyen la cobertura del marco muestral y la no respuesta. El muestreo sistemático con inicio aleatorio puede ser probabilístico: que los elementos restantes queden determinados después del sorteo inicial no implica que tuvieran probabilidad de inclusión cero antes del sorteo.

**Estratos y conglomerados.** La homogeneidad interna de los estratos y la heterogeneidad interna de los conglomerados son una comparación didáctica útil, no definiciones universales. La distinción operativa es muestrear dentro de todos los estratos frente a seleccionar conglomerados; en estos últimos puede observarse a todos sus integrantes o hacer una segunda etapa de muestreo. El propio material muestra ambas posibilidades.

**TCL.** Los umbrales de 30, 50 y 100 observaciones son reglas orientativas, no garantías matemáticas. La aproximación depende de la distribución y de los supuestos de muestreo. Si las observaciones independientes provienen de una población normal, la media muestral es normal para cualquier tamaño de muestra.

**Intervalos y cuantiles.** Para evitar confusiones con el cuantil inferior negativo usado en las diapositivas, puede escribirse el margen con el cuantil superior positivo: `z_(1 - alfa/2)`. Para 99%, su valor es aproximadamente 2,576; el material usa 2,57 en un ejemplo y 2,58 en otra fórmula, de modo que pequeñas diferencias numéricas responden al redondeo.

**Boxplot.** Conviene distinguir las cercas teóricas `q1 - 1,5 RIQ` y `q3 + 1,5 RIQ` de los extremos de los bigotes. En la convención usual de Tukey, los bigotes llegan a las observaciones más extremas que permanecen dentro de esas cercas. La fórmula simplificada reproducida en los materiales puede ubicar el extremo en una cerca sin una observación allí.

**Diferencia de salarios.** Que un intervalo de diferencia de medias excluya cero aporta evidencia de una diferencia entre promedios bajo los supuestos utilizados. Eso no identifica por sí solo un efecto causal de estudiar una carrera, coherentemente con la discusión inicial sobre universidad e ingresos.

## 7. Cómo usar conjuntamente los materiales

Una secuencia de estudio posible es comenzar por la portada para conocer la organización del curso, seguir la Parte 1 junto con `clase1.tex` y reservar las Partes 2 y 3 para el repaso de ayudantía. Los casos web ayudan a interpretar conceptos; los archivos locales permiten seguir las fórmulas y los ejercicios en formato de presentación.

En descriptiva, interesa poder explicar qué cambia al introducir un dato atípico. En inferencia, interesa identificar el parámetro, los supuestos, el error estándar y la interpretación del intervalo antes de sustituir números. Para preparar la siguiente clase, la página propone el capítulo 1 y el apéndice C de Wooldridge.

## 8. Referencias locales

- [Introducción: fuente LaTeX](clase-1-pasado/clase1.tex) y [presentación PDF](clase-1-pasado/clase1.pdf).
- [Repaso descriptivo: fuente LaTeX](clase-1-pasado/clase1-repaso-estadistica-ayudantia.tex) y [presentación PDF](clase-1-pasado/clase1-repaso-estadistica-ayudantia.pdf).
- [Repaso inferencial: fuente LaTeX](clase-1-pasado/clase1-repaso-estadistica-ii.tex) y [presentación PDF](clase-1-pasado/clase1-repaso-estadistica-ii.pdf).

Los enlaces locales son relativos a este documento para conservar su funcionamiento al mover la carpeta completa del proyecto. El PDF `Econometria_USM_2026_3.pdf`, situado fuera de `clase-1-pasado`, no se utilizó como fuente de esta comparación.
