# Clase 2 · Regresión lineal simple en R

Casos prácticos con wage1: de la nube de puntos al ajuste y su interpretación.

Docente: Iván Canales

Ejecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.

## Agenda

- 18:50–19:00: Datos y entorno
- 19:00–19:15: Tres nubes y modelo con error
- 19:15–19:30: Esperanza y promedios por grupo
- 19:30–20:00: MCO y parámetros en R
- 20:00–20:15: Descanso
- 20:15–20:45: Tres regresiones e interpretación
- 20:45–21:05: Residuos, descomposición y R²
- 21:05–21:25: Actividad de comparación y cierre

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

### Tres nubes: anticipar el signo de la pendiente

Alterna entre los tres casos. Antes de mostrar la recta, predice si la tendencia es ascendente, descendente o poco marcada. Los tres usan la misma base sin alterar los datos.

```r
par(mfrow = c(1, 3))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9080")
plot(educ ~ exper, data = datos, pch = 19, col = "#005E9080")
plot(wage ~ numdep, data = datos, pch = 19, col = "#005E9080")
par(mfrow = c(1, 1))
```

**Lectura del resultado:** La tendencia describe una asociación promedio. Una nube ancha puede tener pendiente distinta de cero; una recta casi horizontal tampoco prueba independencia.

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

### Mínimos cuadrados: elegir una recta

Ajusta intercepto y pendiente para reducir la suma de residuos al cuadrado. Luego compara tu propuesta con lm(). Un residuo es y observado menos y ajustado; se eleva al cuadrado para evitar que signos opuestos se cancelen.

```r
modelo_pos <- lm(wage ~ educ, data = datos)
print(coef(modelo_pos))
print(sum(resid(modelo_pos)^2))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060")
abline(modelo_pos, col = "#D6A600", lwd = 3)
```

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

**Lectura del resultado:** Los dos métodos coinciden salvo redondeo numérico. La recta pasa por (x̄, ȳ). No confundas β₁ poblacional con b₁ estimado.

## Parte 2 · Taller · Tres casos, diagnóstico y comparación

### Caso positivo: educación y salario

Estima, dibuja e interpreta la pendiente en sus unidades. Predice para 12 y 16 años de educación. ¿Representa cada predicción el salario exacto de una persona?

```r
modelo_pos <- lm(wage ~ educ, data = datos)
summary(modelo_pos)
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)
predict(modelo_pos, newdata = data.frame(educ = c(12, 16)))
```

**Lectura del resultado:** La pendiente es aproximadamente 0.541. Las predicciones son valores medios ajustados, no salarios individuales garantizados. Factores omitidos pueden estar relacionados con educación.

### Caso negativo: experiencia potencial y educación

Ahora y es educ y x es exper. Mantén explícito este cambio: ya no estamos explicando salarios. Predice el signo antes de ejecutar.

```r
modelo_neg <- lm(educ ~ exper, data = datos)
summary(modelo_neg)
plot(educ ~ exper, data = datos, pch = 19, col = "#005E9060",
     xlab = "Experiencia potencial (años)", ylab = "Educación (años)")
abline(modelo_neg, col = "#D6A600", lwd = 3)
```

**Lectura del resultado:** b₁ ≈ −0.0611: un año adicional de experiencia potencial se asocia con 0.061 años menos de educación en promedio. La relación es débil en capacidad explicativa. Además, experiencia potencial se construye habitualmente usando edad y educación: no interpretes el resultado como que trabajar reduce la escolaridad.

### Caso sin evidencia de pendiente: dependientes y salario

Estima wage ~ numdep. Mira primero la nube, después la recta y al final el p-valor de numdep en summary(). Usa 5 % como umbral descriptivo de la decisión estadística.

```r
modelo_plano <- lm(wage ~ numdep, data = datos)
summary(modelo_plano)
confint(modelo_plano, "numdep", level = 0.95)
plot(wage ~ numdep, data = datos, pch = 19, col = "#005E9060",
     xlab = "Número de dependientes", ylab = "Salario por hora (USD de 1976)")
abline(modelo_plano, col = "#D6A600", lwd = 3)
```

**Lectura del resultado:** b₁ ≈ −0.157 y p ≈ 0.218: no rechazamos β₁ = 0 al 5 % con la inferencia clásica de summary(lm). No hemos demostrado una pendiente exactamente cero ni ausencia de toda relación. Esa inferencia requiere sus supuestos; no sirve para afirmar causalidad.

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

**Lectura del resultado:** R² = SSE/SST = 1 − SSR/SST. Un R² alto no demuestra causalidad. Educación como respuesta tiene unidades distintas del salario: compara fracciones explicadas, no las SST brutas de esos modelos.

### Tu turno: comparar y comunicar los tres casos

Completa una tabla con respuesta, predictor, signo, pendiente y R². Redacta una frase en unidades para cada caso y una limitación. Antes de abrir el código, construye la tabla usando coef() y summary().

```r
comparacion <- data.frame(
  caso = c("Salario y educación", "Educación y experiencia", "Salario y dependientes"),
  pendiente = sapply(modelos, function(m) coef(m)[2]),
  R2 = sapply(modelos, function(m) summary(m)$r.squared),
  p_pendiente = sapply(modelos, function(m) coef(summary(m))[2, 4]))
print(comparacion)
# Escribe tus conclusiones en una celda Markdown del notebook.
```

**Lectura del resultado:** Revisa dirección, unidades y dispersión alrededor de la recta. El caso no significativo no es una prueba de equivalencia a cero. Diferencia siempre asociación, predicción y causalidad.
