# Taller 3: ejecutar desde clase-3-taller/.
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

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y_NT = c(75, 40, 60, 20, 45),
  Y_T = c(100, 55, 80, 30, 60)
)
personas$Y <- ifelse(personas$T == 1, personas$Y_T, personas$Y_NT)
observado <- personas[, c("nombre", "T", "Y")]
print(observado)

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

auxiliar <- lm(x2 ~ x1, data = sim_ov)
b_corta <- unname(coef(corta)["x1"])
b1 <- unname(coef(larga)["x1"])
b2 <- unname(coef(larga)["x2"])
delta1 <- unname(coef(auxiliar)["x1"])
print(c(pendiente_corta = b_corta,
        b1_mas_b2_delta = b1 + b2 * delta1,
        cambio_por_omitir = b2 * delta1))
print(all.equal(b_corta, b1 + b2 * delta1))

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

print(summary(trabajo))
print(cor(trabajo))
plot(wage ~ educ, data = trabajo, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Ingreso mensual (USD)")

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
