# Taller 2: ejecutar desde clase-2-taller/.
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

# Salario vs Educación
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9080")

# Otros gráficos:
par(mfrow = c(1, 3))
plot(wage ~ exper, data = datos, pch = 19, col = "#005E9080")
plot(wage ~ numdep, data = datos, pch = 19, col = "#005E9080")
par(mfrow = c(1, 1))

x <- datos$educ
y <- datos$wage
plot(x, y, pch = 19, col = "#005E9080",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(a = 0, b = 0.5, col = "#D6A600", lwd = 3)

promedio <- mean(datos$wage)
por_educ <- aggregate(wage ~ educ, data = datos, FUN = mean)
print(promedio)
print(por_educ)
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9040")
points(por_educ$educ, por_educ$wage, pch = 19, col = "#D6A600", cex = 1.4)
abline(h = promedio, lty = 2)

# Consultar los argumentos oficiales sin ajustar un modelo:
args(stats::lm)

# Ver la configuración actual para valores faltantes:
getOption("na.action")

modelo_pos <- lm(wage ~ educ, data = datos)
print(nobs(modelo_pos))
print(coef(modelo_pos))
print(predict(modelo_pos, newdata = data.frame(educ = c(12, 16))))
print(sum(resid(modelo_pos)^2))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)

x <- datos$educ
y <- datos$wage
b1 <- sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x))^2)
b0 <- mean(y) - b1 * mean(x)
print(c(b0 = b0, b1 = b1))
print(coef(modelo_pos))
y_ajustado <- b0 + b1 * x
residuos <- y - y_ajustado
print(head(data.frame(y, y_ajustado, residuos)))

modelo_pos <- lm(wage ~ educ, data = datos)
print(summary(modelo_pos))
print(anova(modelo_pos))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)
predict(modelo_pos, newdata = data.frame(educ = c(12, 16)))

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

# Ejecuta primero la lámina 09 para crear autos y modelo_plano.
print(summary(modelo_plano))
print(anova(modelo_plano))
print(confint(modelo_plano, "drat", level = 0.95))
plot(qsec ~ drat, data = autos, pch = 19, col = "#005E9060",
     xlab = "Relación de transmisión (sin unidades)",
     ylab = "Tiempo de 1/4 de milla (s)")
abline(modelo_plano, col = "#D6A600", lwd = 3)

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

# 1. Cargar la base del libro. En Colab se descarga el paquete si hace falta.
# La copia CSV permite trabajar sin conexión desde la carpeta del taller.
if (file.exists("datos/ceosal1.csv")) {
  datos_practica <- read.csv("datos/ceosal1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  datos_practica <- wooldridge::ceosal1
}

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
modelo_practica <- lm(salary ~ roe, data = datos_practica)
print(nobs(modelo_practica))
print(coef(modelo_practica))
print(summary(modelo_practica))
print(anova(modelo_practica))
abline(modelo_practica, col = "#D6A600", lwd = 3)

# 5. Predecir para dos empresas hipotéticas; resultados en miles de USD.
nuevos_casos <- data.frame(roe = c(10, 20))
print(data.frame(nuevos_casos,
                 salario_ajustado = predict(modelo_practica, nuevos_casos)))

# 6. Descomponer la variación usando las filas efectivas del modelo.
y_practica <- model.response(model.frame(modelo_practica))
ajustados_practica <- fitted(modelo_practica)
residuos_practica <- resid(modelo_practica)
SST_practica <- sum((y_practica - mean(y_practica))^2)
SSE_practica <- sum((ajustados_practica - mean(y_practica))^2)
SSR_practica <- sum(residuos_practica^2)
print(c(SST = SST_practica, SSE = SSE_practica, SSR = SSR_practica,
        R2 = 1 - SSR_practica / SST_practica))
print(all.equal(SST_practica, SSE_practica + SSR_practica))

# 7. En una celda Markdown, escribe tu interpretación con unidades.
# Distingue signo, significancia, R2 y asociación frente a causalidad.
