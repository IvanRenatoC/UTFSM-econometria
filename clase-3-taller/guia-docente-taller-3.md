# Guía docente · Taller 3

Docente: Iván Canales. Grupo de 8–10 estudiantes. Modalidad: presencial, exclusivamente R.

## Secuencia y ritmo

| Horario | Tema de la cátedra | Láminas y dinámica |
|---|---|---|
| 18:50–19:00 | 1. Asociación y contrafactual | 01: retomar wage1 y la pendiente del taller 2; pedir una interpretación sin lenguaje causal. |
| 19:00–19:20 | 2. Resultados potenciales | 02–03: revelar la tabla artificial, calcular ATE/ATT y cambiar a Juan. |
| 19:20–19:40 | 3. Selección | 04–05: reconstruir 50 = 20 + 30 y discutir el caso de las alarmas. |
| 19:40–20:00 | 4. Aleatorización | 06–07: ejecutar una asignación; mostrar las 200 repeticiones como demostración guiada. |
| 20:00–20:15 | Descanso | 15 minutos. |
| 20:15–20:35 | 5. Variable omitida | 08–09: estimar corta, larga y auxiliar; verificar la identidad. |
| 20:35–20:45 | 6. Signo del sesgo | 10: predecir antes de pulsar cada combinación. |
| 20:45–21:00 | 7. Controles | 11–12: fumar/edad simulados; comparar la nube agregada y las líneas a edad fija. |
| 21:00–21:10 | 8. Variables irrelevantes | 13: mostrar la simulación repetida y discutir dispersión. |
| 21:10–21:25 | Aplicación y conclusiones | 14–16: trabajar en parejas con wage2; interpretar las dos pendientes y cerrar con la autoevaluación. |

No es necesario transcribir todos los ciclos de simulación en esta sesión. Priorizar que los alumnos escriban las diferencias de medias, los tres modelos de omisión y la práctica de wage2. Las repeticiones y las figuras están disponibles para profundizar después. El bloque final reúne todo el código del ejercicio real para evitar demoras en la carga.

## Método

1. Pedir una predicción verbal antes de mostrar el resultado.
2. Escribir la instrucción en Colab con kernel R; abrir el código plegado después del intento.
3. Usar los botones de cada instrucción para explicar su función y argumentos nuevos.
4. Contrastar las salidas de R con la figura; pedir una frase con unidades y una limitación.

Nuevas sentencias: `ifelse`, `rnorm`, `runif`, `as.numeric` sobre una condición, selección con `!`, extracción de coeficientes por nombre, `unname`, `all.equal`, `lines`, `colMeans`, `apply` y `complete.cases`. La fórmula `y ~ x1 + x2` se presenta como control para estudiar la omisión, sin desarrollar la teoría completa de regresión múltiple de la próxima cátedra. `lm`, `summary`, `anova`, `predict`, `aggregate`, `plot` y `abline` retoman el taller 2.

## Límites que hay que conservar

- ATE y ATT se conocen en las simulaciones porque inventamos los contrafactuales; no se observan automáticamente en una base real.
- Aleatorización: comparabilidad en promedio sobre asignaciones; nunca prometer equilibrio perfecto en cada muestra.
- `b_corta = b1 + b2 × delta1` es una identidad entre ajustes con intercepto y la misma muestra. Su interpretación como sesgo causal exige supuestos adicionales.
- El ejemplo fumar/edad usa un índice artificial, no una probabilidad ni evidencia médica.
- IQ es una medida imperfecta. La diferencia entre 60.214 y 42.058 no identifica por sí sola el sesgo causal de educación.
- ANOVA con varios predictores es secuencial: el orden importa. R² y significancia no prueban causalidad.
- Un predictor irrelevante correlacionado puede aumentar la varianza. Un control relevante puede mejorar precisión; no enseñar que todos los controles perjudican.

## Referencias

[Cátedra 3 de Sebastián Azócar](https://hizocar.github.io/econometria-usm/clases/clase3/), consultada el 2 de noviembre de 2026. Se sigue su orden temático; los ejemplos se adaptan para el taller. La tabla de cinco personas y los mecanismos de simulación se identifican expresamente como didácticos. Referencia de lectura: Wooldridge, sección 3.3 y las indicaciones de la cátedra.
