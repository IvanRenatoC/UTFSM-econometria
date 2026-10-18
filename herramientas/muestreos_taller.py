"""Ejemplos propios en R, en el orden de los muestreos de Sebastián."""
PREPARACION = '''# Ejecuta esta preparación una vez antes de los cuatro ejemplos.
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos <- as.data.frame(wooldridge::wage1)
datos$educ16 <- datos$educ >= 16
N <- nrow(datos)
marco <- 1:N
set.seed(36)'''
EJEMPLOS = [
 dict(title='Muestreo aleatorio simple',
      description='Sorteamos 24 personas sin reemplazo. Cada fila de la base tiene la misma probabilidad de ser incluida.',
      code='''ids_simple <- sample(marco, size = 24, replace = FALSE)
muestra_simple <- datos[ids_simple, ]
print(muestra_simple[c("wage", "educ", "female")])''',
      reading='Se obtienen 24 filas distintas. set.seed() permite repetir la selección cuando se ejecuta la preparación y luego los ejemplos en el mismo orden.'),
 dict(title='Muestreo aleatorio sistemático',
      description='Conservamos el orden de las filas, sorteamos el inicio entre 1 y 20 y elegimos después una de cada 20 personas.',
      code='''k <- 20
inicio <- sample(1:k, size = 1)
ids_sistema <- seq(inicio, N, by = k)
muestra_sistematica <- datos[ids_sistema, ]
print(muestra_sistematica[c("wage", "educ", "female")])''',
      reading='El tamaño será 26 o 27 personas. Con este inicio aleatorio, cada fila tiene probabilidad 1/20 de entrar antes de realizar el sorteo. Por eso es un diseño probabilístico, aunque no permite todas las combinaciones de una muestra aleatoria simple. Una vez fijado el inicio, las demás posiciones quedan determinadas. El orden de la lista y posibles patrones periódicos importan.'),
 dict(title='Muestreo aleatorio estratificado',
      description='Dividimos la base en dos estratos de educación: menos de 16 años y 16 años o más. Sorteamos 12 personas dentro de cada uno.',
      code='''estrato_menos16 <- which(!datos$educ16)
estrato_16omas <- which(datos$educ16)
ids_estrato <- c(sample(estrato_menos16, size = 12),
                 sample(estrato_16omas, size = 12))
muestra_estratificada <- datos[ids_estrato, ]
print(table(muestra_estratificada$educ16))
print(muestra_estratificada[c("wage", "educ")])''',
      reading='Participan ambos estratos: 12 personas de cada uno. Como sus tamaños en la base son distintos (427 y 99), seleccionar la misma cantidad no conserva sus proporciones. Para estimar una media global con este diseño habría que ponderar por el tamaño de cada estrato.'),
 dict(title='Muestreo por conglomerados (cluster)',
      description='Creamos 12 grupos artificiales y realizamos un muestreo de dos etapas: primero sorteamos dos grupos y luego sorteamos 12 personas dentro de cada grupo elegido. Los grupos son didácticos y no representan barrios o escuelas reales de la CPS.',
      code='''grupo_artificial <- rep(1:12, length.out = N)
elegidos <- sample(unique(grupo_artificial), size = 2)

# Segunda etapa: seleccionar personas dentro de los grupos elegidos.
personas_grupo1 <- which(grupo_artificial == elegidos[1])
personas_grupo2 <- which(grupo_artificial == elegidos[2])
ids_conglomerado <- c(sample(personas_grupo1, size = 12),
                     sample(personas_grupo2, size = 12))
muestra_conglomerados <- datos[ids_conglomerado, ]
print(elegidos)
print(table(grupo_artificial[ids_conglomerado]))
print(muestra_conglomerados[c("wage", "educ", "female")])''',
      reading='La muestra tiene 24 personas: 12 de cada uno de los dos grupos sorteados. En el estratificado entran personas de todos los estratos; aquí solo de los conglomerados elegidos. Si incluyéramos a todas las personas de esos grupos, sería un diseño de una etapa. Los grupos artificiales permiten ilustrar el algoritmo, no evaluar la eficiencia de un diseño geográfico real.')
]
