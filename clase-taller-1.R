# Taller 1: ejecutar desde la raíz del proyecto en una sesión limpia.
# Equivalente a todas las celdas R del notebook; no instala paquetes.

# NIV-01 · Escribe tu nombre
print("tu nombre")

# NIV-ASIG · Asignación de valores
x <- 2
y <- 5
z <- x - y
w <- abs(x - y)
print(x)
print(w)

# NIV-03 · Condicionales: if, else y operadores lógicos
v <- c(2, 7, 9)  # Valores del ejemplo, definidos antes de usarlos.
valor <- 8
if (valor > 4) {
  mensaje <- "Supera el umbral"
} else {
  mensaje <- "No supera el umbral"
}
print(mensaje)
print(v[v > 4])

# NIV-06 · Ciclos while y condiciones de término
valor <- 1
paso <- 0
max_pasos <- 20
trayectoria <- numeric(max_pasos + 1)
trayectoria[1] <- valor
while (valor < 100 && paso < max_pasos) {
  valor <- 2 * valor
  paso <- paso + 1
  trayectoria[paso + 1] <- valor
}
print(trayectoria[seq_len(paso + 1)])
print(c(pasos = paso, valor = valor))

# NIV-FOR · Ciclos for y condiciones de término
valor <- 1
max_pasos <- 20
trayectoria <- numeric(max_pasos + 1)
trayectoria[1] <- valor
for (paso in seq_len(max_pasos)) {
  valor <- 2 * valor
  trayectoria[paso + 1] <- valor
  if (valor >= 100) {
    break
  }
}
print(trayectoria[seq_len(paso + 1)])
print(c(pasos = paso, valor = valor))

# NIV-05 · Sucesión geométrica: 1, 2, 4, 8, 16…
sucesion <- numeric(6)
sucesion[1] <- 1
for (i in 2:6) {
  sucesion[i] <- 2 * sucesion[i - 1]
}
print(sucesion)

# NIV-02 · Vectores: creación, selección, modificación y llenado con for
v <- numeric(20)
for (i in 1:20) {
  if (i %% 2 != 0) {
    v[i] <- -1
  }
}
print(v)

# Comprueba lo aprendido: Trabaja sobre el vector anterior: reemplaza cada 0 por el número de su posición y conserva los valores −1.
for (i in seq_along(v)) {
  if (v[i] == 0) {
    v[i] <- i
  }
}
print(v)

# NIV-07 · Matrices y ciclos anidados
A <- matrix(0, nrow = 3, ncol = 3)
for (i in 1:3) {
  A[i, i] <- 1
}
print(A)

# Comprueba lo aprendido: 
A <- matrix(1:8, nrow = 2, ncol = 4)
print(A[2, 3])
print(t(A)[3, 2])
print(A[2, 3] == t(A)[3, 2])

# NIV-08 · Actividad integradora: sucesiones y matrices
sucesion <- 3^(1:6)
A <- matrix(sucesion, nrow = 3, ncol = 2)
print(sucesion)
print(A)

# NIV-NOTEBOOK · Vista general de un notebook
# Librerías -> adecuación de datos -> EDA -> modelamiento -> resultados

# P1-07 · Tipos y estructura de los datos económicos
# Ejemplos ficticios: los mismos puntos que aparecen en el video.
transversal <- data.frame(
  unidad = LETTERS[1:6], anio = rep(2020, 6),
  valor = c(5, 12, 8, 16, 10, 19))

serie_tiempo <- data.frame(
  unidad = rep("A", 6), anio = 2020:2025,
  valor = c(4, 6, 5, 8, 7, 10))

panel <- data.frame(
  unidad = rep(c("A", "B", "C"), each = 6),
  anio = rep(2020:2025, 3),
  valor = c(4, 6, 5, 8, 7, 10,
            10, 9, 12, 11, 14, 13,
            16, 15, 18, 17, 19, 20))

print(transversal)
print(serie_tiempo)
print(panel)

# P1-01 · Introducción a la econometría y a los datos
# Usa la copia local; si no está, carga la base del paquete.
if (file.exists("datos/wage1.csv")) {
  datos <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  datos <- wooldridge::wage1
}

# Conserva las seis variables que utilizaremos en el taller.
datos <- datos[c("wage", "educ", "exper", "tenure", "female", "married")]
head(datos)
str(datos)
summary(datos)

# P1-02 · Exploración gráfica de los datos
# wage · Histograma
hist(datos$wage, breaks = seq(0, 26, by = 2), right = FALSE,
     col = "#0160a0", border = "white", main = "Salario por hora",
     xlab = "USD de 1976", ylab = "Frecuencia (personas)")

# educ · Gráfico de barras
anios <- seq(min(datos$educ), max(datos$educ))
frecuencias <- table(factor(datos$educ, levels = anios))
barplot(frecuencias, col = "#0160a0", border = "white",
        main = "educ", xlab = "Años", ylab = "Frecuencia (personas)")

# exper · Gráfico de barras
anios <- seq(min(datos$exper), max(datos$exper))
frecuencias <- table(factor(datos$exper, levels = anios))
barplot(frecuencias, col = "#e12523", border = "white",
        main = "exper", xlab = "Años", ylab = "Frecuencia (personas)")

# tenure · Gráfico de barras
anios <- seq(min(datos$tenure), max(datos$tenure))
frecuencias <- table(factor(datos$tenure, levels = anios))
barplot(frecuencias, col = "#00875a", border = "white",
        main = "tenure", xlab = "Años", ylab = "Frecuencia (personas)")

# female · Gráfico circular
frecuencias <- table(factor(datos$female, levels = c(0, 1)))
etiquetas <- c("Hombre (0)", "Mujer (1)")
porcentajes <- round(100 * frecuencias / sum(frecuencias), 1)
pie(frecuencias, labels = paste(etiquetas, porcentajes, "%"),
    col = c("#0160a0", "#f8c751"), main = "female")

# married · Gráfico circular
frecuencias <- table(factor(datos$married, levels = c(0, 1)))
etiquetas <- c("No casado/a (0)", "Casado/a (1)")
porcentajes <- round(100 * frecuencias / sum(frecuencias), 1)
pie(frecuencias, labels = paste(etiquetas, porcentajes, "%"),
    col = c("#0160a0", "#f8c751"), main = "married")

# P1-04 · Correlación, causalidad y factores no observados
colores <- c("#0160A080", "#F8C75180")  # Azul para hombres (0), amarillo para mujeres (1)

plot(datos$educ, datos$wage,
     pch = 19,
     col = colores[datos$female + 1],
     xlab = "Educación (años)",
     ylab = "Salario por hora (USD de 1976)",
     main = "Educación y salario por género")

# Añadir una leyenda para identificar los colores.
legend("topleft",
       legend = c("Hombre", "Mujer"),
       col = colores,
       pch = 19)

# P1-05 · Educación y salarios: alcances de la comparación
datos$educ16 <- datos$educ >= 16
print(head(datos[c("educ", "educ16", "wage", "exper")], 12))

# P1-06 · Comparar salarios con boxplots
# educ · Boxplot del salario
grupo <- factor(datos$educ >= 16, levels = c(FALSE, TRUE),
                labels = c("Menos de 16 años", "16 años o más"))
boxplot(datos$wage ~ grupo, col = c("#0160a0", "#f8c751"),
        main = "Salario según educ", xlab = "Grupo",
        ylab = "Salario por hora (USD de 1976)")

# female · Boxplot del salario
grupo <- factor(datos$female, levels = c(0, 1),
                labels = c("Hombre (0)", "Mujer (1)"))
boxplot(datos$wage ~ grupo, col = c("#0160a0", "#f8c751"),
        main = "Salario según female", xlab = "Grupo",
        ylab = "Salario por hora (USD de 1976)")

# married · Boxplot del salario
grupo <- factor(datos$married, levels = c(0, 1),
                labels = c("No casado/a (0)", "Casado/a (1)"))
boxplot(datos$wage ~ grupo, col = c("#0160a0", "#f8c751"),
        main = "Salario según married", xlab = "Grupo",
        ylab = "Salario por hora (USD de 1976)")

# P1-09 · Razones para trabajar con muestras


# P1-08 · Cuatro técnicas de muestreo en R con wage1
# Ejecuta esta preparación una vez antes de los cuatro ejemplos.
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos <- as.data.frame(wooldridge::wage1)
datos$educ16 <- datos$educ >= 16
N <- nrow(datos)
marco <- 1:N
set.seed(36)

# Muestreo aleatorio simple
ids_simple <- sample(marco, size = 24, replace = FALSE)
muestra_simple <- datos[ids_simple, ]
print(muestra_simple[c("wage", "educ", "female")])

# Muestreo aleatorio sistemático
k <- 20
inicio <- sample(1:k, size = 1)
ids_sistema <- seq(inicio, N, by = k)
muestra_sistematica <- datos[ids_sistema, ]
print(muestra_sistematica[c("wage", "educ", "female")])

# Muestreo aleatorio estratificado
estrato_menos16 <- which(!datos$educ16)
estrato_16omas <- which(datos$educ16)
ids_estrato <- c(sample(estrato_menos16, size = 12),
                 sample(estrato_16omas, size = 12))
muestra_estratificada <- datos[ids_estrato, ]
print(table(muestra_estratificada$educ16))
print(muestra_estratificada[c("wage", "educ")])

# Muestreo por conglomerados (cluster)
grupo_artificial <- rep(1:12, length.out = N)
elegidos <- sample(unique(grupo_artificial), size = 2)

# Segunda etapa: seleccionar personas dentro de los grupos elegidos.
personas_grupo1 <- which(grupo_artificial == elegidos[1])
personas_grupo2 <- which(grupo_artificial == elegidos[2])
ids_conglomerado <- c(sample(personas_grupo1, size = 12),
                     sample(personas_grupo2, size = 12))
muestra_conglomerados <- datos[ids_conglomerado, ]
print(elegidos)
print(table(grupo_artificial[ids_conglomerado]))
print(muestra_conglomerados[c("wage", "educ", "female")])

# P2-01 · Salarios: promedio, mediana, moda y percentiles
# Salarios de la base completa wage1, no de las submuestras anteriores.
if (file.exists("datos/wage1.csv")) {
  base <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  base <- as.data.frame(wooldridge::wage1)
}
# married = 0 significa no casado/a; no identifica solamente a solteros.
grupos <- list(Total = base$wage,
               No_casados = base$wage[base$married == 0],
               Casados = base$wage[base$married == 1])

resumir <- function(x) {
  frecuencias <- table(x)
  modas <- names(frecuencias)[frecuencias == max(frecuencias)]
  percentiles <- quantile(x, probs = c(0.24, 0.50, 0.75), type = 7,
                         names = FALSE)
  data.frame(n = length(x), promedio = mean(x), mediana = median(x),
             moda = paste(modas, collapse = "; "),
             P24 = percentiles[1], P50 = percentiles[2], P75 = percentiles[3])
}
resumen <- do.call(rbind, lapply(grupos, resumir))
print(resumen)

# Comparar el promedio de cada grupo.
barplot(resumen$promedio, names.arg = rownames(resumen),
        col = c("#00875A", "#0160A0", "#F8C751"),
        ylab = "Salario por hora (USD de 1976)",
        main = "Promedio salarial: total y estado civil")
# La mediana coincide con P50. Las diferencias no demuestran causalidad.

# P2-02 · Dispersión: de la nube compacta a la nube amplia
# Indicadores de dispersión del salario en wage1.
if (file.exists("datos/wage1.csv")) {
  base <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  base <- as.data.frame(wooldridge::wage1)
}
grupos <- list(Total = base$wage,
               No_casados = base$wage[base$married == 0],
               Casados = base$wage[base$married == 1])
dispersion <- function(x) {
  data.frame(n = length(x), varianza = var(x), desviacion = sd(x),
             rango = diff(range(x)), RIQ = IQR(x, type = 7),
             CV_porcentaje = 100 * sd(x) / mean(x))
}
print(do.call(rbind, lapply(grupos, dispersion)))
boxplot(grupos, col = c("#00875A", "#0160A0", "#F8C751"),
        ylab = "Salario por hora (USD de 1976)", main = "Dispersión salarial")

# Ilustración artificial: misma media 10 y dispersión creciente.
set.seed(39)
z <- rnorm(60)
z <- (z - mean(z)) / sd(z)
altura_visual <- runif(60, -1, 1)
for (s in seq(0.2, 2.5, length.out = 80)) {
  valores <- 10 + s * z
  plot(valores, altura_visual, pch = 19, col = "#0160A080",
       xlim = c(0, 20), ylim = c(-1.3, 1.3), yaxt = "n", ylab = "",
       xlab = "Valor artificial", main = paste("Varianza =", round(var(valores), 2)))
  abline(v = 10, lty = 2)
  Sys.sleep(0.06)
}
# El eje vertical solo separa los puntos: no representa otra variable.
# var() usa n - 1; sd() conserva unidades; la varianza las eleva al cuadrado.

# P3-01 · Inferir, TCL y supuestos
if (file.exists("datos/wage1.csv")) {
  base <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  base <- as.data.frame(wooldridge::wage1)
}
poblacion <- base$wage
mu <- mean(poblacion)
sigma <- sqrt(mean((poblacion - mu)^2))  # Momento poblacional: divisor N.
n <- 50
set.seed(40)
medias <- replicate(1000, mean(sample(poblacion, n, replace = TRUE)))
hist(medias, probability = TRUE, col = "#0160A0", border = "white",
     xlab = "Promedio salarial (USD/h de 1976)", main = paste("Medias con n =", n))
curve(dnorm(x, mean = mu, sd = sigma / sqrt(n)), add = TRUE,
      col = "#E12523", lwd = 2)
print(c(media_poblacional = mu, varianza_media = sigma^2 / n,
        error_estandar = sigma / sqrt(n)))

# P3-05 · Intervalo de confianza para una media
xbarra <- 200
sigma <- 60
n <- 36
confianza <- 0.95
z <- qnorm((1 + confianza) / 2)
se <- sigma / sqrt(n)
ic <- xbarra + c(-1, 1) * z * se
print(c(estimacion = xbarra, margen = z * se, inferior = ic[1], superior = ic[2]))

# Ilustración normal con mu = 200 fijo; no es un parámetro estimado de wage1.
mu_demo <- 200
z_demo <- c(-0.271313, -1.056361, 0.197561, 0.002057, 0.870213, 2.519121, -0.91341, -0.254936, 0.322156, 0.578074, 1.506138, 0.186028, -0.36742, 0.614709, -0.81785, 0.118748, -0.002822, 1.631639, -0.215701, -1.137394)
medias_demo <- mu_demo + z_demo * se
inferior <- medias_demo - z * se
superior <- medias_demo + z * se
cubre <- inferior <= mu_demo & superior >= mu_demo
plot(range(c(inferior, superior, mu_demo)), c(1, 20), type = "n",
     xlab = "Media de ventas", ylab = "Repetición")
segments(inferior, 1:20, superior, 1:20,
         col = ifelse(cubre, "#0160A0", "#E12523"), lwd = 2)
abline(v = mu_demo, lty = 2)
print(mean(cubre))

# P3-07 · Confianza, precisión y tamaño muestral
xbarra <- 200
sigma <- 60
n <- 36
confianza <- 0.95
E <- 10
niveles <- c(0.90, 0.95, 0.99)
z_niveles <- qnorm((1 + niveles) / 2)
se <- sigma / sqrt(n)
limites <- cbind(inferior = xbarra - z_niveles * se,
                 superior = xbarra + z_niveles * se)
rownames(limites) <- paste0(100 * niveles, "%")
print(limites)
plot(range(limites), c(1, 3), type = "n", yaxt = "n",
     xlab = "Media de ventas", ylab = "Confianza")
axis(2, at = 1:3, labels = rownames(limites))
segments(limites[, 1], 1:3, limites[, 2], 1:3, lwd = 3, col = "#0160A0")
points(rep(xbarra, 3), 1:3, pch = 19)
n_requerido <- ceiling((qnorm((1 + confianza) / 2) * sigma / E)^2)
print(c(margen_deseado = E, n_requerido = n_requerido))

# P3-11 · Proporciones: intervalo y planificación
exitos <- 19
n <- 200
confianza <- 0.95
p_previa <- 0.5
E <- 0.03
p_hat <- exitos / n
z <- qnorm((1 + confianza) / 2)
if (n >= 30 && exitos > 5 && n - exitos > 5) {
  se <- sqrt(p_hat * (1 - p_hat) / n)
  ic <- p_hat + c(-1, 1) * z * se
  print(c(proporcion = p_hat, inferior = ic[1], superior = ic[2],
          contiene_0_05 = ic[1] <= 0.05 && ic[2] >= 0.05))
  plot(range(c(ic, 0.05)), c(0, 1), type = "n", yaxt = "n",
       xlab = "Proporción de defectuosos", ylab = "")
  segments(ic[1], 0.5, ic[2], 0.5, lwd = 3, col = "#0160A0")
  points(p_hat, 0.5, pch = 19)
  abline(v = 0.05, lty = 2)
} else {
  message("No se cumplen las condiciones de la aproximación normal.")
}
n_requerido <- ceiling(z^2 * p_previa * (1 - p_previa) / E^2)
print(c(n_requerido = n_requerido, largo_deseado = 2 * E))

# P3-15 · Diferencia de dos medias independientes
xbarra <- 800000
ybarra <- 680000
sigma_x <- 60000
sigma_y <- 50000
nx <- 144
ny <- 121
confianza <- 0.95
diferencia <- xbarra - ybarra
se <- sqrt(sigma_x^2 / nx + sigma_y^2 / ny)
z <- qnorm((1 + confianza) / 2)
ic <- diferencia + c(-1, 1) * z * se
print(c(diferencia = diferencia, inferior = ic[1], superior = ic[2],
        contiene_cero = ic[1] <= 0 && ic[2] >= 0))
plot(range(c(ic, 0)), c(0, 1), type = "n", yaxt = "n",
     xlab = "Diferencia de medias (pesos del ejemplo de cátedra)", ylab = "")
segments(ic[1], 0.5, ic[2], 0.5, lwd = 3, col = "#0160A0")
points(diferencia, 0.5, pch = 19)
abline(v = 0, lty = 2)

# Ejercitación: resuelve las consignas de la guía.
# Desafío wall balls: escribe aquí tu programa.
# Ejecuta la instalación una vez, si aún no tienes el paquete:
# install.packages("wooldridge", repos = "https://cloud.r-project.org/")
library(wooldridge)
datos_ejercicio <- as.data.frame(wooldridge::wage2)
head(datos_ejercicio)
# Diccionario completo de las variables:
help("wage2", package = "wooldridge")
# Pregunta 1: escribe tu respuesta.
# Pregunta 2: escribe tu respuesta.
# Pregunta 3: escribe tu respuesta.
# Pregunta 4: escribe tu respuesta.
# Pregunta 5: escribe tu respuesta.
# Pregunta 6: escribe tu respuesta.
# Pregunta 7: escribe tu respuesta.
# Pregunta 8: escribe tu respuesta.
# Pregunta 9: escribe tu respuesta.
# Pregunta 10: escribe tu respuesta.

cat("Todas las actividades finalizaron. Revise también gráficos e interpretaciones.\n")
sessionInfo()
