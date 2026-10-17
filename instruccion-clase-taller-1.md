# Instrucción para preparar la clase de taller 1

**Horario y duración:** diseñar el material para una sesión presencial de **18:50 a 21:25**, con una **pausa de 15 minutos**. La ventana total es de **155 minutos**, con **140 minutos efectivos de trabajo**. El cronograma debe incluir la nivelación inicial, las actividades del curso y el cierre dentro de ese tiempo; indicar explícitamente dónde se ubica la pausa.

## 1. Encargo y contexto docente

Actúa como diseñador de material docente y especialista en enseñanza de R para econometría. Prepara una propuesta completa de taller presencial para Iván, profesor de taller de Econometría ICS-294 de la Universidad Técnica Federico Santa María.

La audiencia es un grupo de 8 a 10 estudiantes. El taller desarrolla la parte computacional de los contenidos que Sebastián Azócar presenta en cátedra. La propuesta debe permitir que el profesor explique, ejecute código frente al grupo, acompañe el trabajo de los estudiantes y discuta sus interpretaciones.

El objetivo es elaborar una experiencia similar en estructura pedagógica y línea editorial a la página de Sebastián, adaptada a una sesión práctica presencial en R. Este archivo contiene instrucciones para producir ese material; no constituye todavía la guía final del estudiante.

## 2. Documentos vinculados y jerarquía de fuentes

Lee estas fuentes antes de preparar la propuesta:

1. [Clase 1: Introducción y repaso de estadística](https://hizocar.github.io/econometria-usm/clases/clase1/). Es la referencia principal para el alcance conceptual y el orden del contenido del curso.
2. [Página principal del curso](https://hizocar.github.io/econometria-usm/). Úsala para el contexto, roles docentes y organización.
3. [Lectura clase 1 - material existente](Lectura%20clase%201%20-%20material%20existente.md). Contiene la comparación de la web con las presentaciones locales y precisiones conceptuales.
4. Material de apoyo local: [introducción](clase-1-pasado/clase1.tex), [repaso descriptivo](clase-1-pasado/clase1-repaso-estadistica-ayudantia.tex) y [repaso inferencial](clase-1-pasado/clase1-repaso-estadistica-ii.tex), junto con los PDF de igual nombre en esa carpeta.
5. [Documentación del paquete de R wooldridge](https://justinmshea.github.io/wooldridge/) y [documentación de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html), para comprobar datos, variables y procedencia.

La expresión «Guldrich» del encargo se interpreta provisionalmente como **Jeffrey M. Wooldridge**, autor del libro *Introductory Econometrics: A Modern Approach*. Confirmar la edición solo si hace falta citar ejercicios o páginas concretas. No inventar números de ejercicios, páginas ni citas del libro.

**Vinculación obligatoria confirmada por el profesor:** el material debe estar enlazado al 100% con un notebook Jupyter `.ipynb`, con kernel de R. Se interpreta la extensión escrita como «.pynb» como `.ipynb`. El notebook previsto se llamará `clase-taller-1.ipynb` y se guardará en la misma carpeta que este documento. El encargo ya fue ejecutado: [abrir notebook de R](clase-taller-1.ipynb), [guía de actividades](guia-actividades-taller-1.md) y [guía docente](guia-docente-taller-1.md). Los enlaces de retorno están incluidos en los entregables.

## 3. Requisitos obligatorios

- Todos los ejemplos, ejercicios, cálculos, gráficos y simulaciones deben estar escritos exclusivamente en R. Puede usarse RStudio como entorno de trabajo.
- Comenzar con una nivelación computacional. Solo después comenzar los contenidos del curso.
- Tras la nivelación, seguir el orden de la página de clase 1, incluida la secuencia introducción, estadística descriptiva y estadística inferencial. No adelantar un bloque para facilitar un ejemplo.
- Usar bases reales de **corte transversal** del libro de Wooldridge para las aplicaciones del curso. «Corte transversal» no equivale a una cohorte seguida en el tiempo.
- Mantener el alcance exclusivo de clase 1. No introducir estimación de regresiones, mínimos cuadrados, pruebas de coeficientes, modelos múltiples, métodos de identificación causal ni contenidos de clases posteriores.
- Mantener una línea editorial coherente con Sebastián: preguntas concretas, intuición antes de cálculo, ejemplos económicos comprensibles, apoyos visuales y autoevaluación breve.
- Diferenciar explícitamente una aplicación construida por la IA con datos del libro de un ejercicio que realmente figure en el libro.
- No copiar extensamente el libro. Citar los datos y redactar explicaciones y actividades propias.

## 4. Bloque inicial: nivelación de computación en R

Diseña una nivelación que pueda impartirse antes del bloque disciplinar, con diagnóstico inicial y ejercicios graduales. No asumir que los estudiantes dominan programación.

Seguir esta progresión:

1. **Entorno y operaciones básicas:** consola, script, comentarios, ejecución de líneas, asignación, operadores, tipos básicos, nombres de objetos e índices que comienzan en 1.
2. **Vectores:** creación, acceso, longitud, selección, modificación y preasignación mediante `numeric()` o `integer()`.
3. **Condicionales:** operadores lógicos e `if`/`else`; explicar que `if` espera una condición de longitud uno y distinguirlo de la selección de varios elementos de un vector.
4. **Ciclo `for`:** recorrer índices y llenar un vector previamente reservado; favorecer `seq_along()` o `seq_len()` según corresponda.
5. **Sucesiones:** construir sucesiones aritméticas, geométricas y una definida por recurrencia; establecer el primer término y producir los siguientes con un ciclo. Después comparar con una alternativa vectorizada cuando exista.
6. **Ciclo `while`:** explicar condición, actualización y término. Incluir una tarea de sucesión con un umbral y un máximo de iteraciones para evitar ciclos infinitos.
7. **Matrices:** dimensiones, creación, acceso por fila y columna, modificación y llenado mediante ciclos anidados. Explicar la diferencia entre un vector, una matriz y una tabla de datos.
8. **Actividad integradora:** llenar un vector con una sucesión, usar un condicional para clasificar términos y guardar resultados en una matriz con dimensiones y etiquetas claras.

Para cada tema: explicar para qué sirve, mostrar un ejemplo pequeño, pedir una predicción antes de ejecutar, proponer una modificación y mostrar la solución comentada. Incluir errores frecuentes: índices incorrectos, objetos sin inicializar, longitud de condiciones y falta de actualización en `while`.

Las sucesiones y los objetos pequeños de esta nivelación pueden ser construidos con fines de programación. Identificarlos como ejercicios computacionales, separados de las aplicaciones empíricas con Wooldridge. No introducir teoría estadística antes de su lugar en la secuencia del curso.

## 5. Datos y continuidad de los ejemplos

Preferir una base principal para evitar cambios innecesarios de contexto. Una candidata documentada es `wage1`, del paquete `wooldridge`: contiene 526 observaciones y 24 variables de la Current Population Survey de 1976. Incluye salario por hora (`wage`), años de educación (`educ`), experiencia potencial (`exper`), antigüedad laboral (`tenure`) e indicadores como `female` y `married`. Comprobar estas definiciones en su documentación antes de usarlas.

Construir aplicaciones sobre salarios, educación, distribución de ingresos laborales y comparación descriptiva de grupos. Respetar país, período, unidad de observación y unidades originales: no presentar estos datos como salarios actuales de Chile ni convertirlos implícitamente a pesos chilenos. Un umbral de educación debe describirse como tal; no afirmar que identifica exactamente un título universitario sin justificación documental.

Si se requiere otra base transversal del libro, justificar su elección, comprobar sus variables y explicar qué aporta. No usar series temporales, paneles ni cortes transversales combinados para las aplicaciones. En la sección de tipos de datos sí explicar las tres estructuras, mediante esquemas conceptuales y la identificación de la estructura de la base elegida.

Al cargar los datos, incluir instalación separada y de una sola vez del paquete, carga reproducible, inspección de estructura, diccionario de las variables utilizadas y tratamiento explícito de valores faltantes. Priorizar R base y pocos paquetes. No exigir cuentas, claves ni servicios externos.

## 6. Secuencia obligatoria del contenido del curso

Usar esta tabla como lista de cobertura. Las láminas corresponden a la numeración de contenido de la web, sin portada. Una actividad puede abarcar láminas consecutivas, pero no alterar su orden.

### Parte 1: introducción a la econometría

| Orden web | Tema | Adaptación requerida para el taller |
|---|---|---|
| 1 | Qué es econometría | Abrir con una pregunta sobre salarios y educación; reconocer qué información permite responderla. Inspeccionar observaciones sin anticipar cálculos de bloques posteriores. |
| 2 | Econometría moderna | Distinguir descripción, causalidad y predicción mediante preguntas sobre la misma base; no ajustar modelos predictivos. |
| 3 | Método econométrico | Formular pregunta, variables observables y factores no observados; vincular el modelo conceptual con las columnas de la base. No estimar regresiones. |
| 4 | Causalidad y correlación | Explicar por qué una asociación observada no demuestra un efecto; discutir factores omitidos. Si se muestra un gráfico, evitar incorporar una medida no enseñada como requisito adicional. |
| 5–6 | Universidad y salarios | Adaptar la pregunta a educación y salarios de la base; separar asociación de efecto causal y explicitar las limitaciones de cualquier clasificación educativa. |
| 7 | Herramienta aplicada | Conectar las preguntas de desparasitación y consultoría mencionadas en cátedra con la importancia del diseño y los datos. No atribuir a `wage1` los resultados de esos estudios ni inventar sus bases. |
| 8–11 | Tipos de datos | Separar origen experimental/observacional de estructura transversal/temporal/panel. Identificar y justificar el carácter transversal y observacional de la base elegida. |
| 12–13 | Muestreo, población y muestra | Identificar unidad, población de referencia y muestra; presentar el marco de datos disponible para las prácticas. |
| 14 | Por qué muestrear | Discutir recursos, acceso y alcance de la información. |
| 15 | Objetivos del muestreo | Distinguir variable, parámetro y estadístico sin adelantar el desarrollo de las fórmulas descriptivas. |
| 16–17 | Métodos de muestreo | Practicar selección aleatoria simple, sistemática, estratificada y por conglomerados cuando la estructura disponible lo permita. |
| 18 | Estratos y conglomerados | Comparar selección dentro de estratos y selección de grupos. No inventar barrios, hogares ni conglomerados naturales de la base. Si se crean grupos artificiales, señalar que solo ilustran el algoritmo y no un diseño real de encuesta. |
| 19 | Muestreo no probabilístico | Construir una selección por conveniencia o criterio explícito y discutir sus limitaciones, sin presentarla como representativa. |
| 20 | Descriptiva e inferencial | Cerrar distinguiendo resumir los datos observados de inferir a una población. |

Para las prácticas de selección, usar provisionalmente la base completa como **población finita didáctica**. Submuestrearla no reproduce automáticamente el diseño original de la encuesta. Mantener esta distinción en las actividades posteriores.

### Parte 2: estadística descriptiva

| Orden web | Tema | Adaptación requerida para el taller |
|---|---|---|
| 1 | Ramas de la estadística | Recuperar la distinción descriptiva/inferencial con la pregunta empírica. |
| 2 | Estadísticos como funciones de datos | Identificar el vector que se resumirá y el resultado de una función. |
| 3–4 | Media y mediana | Calcular ambas en R, mostrar cómo se obtienen y comparar sensibilidad a extremos. |
| 5 | Percentiles y cuartiles | Usar `quantile()` e indicar la convención elegida. |
| 6–7 | Dispersión | Calcular rango intercuartílico, varianza muestral y desviación estándar; interpretar unidades y denominador `n - 1`. |
| 8 | Histograma | Usar `hist()` y comparar distintos números de intervalos sin cambiar los datos. |
| 9–10 | Boxplot | Usar `boxplot()` e interpretar mediana, caja, bigotes y posibles atípicos. |

No afirmar que los valores del boxplot de R coinciden necesariamente con `quantile()` bajo todas las convenciones. Explicar diferencias si aparecen. Si se agrega un valor extremo artificial, hacerlo sobre una copia identificada como modificación didáctica, preservando la base original.

### Parte 3: estadística inferencial

| Orden web | Tema | Adaptación requerida para el taller |
|---|---|---|
| 1 | Inferencia | Precisar qué parámetro se quiere estudiar y bajo qué supuestos. |
| 2 | Intervalos de confianza | Explicar estimación e incertidumbre antes de presentar código. |
| 3 | TCL | Preparar una visualización de la distribución de medias muestrales. |
| 4 | Supuestos TCL | Revisar independencia, distribución común, momentos finitos y carácter orientativo de los tamaños recomendados. |
| 5–7 | Primer ejemplo de IC | Construir un ejemplo análogo al de ventas con una variable de la base de Wooldridge, sin atribuirle los datos originales de ventas. |
| 8 | IC de 95% | Identificar estimación, error estándar, valor crítico y límites. |
| 9–10 | Otros niveles de confianza | Cambiar el nivel manteniendo constantes los datos del ejercicio. |
| 11 | Comparación de intervalos | Visualizar el cambio de anchura. |
| 12–13 | Confianza y precisión | Repetir el muestreo y observar cobertura y margen de error. |
| 14 | Tamaño muestral para una media | Calcular un tamaño para una precisión deseada y redondear hacia arriba. |
| 15–19 | Proporciones | Elegir un indicador real de la base o una definición derivada explícita; calcular estimación, condiciones e intervalo aproximado. |
| 20–21 | Ejemplo y respuesta de proporciones | Proponer un enunciado propio con la base, dejar tiempo de resolución y luego mostrar la solución. |
| 22 | Tamaño muestral para proporciones | Explicar estimación preliminar y alternativa conservadora de 0,5. |
| 23–24 | Aplicación de tamaño muestral | Resolver un caso análogo al de chips con la proporción seleccionada; distinguir longitud total y margen de error. |
| 25 | Diferencia de medias | Formular una comparación de dos grupos de la base. |
| 26–27 | Parámetro e interpretación | Definir el sentido de la resta y qué significa incluir o excluir cero. |
| 28–31 | Caso de varianzas conocidas y muestras grandes | Desarrollar el procedimiento de cátedra con supuestos explícitos. |
| 32–34 | Ejemplo, solución y conclusión | Resolver la comparación y redactar una conclusión estadística sin atribución causal. |

**Restricción para inferencia:** las bases reales normalmente no ofrecen una desviación poblacional conocida. No usar la desviación de la muestra y llamarla poblacional. Para conservar el procedimiento de clase 1, proponer una simulación basada en la distribución empírica completa de la base, tratada como población didáctica conocida, y extraer muestras independientes con reemplazo. Así pueden conocerse la media y varianza de esa distribución y observarse cobertura y TCL. Calcular la varianza poblacional con denominador `N`, no con `N - 1`. Para comparar grupos, definir dos distribuciones empíricas y muestrear de cada una por separado.

Distinguir esos resultados didácticos de una inferencia sobre la población real de la encuesta. No introducir automáticamente intervalos t, bootstrap, correcciones de diseño o nuevas técnicas para resolver esta limitación, porque ampliarían el alcance solicitado. Si se desea muestreo sin reemplazo, explicar la corrección por población finita o usar el esquema con reemplazo para conservar la fórmula vista en cátedra.

## 7. Línea editorial y dinámica presencial

Redactar en español claro, cercano y riguroso. Usar títulos breves, preguntas iniciales y apoyos visuales cuando aporten. Mantener el patrón de la página de Sebastián: objetivo, caso, intuición, actividad, solución y autoevaluación. Evitar reproducir su identidad o atribuirle la autoría de actividades nuevas.

Cada actividad debe contener:

1. Pregunta económica o computacional y vínculo exacto con el apartado de clase 1.
2. Base y variables, con unidades y procedencia.
3. Predicción breve del estudiante antes de ejecutar.
4. Código R inicial y consigna de modificación o resolución.
5. Solución comentada, separada de la consigna para no revelarla antes de tiempo.
6. Interpretación y límite de la conclusión.
7. Error frecuente y pregunta breve de verificación.

Para 8 a 10 alumnos, proponer trabajo individual o en 4 a 5 parejas, con pausas de discusión colectiva. Alternar demostraciones cortas con ejecución por los estudiantes. Permitir que el profesor observe avances sin convertir cada actividad en una evaluación formal.

La interactividad debe implementarse mediante cambios de parámetros y ejecución en R. No exigir una aplicación web ni Shiny para comenzar. Si se propone después un formato web, mantener todos los cálculos y ejemplos del taller en R.

## 8. Planificación y entregables que debe producir la IA

Planificar la sesión de 18:50 a 21:25, reservando 15 minutos de pausa y distribuyendo exactamente 140 minutos efectivos entre nivelación, contenidos del curso, práctica y cierre. Proponer la ubicación de la pausa, ya que su hora exacta no está fijada. Presentar una agenda con horas de inicio y término por bloque. Mantener todos los contenidos en el material y en el notebook, en el orden requerido; distinguir las actividades que se realizan presencialmente de las ampliaciones para trabajo autónomo cuando sea necesario para respetar el horario. No comprimir artificialmente los ejercicios ni suponer que cada lámina requiere una actividad independiente.

Producir una guía docente y una guía de actividades que incluyan:

- Objetivos observables y diagnóstico inicial de programación.
- Agenda modular: nivelación primero y contenidos del curso después, respetando el orden.
- Mapa de correspondencia con todos los apartados de clase 1.
- Casos propios basados en datos de Wooldridge, con atribución y diccionario mínimo.
- Código R reproducible, ejercicios graduados y soluciones separadas.
- Guion de preguntas y pausas para conducir la sesión presencial.
- Autoevaluación final breve, con respuestas justificadas.
- Lista de preparación: R y RStudio, paquete de datos, scripts y alternativa local si falla internet.
- Referencias y registro de decisiones o supuestos pendientes.

No crear ni publicar un sitio, modificar la página de Sebastián ni enviar material a los alumnos sin que el profesor lo solicite. El primer resultado debe ser revisable localmente.

## 9. Correspondencia completa con el notebook de R

El entregable computacional obligatorio es `clase-taller-1.ipynb`. Debe cubrir el 100% del material desarrollado para el taller, desde la nivelación hasta el cierre del curso, en idéntico orden. No basta con enlazar un notebook que contenga solo algunos ejemplos.

- Usar celdas Markdown para objetivos, preguntas, explicaciones, consignas, interpretación, referencias y soluciones narrativas; usar celdas de código exclusivamente R para cálculos, gráficos y simulaciones.
- Configurar el kernel de R mediante IRkernel e incluir instrucciones de preparación. La interfaz Jupyter no habilita ejemplos ni celdas Python.
- Asignar identificadores estables a todos los bloques y actividades, por ejemplo `NIV-01`, `P1-01`, `P2-01` y `P3-01`. Usar los mismos identificadores en la guía, en el notebook y en la matriz de correspondencia.
- Incluir una matriz de trazabilidad que relacione cada requisito de estas instrucciones y cada actividad de la guía con su sección o celda identificada del notebook. Los requisitos de contexto y estilo deben reflejarse en el diseño o metadatos correspondientes; no convertirlos artificialmente en ejercicios.
- Mantener coincidencia entre enunciados, datos, variables, código, resultados y soluciones. No dejar ejercicios de la guía sin desarrollo en el notebook ni ejemplos computacionales del notebook sin referencia en la guía.
- Separar enunciado y solución en celdas distintas, para que el profesor pueda decidir cuándo mostrarla. No depender de extensiones no documentadas para ocultar respuestas.
- Añadir un enlace relativo desde esta instrucción al notebook y desde el notebook a `instruccion-clase-taller-1.md`, una vez creado. Añadir también el enlace a la lectura comparativa y a la página de clase 1.
- Verificar que el notebook se ejecuta de principio a fin con un kernel limpio, sin depender del orden manual de ejecución, objetos previos ni rutas absolutas del computador del profesor.
- Informar la cobertura final como requisitos y actividades cubiertos sobre el total. Exigir 100%; si falta algo, enumerarlo y completar el trabajo antes de declararlo terminado.

La elaboración del notebook fue solicitada posteriormente por el profesor y los entregables están vinculados en la sección 2. La ejecución con R queda pendiente por falta de un runtime disponible en el entorno de elaboración; revisar el estado de validación en la guía.

## 10. Validación antes de entregar

Comprobar el orden, alcance y coherencia con la web consultada. Ejecutar todo el código en una sesión limpia de R, si el entorno lo permite, y registrar qué se verificó. Si no se puede ejecutar, indicar claramente qué quedó sin validar; no inventar salidas numéricas.

Usar `set.seed()` en las actividades aleatorias, verificar tamaños y grupos, manejar faltantes y conservar los datos originales. Comprobar que las soluciones coinciden con el código y que los gráficos tienen títulos, ejes y unidades legibles.

Revisar especialmente que ninguna comparación descriptiva se presente como causal, que no se introduzcan regresiones y que todos los ejemplos empíricos provengan de bases transversales documentadas de Wooldridge.

## 11. Preguntas pendientes para el profesor

1. ¿Qué experiencia tienen los alumnos con R y tendrán computador con R/RStudio instalado?

Estas preguntas permiten afinar la implementación. No impiden preparar la estructura y las actividades bajo los requisitos ya establecidos.
