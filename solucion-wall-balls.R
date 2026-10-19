# Tiempos en décimas de segundo para comparar valores exactos.
meta <- 100
max_tanda <- 20
# El lanzamiento j tarda 11 + 3*j décimas.
tiempo_tanda <- numeric(max_tanda)
for (k in 1:max_tanda) {
  for (j in 1:k) {
    tiempo_tanda[k] <- tiempo_tanda[k] + 11 + 3 * j
  }
}

# mejor[n+1]: mínimo tiempo para completar n lanzamientos,
# sin descanso después del último. mejor[1] corresponde a n = 0.
mejor <- rep(Inf, meta + 1)
elegida <- numeric(meta + 1)
mejor[1] <- 0
for (n in 1:meta) {
  for (k in 1:min(max_tanda, n)) {
    descanso <- 0
    if (k < n) {
      descanso <- 30 * k
    }
    candidato <- tiempo_tanda[k] + descanso + mejor[n - k + 1]
    if (candidato < mejor[n + 1]) {
      mejor[n + 1] <- candidato
      elegida[n + 1] <- k
    }
  }
}

# Recuperar las tandas elegidas desde el problema de 100 lanzamientos.
tandas <- numeric(meta)  # A lo sumo, 100 tandas de un lanzamiento.
pendientes <- meta
b <- 0
while (pendientes > 0) {
  b <- b + 1
  tandas[b] <- elegida[pendientes + 1]
  pendientes <- pendientes - tandas[b]
}
tandas <- tandas[1:b]
# Un descanso después de cada tanda, excepto la última.
ejecucion <- tiempo_tanda[tandas] / 10
descansos <- 3 * tandas
descansos[b] <- 0
registro <- data.frame(
  tanda = 1:b, lanzamientos = tandas,
  acumulado = cumsum(tandas),
  ejecucion_seg = ejecucion, descanso_seg = descansos,
  tiempo_acumulado_seg = cumsum(ejecucion + descansos)
)
print(registro)
print(tandas)
cat("Tiempo mínimo:", mejor[meta + 1] / 10, "segundos\n")
cat("Tandas:", b, "| Descansos:", b - 1, "\n")
cat("Tiempo lanzando:", sum(ejecucion), "| Tiempo descansando:", sum(descansos), "\n")
stopifnot(sum(tandas) == meta, all(tandas >= 1 & tandas <= max_tanda),
          abs(sum(ejecucion + descansos) - mejor[meta + 1] / 10) < 1e-9)
