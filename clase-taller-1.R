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

# P1-02 · Exploración gráfica de los datos
# Elige: "wage", "educ", "exper", "tenure", "female" o "married".
variable <- "wage"
if (variable == "wage") {
  hist(datos$wage, breaks = seq(0, 26, by = 2), right = FALSE,
       col = "#0160a0", border = "white", main = "Salario por hora",
       xlab = "USD de 1976", ylab = "Frecuencia (personas)")
} else if (variable %in% c("educ", "exper", "tenure")) {
  anios <- seq(min(datos[[variable]]), max(datos[[variable]]))
  frecuencias <- table(factor(datos[[variable]], levels = anios))
  colores <- c(educ = "#0160a0", exper = "#e12523", tenure = "#00875a")
  barplot(frecuencias, col = colores[variable], border = "white",
          main = variable, xlab = "Años", ylab = "Frecuencia (personas)")
} else if (variable %in% c("female", "married")) {
  frecuencias <- table(factor(datos[[variable]], levels = c(0, 1)))
  etiquetas <- if (variable == "female") c("Hombre (0)", "Mujer (1)") else
    c("No casado/a (0)", "Casado/a (1)")
  porcentajes <- round(100 * frecuencias / sum(frecuencias), 1)
  pie(frecuencias, labels = paste(etiquetas, porcentajes, "%"),
      col = c("#0160a0", "#f8c751"), main = variable)
}

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
# Elige: "educ", "female" o "married".
variable <- "educ"
colores <- c("#0160A0", "#F8C751")

if (variable == "educ") {
  grupo <- factor(datos$educ >= 16, levels = c(FALSE, TRUE),
                  labels = c("Menos de 16 años", "16 años o más"))
} else if (variable == "female") {
  grupo <- factor(datos$female, levels = c(0, 1),
                  labels = c("Hombre (0)", "Mujer (1)"))
} else if (variable == "married") {
  grupo <- factor(datos$married, levels = c(0, 1),
                  labels = c("No casado/a (0)", "Casado/a (1)"))
}

boxplot(datos$wage ~ grupo,
        col = colores,
        main = paste("Salario según", variable),
        xlab = "Grupo", ylab = "Salario por hora (USD de 1976)")

# P1-07 · Tipos y estructura de los datos económicos
# Ejemplos ficticios para reconocer la estructura de las filas.
transversal <- data.frame(
  persona = c("Ana", "Bruno", "Carla", "Diego"),
  anio = c(2020, 2020, 2020, 2020),
  educ = c(12, 16, 14, 10), salario = c(4, 8, 6, 3))

serie_temporal <- data.frame(
  empresa = rep("Empresa A", 4), anio = 2020:2023,
  publicidad = c(10, 12, 11, 15), ventas = c(42, 45, 44, 52))

cortes_repetidos <- data.frame(
  persona = c("Ana", "Bruno", "Elena", "Felipe"),
  anio = c(2020, 2020, 2023, 2023),
  educ = c(12, 16, 12, 16), salario = c(4, 8, 5, 9))

panel <- data.frame(
  persona = c("Ana", "Ana", "Bruno", "Bruno"),
  anio = c(2020, 2023, 2020, 2023),
  educ = c(12, 13, 16, 16), salario = c(4, 5, 8, 9))

print(transversal)
print(serie_temporal)
print(cortes_repetidos)
print(panel)

# P1-08 · Población, muestra y unidad de observación
set.seed(16201)
N <- nrow(datos)
marco <- seq_len(N)
ids <- sample(marco, size = 12, replace = FALSE)
print(datos[ids, c("wage", "educ")])

# P1-09 · Razones para trabajar con muestras
presupuesto <- 100
costo <- 5
capacidad <- floor(presupuesto/costo)
print(capacidad)

# P1-10 · Variables, parámetros y estadísticos
print(data.frame(
  concepto = c("Variable", "Parámetro", "Estadístico"),
  ejemplo = c("Salario por hora individual",
              "Media salarial de la población objetivo",
              "Media salarial calculada en una muestra")))

# P1-11 · Métodos de muestreo probabilístico en R
set.seed(16202)
ids_simple <- sample(marco, 24)
k <- 20L
inicio <- sample.int(k, 1)
ids_sistema <- seq.int(inicio, N, by = k)
estratos <- split(marco, datos$educ16)
stopifnot(all(lengths(estratos) >= 12))
ids_estrato <- unlist(lapply(estratos, function(g) sample(g, 12)), use.names = FALSE)
# Grupos artificiales: ilustración algorítmica, no barrios reales.
grupo_artificial <- rep(seq_len(12), length.out = N)
elegidos <- sample(unique(grupo_artificial), 2)
ids_conglomerado <- which(grupo_artificial %in% elegidos)
print(list(simple = ids_simple, sistematico = ids_sistema,
           estratificado = ids_estrato, conglomerados = ids_conglomerado))

# P1-12 · Muestreo estratificado y por conglomerados
print(table(datos$educ16[ids_estrato]))
print(table(grupo_artificial[ids_conglomerado]))

# P1-13 · Muestreo no probabilístico y selección
ids_conveniencia <- head(which(datos$educ16), 12)
print(datos[ids_conveniencia, c("wage", "educ")])

# P1-14 · Estadística descriptiva e inferencial
frases <- c("Describo los salarios de las filas observadas",
            "Quiero estimar un promedio de una población definida")
print(frases)

# P2-01 · Ramas de la estadística
x <- datos$wage
print(length(x))

# P2-02 · Estadísticos como funciones de los datos
resumen_inicial <- c(n = length(x), minimo = min(x), maximo = max(x))
print(resumen_inicial)

# P2-03 · Medidas de localización central: media y mediana
centro <- function(z) c(media = mean(z), mediana = median(z))
print(centro(x))
x_modificado <- c(x, 10*max(x))
print(rbind(original = centro(x), copia_con_extremo = centro(x_modificado)))
ordenados <- sort(x)
n_x <- length(x)
mediana_manual <- if (n_x %% 2 == 1) ordenados[(n_x+1)/2] else
  (ordenados[n_x/2] + ordenados[n_x/2+1])/2
stopifnot(isTRUE(all.equal(mediana_manual, median(x))))

# P2-04 · Percentiles y cuartiles
cuartiles <- quantile(x, probs = c(.25, .5, .75), type = 7)
print(cuartiles)
print(quantile(x, .9, type = 7))

# P2-05 · Medidas de dispersión: RIQ, varianza y desviación
print(c(RIQ = IQR(x, type = 7), varianza = var(x), desviacion = sd(x)))
s2_manual <- sum((x-mean(x))^2)/(length(x)-1)
stopifnot(isTRUE(all.equal(s2_manual, var(x))))

# P2-06 · Histogramas y elección de intervalos
op <- par(mfrow = c(1,2))
for (b in c(5,20)) hist(x, breaks = b, col = "#7DB4B5",
  main = paste("Cortes sugeridos:", b),
  xlab = "Salario por hora (USD de 1976)", ylab = "Frecuencia")
par(op)

# P2-07 · Gráfico de caja, bigotes y valores atípicos
boxplot(x, horizontal = TRUE, col = "#7DB4B5",
  main = "Salarios: posición y dispersión", xlab = "USD por hora de 1976")
bp <- boxplot.stats(x)
print(bp$stats); print(bp$out)
print(quantile(x, c(.25,.5,.75), type = 7))

# P3-01 · Inferencia y población empírica de referencia
poblacion <- datos$wage
mu <- mean(poblacion)
sigma2 <- mean((poblacion-mu)^2)
sigma <- sqrt(sigma2)
print(c(mu = mu, sigma = sigma, N = length(poblacion)))

# P3-02 · Intervalos de confianza e incertidumbre
print(c("El parámetro didáctico permanece fijo",
        "La muestra y sus límites cambian",
        "La confianza describe el procedimiento"))

# P3-03 · Teorema central del límite: simulación en R
set.seed(16203)
B <- 1000L
op <- par(mfrow = c(1,2))
for (n in c(5,100)) {
  medias <- replicate(B, mean(sample(poblacion, n, replace = TRUE)))
  hist(medias, probability = TRUE, breaks = 25, col = "#7DB4B5",
       main = paste("Medias con n =", n), xlab = "Media salarial (USD/h)")
  curve(dnorm(x, mu, sigma/sqrt(n)), add = TRUE, col = "#BD4C45", lwd = 2)
  print(c(n = n, media_medias = mean(medias),
          sd_medias = sd(medias), error_teorico = sigma/sqrt(n)))
}
par(op)

# P3-04 · Supuestos del teorema central del límite
stopifnot(all(is.finite(poblacion)), sigma2 > 0)
print(c(media_finita = is.finite(mu), varianza_finita = is.finite(sigma2)))

# P3-05 · Intervalo para una media: ejemplo salarial
set.seed(16204)
n_ic <- 36L
muestra_ic <- sample(poblacion, n_ic, replace = TRUE)
xbarra <- mean(muestra_ic)
z95 <- qnorm(.975)
se <- sigma/sqrt(n_ic)
ic95 <- xbarra + c(-1,1)*z95*se
print(c(estimacion = xbarra, error_estandar = se,
        inferior = ic95[1], superior = ic95[2], mu_didactica = mu))

# P3-06 · Componentes del intervalo de confianza de 95%
margen95 <- z95*se
print(c(estimacion = xbarra, z = z95, se = se, margen = margen95))
stopifnot(isTRUE(all.equal(diff(ic95), 2*margen95)))

# P3-07 · Intervalos con distintos niveles de confianza
niveles <- c(.90,.95,.99)
z <- qnorm((1+niveles)/2)
limites <- cbind(inferior = xbarra-z*se, superior = xbarra+z*se)
rownames(limites) <- paste0(100*niveles, "%")
print(limites)

# P3-08 · Comparación gráfica de intervalos de confianza
plot(range(limites), c(1,3), type = "n", yaxt = "n",
     xlab = "Media salarial (USD/h)", ylab = "Confianza",
     main = "La misma muestra, distinta confianza")
axis(2, at = 1:3, labels = rownames(limites))
segments(limites[,1], 1:3, limites[,2], 1:3, lwd = 3, col = "#35618A")
points(rep(xbarra,3), 1:3, pch = 19)

# P3-09 · Cobertura, confianza y precisión
set.seed(16205)
medias_ic <- replicate(1000, mean(sample(poblacion, n_ic, replace = TRUE)))
L <- medias_ic-z95*se; U <- medias_ic+z95*se
cubre <- L <= mu & mu <= U
print(c(cobertura_observada = mean(cubre), confianza_nominal = .95,
        margen_n36 = margen95, margen_n144 = z95*sigma/sqrt(144)))
j <- seq_len(100)
plot(range(c(L[j],U[j],mu)), range(j), type = "n",
     xlab = "Media salarial (USD/h)", ylab = "Muestra", main = "100 intervalos")
segments(L[j],j,U[j],j,col = ifelse(cubre[j],"#35618A","#BD4C45"))
abline(v = mu, lty = 2)

# P3-10 · Tamaño muestral para estimar una media
E_media <- .5
n_necesario <- ceiling((qnorm(.975)*sigma/E_media)^2)
print(c(n = n_necesario, margen = qnorm(.975)*sigma/sqrt(n_necesario)))

# P3-11 · Intervalos de confianza para proporciones
indicador <- as.integer(datos$educ >= 16)
p_real <- mean(indicador)
set.seed(16206)
muestra_p <- sample(indicador, 200, replace = TRUE)
n_p <- length(muestra_p)
p_hat <- mean(muestra_p)
exitos <- sum(muestra_p); fracasos <- n_p-exitos
stopifnot(exitos > 5, fracasos > 5)
se_p <- sqrt(p_hat*(1-p_hat)/n_p)
ic_p <- p_hat+c(-1,1)*qnorm(.975)*se_p
print(c(exitos = exitos, fracasos = fracasos, p_hat = p_hat,
        inferior = ic_p[1], superior = ic_p[2], p_didactica = p_real))

# P3-12 · Proporciones: comparación con una referencia
referencia <- .20
compatible <- ic_p[1] <= referencia && referencia <= ic_p[2]
print(c(referencia = referencia, dentro_del_IC = compatible))

# P3-13 · Tamaño muestral para estimar una proporción
E_p <- .03
print(c(con_piloto = ceiling(qnorm(.975)^2*p_hat*(1-p_hat)/E_p^2),
        conservador = ceiling(qnorm(.975)^2*.25/E_p^2)))

# P3-14 · Aplicación: longitud y margen de error
set.seed(16207)
piloto <- sample(indicador, 30, replace = TRUE)
p_estrella <- mean(piloto)
longitud_max <- .05
E_plan <- longitud_max/2
n_plan <- ceiling(qnorm(.975)^2*p_estrella*(1-p_estrella)/E_plan^2)
n_conservador <- ceiling(qnorm(.975)^2*.25/E_plan^2)
print(c(piloto = p_estrella, margen = E_plan, n_piloto = n_plan,
        n_conservador = n_conservador))

# P3-15 · Comparación de medias entre dos poblaciones
pob_alta <- datos$wage[datos$educ >= 16]
pob_resto <- datos$wage[datos$educ < 16]
stopifnot(length(pob_alta) > 1, length(pob_resto) > 1)
print(c(N_alta = length(pob_alta), N_resto = length(pob_resto)))

# P3-16 · Diferencia de medias: parámetro e interpretación
mu_alta <- mean(pob_alta); mu_resto <- mean(pob_resto)
delta <- mu_alta-mu_resto
print(c(delta_didactica = delta))

# P3-17 · Diferencia de medias con varianzas conocidas
var_alta <- mean((pob_alta-mu_alta)^2)
var_resto <- mean((pob_resto-mu_resto)^2)
set.seed(16208)
n_a <- 144L; n_b <- 121L
m_a <- sample(pob_alta, n_a, replace = TRUE)
m_b <- sample(pob_resto, n_b, replace = TRUE)
diferencia <- mean(m_a)-mean(m_b)
se_diferencia <- sqrt(var_alta/n_a+var_resto/n_b)
print(c(estimacion = diferencia, error_estandar = se_diferencia))

# P3-18 · Diferencia de medias: intervalo y conclusión
ic_d <- diferencia+c(-1,1)*qnorm(.975)*se_diferencia
print(c(inferior = ic_d[1], superior = ic_d[2], delta_didactica = delta,
        contiene_cero = ic_d[1] <= 0 && ic_d[2] >= 0))
plot(range(c(ic_d,0)), c(0,1), type = "n", yaxt = "n", ylab = "",
     xlab = "Diferencia de medias (USD/h de 1976)", main = "Alta educación menos resto")
segments(ic_d[1],.5,ic_d[2],.5,lwd = 3,col = "#35618A")
points(diferencia,.5,pch = 19); abline(v = 0,lty = 2)

cat("Todas las actividades finalizaron. Revise también gráficos e interpretaciones.\n")
sessionInfo()
