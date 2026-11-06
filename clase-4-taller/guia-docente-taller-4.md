# Clase 4 · Regresión lineal múltiple en R

Ejecuta en orden con kernel R. En Google Colab selecciona R como tipo de entorno. No uses rpy2 ni %%R.

[Clase teórica de referencia](https://hizocar.github.io/econometria-usm/clases/clase4/)

## Agenda

| Horario | Actividad |
|---|---|
| 18:50–19:10 | Del modelo simple al múltiple |
| 19:10–19:25 | MCO con dos regresores |
| 19:25–19:45 | Notación y operaciones matriciales |
| 19:45–20:00 | Fórmula de MCO y propiedades |
| 20:00–20:15 | Descanso |
| 20:15–20:35 | R² y R² ajustado |
| 20:35–20:55 | Ejemplo y lectura de resultados |
| 20:55–21:20 | Inversa por cofactores |
| 21:20–21:25 | Síntesis y cierre |

## 01 · Preparar wage2 y reconocer las unidades

Comenzamos con datos reales de salarios, educación e IQ. La copia local permite trabajar sin conexión; en Colab se carga el paquete cuando no está el CSV.

### El código, paso a paso

**`complete.cases(original[variables])`**

Devuelve TRUE en las filas sin faltantes en las tres variables seleccionadas. El mismo conjunto de personas se usará en las regresiones que comparemos.

**`original[filas, columnas]`**

Selecciona filas y columnas de un data frame. variables contiene los nombres que queremos conservar.

**`str() y summary()`**

str(datos) describe la estructura; summary(datos) resume cada columna. No ajustan una regresión.

```r
if (file.exists("datos/wage2.csv")) {
  original <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  original <- as.data.frame(wooldridge::wage2)
}
variables <- c("wage", "educ", "IQ")
print(colSums(is.na(original[variables])))
datos <- original[complete.cases(original[variables]), variables]
print(c(filas_originales = nrow(original), filas_usadas = nrow(datos)))
str(datos)
summary(datos)
head(datos)
```

### Cómo leer el resultado

wage es salario mensual en dólares; educ son años de educación; IQ es una puntuación de inteligencia. wage2 contiene 935 hombres trabajadores de Estados Unidos en 1980. Cada fila es una persona. Se informa el número de filas para comparar modelos sobre la misma muestra.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
wage educ   IQ
   0    0    0
filas_originales     filas_usadas
             935              935
'data.frame':	935 obs. of  3 variables:
 $ wage: int  769 808 825 650 562 1400 600 1081 1154 1000 ...
 $ educ: int  12 18 14 12 11 16 10 18 15 12 ...
 $ IQ  : int  93 119 108 96 74 116 91 114 111 95 ...
  wage educ  IQ
1  769   12  93
2  808   18 119
3  825   14 108
4  650   12  96
5  562   11  74
6 1400   16 116
```

</details>

### Comprueba lo aprendido

¿La columna IQ es un porcentaje?

<details><summary>Mostrar respuesta</summary>

No: es una puntuación. Un punto de IQ y un año de educación son unidades diferentes.

</details>

## 02 · Del modelo simple al múltiple

Compara la pendiente de educación antes y después de incluir IQ. El signo + en una fórmula añade una variable explicativa; no suma sus columnas previamente.

$$\widehat{wage}=\widehat\beta_0+\widehat\beta_1\,educ+\widehat\beta_2\,IQ$$

### El código, paso a paso

**`lm(wage ~ educ + IQ, data = datos)`**

Estima intercepto y dos pendientes. La variable dependiente está a la izquierda de ~.

**`coef(multiple)["educ"]`**

Extrae por su nombre la pendiente de educación del modelo múltiple.

**`data.frame(modelo = ..., pendiente_educ = ...)`**

Organiza los coeficientes en una tabla para comparar las mismas unidades.

```r
simple <- lm(wage ~ educ, data = datos)
multiple <- lm(wage ~ educ + IQ, data = datos)
print(coef(simple))
print(coef(multiple))
comparacion <- data.frame(
  modelo = c("Simple", "Con IQ"),
  pendiente_educ = c(coef(simple)["educ"], coef(multiple)["educ"])
)
print(comparacion)
plot(wage ~ educ, data = datos, pch = 19, col = "#005F9640")
abline(simple, col = "#D6A600", lwd = 3)
```

### Cómo leer el resultado

Al incluir IQ cambia la asociación estimada de educación con salario. La pendiente múltiple se interpreta manteniendo IQ fijo. Ninguna de las dos regresiones demuestra por sí sola un efecto causal.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
(Intercept)        educ
  146.95244    60.21428
(Intercept)        educ          IQ
-128.889881   42.057619    5.137958
  modelo pendiente_educ
1 Simple       60.21428
2 Con IQ       42.05762
```

</details>

### Comprueba lo aprendido

¿Agregar un control siempre reduce la pendiente de educación?

<details><summary>Mostrar respuesta</summary>

No. Aquí cambia según la relación entre las variables. Puede aumentar, disminuir o mantener su valor.

</details>

## 03 · Ceteris paribus: mover educación y dejar IQ fijo

Usa los controles para comparar salarios predichos a un IQ fijo. Después cambia IQ: se desplaza la recta condicional, pero la pendiente de educación se conserva porque este modelo no incluye interacciones.

$$\Delta\widehat{wage}=\widehat\beta_1\Delta educ\quad\text{con IQ fijo}$$

### El código, paso a paso

**`predict(multiple, newdata = nuevos)`**

Calcula predicciones para cada fila de nuevos. Debe contener las variables explicativas con los mismos nombres que el modelo.

**`diff(predicciones)`**

Resta valores consecutivos: aquí, la segunda predicción menos la primera.

**`seq(9, 18, length.out = 50)`**

Genera 50 valores equidistantes para dibujar una línea suave.

```r
nuevos <- data.frame(educ = c(12, 13), IQ = c(100, 100))
predicciones <- predict(multiple, newdata = nuevos)
print(data.frame(nuevos, salario_predicho = predicciones))
print(diff(predicciones))
print(coef(multiple)["educ"])
rejilla <- data.frame(educ = seq(9, 18, length.out = 50), IQ = 100)
plot(rejilla$educ, predict(multiple, newdata = rejilla), type = "l",
     col = "#005F96", lwd = 3, xlab = "Educación (años)",
     ylab = "Salario mensual predicho (USD)")
```

### Cómo leer el resultado

La diferencia entre 13 y 12 años, manteniendo IQ = 100, coincide con la pendiente de educación. Es una diferencia de predicciones del modelo, no una comparación causal garantizada entre personas.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
  educ  IQ salario_predicho
1   12 100         889.5973
2   13 100         931.6549
       2
42.05762
    educ
42.05762
```

</details>

### Comprueba lo aprendido

¿Qué se mantiene constante cuando se interpreta la pendiente de educación?

<details><summary>Mostrar respuesta</summary>

Las otras variables incluidas: aquí, IQ.

</details>

## 04 · MCO: elegir el plano que reduce los residuos

En el modelo múltiple elegimos tres coeficientes para minimizar la suma de residuos al cuadrado. La ilustración usa los cinco datos de la cátedra para poder seguir cada observación.

$$\min_{b_0,b_1,b_2}\sum_i(y_i-b_0-b_1x_{i1}-b_2x_{i2})^2$$

### El código, paso a paso

**`fitted(modelo5)`**

Devuelve una predicción para cada observación usada en el ajuste.

**`resid(modelo5)`**

Calcula los residuos: salario observado menos salario ajustado.

**`sum(resid(modelo5)^2)`**

Eleva cada residuo al cuadrado y suma. Esta es la función objetivo de MCO.

```r
ejemplo <- data.frame(
  persona = c("Juan", "Pedro", "Sofía", "Caro", "Alex"),
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
modelo5 <- lm(salario ~ experiencia + educacion, data = ejemplo)
print(coef(modelo5))
print(data.frame(ejemplo, ajustado = fitted(modelo5), residuo = resid(modelo5)))
print(sum(resid(modelo5)^2))
```

### Cómo leer el resultado

fitted() entrega los valores ajustados; resid() calcula observado menos ajustado. Los residuos pueden ser positivos o negativos, pero sus cuadrados son no negativos. Los valores de educación 74 a 119 se conservan como valores del ejemplo numérico de cátedra, sin interpretarlos como años reales.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
(Intercept) experiencia   educacion
 140.586358  -16.789532    8.236667
  persona experiencia educacion salario ajustado    residuo
1    Juan          12        93     769 705.1220  63.877990
2   Pedro          18       119     808 818.5382 -10.538161
3   Sofía          14       108     825 795.0930  29.907049
4    Caro          12        96     650 729.8320 -79.832011
5    Alex          11        74     562 565.4149  -3.414868
[1] 11470.69
```

</details>

### Comprueba lo aprendido

¿Minimizar residuos al cuadrado obliga a que todos los residuos sean cero?

<details><summary>Mostrar respuesta</summary>

No. MCO elige el mejor ajuste dentro de este modelo, pero suele quedar variación sin explicar.

</details>

## 05 · Construir X, y y el vector de parámetros

Cada fila de X representa una persona. La columna de unos permite estimar el intercepto. Recorre las filas para ver qué datos entran en cada ecuación.

$$y=X\beta+u,\quad X:\ n\times(k+1),\quad\beta:\ (k+1)\times1$$

### El código, paso a paso

**`model.matrix(modelo5)`**

Construye la matriz de diseño según la fórmula y las observaciones del modelo; incluye una columna de unos si hay intercepto.

**`cbind(unos = 1, ...)`**

Une columnas. El 1 se repite en las cinco filas al combinarse con los vectores.

**`dim(X), colnames(X) y as.vector(X)`**

dim entrega filas y columnas; colnames muestra los nombres; as.vector permite comparar los valores de ambas matrices sin sus atributos.

```r
X <- model.matrix(modelo5)
y <- ejemplo$salario
print(X)
print(y)
print(dim(X))
print(length(y))
print(colnames(X))
X_manual <- cbind(unos = 1, ejemplo$experiencia, ejemplo$educacion)
print(identical(as.vector(X), as.vector(X_manual)))
```

### Cómo leer el resultado

Hay n = 5 observaciones y k = 2 variables explicativas: X tiene dimensión 5 × 3; el vector de parámetros tiene 3 elementos. Las columnas son intercepto, experiencia y educación. El vector y tiene 5 valores.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
  (Intercept) experiencia educacion
1           1          12        93
2           1          18       119
3           1          14       108
4           1          12        96
5           1          11        74
attr(,"assign")
[1] 0 1 2
[1] 769 808 825 650 562
[1] 5 3
[1] 5
[1] "(Intercept)" "experiencia" "educacion"
[1] TRUE
```

</details>

### Comprueba lo aprendido

¿Por qué X tiene tres columnas si hay dos variables explicativas?

<details><summary>Mostrar respuesta</summary>

La tercera columna es la de unos para el intercepto.

</details>

## 06 · Transpuesta y producto matricial: t() y %*%

Selecciona una celda de XᵀX: verás qué dos columnas se multiplican y suman para obtenerla. La transpuesta convierte filas en columnas.

$$(X^\top X)_{23}=\sum_{i=1}^5x_{i1}x_{i2}$$

### El código, paso a paso

**`t(X)`**

Intercambia filas y columnas: de 5 × 3 pasa a 3 × 5.

**`t(X) %*% X`**

Producto matricial. Las dimensiones interiores deben coincidir: (3 × 5)(5 × 3) da 3 × 3.

**`X[, 2] * X[, 3]`**

Multiplica las dos columnas elemento a elemento. sum() produce el producto interno que aparece en XtX[2,3].

```r
XtX <- t(X) %*% X
Xty <- t(X) %*% y
print(XtX)
print(Xty)
print(dim(XtX))
print(sum(X[, 2] * X[, 3]))
print(XtX[2, 3])
print(head(X * X))
```

### Cómo leer el resultado

La entrada (2,3) de XᵀX es la suma de experiencia × educación. %*% multiplica matrices mediante sumas de productos; * multiplica elemento a elemento. XᵀX es 3 × 3; Xᵀy es 3 × 1.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
            (Intercept) experiencia educacion
(Intercept)           5          67       490
experiencia          67         929      6736
educacion           490        6736     49166
              [,1]
(Intercept)   3614
experiencia  49304
educacion   360757
[1] 3 3
[1] 6736
[1] 6736
  (Intercept) experiencia educacion
1           1         144      8649
2           1         324     14161
3           1         196     11664
4           1         144      9216
5           1         121      5476
```

</details>

### Comprueba lo aprendido

¿X * X es lo mismo que t(X) %*% X?

<details><summary>Mostrar respuesta</summary>

No. X * X mantiene la dimensión 5 × 3 y eleva cada celda al cuadrado.

</details>

## 07 · Calcular los coeficientes con solve() y compararlos con lm()

Primero reproducimos la fórmula de la cátedra. Después resolvemos las ecuaciones normales sin formar explícitamente la inversa.

$$\widehat\beta=(X^\top X)^{-1}X^\top y$$

### El código, paso a paso

**`solve(XtX)`**

Devuelve la inversa de XtX si es invertible. Aquí permite reproducir la fórmula teórica.

**`solve(XtX, Xty)`**

Resuelve XtX · beta = Xty sin pedir una inversa explícita. No elimina los problemas de condicionamiento de las ecuaciones normales.

**`all.equal(...), as.numeric(...) e isTRUE(...)`**

as.numeric convierte a vector; all.equal compara con tolerancia numérica; isTRUE produce un único TRUE o FALSE.

```r
beta_formula <- solve(XtX) %*% Xty
beta_sistema <- solve(XtX, Xty)
print(beta_formula)
print(beta_sistema)
print(coef(modelo5))
print(isTRUE(all.equal(as.numeric(beta_sistema), unname(coef(modelo5)))))
y_ajustado <- X %*% beta_sistema
print(cbind(observado = y, ajustado = y_ajustado))
```

### Cómo leer el resultado

Los tres métodos coinciden salvo diferencias de redondeo: aproximadamente 140,586; −16,790; 8,237. solve(A) calcula la inversa; solve(A,b) resuelve A·x = b. Para ajustar regresiones en la práctica usamos lm(), que evita formar las ecuaciones normales explícitamente y utiliza QR.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
                  [,1]
(Intercept) 140.586358
experiencia -16.789532
educacion     8.236667
                  [,1]
(Intercept) 140.586358
experiencia -16.789532
educacion     8.236667
(Intercept) experiencia   educacion
 140.586358  -16.789532    8.236667
[1] TRUE
  observado
1       769 705.1220
2       808 818.5382
3       825 795.0930
4       650 729.8320
5       562 565.4149
```

</details>

### Comprueba lo aprendido

¿Conviene redondear la inversa antes de multiplicar?

<details><summary>Mostrar respuesta</summary>

No. Redondea solo al mostrar; conserva precisión durante los cálculos.

</details>

## 08 · Verificar las propiedades algebraicas de MCO

Comprueba las condiciones de primer orden con los mismos cinco datos. Son propiedades del ajuste con intercepto, no supuestos sobre la distribución del error.

$$X^\top\widehat u=0,\quad\bar y=\overline{\widehat y}$$

### El código, paso a paso

**`round(t(X) %*% u_hat, 8)`**

Muestra con ocho decimales la ortogonalidad de los residuos con cada columna de X.

**`mean(y_ajustado)`**

Promedia los salarios ajustados; con intercepto coincide con mean(y).

**`predict(modelo5, newdata = medias)`**

Evalúa el plano en la media de cada variable explicativa.

```r
u_hat <- y - as.numeric(y_ajustado)
print(round(t(X) %*% u_hat, 8))
print(c(media_y = mean(y), media_ajustada = mean(y_ajustado)))
medias <- data.frame(experiencia = mean(ejemplo$experiencia),
                     educacion = mean(ejemplo$educacion))
print(predict(modelo5, newdata = medias))
print(mean(y))
```

### Cómo leer el resultado

La suma de residuos y la suma de cada regresor multiplicado por los residuos son cercanas a cero. La media observada coincide con la ajustada. El plano pasa por el punto de medias. Un valor como 10⁻¹⁰ es un residuo de precisión numérica, no una contradicción.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
            [,1]
(Intercept)    0
experiencia    0
educacion      0
       media_y media_ajustada
         722.8          722.8
    1
722.8
[1] 722.8
```

</details>

### Comprueba lo aprendido

¿Estas igualdades prueban que no hay variables omitidas?

<details><summary>Mostrar respuesta</summary>

No. Se cumplen algebraicamente en el ajuste MCO con intercepto, aunque la especificación sea inadecuada.

</details>

## 09 · Rango completo: cuándo falla la inversa

Duplica deliberadamente una columna para reconocer la colinealidad exacta. Este es un ejemplo de diagnóstico, no una instrucción para construir el modelo final.

### El código, paso a paso

**`qr(X_duplicada)$rank`**

Obtiene el número de columnas linealmente independientes. Debe coincidir con el número de parámetros para invertir XᵀX.

**`tryCatch(..., error = function(e) conditionMessage(e))`**

Captura el error esperado y lo muestra como texto para que el notebook continúe. e contiene la información del error.

**`coef(lm(...))`**

Una pendiente puede aparecer como NA porque es redundante; no porque haya una fila con valor faltante.

```r
X_duplicada <- cbind(unos = 1, experiencia = ejemplo$experiencia,
                      repetida = ejemplo$experiencia)
print(c(columnas = ncol(X_duplicada), rango = qr(X_duplicada)$rank))
problema <- tryCatch(solve(t(X_duplicada) %*% X_duplicada),
                     error = function(e) conditionMessage(e))
print(problema)
ejemplo$repetida <- ejemplo$experiencia
print(coef(lm(salario ~ experiencia + repetida, data = ejemplo)))
```

### Cómo leer el resultado

Hay tres columnas, pero solo dos independientes. No se pueden identificar dos pendientes separadas para columnas idénticas. solve() informa el problema y lm() marca un coeficiente redundante con NA. No se trata de un dato faltante del dataset.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
columnas    rango
       3        2
[1] "Lapack routine dgesv: system is exactly singular: U[3,3] = 0"
(Intercept) experiencia    repetida
  346.39744    28.08974          NA
```

</details>

### Comprueba lo aprendido

¿Tener más filas que columnas garantiza rango completo?

<details><summary>Mostrar respuesta</summary>

No. Puede haber columnas duplicadas o combinaciones lineales exactas.

</details>

## 10 · R² y R² ajustado: comparar sobre la misma muestra

Usa la botonera para cambiar de modelo. La comparación utiliza siempre las mismas 935 personas y la misma variable dependiente.

$$R^2=1-\frac{SSR}{SST},\quad\overline R^2=1-\frac{n-1}{n-k-1}\frac{SSR}{SST}$$

### El código, paso a paso

**`summary(modelo)$adj.r.squared`**

Extrae el R² ajustado del resumen; r.squared entrega el R² sin penalización.

**`nobs(modelo) y length(coef(modelo)) - 1`**

nobs cuenta observaciones usadas. Restamos el intercepto para contar k en este modelo de rango completo.

**`function(modelo) y rbind(...)`**

Define una función reutilizable y apila sus resultados como filas para comparar.

```r
medidas <- function(modelo) {
  s <- summary(modelo)
  c(n = nobs(modelo), R2 = s$r.squared,
    R2_ajustado = s$adj.r.squared, SSR = sum(resid(modelo)^2))
}
print(rbind(simple = medidas(simple), multiple = medidas(multiple)))
SSR <- sum(resid(multiple)^2)
SST <- sum((datos$wage - mean(datos$wage))^2)
SSE <- sum((fitted(multiple) - mean(datos$wage))^2)
n <- nobs(multiple)
k <- length(coef(multiple)) - 1
print(c(R2 = 1 - SSR/SST,
        R2_ajustado = 1 - (SSR/(n-k-1))/(SST/(n-1))))
print(c(SST = SST, SSE_mas_SSR = SSE + SSR))
```

### Cómo leer el resultado

Seguimos la nomenclatura de cátedra: SSR es residual; SSE es explicada; SST es total. En modelos anidados con intercepto sobre la misma muestra, R² no disminuye al agregar regresores; el ajustado sí puede disminuir. Ninguno mide por sí solo causalidad o desempeño fuera de muestra.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
           n        R2 R2_ajustado       SSR
simple   935 0.1070001   0.1060430 136375524
multiple 935 0.1338534   0.1319947 132274591
         R2 R2_ajustado
  0.1338534   0.1319947
        SST SSE_mas_SSR
  152716168   152716168
```

</details>

### Comprueba lo aprendido

¿Se puede comparar R² directamente si cambia la variable dependiente o la muestra?

<details><summary>Mostrar respuesta</summary>

La comparación deja de aislar el cambio de regresores. Aquí fijamos tanto la muestra como wage.

</details>

## 11 · La trampa de agregar variables de ruido

Un experimento simulado separa ajuste dentro de muestra de información real. Mueve el número de variables añadidas y observa qué medida sube o baja.

### El código, paso a paso

**`matrix(..., nrow = ..., ncol = ...)`**

Ordena los valores aleatorios en una matriz de 30 filas y 10 columnas.

**`ruido[, seq_len(j), drop = FALSE]`**

Conserva las primeras j columnas; drop = FALSE evita convertir la selección de una sola columna en un vector.

**`matplot(x, y, type = "l", lty = 1)`**

Dibuja una línea por columna de y. type elige líneas y lty su estilo.

```r
set.seed(5)
n_sim <- 30
x_sim <- rnorm(n_sim)
y_sim <- 1 + 2*x_sim + rnorm(n_sim, sd = 2)
ruido <- matrix(rnorm(n_sim*10), nrow = n_sim, ncol = 10)
trayectoria <- data.frame(k_ruido = 0:10, R2 = NA, R2_ajustado = NA)
for (j in 0:10) {
  if (j == 0) {
    modelo_ruido <- lm(y_sim ~ x_sim)
  } else {
    z <- ruido[, seq_len(j), drop = FALSE]
    modelo_ruido <- lm(y_sim ~ x_sim + z)
  }
  s <- summary(modelo_ruido)
  trayectoria$R2[j+1] <- s$r.squared
  trayectoria$R2_ajustado[j+1] <- s$adj.r.squared
}
print(trayectoria)
matplot(trayectoria$k_ruido, trayectoria[, c("R2", "R2_ajustado")],
        type = "l", lty = 1, col = c("#005F96", "#D6A600"),
        xlab = "Variables de ruido añadidas", ylab = "Bondad de ajuste")
legend("bottomright", c("R²", "R² ajustado"), lty = 1,
       col = c("#005F96", "#D6A600"))
```

### Cómo leer el resultado

Las variables añadidas se generaron sin relación poblacional con y, pero pueden ajustar variación accidental de esta muestra. R² sube o se mantiene; el ajustado puede subir o bajar. No es una prueba definitiva de relevancia ni una medida de validación fuera de muestra.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
   k_ruido        R2 R2_ajustado
1        0 0.6519739   0.6395443
2        1 0.6623217   0.6373085
3        2 0.6697446   0.6316382
4        3 0.6711030   0.6184794
5        4 0.6757681   0.6082198
6        5 0.6833896   0.6007956
7        6 0.6860987   0.5862211
8        7 0.6957605   0.5798597
9        8 0.6959812   0.5591727
10       9 0.6979866   0.5390321
11      10 0.6993595   0.5156348
```

</details>

### Comprueba lo aprendido

¿El R² ajustado siempre baja al agregar ruido?

<details><summary>Mostrar respuesta</summary>

No. Puede subir por una asociación accidental en una muestra. La simulación muestra por qué no basta con mirar R².

</details>

## 12 · Interpretar summary() y ANOVA en el ejemplo de cátedra

Abre los componentes para identificar estimaciones, incertidumbre, grados de libertad y suma de cuadrados. Aquí n = 5 y k = 2: solo quedan dos grados de libertad residuales.

### El código, paso a paso

**`summary(modelo5)$coefficients`**

Estimate es el coeficiente; Std. Error su error estándar; t value contrasta coeficiente cero y Pr(>|t|) es su p-valor bajo los supuestos del contraste.

**`anova(modelo5)`**

Da ANOVA secuencial: cada fila incorpora el regresor después de los anteriores. El orden puede afectar estas contribuciones cuando están correlacionados.

**`df.residual(modelo5)`**

Entrega n menos el rango de X: aquí 5 − 3 = 2. La prueba F global de summary contrasta conjuntamente las dos pendientes iguales a cero.

```r
resumen5 <- summary(modelo5)
print(resumen5)
print(resumen5$coefficients)
print(anova(modelo5))
print(c(R2 = resumen5$r.squared, R2_ajustado = resumen5$adj.r.squared))
print(df.residual(modelo5))
```

### Cómo leer el resultado

Los coeficientes coinciden con el cálculo matricial. Un coeficiente estimado negativo no implica una relación conocida con certeza: hay mucha incertidumbre con cinco datos. anova(modelo5) muestra sumas de cuadrados secuenciales, que pueden cambiar de asignación si cambia el orden de los regresores.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text

Call:
lm(formula = salario ~ experiencia + educacion, data = ejemplo)

Residuals:
      1       2       3       4       5
 63.878 -10.538  29.907 -79.832  -3.415

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  140.586    224.616   0.626    0.595
experiencia  -16.790     30.964  -0.542    0.642
educacion      8.237      5.109   1.612    0.248

Residual standard error: 75.73 on 2 degrees of freedom
Multiple R-squared:  0.7751,	Adjusted R-squared:  0.5501
F-statistic: 3.446 on 2 and 2 DF,  p-value: 0.2249

              Estimate Std. Error    t value  Pr(>|t|)
(Intercept) 140.586358 224.616363  0.6258954 0.5952896
experiencia -16.789532  30.964358 -0.5422212 0.6420030
educacion     8.236667   5.109131  1.6121463 0.2482525
Analysis of Variance Table

Response: salario
            Df Sum Sq Mean Sq F value Pr(>F)
experiencia  1  24618 24617.9  4.2923 0.1741
educacion    1  14906 14906.3  2.5990 0.2483
Residuals    2  11471  5735.3
         R2 R2_ajustado
  0.7750615   0.5501230
[1] 2
```

</details>

### Comprueba lo aprendido

¿La ANOVA secuencial de experiencia equivale a su prueba t controlando educación?

<details><summary>Mostrar respuesta</summary>

No en general. La primera fila entra antes de educación; la prueba t del modelo completo controla ambas variables.

</details>

## 13 · Ejercicio guiado: estimar y explicar una regresión múltiple real

Con wage2, escribe el modelo wage ~ educ + IQ. Compara los coeficientes, calcula la predicción para educ = 12 e IQ = 100 y comprueba la fórmula matricial. Intenta resolverlo antes de desplegar el código.

### El código, paso a paso

**`model.frame(fit)`**

Recupera las filas y variables que efectivamente utilizó el ajuste.

**`model.response(model.frame(fit))`**

Extrae de esas filas la respuesta, alineada con model.matrix(fit). Evita comparar matrices con observaciones distintas.

**`summary(fit), anova(fit) y coef(fit)`**

Resumen completo, descomposición secuencial y coeficientes. Responde con unidades y distingue asociación de causalidad.

```r
fit <- lm(wage ~ educ + IQ, data = datos)
print(summary(fit))
print(anova(fit))
print(coef(fit))
print(predict(fit, newdata = data.frame(educ = 12, IQ = 100)))
X_real <- model.matrix(fit)
y_real <- model.response(model.frame(fit))
beta_real <- solve(t(X_real) %*% X_real, t(X_real) %*% y_real)
print(beta_real)
print(isTRUE(all.equal(as.numeric(beta_real), unname(coef(fit)))))
print(head(data.frame(observado = y_real, predicho = fitted(fit),
                      residuo = resid(fit))))
```

### Cómo leer el resultado

Interpreta educación en USD mensuales por un año adicional, manteniendo IQ constante; IQ en USD mensuales por un punto adicional, manteniendo educación constante. El intercepto puede quedar fuera de una situación económicamente plausible.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text

Call:
lm(formula = wage ~ educ + IQ, data = datos)

Residuals:
    Min      1Q  Median      3Q     Max
-860.29 -251.00  -35.31  203.98 2110.38

Coefficients:
             Estimate Std. Error t value Pr(>|t|)
(Intercept) -128.8899    92.1823  -1.398    0.162
educ          42.0576     6.5498   6.421 2.15e-10 ***
IQ             5.1380     0.9558   5.375 9.66e-08 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 376.7 on 932 degrees of freedom
Multiple R-squared:  0.1339,	Adjusted R-squared:  0.132
F-statistic: 72.02 on 2 and 932 DF,  p-value: < 2.2e-16

Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
educ        1  16340645 16340645 115.135 < 2.2e-16 ***
IQ          1   4100932  4100932  28.895  9.66e-08 ***
Residuals 932 132274591   141926
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
(Intercept)        educ          IQ
-128.889881   42.057619    5.137958
       1
889.5973
                   [,1]
(Intercept) -128.889881
educ          42.057619
IQ             5.137958
[1] TRUE
  observado  predicho   residuo
1       769  853.6316  -84.6316
2       808 1239.5642 -431.5642
3       825 1014.8162 -189.8162
4       650  869.0455 -219.0455
5       562  713.9528 -151.9528
6      1400 1140.0351  259.9649
```

</details>

### Comprueba lo aprendido

¿Qué debes reportar además del signo de una pendiente?

<details><summary>Mostrar respuesta</summary>

Su valor, sus unidades, qué variables se mantienen constantes y la incertidumbre de la estimación.

</details>

## 14 · Inversa por cofactores: elegir un menor

Usamos A = XᵀX del ejemplo de cinco personas. Al seleccionar una celda, se destaca la fila y columna que se eliminan para formar el menor 2 × 2.

$$C_{ij}=(-1)^{i+j}\det(A_{-i,-j})$$

### El código, paso a paso

**`A[-i, -j]`**

Los índices negativos excluyen una fila y una columna. Aquí se elimina la fila 1 y la columna 2.

**`det(menor)`**

Calcula el determinante de la submatriz. En 2 × 2 equivale a a·d − b·c.

**`(-1)^(i+j)`**

Aplica el patrón de signos del cofactor: positivo si i+j es par, negativo si es impar.

```r
A <- t(X) %*% X
print(A)
i <- 1
j <- 2
menor <- A[-i, -j]
print(menor)
print(det(menor))
print((-1)^(i+j) * det(menor))
```

### Cómo leer el resultado

Para (i,j) = (1,2), el menor tiene determinante −6518 y el cofactor cambia el signo, por lo que vale 6518. Un menor es un determinante; la submatriz es el bloque que queda al eliminar fila y columna.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
            (Intercept) experiencia educacion
(Intercept)           5          67       490
experiencia          67         929      6736
educacion           490        6736     49166
            (Intercept) educacion
experiencia          67      6736
educacion           490     49166
[1] -6518
[1] 6518
```

</details>

### Comprueba lo aprendido

¿Un menor negativo siempre produce un cofactor negativo?

<details><summary>Mostrar respuesta</summary>

No. Depende también del factor (−1)^(i+j).

</details>

## 15 · Cofactores, adjunta, determinante e inversa

Construye la matriz de cofactores mediante dos ciclos for. Luego transpón y divide por el determinante. Recorre los pasos en la animación.

$$A^{-1}=\frac{C^\top}{\det(A)}$$

### El código, paso a paso

**`for (i in 1:3) y for (j in 1:3)`**

Recorren las nueve celdas: una fila y, dentro de ella, las tres columnas.

**`sum(A[1, ] * cofactores[1, ])`**

Expande el determinante por la primera fila. No es la suma simple de los elementos de A.

**`adjunta / determinante`**

Divide cada elemento de la adjunta por un escalar. Solo se puede hacer si el determinante no es cero.

```r
cofactores <- matrix(0, nrow = 3, ncol = 3)
for (i in 1:3) {
  for (j in 1:3) {
    cofactores[i, j] <- (-1)^(i+j) * det(A[-i, -j])
  }
}
adjunta <- t(cofactores)
determinante <- sum(A[1, ] * cofactores[1, ])
inversa <- adjunta / determinante
print(round(cofactores))
print(determinante)
print(round(inversa, 6))
print(isTRUE(all.equal(inversa, unname(solve(A)), check.attributes = FALSE)))
print(round(A %*% inversa, 8))
```

### Cómo leer el resultado

El determinante es 34276. La matriz producto A·A⁻¹ es la identidad. La adjunta coincide con los cofactores en este ejemplo simétrico, pero la definición general exige transponer. El procedimiento es didáctico; para sistemas reales se prefieren algoritmos numéricos.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
       [,1] [,2]  [,3]
[1,] 301518 6518 -3898
[2,]   6518 5730  -850
[3,]  -3898 -850   156
[1] 34276
          [,1]      [,2]      [,3]
[1,]  8.796767  0.190162 -0.113724
[2,]  0.190162  0.167172 -0.024799
[3,] -0.113724 -0.024799  0.004551
[1] TRUE
            [,1] [,2] [,3]
(Intercept)    1    0    0
experiencia    0    1    0
educacion      0    0    1
```

</details>

### Comprueba lo aprendido

¿La adjunta es siempre igual a la matriz de cofactores?

<details><summary>Mostrar respuesta</summary>

No. Es su transpuesta; aquí coinciden por simetría.

</details>

## 16 · Cerrar el recorrido: de los datos a la predicción

Ejecuta este bloque completo con los cinco datos, sin depender de variables anteriores. Reproduce el cálculo matricial, las predicciones, el resumen y la ANOVA. Después explica cada resultado con tus palabras.

### El código, paso a paso

**`lm(salario ~ experiencia + educacion, data = ejercicio)`**

Especifica la relación que se estima: dos pendientes e intercepto.

**`X_final %*% beta_final`**

Reconstruye las predicciones con las mismas columnas y en el mismo orden.

**`t(X_final) %*% resid(fit_final)`**

Comprueba las tres condiciones de ortogonalidad del ajuste.

```r
ejercicio <- data.frame(
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
fit_final <- lm(salario ~ experiencia + educacion, data = ejercicio)
X_final <- model.matrix(fit_final)
y_final <- ejercicio$salario
beta_final <- solve(t(X_final) %*% X_final, t(X_final) %*% y_final)
print(beta_final)
print(summary(fit_final))
print(anova(fit_final))
print(data.frame(ejercicio, ajustado = as.numeric(X_final %*% beta_final),
                 residuo = resid(fit_final)))
print(round(t(X_final) %*% resid(fit_final), 8))
```

### Cómo leer el resultado

La fórmula matricial y lm() llegan al mismo ajuste. Antes de interpretar: identifica respuesta, unidades, regresores, muestra y grados de libertad. Al agregar variables, recuerda que un mejor ajuste muestral no demuestra causalidad ni asegura mejores predicciones nuevas.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
                  [,1]
(Intercept) 140.586358
experiencia -16.789532
educacion     8.236667

Call:
lm(formula = salario ~ experiencia + educacion, data = ejercicio)

Residuals:
      1       2       3       4       5
 63.878 -10.538  29.907 -79.832  -3.415

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  140.586    224.616   0.626    0.595
experiencia  -16.790     30.964  -0.542    0.642
educacion      8.237      5.109   1.612    0.248

Residual standard error: 75.73 on 2 degrees of freedom
Multiple R-squared:  0.7751,	Adjusted R-squared:  0.5501
F-statistic: 3.446 on 2 and 2 DF,  p-value: 0.2249

Analysis of Variance Table

Response: salario
            Df Sum Sq Mean Sq F value Pr(>F)
experiencia  1  24618 24617.9  4.2923 0.1741
educacion    1  14906 14906.3  2.5990 0.2483
Residuals    2  11471  5735.3
  experiencia educacion salario ajustado    residuo
1          12        93     769 705.1220  63.877990
2          18       119     808 818.5382 -10.538161
3          14       108     825 795.0930  29.907049
4          12        96     650 729.8320 -79.832011
5          11        74     562 565.4149  -3.414868
            [,1]
(Intercept)    0
experiencia    0
educacion      0
```

</details>

### Comprueba lo aprendido

¿Qué conecta los siete temas de la clase?

<details><summary>Mostrar respuesta</summary>

La matriz X organiza el modelo; MCO estima sus coeficientes; los residuos verifican propiedades y las medidas de ajuste resumen cuánto se explica.

</details>

## Para la próxima clase

Revisa las indicaciones de la cátedra. Repasa los siete temas y reconstruye el ejemplo de cinco personas sin mirar la solución.
