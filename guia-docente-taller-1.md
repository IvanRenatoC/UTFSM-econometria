# Guía docente · Taller 1

Iván dirige el taller computacional de la materia de Sebastián para 8 a 10 alumnos, en 4 a 5 parejas. Se asume experiencia inicial heterogénea; no se exige programación previa. La sesión está diseñada para 18:50–21:25 con pausa 20:00–20:15: 140 minutos efectivos.

[Guía de actividades](guia-actividades-taller-1.md) · [Notebook R](clase-taller-1.ipynb) · [Script equivalente](clase-taller-1.R) · [Instrucciones](instruccion-clase-taller-1.md)

## Preparación antes de la clase

- Comprobar R y RStudio en los equipos. Para notebook, instalar Jupyter e IRkernel y seleccionar kernel R según el inicio de la guía.
- Entregar la carpeta con el notebook, script y `datos/wage1.csv`. Mantener rutas relativas.
- Ejecutar todo previamente: en una terminal con R disponible, `Rscript --vanilla clase-taller-1.R`; desde RStudio abrir la carpeta del proyecto, reiniciar R y ejecutar el script. El notebook debe ejecutarse desde su primera celda con kernel limpio.
- No hay ejecución R verificada en el entorno de elaboración; no usar este material en clase sin esa comprobación. Si una celda falla, conservar el mensaje y corregir antes de continuar.
- Los ejercicios son propios con datos de Wooldridge. La documentación de wage1 identifica sus variables; no adjudicar a Sebastián ni al libro los enunciados creados aquí.

## Conducción minuto a minuto

| Hora | Ruta y conducción |
|---|---|
| 18:50–18:55 | Diagnóstico del inicio. Pedir respuestas a tres estudiantes distintos. Abrir notebook y confirmar kernel. |
| 18:55–18:57 | NIV-01 (lámina 01). Escribe tu nombre y observa la consola. |
| 18:57–19:00 | NIV-ASIG (lámina 02). Asigna x e y, calcula z y w; print(x) y print(w) muestran 2 y 3. |
| 19:00–19:04 | NIV-03 (lámina 03). Anticipar el mensaje con valores 3 y 8; el ejemplo define sus propios valores. |
| 19:04–19:07 | NIV-06 (lámina 04). while: condición previa, actualización y límite de seguridad. |
| 19:07–19:09 | NIV-FOR (lámina 05). for: recorrido de pasos y salida anticipada con break. |
| 19:09–19:14 | NIV-05 (lámina 06). Parejas completan 1, 2, 4, 8, 16 y 32. |
| 19:14–19:20 | NIV-02 (lámina 07). Reservar 20 ceros; asignar −1 en posiciones impares y luego reemplazar cada cero por su índice. |
| 19:20–19:27 | NIV-07. Crear la identidad de 3 × 3; reconocer filas, columnas y la transposición. |
| 19:27–19:33 | NIV-08. Crear las potencias de 3 y organizarlas en una matriz de 3 × 2; leer sus columnas. |
| 19:33–19:35 | NIV-NOTEBOOK (lámina 10). Vista general: librerías, adecuación de datos, EDA, modelamiento y resultados. |
| 19:35–19:42 | P1-01 a P1-05 en orden. Cargar datos; ubicar país/año; discutir asociación sin calcular aún medias. |
| 19:42–19:47 | Recorrer video, gráficos y razones para muestrear. Preparar wage1 para P1-08. |
| 19:47–20:00 | P1-08: ejecutar preparación y cuatro muestreos en orden. Continuar con P1-14. No comparar eficiencia de grupos artificiales. |
| 20:00–20:15 | Pausa de 15 minutos. |
| 20:15–20:18 | P2-01 y P2-02. Qué entra y sale de una función. |
| 20:18–20:27 | P2-03 a P2-05. Cada pareja anticipa qué hace un extremo y calcula medidas de centro y dispersión. |
| 20:27–20:40 | P2-06 y P2-07. Mostrar histograma y boxplot, comparar intervalos y explicar atípicos sin borrarlos. |
| 20:40–20:47 | P3-01: inferencia, TCL y supuestos; cambiar n en la figura. |
| 20:47–20:54 | P3-05: IC de media y repetición de intervalos del ejemplo de ventas. |
| 20:54–21:01 | P3-07: confianza, precisión y planificación de n. |
| 21:01–21:08 | P3-11: 19/200 defectuosos, referencia 0,05 y tamaño para proporciones. |
| 21:08–21:15 | P3-15: diferencia de medias con varianzas conocidas, ejemplo de carreras de Sebastián. |
| 21:15–21:25 | Autoevaluación individual, discusión en pareja y respuesta colectiva. Registrar dudas para apoyo posterior. |

El tiempo para todas las láminas es una revisión computacional selectiva, no una clase exhaustiva de inferencia. Las ampliaciones se conservan en orden y no se eliminan del notebook. Si el diagnóstico muestra dificultades, reducir modificaciones autónomas durante la sesión y usar las demostraciones ya preparadas; conservar el horario y asignar la práctica restante para después.

## Preguntas que vale la pena detenerse a escuchar

- NIV-03: ¿por qué no usar if con todo el vector? Esperar que distingan una decisión de una selección por elemento.
- P1-04: ¿qué no mantiene constante este gráfico? Esperar habilidad, experiencia o contexto familiar.
- P1-08: ¿qué representa cada selección? Aclarar inicio aleatorio del sistemático, pesos por estrato y grupos artificiales.
- P2-03: ¿el dato extremo es real? No: es una copia alterada con propósito explícito.
- P3-01: ¿de qué población conocemos sigma? Solo de nuestra distribución empírica didáctica.
- P3-05: ¿el 95% tiene que cumplirse exactamente en pocas repeticiones? No; fluctúa y depende de aproximación.
- P3-15: ¿puede decirse que estudiar causó la diferencia? No.

## Revisión y decisiones

La matriz completa de cobertura y los IDs están al final de la guía y notebook. Las guías y el notebook comparten consignas, soluciones y código generados desde `herramientas/generar_taller.py`. No editar solo una copia: regenerar las salidas tras modificar ese origen. El script `.R` facilita una alternativa en RStudio.

No se publicó ni modificó ningún sitio. No se requirió GitHub para crear el material. La experiencia previa e instalaciones de los alumnos siguen sin confirmarse; comprobarlas antes del taller. El material contiene soluciones abiertas en celdas separadas: durante la actividad detenerse antes de la solución y pedir al estudiante que escriba su intento en una celda nueva.

## Correspondencia de las cinco láminas de inferencia con Sebastián

| Lámina del taller | Contenido de la cátedra conservado |
|---|---|
| 01 · Inferir, TCL y supuestos | Estadística inferencial, distribución muestral del promedio, TCL, i.i.d. y momentos finitos. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#teorema-central-del-limite). |
| 02 · IC de una media | Interpretación frecuentista, σ conocida, ventas: media 200, σ 60, n 36, IC 95 %. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ic-ejemplo1). |
| 03 · Confianza, precisión y n | Niveles de confianza, ancho/margen, efecto de n y fórmula de tamaño muestral con redondeo superior. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#intervalos-de-confianza-determinacion-del-tamano-muestral). |
| 04 · Proporciones | Aproximación normal y condiciones, 19 defectuosos de 200, referencia 0,05, planificación con p* y E. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ic-para-las-proporciones-ejemplo). |
| 05 · Diferencia de medias | Dos grupos independientes, varianzas conocidas, medias 800.000/680.000, n 144/121 y σ 60.000/50.000; interpretación del cero. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ejemplo_1). |

La visualización del TCL usa wage1 como población empírica didáctica. Los otros ejemplos conservan los números de Sebastián y no se atribuyen a wage1. No se añaden pruebas de hipótesis, regresiones estimadas ni métodos fuera del repaso de la cátedra. Las figuras se actualizan matemáticamente en el navegador; el código R reproduce las fórmulas y sus parámetros. No se ha ejecutado R en este entorno.
