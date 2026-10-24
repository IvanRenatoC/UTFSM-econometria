# Restricciones: 100 lanzamientos, como máximo 20 tandas,
# y entre 1 y 20 lanzamientos en cada tanda.
meta <- 100
max_tandas <- 20
max_lanzamientos <- 20
# Tiempos en décimas de segundo: evita errores de redondeo.
tiempo_tanda <- numeric(max_lanzamientos)
for (k in 1:max_lanzamientos) {
  for (j in 1:k) {
    tiempo_tanda[k] <- tiempo_tanda[k] + 11 + 3 * j
  }
}

# Guardamos en vectores los estados (n lanzamientos, b tandas exactas).
# Cada grupo de meta+1 posiciones corresponde a una cantidad de tandas.
posicion <- function(n, b) {
  n + 1 + b * (meta + 1)
}
mejor <- rep(Inf, (meta + 1) * (max_tandas + 1))
elegida <- numeric(length(mejor))
mejor[posicion(0, 0)] <- 0
for (b in 1:max_tandas) {
  for (n in 1:meta) {
    for (k in 1:min(max_lanzamientos, n)) {
      descanso <- 0
      if (k < n) {
        descanso <- 30 * k
      }
      candidato <- tiempo_tanda[k] + descanso + mejor[posicion(n - k, b - 1)]
      if (candidato < mejor[posicion(n, b)]) {
        mejor[posicion(n, b)] <- candidato
        elegida[posicion(n, b)] <- k
      }
    }
  }
}
# Elegir entre todas las cantidades permitidas de tandas, no imponer 20.
tiempo_final <- numeric(max_tandas)
for (b in 1:max_tandas) {
  tiempo_final[b] <- mejor[posicion(meta, b)]
}
if (!any(is.finite(tiempo_final))) {
  stop("No existe un plan que cumpla estas restricciones.")
}
b_optimo <- which.min(tiempo_final)

# Recuperar la sucesión óptima.
tandas <- numeric(b_optimo)
pendientes <- meta
b_restantes <- b_optimo
i <- 0
while (pendientes > 0) {
  i <- i + 1
  k <- elegida[posicion(pendientes, b_restantes)]
  tandas[i] <- k
  pendientes <- pendientes - k
  b_restantes <- b_restantes - 1
}
ejecucion <- tiempo_tanda[tandas] / 10
descansos <- 3 * tandas
descansos[length(tandas)] <- 0
registro <- data.frame(
  tanda = seq_along(tandas), lanzamientos = tandas,
  acumulado = cumsum(tandas), ejecucion_seg = ejecucion,
  descanso_seg = descansos,
  tiempo_acumulado_seg = cumsum(ejecucion + descansos)
)
print(registro)
print(tandas)
cat("Tiempo mínimo:", tiempo_final[b_optimo] / 10, "segundos\n")
cat("Tandas:", length(tandas), "| Descansos:", length(tandas) - 1, "\n")
cat("Tiempo lanzando:", sum(ejecucion), "| Tiempo descansando:", sum(descansos), "\n")
stopifnot(sum(tandas) == meta, length(tandas) <= max_tandas,
          all(tandas >= 1 & tandas <= max_lanzamientos),
          b_restantes == 0,
          abs(sum(ejecucion + descansos) - tiempo_final[b_optimo] / 10) < 1e-9)
