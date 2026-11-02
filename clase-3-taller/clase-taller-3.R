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
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
Y_recuperado <- ifelse(personas$T == 1, personas$Y_T, personas$Y_NT)
print(Y_recuperado)
print(all(Y_recuperado == personas$Y))

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
ATE <- mean(personas$efecto)
ATT <- mean(personas$efecto[personas$T == 1])
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])
print(c(ATE = ATE, ATT = ATT))

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
ATE <- mean(personas$efecto)
ATT <- mean(personas$efecto[personas$T == 1])
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])
print(c(ATE = ATE, ATT = ATT))

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
alternativa <- personas
alternativa$Y_T[alternativa$nombre == "Juan"] <- 60
alternativa$efecto <- alternativa$Y_T - alternativa$Y_NT
print(c(ATE = mean(alternativa$efecto),
        ATT = mean(alternativa$efecto[alternativa$T == 1])))

personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
tratados <- personas$T == 1
brecha <- mean(personas$Y[tratados]) - mean(personas$Y[!tratados])
ATT <- mean(personas$efecto[tratados])
seleccion <- mean(personas$Y_NT[tratados]) - mean(personas$Y_NT[!tratados])
print(c(brecha = brecha, ATT = ATT, seleccion = seleccion,
        suma = ATT + seleccion))
modelo_T <- lm(Y ~ T, data = personas)
print(coef(modelo_T))

media_tratados <- mean(c(100, 80, 60))
media_control <- mean(c(40, 20))
print(c(tratados = media_tratados, control = media_control,
        brecha = media_tratados - media_control))

ATT <- mean(c(100 - 75, 80 - 60, 60 - 45))
seleccion <- mean(c(75, 60, 45)) - mean(c(40, 20))
print(c(ATT = ATT, seleccion = seleccion, suma = ATT + seleccion))

observado <- data.frame(T = c(1, 0, 1, 0, 1),
                        Y = c(100, 40, 80, 20, 60))
print(coef(lm(Y ~ T, data = observado)))

casas <- data.frame(
  grupo = c("Instalan alarma", "No instalan"),
  T = c(1, 0),
  Y_NT = c(12, 4),
  efecto_supuesto = c(-5, -2)
)
casas$Y_T <- casas$Y_NT + casas$efecto_supuesto
casas$Y <- ifelse(casas$T == 1, casas$Y_T, casas$Y_NT)
tratadas <- casas$T == 1
brecha_alarmas <- casas$Y[tratadas] - casas$Y[!tratadas]
ATT_alarmas <- casas$Y_T[tratadas] - casas$Y_NT[tratadas]
seleccion_alarmas <- casas$Y_NT[tratadas] - casas$Y_NT[!tratadas]
print(casas)
print(c(brecha = brecha_alarmas, ATT = ATT_alarmas,
        seleccion = seleccion_alarmas, suma = ATT_alarmas + seleccion_alarmas))
barplot(casas$Y, names.arg = casas$grupo,
        col = c("#005E90", "#D6A600"),
        ylab = "Robos por cada 100 casas (ejemplo hipotético)")

casas <- data.frame(
  grupo = c("Instalan alarma", "No instalan"),
  T = c(1, 0),
  Y_NT = c(12, 4),
  efecto_supuesto = c(-5, -2)
)
casas$Y_T <- casas$Y_NT + casas$efecto_supuesto
casas$Y <- ifelse(casas$T == 1, casas$Y_T, casas$Y_NT)
print(casas)

ATT_alarmas <- 7 - 12
seleccion_alarmas <- 12 - 4
brecha_alarmas <- 7 - 4
print(c(ATT = ATT_alarmas, seleccion = seleccion_alarmas,
        brecha = brecha_alarmas, suma = ATT_alarmas + seleccion_alarmas))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
# Escenario 1: participan las personas con habilidad mayor que cero.
T_auto <- as.numeric(habilidad > 0)
Y_auto <- ifelse(T_auto == 1, Y_T, Y_NT)
# Escenario 2: se sortean 500 cupos, sin cambiar los resultados potenciales.
T_azar <- sample(c(rep(1, n / 2), rep(0, n / 2)))
Y_azar <- ifelse(T_azar == 1, Y_T, Y_NT)
brecha_auto <- mean(Y_auto[T_auto == 1]) - mean(Y_auto[T_auto == 0])
brecha_azar <- mean(Y_azar[T_azar == 1]) - mean(Y_azar[T_azar == 0])
comparacion <- data.frame(
  asignacion = c("Autoselección", "Sorteo"),
  efecto_verdadero = c(10, 10),
  diferencia_observada = c(brecha_auto, brecha_azar)
)
print(comparacion)
print(aggregate(habilidad, list(T = T_auto), mean))
print(aggregate(habilidad, list(T = T_azar), mean))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
print(head(data.frame(Y_NT, Y_T, efecto = Y_T - Y_NT)))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
T_auto <- as.numeric(habilidad > 0)
Y_auto <- ifelse(T_auto == 1, Y_T, Y_NT)
print(mean(Y_auto[T_auto == 1]) - mean(Y_auto[T_auto == 0]))
print(aggregate(habilidad, list(T = T_auto), mean))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
T_azar <- sample(c(rep(1, n / 2), rep(0, n / 2)))
Y_azar <- ifelse(T_azar == 1, Y_T, Y_NT)
print(mean(Y_azar[T_azar == 1]) - mean(Y_azar[T_azar == 0]))
print(aggregate(habilidad, list(T = T_azar), mean))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10

# Repetir la asignación sobre la población que acabamos de construir.
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))
print(c(promedio = mean(estimaciones), dispersion = sd(estimaciones)))
hist(estimaciones, col = "#005E90", border = "white",
     main = "200 sorteos sobre la misma población",
     xlab = "Efecto estimado: diferencia de productividades medias (puntos)")
abline(v = 10, col = "#D6A600", lwd = 3)

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))

set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10

# Repetir la asignación sobre la población que acabamos de construir.
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))
print(c(promedio = mean(estimaciones), dispersion = sd(estimaciones)))
hist(estimaciones, col = "#005E90", border = "white",
     main = "200 sorteos sobre la misma población",
     xlab = "Efecto estimado: diferencia de productividades medias (puntos)")
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
plot(y ~ x1, data = sim_ov, pch = 19, col = "#005E9060",
     xlab = "x1 simulada", ylab = "y simulada")
abline(corta, col = "#D6A600", lwd = 3)
# Recta del modelo con control, manteniendo x2 = 0.
abline(a = coef(larga)["(Intercept)"], b = coef(larga)["x1"],
       col = "#005E90", lwd = 3, lty = 2)

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
auxiliar <- lm(x2 ~ x1, data = sim_ov)
b_corta <- unname(coef(corta)["x1"])
b1 <- unname(coef(larga)["x1"])
b2 <- unname(coef(larga)["x2"])
delta1 <- unname(coef(auxiliar)["x1"])
print(c(pendiente_corta = b_corta,
        b1_mas_b2_delta = b1 + b2 * delta1,
        cambio_por_omitir = b2 * delta1))
print(all.equal(b_corta, b1 + b2 * delta1))

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

# Cambiar únicamente los dos parámetros de cada escenario.
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
fumar_datos$persona <- seq_len(nrow(fumar_datos))
fumar_datos$grupo_edad <- cut(fumar_datos$edad,
  breaks = c(20, 40, 60, 80), right = FALSE, include.lowest = TRUE,
  labels = c("20 a <40", "40 a <60", "60 a 80"))
sin_edad <- lm(Y ~ fumar, data = fumar_datos)
con_edad <- lm(Y ~ fumar + edad, data = fumar_datos)
print(table(fumar_datos$grupo_edad))
print(aggregate(cbind(edad, fumar, Y) ~ grupo_edad,
                data = fumar_datos, FUN = mean))
# Cambia este texto por "20 a <40", "40 a <60" o "60 a 80".
grupo_elegido <- "Todos"
observados <- if (grupo_elegido == "Todos") fumar_datos else
  fumar_datos[fumar_datos$grupo_edad == grupo_elegido, ]
print(head(observados[, c("persona", "edad", "fumar", "Y", "grupo_edad")], 10))
colores_edad <- c("#005E90", "#D6A600", "#B83B45")
plot(Y ~ fumar, data = observados, pch = 19,
     col = colores_edad[as.integer(observados$grupo_edad)],
     xlim = range(fumar_datos$fumar), ylim = range(fumar_datos$Y),
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
abline(sin_edad, col = "#1B2A5E", lwd = 3)
print(coef(sin_edad))
print(coef(con_edad))

set.seed(2026)
fumar_datos <- data.frame(edad = runif(100, min = 20, max = 80))
fumar_datos$fumar <- 30 - 0.3 * fumar_datos$edad + rnorm(100, sd = 2.3)
fumar_datos$Y <- 13 + 0.94 * fumar_datos$fumar +
                0.98 * fumar_datos$edad + rnorm(100)
fumar_datos$persona <- seq_len(nrow(fumar_datos))
fumar_datos$grupo_edad <- cut(fumar_datos$edad,
  breaks = c(20, 40, 60, 80), right = FALSE, include.lowest = TRUE,
  labels = c("20 a <40", "40 a <60", "60 a 80"))
sin_edad <- lm(Y ~ fumar, data = fumar_datos)
con_edad <- lm(Y ~ fumar + edad, data = fumar_datos)
# El filtro cambia los puntos mostrados, no la muestra que ajustó con_edad.
grupo_elegido <- "Todos"
observados <- if (grupo_elegido == "Todos") fumar_datos else
  fumar_datos[fumar_datos$grupo_edad == grupo_elegido, ]
print(head(observados[, c("persona", "edad", "fumar", "Y", "grupo_edad")], 10))
print(aggregate(cbind(edad, fumar, Y) ~ grupo_edad,
                data = fumar_datos, FUN = mean))
grid_fumar <- seq(min(fumar_datos$fumar), max(fumar_datos$fumar), length.out = 50)
a30 <- data.frame(fumar = grid_fumar, edad = 30)
a60 <- data.frame(fumar = grid_fumar, edad = 60)
colores_edad <- c("#005E90", "#D6A600", "#B83B45")
plot(Y ~ fumar, data = observados, pch = 19,
     col = colores_edad[as.integer(observados$grupo_edad)],
     xlim = range(fumar_datos$fumar), ylim = range(fumar_datos$Y),
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
lines(grid_fumar, predict(con_edad, newdata = a30), col = "#1B2A5E", lwd = 3)
lines(grid_fumar, predict(con_edad, newdata = a60), col = "#1B2A5E", lwd = 3, lty = 2)
legend("topright", c("Edad fija: 30", "Edad fija: 60"),
       col = "#1B2A5E", lwd = 3, lty = c(1, 2))
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
print(pendientes[1, ])
barplot(pendientes[1, ], col = c("#005E90", "#D6A600"),
        ylab = "Pendiente estimada", main = "Una sola muestra")
abline(h = 2, lty = 2)
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
