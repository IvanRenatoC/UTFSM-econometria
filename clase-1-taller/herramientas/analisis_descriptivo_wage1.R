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
