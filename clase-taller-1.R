# Taller 1: ejecutar desde la raíz del proyecto en una sesión limpia.
# Equivalente a todas las celdas R del notebook; no instala paquetes.

# NIV-01 · Tu primera instrucción
saldo <- 10
saldo <- saldo + 3
print(saldo)
print(c(tipo = typeof(saldo), longitud = length(saldo)))

# NIV-02 · Reserva y llena un vector
v <- numeric(3)
v[1] <- 2; v[2] <- 6; v[3] <- 9
print(v[v > 4])
v[2] <- 7
print(v); print(length(v))

# NIV-03 · Tomar una decisión
valor <- 8
if (valor > 4) {
  mensaje <- "Supera el umbral"
} else {
  mensaje <- "No supera el umbral"
}
print(mensaje)
print(v[v > 4])

# NIV-04 · Repetir con for
dobles <- numeric(5)
for (i in seq_along(dobles)) {
  dobles[i] <- 2 * i
}
print(dobles)

# NIV-05 · Tres sucesiones
a <- g <- r <- numeric(6)
a[1] <- 2; g[1] <- 2; r[1] <- 1
for (i in 2:length(a)) {
  a[i] <- a[i-1] + 3
  g[i] <- 2 * g[i-1]
  r[i] <- 2 * r[i-1] + 1
}
print(rbind(aritmetica = a, geometrica = g, recurrencia = r))
stopifnot(all(a == 2 + 3 * (seq_along(a)-1)),
          all(g == 2 * 2^(seq_along(g)-1)))

# NIV-06 · Un while que termina
valor <- 1
paso <- 0L
max_pasos <- 20L
trayectoria <- numeric(max_pasos + 1L)
trayectoria[1] <- valor
while (valor < 100 && paso < max_pasos) {
  valor <- 2 * valor
  paso <- paso + 1L
  trayectoria[paso + 1L] <- valor
}
print(trayectoria[seq_len(paso + 1L)])
print(c(pasos = paso, valor = valor))

# NIV-07 · Una matriz, dos índices
m <- matrix(0, nrow = 2, ncol = 3)
for (i in seq_len(nrow(m))) {
  for (j in seq_len(ncol(m))) {
    m[i,j] <- 10*i + j
  }
}
print(m)
m[1,1] <- 99
print(m); print(dim(m))

# NIV-08 · Integra: término y clasificación
terminos <- numeric(6)
terminos[1] <- 2
for (i in 2:length(terminos)) terminos[i] <- terminos[i-1] + 3
resultado <- matrix(0, nrow = 6, ncol = 3,
                    dimnames = list(NULL, c("indice", "valor", "supera_10")))
for (i in seq_along(terminos)) {
  resultado[i,1] <- i
  resultado[i,2] <- terminos[i]
  if (terminos[i] > 10) resultado[i,3] <- 1
}
print(resultado)

# P1-01 · ¿Qué podemos preguntar a los datos?
# La copia local permite trabajar sin conexión.
if (file.exists("datos/wage1.csv")) {
  original <- read.csv("datos/wage1.csv")
  original$rownames <- NULL
} else if (requireNamespace("wooldridge", quietly = TRUE)) {
  original <- as.data.frame(wooldridge::wage1)
} else {
  stop("Abra el proyecto desde su carpeta raíz o instale wooldridge.")
}
variables <- c("wage", "educ", "exper", "tenure", "female", "married")
stopifnot(nrow(original) == 526L, all(variables %in% names(original)))
print(colSums(is.na(original[variables])))
datos <- original[complete.cases(original[variables]), variables]
stopifnot(all(datos$wage > 0), all(datos$female %in% 0:1),
          all(datos$married %in% 0:1), nrow(datos) > 100)
str(datos)
head(datos)

# P1-02 · Tres preguntas distintas
preguntas <- data.frame(
  pregunta = c("¿Cómo se relacionan educación y salario?",
               "¿Más educación causa mayor salario?",
               "¿Qué salario tendrá otra persona?"),
  finalidad = c("Descripción", "Causalidad", "Predicción"))
print(preguntas)

# P1-03 · De la pregunta a las columnas
print(names(datos))
print(head(datos[c("wage", "educ", "exper")]))

# P1-04 · Mirar una asociación
plot(datos$educ, datos$wage, pch = 19, col = "#35618A80",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)",
     main = "Educación y salario: observar no es aislar una causa")

# P1-05 · Educación: grupos con límites
datos$educ16 <- datos$educ >= 16
print(head(datos[c("educ", "educ16", "wage", "exper")], 12))

# P1-06 · La base correcta para cada pregunta
necesidades <- list(
  desparasitacion = c("asignación", "tratamiento", "asistencia", "escuela"),
  consultoria = c("asignación", "consultoría", "productividad", "fábrica"))
print(necesidades)

# P1-07 · La forma de la tabla
estructuras <- data.frame(
  tipo = c("Corte transversal", "Serie temporal", "Panel"),
  unidades = c("Muchas", "Una", "Muchas"),
  periodos = c("Uno", "Varios", "Varios por unidad"))
print(estructuras)

# P1-08 · Una población didáctica
set.seed(16201)
N <- nrow(datos)
marco <- seq_len(N)
ids <- sample(marco, size = 12, replace = FALSE)
print(datos[ids, c("wage", "educ")])

# P1-09 · ¿Por qué no observar a todos?
presupuesto <- 100
costo <- 5
capacidad <- floor(presupuesto/costo)
print(capacidad)

# P1-10 · ¿Qué queremos estimar?
print(data.frame(
  concepto = c("Variable", "Parámetro", "Estadístico"),
  ejemplo = c("Salario por hora individual",
              "Media salarial de la población objetivo",
              "Media salarial calculada en una muestra")))

# P1-11 · Cuatro formas de seleccionar
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

# P1-12 · Dentro de todos o algunos grupos
print(table(datos$educ16[ids_estrato]))
print(table(grupo_artificial[ids_conglomerado]))

# P1-13 · Seleccionar por conveniencia
ids_conveniencia <- head(which(datos$educ16), 12)
print(datos[ids_conveniencia, c("wage", "educ")])

# P1-14 · La frontera entre resumir e inferir
frases <- c("Describo los salarios de las filas observadas",
            "Quiero estimar un promedio de una población definida")
print(frases)

# P2-01 · Primero describir
x <- datos$wage
print(length(x))

# P2-02 · Una función resume muchos datos
resumen_inicial <- c(n = length(x), minimo = min(x), maximo = max(x))
print(resumen_inicial)

# P2-03 · ¿El sueldo típico es el promedio?
centro <- function(z) c(media = mean(z), mediana = median(z))
print(centro(x))
x_modificado <- c(x, 10*max(x))
print(rbind(original = centro(x), copia_con_extremo = centro(x_modificado)))
ordenados <- sort(x)
n_x <- length(x)
mediana_manual <- if (n_x %% 2 == 1) ordenados[(n_x+1)/2] else
  (ordenados[n_x/2] + ordenados[n_x/2+1])/2
stopifnot(isTRUE(all.equal(mediana_manual, median(x))))

# P2-04 · Ubicarse en la distribución
cuartiles <- quantile(x, probs = c(.25, .5, .75), type = 7)
print(cuartiles)
print(quantile(x, .9, type = 7))

# P2-05 · Cuánto se dispersan los salarios
print(c(RIQ = IQR(x, type = 7), varianza = var(x), desviacion = sd(x)))
s2_manual <- sum((x-mean(x))^2)/(length(x)-1)
stopifnot(isTRUE(all.equal(s2_manual, var(x))))

# P2-06 · Un histograma, varias decisiones
op <- par(mfrow = c(1,2))
for (b in c(5,20)) hist(x, breaks = b, col = "#7DB4B5",
  main = paste("Cortes sugeridos:", b),
  xlab = "Salario por hora (USD de 1976)", ylab = "Frecuencia")
par(op)

# P2-07 · Leer la caja y los bigotes
boxplot(x, horizontal = TRUE, col = "#7DB4B5",
  main = "Salarios: posición y dispersión", xlab = "USD por hora de 1976")
bp <- boxplot.stats(x)
print(bp$stats); print(bp$out)
print(quantile(x, c(.25,.5,.75), type = 7))

# P3-01 · Conocer una población para aprender a inferir
poblacion <- datos$wage
mu <- mean(poblacion)
sigma2 <- mean((poblacion-mu)^2)
sigma <- sqrt(sigma2)
print(c(mu = mu, sigma = sigma, N = length(poblacion)))

# P3-02 · Un intervalo, una afirmación limitada
print(c("El parámetro didáctico permanece fijo",
        "La muestra y sus límites cambian",
        "La confianza describe el procedimiento"))

# P3-03 · Muchas muestras, muchas medias
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

# P3-04 · Cuándo confiar en la aproximación
stopifnot(all(is.finite(poblacion)), sigma2 > 0)
print(c(media_finita = is.finite(mu), varianza_finita = is.finite(sigma2)))

# P3-05 · El primer intervalo salarial
set.seed(16204)
n_ic <- 36L
muestra_ic <- sample(poblacion, n_ic, replace = TRUE)
xbarra <- mean(muestra_ic)
z95 <- qnorm(.975)
se <- sigma/sqrt(n_ic)
ic95 <- xbarra + c(-1,1)*z95*se
print(c(estimacion = xbarra, error_estandar = se,
        inferior = ic95[1], superior = ic95[2], mu_didactica = mu))

# P3-06 · Desarmar el IC de 95%
margen95 <- z95*se
print(c(estimacion = xbarra, z = z95, se = se, margen = margen95))
stopifnot(isTRUE(all.equal(diff(ic95), 2*margen95)))

# P3-07 · Cambiar solo la confianza
niveles <- c(.90,.95,.99)
z <- qnorm((1+niveles)/2)
limites <- cbind(inferior = xbarra-z*se, superior = xbarra+z*se)
rownames(limites) <- paste0(100*niveles, "%")
print(limites)

# P3-08 · Ver la anchura
plot(range(limites), c(1,3), type = "n", yaxt = "n",
     xlab = "Media salarial (USD/h)", ylab = "Confianza",
     main = "La misma muestra, distinta confianza")
axis(2, at = 1:3, labels = rownames(limites))
segments(limites[,1], 1:3, limites[,2], 1:3, lwd = 3, col = "#35618A")
points(rep(xbarra,3), 1:3, pch = 19)

# P3-09 · ¿Qué significa 95% de confianza?
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

# P3-10 · Planificar el tamaño para una media
E_media <- .5
n_necesario <- ceiling((qnorm(.975)*sigma/E_media)^2)
print(c(n = n_necesario, margen = qnorm(.975)*sigma/sqrt(n_necesario)))

# P3-11 · Una proporción educativa
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

# P3-12 · ¿Es compatible una referencia?
referencia <- .20
compatible <- ic_p[1] <= referencia && referencia <= ic_p[2]
print(c(referencia = referencia, dentro_del_IC = compatible))

# P3-13 · Tamaño para una proporción
E_p <- .03
print(c(con_piloto = ceiling(qnorm(.975)^2*p_hat*(1-p_hat)/E_p^2),
        conservador = ceiling(qnorm(.975)^2*.25/E_p^2)))

# P3-14 · Longitud no es margen
set.seed(16207)
piloto <- sample(indicador, 30, replace = TRUE)
p_estrella <- mean(piloto)
longitud_max <- .05
E_plan <- longitud_max/2
n_plan <- ceiling(qnorm(.975)^2*p_estrella*(1-p_estrella)/E_plan^2)
n_conservador <- ceiling(qnorm(.975)^2*.25/E_plan^2)
print(c(piloto = p_estrella, margen = E_plan, n_piloto = n_plan,
        n_conservador = n_conservador))

# P3-15 · Comparar dos grupos educativos
pob_alta <- datos$wage[datos$educ >= 16]
pob_resto <- datos$wage[datos$educ < 16]
stopifnot(length(pob_alta) > 1, length(pob_resto) > 1)
print(c(N_alta = length(pob_alta), N_resto = length(pob_resto)))

# P3-16 · Definir el sentido de la diferencia
mu_alta <- mean(pob_alta); mu_resto <- mean(pob_resto)
delta <- mu_alta-mu_resto
print(c(delta_didactica = delta))

# P3-17 · Sumar incertidumbre de dos medias
var_alta <- mean((pob_alta-mu_alta)^2)
var_resto <- mean((pob_resto-mu_resto)^2)
set.seed(16208)
n_a <- 144L; n_b <- 121L
m_a <- sample(pob_alta, n_a, replace = TRUE)
m_b <- sample(pob_resto, n_b, replace = TRUE)
diferencia <- mean(m_a)-mean(m_b)
se_diferencia <- sqrt(var_alta/n_a+var_resto/n_b)
print(c(estimacion = diferencia, error_estandar = se_diferencia))

# P3-18 · Cerrar con una conclusión honesta
ic_d <- diferencia+c(-1,1)*qnorm(.975)*se_diferencia
print(c(inferior = ic_d[1], superior = ic_d[2], delta_didactica = delta,
        contiene_cero = ic_d[1] <= 0 && ic_d[2] >= 0))
plot(range(c(ic_d,0)), c(0,1), type = "n", yaxt = "n", ylab = "",
     xlab = "Diferencia de medias (USD/h de 1976)", main = "Alta educación menos resto")
segments(ic_d[1],.5,ic_d[2],.5,lwd = 3,col = "#35618A")
points(diferencia,.5,pch = 19); abline(v = 0,lty = 2)

cat("Todas las actividades finalizaron. Revise también gráficos e interpretaciones.\n")
sessionInfo()
