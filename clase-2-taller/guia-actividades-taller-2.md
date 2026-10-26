# Clase 2 · Regresión lineal simple en R

Casos prácticos con wage1 y mtcars: de la nube de puntos al ajuste y su interpretación.

Docente: Iván Canales

Ejecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.

## Agenda

- 18:50–19:00: Datos y entorno
- 19:00–19:15: Tres nubes y modelo con error
- 19:15–19:30: Esperanza y promedios por grupo
- 19:30–20:00: Conocer lm(), aplicarlo y calcular MCO
- 20:00–20:15: Descanso
- 20:15–20:45: Tres regresiones e interpretación
- 20:45–21:05: Residuos, descomposición y R²
- 21:05–21:12: Práctica: descargar y explorar ceosal1
- 21:12–21:20: Práctica: construir e interpretar la regresión
- 21:20–21:25: Código completo y puesta en común

## Parte 1 · Taller · De los datos a mínimos cuadrados

### Cargar datos y reconocer las unidades

Carga wage1 del libro de Wooldridge. Son 526 personas de Estados Unidos, CPS 1976: wage es salario por hora en USD de 1976; educ, años de educación; exper, años de experiencia potencial; numdep, número de dependientes. Cada fila representa una persona, no un período.

```r
# Usa la copia local; si no está, carga la base del paquete.
if (file.exists("datos/wage1.csv")) {
  datos <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  datos <- wooldridge::wage1
}
head(datos)
str(datos)
summary(datos)
```

**Lectura del resultado:** Observa los nombres y rangos antes de modelar. La experiencia es potencial, no necesariamente experiencia laboral efectivamente acumulada. La columna rownames de la copia CSV es un identificador de fila y no se usa como predictor.

### Nube de puntos: salario y educación

Observa la nube de salario y educación. Antes de mostrar la recta, anticipa la dirección de la tendencia. Luego ejecuta los otros gráficos en R para explorar salario frente a experiencia potencial y número de dependientes.

```r
# Salario vs Educación
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9080")

# Otros gráficos:
par(mfrow = c(1, 3))
plot(wage ~ exper, data = datos, pch = 19, col = "#005E9080")
plot(wage ~ numdep, data = datos, pch = 19, col = "#005E9080")
par(mfrow = c(1, 1))
```

**Lectura del resultado:** La nube de salario y educación muestra una tendencia creciente, con dispersión entre personas de un mismo nivel educativo. Recordemos que la recta resume la asociación promedio. La bondad de ajuste es baja: el R² es aproximadamente 16 %, es decir, el modelo explica cerca del 16 % de la variación observada del salario en esta muestra.

### Modelo, error y factores que no observamos

Trabaja con wage = β₀ + β₁ educ + u. Propón factores que podrían integrar u: habilidad, ocupación o condiciones del empleo. Mueve la recta y observa las distancias verticales. El error poblacional u no se observa; los residuos se calculan después de estimar.

```r
x <- datos$educ
y <- datos$wage
plot(x, y, pch = 19, col = "#005E9080",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(a = 0, b = 0.5, col = "#D6A600", lwd = 3)
```

**Lectura del resultado:** La recta dibujada es una propuesta inicial, no una estimación. La linealidad es en los parámetros. E[u | x] = 0 es un supuesto sobre la población: esta nube no permite comprobarlo. Una asociación salarial no basta para concluir causalidad.

### Esperanza y esperanza condicional en los datos

Compara el salario promedio de toda la muestra con el promedio dentro de cada nivel educativo. Son promedios muestrales que aproximan esperanzas; no son la función poblacional conocida.

```r
promedio <- mean(datos$wage)
por_educ <- aggregate(wage ~ educ, data = datos, FUN = mean)
print(promedio)
print(por_educ)
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9040")
points(por_educ$educ, por_educ$wage, pch = 19, col = "#D6A600", cex = 1.4)
abline(h = promedio, lty = 2)
```

**Lectura del resultado:** Cada punto dorado resume personas con el mismo educ; la línea horizontal resume a todas. Los tamaños de los grupos son diferentes. Bajo E[u | educ] = 0, la regresión poblacional es E[wage | educ] = β₀ + β₁ educ.

### Conoce lm(): sintaxis y parámetros

La función nativa de R para ajustar modelos lineales es lm(), abreviatura de Linear Model, del paquete stats. No necesitas indicar todos sus argumentos: para este taller bastan formula y data. Pulsa cada parámetro para explorar su función; los argumentos avanzados se presentan como referencia y no amplían el modelo simple que trabajaremos.

**Firma oficial de lm() — referencia, no ejecutar como llamada completa**

```r
lm(formula,
   data,
   subset,
   weights,
   na.action,
   method = "qr",
   model = TRUE,
   x = FALSE,
   y = FALSE,
   qr = TRUE,
   singular.ok = TRUE,
   contrasts = NULL,
   offset, ...)
```

[Documentación oficial de R](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html)

```r
# Consultar los argumentos oficiales sin ajustar un modelo:
args(stats::lm)

# Ver la configuración actual para valores faltantes:
getOption("na.action")
```

**El código, paso a paso**

**formula · ¿qué queremos explicar?**

Describe el modelo con una fórmula: la respuesta va a la izquierda de ~ y los predictores a la derecha. Por ejemplo, y ~ x. La fórmula incluye intercepto por defecto. En este taller usaremos un solo predictor: regresión lineal simple.

**data · ¿dónde están las variables?**

Indica la tabla que contiene las columnas. Si una variable no aparece allí, R la busca en el entorno de la fórmula, que suele ser desde donde se llama lm(); no necesariamente es siempre el entorno global. Usar data de forma explícita ayuda a evitar confusiones.

**subset · ¿qué filas entran?**

Permite seleccionar observaciones mediante índices o una condición lógica. Por ejemplo, subset = educ >= 12 selecciona esas filas; cambiar la muestra cambia el análisis. Lo dejaremos sin especificar para usar todas las observaciones disponibles del caso.

**weights · ¿todas las filas pesan igual?**

Pesos numéricos opcionales. Si se indican, lm() minimiza la suma de residuos al cuadrado multiplicados por sus pesos: mínimos cuadrados ponderados. Aquí no los indicaremos y utilizaremos mínimos cuadrados ordinarios.

**na.action · ¿qué hacer con NA?**

Controla el tratamiento de valores faltantes. Depende de getOption("na.action"): la configuración inicial habitual de R es na.omit, que excluye filas con NA en las variables utilizadas por el ajuste. Si la opción no está definida, lm() utiliza na.fail. No se eliminan filas por NA en columnas ajenas al modelo.

**method = "qr" · ¿cómo se calcula el ajuste?**

El método habitual de cálculo es la descomposición QR. Es la opción de ajuste admitida por lm(). La alternativa method = "model.frame" devuelve la tabla utilizada por el modelo, sin estimar la regresión. Mantendremos "qr".

**model = TRUE · guardar los datos utilizados**

Conserva dentro del resultado la tabla de variables utilizada por el modelo (model frame), incluidas las transformaciones y la selección de filas que correspondan. No es necesariamente una copia completa del dataset original.

**x = FALSE · guardar la matriz de diseño**

Si x = TRUE, conserva la matriz numérica con la que se estima el ajuste: incluye una columna para el intercepto y las columnas de los predictores. FALSE evita guardar ese componente por separado; no elimina los predictores del modelo.

**y = FALSE · guardar la respuesta**

Si y = TRUE, conserva por separado el vector de respuesta utilizado en el ajuste. El valor FALSE no elimina la respuesta ni impide estimar; sólo controla si se guarda ese componente adicional.

**qr = TRUE · conservar la descomposición**

Guarda la descomposición QR dentro del resultado. Funciones posteriores, como summary() para un ajuste lm ordinario, necesitan este componente. Conviene conservar el valor predeterminado.

**singular.ok = TRUE · columnas redundantes**

Permite continuar si la matriz de diseño tiene columnas perfectamente redundantes. Los coeficientes no identificables aparecen como NA. Con FALSE se produce un error. Esta tolerancia no resuelve el problema de identificación; sólo controla la reacción de R.

**contrasts = NULL · codificar factores**

Permite elegir cómo se representan los factores mediante columnas numéricas en la matriz de diseño. NULL deja la codificación habitual. No es necesario configurarlo para nuestro predictor numérico educ.

**offset · un componente conocido**

Añade al predictor lineal un componente conocido cuyo coeficiente queda fijado en 1, en lugar de estimarse. Puede indicarse como argumento o en la fórmula. No lo necesitamos en la regresión simple del taller.

**... · otros argumentos**

Permite pasar argumentos adicionales a las funciones internas de ajuste. No significa que falte completar algo: puedes omitirlo, igual que los demás argumentos opcionales.

**Lectura del resultado:** La firma muestra los argumentos disponibles, no una llamada que debas ejecutar con todos ellos. TRUE y FALSE controlan qué componentes se conservan; no añaden variables explicativas. En la siguiente lámina aplicaremos lm(wage ~ educ, data = datos).

### Aplicar lm() a wage1: educación y salario

Ahora usa la función con una pregunta concreta: ¿cómo se relacionan los años de educación y el salario por hora? Ajusta con las 526 personas de wage1, interpreta la pendiente y compara las predicciones para 12 y 16 años de educación. Aquí nos concentramos en la aplicación; el resumen estadístico y la ANOVA se revisarán en la lámina 08.

```r
modelo_pos <- lm(wage ~ educ, data = datos)
print(nobs(modelo_pos))
print(coef(modelo_pos))
print(predict(modelo_pos, newdata = data.frame(educ = c(12, 16))))
print(sum(resid(modelo_pos)^2))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)
```

**El código, paso a paso**

**Traducir la pregunta: lm(wage ~ educ, data = datos)**

wage es el salario por hora que queremos explicar; educ es el predictor medido en años. datos contiene ambas columnas. Guardamos el ajuste en modelo_pos para consultarlo después. Dejamos los demás argumentos en sus valores habituales: no seleccionamos filas ni aplicamos pesos.

**Comprobar la muestra: print(nobs(modelo_pos))**

Muestra cuántas observaciones entraron efectivamente al ajuste: 526. Es importante comprobarlo, porque las filas usadas podrían reducirse si hubiera valores faltantes en las variables del modelo.

**Interpretar coeficientes: print(coef(modelo_pos))**

Obtenemos intercepto ≈ −0.905 y pendiente ≈ 0.541. La recta es salario ajustado = −0.905 + 0.541 × años de educación. Un año adicional se asocia con aproximadamente 0.541 USD/h más de salario ajustado. El signo positivo no prueba causalidad.

**Aplicar la recta: print(predict(...))**

newdata crea dos casos con el nombre de columna esperado, educ. Las predicciones para 12 y 16 años son aproximadamente 5.591 y 7.757 USD/h. La diferencia es 4 × 0.541 ≈ 2.165 USD/h. Son valores ajustados, no salarios individuales garantizados.

**Medir lo que falta explicar: print(sum(resid(modelo_pos)^2))**

resid() calcula salario observado menos ajustado, ^2 eleva cada diferencia al cuadrado y sum() las suma. El resultado SSR ≈ 5980.682 es el mínimo de esta suma para una recta con intercepto en esta muestra; no es un promedio ni un porcentaje.

**Contrastar con la nube: plot(...) y abline(...)**

La nube conserva los salarios observados. La línea dorada es el ajuste calculado por lm(), cuyos coeficientes no se modifican aquí. Observa la dispersión alrededor de la recta: personas con los mismos años de educación pueden ganar salarios distintos.

**Lectura del resultado:** MCO minimiza SSR = Σ(yᵢ − ŷᵢ)². El ajuste observado es aproximadamente ŷ = −0.905 + 0.541 educ. Un año adicional de educación se asocia con 0.541 USD/h más, en promedio. El intercepto no debe interpretarse fuera del contexto y soporte de los datos.

### De la fórmula a lm(): regresión muestral

Calcula los parámetros con vectores y compara con lm(). Esta es una estimación en la muestra, no los parámetros poblacionales conocidos.

```r
x <- datos$educ
y <- datos$wage
b1 <- sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x))^2)
b0 <- mean(y) - b1 * mean(x)
print(c(b0 = b0, b1 = b1))
print(coef(modelo_pos))
y_ajustado <- b0 + b1 * x
residuos <- y - y_ajustado
print(head(data.frame(y, y_ajustado, residuos)))
```

**El código, paso a paso**

**x <- datos$educ; y <- datos$wage**

Extraemos dos columnas del dataset y las guardamos como vectores: x contiene los años de educación e y, el salario por hora. Las posiciones coinciden: x[i] e y[i] corresponden a la misma persona. La flecha <- asigna los valores a un nombre.

**b1 <- sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x))^2)**

Calculamos la pendiente de mínimos cuadrados. mean(x) y mean(y) son los promedios. Al restarlos obtenemos cuánto se aleja cada observación de su promedio. El numerador multiplica esas diferencias persona por persona y las suma: resume cómo varían juntas educación y salario. El denominador suma las diferencias de educación al cuadrado: mide la variación de x y debe ser mayor que cero. Dividir ambos resultados produce b1 ≈ 0.541: por cada año adicional de educación, el salario ajustado aumenta aproximadamente 0.541 USD por hora.

**b0 <- mean(y) - b1 * mean(x)**

Calculamos el intercepto: al salario promedio le restamos la pendiente multiplicada por la educación promedio. Obtenemos b0 ≈ −0.905. Esta elección hace que la recta pase por el punto de los promedios (x̄, ȳ). No significa que exista un salario negativo observado.

**print(c(b0 = b0, b1 = b1))**

c() reúne los dos resultados en un vector con nombres. print() muestra el intercepto y la pendiente calculados con la fórmula. Los nombres b0 y b1 permiten distinguirlos en la salida.

**print(coef(modelo_pos))**

coef() extrae los coeficientes que lm() calculó en la lámina anterior. print() los muestra con los nombres (Intercept) y educ. Deben coincidir con b0 y b1, salvo diferencias mínimas de precisión numérica: estamos aplicando el mismo método. Primero debes ejecutar la celda que crea modelo_pos.

**y_ajustado <- b0 + b1 * x**

Aplicamos la ecuación de la recta a cada persona. R multiplica cada valor de x por b1 y le suma b0; así construye un vector de salarios ajustados. Por ejemplo, con 12 años de educación se obtiene aproximadamente 5.591 USD por hora. Es un valor sobre la recta, no el salario exacto que cada persona debe recibir.

**residuos <- y - y_ajustado**

Restamos, persona por persona, salario observado menos salario ajustado. Un residuo positivo indica que la persona gana más de lo que ajusta el modelo; uno negativo indica que gana menos. Este residuo calculado en la muestra se distingue del error poblacional u, que no observamos.

**print(head(data.frame(y, y_ajustado, residuos)))**

data.frame() coloca los tres vectores como columnas de una tabla; head() selecciona las primeras seis filas y print() las muestra. Compara cada salario real con su ajuste y verifica la resta. En la primera fila: 3.10 − 5.050 ≈ −1.950 USD por hora.

**Lectura del resultado:** Los dos métodos coinciden salvo redondeo numérico. La recta pasa por (x̄, ȳ). No confundas β₁ poblacional con b₁ estimado.

## Parte 2 · Taller · Tres casos, diagnóstico y comparación

### Caso positivo: educación y salario

Consulta summary(modelo_pos) y anova(modelo_pos). Despliega cada salida e interpreta sus componentes con los botones. El modelo explica salario por hora a partir de educación. Predice para 12 y 16 años: ¿es un salario individual garantizado?

```r
modelo_pos <- lm(wage ~ educ, data = datos)
print(summary(modelo_pos))
print(anova(modelo_pos))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)
predict(modelo_pos, newdata = data.frame(educ = c(12, 16)))
```

**ANOVA · Salario y educación · wage ~ educ · n = 526**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Regresión · SSE = Σ(ŷᵢ − ȳ)² | 1179.732 | 1 | 1179.732 | 103.363 | 2.78e-22 |
| Error · SSR = Σ(yᵢ − ŷᵢ)² | 5980.682 | 524 | 11.414 | — | — |
| Total · SST = Σ(yᵢ − ȳ)² | 7160.414 | 525 | — | — | — |

Con intercepto: SST = SSE + SSR. Cuadrado medio = suma de cuadrados / grados de libertad; F = CM de regresión / CM del error. Las siglas siguen la cátedra: SSE explicada, SSR residual. En otras fuentes se intercambian; identifica siempre qué suma representa cada fila. La fila Total es una adición didáctica a la salida de anova() de R. Valores redondeados.

**Resultados de referencia calculados en R**

**Ver summary(modelo_pos)**

```text
Call:
lm(formula = wage ~ educ, data = datos)

Residuals:
    Min      1Q  Median      3Q     Max
-5.3396 -2.1501 -0.9674  1.1921 16.6085

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) -0.90485    0.68497  -1.321    0.187
educ         0.54136    0.05325  10.167   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 3.378 on 524 degrees of freedom
Multiple R-squared:  0.1648,	Adjusted R-squared:  0.1632
F-statistic: 103.4 on 1 and 524 DF,  p-value: < 2.2e-16
```

**Ver anova(modelo_pos)**

```text
Analysis of Variance Table

Response: wage
           Df Sum Sq Mean Sq F value    Pr(>F)
educ        1 1179.7 1179.73  103.36 < 2.2e-16 ***
Residuals 524 5980.7   11.41
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

**El código, paso a paso**

**summary · Estimate: intercepto y pendiente**

Estimate contiene los coeficientes: intercepto ≈ −0.905 y pendiente de educ ≈ 0.541. Un año adicional de educación se asocia con 0.541 USD/h más de salario ajustado. El intercepto es la altura de la recta cuando educ = 0; no es un salario observado negativo.

**summary · Std. Error, t value y Pr(>|t|)**

El error estándar mide la incertidumbre del coeficiente estimado. Para educ es ≈ 0.05325; t = 0.54136/0.05325 ≈ 10.167. Su p-valor ≈ 2.78 × 10⁻²² contrasta H₀: β₁ = 0 bajo los supuestos clásicos. No es la probabilidad de que H₀ sea verdadera ni una medida del tamaño del efecto.

**summary · Residual standard error y R²**

El error estándar residual es ≈ 3.378 USD/h: raíz de SSR/(n−2). R² ≈ 0.1648 indica que la recta explica aproximadamente el 16.48 % de la variación salarial en esta muestra; el R² ajustado es ≈ 0.1632. Una pendiente significativa puede coexistir con baja capacidad explicativa.

**ANOVA · Df: grados de libertad**

La fila educ tiene 1 grado de libertad porque incorporamos una pendiente. Residuals tiene 524 = 526 − 2: estimamos intercepto y pendiente. Los grados de libertad totales son 525 = n − 1.

**ANOVA · Sum Sq: variación explicada y residual**

En la fila educ, Sum Sq ≈ 1179.732 es la suma explicada SSE. En Residuals, Sum Sq ≈ 5980.682 es la suma residual SSR. Ambas suman SST ≈ 7160.414. R² = 1179.732/7160.414 ≈ 0.1648. Seguimos la notación de la cátedra.

**ANOVA · Mean Sq, F value y Pr(>F)**

Mean Sq divide Sum Sq por Df: 1179.732/1 ≈ 1179.732 y 5980.682/524 ≈ 11.4135. F divide ambos cuadrados medios: ≈ 103.36. Pr(>F) es el p-valor del contraste global contra un modelo con sólo intercepto. En esta regresión simple, contrasta β₁ = 0; F = t² y su p-valor coincide con el de la pendiente.

**Predicciones y límites de interpretación**

Para educ = 12 y 16, predict() entrega aproximadamente 5.591 y 7.757 USD/h. Son puntos sobre la recta. Ni la ANOVA ni el p-valor prueban que estudiar cause un cambio salarial; la interpretación inferencial requiere supuestos sobre el error y la muestra.

**Lectura del resultado:** La pendiente es aproximadamente 0.541. Las predicciones son valores medios ajustados, no salarios individuales garantizados. Factores omitidos pueden estar relacionados con educación.

### Tiempo de aceleración: casos negativo y no significativo

Usaremos mtcars, 32 automóviles de modelos 1973–1974, con datos publicados por Motor Trend en 1974. La respuesta es qsec: segundos para recorrer un cuarto de milla (aproximadamente 402 m). hp es potencia bruta en caballos de fuerza; drat es la relación de transmisión del eje trasero, sin unidades. Alterna entre ambos predictores y anticipa el signo. La base viene incluida en R: no necesitas instalar paquetes.

```r
autos <- datasets::mtcars
head(autos[, c("qsec", "hp", "drat")])

# Caso negativo: potencia y tiempo de aceleración
modelo_neg <- lm(qsec ~ hp, data = autos)
print(summary(modelo_neg))
print(anova(modelo_neg))

# Caso no significativo: relación de transmisión y tiempo
modelo_plano <- lm(qsec ~ drat, data = autos)
print(summary(modelo_plano))
print(anova(modelo_plano))

par(mfrow = c(1, 2))
plot(qsec ~ hp, data = autos, pch = 19, col = "#005E9080",
     xlab = "Potencia bruta (hp)", ylab = "Tiempo de 1/4 de milla (s)")
abline(modelo_neg, col = "#D6A600", lwd = 3)
plot(qsec ~ drat, data = autos, pch = 19, col = "#005E9080",
     xlab = "Relación de transmisión (sin unidades)",
     ylab = "Tiempo de 1/4 de milla (s)")
abline(modelo_plano, col = "#D6A600", lwd = 3)
par(mfrow = c(1, 1))
```

**ANOVA · Potencia y tiempo · qsec ~ hp · n = 32**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Regresión · SSE = Σ(ŷᵢ − ȳ)² | 49.651 | 1 | 49.651 | 30.190 | 5.77e-06 |
| Error · SSR = Σ(yᵢ − ŷᵢ)² | 49.338 | 30 | 1.645 | — | — |
| Total · SST = Σ(yᵢ − ȳ)² | 98.988 | 31 | — | — | — |

**ANOVA · Transmisión y tiempo · qsec ~ drat · n = 32**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Regresión · SSE = Σ(ŷᵢ − ȳ)² | 0.823 | 1 | 0.823 | 0.252 | 0.62 |
| Error · SSR = Σ(yᵢ − ŷᵢ)² | 98.165 | 30 | 3.272 | — | — |
| Total · SST = Σ(yᵢ − ȳ)² | 98.988 | 31 | — | — | — |

Con intercepto: SST = SSE + SSR. Cuadrado medio = suma de cuadrados / grados de libertad; F = CM de regresión / CM del error. Las siglas siguen la cátedra: SSE explicada, SSR residual. En otras fuentes se intercambian; identifica siempre qué suma representa cada fila. La fila Total es una adición didáctica a la salida de anova() de R. Valores redondeados.

**El código, paso a paso**

**Potencia: ¿por qué una pendiente negativa?**

Menos segundos significa completar antes la distancia. Por eso una mayor potencia asociada con un menor tiempo produce una pendiente negativa. Diez hp adicionales se asocian con unos 0.185 segundos menos en el ajuste simple. No estamos comparando el mismo automóvil con y sin una intervención.

**Relación de transmisión: ¿qué significa “neutro”?**

drat describe la relación del eje trasero, no la velocidad medida ni la potencia. Su pendiente es pequeña respecto de su error estándar (0.3048 frente a 0.6076). Con p ≈ 0.62 no hay evidencia suficiente contra β₁ = 0 al 5 %. Esta muestra pequeña no demuestra ausencia de efecto mecánico ni independencia.

**Leer las dos tablas ANOVA**

Potencia: F ≈ 30.190 y p ≈ 0.00000577; rechazamos pendiente cero al 5 % bajo los supuestos clásicos. Transmisión: F ≈ 0.252 y p ≈ 0.620; no rechazamos pendiente cero. Ambos modelos usan los mismos 32 tiempos, por eso comparten SST y 31 grados de libertad totales. La regresión de potencia explica una fracción mucho mayor de esa variación.

**Lectura del resultado:** Con hp, la pendiente es aproximadamente −0.01846 segundos por hp (R² ≈ 0.5016; p ≈ 0.00000577): los autos más potentes tienden a completar la distancia en menos tiempo. Con drat, la pendiente es ≈ 0.3048 segundos por unidad (R² ≈ 0.0083; p ≈ 0.6196): no rechazamos pendiente poblacional cero al 5 %. Este segundo caso es el ejemplo “neutro” en sentido de falta de evidencia lineal, no de pendiente exactamente cero. Son asociaciones entre automóviles distintos; peso, diseño y otras diferencias impiden una conclusión causal.

### Comprobar el caso no significativo con un intervalo

Continúa con mtcars y el modelo qsec ~ drat de la lámina 09. Obtén el intervalo de confianza de la pendiente y compáralo con el p-valor. ¿Incluye el cero? ¿Qué valores positivos y negativos siguen siendo compatibles con estos datos?

```r
# Ejecuta primero la lámina 09 para crear autos y modelo_plano.
print(summary(modelo_plano))
print(anova(modelo_plano))
print(confint(modelo_plano, "drat", level = 0.95))
plot(qsec ~ drat, data = autos, pch = 19, col = "#005E9060",
     xlab = "Relación de transmisión (sin unidades)",
     ylab = "Tiempo de 1/4 de milla (s)")
abline(modelo_plano, col = "#D6A600", lwd = 3)
```

**ANOVA · Caso no significativo · qsec ~ drat · n = 32**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Regresión · SSE = Σ(ŷᵢ − ȳ)² | 0.823 | 1 | 0.823 | 0.252 | 0.62 |
| Error · SSR = Σ(yᵢ − ŷᵢ)² | 98.165 | 30 | 3.272 | — | — |
| Total · SST = Σ(yᵢ − ȳ)² | 98.988 | 31 | — | — | — |

Con intercepto: SST = SSE + SSR. Cuadrado medio = suma de cuadrados / grados de libertad; F = CM de regresión / CM del error. Las siglas siguen la cátedra: SSE explicada, SSR residual. En otras fuentes se intercambian; identifica siempre qué suma representa cada fila. La fila Total es una adición didáctica a la salida de anova() de R. Valores redondeados.

**El código, paso a paso**

**ANOVA e intervalo: dos lecturas del mismo contraste**

La tabla da F ≈ 0.252 con 1 y 30 grados de libertad y p ≈ 0.620. En una regresión simple con intercepto, F = t². El intervalo del 95 % de la pendiente incluye cero, coherente con no rechazar β₁ = 0 al 5 %. Ninguno de estos resultados prueba que la pendiente sea exactamente cero.

**Lectura del resultado:** El intervalo del 95 % para la pendiente es aproximadamente [−0.936, 1.546] segundos por unidad de drat. Incluye cero, en concordancia con p ≈ 0.620. La pendiente estimada es positiva, pero no significativa al 5 %. El intervalo también incluye asociaciones de magnitudes relevantes: no podemos concluir equivalencia a cero. Se aplica la inferencia clásica de lm(), condicionada a sus supuestos.

### Residuos y propiedades del ajuste

Activa la animación para dibujar las distancias verticales de los datos a su recta. Comprueba las propiedades algebraicas de MCO con intercepto.

```r
modelo <- modelo_pos
x <- datos$educ
y <- datos$wage
ajuste <- fitted(modelo)
e <- resid(modelo)
print(c(suma_residuos = sum(e), suma_x_residuos = sum(x * e),
        media_y = mean(y), media_ajustada = mean(ajuste)))
plot(x, y, pch = 19, col = "#005E9060")
segments(x, ajuste, x, y, col = "#D6A60060")
abline(modelo, col = "#D6A600", lwd = 3)
```

**Lectura del resultado:** Las sumas son prácticamente cero por redondeo de la computadora. Son propiedades del ajuste, no una prueba de E[u | x] = 0 ni del cumplimiento de los supuestos.

### SST, SSE, SSR y R²: ¿cuánto explica la recta?

Compara los tres casos con la misma definición que la cátedra: SST total, SSE explicada y SSR residual. En MCO con intercepto, SST = SSE + SSR.

```r
modelos <- list(positivo = modelo_pos, negativo = modelo_neg, plano = modelo_plano)
resumen <- do.call(rbind, lapply(modelos, function(m) {
  y <- model.response(model.frame(m))
  SST <- sum((y - mean(y))^2)
  SSE <- sum((fitted(m) - mean(y))^2)
  SSR <- sum(resid(m)^2)
  c(SST = SST, SSE = SSE, SSR = SSR, R2 = 1 - SSR / SST)
}))
print(resumen)
barplot(t(cbind(resumen[, "R2"], 1 - resumen[, "R2"])),
        col = c("#D6A600", "#005E90"),
        legend.text = c("Explicada", "Residual"),
        names.arg = rownames(resumen), ylab = "Fracción de SST")
```

**Lectura del resultado:** R² = SSE/SST = 1 − SSR/SST. El ajuste salarial explica cerca del 16.48 %; potencia y tiempo, 50.16 %; transmisión y tiempo, 0.83 %. Salario y tiempo son respuestas con unidades y muestras diferentes: compara las fracciones explicadas, no sus SST brutas. El R² no demuestra causalidad.

### Práctica 1 · Preparar una nueva base de Wooldridge

21:05–21:12 · En Colab, selecciona R como tipo de entorno. Copia y ejecuta primero el bloque de carga: descarga el paquete del libro desde CRAN si hace falta y deja ceosal1 lista en datos_practica. Después ejecuta las soluciones de exploración y gráfico. Pregunta: ¿las empresas con mayor rentabilidad del patrimonio pagan salarios más altos a sus directores ejecutivos? Al terminar la exploración, ejecuta el ejercicio 4: crea fit y consulta tanto summary(fit) como anova(fit).

```r
# Colab: selecciona R como tipo de entorno y ejecuta esta celda.
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos_practica <- wooldridge::ceosal1
```

**Ejercicio 2 · Explorar la base y revisar faltantes**

```r
print(head(datos_practica))
str(datos_practica)
print(summary(datos_practica[, c("salary", "roe")]))
print(colSums(is.na(datos_practica[, c("salary", "roe")])))
print(nrow(datos_practica))
```

Hay 209 filas y no hay NA en salary ni roe. salary se mide en miles de USD y roe, en porcentaje.

**Ejercicio 3 · Dibujar la nube de puntos**

```r
plot(salary ~ roe, data = datos_practica, pch = 19, col = "#005E9080",
     xlab = "Rentabilidad del patrimonio: roe (%)",
     ylab = "Salario del director ejecutivo (miles de USD, 1990)",
     main = "Rentabilidad y salario del director ejecutivo")
```

La respuesta salary va en el eje vertical; roe, en el horizontal. Observa dispersión y salarios extremos antes de ajustar.

**Ejercicio 4 · Primer ajuste: fit, summary y ANOVA**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja.

**El código, paso a paso**

**Tu tarea · Conseguir y reconocer los datos**

Usen install.packages("wooldridge", repos = "https://cloud.r-project.org/") si el paquete no está disponible; después carguen wooldridge::ceosal1 en datos_practica. Examinen head(), str() y summary(). No cambien la base datos usada anteriormente en el taller.

**Tu tarea · Definir respuesta y predictor**

Escriban en Markdown qué variable quieren explicar y con cuál la relacionarán. Identifiquen las unidades y revisen cuántas filas tienen NA en salary o roe. Indiquen cuántas observaciones podrán usar.

**Tu tarea · Predecir antes de ajustar**

Dibujen salary en el eje vertical y roe en el horizontal. Antes de agregar una recta, propongan el signo de la pendiente. ¿La nube es estrecha o dispersa? ¿Hay salarios muy alejados del resto? No eliminen observaciones sólo porque sean extremas.

**Lectura del resultado:** La base contiene 209 observaciones y 12 variables, a partir de datos publicados por Businessweek en 1991. salary es el salario de 1990 en miles de dólares; roe es la rentabilidad del patrimonio promedio de 1988–1990, expresada en porcentaje. Cada fila vincula a un director ejecutivo con su empresa. No son mediciones sucesivas de una sola persona.

### Práctica 2 · Estimar e interpretar su propia regresión

21:12–21:20 · Ejecuta primero la carga de datos de la lámina 13. Cada solución crea explícitamente fit con lm(), consulta summary(fit) y anova(fit), y luego resuelve la tarea. Así cada bloque utiliza un ajuste identificado y no depende de haber creado el modelo en otro ejercicio. Todos requieren datos_practica cargado.

**Ejercicio 1 · Estimar la regresión y obtener coeficientes**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)

# Aplicar el resultado al ejercicio.
print(nobs(fit))
print(coef(fit))
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. En este ejercicio: Se usan 209 observaciones. Salario ajustado ≈ 963.191 + 18.501 × roe, en miles de USD. Un punto porcentual adicional se asocia con 18.501 miles de USD más de salario ajustado.

**Ejercicio 2 · Obtener summary y ANOVA**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. En este ejercicio: R² ≈ 0.0132 y p ≈ 0.0978. La pendiente estimada es positiva, pero no significativa al 5 %. Se explica cerca de 1.32 % de la variación salarial.

**Ejercicio 3 · Predecir para roe de 10 % y 20 %**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)

# Aplicar el resultado al ejercicio.
nuevos_casos <- data.frame(roe = c(10, 20))
print(data.frame(nuevos_casos,
                 salario_ajustado = predict(fit, nuevos_casos)))
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. En este ejercicio: Los valores ajustados son aproximadamente 1148.203 y 1333.215 miles de USD, respectivamente; no son salarios individuales garantizados.

**Ejercicio 4 · Descomponer la variación y agregar la recta**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)

# Aplicar el resultado al ejercicio.
y_practica <- model.response(model.frame(fit))
ajustados_practica <- fitted(fit)
residuos_practica <- resid(fit)
SST_practica <- sum((y_practica - mean(y_practica))^2)
SSE_practica <- sum((ajustados_practica - mean(y_practica))^2)
SSR_practica <- sum(residuos_practica^2)
print(c(SST = SST_practica, SSE = SSE_practica, SSR = SSR_practica,
        R2 = 1 - SSR_practica / SST_practica))
print(all.equal(SST_practica, SSE_practica + SSR_practica))


plot(salary ~ roe, data = datos_practica, pch = 19, col = "#005E9080",
     xlab = "Rentabilidad del patrimonio: roe (%)",
     ylab = "Salario del director ejecutivo (miles de USD, 1990)",
     main = "Rentabilidad y salario del director ejecutivo")
abline(fit, col = "#D6A600", lwd = 3)
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. En este ejercicio: all.equal() devuelve TRUE: SST ≈ SSE + SSR. La recta resume una asociación de baja capacidad explicativa. No demuestra causalidad.

**Ejercicio 5 · Redactar una conclusión en R**

```r
# 1. Ajustar y guardar el modelo con el nombre fit.
fit <- lm(salary ~ roe, data = datos_practica)

# 2. Ver coeficientes, incertidumbre y bondad de ajuste.
summary(fit)

# 3. Ver la tabla ANOVA del mismo modelo.
anova(fit)

# Aplicar el resultado al ejercicio.
cat("La asociación estimada es positiva: 18.501 miles de USD por punto porcentual de roe.\n")
cat("El ajuste es bajo (R2 ≈ 1.32 %) y la pendiente no es significativa al 5 % (p ≈ 0.0978).\n")
cat("Estos datos observacionales no permiten concluir que aumentar roe cause un aumento salarial.\n")
```

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. En este ejercicio: Usa esta redacción como referencia y escribe tu propia explicación en una celda Markdown.

**El código, paso a paso**

**Reto 1 · Ajustar y escribir la ecuación**

Usen lm() y guarden el resultado en modelo_practica. Extraigan los coeficientes con coef(). Escriban la ecuación de salario ajustado en función de roe. ¿Qué significa aumentar roe en un punto porcentual? ¿Cuánto cambia el ajuste si aumenta diez puntos porcentuales?

**Reto 2 · Leer summary() y ANOVA**

Obtengan summary() y anova(). Identifiquen pendiente, error estándar, p-valor y R². Apliquen el umbral del 5 %: ¿pueden rechazar pendiente poblacional cero? ¿Es lo mismo una pendiente positiva que una pendiente significativa?

**Reto 3 · Predecir y explicar**

Con predict(), calculen los salarios ajustados para roe = 10 y roe = 20. El nombre de la columna de newdata debe coincidir con el predictor. Recuerden expresar el resultado en miles de dólares y distinguir valor ajustado de salario individual garantizado.

**Reto 4 · Comprobar y comunicar**

Calculen SST, SSE y SSR según la convención de la cátedra y verifiquen SST ≈ SSE + SSR. Agreguen la recta a la nube. Escriban una conclusión de tres frases: dirección de la asociación, capacidad explicativa y limitación de interpretación.

**Lectura del resultado:** Entregable de la pareja: un gráfico con su recta, la ecuación estimada, una interpretación de la pendiente con unidades, la lectura de R² y p-valor, dos predicciones y una limitación. La base es observacional; una asociación no demuestra causalidad.

### Práctica 3 · Código completo y explicación de la solución

21:20–21:25 · Si prefieres ejecutar todo de una vez en Colab, copia este único bloque completo. Incluye instalación y carga, exploración, gráfico, regresión, resumen, ANOVA, predicciones y comprobación de las sumas de cuadrados. No requiere subir archivos CSV. El modelo se guarda como fit: las consultas summary(fit) y anova(fit) se refieren al mismo ajuste.

```r
# 1. Descargar el paquete del libro y cargar ceosal1.
# Colab: selecciona R como tipo de entorno y ejecuta esta celda.
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos_practica <- wooldridge::ceosal1

# 2. Explorar y comprobar faltantes en las dos variables del modelo.
print(head(datos_practica))
str(datos_practica)
print(summary(datos_practica[, c("salary", "roe")]))
print(colSums(is.na(datos_practica[, c("salary", "roe")])))

# 3. Dibujar la nube: salary está en miles de dólares; roe, en porcentaje.
plot(salary ~ roe, data = datos_practica, pch = 19, col = "#005E9080",
     xlab = "Rentabilidad del patrimonio: roe (%)",
     ylab = "Salario del director ejecutivo (miles de USD, 1990)",
     main = "Rentabilidad y salario del director ejecutivo")

# 4. Estimar la regresión y consultar coeficientes, resumen y ANOVA.
fit <- lm(salary ~ roe, data = datos_practica)
print(nobs(fit))
print(coef(fit))
summary(fit)
anova(fit)
abline(fit, col = "#D6A600", lwd = 3)

# 5. Predecir para dos empresas hipotéticas; resultados en miles de USD.
nuevos_casos <- data.frame(roe = c(10, 20))
print(data.frame(nuevos_casos,
                 salario_ajustado = predict(fit, nuevos_casos)))

# 6. Descomponer la variación usando las filas efectivas del modelo.
y_practica <- model.response(model.frame(fit))
ajustados_practica <- fitted(fit)
residuos_practica <- resid(fit)
SST_practica <- sum((y_practica - mean(y_practica))^2)
SSE_practica <- sum((ajustados_practica - mean(y_practica))^2)
SSR_practica <- sum(residuos_practica^2)
print(c(SST = SST_practica, SSE = SSE_practica, SSR = SSR_practica,
        R2 = 1 - SSR_practica / SST_practica))
print(all.equal(SST_practica, SSE_practica + SSR_practica))

# 7. En una celda Markdown, escribe tu interpretación con unidades.
# Distingue signo, significancia, R2 y asociación frente a causalidad.
```

**El código, paso a paso**

**Paso 1 · Obtener datos sin sobrescribir el trabajo anterior**

Instala wooldridge desde CRAN sólo si el paquete no está disponible y carga ceosal1 con el nombre datos_practica. La instalación inicial necesita conexión. No hace falta buscar ni subir un archivo CSV a Colab.

**Paso 2 · Revisar antes de modelar**

head() muestra las primeras filas; str(), los tipos de columnas; summary(), un resumen de salary y roe. is.na() identifica faltantes y colSums() cuenta cuántos hay por variable. En esta base ambas columnas están completas.

**Paso 3 · Mirar las observaciones**

La fórmula salary ~ roe coloca el salario en el eje vertical. Los títulos conservan las unidades. La nube ayuda a anticipar la tendencia y detectar dispersión y observaciones extremas antes de leer una prueba estadística.

**Paso 4 · fit <- lm(...), summary(fit) y anova(fit)**

lm() estima salary ~ roe y guarda el resultado en fit; summary(fit) resume ese ajuste: intercepto ≈ 963.191, pendiente ≈ 18.501, error estándar de la pendiente ≈ 11.12, p ≈ 0.0978 y R² ≈ 0.0132. anova(fit) muestra los grados de libertad (1 y 207), las sumas de cuadrados, los cuadrados medios y F ≈ 2.767, con el mismo p-valor de la pendiente porque hay un solo predictor. La pendiente es positiva, pero no significativa al 5 %; la capacidad explicativa es baja. nobs(fit) comprueba el tamaño utilizado, coef(fit) extrae los coeficientes y abline(fit) añade la recta a la nube.

**Paso 5 · Predecir en las mismas unidades**

data.frame(roe = c(10, 20)) contiene dos casos con el nombre esperado por el modelo. predict() entrega valores sobre la recta, en miles de dólares. La diferencia entre los ajustes es diez veces la pendiente: aproximadamente 185.012 miles de USD.

**Paso 6 · Verificar las sumas de cuadrados**

Se usan las filas efectivas de model.frame(). SST mide variación total; SSE, variación de los ajustes respecto al promedio; SSR, variación residual. all.equal() comprueba la igualdad con tolerancia numérica. No necesitamos que una igualdad de decimales sea exacta bit por bit.

**Paso 7 · Redactar una conclusión**

Relaciona la pendiente con sus unidades, indica que la capacidad explicativa es baja y distingue no rechazar β₁ = 0 de demostrar β₁ = 0. Reconoce factores omitidos, la naturaleza observacional y el alcance histórico de la base.

**Lectura del resultado:** Resultados de control: 209 observaciones; salario ajustado ≈ 963.191 + 18.501 × roe, en miles de USD. Un punto porcentual adicional de roe se asocia con 18.501 miles de USD más de salario ajustado. R² ≈ 0.0132 (1.32 %) y p ≈ 0.0978: al 5 % no rechazamos pendiente cero. Para roe de 10 % y 20 %, los ajustes son aproximadamente 1148.203 y 1333.215 miles de USD. La pendiente positiva no implica un buen ajuste ni demuestra causalidad. Los salarios extremos merecen revisión; no los borramos automáticamente.
