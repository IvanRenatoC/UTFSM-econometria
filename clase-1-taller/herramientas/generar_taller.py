from pathlib import Path
import json, csv, hashlib, re
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
load='''# Usa la copia local; si no está, carga la base del paquete.
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
'''

add('P1-01','¿Qué podemos preguntar a los datos?','Parte 1 · lámina 1','¿Qué sabemos de educación y salario de cada persona?','¿Cada fila representa una persona o un mes?','Carga la base e identifica wage y educ en seis filas.',load,'wage1 es un corte transversal observacional de Estados Unidos en 1976. wage es remuneración por hora en dólares nominales de ese período; educ son años de educación. No son pesos chilenos actuales. La inspección no prueba efectos.','Confundir índice de fila con tiempo o borrar faltantes sin informar cuántos.','¿526 filas equivalen a 526 períodos? No.','Presencial')
activities[-1].update(
 question='', predict='', error='',
 check='¿Cuántas filas tiene el dataset? Tiene 526 filas: son observaciones de personas, no períodos de tiempo.',
 description='datos/wage1.csv es una copia local de wage1, una base del paquete de R wooldridge, asociado al libro de Jeffrey M. Wooldridge. Contiene 526 observaciones de personas y 24 variables de la Current Population Survey (CPS) de Estados Unidos de 1976. Es una base de corte transversal: cada fila corresponde a una persona. En este taller utilizaremos seis variables.',
 variable_definitions=[
  ('wage', 'Salario promedio por hora, en dólares estadounidenses de 1976.'),
  ('educ', 'Años de educación.'),
  ('exper', 'Años de experiencia laboral potencial.'),
  ('tenure', 'Años de antigüedad con el empleador actual.'),
  ('female', 'Indicador: 1 si la persona está registrada como mujer; 0 en caso contrario.'),
  ('married', 'Indicador: 1 si la persona está registrada como casada; 0 en caso contrario.')])
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
while_activity['title'] = 'Ciclos while y condiciones de término'
while_activity['question'] = 'Primera parte: while. ¿Cuántas duplicaciones hacen falta para llegar a 100?'
while_activity['answer'] = 'while evalúa su condición antes de cada repetición: seguimos si valor < 100 y paso < max_pasos. El cuerpo actualiza valor y paso. Se llega a 128 en siete duplicaciones y la condición valor < 100 deja de cumplirse. El límite adicional de 20 pasos protege ante una condición mal planteada; si la condición inicial fuese falsa, el cuerpo no se ejecutaría.'
add('NIV-FOR', 'Ciclos for y condiciones de término', 'Nivelación',
    'Segunda parte: for. ¿Cómo repetimos el cálculo con un límite de pasos?',
    '¿Cuándo terminará: al agotar los 20 pasos o al alcanzar 100?',
    'Ejecuta la versión con for. Compara su trayectoria con la del while y prueba max_pasos <- 3.',
    'valor <- 1\nmax_pasos <- 20L\ntrayectoria <- numeric(max_pasos + 1L)\ntrayectoria[1] <- valor\nfor (paso in seq_len(max_pasos)) {\n  valor <- 2 * valor\n  trayectoria[paso + 1L] <- valor\n  if (valor >= 100) {\n    break\n  }\n}\nprint(trayectoria[seq_len(paso + 1L)])\nprint(c(pasos = paso, valor = valor))',
    'for recorre los pasos de seq_len(max_pasos). Termina al agotar esa secuencia o antes si ejecuta break. Aquí el if detecta valor >= 100 y break sale del ciclo en el paso 7, con valor 128; la trayectoria coincide con la del while. Si max_pasos es 3, se agota la secuencia con valor 8. En este ejemplo max_pasos debe ser un entero positivo; paso recibe automáticamente cada índice, sin escribir paso <- paso + 1.',
    'Confundir el recorrido de for con una prueba automática de valor < 100: esa condición de salida anticipada se expresa con if y break. No usar paso después de un ciclo vacío sin inicializarlo.',
    '¿Qué ocurre si eliminas if y break? Se ejecutan los 20 pasos. ¿Qué ocurre con max_pasos <- 3? Termina por agotar los pasos, sin alcanzar 100.',
    'Presencial')
activities.insert(activities.index(while_activity) + 1, activities.pop())





# Contenido definitivo de la revisión docente, compartido por todos los formatos.
por_id['NIV-ASIG'].update(
 title='Asignación de valores',
 task='Ejecuta las instrucciones una a una. Después consulta z con print(z).',
 code='x <- 2\ny <- 5\nz <- x - y\nw <- abs(x - y)\nprint(x)\nprint(w)',
 answer='La flecha <- asigna el resultado de la derecha al nombre de la izquierda. x recibe 2 e y recibe 5. z recibe x - y = -3. abs() calcula el valor absoluto: w recibe 3. print(x) muestra 2 y print(w) muestra 3. z queda guardado, aunque no se imprime en estas instrucciones. Si cambias x o y, debes ejecutar de nuevo las asignaciones de z y w para recalcularlos.',
 note='Los valores quedan asignados mientras la sesión siga activa. En R de escritorio se conservan hasta que los reasignes, los elimines o cierres o reinicies la sesión. En Google Colab ocurre lo mismo mientras el entorno de ejecución permanezca activo: se pierden al reiniciarlo o eliminarlo, no necesariamente por una desconexión temporal.')
while_activity.update(
 question='Primera parte: while. Iteraciones y loops',
 task='Parte en 1 y multiplica el valor por 2 en cada iteración, hasta alcanzar 100. Conserva los valores de cada paso.',
 answer='while evalúa su condición antes de cada repetición: seguimos si valor < 100 y paso < max_pasos. En cada iteración se multiplica el valor por 2 y se actualiza el contador paso. Se llega a 128 después de siete iteraciones y la condición valor < 100 deja de cumplirse. El límite de 20 pasos evita que el ciclo continúe indefinidamente si la condición se plantea mal. Si la condición inicial es falsa, el cuerpo no se ejecuta.')
while_activity['code'] = re.sub(r'(\d+)L\b', r'\1', while_activity['code'])
for_activity = next(a for a in activities if a['id'] == 'NIV-FOR')
for_activity['code'] = re.sub(r'(\d+)L\b', r'\1', for_activity['code'])
for_activity['comparison'] = 'while repite instrucciones mientras una condición sea verdadera; el número de repeticiones depende de cuándo deje de cumplirse. for recorre una secuencia de valores, uno por iteración. En este ejemplo, for puede terminar antes de agotar la secuencia porque if detecta que se alcanzó 100 y break sale del ciclo. Ambos producen la misma trayectoria, pero expresan el control de la repetición de distinta forma.'
por_id['NIV-05'].update(
 title='Sucesión geométrica: 1, 2, 4, 8, 16…',
 question='¿Cómo construimos la sucesión 1, 2, 4, 8, 16…?',
 predict='Observa la sucesión 1, 2, 4, 8, 16… ¿Cuál es el siguiente número?',
 task='Genera los seis primeros términos de la sucesión 1, 2, 4, 8, 16… Multiplica cada término por 2 para obtener el siguiente.',
 code='sucesion <- numeric(6)\nsucesion[1] <- 1\nfor (i in 2:6) {\n  sucesion[i] <- 2 * sucesion[i - 1]\n}\nprint(sucesion)',
 answer='El resultado es 1, 2, 4, 8, 16, 32. Cada término es el anterior multiplicado por 2: por eso es una sucesión geométrica de razón 2. Primero asignamos el valor 1 a la primera posición; el ciclo calcula las cinco posiciones restantes.',
 error='Empezar el ciclo en la posición 1 y tratar de leer la posición 0. En R los índices comienzan en 1.',
 check='¿Qué número sigue después de 32? 64, porque 32 × 2 = 64.')
vector.update(
 question='¿Cómo reservamos un vector y modificamos solo algunas posiciones?',
 predict='',
 task='Crea un vector de largo 20, solo con valores 0, pero con un −1 en las posiciones impares.',
 code='v <- numeric(20)\nfor (i in 1:20) {\n  if (i %% 2 != 0) {\n    v[i] <- -1\n  }\n}\nprint(v)',
 answer='El vector alterna −1, 0, −1, 0 hasta completar 20 posiciones. numeric(20) reserva un vector de veinte ceros. El ciclo recorre sus posiciones y la condición i %% 2 != 0 identifica los índices impares. Solo esas posiciones cambian a −1: quedan diez valores −1 y diez ceros.',
 error='Confundir el valor guardado con su posición. La condición se aplica al índice i, no al contenido v[i].',
 check='')
vector['practice'] = dict(
 hide_heading=True,
 task='Trabaja sobre el vector anterior: reemplaza cada 0 por el número de su posición y conserva los valores −1.',
 code='for (i in seq_along(v)) {\n  if (v[i] == 0) {\n    v[i] <- i\n  }\n}\nprint(v)',
 answer='El resultado alterna −1, 2, −1, 4, −1, 6 y continúa hasta −1, 20. Las posiciones impares conservan −1; cada posición par contiene su propio índice.')
por_id['NIV-07'].update(
 predict='Indica cuáles son las posiciones (2, 3) y (3, 2).',
 task='Llena una matriz de 3 × 3 solo con valores 0; luego haz que su diagonal principal contenga únicamente valores 1.',
 code='A <- matrix(0, nrow = 3, ncol = 3)\nfor (i in 1:3) {\n  A[i, i] <- 1\n}\nprint(A)',
 answer='Esta es la matriz identidad: cumple en la multiplicación de matrices un papel similar al 1 en los escalares. Tiene unos en la diagonal principal y ceros en las otras posiciones.',
 error='Confundir la diagonal principal con una fila completa. En la diagonal principal coinciden el índice de fila y el de columna.',
 check='Si A es una matriz de 2 × 4, ¿se cumple A(2,3) = Aᵀ(3,2)? Aᵀ es la transpuesta de A.',
 check_markdown='Si $A$ es una matriz de $2 \\times 4$, ¿se cumple $A(2,3) = A^{\\mathsf{T}}(3,2)$? $A^{\\mathsf{T}}$ es la transpuesta de $A$ y en R se obtiene con `t(A)`.',
 check_html='<p>Si <var>A</var> es una matriz de 2 × 4, ¿se cumple <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>=</mo><msup><mi>A</mi><mi>T</mi></msup><mo>(</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>? <var>A</var><sup>T</sup> es la transpuesta de <var>A</var> y en R se obtiene con <code>t(A)</code>.</p>')
por_id['NIV-07']['practice'] = dict(
 hide_heading=True,
 task='',
 code='A <- matrix(1:8, nrow = 2, ncol = 4)\nprint(A[2, 3])\nprint(t(A)[3, 2])\nprint(A[2, 3] == t(A)[3, 2])',
 answer='Sí. La transposición intercambia filas y columnas: A[2,3] y t(A)[3,2] contienen el mismo elemento. En este ejemplo ambos valen 6 y la comparación devuelve TRUE.')
por_id['NIV-08'].update(
 question='¿Cómo organizamos una sucesión de números en una matriz?',
 predict='',
 task='Genera la sucesión 3, 9, 27, 81, 243 y 729, es decir, 3 elevado a 1, 2, 3, 4, 5 y 6. Con esos números crea una matriz de 3 × 2.',
 code='sucesion <- 3^(1:6)\nA <- matrix(sucesion, nrow = 3, ncol = 2)\nprint(sucesion)\nprint(A)',
 answer='La sucesión contiene las seis primeras potencias de 3. matrix() distribuye estos valores por columnas: la primera contiene 3, 9 y 27; la segunda, 81, 243 y 729. Una matriz puede entenderse como varios vectores columna organizados juntos. En estadística siempre vemos matrices.',
 error='Leer los valores por filas cuando matrix() los ha organizado por columnas de forma predeterminada.',
 check='¿Cuáles son los valores de la segunda columna? 81, 243 y 729.')


# Lámina conceptual de cierre de la nivelación; sin celda de ejecución.
add('NIV-NOTEBOOK', 'Vista general de un notebook', 'Nivelación',
    'Librerías → adecuación de datos → EDA → modelamiento → resultados',
    '', 'EDA significa análisis exploratorio de datos.',
    '# Librerías -> adecuación de datos -> EDA -> modelamiento -> resultados',
    '', '', '', 'Presencial')
activities[-1]['overview'] = True
activities.insert(next(i for i, a in enumerate(activities) if not a['id'].startswith('NIV-')), activities.pop())

# La exploración gráfica sustituye el contenido de la segunda lámina de econometría.
exploracion = next(a for a in activities if a['id'] == 'P1-02')
exploracion.update(
 title='Exploración gráfica de los datos', data_explorer=True,
 question='Selecciona una variable para explorar su distribución.', predict='',
 task='En la web, pulsa wage, educ, exper, tenure, female o married. En R, cambia el nombre de variable y ejecuta la celda para reproducir el gráfico.',
 code='''# Elige: "wage", "educ", "exper", "tenure", "female" o "married".
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
}''',
 answer='Cada gráfico resume las mismas 526 personas. El histograma agrupa salarios en intervalos de 2 USD; las barras cuentan personas para cada cantidad de años; los gráficos circulares muestran proporciones de las categorías 0 y 1.',
 error='', check='')

# Se conserva el título exterior de P1-04 y se reemplaza su contenido.
relacion = next(a for a in activities if a['id'] == 'P1-04')
relacion.update(
 scatter=True, question='Relación lineal de dos variables', predict='',
 task='Observa el gráfico: cada punto representa a una persona. El eje horizontal muestra sus años de educación y el vertical, su salario por hora. El azul identifica a los hombres y el amarillo a las mujeres.',
 code='''colores <- c("#0160A080", "#F8C75180")  # Azul para hombres (0), amarillo para mujeres (1)

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
       pch = 19)''',
 answer='La nube de puntos sugiere una asociación positiva: a más años de educación, los salarios tienden a ser mayores, aunque hay mucha dispersión. Las columnas de puntos aparecen porque varias personas tienen los mismos años de educación. A igual educación se observan salarios distintos y los colores permiten comparar ambos grupos. No se ha dibujado ni estimado una recta: el gráfico es una primera aproximación para estudiar una posible relación lineal. Esta asociación, por sí sola, no demuestra que estudiar cause un aumento salarial o que el género corresponda a una condición causal a las diferencias. Para llegar a esa conclusión se debe hacer un estudio más profundo.',
 error='', check='')

umbral = next(a for a in activities if a['id'] == 'P1-05')
umbral.update(
 explanation_title='¿Por qué educ ≥ 16 y no educ ≥ 18?',
 explanation='educ mide años de educación, no la edad. Usamos 16 como un umbral didáctico: la referencia habitual es 12 años escolares más unos 4 años de estudios universitarios en Estados Unidos. Esto no permite afirmar que cada persona tenga un título universitario. Exigir 18 años de educación seleccionaría una trayectoria educativa más larga y dejaría fuera a quienes registran 16 o 17 años. En esta base, educ ≥ 16 reúne 99 personas, mientras que educ ≥ 18 reúne solo 19. Para la comparación siguiente mantendremos dos grupos: menos de 16 años y 16 años o más. Es una decisión de agrupación para este ejercicio, no una frontera universal ni una prueba de causalidad.',
 explanation_source='https://nces.ed.gov/surveys/ctes/tables/glossary_college.asp')

comparacion = next(a for a in activities if a['id'] == 'P1-06')
comparacion.update(
 title='Comparar salarios con boxplots', boxplots=True,
 question='¿Cómo cambia la distribución salarial entre grupos?', predict='',
 task='Selecciona educ, female o married en la web. En R, cambia variable para comparar los salarios por educación (menos de 16 años y 16 años o más), sexo registrado o estado civil registrado.',
 code='''# Elige: "educ", "female" o "married".
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
        xlab = "Grupo", ylab = "Salario por hora (USD de 1976)")''',
 answer='La línea dentro de la caja es la mediana; la caja resume la mitad central de los salarios. Los bigotes llegan hasta los valores más extremos dentro de 1,5 veces el rango intercuartílico desde los bordes de la caja. Los puntos exteriores son valores atípicos según esta regla, no necesariamente errores. Compara medianas y dispersión; las diferencias entre grupos no demuestran causalidad.',
 error='', check='')

# Código explícito de cada gráfico, compartido entre web y notebook.
from codigos_graficos import EXPLORACION, BOXPLOTS
for actividad_id, bloques in [('P1-02', EXPLORACION), ('P1-06', BOXPLOTS)]:
 actividad = next(a for a in activities if a['id'] == actividad_id)
 actividad['code'] = '\n\n'.join('# '+titulo+'\n'+codigo for titulo, codigo in bloques)
 actividad['task'] = 'Ejecuta los bloques de R para reproducir cada uno de los gráficos de esta lámina, después de cargar datos en la lámina 02.'

from video_datasets import CHAPTERS
estructuras = next(a for a in activities if a['id'] == 'P1-07')
estructuras.update(
 dataset_video=True, question='¿Qué representa cada punto y cómo se ordena?', predict='',
 task='Observa el video silencioso de 45 segundos: corte transversal, serie de tiempo y datos de panel. Los puntos se ordenan por unidad, por período o por ambos. Los ejemplos son ficticios.',
 lesson_transcript=chr(10).join('### ' + c['title'] + chr(10) + chr(10) + c['explanation'] + chr(10) for c in CHAPTERS),
 code='''# Ejemplos ficticios: los mismos puntos que aparecen en el video.
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
print(panel)''',
 answer='En el corte transversal cada punto es una unidad distinta en 2020. En la serie de tiempo cada punto es un período de la unidad A. En el panel cada punto combina una de las unidades A, B o C con un período. Los colores conservan la identidad de la unidad y las líneas solo conectan observaciones; no son regresiones estimadas. wage1 es transversal.',
 error='', check='Si seguimos a las mismas personas A, B y C en 2020, 2021 y 2022, tenemos datos de panel.')

activities = [a for a in activities if a['id'] != 'P1-03']

# Primero las razones para muestrear y luego población, muestra y unidad.
indice_poblacion = next(i for i,a in enumerate(activities) if a['id'] == 'P1-08')
indice_razones = next(i for i,a in enumerate(activities) if a['id'] == 'P1-09')
activities[indice_poblacion], activities[indice_razones] = activities[indice_razones], activities[indice_poblacion]
razones = next(a for a in activities if a['id'] == 'P1-09')
razones.update(
 question='¿Para qué trabajar con una parte de los datos?', predict='',
 reason_panels=[
  ('computacional', 'Costo computacional',
   'Con volúmenes muy grandes, por ejemplo terabytes (TB), incluso un análisis descriptivo puede requerir mucho tiempo, memoria e infraestructura analítica. Repetir cálculos para explorar y aprender de los datos también tiene un costo. Una alternativa es trabajar con una muestra representativa de la población de datos, seleccionada mediante un diseño acorde con el objetivo. Esto reduce la carga de cálculo, pero introduce incertidumbre muestral: hay que revisar la cobertura de los grupos, la precisión y posibles sesgos, especialmente si interesan eventos poco frecuentes. Una muestra grande o cómoda de obtener no garantiza representatividad.'),
  ('presupuesto', 'Presupuesto',
   'Observar a toda la población puede exigir más dinero, tiempo y personal de los disponibles. Una muestra permite planificar la recolección y concentrar recursos en mediciones de calidad. Por ejemplo, con un presupuesto de 100 unidades y un costo de 5 por entrevista, podemos financiar 20 entrevistas. El tamaño y la selección deben responder al objetivo del estudio: ahorrar no garantiza representatividad ni precisión.'),
  ('validaciones', 'Validaciones (train / test)',
   'Para evaluar un modelo predictivo, dividimos los datos disponibles: train se utiliza para ajustar el modelo y test para medir su desempeño con observaciones que no participaron en el ajuste. Si evaluamos con los mismos datos de entrenamiento, podemos obtener una impresión demasiado optimista. El conjunto test se reserva para la evaluación final; la elección y el ajuste del modelo se realizan dentro de train, por ejemplo con validación cruzada. Esta partición evalúa predicción: no prueba causalidad ni corrige una muestra sesgada. En series de tiempo debemos respetar el orden temporal.'),
  ('terreno', 'Estudios en terreno',
   'Visitar hogares, empresas o localidades requiere coordinar rutas, encuestadores, horarios y permisos. Una muestra hace viable ese trabajo y permite supervisar las entrevistas y revisar la calidad de las respuestas. Antes de salir se define a quién se quiere estudiar, el marco de selección y cómo se elegirán las unidades; luego se registran los rechazos y las ausencias. Entrevistar únicamente a quienes resulta más fácil contactar puede dejar fuera a grupos importantes y sesgar las conclusiones.')])

# La explicación de estructuras abre la parte de econometría.
video_inicial = next(a for a in activities if a['id'] == 'P1-07')
activities.remove(video_inicial)
inicio_econometria = next(i for i,a in enumerate(activities) if a['id'].startswith('P1-'))
activities.insert(inicio_econometria, video_inicial)

next(a for a in activities if a['id'] == 'P1-09').update(reason_only=True, code='', task='', answer='')

from muestreos_taller import PREPARACION, EJEMPLOS
muestreo = next(a for a in activities if a['id'] == 'P1-08')
muestreo.update(
 title='Tipos de muestreo en R con wage1', sampling_examples=EJEMPLOS,
 preparation_code=PREPARACION,
 question='¿Cómo seleccionamos personas con cada tipo de muestreo?', predict='',
 task='Usamos wage1, incluida en el paquete wooldridge. Ejecuta la preparación una vez y luego cada ejemplo en el orden de la clase de Sebastián. Para practicar, las 526 filas forman nuestro marco didáctico; no reproducimos el diseño original de la CPS ni afirmamos representatividad nacional.',
 code=PREPARACION+'\n\n'+'\n\n'.join('# '+example['title']+'\n'+example['code'] for example in EJEMPLOS),
 answer='Los ejemplos seleccionan filas de wage1. Los cuatro primeros usan un mecanismo aleatorio; el último depende de un criterio y del orden disponible. Los diseños tienen tamaños y probabilidades de inclusión diferentes: aquí aprendemos a seleccionar, no comparamos su precisión.',
 error='', check='¿En qué método aparecen todos los estratos? En el estratificado. ¿En cuál seleccionamos primero grupos y después personas? En conglomerados de dos etapas.')
# Se eliminan las que eran las láminas 09 y 10 antes de esta revisión.
activities = [a for a in activities if a['id'] not in ('P1-10', 'P1-11')]

# Fusionar las actuales 08, 09 y 10 en una sola lámina de cuatro métodos.
activities = [a for a in activities if a['id'] not in ('P1-12', 'P1-13')]
muestreo.update(
 title='Cuatro técnicas de muestreo en R con wage1',
 task='Usamos wage1, incluida en el paquete wooldridge. Ejecuta la preparación una vez y después los cuatro ejemplos en orden. Las 526 personas de la base forman nuestro marco didáctico; estas selecciones no reproducen el diseño original de la CPS ni permiten afirmar representatividad nacional.',
 answer='Simple: sortea personas directamente. Sistemático: sortea un inicio y recorre la lista cada 20 posiciones. Estratificado: sortea personas dentro de todos los estratos. Conglomerados de dos etapas: sortea grupos y después personas dentro de esos grupos.',
 check='¿Qué diferencia hay entre estratificar y seleccionar conglomerados? En el estratificado seleccionamos dentro de todos los estratos; en conglomerados seleccionamos solo algunos grupos y, en este ejemplo, sorteamos personas dentro de ellos.')

descriptiva = next(a for a in activities if a['id'] == 'P1-14')
descriptiva.update(
 title='Análisis descriptivo de wage1', descriptive=True,
 question='¿Qué nos dicen las seis variables de la base completa?', predict='',
 task='Explora calidad, medidas descriptivas, frecuencias, correlaciones y salarios por grupo. El código completo en R está al final de la lámina y en la celda siguiente. Describe las 526 personas de la base completa, no las submuestras de los ejercicios de muestreo.',
 code=(root/'herramientas/analisis_descriptivo_wage1.R').read_text().strip(),
 answer='La media y la mediana describen el centro; varianza, desviación y RIQ describen dispersión; percentiles y forma ayudan a reconocer asimetría y valores extremos. Las correlaciones Pearson y Spearman resumen asociaciones diferentes. Las medias de indicadores 0/1 son proporciones. Las comparaciones por educación, sexo y estado civil son descriptivas, no causales.',
 error='', check='¿La media de female es un salario? No: es la proporción de registros con female = 1. ¿Una correlación demuestra causalidad? No.')

# La antigua lámina 09 de Econometría abre ahora la ayudantía descriptiva.
activities = [a for a in activities if a['id'] != 'P2-01']
descriptiva.update(id='P2-01', title='Salarios: promedio, mediana, moda y percentiles',
 slides='Ayudantía · Localización central y percentiles de Sebastián',
 question='¿Cómo se distribuye el salario total y por estado civil?',
 task='Compara el total, no casados (married = 0) y casados (married = 1). Obtén promedio, mediana, moda y percentiles 24, 50 y 75. married = 0 no identifica exclusivamente a personas solteras.',
 code=(root/'herramientas/analisis_descriptivo_wage1.R').read_text().strip(),
 answer='La mediana coincide con P50. La moda puede contener varios valores empatados. Los percentiles usan type = 7. Los salarios son USD por hora de 1976 y la comparación entre estados civiles es descriptiva, no causal.',
 check='¿P50 coincide con la mediana? Sí. ¿married = 0 significa exclusivamente soltero? No.')
activities.remove(descriptiva)
inicio_p2 = next(i for i,a in enumerate(activities) if a['id'].startswith('P2-'))
activities.insert(inicio_p2,descriptiva)

# La ayudantía descriptiva se concentra en dos láminas.
activities = [a for a in activities if not a['id'].startswith('P2-') or a['id']=='P2-01']
dispersion_actividad = dict(id='P2-02',title='Dispersión: de la nube compacta a la nube amplia',
 slides='Ayudantía · Dispersión, histograma y boxplot de Sebastián', mode='Presencial',
 question='¿Cómo cambia una nube cuando aumenta su varianza?',predict='',
 task='Compara varianza, desviación estándar, rango, RIQ y CV del salario total y por estado civil. Después usa la nube artificial para aumentar la dispersión sin mover la media.',
 code=(root/'herramientas/dispersion_salarios.R').read_text().strip(),
 answer='Varianza = desviación estándar al cuadrado. La varianza usa n − 1 y unidades al cuadrado; la desviación mantiene las unidades originales. RIQ = P75 − P25. La altura de la nube solo separa puntos; la variación representada es horizontal.',
 error='',check='',dispersion_demo=True)
activities.insert(next(i for i,a in enumerate(activities) if a['id'].startswith('P3-')),dispersion_actividad)

# Síntesis de inferencia: cinco láminas, sin temas ajenos a la cátedra.
from inferencia_compacta import ACTIVITIES as INFERENCIA
activities = [a for a in activities if not a['id'].startswith('P3-')] + INFERENCIA

header='''# Taller 1 · Del código a los datos

**Iván · Taller presencial · Econometría ICS-294 · 8 a 10 estudiantes**

¿Podemos describir salarios sin confundir una asociación con una causa? Primero aprenderemos a dar instrucciones a R; después recorreremos los contenidos de Sebastián, en su mismo orden.

[Instrucciones](instruccion-clase-taller-1.md) · [Notebook de R](clase-taller-1.ipynb) · [Guía docente](guia-docente-taller-1.md) · [Lectura comparativa](Lectura%20clase%201%20-%20material%20existente.md) · [Clase de Sebastián](https://hizocar.github.io/econometria-usm/clases/clase1/)

## Objetivos

Al terminar la ruta presencial podrás:

- Usar sentencias clave como if, else, while y for, para hacer rutinas.
- Crear y modificar **vectores y matrices**, utilizando índices y preasignación.
- Reconocer una base transversal, resumir salarios con gráficos y estadísticos y explicar la interpretación de un intervalo de confianza. Las ampliaciones permiten completar la práctica de todos los apartados.

## Agenda presencial · 140 minutos efectivos

| Hora | Minutos | Trabajo |
|---|---:|---|
| 18:50–18:55 | 5 | Diagnóstico y apertura del notebook |
| 18:55–19:35 | 40 | NIV-01 a NIV-08 y NIV-NOTEBOOK: demostraciones, integración y vista general |
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

La documentación advierte inconsistencias entre experiencia potencial y antigüedad en algunos registros. No las corregimos arbitrariamente ni usamos esas columnas para inferir trayectoria laboral. La carga conserva todas las filas y selecciona las seis variables del taller, sin eliminar observaciones. Esta selección no garantiza representatividad. `educ16` se deriva de educ >= 16, sin afirmar titulación.

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
 if numero == 1 and bloque in ('P2', 'P3'):
  titulo_bloque = {'P2': 'Parte 2 · Ayudantía · Repaso de estadística descriptiva', 'P3': 'Parte 3 · Ayudantía · Estadística inferencial'}[bloque]
  md('# '+titulo_bloque+'\n', bloque.lower()+'-titulo')
  sections.append('# '+titulo_bloque+'\n')
 if a.get('sampling_examples'):
  intro=f'<a id="{id}"></a>\n## Lámina {numero:02d} · {a["title"]}\n\n{a["task"]}\n\n[Tipos de muestreo en la clase de Sebastián](https://hizocar.github.io/econometria-usm/clases/clase1/#muestreo-aleatorio).\n\n### Preparación\n'
  md(intro,id.lower()+'-consigna');rc(a['preparation_code'],id.lower()+'-r')
  sections.extend([intro,'```r\n'+a['preparation_code']+'\n```\n'])
  for j,example in enumerate(a['sampling_examples'],1):
   explanation='### '+str(j)+'. '+example['title']+'\n\n'+example['description']+'\n'
   md(explanation,id.lower()+f'-metodo-{j}');rc(example['code'],id.lower()+f'-metodo-{j}-r')
   md(example['reading'],id.lower()+f'-metodo-{j}-lectura')
   sections.extend([explanation,'```r\n'+example['code']+'\n```\n',example['reading']+'\n'])
  continue
 if a.get('reason_only'):
  reasons=f'<a id="{id}"></a>\n## Lámina {numero:02d} · {a["title"]}\n\n{a["question"]}\n\n'
  reasons += '\n'.join('### '+title+'\n\n'+text+'\n' for _,title,text in a['reason_panels'])
  reasons += '\nReferencias: [tidymodels](https://www.tidymodels.org/start/recipes/) y [Banco Mundial](https://www.worldbank.org/en/programs/lsms/publication/capturing-what-matters).\n\n**Comprueba:** '+a['check']+'\n'
  md(reasons,id.lower()+'-consigna');sections.append(reasons)
  continue
 if a.get('overview'):
  overview=f"<a id=\"{id}\"></a>\n## Lámina {numero:02d} · {a['title']}\n\n### {a['question']}\n\n{a['task']}\n"
  md(overview,id.lower()+'-consigna')
  sections.append(overview)
  continue
 intro=f'''<a id="{id}"></a>
## Lámina {numero:02d} · {a['title']}

**Identificador de enlace:** `{id}`. La numeración se reinicia por bloque, como en la web.

**Referencia:** {a['slides']} · **Modalidad:** {a['mode']}.

{('**Pregunta:** ' + a['question']) if a['question'] else ''}

{a.get('description', '')}

{chr(10).join('### ' + title + chr(10) + chr(10) + text + chr(10) for _,title,text in a.get('reason_panels', []))}

{('[Referencias: evaluación predictiva, tidymodels](https://www.tidymodels.org/start/recipes/) y [diseño de encuestas, Banco Mundial](https://www.worldbank.org/en/programs/lsms/publication/capturing-what-matters).') if a.get('reason_panels') else ''}

{('[Video interactivo en la web](https://ivanrenatoc.github.io/UTFSM-econometria/#P1-07)' + chr(10) + chr(10) + a['lesson_transcript']) if a.get('lesson_transcript') else ''}

{('### ' + a['explanation_title'] + chr(10) + chr(10) + a['explanation'] + chr(10) + chr(10) + '[Referencia: duración habitual de estudios universitarios, NCES](' + a['explanation_source'] + '). Los tamaños de grupo se calcularon con el CSV del taller.') if a.get('explanation') else ''}

{chr(10).join('- `' + name + '`: ' + meaning for name, meaning in a.get('variable_definitions', []))}

{('[Documentación de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html). El paquete se instala desde CRAN: `repos = "https://cloud.r-project.org/"`.') if a.get('description') else ''}

{('**Antes de ejecutar:** ' + a['predict']) if a['predict'] else ''}

**Consigna:** {a['task']}

**Datos:** {'Objetos artificiales de programación.' if id.startswith('NIV') else 'wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.'}
'''
 md(intro,id.lower()+'-consigna')
 solution=f"### Solución · {id}\n\nEjecutar después de intentar la consigna.\n"
 md(solution,id.lower()+'-solucion')
 rc(a['code'],id.lower()+'-r',['solucion'])
 discussion=f"**Lectura del resultado:** {a['answer']}\n"
 if a.get('note'): discussion += '\n**' + a['note'] + '**\n'
 if a.get('comparison'): discussion += '\n**Diferencia entre while y for:** ' + a['comparison'] + '\n'
 if a['error']: discussion += f"\n**Error frecuente:** {a['error']}\n"
 if a['check']: discussion += f"\n**Comprueba:** {a.get('check_markdown', a['check'])}\n"
 md(discussion,id.lower()+'-lectura')
 sections.extend([intro,solution,'```r\n'+a['code']+'\n```\n',discussion])
 if 'practice' in a:
  practice=a['practice']
  exercise=f"### Comprueba lo aprendido · Lámina {numero:02d}\n\n{practice['task']}\n\nIntenta resolverlo antes de continuar a la solución.\n"
  md(exercise,id.lower()+'-practica-consigna')
  md('### Solución del ejercicio de comprobación\n',id.lower()+'-practica-solucion')
  rc(practice['code'],id.lower()+'-practica-r',['solucion','comprobacion'])
  md(practice['answer'],id.lower()+'-practica-lectura')
  sections.extend([exercise,'### Solución del ejercicio de comprobación\n','```r\n'+practice['code']+'\n```\n',practice['answer']])
md(closing,'cierre'); sections.append(closing)
from ejercitacion import markdown as ejercicios_markdown, LOAD as ejercicios_carga
md(ejercicios_markdown(), 'ejercitacion')
sections.append(ejercicios_markdown())
rc('# Escribe aquí tu solución del desafío de wall balls.', 'ejercitacion-wall-balls-r')
rc(ejercicios_carga, 'ejercitacion-wage2-carga')
for pregunta in range(1, 11):
 rc(f'# Respuesta a la pregunta {pregunta}: código e interpretación.', f'ejercitacion-pregunta-{pregunta}')
rows=['| Actividad | Referencia web | Sección y celda de código del notebook | Modalidad |','|---|---|---|---|']
for a in activities:
 cells_ref=f"`{a['id'].lower()}-consigna`" if a.get('overview') or a.get('reason_only') else f"`{a['id'].lower()}-consigna` / `{a['id'].lower()}-r`"
 rows.append(f"| {a['id']} | {a['slides']} | {cells_ref} | {a['mode']} |")
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
| Muestras didácticas, sigma conocida y límites de inferencia | P1-08, P3-01 a P3-18 |
| Semillas, reproducción y verificación | Celdas de selección/simulación, cierre |
| Autoevaluación y soluciones | cierre |
| Preparación y alternativa sin conexión | inicio, P1-01 |
| Trazabilidad y cobertura | matriz-correspondencia |

**Organización actual:** 25 láminas (10 de nivelación, 8 introductorias, 2 descriptivas y 5 inferenciales), con las modificaciones y eliminaciones solicitadas por el docente. La trazabilidad muestra el material conservado; no equivale a una certificación de ejecución ni a 25 láminas resueltas en clase.
'''
md(trace,'matriz-correspondencia'); sections.append(trace)
notebook=dict(nbformat=4,nbformat_minor=5,metadata=dict(kernelspec=dict(display_name='R',language='R',name='ir'),language_info=dict(name='R',file_extension='.r',mimetype='text/x-r-source'),taller=dict(docente='Iván',audiencia='8–10',inicio='18:50',fin='21:25',pausa_min=15,trabajo_min=140)),cells=cells)
(root/'clase-taller-1.ipynb').write_text(json.dumps(notebook,ensure_ascii=False,indent=1)+'\n')
(root/'guia-actividades-taller-1.md').write_text('\n\n'.join(sections))
script=['# Taller 1: ejecutar desde clase-1-taller/ en una sesión limpia.\n# Equivalente a todas las celdas R del notebook; no instala paquetes.\n']
for a in activities:
 script.extend(['\n# '+a['id']+' · '+a['title']+'\n',a['code']+'\n'])
 if 'practice' in a:
  script.extend(['\n# Comprueba lo aprendido: '+a['practice']['task']+'\n',a['practice']['code']+'\n'])
script.extend(['\n# Ejercitación: resuelve las consignas de la guía.\n', '# Desafío wall balls: escribe aquí tu programa.\n', ejercicios_carga+'\n', '\n'.join(f'# Pregunta {i}: escribe tu respuesta.' for i in range(1, 11))+'\n'])
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
| 18:57–19:00 | NIV-ASIG (lámina 02). Asigna x e y, calcula z y w; print(x) y print(w) muestran 2 y 3. |
| 19:00–19:04 | NIV-03 (lámina 03). Anticipar el mensaje con valores 3 y 8; el ejemplo define sus propios valores. |
| 19:04–19:07 | NIV-06 (lámina 04). while: condición previa, actualización y límite de seguridad. |
| 19:07–19:09 | NIV-FOR (lámina 05). for: recorrido de pasos y salida anticipada con break. |
| 19:09–19:14 | NIV-05 (lámina 06). Parejas completan 1, 2, 4, 8, 16 y 32. |
| 19:14–19:20 | NIV-02 (lámina 07). Reservar 20 ceros; asignar −1 en posiciones impares y luego reemplazar cada cero por su índice. |
| 19:20–19:27 | NIV-07. Crear la identidad de 3 × 3; reconocer filas, columnas y la transposición. |
| 19:27–19:33 | NIV-08. Crear las potencias de 3 y organizarlas en una matriz de 3 × 2; leer sus columnas. |
| 19:33–19:35 | NIV-NOTEBOOK (lámina 10). Vista general: librerías, adecuación de datos, EDA, modelamiento y resultados. |
| 19:35–19:42 | P1-01 a P1-05 en orden. Cargar datos; ubicar país/año; discutir asociación sin calcular aún medias. |
| 19:42–19:47 | Recorrer video, gráficos y razones para muestrear. Preparar wage1 para P1-08. |
| 19:47–20:00 | P1-08: ejecutar preparación y cuatro muestreos en orden. Continuar con P1-14. No comparar eficiencia de grupos artificiales. |
| 20:00–20:15 | Pausa de 15 minutos. |
| 20:15–20:18 | P2-01 y P2-02. Qué entra y sale de una función. |
| 20:18–20:27 | P2-03 a P2-05. Cada pareja anticipa qué hace un extremo y calcula medidas de centro y dispersión. |
| 20:27–20:40 | P2-06 y P2-07. Mostrar histograma y boxplot, comparar intervalos y explicar atípicos sin borrarlos. |
| 20:40–20:47 | P3-01: inferencia, TCL y supuestos; cambiar n en la figura. |
| 20:47–20:54 | P3-05: IC de media y repetición de intervalos del ejemplo de ventas. |
| 20:54–21:01 | P3-07: confianza, precisión y planificación de n. |
| 21:01–21:08 | P3-11: 19/200 defectuosos, referencia 0,05 y tamaño para proporciones. |
| 21:08–21:15 | P3-15: diferencia de medias con varianzas conocidas, ejemplo de carreras de Sebastián. |
| 21:15–21:25 | Autoevaluación individual, discusión en pareja y respuesta colectiva. Registrar dudas para apoyo posterior. |

El tiempo para todas las láminas es una revisión computacional selectiva, no una clase exhaustiva de inferencia. Las ampliaciones se conservan en orden y no se eliminan del notebook. Si el diagnóstico muestra dificultades, reducir modificaciones autónomas durante la sesión y usar las demostraciones ya preparadas; conservar el horario y asignar la práctica restante para después.

## Preguntas que vale la pena detenerse a escuchar

- NIV-03: ¿por qué no usar if con todo el vector? Esperar que distingan una decisión de una selección por elemento.
- P1-04: ¿qué no mantiene constante este gráfico? Esperar habilidad, experiencia o contexto familiar.
- P1-08: ¿qué representa cada selección? Aclarar inicio aleatorio del sistemático, pesos por estrato y grupos artificiales.
- P2-03: ¿el dato extremo es real? No: es una copia alterada con propósito explícito.
- P3-01: ¿de qué población conocemos sigma? Solo de nuestra distribución empírica didáctica.
- P3-05: ¿el 95% tiene que cumplirse exactamente en pocas repeticiones? No; fluctúa y depende de aproximación.
- P3-15: ¿puede decirse que estudiar causó la diferencia? No.

## Revisión y decisiones

La matriz completa de cobertura y los IDs están al final de la guía y notebook. Las guías y el notebook comparten consignas, soluciones y código generados desde `herramientas/generar_taller.py`. No editar solo una copia: regenerar las salidas tras modificar ese origen. El script `.R` facilita una alternativa en RStudio.

No se publicó ni modificó ningún sitio. No se requirió GitHub para crear el material. La experiencia previa e instalaciones de los alumnos siguen sin confirmarse; comprobarlas antes del taller. El material contiene soluciones abiertas en celdas separadas: durante la actividad detenerse antes de la solución y pedir al estudiante que escriba su intento en una celda nueva.
''')
# Correspondencia explícita de la síntesis con la fuente de la cátedra.
with (root/'guia-docente-taller-1.md').open('a') as archivo:
 archivo.write('''\n## Correspondencia de las cinco láminas de inferencia con Sebastián\n\n| Lámina del taller | Contenido de la cátedra conservado |\n|---|---|\n| 01 · Inferir, TCL y supuestos | Estadística inferencial, distribución muestral del promedio, TCL, i.i.d. y momentos finitos. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#teorema-central-del-limite). |\n| 02 · IC de una media | Interpretación frecuentista, σ conocida, ventas: media 200, σ 60, n 36, IC 95 %. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ic-ejemplo1). |\n| 03 · Confianza, precisión y n | Niveles de confianza, ancho/margen, efecto de n y fórmula de tamaño muestral con redondeo superior. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#intervalos-de-confianza-determinacion-del-tamano-muestral). |\n| 04 · Proporciones | Aproximación normal y condiciones, 19 defectuosos de 200, referencia 0,05, planificación con p* y E. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ic-para-las-proporciones-ejemplo). |\n| 05 · Diferencia de medias | Dos grupos independientes, varianzas conocidas, medias 800.000/680.000, n 144/121 y σ 60.000/50.000; interpretación del cero. [Fuente](https://hizocar.github.io/econometria-usm/clases/clase1/#ejemplo_1). |\n\nLa visualización del TCL usa wage1 como población empírica didáctica. Los otros ejemplos conservan los números de Sebastián y no se atribuyen a wage1. No se añaden pruebas de hipótesis, regresiones estimadas ni métodos fuera del repaso de la cátedra. Las figuras se actualizan matemáticamente en el navegador; el código R reproduce las fórmulas y sus parámetros. No se ha ejecutado R en este entorno.\n''')

# Checks on data, notebook IDs and complete mapping; no claim of R execution.
ids=[c['id'] for c in cells]
assert len(ids)==len(set(ids))
assert len(activities)==25
assert sum(c['cell_type']=='code' for c in cells)==sum(not a.get('overview') and not a.get('reason_only') for a in activities)+sum('practice' in a for a in activities)+sum(len(a.get('sampling_examples', [])) for a in activities)+12
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
