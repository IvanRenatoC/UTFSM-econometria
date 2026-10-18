"""Ejemplos propios en R, en el orden de los muestreos de Sebastián."""
PREPARACION = '''# Ejecuta esta preparación una vez antes de los cinco ejemplos.
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
      reading='El tamaño será 26 o 27 personas. Es un diseño probabilístico con inicio aleatorio, aunque no permite todas las combinaciones posibles de una muestra aleatoria simple. El orden de la lista y posibles patrones periódicos importan.'),
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
 dict(title='Muestreo por conglomerados',
      description='Creamos 12 grupos artificiales, sorteamos dos y conservamos todas las personas de los grupos elegidos. Es una ilustración de conglomerados de una etapa; los grupos no representan geografía real de la encuesta.',
      code='''grupo_artificial <- rep(1:12, length.out = N)
elegidos <- sample(unique(grupo_artificial), size = 2)
ids_conglomerado <- which(grupo_artificial %in% elegidos)
muestra_conglomerados <- datos[ids_conglomerado, ]
print(elegidos)
print(table(grupo_artificial[ids_conglomerado]))
print(muestra_conglomerados[c("wage", "educ", "female")])''',
      reading='Solo entran dos grupos, pero entran completos. La diferencia con estratificar es que no seleccionamos personas dentro de todos los grupos. En un diseño de dos etapas podríamos sortear personas dentro de los conglomerados elegidos.'),
 dict(title='Muestreo no probabilístico',
      description='Elegimos por criterio y orden disponible: las primeras 12 personas con al menos 16 años de educación. Aquí no se realiza un sorteo.',
      code='''ids_conveniencia <- head(which(datos$educ16), 12)
muestra_no_probabilistica <- datos[ids_conveniencia, ]
print(muestra_no_probabilistica[c("wage", "educ", "female")])''',
      reading='La selección depende del criterio y del orden de la base. Las personas con menos de 16 años quedan fuera, de modo que no podemos tratar esta selección como una muestra aleatoria de las 526 personas.')
]
