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

[Documentación de wage2](https://justinmshea.github.io/wooldridge/reference/wage2.html)

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

## 05 · ¿Cuánto cambia el salario predicho con un año más de educación?

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

## 06 · Del modelo simple al múltiple

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

## 07 · Ceteris paribus: mover educación y dejar IQ fijo

Usa los controles para comparar salarios predichos a un IQ fijo. Después cambia IQ: se desplaza la recta condicional, pero la pendiente de educación se conserva porque este modelo no incluye interacciones.

$$\Delta\widehat{wage}=\widehat\beta_1\Delta educ\quad\text{con IQ fijo}$$

### En R · Tu turno

### El código, paso a paso

**`predict(multiple, newdata = nuevos)`**

Calcula predicciones para cada fila de nuevos. Debe contener las variables explicativas con los mismos nombres que el modelo.

**`diff(predicciones)`**

Resta valores consecutivos: aquí, la segunda predicción menos la primera.

**`seq(9, 18, length.out = 50)`**

Genera 50 valores equidistantes para dibujar una línea suave.

**`plot(x, y, type = "l")`**

Dibuja los pares de coordenadas x e y. type = "l" une los puntos en el orden del vector de educación. Aquí y son las predicciones del modelo múltiple con IQ fijo.

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

Cada fila de X representa una persona. La columna de unos permite estimar el intercepto. Recorre las filas para ver qué datos entran en cada ecuación.

$$y=X\beta+u,\quad X:\ n\times(k+1),\quad\beta:\ (k+1)\times1$$

### En R · Tu turno

### El código, paso a paso

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

model.matrix() construye X con los valores de los regresores que entran al ajuste. En la lámina 4, matrix() ordenó los salarios ya predichos en una cuadrícula para el gráfico. Aquí las filas son observaciones y las columnas son términos del modelo. En la rejilla de la lámina 4, las filas y columnas son valores de educación e IQ.

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

## 11 · Calcular los coeficientes con solve() y compararlos con lm()

Primero reproducimos la fórmula de la cátedra. Después resolvemos las ecuaciones normales sin formar explícitamente la inversa.

$$\widehat\beta=(X^\top X)^{-1}X^\top y$$

### En R · Tu turno

### El código, paso a paso

**`solve(XtX)`**

Devuelve la inversa de XtX si es invertible. Aquí permite reproducir la fórmula teórica.

**`solve(XtX, Xty)`**

Resuelve XtX · beta = Xty sin pedir una inversa explícita. No elimina los problemas de condicionamiento de las ecuaciones normales.

**`all.equal(...), as.numeric(...) e isTRUE(...)`**

as.numeric convierte a vector; all.equal compara con tolerancia numérica; isTRUE produce un único TRUE o FALSE.

**`unname(coef(modelo5))`**

Quita las etiquetas de los coeficientes para compararlos con beta_sistema convertido a vector numérico. all.equal() comprueba la igualdad aproximada e isTRUE() devuelve TRUE solo si la comprobación tiene éxito.

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

## 12 · Verificar las propiedades algebraicas de MCO

Comprueba las condiciones de primer orden con los mismos cinco datos. Son propiedades del ajuste con intercepto, no supuestos sobre la distribución del error.

$$X^\top\widehat u=0,\quad\bar y=\overline{\widehat y}$$

### En R · Tu turno

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

## 13 · Rango completo: cuándo falla la inversa

Duplica deliberadamente una columna para reconocer la colinealidad exacta. Este es un ejemplo de diagnóstico, no una instrucción para construir el modelo final.

### En R · Tu turno

### El código, paso a paso

**`qr(X_duplicada)$rank`**

Obtiene el número de columnas linealmente independientes. Debe coincidir con el número de parámetros para invertir XᵀX.

**`tryCatch(..., error = function(e) conditionMessage(e))`**

Captura el error esperado y lo muestra como texto para que el notebook continúe. e contiene la información del error.

**`coef(lm(...))`**

Una pendiente puede aparecer como NA porque es redundante; no porque haya una fila con valor faltante.

**`ncol(X_duplicada)`**

Cuenta las columnas de la matriz. Comparamos ese número con el rango que devuelve la descomposición QR.

**`ejemplo$repetida <- ejemplo$experiencia`**

Crea una columna nueva llamada repetida y le asigna los mismos valores de experiencia, fila por fila.

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

## 14 · R² y R² ajustado: comparar sobre la misma muestra

Usa la botonera para cambiar de modelo. La comparación utiliza siempre las mismas 935 personas y la misma variable dependiente.

$$R^2=1-\frac{SSR}{SST},\quad\overline R^2=1-\frac{n-1}{n-k-1}\frac{SSR}{SST}$$

### En R · Tu turno

### El código, paso a paso

**`summary(modelo)$adj.r.squared`**

Extrae el R² ajustado del resumen; r.squared entrega el R² sin penalización.

**`nobs(modelo) y length(coef(modelo)) - 1`**

nobs cuenta observaciones usadas. Restamos el intercepto para contar k en este modelo de rango completo.

**`function(modelo) y rbind(...)`**

function(modelo) { ... } define una función con un argumento llamado modelo. Cada llamada calcula cuatro medidas para el ajuste entregado y devuelve la última expresión, el vector c(...). rbind() apila los vectores resultantes como filas para comparar ambos modelos.

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

## 15 · La trampa de agregar variables de ruido

Un experimento simulado separa ajuste dentro de muestra de información real. Mueve el número de variables añadidas y observa qué medida sube o baja.

### En R · Tu turno

### El código, paso a paso

**`matrix(..., nrow = ..., ncol = ...)`**

Ordena los valores aleatorios en una matriz de 30 filas y 10 columnas.

**`ruido[, seq_len(j), drop = FALSE]`**

Conserva las primeras j columnas; drop = FALSE evita convertir la selección de una sola columna en un vector.

**`matplot(x, y, type = "l", lty = 1)`**

Dibuja una línea por columna de y. type elige líneas y lty su estilo.

**`set.seed(5) y rnorm(n_sim, sd = 2)`**

set.seed() inicia el generador en un estado reproducible. rnorm() genera n_sim valores de una distribución normal con media 0 por defecto. sd = 2 fija la desviación estándar del ruido. Al omitir sd se usa 1.

**`for (j in 0:10) y if (j == 0)`**

0:10 crea los enteros de 0 a 10. for ejecuta el bloque con cada valor de j. Para j = 0 ajustamos sin ruido. Para j > 0 añadimos las primeras j columnas de ruido. Guardamos cada resultado en la fila j + 1 porque las posiciones de R empiezan en 1. NA reserva las posiciones aún sin calcular.

**`legend("bottomright", ..., lty = 1, col = ...)`**

Agrega una leyenda en la esquina inferior derecha. El vector de textos sigue el orden de las líneas. lty = 1 indica línea continua y col asigna los colores correspondientes.

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

## 16 · Interpretar summary() y ANOVA en el ejemplo de cátedra

Abre los componentes para identificar estimaciones, incertidumbre, grados de libertad y suma de cuadrados. Aquí n = 5 y k = 2: solo quedan dos grados de libertad residuales.

### En R · Tu turno

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

## 17 · Ejercicio guiado: estimar y explicar una regresión múltiple real

Con wage2, escribe el modelo wage ~ educ + IQ. Compara los coeficientes, calcula la predicción para educ = 12 e IQ = 100 y comprueba la fórmula matricial. Intenta resolverlo antes de desplegar el código.

### En R · Tu turno

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

## 18 · Inversa por cofactores: elegir un menor

Usamos A = XᵀX del ejemplo de cinco personas. Al seleccionar una celda, se destaca la fila y columna que se eliminan para formar el menor 2 × 2.

$$C_{ij}=(-1)^{i+j}\det(A_{-i,-j})$$

### En R · Tu turno

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

## 19 · Cofactores, adjunta, determinante e inversa

Construye la matriz de cofactores mediante dos ciclos for. Luego transpón y divide por el determinante. Recorre los pasos en la animación.

$$A^{-1}=\frac{C^\top}{\det(A)}$$

### En R · Tu turno

### El código, paso a paso

**`for (i in 1:3) y for (j in 1:3)`**

Recorren las nueve celdas: una fila y, dentro de ella, las tres columnas.

**`sum(A[1, ] * cofactores[1, ])`**

Expande el determinante por la primera fila. No es la suma simple de los elementos de A.

**`adjunta / determinante`**

Divide cada elemento de la adjunta por un escalar. Solo se puede hacer si el determinante no es cero.

**`all.equal(..., check.attributes = FALSE)`**

Compara los valores de la inversa por cofactores con los de solve(A) y omite los atributos en esa comparación. La comprobación posterior A %*% inversa muestra la matriz identidad redondeada.

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

## 20 · Cerrar el recorrido: de los datos a la predicción

Ejecuta este bloque completo con los cinco datos, sin depender de variables anteriores. Reproduce el cálculo matricial, las predicciones, el resumen y la ANOVA. Después explica cada resultado con tus palabras.

### En R · Tu turno

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
