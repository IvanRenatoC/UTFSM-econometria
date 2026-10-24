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

par(mfrow = c(1, 3))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9080")
plot(educ ~ exper, data = datos, pch = 19, col = "#005E9080")
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

modelo_pos <- lm(wage ~ educ, data = datos)
print(coef(modelo_pos))
print(sum(resid(modelo_pos)^2))
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060")
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
summary(modelo_pos)
plot(wage ~ educ, data = datos, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_pos, col = "#D6A600", lwd = 3)
predict(modelo_pos, newdata = data.frame(educ = c(12, 16)))

modelo_neg <- lm(educ ~ exper, data = datos)
summary(modelo_neg)
plot(educ ~ exper, data = datos, pch = 19, col = "#005E9060",
     xlab = "Experiencia potencial (años)", ylab = "Educación (años)")
abline(modelo_neg, col = "#D6A600", lwd = 3)

modelo_plano <- lm(wage ~ numdep, data = datos)
summary(modelo_plano)
confint(modelo_plano, "numdep", level = 0.95)
plot(wage ~ numdep, data = datos, pch = 19, col = "#005E9060",
     xlab = "Número de dependientes", ylab = "Salario por hora (USD de 1976)")
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

comparacion <- data.frame(
  caso = c("Salario y educación", "Educación y experiencia", "Salario y dependientes"),
  pendiente = sapply(modelos, function(m) coef(m)[2]),
  R2 = sapply(modelos, function(m) summary(m)$r.squared),
  p_pendiente = sapply(modelos, function(m) coef(summary(m))[2, 4]))
print(comparacion)
# Escribe tus conclusiones en una celda Markdown del notebook.
