from pathlib import Path
import json, csv, hashlib
root=Path(__file__).resolve().parent.parent
activities=[]
def add(id,title,slides,question,predict,task,code,answer,error,check,mode='Ampliación autónoma',starter=''):
 activities.append(dict(id=id,title=title,slides=slides,question=question,predict=predict,task=task,code=code.strip(),answer=answer,error=error,check=check,mode=mode,starter=starter))
add('NIV-01','Escribe tu nombre','Nivelación','Vamos a hacer un ejercicio muy elemental, para que vayamos partiendo desde el inicio para terminar en algo mucho más avanzado.','¿Qué crees que aparecerá en la consola al ejecutar print("tu nombre")?','Reemplaza tu nombre por tu propio nombre, conservando las comillas, y ejecuta la instrucción.','print("tu nombre")','print() muestra el texto entre comillas en la consola. Al reemplazarlo por tu nombre, R imprimirá ese nombre.','Escribir el nombre sin comillas: R intentará interpretarlo como un objeto.','¿Qué debes cambiar para mostrar otro nombre? El texto que está dentro de las comillas.','Presencial')
add('NIV-02','Reserva y llena un vector','Nivelación','¿Cómo guardamos varios valores?','¿Qué posición contiene 6?','Crea tres valores, selecciona los mayores que 4 y modifica la segunda posición.','v <- numeric(3)\nv[1] <- 2; v[2] <- 6; v[3] <- 9\nprint(v[v > 4])\nv[2] <- 7\nprint(v); print(length(v))','R cuenta posiciones desde 1. El resultado final es 2, 7, 9; un vector reúne elementos del mismo tipo.','Usar el índice 0 como primera posición.','¿length(v) cambia al modificar v[2]? No.','Presencial')
add('NIV-03','Tomar una decisión','Nivelación','¿Cómo elegimos una acción según una condición?','¿Qué mensaje produce valor = 8?','Prueba con 3 y con 8; selecciona además todos los valores mayores que 4 del vector anterior.','valor <- 8\nif (valor > 4) {\n  mensaje <- "Supera el umbral"\n} else {\n  mensaje <- "No supera el umbral"\n}\nprint(mensaje)\nprint(v[v > 4])','if elige un camino con una condición única. La selección lógica trabaja con varias posiciones. Usa & y | para condiciones por elemento, && y || para condiciones escalares.','Escribir if(v > 4), con una condición por cada elemento.','¿valor > 4 es una asignación? No, es una comparación.','Presencial')
add('NIV-04','Repetir con for','Nivelación','¿Cómo evitamos escribir cada asignación?','¿Cuáles serán el primer y último término?','Llena cinco posiciones con el doble de su índice; amplía a ocho.','dobles <- numeric(5)\nfor (i in seq_along(dobles)) {\n  dobles[i] <- 2 * i\n}\nprint(dobles)','La salida con cinco posiciones es 2, 4, 6, 8, 10. Se reserva espacio antes del ciclo.','Llenar un objeto inexistente o recorrer más índices de los reservados.','¿Qué cambia al reservar numeric(8)? Se calculan ocho términos.','Presencial')
add('NIV-05','Tres sucesiones','Nivelación','¿Cómo se calcula un término desde el anterior?','Predice los cuatro primeros términos de cada sucesión.','Construye seis términos: aritmética con inicio 2 y paso 3; geométrica con inicio 2 y razón 2; recurrencia con inicio 1 y a[i] = 2*a[i-1]+1.','a <- g <- r <- numeric(6)\na[1] <- 2; g[1] <- 2; r[1] <- 1\nfor (i in 2:length(a)) {\n  a[i] <- a[i-1] + 3\n  g[i] <- 2 * g[i-1]\n  r[i] <- 2 * r[i-1] + 1\n}\nprint(rbind(aritmetica = a, geometrica = g, recurrencia = r))\nstopifnot(all(a == 2 + 3 * (seq_along(a)-1)),\n          all(g == 2 * 2^(seq_along(g)-1)))','Las fórmulas vectorizadas comprueban las dos primeras sucesiones. La recurrencia exige inicializar el primer valor. Aquí se garantiza longitud 6 antes de usar 2:length(a).','Olvidar el primer término o aplicar 2:n cuando n podría ser menor que 2.','¿Cuál es el tercer término de la recurrencia? 7.','Presencial')
add('NIV-06','Un while que termina','Nivelación','¿Cuántas duplicaciones hacen falta para llegar a 100?','¿Se detendrá antes de 20 pasos?','Parte en 1, duplica hasta alcanzar 100 y conserva los términos.','valor <- 1\npaso <- 0L\nmax_pasos <- 20L\ntrayectoria <- numeric(max_pasos + 1L)\ntrayectoria[1] <- valor\nwhile (valor < 100 && paso < max_pasos) {\n  valor <- 2 * valor\n  paso <- paso + 1L\n  trayectoria[paso + 1L] <- valor\n}\nprint(trayectoria[seq_len(paso + 1L)])\nprint(c(pasos = paso, valor = valor))','Se llega a 128 en siete duplicaciones. El límite adicional protege de una condición mal planteada.','No actualizar valor o paso.','¿Qué ocurre si max_pasos es 3? Termina por el límite, sin llegar a 100.','Presencial')
add('NIV-07','Una matriz, dos índices','Nivelación','¿Cómo guardamos resultados por filas y columnas?','¿Cuánto valdrá la posición [2,3]?','Llena una matriz 2 por 3 con 10*fila + columna; luego modifica [1,1].','m <- matrix(0, nrow = 2, ncol = 3)\nfor (i in seq_len(nrow(m))) {\n  for (j in seq_len(ncol(m))) {\n    m[i,j] <- 10*i + j\n  }\n}\nprint(m)\nm[1,1] <- 99\nprint(m); print(dim(m))','La posición [2,3] vale 23 antes y después de modificar [1,1]. Una matriz tiene un tipo común; un data.frame permite columnas de distintos tipos.','Intercambiar fila y columna.','¿m[2,3] y m[3,2] son siempre válidos? No: solo hay dos filas.','Presencial')
add('NIV-08','Integra: término y clasificación','Nivelación','¿Podemos reunir una sucesión y una decisión?','¿Desde qué término se supera 10?','Genera 2,5,8,11,14,17 y guarda índice, valor e indicador de superar 10.','terminos <- numeric(6)\nterminos[1] <- 2\nfor (i in 2:length(terminos)) terminos[i] <- terminos[i-1] + 3\nresultado <- matrix(0, nrow = 6, ncol = 3,\n                    dimnames = list(NULL, c("indice", "valor", "supera_10")))\nfor (i in seq_along(terminos)) {\n  resultado[i,1] <- i\n  resultado[i,2] <- terminos[i]\n  if (terminos[i] > 10) resultado[i,3] <- 1\n}\nprint(resultado)','El indicador vale 1 desde el cuarto término. Esta es programación con objetos artificiales, no evidencia económica.','Asignar una cadena de texto a una matriz numérica y convertir toda la matriz a texto.','¿Qué cambia con umbral 14 y condición estricta >? Solo el último indicador vale 1.','Presencial')
load='''# La copia local permite trabajar sin conexión.
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
'''
add('P1-01','¿Qué podemos preguntar a los datos?','Parte 1 · lámina 1','¿Qué sabemos de educación y salario de cada persona?','¿Cada fila representa una persona o un mes?','Carga la base e identifica wage y educ en seis filas.',load,'wage1 es un corte transversal observacional de Estados Unidos en 1976. wage es remuneración por hora en dólares nominales de ese período; educ son años de educación. No son pesos chilenos actuales. La inspección no prueba efectos.','Confundir índice de fila con tiempo o borrar faltantes sin informar cuántos.','¿526 filas equivalen a 526 períodos? No.','Presencial')
add('P1-02','Tres preguntas distintas','Parte 1 · lámina 2','¿Describir, explicar una causa o predecir?','Clasifica: ¿quién gana más?, ¿estudiar cambia el salario?, ¿cuánto ganará alguien?','Asocia cada pregunta con una finalidad.','preguntas <- data.frame(\n  pregunta = c("¿Cómo se relacionan educación y salario?",\n               "¿Más educación causa mayor salario?",\n               "¿Qué salario tendrá otra persona?"),\n  finalidad = c("Descripción", "Causalidad", "Predicción"))\nprint(preguntas)','Una misma tabla permite formular preguntas distintas, pero no garantiza resolverlas todas. Aquí no entrenamos predictores ni estimamos efectos.','Tratar una predicción acertada como identificación causal.','¿Una pregunta causal requiere supuestos adicionales? Sí.','Presencial')
add('P1-03','De la pregunta a las columnas','Parte 1 · lámina 3','¿Qué parte del modelo conceptual observamos?','¿Está la habilidad directamente medida en estas columnas?','Distingue salario, educación, experiencia y factores no observados.','print(names(datos))\nprint(head(datos[c("wage", "educ", "exper")]))','Una formulación conceptual es salario = f(educación, experiencia, otros factores) + error. Habilidad y recursos familiares no se identifican en estas columnas. No estimamos f.','Interpretar el error como un simple error de digitación.','¿Que una variable no esté en la tabla significa que no importa? No.','Presencial')
add('P1-04','Mirar una asociación','Parte 1 · lámina 4','¿Una nube ascendente demuestra una causa?','¿Podrían existir personas con igual educación y salarios diferentes?','Dibuja salario frente a educación y propón dos factores adicionales.','plot(datos$educ, datos$wage, pch = 19, col = "#35618A80",\n     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)",\n     main = "Educación y salario: observar no es aislar una causa")','Cada punto es una persona. La comparación no mantiene constantes habilidad, ocupación o experiencia. La temperatura en el caso de helados y tiburones de cátedra ilustra el mismo problema de un factor común.','Dibujar una flecha causal solo por observar una asociación.','¿El gráfico mantiene todo lo demás constante? No.','Presencial')
add('P1-05','Educación: grupos con límites','Parte 1 · láminas 5–6','¿Podemos llamar universitario a todo registro con educ >= 16?','¿Los dos grupos serán idénticos en sus otras características?','Crea una etiqueta de umbral educativo y examina filas, sin calcular todavía diferencias de medias.','datos$educ16 <- datos$educ >= 16\nprint(head(datos[c("educ", "educ16", "wage", "exper")], 12))','educ >= 16 es un umbral de años de educación, no una certificación de título. El ejemplo del 30% de Chile pertenece a cátedra; no se atribuye a esta base. La comparación de promedios se hará en su bloque.','Repetir el 30% como si se hubiese calculado con wage1.','¿Una diferencia entre grupos sería automáticamente efecto de estudiar? No.','Presencial')
add('P1-06','La base correcta para cada pregunta','Parte 1 · lámina 7','¿wage1 permite medir el efecto de pastillas escolares o consultorías?','¿Qué columnas faltarían?','Escribe en R los datos que pedirías para cada estudio.','necesidades <- list(\n  desparasitacion = c("asignación", "tratamiento", "asistencia", "escuela"),\n  consultoria = c("asignación", "consultoría", "productividad", "fábrica"))\nprint(necesidades)','Los casos de Kenia e India de cátedra muestran el papel del diseño. wage1 no contiene sus tratamientos ni resultados; no calculamos esos estudios con salarios.','Inventar una variable de tratamiento para atribuir resultados de otro estudio.','¿Basta una tabla grande para responder cualquier pregunta? No.')
add('P1-07','La forma de la tabla','Parte 1 · láminas 8–11','¿Qué dimensiones definen nuestros datos?','¿Tenemos observaciones repetidas de cada persona en varios años?','Construye un esquema conceptual de las tres estructuras.','estructuras <- data.frame(\n  tipo = c("Corte transversal", "Serie temporal", "Panel"),\n  unidades = c("Muchas", "Una", "Muchas"),\n  periodos = c("Uno", "Varios", "Varios por unidad"))\nprint(estructuras)','La base de aplicación es transversal y observacional. Lo experimental describe cómo se asigna una exposición; panel describe la estructura. Los esquemas no son nuevas bases empíricas.','Suponer que toda base transversal fue obtenida por muestreo aleatorio simple.','¿Experimental y transversal son categorías incompatibles? No.','Presencial')
add('P1-08','Una población didáctica','Parte 1 · láminas 12–13','¿De qué conjunto seleccionaremos personas?','¿Una submuestra representa automáticamente a Estados Unidos?','Define el marco de filas de datos y extrae 12 registros sin reemplazo.','set.seed(16201)\nN <- nrow(datos)\nmarco <- seq_len(N)\nids <- sample(marco, size = 12, replace = FALSE)\nprint(datos[ids, c("wage", "educ")])','Tratamos la tabla completa como población finita didáctica. Su encuesta original tiene otra población y diseño; nuestro submuestreo no los reproduce.','Llamar población real completa a las 526 observaciones.','¿Cuál es nuestra unidad de observación? La persona registrada.','Presencial')
add('P1-09','¿Por qué no observar a todos?','Parte 1 · lámina 14','¿Cómo limita el presupuesto el número de entrevistas?','Si cada entrevista cuesta 5 unidades, ¿alcanzan 100 para toda la tabla?','Calcula cuántas entrevistas financia ese presupuesto.','presupuesto <- 100\ncosto <- 5\ncapacidad <- floor(presupuesto/costo)\nprint(capacidad)','Son 20 entrevistas bajo costos hipotéticos, un ejercicio de planificación con el marco real. Un presupuesto no define por sí solo un buen diseño.','Confundir capacidad de entrevistar con representatividad.','¿Una muestra barata garantiza precisión? No.')
add('P1-10','¿Qué queremos estimar?','Parte 1 · lámina 15','¿Es lo mismo una variable que un parámetro?','¿El salario de una persona es un promedio poblacional?','Clasifica variable, parámetro objetivo y estadístico.','print(data.frame(\n  concepto = c("Variable", "Parámetro", "Estadístico"),\n  ejemplo = c("Salario por hora individual",\n              "Media salarial de la población objetivo",\n              "Media salarial calculada en una muestra")))','La variable se observa por persona; el parámetro resume una población; el estadístico depende de la muestra. Las fórmulas vienen después.','Llamar parámetro a cualquier número de una fila.','¿Un estadístico cambia al cambiar la muestra? Generalmente sí.')
add('P1-11','Cuatro formas de seleccionar','Parte 1 · láminas 16–17','¿Cómo cambia quién entra según el método?','¿Estratificar garantiza que ambos grupos definidos tengan participantes?','Selecciona por cuatro algoritmos y conserva sus índices.','set.seed(16202)\nids_simple <- sample(marco, 24)\nk <- 20L\ninicio <- sample.int(k, 1)\nids_sistema <- seq.int(inicio, N, by = k)\nestratos <- split(marco, datos$educ16)\nstopifnot(all(lengths(estratos) >= 12))\nids_estrato <- unlist(lapply(estratos, function(g) sample(g, 12)), use.names = FALSE)\n# Grupos artificiales: ilustración algorítmica, no barrios reales.\ngrupo_artificial <- rep(seq_len(12), length.out = N)\nelegidos <- sample(unique(grupo_artificial), 2)\nids_conglomerado <- which(grupo_artificial %in% elegidos)\nprint(list(simple = ids_simple, sistematico = ids_sistema,\n           estratificado = ids_estrato, conglomerados = ids_conglomerado))','El sistemático usa inicio aleatorio; su tamaño puede variar aquí. Los grupos artificiales no sustentan una comparación real de eficiencia. La afijación igual por estrato requeriría ponderar al estimar una media global si difieren los tamaños; aquí solo seleccionamos.','Comparar precisión de diseños con tamaños distintos o usar media estratificada no ponderada como estimador global.','¿El sistemático deja de ser probabilístico porque solo se sortea el inicio? No.','Presencial')
add('P1-12','Dentro de todos o algunos grupos','Parte 1 · lámina 18','¿En qué se diferencian estratos y conglomerados?','¿En qué selección aparecen todos los estratos?','Inspecciona los grupos incluidos por cada selección.','print(table(datos$educ16[ids_estrato]))\nprint(table(grupo_artificial[ids_conglomerado]))','Estratificar selecciona dentro de todos los estratos; conglomerados selecciona algunos grupos. Homogeneidad y heterogeneidad son criterios didácticos, no definiciones universales.','Presentar grupos artificiales como geografía de la encuesta.','¿Conglomerados puede tener una segunda etapa de muestreo? Sí.')
add('P1-13','Seleccionar por conveniencia','Parte 1 · lámina 19','¿Qué sucede si solo invitamos a quienes tienen al menos 16 años de educación?','¿Quién queda sin oportunidad de selección?','Selecciona las primeras 12 filas que cumplen ese criterio.','ids_conveniencia <- head(which(datos$educ16), 12)\nprint(datos[ids_conveniencia, c("wage", "educ")])','Es una selección por criterio y orden disponible, no una muestra probabilística del conjunto. Una muestra grande no elimina sesgos de cobertura o respuesta, como ilustra Literary Digest en la web.','Generalizar sin supuestos a quienes quedaron fuera.','¿Conocer el criterio equivale a conocer probabilidades de selección aleatoria? No.','Presencial')
add('P1-14','La frontera entre resumir e inferir','Parte 1 · lámina 20','¿Describimos la tabla o hablamos de una población?','¿Decir “en estas filas” cambia el alcance?','Redacta una frase descriptiva y otra inferencial, identificando qué supuesto falta.','frases <- c("Describo los salarios de las filas observadas",\n            "Quiero estimar un promedio de una población definida")\nprint(frases)','La segunda frase exige definir población y mecanismo de muestreo. Continúa con la descripción antes de construir intervalos.','Generalizar sin identificar el universo.','¿La inferencia usa solo programación? No, también supuestos.','Presencial')
add('P2-01','Primero describir','Parte 2 · lámina 1','¿Qué puede decirnos una tabla antes de generalizar?','¿Un resumen de esta muestra es ya una ley general?','Selecciona la variable salarial y verifica su tamaño.','x <- datos$wage\nprint(length(x))','Descriptiva resume x; inferencia requiere un marco adicional. Los datos conservan sus unidades históricas.','Cambiar de población sin avisar.','¿Un histograma es descriptivo? Sí.')
add('P2-02','Una función resume muchos datos','Parte 2 · lámina 2','¿Qué entra y qué sale de un estadístico?','¿length devuelve un vector de 526 valores?','Construye un pequeño resumen de tamaño y rango observado.','resumen_inicial <- c(n = length(x), minimo = min(x), maximo = max(x))\nprint(resumen_inicial)','Cada función transforma el vector en un resultado. Un estadístico es una función de la muestra.','Confundir el vector de datos con su resumen.','¿max(x) conserva todas las observaciones? No.','Presencial')
add('P2-03','¿El sueldo típico es el promedio?','Parte 2 · láminas 3–4','¿Media y mediana reaccionan igual a un salario extremo?','¿Cuál cambiará más al añadir un valor enorme?','Calcula ambas y compara con una copia que añade un dato artificial.','centro <- function(z) c(media = mean(z), mediana = median(z))\nprint(centro(x))\nx_modificado <- c(x, 10*max(x))\nprint(rbind(original = centro(x), copia_con_extremo = centro(x_modificado)))\nordenados <- sort(x)\nn_x <- length(x)\nmediana_manual <- if (n_x %% 2 == 1) ordenados[(n_x+1)/2] else\n  (ordenados[n_x/2] + ordenados[n_x/2+1])/2\nstopifnot(isTRUE(all.equal(mediana_manual, median(x))))','La media es sensible a extremos. La mediana se obtiene de posiciones centrales; la copia modificada no es una nueva observación real.','Guardar el dato artificial sobre la base original.','¿La mediana exige ordenar conceptualmente los datos? Sí.','Presencial')
add('P2-04','Ubicarse en la distribución','Parte 2 · lámina 5','¿Dónde comienza el cuarto superior?','¿P50 coincide con la mediana?','Obtén cuartiles y el percentil 90 con interpolación tipo 7.','cuartiles <- quantile(x, probs = c(.25, .5, .75), type = 7)\nprint(cuartiles)\nprint(quantile(x, .9, type = 7))','Los cuartiles delimitan posiciones de la distribución; type=7 especifica la interpolación. Empates y convenciones pueden alterar recuentos exactos.','Interpretar P75 como el 75% del salario máximo.','¿P50 es la mitad del máximo? No.','Presencial')
add('P2-05','Cuánto se dispersan los salarios','Parte 2 · láminas 6–7','¿Dos muestras con la misma media pueden ser diferentes?','¿Varianza y salario tienen las mismas unidades?','Calcula RIQ, varianza muestral y desviación estándar; verifica manualmente.','print(c(RIQ = IQR(x, type = 7), varianza = var(x), desviacion = sd(x)))\ns2_manual <- sum((x-mean(x))^2)/(length(x)-1)\nstopifnot(isTRUE(all.equal(s2_manual, var(x))))','La varianza usa unidades al cuadrado y n-1; sd conserva USD por hora. RIQ mide la separación entre P75 y P25.','Confundir desviación estándar con error estándar de la media.','¿sd(x) disminuye necesariamente cuando aumenta n? No.','Presencial')
add('P2-06','Un histograma, varias decisiones','Parte 2 · lámina 8','¿Cambian los datos cuando cambiamos los intervalos?','¿Esperas ver la misma apariencia con 5 y 20 cortes sugeridos?','Dibuja dos histogramas y compara forma y frecuencias.','op <- par(mfrow = c(1,2))\nfor (b in c(5,20)) hist(x, breaks = b, col = "#7DB4B5",\n  main = paste("Cortes sugeridos:", b),\n  xlab = "Salario por hora (USD de 1976)", ylab = "Frecuencia")\npar(op)','breaks numérico es una sugerencia a R, que elige límites convenientes. La forma visual cambia aunque la muestra sea idéntica.','Confundir barras de frecuencia con la lista de valores individuales.','¿Un histograma con otra anchura prueba otra población? No.','Presencial')
add('P2-07','Leer la caja y los bigotes','Parte 2 · láminas 9–10','¿Un punto fuera de los bigotes es un error?','¿Cuántos posibles atípicos crees que aparecerán?','Dibuja la caja, extrae sus límites y contrasta bisagras con cuartiles tipo 7.','boxplot(x, horizontal = TRUE, col = "#7DB4B5",\n  main = "Salarios: posición y dispersión", xlab = "USD por hora de 1976")\nbp <- boxplot.stats(x)\nprint(bp$stats); print(bp$out)\nprint(quantile(x, c(.25,.5,.75), type = 7))','R usa bisagras para la caja, que no siempre coinciden con quantile(type=7). Los bigotes terminan en observaciones dentro de 1,5 veces el rango entre bisagras; las cercas no son necesariamente datos. Un atípico requiere investigar, no borrar.','Eliminar automáticamente puntos extremos.','¿El bigote siempre termina justo en q3+1,5*RIQ? No.','Presencial')
add('P3-01','Conocer una población para aprender a inferir','Parte 3 · lámina 1','¿Cómo podemos evaluar un método si normalmente no conocemos la verdad?','¿Qué cambia si tratamos toda la tabla como una distribución conocida?','Define la distribución empírica de salarios y sus momentos poblacionales.','poblacion <- datos$wage\nmu <- mean(poblacion)\nsigma2 <- mean((poblacion-mu)^2)\nsigma <- sqrt(sigma2)\nprint(c(mu = mu, sigma = sigma, N = length(poblacion)))','Cada fila tiene probabilidad 1/N en esta distribución didáctica. Usamos denominador N; no afirmamos conocer la varianza salarial de todo Estados Unidos.','Llamar sigma a sd de la muestra sin justificar una población conocida.','¿Esta media es un parámetro de nuestra distribución didáctica? Sí.','Presencial')
add('P3-02','Un intervalo, una afirmación limitada','Parte 3 · lámina 2','¿Qué aporta un intervalo frente a un valor único?','¿Un intervalo ya calculado tiene parámetro aleatorio?','Escribe qué cambia al repetir el muestreo.','print(c("El parámetro didáctico permanece fijo",\n        "La muestra y sus límites cambian",\n        "La confianza describe el procedimiento"))','Como en los aros y la estaca de cátedra, mu permanece fijo y los intervalos cambian. La cobertura es una propiedad de repetición.','Decir que el 95% de las observaciones está dentro del IC de la media.','¿Un IC de media es un intervalo de salarios individuales? No.','Presencial')
add('P3-03','Muchas muestras, muchas medias','Parte 3 · lámina 3','¿Cómo se distribuye el promedio al repetir muestras?','¿Las medias de n=100 serán menos dispersas que las de n=5?','Extrae 1.000 muestras por tamaño, independientes y con reemplazo.','set.seed(16203)\nB <- 1000L\nop <- par(mfrow = c(1,2))\nfor (n in c(5,100)) {\n  medias <- replicate(B, mean(sample(poblacion, n, replace = TRUE)))\n  hist(medias, probability = TRUE, breaks = 25, col = "#7DB4B5",\n       main = paste("Medias con n =", n), xlab = "Media salarial (USD/h)")\n  curve(dnorm(x, mu, sigma/sqrt(n)), add = TRUE, col = "#BD4C45", lwd = 2)\n  print(c(n = n, media_medias = mean(medias),\n          sd_medias = sd(medias), error_teorico = sigma/sqrt(n)))\n}\npar(op)','La comparación usa muestras de una población empírica conocida, no remuestreo de una muestra para estimar un parámetro desconocido. El TCL aproxima la forma de la distribución de medias.','Confundir salarios individuales con medias muestrales.','¿sigma/sqrt(n) es la desviación de salarios? No, de la media.','Presencial')
add('P3-04','Cuándo confiar en la aproximación','Parte 3 · lámina 4','¿n=30 garantiza normalidad en cualquier caso?','¿La asimetría afecta la rapidez de aproximación?','Comprueba que los datos utilizados son finitos y revisa el mecanismo de muestreo.','stopifnot(all(is.finite(poblacion)), sigma2 > 0)\nprint(c(media_finita = is.finite(mu), varianza_finita = is.finite(sigma2)))','Con reemplazo cada extracción tiene la misma distribución y es independiente. Los umbrales de tamaño son orientativos. Si la población fuera normal, su media muestral sería normal para cualquier n.','Tratar 30, 50 o 100 como garantías universales.','¿El ciclo por sí solo demuestra independencia en la encuesta original? No.')
add('P3-05','El primer intervalo salarial','Parte 3 · láminas 5–7','¿Cómo estimamos mu con una muestra de 36 salarios?','¿El resultado quedará centrado en mu o en la media de la muestra?','Extrae 36 observaciones y calcula el intervalo normal de 95% con sigma conocida didáctica.','set.seed(16204)\nn_ic <- 36L\nmuestra_ic <- sample(poblacion, n_ic, replace = TRUE)\nxbarra <- mean(muestra_ic)\nz95 <- qnorm(.975)\nse <- sigma/sqrt(n_ic)\nic95 <- xbarra + c(-1,1)*z95*se\nprint(c(estimacion = xbarra, error_estandar = se,\n        inferior = ic95[1], superior = ic95[2], mu_didactica = mu))','Es un ejercicio propio con wage1, análogo al ejemplo de ventas; no reproduce su media 200 ni su sigma 60. La cobertura normal aquí es aproximada.','Atribuir los números de ventas del sitio a la base salarial.','¿Cuál es el centro del intervalo? xbarra.','Presencial')
add('P3-06','Desarmar el IC de 95%','Parte 3 · lámina 8','¿Qué papel tiene cada pieza?','¿Qué ocurre al duplicar sigma y conservar lo demás?','Separa estimación, valor crítico, error estándar y margen.','margen95 <- z95*se\nprint(c(estimacion = xbarra, z = z95, se = se, margen = margen95))\nstopifnot(isTRUE(all.equal(diff(ic95), 2*margen95)))','El margen es z por error estándar; la longitud total es el doble del margen.','Usar el margen como si fuera longitud total.','¿Duplicar sigma duplica el margen? Sí.')
add('P3-07','Cambiar solo la confianza','Parte 3 · láminas 9–10','¿Qué cambia al pasar a 99%?','¿El centro debería moverse?','Calcula 90%, 95% y 99% para la misma muestra.','niveles <- c(.90,.95,.99)\nz <- qnorm((1+niveles)/2)\nlimites <- cbind(inferior = xbarra-z*se, superior = xbarra+z*se)\nrownames(limites) <- paste0(100*niveles, "%")\nprint(limites)','Se utiliza el cuantil superior positivo; el centro se conserva. qnorm evita inconsistencias por redondeo de 2,57 o 2,58.','Extraer otra muestra y atribuir todo cambio a la confianza.','¿Qué intervalo es más ancho? El de 99%.','Presencial')
add('P3-08','Ver la anchura','Parte 3 · lámina 11','¿Podemos comparar los intervalos de un vistazo?','¿Cuál abarcará a los otros?','Representa los límites en una misma recta salarial.','plot(range(limites), c(1,3), type = "n", yaxt = "n",\n     xlab = "Media salarial (USD/h)", ylab = "Confianza",\n     main = "La misma muestra, distinta confianza")\naxis(2, at = 1:3, labels = rownames(limites))\nsegments(limites[,1], 1:3, limites[,2], 1:3, lwd = 3, col = "#35618A")\npoints(rep(xbarra,3), 1:3, pch = 19)','El intervalo mayor ofrece más cobertura bajo el modelo a costa de anchura.','Confundir intervalo más ancho con mejor precisión.','¿El centro de los tres es idéntico? Sí.')
add('P3-09','¿Qué significa 95% de confianza?','Parte 3 · láminas 12–13','¿Cuántos intervalos capturan la media conocida?','¿Se obtendrán exactamente 950 aciertos de 1.000?','Repite 1.000 veces y visualiza los primeros 100 intervalos.','set.seed(16205)\nmedias_ic <- replicate(1000, mean(sample(poblacion, n_ic, replace = TRUE)))\nL <- medias_ic-z95*se; U <- medias_ic+z95*se\ncubre <- L <= mu & mu <= U\nprint(c(cobertura_observada = mean(cubre), confianza_nominal = .95,\n        margen_n36 = margen95, margen_n144 = z95*sigma/sqrt(144)))\nj <- seq_len(100)\nplot(range(c(L[j],U[j],mu)), range(j), type = "n",\n     xlab = "Media salarial (USD/h)", ylab = "Muestra", main = "100 intervalos")\nsegments(L[j],j,U[j],j,col = ifelse(cubre[j],"#35618A","#BD4C45"))\nabline(v = mu, lty = 2)','La proporción observada fluctúa y la aproximación normal puede afectar cobertura. Cuadruplicar n reduce el margen a la mitad manteniendo confianza y sigma.','Prometer exactamente 95 aciertos en cada 100 muestras.','¿Un intervalo fallido demuestra que el código está mal? No.','Presencial')
add('P3-10','Planificar el tamaño para una media','Parte 3 · lámina 14','¿Cuántas observaciones para un margen de 0,5 USD/h?','¿Reducir el margen a la mitad duplicará n?','Despeja n y verifica el margen obtenido después de redondear.','E_media <- .5\nn_necesario <- ceiling((qnorm(.975)*sigma/E_media)^2)\nprint(c(n = n_necesario, margen = qnorm(.975)*sigma/sqrt(n_necesario)))','n crece con el inverso del margen al cuadrado. El muestreo con reemplazo puede requerir más extracciones que filas únicas. No es un plan validado para una encuesta nacional.','Redondear hacia abajo.','¿Reducir E a la mitad multiplica n por cuatro antes del redondeo? Sí.')
add('P3-11','Una proporción educativa','Parte 3 · láminas 15–19','¿Qué fracción tiene al menos 16 años de educación?','¿Puede una proporción ser mayor que 1?','Define el indicador, extrae n=200 y calcula el IC normal aproximado si se cumplen las condiciones.','indicador <- as.integer(datos$educ >= 16)\np_real <- mean(indicador)\nset.seed(16206)\nmuestra_p <- sample(indicador, 200, replace = TRUE)\nn_p <- length(muestra_p)\np_hat <- mean(muestra_p)\nexitos <- sum(muestra_p); fracasos <- n_p-exitos\nstopifnot(exitos > 5, fracasos > 5)\nse_p <- sqrt(p_hat*(1-p_hat)/n_p)\nic_p <- p_hat+c(-1,1)*qnorm(.975)*se_p\nprint(c(exitos = exitos, fracasos = fracasos, p_hat = p_hat,\n        inferior = ic_p[1], superior = ic_p[2], p_didactica = p_real))','El indicador es derivado, con definición explícita. Para aproximación poblacional se consideran np y n(1-p); los conteos observados sirven de diagnóstico práctico. Este intervalo de Wald puede funcionar mal cerca de 0 o 1; aquí no se amplían métodos.','Confundir “éxito” estadístico con juicio de valor o título universitario.','¿Un 1 representa exactamente qué? educ >= 16.','Presencial')
add('P3-12','¿Es compatible una referencia?','Parte 3 · láminas 20–21','¿La proporción de referencia 0,20 queda en el intervalo?','Predice mirando los límites anteriores.','Comprueba inclusión y escribe una conclusión bajo el modelo didáctico.','referencia <- .20\ncompatible <- ic_p[1] <= referencia && referencia <= ic_p[2]\nprint(c(referencia = referencia, dentro_del_IC = compatible))','Si queda fuera, hay evidencia de diferencia bajo los supuestos; si queda dentro, no se ha demostrado igualdad. La referencia es hipotética, no una afirmación publicada sobre Estados Unidos.','Convertir ausencia de evidencia en prueba de igualdad.','¿Que quede dentro prueba p=0,20? No.')
add('P3-13','Tamaño para una proporción','Parte 3 · lámina 22','¿Qué pasa si no tenemos estimación previa?','¿p=0,5 maximiza p(1-p)?','Compara el plan con p piloto y el conservador para margen 0,03.','E_p <- .03\nprint(c(con_piloto = ceiling(qnorm(.975)^2*p_hat*(1-p_hat)/E_p^2),\n        conservador = ceiling(qnorm(.975)^2*.25/E_p^2)))','Usar 0,5 maximiza la varianza Bernoulli. Una proporción piloto imprecisa puede producir un plan optimista.','Usar p_hat=0 como garantía de tamaño cero suficiente.','¿El plan conservador depende de observar éxitos en el piloto? No.')
add('P3-14','Longitud no es margen','Parte 3 · láminas 23–24','¿Cuántas extracciones para longitud total máxima 0,05?','¿El margen será 0,05 o 0,025?','Usa una muestra piloto de 30 indicadores educativos y compara con el caso conservador.','set.seed(16207)\npiloto <- sample(indicador, 30, replace = TRUE)\np_estrella <- mean(piloto)\nlongitud_max <- .05\nE_plan <- longitud_max/2\nn_plan <- ceiling(qnorm(.975)^2*p_estrella*(1-p_estrella)/E_plan^2)\nn_conservador <- ceiling(qnorm(.975)^2*.25/E_plan^2)\nprint(c(piloto = p_estrella, margen = E_plan, n_piloto = n_plan,\n        n_conservador = n_conservador))','Es un caso propio análogo a chips; el n del piloto es una planificación aproximada, no garantía de longitud real para toda muestra futura con varianza estimada.','Afirmar que el resultado debe ser 711 porque ese es el ejemplo de chips.','¿De dónde sale E=0,025? De dividir la longitud total por dos.')
add('P3-15','Comparar dos grupos educativos','Parte 3 · lámina 25','¿Cómo cambia el salario medio entre umbrales educativos?','¿Qué signo esperas para alta educación menos el resto?','Define las dos poblaciones empíricas sin mezclarlas.','pob_alta <- datos$wage[datos$educ >= 16]\npob_resto <- datos$wage[datos$educ < 16]\nstopifnot(length(pob_alta) > 1, length(pob_resto) > 1)\nprint(c(N_alta = length(pob_alta), N_resto = length(pob_resto)))','Los grupos son dos distribuciones empíricas para una comparación didáctica. No son carreras universitarias ni grupos aleatorizados.','Cambiar la definición de los grupos a mitad del ejercicio.','¿Los grupos se superponen? No.')
add('P3-16','Definir el sentido de la diferencia','Parte 3 · láminas 26–27','¿Qué significa que el intervalo incluya cero?','¿Qué pasa con el signo si invertimos el orden?','Define delta como media de alta educación menos media del resto.','mu_alta <- mean(pob_alta); mu_resto <- mean(pob_resto)\ndelta <- mu_alta-mu_resto\nprint(c(delta_didactica = delta))','Un intervalo que excluye cero aporta evidencia de diferencia bajo el procedimiento. Invertir el orden invierte el signo y los extremos correspondientes.','Interpretar incluir cero como demostrar igualdad.','¿Excluir cero prueba causalidad? No.')
add('P3-17','Sumar incertidumbre de dos medias','Parte 3 · láminas 28–31','¿Cómo se combina la incertidumbre de muestras independientes?','¿Se restan o se suman las varianzas?','Extrae 144 y 121 salarios con reemplazo de cada grupo; calcula el error estándar de la diferencia.','var_alta <- mean((pob_alta-mu_alta)^2)\nvar_resto <- mean((pob_resto-mu_resto)^2)\nset.seed(16208)\nn_a <- 144L; n_b <- 121L\nm_a <- sample(pob_alta, n_a, replace = TRUE)\nm_b <- sample(pob_resto, n_b, replace = TRUE)\ndiferencia <- mean(m_a)-mean(m_b)\nse_diferencia <- sqrt(var_alta/n_a+var_resto/n_b)\nprint(c(estimacion = diferencia, error_estandar = se_diferencia))','Las varianzas se suman por independencia aunque las medias se resten. Los momentos conocidos son de las distribuciones didácticas con denominador N de cada grupo.','Usar var(m_a) y llamarla varianza poblacional conocida.','¿Usar una sola muestra compartida garantizaría independencia? No.')
add('P3-18','Cerrar con una conclusión honesta','Parte 3 · láminas 32–34','¿La diferencia es compatible con cero?','¿Tu conclusión cambia si hablas de causa?','Calcula límites y escribe dos frases: resultado e interpretación limitada.','ic_d <- diferencia+c(-1,1)*qnorm(.975)*se_diferencia\nprint(c(inferior = ic_d[1], superior = ic_d[2], delta_didactica = delta,\n        contiene_cero = ic_d[1] <= 0 && ic_d[2] >= 0))\nplot(range(c(ic_d,0)), c(0,1), type = "n", yaxt = "n", ylab = "",\n     xlab = "Diferencia de medias (USD/h de 1976)", main = "Alta educación menos resto")\nsegments(ic_d[1],.5,ic_d[2],.5,lwd = 3,col = "#35618A")\npoints(diferencia,.5,pch = 19); abline(v = 0,lty = 2)','Redacta según la salida efectiva: el IC incluye o excluye cero. El resultado compara medias de las poblaciones didácticas bajo muestreo independiente; no estima el efecto causal de educarse ni una brecha actual chilena.','Copiar la conclusión sin mirar los límites obtenidos.','¿Controlamos habilidad y contexto familiar? No.','Presencial')
titulos_editoriales = {'NIV-01': 'Escribe tu nombre', 'NIV-02': 'Vectores: creación, selección y modificación', 'NIV-03': 'Condicionales: if, else y operadores lógicos', 'NIV-04': 'Ciclos for y llenado de vectores', 'NIV-05': 'Sucesiones aritméticas, geométricas y recurrentes', 'NIV-06': 'Ciclos while y condiciones de término', 'NIV-07': 'Matrices y ciclos anidados', 'NIV-08': 'Actividad integradora: sucesiones y matrices', 'P1-01': 'Introducción a la econometría y a los datos', 'P1-02': 'Econometría moderna: describir, explicar y predecir', 'P1-03': 'Del modelo económico a las variables observadas', 'P1-04': 'Correlación, causalidad y factores no observados', 'P1-05': 'Educación y salarios: alcances de la comparación', 'P1-06': 'Econometría aplicada y diseño de estudios', 'P1-07': 'Tipos y estructura de los datos económicos', 'P1-08': 'Población, muestra y unidad de observación', 'P1-09': 'Razones para trabajar con muestras', 'P1-10': 'Variables, parámetros y estadísticos', 'P1-11': 'Métodos de muestreo probabilístico en R', 'P1-12': 'Muestreo estratificado y por conglomerados', 'P1-13': 'Muestreo no probabilístico y selección', 'P1-14': 'Estadística descriptiva e inferencial', 'P2-01': 'Ramas de la estadística', 'P2-02': 'Estadísticos como funciones de los datos', 'P2-03': 'Medidas de localización central: media y mediana', 'P2-04': 'Percentiles y cuartiles', 'P2-05': 'Medidas de dispersión: RIQ, varianza y desviación', 'P2-06': 'Histogramas y elección de intervalos', 'P2-07': 'Gráfico de caja, bigotes y valores atípicos', 'P3-01': 'Inferencia y población empírica de referencia', 'P3-02': 'Intervalos de confianza e incertidumbre', 'P3-03': 'Teorema central del límite: simulación en R', 'P3-04': 'Supuestos del teorema central del límite', 'P3-05': 'Intervalo para una media: ejemplo salarial', 'P3-06': 'Componentes del intervalo de confianza de 95%', 'P3-07': 'Intervalos con distintos niveles de confianza', 'P3-08': 'Comparación gráfica de intervalos de confianza', 'P3-09': 'Cobertura, confianza y precisión', 'P3-10': 'Tamaño muestral para estimar una media', 'P3-11': 'Intervalos de confianza para proporciones', 'P3-12': 'Proporciones: comparación con una referencia', 'P3-13': 'Tamaño muestral para estimar una proporción', 'P3-14': 'Aplicación: longitud y margen de error', 'P3-15': 'Comparación de medias entre dos poblaciones', 'P3-16': 'Diferencia de medias: parámetro e interpretación', 'P3-17': 'Diferencia de medias con varianzas conocidas', 'P3-18': 'Diferencia de medias: intervalo y conclusión'}
for actividad in activities:
 actividad["title"] = titulos_editoriales[actividad["id"]]


# La antigua NIV-04 se integra en NIV-02; NIV-03 queda inmediatamente después.
vector = next(a for a in activities if a['id'] == 'NIV-02')
loop = next(a for a in activities if a['id'] == 'NIV-04')
vector.update(
 title='Vectores: creación, selección, modificación y llenado con for',
 question='¿Cómo guardamos varios valores y los llenamos con un ciclo for?',
 predict=vector['predict'] + ' En el vector de dobles, ' + loop['predict'].lower(),
 task=vector['task'] + ' Después, ' + loop['task'].lower(),
 code='# 1. Crear, seleccionar y modificar\n' + vector['code'] + '\n\n# 2. Reservar y llenar con for\n' + loop['code'],
 answer=vector['answer'] + ' ' + loop['answer'],
 error=vector['error'] + ' ' + loop['error'],
 check=vector['check'] + ' ' + loop['check'])
activities = [a for a in activities if a['id'] != 'NIV-04']

# Inserta una introducción a la asignación antes de los vectores.
add('NIV-ASIG', 'Asignación de valores: nombres y flecha <-', 'Nivelación',
    '¿Cómo damos un nombre a un valor y lo usamos en un cálculo?',
    'Con x = 2 e y = 5, ¿cuánto valdrán z y w? ¿Qué mostrará cada print?',
    'Ejecuta las instrucciones una a una. Después consulta z y w con print(z) y print(w).',
    'x <- 2\ny <- 5\nz <- x - y\nw <- abs(x - y)\nprint(x)\nprint(y)',
    'La flecha <- asigna el resultado de la derecha al nombre de la izquierda. x recibe 2 e y recibe 5. z recibe x - y = -3. abs() calcula el valor absoluto: w recibe 3. print(x) muestra 2 y print(y) muestra 5; z y w quedan guardados, pero esas dos instrucciones no los imprimen. Los nombres permiten recuperar los valores asociados. La flecha se lee como asignación, no como un puntero de memoria: no se guardan direcciones ni una fórmula que se actualice sola. Si luego cambias x, debes ejecutar de nuevo las asignaciones de z y w para recalcularlos.',
    'Invertir la flecha o creer que z se recalcula automáticamente al cambiar x. En la expresión de la derecha, x e y deben estar definidos previamente.',
    '¿Cuánto valen z y w? -3 y 3. Si ejecutas solo x <- 10, ¿cambia z? No; debes volver a ejecutar z <- x - y.',
    'Presencial')
activities.insert(1, activities.pop())

# Orden solicitado, referido a la numeración anterior: 1, 2, 4, 6, 5, 3, 7, 8.
orden_nivelacion = ['NIV-01', 'NIV-ASIG', 'NIV-03', 'NIV-06', 'NIV-05', 'NIV-02', 'NIV-07', 'NIV-08']
por_id = {a['id']: a for a in activities}
activities = [por_id[id] for id in orden_nivelacion] + [a for a in activities if not a['id'].startswith('NIV-')]
# Condicionales ahora precede a vectores: su ejemplo debe ser autónomo.
por_id['NIV-03']['code'] = 'v <- c(2, 7, 9)  # Valores del ejemplo, definidos antes de usarlos.\n' + por_id['NIV-03']['code']
por_id['NIV-03']['task'] = 'Prueba con 3 y con 8; selecciona además todos los valores mayores que 4 del vector de ejemplo.'

# Dos láminas consecutivas para comparar las condiciones de término.
while_activity = por_id['NIV-06']
while_activity['title'] = 'Ciclos while/for y condiciones de término'
while_activity['question'] = 'Primera parte: while. ¿Cuántas duplicaciones hacen falta para llegar a 100?'
while_activity['answer'] = 'while evalúa su condición antes de cada repetición: seguimos si valor < 100 y paso < max_pasos. El cuerpo actualiza valor y paso. Se llega a 128 en siete duplicaciones y la condición valor < 100 deja de cumplirse. El límite adicional de 20 pasos protege ante una condición mal planteada; si la condición inicial fuese falsa, el cuerpo no se ejecutaría.'
add('NIV-FOR', 'Ciclos while/for y condiciones de término · for', 'Nivelación',
    'Segunda parte: for. ¿Cómo repetimos el cálculo con un límite de pasos?',
    '¿Cuándo terminará: al agotar los 20 pasos o al alcanzar 100?',
    'Ejecuta la versión con for. Compara su trayectoria con la del while y prueba max_pasos <- 3.',
    'valor <- 1\nmax_pasos <- 20L\ntrayectoria <- numeric(max_pasos + 1L)\ntrayectoria[1] <- valor\nfor (paso in seq_len(max_pasos)) {\n  valor <- 2 * valor\n  trayectoria[paso + 1L] <- valor\n  if (valor >= 100) {\n    break\n  }\n}\nprint(trayectoria[seq_len(paso + 1L)])\nprint(c(pasos = paso, valor = valor))',
    'for recorre los pasos de seq_len(max_pasos). Termina al agotar esa secuencia o antes si ejecuta break. Aquí el if detecta valor >= 100 y break sale del ciclo en el paso 7, con valor 128; la trayectoria coincide con la del while. Si max_pasos es 3, se agota la secuencia con valor 8. En este ejemplo max_pasos debe ser un entero positivo; paso recibe automáticamente cada índice, sin escribir paso <- paso + 1.',
    'Confundir el recorrido de for con una prueba automática de valor < 100: esa condición de salida anticipada se expresa con if y break. No usar paso después de un ciclo vacío sin inicializarlo.',
    '¿Qué ocurre si eliminas if y break? Se ejecutan los 20 pasos. ¿Qué ocurre con max_pasos <- 3? Termina por agotar los pasos, sin alcanzar 100.',
    'Presencial')
activities.insert(activities.index(while_activity) + 1, activities.pop())




header='''# Taller 1 · Del código a los datos

**Iván · Taller presencial · Econometría ICS-294 · 8 a 10 estudiantes**

¿Podemos describir salarios sin confundir una asociación con una causa? Primero aprenderemos a dar instrucciones a R; después recorreremos los contenidos de Sebastián, en su mismo orden.

[Instrucciones](instruccion-clase-taller-1.md) · [Notebook de R](clase-taller-1.ipynb) · [Guía docente](guia-docente-taller-1.md) · [Lectura comparativa](Lectura%20clase%201%20-%20material%20existente.md) · [Clase de Sebastián](https://hizocar.github.io/econometria-usm/clases/clase1/)

## Objetivos

Al terminar la ruta presencial podrás llenar vectores y matrices con ciclos y condiciones, reconocer una base transversal, resumir salarios con gráficos y estadísticos y explicar la interpretación de un intervalo de confianza. Las ampliaciones permiten completar la práctica de todos los apartados.

## Agenda presencial · 140 minutos efectivos

| Hora | Minutos | Trabajo |
|---|---:|---|
| 18:50–18:55 | 5 | Diagnóstico y apertura del notebook |
| 18:55–19:35 | 40 | NIV-01 a NIV-08: demostraciones breves y actividad integradora |
| 19:35–20:00 | 25 | Parte 1: recorrido en orden; practicar selección simple y estratificada |
| 20:00–20:15 | 15 | Pausa |
| 20:15–20:40 | 25 | Parte 2: centro, posición, dispersión y gráficos |
| 20:40–21:15 | 35 | Parte 3: recorrido en orden; ejecutar TCL, IC de media, proporción y diferencia |
| 21:15–21:25 | 10 | Autoevaluación y cierre |

La sesión dura 155 minutos incluyendo la pausa. Las actividades marcadas «Ampliación autónoma» se presentan brevemente en su lugar, pero su ejecución detallada se reserva para después. La secuencia completa permanece en el notebook; no se promete resolver todo con igual profundidad en una sesión.

## Antes de comenzar

Trabaja en 4 a 5 parejas: una persona conduce el teclado y otra anticipa e interpreta; alternen después de cada bloque. Guarda el notebook en la raíz de esta carpeta, junto a `datos/`. Ejecuta de arriba abajo. En RStudio puedes usar el script equivalente `clase-taller-1.R`; para el notebook usa Jupyter con kernel R.

Preparación, una sola vez, desde R con acceso a internet:

```r
install.packages(c("wooldridge", "IRkernel"), repos = "https://cloud.r-project.org")
# Jupyter debe estar instalado y disponible antes de registrar el kernel.
IRkernel::installspec(user = TRUE)
```

Abrir Jupyter y elegir el kernel **R**. No se necesita Python para resolver los ejercicios. RStudio es la alternativa para ejecutar el script si no se dispone de Jupyter. La instalación de Jupyter depende del equipo y debe quedar resuelta antes de la clase.

La copia `datos/wage1.csv` evita depender de internet y del paquete durante la sesión. El código prefiere esa copia y usa el paquete solo como alternativa. No ejecutar instalaciones durante la clase si ya se preparó el entorno.

## Datos, unidades y procedencia

Las aplicaciones son actividades propias elaboradas con datos asociados al libro de Jeffrey M. Wooldridge; no se presentan como ejercicios textuales ni se les asignan páginas del libro. `wage1` contiene 526 observaciones y 24 variables de la CPS de 1976 de Estados Unidos. Para esta guía se usan:

| Variable | Significado | Unidad o codificación |
|---|---|---|
| wage | Remuneración media por hora | USD nominales de 1976 por hora |
| educ | Educación | Años |
| exper | Experiencia potencial | Años; no experiencia efectiva necesariamente |
| tenure | Antigüedad con empleador actual | Años |
| female | Indicador tal como aparece documentado en la base histórica | 1 si mujer, 0 en otro caso según esa codificación |
| married | Estado civil registrado | 1 si casado/a, 0 en otro caso |

La documentación advierte inconsistencias entre experiencia potencial y antigüedad en algunos registros. No las corregimos arbitrariamente ni usamos esas columnas para inferir trayectoria laboral. Se informan faltantes en las seis variables y se trabaja con casos completos; esto define el conjunto de análisis y no garantiza representatividad. `educ16` se deriva de educ >= 16, sin afirmar titulación.

## Diagnóstico · antes de ejecutar

1. ¿Qué hace `x <- 3`? Asigna 3 a x.
2. ¿Cuál es el primer índice de un vector en R? 1.
3. ¿Qué debe cambiar dentro de un `while`? Algún estado que permita que su condición termine, con límite de seguridad.

Si dos respuestas no están claras, ejecutar todos los ejemplos de nivelación sin omitirlos. Son objetos artificiales para aprender programación, separados de la evidencia económica.
'''
closing='''## CIERRE · Autoevaluación

Responde antes de leer las soluciones:

1. ¿Qué evita un `while` infinito?
2. Si una muestra selecciona solo educ >= 16, ¿describe automáticamente a toda la población?
3. ¿Qué cambia más al añadir un salario extremo: media o mediana?
4. ¿Un IC de 95% contiene el 95% de los salarios individuales?
5. ¿Qué pasa con el margen al cuadruplicar n, con sigma y confianza constantes?
6. ¿Una diferencia de salarios entre grupos educativos prueba el efecto causal de la educación?

### Soluciones del cierre

1. Actualizar el estado y fijar un máximo de iteraciones.
2. No. Tiene un criterio de exclusión y carece de selección probabilística del conjunto.
3. En general la media es más sensible; comprobar en la copia de la actividad.
4. No. El 95% se refiere a la cobertura del procedimiento para el parámetro.
5. Se reduce a la mitad porque depende de 1/sqrt(n).
6. No. No se han aislado diferencias en habilidad, familia y otros factores.

### Para continuar

Revisar las ampliaciones en orden y volver al capítulo 1 y apéndice C de Wooldridge indicados por Sebastián. No se requieren regresiones para completar este taller.

## Referencias y alcance

- [Clase 1 de Sebastián](https://hizocar.github.io/econometria-usm/clases/clase1/): secuencia de 20, 10 y 34 láminas, sin portadas. Revisada en esta conversación el 17 de octubre de 2026; la consulta web automática posterior falló, por lo que se usó también la lectura comparativa local ya verificada.
- [Portada del curso](https://hizocar.github.io/econometria-usm/): roles y organización.
- [Documentación oficial de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html): variables, procedencia y notas.
- [Paquete wooldridge](https://justinmshea.github.io/wooldridge/): datos asociados al libro.
- [Copia pública CSV utilizada](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/wooldridge/wage1.csv): distribución Rdatasets del conjunto; se elimina solo la columna de índice `rownames` al cargar.

No se ha estimado ninguna regresión. Los experimentos mencionados en cátedra se discuten conceptualmente; no se inventan sus bases. Los grupos artificiales se identifican como tales. La inferencia computacional utiliza muestreo independiente con reemplazo de distribuciones empíricas conocidas, no un análisis representativo de la encuesta nacional ni una estimación bootstrap.

## Estado de validación

Se verificaron la estructura JSON del notebook, IDs y orden de actividades, correspondencia literal con la guía, cobertura de las láminas, enlaces locales, filas y columnas del CSV y hash del archivo de datos. **No se ejecutó R ni el kernel del notebook:** no se encontró una instalación disponible en este entorno. Las celdas no contienen resultados inventados. Antes de usarlo en clase, ejecutar el script desde una sesión limpia o ejecutar todo el notebook con kernel R y revisar salidas y gráficos. La cobertura de contenido es completa; la validación de ejecución queda pendiente.
'''
cells=[]
def md(text,id):
 cells.append(dict(cell_type='markdown',id=id,metadata={},source=text.splitlines(True)))
def rc(code,id,tags=None):
 cells.append(dict(cell_type='code',id=id,metadata={'tags':tags or []},source=(code+'\n').splitlines(True),outputs=[],execution_count=None))
md(header,'inicio')
# Installation is documentation, not an executable runtime cell.
sections=[header]
numeros_por_bloque = {}
for a in activities:
 id=a['id']
 bloque=id.split('-')[0]
 numeros_por_bloque[bloque] = numeros_por_bloque.get(bloque, 0) + 1
 numero = numeros_por_bloque[bloque]
 intro=f'''<a id="{id}"></a>
## Lámina {numero:02d} · {a['title']}

**Identificador de enlace:** `{id}`. La numeración se reinicia por bloque, como en la web.

**Referencia:** {a['slides']} · **Modalidad:** {a['mode']}.

**Pregunta:** {a['question']}

**Antes de ejecutar:** {a['predict']}

**Consigna:** {a['task']}

**Datos:** {'Objetos artificiales de programación.' if id.startswith('NIV') else 'wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.'}
'''
 md(intro,id.lower()+'-consigna')
 solution=f"### Solución · {id}\n\nEjecutar después de intentar la consigna.\n"
 md(solution,id.lower()+'-solucion')
 rc(a['code'],id.lower()+'-r',['solucion'])
 discussion=f"**Lectura del resultado:** {a['answer']}\n\n**Error frecuente:** {a['error']}\n\n**Comprueba:** {a['check']}\n"
 md(discussion,id.lower()+'-lectura')
 sections.extend([intro,solution,'```r\n'+a['code']+'\n```\n',discussion])
md(closing,'cierre'); sections.append(closing)
rows=['| Actividad | Referencia web | Sección y celda de código del notebook | Modalidad |','|---|---|---|---|']
for a in activities: rows.append(f"| {a['id']} | {a['slides']} | `{a['id'].lower()}-consigna` / `{a['id'].lower()}-r` | {a['mode']} |")
trace='''## Matriz de correspondencia

La guía y el notebook se generan desde el mismo contenido: todas las consignas, soluciones y celdas R de actividades coinciden. Los IDs son estables. Los enunciados son el código inicial de trabajo: cada pareja escribe su intento en una celda R nueva antes de consultar la celda de solución; no hay ejercicios deliberadamente rotos que impidan ejecutar el notebook completo.

'''+ '\n'.join(rows)+'''

| Requisito de las instrucciones | Ubicación en el notebook |
|---|---|
| Contexto, audiencia y rol docente | inicio |
| Fuentes y enlaces bidireccionales | inicio, cierre |
| R exclusivamente y alcance de clase 1 | Metadatos kernelspec, todas las celdas R, cierre |
| Nivelación completa y anterior al curso | NIV-01 a NIV-08 |
| Datos transversales, unidades, faltantes y copia local | inicio, P1-01 |
| Parte 1: 20 láminas en orden | P1-01 a P1-14 |
| Parte 2: 10 láminas en orden | P2-01 a P2-07 |
| Parte 3: 34 láminas en orden | P3-01 a P3-18 |
| Intuición, predicción, consigna, solución, interpretación y comprobación | Todas las actividades |
| Dinámica presencial y tiempos | inicio; guía docente enlazada |
| Muestras didácticas, sigma conocida y límites de inferencia | P1-08, P1-11, P3-01 a P3-18 |
| Semillas, reproducción y verificación | Celdas de selección/simulación, cierre |
| Autoevaluación y soluciones | cierre |
| Preparación y alternativa sin conexión | inicio, P1-01 |
| Trazabilidad y cobertura | matriz-correspondencia |

**Cobertura documental:** 48/48 actividades (9 de nivelación, 14 introductorias, 7 descriptivas y 18 inferenciales); 64/64 láminas de contenido del curso; 15/15 categorías de requisitos anteriores. Esto no equivale a una certificación de ejecución ni a 48 actividades resueltas en clase.
'''
md(trace,'matriz-correspondencia'); sections.append(trace)
notebook=dict(nbformat=4,nbformat_minor=5,metadata=dict(kernelspec=dict(display_name='R',language='R',name='ir'),language_info=dict(name='R',file_extension='.r',mimetype='text/x-r-source'),taller=dict(docente='Iván',audiencia='8–10',inicio='18:50',fin='21:25',pausa_min=15,trabajo_min=140)),cells=cells)
(root/'clase-taller-1.ipynb').write_text(json.dumps(notebook,ensure_ascii=False,indent=1)+'\n')
(root/'guia-actividades-taller-1.md').write_text('\n\n'.join(sections))
script=['# Taller 1: ejecutar desde la raíz del proyecto en una sesión limpia.\n# Equivalente a todas las celdas R del notebook; no instala paquetes.\n']
for a in activities: script.extend(['\n# '+a['id']+' · '+a['title']+'\n',a['code']+'\n'])
script.append('\ncat("Todas las actividades finalizaron. Revise también gráficos e interpretaciones.\\n")\nsessionInfo()\n')
(root/'clase-taller-1.R').write_text(''.join(script))
(root/'guia-docente-taller-1.md').write_text('''# Guía docente · Taller 1

Iván dirige el taller computacional de la materia de Sebastián para 8 a 10 alumnos, en 4 a 5 parejas. Se asume experiencia inicial heterogénea; no se exige programación previa. La sesión está diseñada para 18:50–21:25 con pausa 20:00–20:15: 140 minutos efectivos.

[Guía de actividades](guia-actividades-taller-1.md) · [Notebook R](clase-taller-1.ipynb) · [Script equivalente](clase-taller-1.R) · [Instrucciones](instruccion-clase-taller-1.md)

## Preparación antes de la clase

- Comprobar R y RStudio en los equipos. Para notebook, instalar Jupyter e IRkernel y seleccionar kernel R según el inicio de la guía.
- Entregar la carpeta con el notebook, script y `datos/wage1.csv`. Mantener rutas relativas.
- Ejecutar todo previamente: en una terminal con R disponible, `Rscript --vanilla clase-taller-1.R`; desde RStudio abrir la carpeta del proyecto, reiniciar R y ejecutar el script. El notebook debe ejecutarse desde su primera celda con kernel limpio.
- No hay ejecución R verificada en el entorno de elaboración; no usar este material en clase sin esa comprobación. Si una celda falla, conservar el mensaje y corregir antes de continuar.
- Los ejercicios son propios con datos de Wooldridge. La documentación de wage1 identifica sus variables; no adjudicar a Sebastián ni al libro los enunciados creados aquí.

## Conducción minuto a minuto

| Hora | Ruta y conducción |
|---|---|
| 18:50–18:55 | Diagnóstico del inicio. Pedir respuestas a tres estudiantes distintos. Abrir notebook y confirmar kernel. |
| 18:55–18:57 | NIV-01 (lámina 01). Escribe tu nombre y observa la consola. |
| 18:57–19:00 | NIV-ASIG (lámina 02). Asigna x e y, anticipa z y w y distingue guardar de imprimir. |
| 19:00–19:04 | NIV-03 (lámina 03). Anticipar el mensaje con valores 3 y 8; el ejemplo define sus propios valores. |
| 19:04–19:07 | NIV-06 (lámina 04). while: condición previa, actualización y límite de seguridad. |
| 19:07–19:09 | NIV-FOR (lámina 05). for: recorrido de pasos y salida anticipada con break. |
| 19:09–19:14 | NIV-05 (lámina 06). Parejas completan una sucesión y revisan las otras. |
| 19:14–19:20 | NIV-02 (lámina 07). Crear, seleccionar, modificar y llenar un vector con for. |
| 19:20–19:27 | NIV-07. Llenar matriz por filas/columnas con ciclos anidados. |
| 19:27–19:35 | NIV-08. Integración en parejas; intercambiar teclado y verificar cuarto término. |
| 19:35–19:42 | P1-01 a P1-05 en orden. Cargar datos; ubicar país/año; discutir asociación sin calcular aún medias. |
| 19:42–19:47 | P1-06 a P1-10 en orden. Recorrido conceptual breve y selección de 12 filas. |
| 19:47–20:00 | P1-11 a P1-14. Ejecutar selección simple y estratificada, mostrar los otros algoritmos y límites. No comparar eficiencia de grupos artificiales. |
| 20:00–20:15 | Pausa de 15 minutos. |
| 20:15–20:18 | P2-01 y P2-02. Qué entra y sale de una función. |
| 20:18–20:27 | P2-03 a P2-05. Cada pareja anticipa qué hace un extremo y calcula medidas de centro y dispersión. |
| 20:27–20:40 | P2-06 y P2-07. Mostrar histograma y boxplot, comparar intervalos y explicar atípicos sin borrarlos. |
| 20:40–20:48 | P3-01 a P3-04. Definir población didáctica y ejecutar demostración TCL. Distinguir sd de salarios y de medias. |
| 20:48–20:58 | P3-05 a P3-10 en orden. IC de media; cambiar confianza; mostrar cobertura y fórmula de tamaño. Ampliar ejercicios de planificación después. |
| 20:58–21:06 | P3-11 a P3-14. Proporción educativa y referencia. Presentar longitud vs margen, dejar cálculos detallados de planificación como ampliación. |
| 21:06–21:15 | P3-15 a P3-18. Dos grupos, independencia, diferencia e interpretación. El profesor ejecuta y una pareja redacta la conclusión mirando la salida. |
| 21:15–21:25 | Autoevaluación individual, discusión en pareja y respuesta colectiva. Registrar dudas para apoyo posterior. |

El tiempo para todas las láminas es una revisión computacional selectiva, no una clase exhaustiva de inferencia. Las ampliaciones se conservan en orden y no se eliminan del notebook. Si el diagnóstico muestra dificultades, reducir modificaciones autónomas durante la sesión y usar las demostraciones ya preparadas; conservar el horario y asignar la práctica restante para después.

## Preguntas que vale la pena detenerse a escuchar

- NIV-03: ¿por qué no usar if con todo el vector? Esperar que distingan una decisión de una selección por elemento.
- P1-04: ¿qué no mantiene constante este gráfico? Esperar habilidad, experiencia o contexto familiar.
- P1-11: ¿qué representa cada selección? Aclarar inicio aleatorio del sistemático, pesos por estrato y grupos artificiales.
- P2-03: ¿el dato extremo es real? No: es una copia alterada con propósito explícito.
- P3-01: ¿de qué población conocemos sigma? Solo de nuestra distribución empírica didáctica.
- P3-09: ¿el 95% tiene que cumplirse exactamente en 100 repeticiones? No; fluctúa y depende de aproximación.
- P3-18: ¿puede decirse que estudiar causó la diferencia? No.

## Revisión y decisiones

La matriz completa de cobertura y los IDs están al final de la guía y notebook. Las guías y el notebook comparten consignas, soluciones y código generados desde `herramientas/generar_taller.py`. No editar solo una copia: regenerar las salidas tras modificar ese origen. El script `.R` facilita una alternativa en RStudio.

No se publicó ni modificó ningún sitio. No se requirió GitHub para crear el material. La experiencia previa e instalaciones de los alumnos siguen sin confirmarse; comprobarlas antes del taller. El material contiene soluciones abiertas en celdas separadas: durante la actividad detenerse antes de la solución y pedir al estudiante que escriba su intento en una celda nueva.
''')
# Checks on data, notebook IDs and complete mapping; no claim of R execution.
ids=[c['id'] for c in cells]
assert len(ids)==len(set(ids))
assert len(activities)==48
assert sum(c['cell_type']=='code' for c in cells)==48
assert all(c.get('execution_count') is None for c in cells if c['cell_type']=='code')
with (root/'datos/wage1.csv').open() as f:
 rows=list(csv.DictReader(f))
assert len(rows)==526 and len(rows[0])==25
sha=hashlib.sha256((root/'datos/wage1.csv').read_bytes()).hexdigest()
(root/'datos/LEEME.md').write_text(f'''# Datos del taller

`wage1.csv`: copia obtenida el 17 de octubre de 2026 de [Rdatasets](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/wooldridge/wage1.csv), distribución de la base del paquete wooldridge. [Documentación original](https://justinmshea.github.io/wooldridge/reference/wage1.html).

526 filas; 24 variables más el índice de distribución `rownames`, eliminado al cargar. No se modificaron valores. País y año: Estados Unidos, 1976; fuente CPS. Salarios en USD nominales por hora. No se afirma representatividad bajo los submuestreos docentes.

SHA-256: `{sha}`.
''')
print(f'Generadas {len(activities)} actividades y {len(cells)} celdas. CSV: 526 filas. Kernel R. Sin ejecución R.')
