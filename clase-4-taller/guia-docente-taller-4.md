# Clase 4 · Regresión lineal múltiple en R

Ejecuta en orden con kernel R. En Google Colab selecciona R como tipo de entorno. No uses rpy2 ni %%R.

[Clase teórica de referencia](https://hizocar.github.io/econometria-usm/clases/clase4/)

## Agenda

| Horario | Actividad |
|---|---|
| 18:50–19:10 | Del modelo simple al múltiple |
| 19:10–19:25 | MCO con dos regresores |
| 19:25–19:45 | Notación y operaciones matriciales |
| 19:45–20:00 | Modelo completo y ANOVA |
| 20:00–20:15 | Descanso |
| 20:15–20:35 | Coeficientes y significancia |
| 20:35–20:55 | Correlaciones y modelo reducido |
| 20:55–21:05 | Comparación de R² y R² ajustado |
| 21:05–21:25 | Ejercicio en Colab |

## 01 · Regresión múltiple: notación y función lm()

El modelo ajustado se escribe Ŷ = Xβ̂: Ŷ contiene las predicciones y β̂ los coeficientes estimados. X contiene los valores observados de los regresores y no lleva acento. Para una observación i, sumamos los p términos de esa fila. Aquí p = k + 1 incluye el intercepto, con Xᵢ₁ = 1; j recorre los parámetros e i identifica la observación.

$$\widehat{Y}=X\widehat{\beta}\qquad \widehat{Y}_i=\sum_{j=1}^{p}\widehat{\beta}_jX_{ij},\quad X_{i1}=1,\quad p=k+1$$

### En R · Tu turno

### El código, paso a paso

**`demo <- data.frame(y = c(...), x1 = c(...), x2 = c(...))`**

c() reúne valores en un vector. data.frame() coloca los vectores en columnas con nombre. Cada posición corresponde a la misma observación en las tres columnas. La flecha <- guarda la tabla bajo el nombre demo.

**`print(coef(modelo_demo))`**

R evalúa primero coef(modelo_demo) y luego print() muestra el resultado. La llamada interior obtiene los coeficientes y la exterior los imprime.

**`lm(formula, data, subset, weights, na.action, method = "qr", ...)`**

Es una referencia de argumentos, no una llamada lista para ejecutar. Normalmente basta con formula y data. method = "qr" usa descomposición QR.

**`formula: y ~ x1 + x2`**

y es la respuesta; x1 y x2 son regresores. + incorpora columnas al modelo. El intercepto se incluye por defecto; y ~ x1 + x2 - 1 lo elimina.

**`data = demo`**

Indica el data frame que contiene las variables. Es recomendable para que R no tome por accidente variables del entorno.

**`subset = condición`**

Opcional: selecciona las filas a utilizar antes del ajuste, por ejemplo subset = x1 >= 2. Cambiar la muestra cambia la comparación.

**`na.action = na.exclude`**

Gestiona filas incompletas. na.omit las excluye; na.exclude también, pero reinserta NA en residuos y predicciones sobre los datos originales. Sin especificarlo se consulta getOption("na.action"). Aquí no hay faltantes.

**`weights = vector_de_pesos`**

Opcional: ajusta por mínimos cuadrados ponderados. No se necesita para los ejemplos MCO sin ponderación de este taller.

**`coef(modelo_demo) y fitted(modelo_demo)`**

coef extrae β̂, con un nombre por parámetro. fitted devuelve Ŷ para las observaciones del ajuste. En cada fila usa los valores de x1 y x2 junto con los coeficientes ya estimados.

```r
demo <- data.frame(y = c(4, 6, 7, 9, 8, 11),
                   x1 = c(1, 2, 3, 4, 2, 5),
                   x2 = c(2, 1, 3, 2, 4, 3))
modelo_demo <- lm(y ~ x1 + x2, data = demo, na.action = na.exclude)
print(coef(modelo_demo))
print(fitted(modelo_demo))
```

### Cómo leer el resultado

La fórmula con acentos representa el ajuste, no la respuesta observada exacta: Y = Ŷ + û. Usamos β̂₁ para el intercepto en la suma indexada desde j = 1; en la convención habitual que comienza en cero se llama β̂₀. lm() incluye intercepto por defecto. Este ejemplo usa seis observaciones simuladas solo para reconocer la sintaxis.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
(Intercept)          x1          x2
  1.9040698   1.4389535   0.6075581
        1         2         3         4         5         6
 4.558140  5.389535  8.043605  8.875000  7.212209 10.921512
```

</details>

### Comprueba lo aprendido

¿Por qué X no lleva acento y por qué la suma usa j?

<details><summary>Mostrar respuesta</summary>

X reúne los regresores observados; estimamos β y calculamos Ŷ. El índice i fija la observación y j recorre las p columnas de esa fila.

</details>

## 02 · Conocer la base wage2 y sus campos

wage2 es una base de corte transversal del paquete wooldridge con 935 observaciones y 17 campos. Cada fila representa a un trabajador observado en 1980. En el taller usaremos el salario mensual como respuesta y la educación y el IQ como regresores.

| Campo | Significado |
|---|---|
| `wage` | Salario mensual en dólares. Variable respuesta. |
| `educ` | Años de educación. Regresor. |
| `IQ` | Puntaje de coeficiente intelectual. Regresor. |
| `hours` | Promedio de horas trabajadas por semana. |
| `KWW` | Puntaje en una prueba de conocimientos sobre el mundo laboral. |
| `exper` | Años de experiencia laboral. |
| `tenure` | Años con el empleador actual. |
| `age` | Edad en años. |
| `married` | Indicador de estado civil. Vale 1 si está casado. |
| `black` | Indicador racial en el registro. Vale 1 para personas negras. |
| `south` | Indicador de residencia en el sur de Estados Unidos. |
| `urban` | Indicador de residencia en un área metropolitana estadística (SMSA). |
| `sibs` | Número de hermanos. |
| `brthord` | Orden de nacimiento entre los hermanos. |
| `meduc` | Educación de la madre. |
| `feduc` | Educación del padre. |
| `lwage` | Logaritmo natural del salario mensual. |

[Documentación del conjunto de datos](https://justinmshea.github.io/wooldridge/reference/wage2.html)

### Cómo leer el resultado

En la lámina 3 cargaremos las 17 columnas en original y crearemos datos con las tres columnas del modelo. Cada regresión de wage2 del taller parte de esa tabla de trabajo.

### Comprueba lo aprendido

¿Qué columna se quiere predecir y cuáles se usarán para predecirla?

<details><summary>Mostrar respuesta</summary>

Queremos predecir wage a partir de educ e IQ.

</details>

## 03 · Cargar wage2 y crear datos

Ejecuta este bloque completo para crear datos. La línea que comienza con datos <- conserva wage, educ e IQ y selecciona las filas que tienen un valor en las tres columnas. Los modelos de wage2 usan este objeto a partir de la lámina 4.

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

### El código, paso a paso

**`if (file.exists(...)) { ... } else { ... }`**

file.exists() devuelve TRUE si el archivo está en la ruta indicada. if ejecuta el primer bloque cuando la condición se cumple. else ejecuta la alternativa. read.csv() lee el archivo con encabezados como una tabla.

**`!requireNamespace(...) e install.packages(...)`**

requireNamespace() comprueba si el paquete se puede cargar. quietly = TRUE sirve para evitar mensajes de diagnóstico. ! invierte el valor lógico. Si el paquete falta, install.packages() lo descarga desde el repositorio indicado en repos.

**`as.data.frame(wooldridge::wage2)`**

:: accede a wage2 dentro del paquete wooldridge. as.data.frame() lo convierte al formato de tabla que usaremos.

**`colSums(is.na(original[variables]))`**

original[variables] selecciona las columnas nombradas en el vector variables. is.na() marca cada faltante como TRUE. colSums() suma esos indicadores por columna y entrega el número de faltantes de cada variable.

**`datos <- original[complete.cases(original[variables]), variables]`**

Esta línea crea datos. Antes de la coma, complete.cases() marca las filas completas en wage, educ e IQ. Después de la coma, variables selecciona esas tres columnas. La flecha guarda el resultado en datos.

**`nrow(), str(), summary() y head()`**

nrow() cuenta filas. str() muestra la estructura y el tipo de cada columna. Para una tabla como datos, summary() resume cada columna. head() muestra las primeras seis filas por defecto.

### Cómo leer el resultado

original conserva la base completa. datos contiene wage, educ e IQ. La salida muestra cero faltantes en esas columnas y confirma que se conservan las 935 filas. Ejecuta esta lámina si reinicias la sesión de R antes de ajustar los modelos.

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

## 04 · El plano de predicción y los vectores de MCO

El plano da el salario mensual predicho para cada combinación de educación e IQ. Cada eje representa una variable. Fija el IQ para recorrer una recta sobre el plano y leer cómo cambia el salario predicho al aumentar la educación.

$$\widehat{wage}=\widehat\beta_0+\widehat\beta_1\,educ+\widehat\beta_2\,IQ\qquad IQ=c\Rightarrow\widehat{wage}=(\widehat\beta_0+\widehat\beta_2c)+\widehat\beta_1\,educ\qquad Y=\widehat Y+\widehat u,\quad \widehat Y=X\widehat\beta$$

### Vectores y notación

- **β̂**. Vector de coeficientes estimados. β̂₀ es el intercepto, β̂₁ es el cambio en el salario predicho por un año adicional de educación con IQ fijo y β̂₂ es el cambio por un punto adicional de IQ con educación fija.
- **Y**. Vector de salarios observados. Tiene un valor por trabajador de la muestra.
- **Ŷ = Xβ̂**. Vector de salarios predichos para esos mismos trabajadores. Cada fila de X aporta el 1 del intercepto, los años de educación y el IQ de un trabajador.
- **û = Y − Ŷ**. Vector de residuos. Cada entrada es la diferencia entre el salario observado y el predicho. En el esquema de proyección, û es perpendicular a Col(X).
- **v**. Otro vector posible de predicciones dentro de Col(X). El segmento Y − v muestra el error que resulta al elegir v. MCO elige Ŷ para minimizar la suma de los errores al cuadrado.
- **Col(X)**. Espacio generado por las columnas de X. Contiene los vectores de predicciones posibles. El gráfico del plano usa los ejes de las variables. El esquema de proyección representa los vectores en el espacio de las observaciones.

### Cómo leer el resultado

En el plano, el corte con IQ fijo permite leer la pendiente de educación. En el esquema de proyección, la distancia de Y a Ŷ representa el tamaño del vector de residuos.

### Comprueba lo aprendido

¿Qué vector reúne las diferencias entre los salarios observados y los predichos?

<details><summary>Mostrar respuesta</summary>

El vector de residuos û = Y − Ŷ.

</details>

## 05 · Del modelo simple al múltiple

Ajusta dos modelos a las mismas observaciones de wage2. El modelo a usa educación y el modelo b usa educación e IQ. Dibuja ambas rectas sobre la misma nube de educación y salario. Para trazar la recta del modelo b, fija IQ = 100.

$$\widehat{wage}=\widehat\beta_0+\widehat\beta_1\,educ+\widehat\beta_2\,IQ$$

### En R · Tu turno

### El código, paso a paso

**`lm(wage ~ educ + IQ, data = datos)`**

Estima intercepto y dos pendientes. La variable dependiente está a la izquierda de ~.

**`coef(multiple)["educ"]`**

Extrae por su nombre la pendiente de educación del modelo múltiple.

**`data.frame(modelo = ..., pendiente_educ = ...)`**

Organiza los coeficientes en una tabla para comparar las mismas unidades.

**`plot(wage ~ educ, data = datos, pch = 19, col = ...)`**

Dibuja educación en el eje horizontal y salario en el vertical. data indica de qué tabla salen las columnas, pch = 19 elige puntos sólidos y col fija el color. Los últimos dos dígitos del color hexadecimal controlan la transparencia.

**`abline(simple, col = ..., lwd = 3)`**

Agrega al gráfico abierto una recta con intercepto y pendiente del modelo simple. col fija el color y lwd el grosor.

**`abline(a = ..., b = ..., lty = 2)`**

Agrega la recta del modelo múltiple al mismo gráfico. a es el intercepto del corte con IQ = 100 y b es la pendiente de educación. lty = 2 dibuja la línea discontinua.

**`legend("topleft", ..., bty = "n")`**

Identifica las dos rectas en la esquina superior izquierda. Cada etiqueta usa el color y el tipo de línea de su modelo. bty = "n" quita el borde de la leyenda.

```r
# a) Modelo simple
simple <- lm(wage ~ educ, data = datos)
# b) Modelo múltiple
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

iq_referencia <- 100
b <- coef(multiple)
abline(a = b["(Intercept)"] + b["IQ"] * iq_referencia,
       b = b["educ"], col = "#B93E42", lwd = 3, lty = 2)
legend("topleft", legend = c("a) Solo educación", "b) Educación + IQ (IQ = 100)"),
       col = c("#D6A600", "#B93E42"), lwd = 3, lty = c(1, 2), bty = "n")
```

### Cómo leer el resultado

La recta dorada continua corresponde al modelo a. La roja discontinua corresponde al modelo b con IQ = 100. Las dos usan la misma nube de observaciones. Compara sus pendientes para ver cuánto cambia la asociación estimada entre educación y salario al incluir IQ. Si fijas otro IQ, cambia el intercepto del corte y se conserva la pendiente del modelo b.

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

## 06 · ¿Cuánto cambia el salario predicho con un año más de educación?

Comparemos el salario mensual predicho para 12 y 13 años de educación. Primero fijamos IQ en 90 y comparamos esas dos predicciones. Luego repetimos la comparación con IQ en 100. El objetivo es distinguir el cambio por un año más de educación del cambio de nivel al elegir otro IQ.

### En R · Tu turno

### El código, paso a paso

**`expand.grid(educ = ..., IQ = ...)`**

Devuelve una tabla con todas las parejas de educación e IQ. Educación es el primer argumento y varía primero. Con educ = c(12, 13) e IQ = c(90, 100), las filas son (12, 90), (13, 90), (12, 100) y (13, 100), en ese orden.

**`predict(modelo_vista, newdata = rejilla_vista)`**

El primer argumento es el modelo que ya estimamos con lm(). newdata es la tabla donde queremos predecir. Sus columnas deben llamarse educ e IQ, como en la fórmula. R toma una fila, multiplica sus valores por las pendientes estimadas y agrega el intercepto. Repite el cálculo para cada fila. En esta llamada devuelve un vector de cuatro salarios predichos en el mismo orden que la tabla. Los coeficientes se mantienen fijos. Si omites newdata, calcula sobre las observaciones del ajuste.

**`matrix(pred_vista, nrow = ..., ncol = ...)`**

persp() necesita una altura z[i, j] para cada cruce entre la educación i y el IQ j. predict() entrega esas alturas en un vector. matrix() conserva los valores y los coloca por columnas. En esta matriz de 2 × 2, las predicciones 1 y 2 llenan la columna de IQ = 90 y las predicciones 3 y 4 llenan la de IQ = 100. Dentro de cada columna, la primera fila es educación 12 y la segunda es educación 13. Este orden coincide con expand.grid() porque educación varía primero.

**`length(educ_vista) y length(iq_vista)`**

length() cuenta los elementos del vector. Aquí ambos vectores tienen dos elementos. La matriz tiene dos filas para educación y dos columnas para IQ.

**`persp(educ_vista, iq_vista, z_vista, ...)`**

Los dos primeros argumentos son las coordenadas de los ejes horizontales. El tercero es la matriz de alturas. persp() toma z_vista[i, j] como el salario predicho para educ_vista[i] e iq_vista[j] y une los puntos para dibujar la superficie. theta y phi ajustan el ángulo de la cámara. xlab, ylab y zlab nombran los ejes, col colorea la superficie y ticktype = "detailed" muestra marcas con sus valores.

```r
modelo_vista <- lm(wage ~ educ + IQ, data = datos)
educ_vista <- c(12, 13)
iq_vista <- c(90, 100)
rejilla_vista <- expand.grid(educ = educ_vista, IQ = iq_vista)
pred_vista <- predict(modelo_vista, newdata = rejilla_vista)
print(data.frame(rejilla_vista, salario_predicho = pred_vista))

# Filas de educación y columnas de IQ
z_vista <- matrix(pred_vista, nrow = length(educ_vista),
                  ncol = length(iq_vista))
print(z_vista)
persp(educ_vista, iq_vista, z_vista, theta = 35, phi = 25,
      xlab = "Educación", ylab = "IQ", zlab = "Salario predicho",
      col = "lightblue", ticktype = "detailed")
```

### Cómo leer el resultado

Con IQ = 90, la predicción sube de USD 838,22 a USD 880,28 al pasar de 12 a 13 años de educación. Con IQ = 100, sube de USD 889,60 a USD 931,65. Calculada antes de redondear, la diferencia es USD 42,06 en ambos casos. En la matriz, baja una fila dentro de una columna para comparar educación con IQ fijo. Al pasar de una columna a otra manteniendo la fila, cambia el IQ y se conserva la educación. El gráfico usa esos cuatro valores como las esquinas de un tramo del plano.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
  educ  IQ salario_predicho
1   12  90         838.2177
2   13  90         880.2753
3   12 100         889.5973
4   13 100         931.6549
         [,1]     [,2]
[1,] 838.2177 889.5973
[2,] 880.2753 931.6549
```

</details>

### Comprueba lo aprendido

¿Qué celdas comparas para medir el cambio de 12 a 13 años con IQ = 100?

<details><summary>Mostrar respuesta</summary>

Las celdas [1, 2] y [2, 2]. Ambas están en la segunda columna, que corresponde a IQ = 100.

</details>

## 07 · ANOVA interactiva del modelo de salario

La tabla muestra cuánto disminuye la suma de residuos al cuadrado al incorporar educación e IQ. Cambia el orden de entrada para comparar cómo se reparte la variación explicada.

### En R · Tu turno

### El código, paso a paso

**`anova(multiple)`**

Con un solo modelo, anova() construye una tabla secuencial. La fila educ mide la reducción de la suma de cuadrados residual al pasar del intercepto solo a educación. La fila IQ mide la reducción adicional al agregar IQ.

**`Df, Sum Sq y Mean Sq`**

Df cuenta grados de libertad. Sum Sq muestra la suma de cuadrados asociada a cada fila. Mean Sq divide esa suma por sus grados de libertad. Residuals muestra la variación que queda tras ajustar ambos regresores.

**`F value y Pr(>F)`**

Para cada término, F divide su cuadrado medio por el cuadrado medio residual del modelo completo. Pr(>F) es el valor p de esa prueba secuencial.

**`lm(wage ~ IQ + educ, data = datos)`**

Invierte el orden de entrada. Conserva los regresores y los valores ajustados. Cambia cuánto se atribuye a cada variable al entrar primero o segundo.

```r
# Modelo solicitado. Educación entra primero e IQ después.
multiple <- lm(wage ~ educ + IQ, data = datos)
anova_wage <- anova(multiple)
print(anova_wage)

# Mismos regresores con el orden invertido
multiple_iq_primero <- lm(wage ~ IQ + educ, data = datos)
anova_wage_invertida <- anova(multiple_iq_primero)
print(anova_wage_invertida)
```

### Cómo leer el resultado

Con educación primero, la fila IQ responde cuánto aporta IQ después de incluir educación. Para leer el aporte de educación después de IQ, usa el orden invertido. En ambos órdenes se conserva la suma de cuadrados residual del modelo completo.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
educ        1  16340645 16340645 115.135 < 2.2e-16 ***
IQ          1   4100932  4100932  28.895  9.66e-08 ***
Residuals 932 132274591   141926
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
IQ          1  14589783 14589783 102.799 < 2.2e-16 ***
educ        1   5851794  5851794  41.231 2.152e-10 ***
Residuals 932 132274591   141926
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

</details>

### Comprueba lo aprendido

¿Qué fila muestra el aporte de IQ una vez incluida educación?

<details><summary>Mostrar respuesta</summary>

La fila IQ de la tabla con educación primero.

</details>

## 08 · MCO: elegir el plano que reduce los residuos

En el modelo múltiple elegimos tres coeficientes para minimizar la suma de residuos al cuadrado. La ilustración usa los cinco datos de la cátedra para poder seguir cada observación.

$$\min_{b_0,b_1,b_2}\sum_i(y_i-b_0-b_1x_{i1}-b_2x_{i2})^2$$

### En R · Tu turno

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

## 09 · Construir X, y y el vector de parámetros

Ejecuta el bloque completo para crear la tabla de cinco personas, ajustar el modelo y obtener sus coeficientes y predicciones. Después examina la matriz X y el vector y que corresponden al mismo ajuste.

$$y=X\beta+u,\quad X:\ n\times(k+1),\quad\beta:\ (k+1)\times1$$

```r
# Cinco observaciones del ejemplo
ejemplo <- data.frame(
  persona = c("Juan", "Pedro", "Sofía", "Caro", "Alex"),
  experiencia = c(12, 18, 14, 12, 11),
  educacion = c(93, 119, 108, 96, 74),
  salario = c(769, 808, 825, 650, 562)
)
modelo5 <- lm(salario ~ experiencia + educacion, data = ejemplo)
print(coef(modelo5))
print(data.frame(ejemplo, prediccion = fitted(modelo5)))

# Matriz de diseño y respuesta
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

### El código, paso a paso

**`ejemplo <- data.frame(...)`**

Crea la tabla exhibida en la lámina. Cada posición de los cuatro vectores corresponde a la misma persona.

**`lm(salario ~ experiencia + educacion, data = ejemplo)`**

Ajusta el salario con intercepto, experiencia y educación. coef() muestra los tres coeficientes. fitted() devuelve las cinco predicciones para las filas de ejemplo, en su orden original.

**`model.matrix(modelo5)`**

Recibe modelo5, el objeto devuelto por lm(salario ~ experiencia + educacion, data = ejemplo). Lee la fórmula y las observaciones usadas en el ajuste. Devuelve X, una matriz numérica de 5 filas y 3 columnas. Cada fila es una persona. Las columnas son (Intercept), experiencia y educacion, en el mismo orden que coef(modelo5). La primera fila es [1, 12, 93]. El 1 multiplica al intercepto. Las otras dos entradas multiplican a sus pendientes. Salario queda en el vector y. X se usará para calcular los coeficientes con álgebra matricial y para obtener ŷ = Xβ̂.

**`cbind(unos = 1, ...)`**

Une columnas. El 1 se repite en las cinco filas al combinarse con los vectores.

**`dim(X), colnames(X) y as.vector(X)`**

dim entrega filas y columnas; colnames muestra los nombres; as.vector permite comparar los valores de ambas matrices sin sus atributos.

**`ejemplo$salario`**

El operador $ extrae una columna por nombre. Aquí devuelve el vector de salarios observados, con el mismo orden de filas de X.

**`identical(as.vector(X), as.vector(X_manual))`**

as.vector() lee los valores por columnas y elimina dimensiones y nombres. identical() exige que ambos vectores sean exactamente iguales en valores y tipo. Así comprobamos las entradas de las matrices aunque los nombres de columnas difieran.

### Cómo leer el resultado

model.matrix() construye X con los valores de los regresores que entran al ajuste. En la lámina 4, matrix() ordenó los salarios ya predichos en una cuadrícula para el gráfico. Aquí las filas son observaciones y las columnas son términos del modelo. En la rejilla de la lámina 4, las filas y columnas son valores de educación e IQ.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
(Intercept) experiencia   educacion
 140.586358  -16.789532    8.236667
  persona experiencia educacion salario prediccion
1    Juan          12        93     769   705.1220
2   Pedro          18       119     808   818.5382
3   Sofía          14       108     825   795.0930
4    Caro          12        96     650   729.8320
5    Alex          11        74     562   565.4149
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

## 10 · Transpuesta y producto matricial: t() y %*%

Selecciona una celda de XᵀX: verás qué dos columnas se multiplican y suman para obtenerla. La transpuesta convierte filas en columnas.

$$(X^\top X)_{23}=\sum_{i=1}^5x_{i1}x_{i2}$$

### En R · Tu turno

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

## 11 · Modelo completo de salario y tabla ANOVA

Recupera las 17 columnas de wage2 desde original. Para predecir wage, usa los 15 regresores disponibles y deja lwage para la exploración de correlaciones. Como lwage se calcula a partir de wage, incorporarlo usaría información de la respuesta para predecirla.

### En R · Tu turno

### El código, paso a paso

**`original[complete.cases(original), ]`**

Selecciona las filas completas en las 17 columnas. La coma seguida de un espacio vacío conserva todas las columnas. Usaremos estas mismas filas en el modelo completo, las correlaciones y el modelo reducido.

**`setdiff(names(datos_comunes), "lwage")`**

names() entrega los nombres de las columnas. setdiff() conserva los nombres del primer argumento que no están en el segundo.

**`lm(wage ~ ., data = datos_modelo)`**

El punto incluye todas las demás columnas de datos_modelo como regresores. wage queda como respuesta. lm() agrega el intercepto por defecto.

**`anova(modelo_completo)`**

Muestra grados de libertad, sumas de cuadrados, cuadrados medios, estadísticos F y valores p secuenciales. La fila Residuals corresponde al modelo con todos los regresores.

```r
# Una muestra común para todos los análisis de este tema
datos_comunes <- original[complete.cases(original), ]
campos_modelo <- setdiff(names(datos_comunes), "lwage")
datos_modelo <- datos_comunes[, campos_modelo]

modelo_completo <- lm(wage ~ ., data = datos_modelo)
print(nobs(modelo_completo))
print(anova(modelo_completo))
```

### Cómo leer el resultado

El modelo usa 663 observaciones completas y 15 regresores. Cada fila de la ANOVA mide la reducción de la suma de cuadrados residual al añadir ese término después de los anteriores. Por eso el valor p de la ANOVA secuencial puede diferir del valor p de ese coeficiente en summary().

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
[1] 663
Analysis of Variance Table

Response: wage
           Df   Sum Sq  Mean Sq F value    Pr(>F)
hours       1   127695   127695  1.0184 0.3132815
IQ          1 10486791 10486791 83.6329 < 2.2e-16 ***
KWW         1  5170696  5170696 41.2367 2.612e-10 ***
educ        1  2345638  2345638 18.7066 1.765e-05 ***
exper       1  1762013  1762013 14.0522 0.0001937 ***
tenure      1   145724   145724  1.1622 0.2814203
age         1   173557   173557  1.3841 0.2398313
married     1  1687971  1687971 13.4617 0.0002635 ***
black       1   281031   281031  2.2412 0.1348606
south       1   522399   522399  4.1662 0.0416442 *
urban       1  4214399  4214399 33.6101 1.053e-08 ***
sibs        1      364      364  0.0029 0.9570614
brthord     1   443713   443713  3.5386 0.0604034 .
meduc       1   555852   555852  4.4330 0.0356361 *
feduc       1   350897   350897  2.7984 0.0948403 .
Residuals 647 81127825   125391
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

</details>

### Comprueba lo aprendido

¿Por qué la tabla ANOVA depende del orden de los regresores?

<details><summary>Mostrar respuesta</summary>

Cada fila mide el aporte de un término después de los que lo preceden.

</details>

## 12 · Coeficientes, significancia y medidas de ajuste

Usa summary() para interpretar cada coeficiente del modelo completo. Aplica un nivel de significancia del 5 % y guarda R² y R² ajustado para comparar después.

### En R · Tu turno

### El código, paso a paso

**`summary(modelo_completo)$coefficients`**

Extrae la matriz de coeficientes. Estimate es el valor estimado. Std. Error mide su incertidumbre. t value divide la estimación por su error estándar. Pr(>|t|) es el valor p bilateral de la prueba de coeficiente cero, dado el resto de los regresores.

**`rownames(coeficientes) e ifelse(p_valores < alfa, "Sí", "No")`**

rownames() recupera el término de cada fila. ifelse() revisa la condición para cada valor p y devuelve una etiqueta por coeficiente.

**`r.squared y adj.r.squared`**

R² mide la proporción de variación muestral explicada. R² ajustado tiene en cuenta el número de regresores y observaciones. Los guardamos como números para usarlos en la lámina 14.

```r
resumen_completo <- summary(modelo_completo)
print(resumen_completo)
coeficientes <- resumen_completo$coefficients
alfa <- 0.05
p_valores <- coeficientes[, "Pr(>|t|)"]

detalle <- data.frame(
  termino = rownames(coeficientes),
  estimacion = coeficientes[, "Estimate"],
  error_estandar = coeficientes[, "Std. Error"],
  t = coeficientes[, "t value"],
  valor_p = p_valores,
  significativo = ifelse(p_valores < alfa, "Sí", "No")
)
print(detalle, row.names = FALSE)

r2_completo <- resumen_completo$r.squared
r2_ajustado_completo <- resumen_completo$adj.r.squared
print(c(R2 = r2_completo, R2_ajustado = r2_ajustado_completo))
```

### Cómo leer el resultado

Cada fila informa estimación, error estándar, estadístico t, valor p y significancia al 5 %. Entre los regresores, hours, IQ, educ, exper, married y urban cumplen p < 0,05. Para un regresor numérico, el coeficiente expresa la diferencia predicha en USD por unidad adicional con los otros campos fijos. Para un indicador, compara el valor 1 con el valor 0. El intercepto es la predicción con todos los regresores en cero.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text

Call:
lm(formula = wage ~ ., data = datos_modelo)

Residuals:
    Min      1Q  Median      3Q     Max
-812.38 -207.81  -43.22  168.91 2047.32

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) -676.890    227.469  -2.976 0.003032 **
hours         -4.391      1.953  -2.248 0.024899 *
IQ             3.089      1.235   2.501 0.012630 *
KWW            4.673      2.413   1.936 0.053293 .
educ          38.146      9.029   4.225 2.73e-05 ***
exper          9.767      4.478   2.181 0.029525 *
tenure         2.747      2.922   0.940 0.347486
age            8.865      6.035   1.469 0.142312
married      177.051     46.444   3.812 0.000151 ***
black        -96.187     56.207  -1.711 0.087503 .
south        -21.698     31.051  -0.699 0.484940
urban        178.488     31.543   5.659 2.29e-08 ***
sibs           8.509      7.952   1.070 0.285044
brthord      -17.090     11.681  -1.463 0.143951
meduc          6.839      6.227   1.098 0.272485
feduc          9.117      5.450   1.673 0.094840 .
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 354.1 on 647 degrees of freedom
Multiple R-squared:  0.2584,	Adjusted R-squared:  0.2412
F-statistic: 15.03 on 15 and 647 DF,  p-value: < 2.2e-16

     termino  estimacion error_estandar          t      valor_p significativo
 (Intercept) -676.889881     227.469009 -2.9757455 3.031810e-03            Sí
       hours   -4.390648       1.952959 -2.2482023 2.489916e-02            Sí
          IQ    3.089307       1.235228  2.5010010 1.263038e-02            Sí
         KWW    4.672608       2.413435  1.9360817 5.329292e-02            No
        educ   38.145971       9.028508  4.2250579 2.732028e-05            Sí
       exper    9.766998       4.477736  2.1812360 2.952527e-02            Sí
      tenure    2.747384       2.922248  0.9401610 3.474859e-01            No
         age    8.865405       6.034885  1.4690262 1.423117e-01            No
     married  177.051342      46.443732  3.8121688 1.509164e-04            Sí
       black  -96.186846      56.206598 -1.7113088 8.750340e-02            No
       south  -21.697682      31.050727 -0.6987818 4.849395e-01            No
       urban  178.487730      31.542872  5.6585756 2.293937e-08            Sí
        sibs    8.508701       7.952480  1.0699431 2.850439e-01            No
     brthord  -17.090091      11.681473 -1.4630083 1.439507e-01            No
       meduc    6.838524       6.226500  1.0982934 2.724849e-01            No
       feduc    9.117406       5.450224  1.6728498 9.484029e-02            No
         R2 R2_ajustado
  0.2584061   0.2412131
```

</details>

### Comprueba lo aprendido

¿Por qué un valor p mayor que 0,05 recibe la etiqueta «No»?

<details><summary>Mostrar respuesta</summary>

Con ese umbral, los datos no aportan evidencia suficiente para rechazar que el coeficiente sea cero, dado el resto del modelo.

</details>

## 13 · Correlaciones y modelo reducido

Explora las 17 columnas con pairs() y cor(). Luego filtra los regresores con p < 0,05. Entre dos regresores que pasen el filtro y tengan |r| ≥ 0,50, conserva el que tenga menor valor p en el modelo completo.

### En R · Tu turno

### El código, paso a paso

**`pairs(datos_comunes, upper.panel = NULL, ...)`**

Dibuja un gráfico por par de columnas. La diagonal indica los nombres. upper.panel = NULL oculta la mitad repetida. pch elige el símbolo y cex reduce el tamaño de los puntos.

**`cor(datos_comunes)`**

Calcula la matriz de correlaciones de Pearson. r resume dirección e intensidad de la relación lineal entre dos columnas.

**`which(upper.tri(...) & abs(...) >= 0.50, arr.ind = TRUE)`**

upper.tri() selecciona la mitad superior sin diagonal. abs() permite buscar asociaciones positivas y negativas. & combina las condiciones. which() devuelve las coordenadas de los pares que superan el umbral.

**`setdiff(significativas, "(Intercept)") y setdiff(regresores, "IQ")`**

El primer filtro retira el nombre del intercepto de la lista de regresores. El segundo aplica la decisión de conservar educación entre los dos regresores correlacionados que pasaron el filtro. El nuevo lm() usa las mismas filas.

```r
pairs(datos_comunes, upper.panel = NULL, pch = 16, cex = 0.25,
      col = "#005F9640", main = "wage2 · Matriz de gráficos de dispersión")
correlaciones <- cor(datos_comunes)
indices <- which(upper.tri(correlaciones) & abs(correlaciones) >= 0.50,
                 arr.ind = TRUE)
pares <- data.frame(
  variable_1 = rownames(correlaciones)[indices[, 1]],
  variable_2 = colnames(correlaciones)[indices[, 2]],
  r = round(correlaciones[indices], 3)
)
print(pares, row.names = FALSE)

significativas <- rownames(coeficientes)[p_valores < alfa]
regresores <- setdiff(significativas, "(Intercept)")
print(c(r_educ_IQ = correlaciones["educ", "IQ"],
        p_educ = p_valores["educ"], p_IQ = p_valores["IQ"]))

# Entre educación e IQ, educación tiene el menor valor p
elegidas <- setdiff(regresores, "IQ")
datos_reducidos <- datos_modelo[, c("wage", elegidas)]
modelo_reducido <- lm(wage ~ ., data = datos_reducidos)
print(elegidas)
print(summary(modelo_reducido))
```

### Cómo leer el resultado

Con el umbral elegido, destacan wage y lwage (r = 0,954), sibs y brthord (0,578), meduc y feduc (0,577) y educ e IQ (0,543). wage y lwage son la misma magnitud en dos escalas. Los pares familiares quedan fuera por el filtro de significancia. Entre educación e IQ, conservamos educación por su menor valor p en el modelo completo. El ajuste reducido queda con hours, educ, exper, married y urban. Esta selección sirve para explorar especificaciones y debe justificarse con el contexto y los diagnósticos.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
 variable_1 variable_2     r
         IQ       educ 0.543
       sibs    brthord 0.578
      meduc      feduc 0.577
       wage      lwage 0.954
   r_educ_IQ  p_educ.educ      p_IQ.IQ
5.434635e-01 2.732028e-05 1.263038e-02
[1] "hours"   "educ"    "exper"   "married" "urban"

Call:
lm(formula = wage ~ ., data = datos_reducidos)

Residuals:
    Min      1Q  Median      3Q     Max
-767.68 -232.16  -35.05  175.53 2025.75

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) -357.811    155.721  -2.298   0.0219 *
hours         -3.428      1.994  -1.719   0.0861 .
educ          72.641      7.159  10.146  < 2e-16 ***
exper         16.844      3.754   4.488 8.50e-06 ***
married      198.179     47.638   4.160 3.60e-05 ***
urban        185.105     31.736   5.833 8.56e-09 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 364.9 on 657 degrees of freedom
Multiple R-squared:  0.2001,	Adjusted R-squared:  0.194
F-statistic: 32.88 on 5 and 657 DF,  p-value: < 2.2e-16

```

</details>

### Comprueba lo aprendido

¿Qué regresor se conserva entre educación e IQ y con qué criterio?

<details><summary>Mostrar respuesta</summary>

Educación, porque tiene el menor valor p en el ajuste completo entre esas dos variables correlacionadas.

</details>

## 14 · Comparar R² y R² ajustado

Compara el modelo completo y el reducido sobre las mismas 663 filas y la misma variable respuesta. Revisa cuánto ajuste se pierde al retirar regresores y cómo cambia el ajuste al considerar el número de parámetros.

### En R · Tu turno

### El código, paso a paso

**`nobs() y length(coef(...)) - 1`**

nobs() cuenta las observaciones usadas. En estos ajustes de rango completo, restar uno al número de coeficientes deja el número de regresores sin el intercepto.

**`data.frame(modelo = ..., R2 = ..., R2_ajustado = ...)`**

Reúne las medidas guardadas en una fila por modelo y muestra el tamaño de muestra para verificar la comparabilidad.

```r
resumen_reducido <- summary(modelo_reducido)
r2_reducido <- resumen_reducido$r.squared
r2_ajustado_reducido <- resumen_reducido$adj.r.squared

comparacion_ajuste <- data.frame(
  modelo = c("Completo", "Reducido"),
  observaciones = c(nobs(modelo_completo), nobs(modelo_reducido)),
  regresores = c(length(coef(modelo_completo)), length(coef(modelo_reducido))) - 1,
  R2 = c(r2_completo, r2_reducido),
  R2_ajustado = c(r2_ajustado_completo, r2_ajustado_reducido)
)
print(comparacion_ajuste, row.names = FALSE)
```

### Cómo leer el resultado

El modelo completo obtiene R² de 25,84 % y R² ajustado de 24,12 %. El reducido obtiene 20,01 % y 19,40 %, respectivamente. En esta muestra, el modelo completo conserva un mayor ajuste incluso después de considerar el número de regresores. El reducido usa 5 regresores frente a 15. Completa la comparación con una revisión de los residuos y del propósito del modelo.

<details><summary>Resultados de referencia ejecutados en R</summary>

```text
   modelo observaciones regresores        R2 R2_ajustado
 Completo           663         15 0.2584061   0.2412131
 Reducido           663          5 0.2001345   0.1940473
```

</details>

### Comprueba lo aprendido

¿Qué condición hace comparable el R² de estos dos modelos?

<details><summary>Mostrar respuesta</summary>

Los dos ajustes usan la misma respuesta y las mismas observaciones.

</details>

## 15 · Ejercicio en clase

Abre un Google Colab nuevo y selecciona un entorno con R. Copia este código y ejecútalo para cargar la base.

```r
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos_ejercicio <- wooldridge::gpa2
```

gpa2 reúne 4.137 estudiantes de una universidad. Cada fila representa a un estudiante. La variable dependiente del ejercicio es colgpa, el promedio de notas universitario al finalizar el semestre de otoño.

| Campo | Significado |
|---|---|
| `sat` | Puntaje total en la prueba SAT. |
| `tothrs` | Créditos acumulados hasta el semestre de otoño. |
| `colgpa` | Promedio de notas universitario al final del semestre de otoño. |
| `athlete` | Indicador de participación deportiva. |
| `verbmath` | Razón entre el puntaje verbal y matemático del SAT. |
| `hsize` | Tamaño de la generación de egreso de secundaria, en centenas de estudiantes. |
| `hsrank` | Posición del estudiante en su generación de secundaria. |
| `hsperc` | Percentil de secundaria medido desde los primeros puestos. |
| `female` | Indicador registrado para mujeres. |
| `white` | Indicador registrado para estudiantes blancos. |
| `black` | Indicador registrado para estudiantes negros. |
| `hsizesq` | Cuadrado de hsize. |

[Documentación del conjunto de datos](https://justinmshea.github.io/wooldridge/reference/gpa2.html)

### Actividades

1. Haz un histograma de colgpa y otro de su logaritmo natural. Para el logaritmo usa los valores estrictamente positivos y reporta cuántos excluiste.
2. Ajusta una regresión lineal con colgpa como respuesta y todas las demás variables como regresores.
3. Construye la matriz de correlaciones de todas las variables e identifica los pares con mayor correlación absoluta.
4. Elige y justifica los regresores de un modelo alternativo. Revisa si los residuos respaldan la forma lineal y la varianza constante. Examina la colinealidad y explica qué información necesitarías para evaluar independencia y exogeneidad.

### Mensaje final

Justifica las variables que conservas y describe qué diagnóstico usarías para evaluar cada supuesto del modelo.
