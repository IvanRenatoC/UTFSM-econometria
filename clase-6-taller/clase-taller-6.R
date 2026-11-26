# Clase 6. Ejecutar en orden con R desde clase-6-taller/ o en Colab.

install.packages("wooldridge", repos = "https://cloud.r-project.org/")

original <- wooldridge::wage1
datos <- original[, c("wage", "educ", "exper")]
head(datos)
str(datos)
summary(datos)

print(c(media = mean(datos$wage), mediana = median(datos$wage)))

modelo_nivel <- lm(wage ~ educ, data = datos)
modelo_log <- lm(log(wage) ~ educ, data = datos)
print(coef(modelo_nivel))
print(coef(modelo_log))
b_educ <- coef(modelo_log)["educ"]
print(c(aproximado = 100 * b_educ,
        exacto_curva = 100 * (exp(b_educ) - 1)))
nuevos <- data.frame(educ = 6:18)
ajuste_log <- predict(modelo_log, newdata = nuevos)
curva <- exp(ajuste_log)
plot(wage ~ educ, data = datos, pch = 19, col = "#005F9640",
     xlab = "Educación (años)", ylab = "Salario (USD/h, 1976)")
lines(nuevos$educ, curva, col = "#D6A600", lwd = 3)

# El logaritmo del salario en el eje vertical.
plot(log(wage) ~ educ, data = datos, pch = 19, col = "#005F9640",
     main = "Logaritmo del salario y educación",
     xlab = "Educación (años)", ylab = "Logaritmo del salario (USD/h)")
abline(modelo_log, col = "#D6A600", lwd = 3)

print(c(aproximado = 100 * b_educ * 2,
        exacto_curva = 100 * (exp(b_educ * 2) - 1)))

# Primera mirada en las dos escalas logarítmicas.
datos_log <- datos[datos$educ > 0, ]
plot(log(wage) ~ log(educ), data = datos_log, pch = 19, col = "#005F9640",
     main = "Salario y educación en logaritmos",
     xlab = "Logaritmo de educación (años)",
     ylab = "Logaritmo del salario (USD/h)")

print(c(antes = nrow(datos), con_educ_positiva = nrow(datos_log)))
modelo_nivel_log <- lm(wage ~ log(educ), data = datos_log)
modelo_log_log <- lm(log(wage) ~ log(educ), data = datos_log)
print(coef(modelo_nivel_log))
print(coef(modelo_log_log))
b_nl <- coef(modelo_nivel_log)["log(educ)"]
b_ll <- coef(modelo_log_log)["log(educ)"]
print(c(usd_h_por_1pct = b_nl / 100,
        porcentaje_por_1pct = b_ll))
print(c(usd_h_por_10pct = b_nl * log(1.10),
        porcentaje_por_10pct = 100 * (1.10^b_ll - 1)))
abline(modelo_log_log, col = "#D6A600", lwd = 3)

print(c(usd_h = b_nl * log(1.05),
        porcentaje_curva = 100 * (1.05^b_ll - 1)))

datos$exper2 <- datos$exper^2
modelo_cuad <- lm(wage ~ exper + exper2, data = datos)
b <- coef(modelo_cuad)
print(b)
experiencias <- c(5, 20, 35)
efecto <- b["exper"] + 2 * b["exper2"] * experiencias
print(data.frame(exper = experiencias, efecto_local = efecto))
giro <- -b["exper"] / (2 * b["exper2"])
print(c(giro = giro, minimo = min(datos$exper), maximo = max(datos$exper)))
grilla <- data.frame(exper = seq(min(datos$exper), max(datos$exper), length.out = 100))
grilla$exper2 <- grilla$exper^2
plot(wage ~ exper, data = datos, pch = 19, col = "#005F9640",
     xlab = "Experiencia potencial (años)", ylab = "Salario (USD/h, 1976)")
lines(grilla$exper, predict(modelo_cuad, newdata = grilla),
      col = "#D6A600", lwd = 3)

print(b["exper"] + 2 * b["exper2"] * c(10, 30))
p <- predict(modelo_cuad, newdata = data.frame(exper = c(10, 11), exper2 = c(10, 11)^2))
print(p[2] - p[1])

modelo_int <- lm(wage ~ educ * exper, data = datos)
bi <- coef(modelo_int)
print(bi)
experiencias <- c(5, 20, 35)
efecto_educ <- bi["educ"] + bi["educ:exper"] * experiencias
print(data.frame(exper = experiencias, usd_h_por_ano_educ = efecto_educ))
comparar <- data.frame(educ = c(12, 13, 12, 13), exper = c(5, 5, 20, 20))
comparar$predicho <- predict(modelo_int, newdata = comparar)
print(comparar)
plot(wage ~ educ, data = datos, pch = 19, col = "#005F9640",
     xlab = "Educación (años)", ylab = "Salario (USD/h, 1976)")
for (e in experiencias) {
  nuevos <- data.frame(educ = 6:18, exper = e)
  lines(nuevos$educ, predict(modelo_int, newdata = nuevos),
        col = c("#005F96", "#D6A600", "#B2292E")[match(e, experiencias)], lwd = 2)
}
legend("topleft", legend = paste(experiencias, "años de experiencia"),
       col = c("#005F96", "#D6A600", "#B2292E"), lwd = 2, bty = "n")

p <- predict(modelo_int, newdata = data.frame(educ = c(12, 13), exper = c(35, 35)))
print(c(diferencia = p[2] - p[1],
        formula = bi["educ"] + bi["educ:exper"] * 35))

print(c(porcentaje_por_ano_educ = 100 * coef(modelo_log)["educ"],
        elasticidad = coef(modelo_log_log)["log(educ)"],
        pendiente_exper_10 = b["exper"] + 2 * b["exper2"] * 10,
        pendiente_educ_exper_20 = bi["educ"] + bi["educ:exper"] * 20))

print(data.frame(
  modelo = c("Log-nivel", "Log-log", "Cuadrático en exper", "Interacción"),
  unidad = c("% aproximado por año de educación", "% aproximado por 1% de educación",
             "USD/h por año de experiencia, en 10 años",
             "USD/h por año de educación, con 20 años de experiencia")))

datos$salario_pesos <- 1000 * datos$wage
datos$educ_meses <- 12 * datos$educ
modelo_pesos <- lm(salario_pesos ~ educ, data = datos)
modelo_meses <- lm(wage ~ educ_meses, data = datos)
print(rbind(dolares = coef(modelo_nivel),
            pesos = coef(modelo_pesos), meses = coef(modelo_meses)))
print(c(R2_dolares = summary(modelo_nivel)$r.squared,
        R2_pesos = summary(modelo_pesos)$r.squared,
        R2_meses = summary(modelo_meses)$r.squared))
print(c(SCR_dolares = sum(resid(modelo_nivel)^2),
        SCR_pesos = sum(resid(modelo_pesos)^2)))
print(all.equal(fitted(modelo_pesos) / 1000, fitted(modelo_nivel)))
print(all.equal(fitted(modelo_meses), fitted(modelo_nivel)))

datos$centavos <- 100 * datos$wage
modelo_centavos <- lm(centavos ~ educ, data = datos)
print(coef(modelo_centavos))
print(sum(resid(modelo_centavos)^2) / sum(resid(modelo_nivel)^2))

# Punto de partida. Ejecuta la carga de la lámina 01 primero.
practica <- original[, c("wage", "tenure")]
practica <- practica[complete.cases(practica) & practica$wage > 0, ]
head(practica)
summary(practica)

modelo_tenure <- lm(log(wage) ~ tenure, data = practica)
bt <- coef(modelo_tenure)["tenure"]
print(coef(modelo_tenure))
print(c(aproximado = 100 * bt * 3,
        exacto_curva = 100 * (exp(bt * 3) - 1)))
plot(log(wage) ~ tenure, data = practica, pch = 19, col = "#005F9640",
     xlab = "Antigüedad con el empleador (años)", ylab = "Logaritmo del salario")
abline(modelo_tenure, col = "#D6A600", lwd = 3)
practica$meses <- 12 * practica$tenure
modelo_tenure_meses <- lm(log(wage) ~ meses, data = practica)
print(coef(modelo_tenure_meses))

# Recupera las cuatro pendientes vistas hoy.
print(c(nivel_nivel = coef(modelo_nivel)["educ"],
        log_nivel = coef(modelo_log)["educ"],
        nivel_log = coef(modelo_nivel_log)["log(educ)"],
        log_log = coef(modelo_log_log)["log(educ)"]))

print(c(usd_h_por_ano = coef(modelo_nivel)["educ"],
        porcentaje_por_ano = 100 * coef(modelo_log)["educ"],
        usd_h_por_1pct = coef(modelo_nivel_log)["log(educ)"] / 100,
        porcentaje_por_1pct = coef(modelo_log_log)["log(educ)"]))
