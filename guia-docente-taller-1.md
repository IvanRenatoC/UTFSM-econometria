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
| 18:57–19:00 | NIV-ASIG (lámina 02). Asigna x e y, anticipa z y w y distingue guardar de imprimir. |
| 19:00–19:10 | NIV-02 (lámina 03; fusiona las antiguas láminas 02 y 04). Crear, seleccionar y modificar un vector; después reservar y llenar con for. |
| 19:10–19:12 | NIV-03 (lámina 04). Después de vectores y for, anticipar el mensaje con valores 3 y 8. |
| 19:12–19:15 | NIV-05. Parejas completan una sucesión y revisan las otras. |
| 19:15–19:20 | NIV-06. Preguntar qué permite terminar el while. |
| 19:20–19:27 | NIV-07. Llenar matriz por filas/columnas con ciclos anidados. |
| 19:27–19:35 | NIV-08. Integración en parejas; intercambiar teclado y verificar cuarto término. |
| 19:35–19:42 | P1-01 a P1-05 en orden. Cargar datos; ubicar país/año; discutir asociación sin calcular aún medias. |
| 19:42–19:47 | P1-06 a P1-10 en orden. Recorrido conceptual breve y selección de 12 filas. |
| 19:47–20:00 | P1-11 a P1-14. Ejecutar selección simple y estratificada, mostrar los otros algoritmos y límites. No comparar eficiencia de grupos artificiales. |
| 20:00–20:15 | Pausa de 15 minutos. |
| 20:15–20:18 | P2-01 y P2-02. Qué entra y sale de una función. |
| 20:18–20:27 | P2-03 a P2-05. Cada pareja anticipa qué hace un extremo y calcula medidas de centro y dispersión. |
| 20:27–20:40 | P2-06 y P2-07. Mostrar histograma y boxplot, comparar intervalos y explicar atípicos sin borrarlos. |
| 20:40–20:48 | P3-01 a P3-04. Definir población didáctica y ejecutar demostración TCL. Distinguir sd de salarios y de medias. |
| 20:48–20:58 | P3-05 a P3-10 en orden. IC de media; cambiar confianza; mostrar cobertura y fórmula de tamaño. Ampliar ejercicios de planificación después. |
| 20:58–21:06 | P3-11 a P3-14. Proporción educativa y referencia. Presentar longitud vs margen, dejar cálculos detallados de planificación como ampliación. |
| 21:06–21:15 | P3-15 a P3-18. Dos grupos, independencia, diferencia e interpretación. El profesor ejecuta y una pareja redacta la conclusión mirando la salida. |
| 21:15–21:25 | Autoevaluación individual, discusión en pareja y respuesta colectiva. Registrar dudas para apoyo posterior. |

El tiempo para todas las láminas es una revisión computacional selectiva, no una clase exhaustiva de inferencia. Las ampliaciones se conservan en orden y no se eliminan del notebook. Si el diagnóstico muestra dificultades, reducir modificaciones autónomas durante la sesión y usar las demostraciones ya preparadas; conservar el horario y asignar la práctica restante para después.

## Preguntas que vale la pena detenerse a escuchar

- NIV-03: ¿por qué no usar if con todo el vector? Esperar que distingan una decisión de una selección por elemento.
- P1-04: ¿qué no mantiene constante este gráfico? Esperar habilidad, experiencia o contexto familiar.
- P1-11: ¿qué representa cada selección? Aclarar inicio aleatorio del sistemático, pesos por estrato y grupos artificiales.
- P2-03: ¿el dato extremo es real? No: es una copia alterada con propósito explícito.
- P3-01: ¿de qué población conocemos sigma? Solo de nuestra distribución empírica didáctica.
- P3-09: ¿el 95% tiene que cumplirse exactamente en 100 repeticiones? No; fluctúa y depende de aproximación.
- P3-18: ¿puede decirse que estudiar causó la diferencia? No.

## Revisión y decisiones

La matriz completa de cobertura y los IDs están al final de la guía y notebook. Las guías y el notebook comparten consignas, soluciones y código generados desde `herramientas/generar_taller.py`. No editar solo una copia: regenerar las salidas tras modificar ese origen. El script `.R` facilita una alternativa en RStudio.

No se publicó ni modificó ningún sitio. No se requirió GitHub para crear el material. La experiencia previa e instalaciones de los alumnos siguen sin confirmarse; comprobarlas antes del taller. El material contiene soluciones abiertas en celdas separadas: durante la actividad detenerse antes de la solución y pedir al estudiante que escriba su intento en una celda nueva.
