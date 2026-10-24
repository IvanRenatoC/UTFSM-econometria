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
