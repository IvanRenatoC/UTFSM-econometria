# Clase 3 · Causalidad y variable omitida en R

Taller práctico de la cátedra 3: de la comparación de promedios a la selección, la aleatorización y los controles.

Docente: Iván Canales

Ejecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.

## Agenda

- 18:50–19:00: Tema 1 · Asociación y contrafactual
- 19:00–19:20: Tema 2 · Resultados potenciales, ATE y ATT
- 19:20–19:40: Tema 3 · Selección y alarmas
- 19:40–20:00: Tema 4 · Aleatorización y repetición
- 20:00–20:15: Descanso
- 20:15–20:35: Tema 5 · Variable omitida y regresión auxiliar
- 20:35–20:45: Tema 6 · Signo del sesgo
- 20:45–21:00: Tema 7 · Controles: fumar y edad
- 21:00–21:10: Tema 8 · Variables irrelevantes
- 21:10–21:25: Práctica guiada con wage2 y cierre

## Parte 1 · Causalidad y selección · Comparar personas no es observar contrafactuales

### De la asociación al problema causal

Retomemos el taller 2: wage1 contiene 526 personas de Estados Unidos (CPS 1976). wage mide salario por hora en USD de 1976; educ, años de educación. ¿La pendiente positiva permite afirmar que estudiar causa ese aumento salarial? Primero describe la nube; luego distingue asociación y causalidad.

**Referencia en la cátedra:** Tema 1 · Esperanza condicional versus causalidad y contrafactual

```r
# Ejecuta primero esta celda en Colab con kernel R.
if (file.exists("datos/wage1.csv")) {
  salarios <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  salarios <- wooldridge::wage1
}
head(salarios[, c("wage", "educ")])
modelo_asociacion <- lm(wage ~ educ, data = salarios)
print(coef(modelo_asociacion))
plot(wage ~ educ, data = salarios, pch = 19, col = "#005E9060",
     main = "Educación y salario: una asociación",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_asociacion, col = "#D6A600", lwd = 3)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)        educ
 -0.9048516   0.5413593
```

**El código, paso a paso**

**lm(wage ~ educ, data = salarios)**

Es el ajuste de la clase anterior. E[Y | X] resume diferencias entre personas observadas; no equivale automáticamente a comparar a una persona consigo misma en dos mundos.

**El contrafactual**

No es simplemente el salario pasado ni el promedio de otra persona. Es el resultado que esa misma persona habría obtenido bajo la alternativa que no ocurrió.

**Lectura del resultado:** La pendiente es aproximadamente 0.541 USD/h por año de educación. Describe una asociación promedio. No conocemos el salario que habría recibido la misma persona con otra educación: ese resultado alternativo es su contrafactual. Habilidad, oportunidades y recursos previos pueden relacionarse con ambas variables.

### Resultados potenciales: solo observamos un mundo

Usaremos las cinco personas del ejemplo de la cátedra. T = 1 indica tratamiento y T = 0, control. Y_NT es el resultado sin tratamiento; Y_T, con tratamiento. Los resultados contrafactuales que revelaremos son inventados con fines didácticos: no son salarios observados ni imputaciones de una base real.

**Referencia en la cátedra:** Tema 2 · Marco de Rubin y resultados observados/no observados

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y_NT = c(75, 40, 60, 20, 45),
  Y_T = c(100, 55, 80, 30, 60)
)
personas$Y <- ifelse(personas$T == 1, personas$Y_T, personas$Y_NT)
observado <- personas[, c("nombre", "T", "Y")]
print(observado)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
    nombre T   Y
1    Sofía 1 100
2    Paula 0  40
3 Ezequiel 1  80
4     Juan 0  20
5     Caro 1  60
```

**El código, paso a paso**

**data.frame(...)**

Construye una tabla: cada vector es una columna y cada fila es una persona. Todas las columnas deben tener la misma cantidad de valores.

**ifelse(condición, valor_si_verdadero, valor_si_falso)**

Evalúa cada posición. Si T == 1, toma Y_T; en caso contrario, toma Y_NT. A diferencia de if, actúa sobre un vector completo.

**personas[, c("nombre", "T", "Y")]**

Antes de la coma se seleccionan filas; después, columnas. Dejar el primer espacio vacío conserva todas las filas.

**Lectura del resultado:** ifelse() selecciona el resultado del estado realmente asignado a cada persona. En datos reales no disponemos de ambas columnas potenciales; aquí las conocemos porque construimos el ejemplo. Las unidades del resultado son artificiales.

### ATE y ATT: promediar efectos diferentes

En este mundo construido podemos calcular el efecto individual Y_T − Y_NT. Primero predice si ATE y ATT serán iguales. Después cambia solo el resultado potencial tratado de Juan: ¿cuál de los dos promedios debería cambiar?

**Referencia en la cátedra:** Tema 2 · ATE y ATT

```r
personas$efecto <- personas$Y_T - personas$Y_NT
ATE <- mean(personas$efecto)
ATT <- mean(personas$efecto[personas$T == 1])
print(personas[, c("nombre", "T", "efecto")])
print(c(ATE = ATE, ATT = ATT))

# Reto: Juan no pertenece al grupo tratado.
alternativa <- personas
alternativa$Y_T[alternativa$nombre == "Juan"] <- 60
alternativa$efecto <- alternativa$Y_T - alternativa$Y_NT
print(c(ATE = mean(alternativa$efecto),
        ATT = mean(alternativa$efecto[alternativa$T == 1])))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
    nombre T efecto
1    Sofía 1     25
2    Paula 0     15
3 Ezequiel 1     20
4     Juan 0     10
5     Caro 1     15
ATE ATT
 17  20
ATE ATT
 23  20
```

**El código, paso a paso**

**efecto[personas$T == 1]**

Filtra el vector de efectos y conserva solo a los tratados. mean() sobre el vector completo calcula ATE; sobre este subconjunto, ATT.

**alternativa <- personas**

Permite hacer el reto sobre otra tabla y conservar personas para las actividades siguientes.

**Lectura del resultado:** En la tabla original, ATE = 17 y ATT = 20. Son promedios de esta población didáctica de cinco personas. Al cambiar Y_T de Juan, ATE pasa a 23 y ATT sigue en 20: Juan no está entre los tratados. En una población real estos efectos no se calculan directamente porque faltan los contrafactuales.

### Diferencia observada = ATT + selección

Compara los promedios que sí observaríamos y separa la diferencia en dos componentes. ¿Cuánto de la brecha habría existido aunque nadie hubiera recibido tratamiento? La regresión con T binaria calcula la misma diferencia de promedios.

**Referencia en la cátedra:** Tema 3 · ATT y sesgo de selección

```r
tratados <- personas$T == 1
brecha <- mean(personas$Y[tratados]) - mean(personas$Y[!tratados])
ATT <- mean(personas$efecto[tratados])
seleccion <- mean(personas$Y_NT[tratados]) - mean(personas$Y_NT[!tratados])
print(c(brecha = brecha, ATT = ATT, seleccion = seleccion,
        suma = ATT + seleccion))
modelo_T <- lm(Y ~ T, data = personas)
print(coef(modelo_T))
barplot(c(ATT = ATT, Seleccion = seleccion),
        col = c("#005E90", "#D6A600"),
        ylab = "Unidades artificiales del resultado")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
   brecha       ATT seleccion      suma
       50        20        30        50
(Intercept)           T
         30          50
```

**El código, paso a paso**

**!tratados**

El signo ! invierte una condición lógica: selecciona a quienes no recibieron tratamiento. No resta valores.

**lm(Y ~ T)**

Cuando T es 0/1 y se incluye intercepto, la pendiente equivale a la media de Y en T = 1 menos la media en T = 0. No corrige por selección.

**Lectura del resultado:** La brecha observada es 50: ATT = 20 más selección = 30. Incluso sin tratamiento, los tratados tendrían un resultado medio 30 unidades mayor. El intercepto de lm(Y ~ T) es 30 y su pendiente es 50. Esa pendiente no es el efecto causal de 20.

### Alarmas: una comparación que puede engañar

El ejemplo de las alarmas de la cátedra permite invertir la intuición. Construiremos dos grupos de casas: las de mayor riesgo instalan alarma. Los valores siguientes son tasas hipotéticas por 100 casas; no son datos de delitos reales.

**Referencia en la cátedra:** Tema 3 · Ejemplo de las alarmas

```r
casas <- data.frame(
  grupo = c("Instalan alarma", "No instalan"),
  robos_sin_alarma = c(12, 4),
  efecto_alarma = c(-5, -2),
  T = c(1, 0)
)
casas$robos_con_alarma <- casas$robos_sin_alarma + casas$efecto_alarma
casas$observado <- ifelse(casas$T == 1,
                         casas$robos_con_alarma, casas$robos_sin_alarma)
print(casas)
print(c(brecha = 7 - 4, ATT = -5, seleccion = 12 - 4))
barplot(casas$observado, names.arg = casas$grupo,
        col = c("#005E90", "#D6A600"),
        ylab = "Robos por cada 100 casas (ejemplo hipotético)")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
            grupo robos_sin_alarma efecto_alarma T robos_con_alarma observado
1 Instalan alarma               12            -5 1                7         7
2     No instalan                4            -2 0                2         4
   brecha       ATT seleccion
        3        -5         8
```

**El código, paso a paso**

**Tasas y efecto**

El efecto se expresa en puntos de la tasa: 12 − 5 = 7 robos por 100 casas. No significa una reducción de 5 % relativa.

**Lectura del resultado:** Observamos 7 frente a 4 robos por 100 casas: brecha = +3. Sin alarma, las casas que la instalaron habrían tenido 12: selección = +8. El efecto en ellas es −5; por tanto, +3 = −5 + 8. Una brecha positiva no demuestra que la alarma aumente los robos.

### Autoselección frente a asignación aleatoria

Construye una población simulada en la que el tratamiento suma exactamente 10 unidades. En un escenario participan quienes tienen mayor habilidad; en otro se sortea el tratamiento. La población y los resultados potenciales permanecen iguales: solo cambia la asignación.

**Referencia en la cátedra:** Tema 4 · Aleatorización

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
T_auto <- as.numeric(habilidad > 0)
T_azar <- sample(c(rep(1, n / 2), rep(0, n / 2)))
Y_auto <- ifelse(T_auto == 1, Y_T, Y_NT)
Y_azar <- ifelse(T_azar == 1, Y_T, Y_NT)
print(coef(lm(Y_auto ~ T_auto)))
print(coef(lm(Y_azar ~ T_azar)))
print(aggregate(habilidad, list(T = T_azar), mean))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)      T_auto
   88.15001    33.52474
(Intercept)      T_azar
   99.59459    10.96493
  T           x
1 0 0.005629664
2 1 0.021903777
```

**El código, paso a paso**

**set.seed(2026)**

Fija el estado del generador para repetir el ejemplo. 2026 es una elección arbitraria; otra semilla produce otro sorteo.

**rnorm(n, mean = 0, sd = 1)**

Genera n valores de una distribución normal. sd mide dispersión; las variables son simuladas, no mediciones de personas reales.

**as.numeric(habilidad > 0)**

Convierte TRUE en 1 y FALSE en 0. La selección por habilidad es deliberada y no es aleatoria.

**sample(c(rep(1, n / 2), rep(0, n / 2)))**

Mezcla sin reemplazo 500 unos y 500 ceros. Todos tienen la misma probabilidad de ser tratados.

**Lectura del resultado:** En la simulación el ATE y el ATT verdaderos son 10. La autoselección mezcla tratamiento y habilidad. El sorteo hace comparables los grupos en promedio sobre las asignaciones, pero una muestra puede conservar desequilibrios. No garantiza que cada estimación sea exactamente 10. En el sorteo ilustrado, usa los valores calculados que muestra la botonera para comparar los dos escenarios.

### Un sorteo no elimina el ruido muestral

Repite 200 asignaciones aleatorias sobre la misma población de la lámina anterior. En cada una calcula la diferencia de promedios. ¿Las estimaciones se concentran alrededor de 10? Esta es una demostración guiada; no hace falta transcribir las 200 repeticiones.

**Referencia en la cátedra:** Tema 4 · Aleatorización y variabilidad de muestras

```r
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(c(promedio = mean(estimaciones), dispersion = sd(estimaciones)))
hist(estimaciones, col = "#005E90", border = "white",
     main = "200 sorteos sobre la misma población",
     xlab = "Diferencia de promedios estimada")
abline(v = 10, col = "#D6A600", lwd = 3)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  promedio dispersion
  9.892482   1.050358
```

**El código, paso a paso**

**numeric(200) y for**

Reserva un vector; el ciclo guarda una estimación por posición. Reutiliza lo aprendido en el taller 1.

**seq_along(estimaciones)**

Produce los índices válidos del vector. Así el ciclo se adapta si cambias la cantidad de repeticiones.

**sd(estimaciones)**

Mide cuánto varían las estimaciones entre sorteos. No es el efecto del tratamiento.

**Lectura del resultado:** La referencia dorada es el efecto verdadero de 10 unidades. Las estimaciones fluctúan alrededor de él. Aleatorizar elimina el sesgo sistemático en el diseño; no borra la variabilidad de una asignación concreta ni revela el contrafactual individual.

## Parte 2 · Variable omitida · Entender qué captura una pendiente

### Variable omitida: construir un sesgo conocido

Pasamos de selección a omisión. Simula el modelo y = 1 + 2x1 + 3x2 + u, con x2 = 0.5x1 + v. x2 influye en y y se relaciona con x1. Antes de estimar, predice la pendiente del modelo que omite x2: 2 + 3 × 0.5 = 3.5.

**Referencia en la cátedra:** Tema 5 · De la selección a la variable omitida

```r
set.seed(3)
n_ov <- 250
x1 <- rnorm(n_ov)
v <- rnorm(n_ov)
u <- rnorm(n_ov)
x2 <- 0.5 * x1 + v
y <- 1 + 2 * x1 + 3 * x2 + u
sim_ov <- data.frame(x1, x2, y)
corta <- lm(y ~ x1, data = sim_ov)
larga <- lm(y ~ x1 + x2, data = sim_ov)
print(coef(corta))
print(coef(larga))
plot(y ~ x1, data = sim_ov, pch = 19, col = "#005E9060")
abline(corta, col = "#D6A600", lwd = 3)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)          x1
   1.089019    3.157912
(Intercept)          x1          x2
  0.8759587   1.9975200   2.9637812
```

**El código, paso a paso**

**lm(y ~ x1 + x2, data = sim_ov)**

El signo + añade x2 como control, no suma ambas columnas antes de estimar. El coeficiente de x1 representa su asociación con y manteniendo x2 constante dentro de este modelo.

**corta y larga**

Son nombres que elegimos para guardar dos ajustes. Un R² más alto del modelo largo no prueba por sí mismo que hayamos identificado causalidad.

**Lectura del resultado:** El coeficiente corto suele acercarse a 3.5 y el de x1 en el modelo con control, a 2; no serán idénticos a los valores poblacionales en cada muestra. Omitir x2 traslada su componente relacionado con x1 a la pendiente corta. Este efecto causal es conocido solo porque definimos el mecanismo de la simulación.

### Comprobar la fórmula con tres regresiones

La teoría propone una regresión corta, una con control y otra auxiliar. Comprueba la identidad con coeficientes estimados sobre las mismas 250 observaciones. Distingue esta igualdad algebraica de la aproximación a los parámetros verdaderos.

**Referencia en la cátedra:** Tema 5 · Regresión auxiliar y fórmula del sesgo

```r
auxiliar <- lm(x2 ~ x1, data = sim_ov)
b_corta <- unname(coef(corta)["x1"])
b1 <- unname(coef(larga)["x1"])
b2 <- unname(coef(larga)["x2"])
delta1 <- unname(coef(auxiliar)["x1"])
print(c(pendiente_corta = b_corta,
        b1_mas_b2_delta = b1 + b2 * delta1,
        cambio_por_omitir = b2 * delta1))
print(all.equal(b_corta, b1 + b2 * delta1))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  pendiente_corta   b1_mas_b2_delta cambio_por_omitir
         3.157912          3.157912          1.160392
[1] TRUE
```

**El código, paso a paso**

**coef(larga)["x2"]**

Extrae el coeficiente por su nombre. Evita confundir el intercepto con la pendiente o depender del orden de columnas.

**unname(...)**

Quita el nombre del número extraído. No cambia su valor y permite comparar números sin diferencias de etiquetas.

**all.equal(a, b)**

Comprueba igualdad numérica con tolerancia al redondeo. Un TRUE confirma la identidad calculada; no valida un supuesto causal.

**Lectura del resultado:** Con intercepto y las mismas filas, b_corta = b1 + b2 × delta1, salvo redondeo de la computadora. El producto estimado mide la diferencia entre pendientes corta y larga. Llamarlo sesgo causal requiere que el modelo largo cumpla los supuestos necesarios; en la simulación conocemos el modelo generador.

### Predecir el signo: cuatro combinaciones

Usa las mismas x1, v y u para cambiar únicamente delta1 y beta2. En cada caso, predice si omitir x2 sube o baja la pendiente respecto del efecto verdadero 2. Después añade un caso con delta1 = 0.

**Referencia en la cátedra:** Tema 6 · El signo del sesgo

```r
casos <- data.frame(delta1 = c(0.8, -0.8, -0.8, 0.8, 0),
                    beta2 = c(2, -2, 2, -2, 2))
casos$sesgo_teorico <- casos$delta1 * casos$beta2
casos$pendiente_estimada <- numeric(nrow(casos))
for (j in seq_len(nrow(casos))) {
  x2_j <- casos$delta1[j] * x1 + v
  y_j <- 1 + 2 * x1 + casos$beta2[j] * x2_j + u
  casos$pendiente_estimada[j] <- coef(lm(y_j ~ x1))["x1"]
}
print(casos)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  delta1 beta2 sesgo_teorico pendiente_estimada
1    0.8     2           1.6          3.3663876
2   -0.8    -2           1.6          3.8002913
3   -0.8     2          -1.6          0.1663876
4    0.8    -2          -1.6          0.6002913
5    0.0     2           0.0          1.7663876
```

**El código, paso a paso**

**seq_len(nrow(casos))**

nrow() cuenta filas; seq_len() genera 1, 2, … hasta ese número. Cada vuelta estima uno de los escenarios de la tabla.

**casos$pendiente_estimada[j] <- ...**

Almacena la pendiente del escenario j. Cambiar el signo de la omitida no cambia el efecto directo que fijamos en 2.

**Lectura del resultado:** Dos signos iguales producen un sesgo poblacional positivo; signos distintos, uno negativo. Si beta2 o delta1 es cero, el sesgo poblacional por esta omisión es cero. Aun así, la estimación de una muestra puede diferir de 2 por variación muestral.

### Fumar y edad: una pendiente que cambia de signo

Reproduce el mecanismo didáctico de la cátedra: en la simulación las personas mayores fuman menos, y la edad aumenta el resultado Y. Y es un índice artificial, no una probabilidad de muerte. No usaremos esta simulación como evidencia médica ni como reproducción exacta del estudio citado.

**Referencia en la cátedra:** Tema 7 · Controles: fumar y edad

```r
set.seed(2026)
fumar_datos <- data.frame(edad = runif(100, min = 20, max = 80))
fumar_datos$fumar <- 30 - 0.3 * fumar_datos$edad + rnorm(100, sd = 2.3)
fumar_datos$Y <- 13 + 0.94 * fumar_datos$fumar +
                0.98 * fumar_datos$edad + rnorm(100)
sin_edad <- lm(Y ~ fumar, data = fumar_datos)
con_edad <- lm(Y ~ fumar + edad, data = fumar_datos)
print(coef(sin_edad))
print(coef(con_edad))
plot(Y ~ fumar, data = fumar_datos, pch = 19,
     col = ifelse(fumar_datos$edad > 50, "#D6A600", "#005E90"),
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
abline(sin_edad, col = "#1B2A5E", lwd = 3)
legend("topright", c("Edad > 50", "Edad <= 50"),
       col = c("#D6A600", "#005E90"), pch = 19)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)       fumar
 103.104478   -1.814066
(Intercept)       fumar        edad
 13.1460302   0.9465336   0.9772352
```

**El código, paso a paso**

**runif(100, min = 20, max = 80)**

Genera 100 edades simuladas entre 20 y 80. min y max son los límites, no la media y la desviación.

**col = ifelse(edad > 50, ... , ...)**

Colorea cada punto según su grupo de edad. Los colores ayudan a reconocer la variable que estaba oculta en la primera regresión.

**Lectura del resultado:** La nube agregada puede tener pendiente negativa, aunque el efecto de fumar fijado en el mecanismo sea positivo (+0.94). La edad genera un sesgo negativo porque aumenta Y y se relaciona negativamente con fumar. Ajustar por edad cambia la comparación; no significa que el efecto poblacional haya cambiado.

### Comparar manteniendo la edad fija

Usa el modelo con edad para dibujar dos líneas ajustadas: una a los 30 años y otra a los 60. Son comparaciones del modelo a una edad fija, no dos nuevas regresiones ni nuevas observaciones. Explica por qué no debemos conectar todos los puntos como una serie temporal.

**Referencia en la cátedra:** Tema 7 · Soluciones mediante controles

```r
grid_fumar <- seq(min(fumar_datos$fumar), max(fumar_datos$fumar), length.out = 50)
a30 <- data.frame(fumar = grid_fumar, edad = 30)
a60 <- data.frame(fumar = grid_fumar, edad = 60)
plot(Y ~ fumar, data = fumar_datos, pch = 19, col = "#005E9040",
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
lines(grid_fumar, predict(con_edad, newdata = a30), col = "#005E90", lwd = 3)
lines(grid_fumar, predict(con_edad, newdata = a60), col = "#D6A600", lwd = 3)
legend("topright", c("Edad fija: 30", "Edad fija: 60"),
       col = c("#005E90", "#D6A600"), lwd = 3)
print(summary(con_edad))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text

Call:
lm(formula = Y ~ fumar + edad, data = fumar_datos)

Residuals:
     Min       1Q   Median       3Q      Max
-2.70738 -0.60540  0.01779  0.56642  2.11791

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 13.14603    1.15783   11.35   <2e-16 ***
fumar        0.94653    0.03830   24.71   <2e-16 ***
edad         0.97724    0.01224   79.85   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.9187 on 97 degrees of freedom
Multiple R-squared:  0.9948,	Adjusted R-squared:  0.9947
F-statistic:  9250 on 2 and 97 DF,  p-value: < 2.2e-16

```

**El código, paso a paso**

**seq(..., length.out = 50)**

Genera 50 puntos ordenados entre dos límites; sirve para dibujar una línea continua. No son 50 personas nuevas.

**predict(con_edad, newdata = a30)**

Ya vimos predict() en el taller 2. newdata incluye ahora ambas columnas que necesita el modelo: fumar y edad.

**lines(x, y, col = ..., lwd = ...)**

Añade puntos unidos por segmentos sobre un gráfico ya creado. A diferencia de abline(), permite dibujar predicciones calculadas en una rejilla.

**Lectura del resultado:** Las dos líneas tienen la misma pendiente de fumar porque este modelo es aditivo y no incluye interacción. Su separación refleja el coeficiente de edad. Las combinaciones extremas pueden estar poco respaldadas por la muestra: fijar una edad no crea observaciones. Controlar corrige la omisión en este mecanismo conocido, no en cualquier base real.

### ¿Más controles siempre es mejor?

En una simulación repetida, x3 se relaciona con x1 pero no forma parte del modelo verdadero de Y. Compara 200 pendientes con y sin ese control. No confundas una variable irrelevante con una variable omitida que sí afecta al resultado.

**Referencia en la cátedra:** Tema 8 · Variables irrelevantes y conclusiones

```r
set.seed(10)
pendientes <- matrix(0, nrow = 200, ncol = 2)
colnames(pendientes) <- c("Sin x3", "Con x3")
for (b in seq_len(nrow(pendientes))) {
  a <- rnorm(80)
  x3 <- 0.9 * a + rnorm(80, sd = 0.45)
  resultado <- 1 + 2 * a + rnorm(80)
  pendientes[b, 1] <- coef(lm(resultado ~ a))["a"]
  pendientes[b, 2] <- coef(lm(resultado ~ a + x3))["a"]
}
print(colMeans(pendientes))
print(apply(pendientes, 2, sd))
boxplot(pendientes, col = c("#005E90", "#D6A600"),
        ylab = "Pendiente estimada", main = "200 muestras simuladas")
abline(h = 2, lty = 2)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  Sin x3   Con x3
1.998904 1.993283
   Sin x3    Con x3
0.1047310 0.2606908
```

**El código, paso a paso**

**colMeans(pendientes)**

Calcula una media por columna de la matriz: aquí, el promedio de las pendientes de cada modelo.

**apply(pendientes, 2, sd)**

Aplica sd a cada columna (2). Con 1 operaría por filas. Resume la dispersión entre muestras de cada estimador.

**boxplot(pendientes)**

Compara las distribuciones de ambas columnas. La referencia horizontal 2 es el efecto definido en la simulación.

**Lectura del resultado:** Ambos promedios se aproximan a 2, pero el ajuste con x3 muestra mayor dispersión en este diseño: el control irrelevante está correlacionado con a. Añadir un predictor que sí explica Y puede mejorar precisión; aumentar R² o la cantidad de columnas no es una regla para identificar efectos causales.

## Parte 3 · Práctica guiada · Aplicar controles a datos reales

### Ejercicio guiado: educación, salario e IQ

Ahora trabaja con wage2 de Wooldridge: 935 observaciones del año 1980. wage registra ingresos mensuales (dólares), educ años de educación e IQ una puntuación de test. No confundas este wage mensual con el salario por hora de wage1. IQ es una medida imperfecta; agregarla no garantiza identificar el efecto causal de la educación.

**Referencia en la cátedra:** Aplicación práctica de los temas 5–8 · Datos reales de Wooldridge

**Ejercicio guiado**

**1. Carga y describe los datos**

Ejecuta el bloque de carga; luego identifica cuántas filas quedan y las unidades de las tres variables.

**2. Antes de ajustar**

Dibuja salario frente a educación y calcula cor(trabajo). Predice qué podría ocurrir al añadir IQ sin suponer que observas la habilidad completa.

**complete.cases(...)**

Devuelve TRUE para filas sin valores faltantes en las columnas seleccionadas. Aplicamos el mismo filtro antes de estimar ambos modelos; no debemos comparar pendientes calculadas sobre muestras distintas.

**Preparar los datos: ejecuta sólo este bloque**

```r
# Carga independiente: puedes copiar esta celda directamente en Colab.
if (file.exists("datos/wage2.csv")) {
  trabajo <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  trabajo <- wooldridge::wage2
}
# Mantén las mismas filas al comparar los dos modelos.
trabajo <- trabajo[complete.cases(trabajo[, c("wage", "educ", "IQ")]),
                   c("wage", "educ", "IQ")]
head(trabajo)
print(c(filas = nrow(trabajo)))
```

La carga funciona desde esta carpeta con el CSV local y desde Colab instalando wooldridge. El filtro conserva las mismas filas en todos los ajustes.

```r
print(summary(trabajo))
print(cor(trabajo))
plot(wage ~ educ, data = trabajo, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Ingreso mensual (USD)")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
      wage             educ             IQ
 Min.   : 115.0   Min.   : 9.00   Min.   : 50.0
 1st Qu.: 669.0   1st Qu.:12.00   1st Qu.: 92.0
 Median : 905.0   Median :12.00   Median :102.0
 Mean   : 957.9   Mean   :13.47   Mean   :101.3
 3rd Qu.:1160.0   3rd Qu.:16.00   3rd Qu.:112.0
 Max.   :3078.0   Max.   :18.00   Max.   :145.0
          wage      educ        IQ
wage 1.0000000 0.3271087 0.3090878
educ 0.3271087 1.0000000 0.5156970
IQ   0.3090878 0.5156970 1.0000000
```

**Lectura del resultado:** Revisa primero unidades y filas comparables. Las correlaciones describen asociaciones lineales entre variables observadas. No vemos los salarios potenciales de una misma persona bajo diferentes niveles de educación y un test no recoge todos los factores omitidos.

### Ejercicio guiado: comparar e interpretar los modelos

Escribe primero el modelo simple y después el que incluye IQ. Obtén summary() y anova() de ambos. Compara la pendiente de educación y verifica la descomposición con IQ ~ educ. Explica qué cambia y qué conclusión causal sigue pendiente.

**Referencia en la cátedra:** Aplicación práctica · Controles y límites de una interpretación causal

**Ejercicio guiado**

**1. Dos ajustes sobre las mismas filas**

Estima wage ~ educ y wage ~ educ + IQ. En el segundo, interpreta educación manteniendo IQ constante dentro del modelo.

**2. summary() y anova()**

Lee signo, unidades y magnitud de la pendiente; distingue significancia estadística de identificación causal. En la ANOVA secuencial, la fila IQ evalúa su aporte tras educ.

**3. Regresión auxiliar**

Estima IQ ~ educ y extrae su pendiente. Multiplica por el coeficiente de IQ del modelo con control para reconstruir la diferencia entre pendientes.

```r
modelo_corto <- lm(wage ~ educ, data = trabajo)
modelo_control <- lm(wage ~ educ + IQ, data = trabajo)
print(summary(modelo_corto))
print(anova(modelo_corto))
print(summary(modelo_control))
print(anova(modelo_control))
aux_IQ <- lm(IQ ~ educ, data = trabajo)
b_educ <- unname(coef(modelo_control)["educ"])
b_IQ <- unname(coef(modelo_control)["IQ"])
delta_IQ <- unname(coef(aux_IQ)["educ"])
print(c(corta = unname(coef(modelo_corto)["educ"]),
        control = b_educ, diferencia = b_IQ * delta_IQ,
        reconstruida = b_educ + b_IQ * delta_IQ))
```

**ANOVA · Modelo simple · wage ~ educ · n = 935**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Educación | 16340645 | 1 | 16340645 | 111.79 | < 2.2e-16 |
| Residuos | 136375524 | 933 | 146169 | — | — |

**ANOVA secuencial · Con control · wage ~ educ + IQ · n = 935**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Educación primero | 16340645 | 1 | 16340645 | 115.135 | < 2.2e-16 |
| IQ después de educ | 4100932 | 1 | 4100932 | 28.895 | 9.66e-08 |
| Residuos | 132274591 | 932 | 141926 | — | — |

Sumas de cuadrados redondeadas de anova() en R. En el modelo con control, las contribuciones son secuenciales y dependen del orden de los predictores. SST = suma total; SSE = suma explicada; SSR = suma residual, como en el taller 2.

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text

Call:
lm(formula = wage ~ educ, data = trabajo)

Residuals:
    Min      1Q  Median      3Q     Max
-877.38 -268.63  -38.38  207.05 2148.26

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  146.952     77.715   1.891   0.0589 .
educ          60.214      5.695  10.573   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 382.3 on 933 degrees of freedom
Multiple R-squared:  0.107,	Adjusted R-squared:  0.106
F-statistic: 111.8 on 1 and 933 DF,  p-value: < 2.2e-16

Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
educ        1  16340645 16340645  111.79 < 2.2e-16 ***
Residuals 933 136375524   146169
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Call:
lm(formula = wage ~ educ + IQ, data = trabajo)

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
       corta      control   diferencia reconstruida
    60.21428     42.05762     18.15666     60.21428
```

**Lectura del resultado:** La pendiente simple de educación disminuye al incluir IQ en estos datos. Es una diferencia entre asociaciones estimadas; no hemos demostrado cuánto era el sesgo causal. summary() presenta coeficientes, errores estándar, pruebas t y R². anova(modelo_control) atribuye sumas de cuadrados secuencialmente: primero educ, luego IQ según la fórmula; su orden importa. Ningún p-valor comprueba ausencia de variables omitidas. En esta muestra: 60.214 USD mensuales por año de educación en el modelo simple frente a 42.058 con IQ; la diferencia es 18.157.

### Programa completo y cierre: ¿qué podemos afirmar?

Este bloque reúne toda la aplicación de wage2, desde la carga hasta la comparación. Puede ejecutarse solo en una sesión nueva de Colab con kernel R. Antes de mirar la solución, explica: ¿un cambio de pendiente prueba causalidad?, ¿una asignación aleatoria debe dar exactamente 10?, ¿más controles siempre ayuda?

**Referencia en la cátedra:** Tema 8 · Conclusiones y práctica integradora

```r
# Carga independiente: puedes copiar esta celda directamente en Colab.
if (file.exists("datos/wage2.csv")) {
  trabajo <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  trabajo <- wooldridge::wage2
}
# Mantén las mismas filas al comparar los dos modelos.
trabajo <- trabajo[complete.cases(trabajo[, c("wage", "educ", "IQ")]),
                   c("wage", "educ", "IQ")]
head(trabajo)
print(c(filas = nrow(trabajo)))
# 1. Explorar las variables y su relación.
summary(trabajo)
cor(trabajo)
plot(wage ~ educ, data = trabajo, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Ingreso mensual (USD)")
# 2. Ajustar sin control y con control por IQ.
modelo_corto <- lm(wage ~ educ, data = trabajo)
modelo_control <- lm(wage ~ educ + IQ, data = trabajo)
# 3. Leer los resultados de cada ajuste.
summary(modelo_corto)
anova(modelo_corto)
summary(modelo_control)
anova(modelo_control)
# 4. Reconstruir la pendiente corta mediante la regresión auxiliar.
aux_IQ <- lm(IQ ~ educ, data = trabajo)
b1 <- unname(coef(modelo_control)["educ"])
b2 <- unname(coef(modelo_control)["IQ"])
delta1 <- unname(coef(aux_IQ)["educ"])
print(c(corta = unname(coef(modelo_corto)["educ"]),
        control = b1, componente = b2 * delta1,
        reconstruida = b1 + b2 * delta1))
# 5. Comparar pendientes; las dos NO son efectos causales demostrados.
barplot(c(Simple = coef(modelo_corto)["educ"],
          Con_IQ = coef(modelo_control)["educ"]),
        col = c("#005E90", "#D6A600"),
        ylab = "USD mensuales por año de educación")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
filas
  935
       corta      control   componente reconstruida
    60.21428     42.05762     18.15666     60.21428
```

**El código, paso a paso**

**1. Carga reproducible**

Instala el paquete solo si hace falta, carga wage2 y selecciona las mismas columnas y filas para ambos ajustes.

**2. Explorar y ajustar**

Primero describe, luego estima y lee summary()/anova(). Una tabla de resultados no reemplaza la explicación económica.

**3. Identidad y conclusión**

Verifica la fórmula; distingue la identidad numérica de una afirmación sobre efectos causales.

**Lectura del resultado:** La regresión describe asociaciones; identificar un efecto causal exige un diseño o supuestos defendibles. Diferencia observada = ATT + selección. El signo de la omisión depende de beta2 × delta1. Los controles cambian la comparación y pueden reducir sesgo, pero no sustituyen los supuestos. Para continuar: sección 3.3 de Wooldridge y las indicaciones de la cátedra.

**Autoevaluación**

La pendiente cambia al añadir IQ. ¿Prueba que ya medimos el efecto causal?

1. Sí, porque mejora el R².
2. No: podrían quedar factores omitidos y errores de medición.
3. Sí, si el p-valor es pequeño.

Respuesta: No: podrían quedar factores omitidos y errores de medición. Correcto: controlar por una variable no asegura que el error sea independiente de educación.

¿Qué garantiza una asignación aleatoria bien implementada?

1. Un efecto estimado idéntico al verdadero en cada muestra.
2. Contrafactuales observados para todas las personas.
3. Comparabilidad en promedio sobre las asignaciones.

Respuesta: Comparabilidad en promedio sobre las asignaciones. Correcto: persiste variación muestral y cada persona sigue observada en un solo estado.
