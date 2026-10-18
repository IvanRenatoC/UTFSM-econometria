# Taller 1 · Del código a los datos

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


<a id="NIV-01"></a>
## Lámina 01 · Escribe tu nombre

**Identificador de enlace:** `NIV-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** Vamos a hacer un ejercicio muy elemental, para que vayamos partiendo desde el inicio para terminar en algo mucho más avanzado.















**Antes de ejecutar:** ¿Qué crees que aparecerá en la consola al ejecutar print("tu nombre")?

**Consigna:** Reemplaza tu nombre por tu propio nombre, conservando las comillas, y ejecuta la instrucción.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-01

Ejecutar después de intentar la consigna.


```r
print("tu nombre")
```


**Lectura del resultado:** print() muestra el texto entre comillas en la consola. Al reemplazarlo por tu nombre, R imprimirá ese nombre.

**Error frecuente:** Escribir el nombre sin comillas: R intentará interpretarlo como un objeto.

**Comprueba:** ¿Qué debes cambiar para mostrar otro nombre? El texto que está dentro de las comillas.


<a id="NIV-ASIG"></a>
## Lámina 02 · Asignación de valores

**Identificador de enlace:** `NIV-ASIG`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo damos un nombre a un valor y lo usamos en un cálculo?















**Antes de ejecutar:** Con x = 2 e y = 5, ¿cuánto valdrán z y w? ¿Qué mostrará cada print?

**Consigna:** Ejecuta las instrucciones una a una. Después consulta z con print(z).

**Datos:** Objetos artificiales de programación.


### Solución · NIV-ASIG

Ejecutar después de intentar la consigna.


```r
x <- 2
y <- 5
z <- x - y
w <- abs(x - y)
print(x)
print(w)
```


**Lectura del resultado:** La flecha <- asigna el resultado de la derecha al nombre de la izquierda. x recibe 2 e y recibe 5. z recibe x - y = -3. abs() calcula el valor absoluto: w recibe 3. print(x) muestra 2 y print(w) muestra 3. z queda guardado, aunque no se imprime en estas instrucciones. Si cambias x o y, debes ejecutar de nuevo las asignaciones de z y w para recalcularlos.

**Los valores quedan asignados mientras la sesión siga activa. En R de escritorio se conservan hasta que los reasignes, los elimines o cierres o reinicies la sesión. En Google Colab ocurre lo mismo mientras el entorno de ejecución permanezca activo: se pierden al reiniciarlo o eliminarlo, no necesariamente por una desconexión temporal.**

**Error frecuente:** Invertir la flecha o creer que z se recalcula automáticamente al cambiar x. En la expresión de la derecha, x e y deben estar definidos previamente.

**Comprueba:** ¿Cuánto valen z y w? -3 y 3. Si ejecutas solo x <- 10, ¿cambia z? No; debes volver a ejecutar z <- x - y.


<a id="NIV-03"></a>
## Lámina 03 · Condicionales: if, else y operadores lógicos

**Identificador de enlace:** `NIV-03`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo elegimos una acción según una condición?















**Antes de ejecutar:** ¿Qué mensaje produce valor = 8?

**Consigna:** Prueba con 3 y con 8; selecciona además todos los valores mayores que 4 del vector de ejemplo.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-03

Ejecutar después de intentar la consigna.


```r
v <- c(2, 7, 9)  # Valores del ejemplo, definidos antes de usarlos.
valor <- 8
if (valor > 4) {
  mensaje <- "Supera el umbral"
} else {
  mensaje <- "No supera el umbral"
}
print(mensaje)
print(v[v > 4])
```


**Lectura del resultado:** if elige un camino con una condición única. La selección lógica trabaja con varias posiciones. Usa & y | para condiciones por elemento, && y || para condiciones escalares.

**Error frecuente:** Escribir if(v > 4), con una condición por cada elemento.

**Comprueba:** ¿valor > 4 es una asignación? No, es una comparación.


<a id="NIV-06"></a>
## Lámina 04 · Ciclos while y condiciones de término

**Identificador de enlace:** `NIV-06`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** Primera parte: while. Iteraciones y loops















**Antes de ejecutar:** ¿Se detendrá antes de 20 pasos?

**Consigna:** Parte en 1 y multiplica el valor por 2 en cada iteración, hasta alcanzar 100. Conserva los valores de cada paso.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-06

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** while evalúa su condición antes de cada repetición: seguimos si valor < 100 y paso < max_pasos. En cada iteración se multiplica el valor por 2 y se actualiza el contador paso. Se llega a 128 después de siete iteraciones y la condición valor < 100 deja de cumplirse. El límite de 20 pasos evita que el ciclo continúe indefinidamente si la condición se plantea mal. Si la condición inicial es falsa, el cuerpo no se ejecuta.

**Error frecuente:** No actualizar valor o paso.

**Comprueba:** ¿Qué ocurre si max_pasos es 3? Termina por el límite, sin llegar a 100.


<a id="NIV-FOR"></a>
## Lámina 05 · Ciclos for y condiciones de término

**Identificador de enlace:** `NIV-FOR`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** Segunda parte: for. ¿Cómo repetimos el cálculo con un límite de pasos?















**Antes de ejecutar:** ¿Cuándo terminará: al agotar los 20 pasos o al alcanzar 100?

**Consigna:** Ejecuta la versión con for. Compara su trayectoria con la del while y prueba max_pasos <- 3.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-FOR

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** for recorre los pasos de seq_len(max_pasos). Termina al agotar esa secuencia o antes si ejecuta break. Aquí el if detecta valor >= 100 y break sale del ciclo en el paso 7, con valor 128; la trayectoria coincide con la del while. Si max_pasos es 3, se agota la secuencia con valor 8. En este ejemplo max_pasos debe ser un entero positivo; paso recibe automáticamente cada índice, sin escribir paso <- paso + 1.

**Diferencia entre while y for:** while repite instrucciones mientras una condición sea verdadera; el número de repeticiones depende de cuándo deje de cumplirse. for recorre una secuencia de valores, uno por iteración. En este ejemplo, for puede terminar antes de agotar la secuencia porque if detecta que se alcanzó 100 y break sale del ciclo. Ambos producen la misma trayectoria, pero expresan el control de la repetición de distinta forma.

**Error frecuente:** Confundir el recorrido de for con una prueba automática de valor < 100: esa condición de salida anticipada se expresa con if y break. No usar paso después de un ciclo vacío sin inicializarlo.

**Comprueba:** ¿Qué ocurre si eliminas if y break? Se ejecutan los 20 pasos. ¿Qué ocurre con max_pasos <- 3? Termina por agotar los pasos, sin alcanzar 100.


<a id="NIV-05"></a>
## Lámina 06 · Sucesión geométrica: 1, 2, 4, 8, 16…

**Identificador de enlace:** `NIV-05`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo construimos la sucesión 1, 2, 4, 8, 16…?















**Antes de ejecutar:** Observa la sucesión 1, 2, 4, 8, 16… ¿Cuál es el siguiente número?

**Consigna:** Genera los seis primeros términos de la sucesión 1, 2, 4, 8, 16… Multiplica cada término por 2 para obtener el siguiente.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-05

Ejecutar después de intentar la consigna.


```r
sucesion <- numeric(6)
sucesion[1] <- 1
for (i in 2:6) {
  sucesion[i] <- 2 * sucesion[i - 1]
}
print(sucesion)
```


**Lectura del resultado:** El resultado es 1, 2, 4, 8, 16, 32. Cada término es el anterior multiplicado por 2: por eso es una sucesión geométrica de razón 2. Primero asignamos el valor 1 a la primera posición; el ciclo calcula las cinco posiciones restantes.

**Error frecuente:** Empezar el ciclo en la posición 1 y tratar de leer la posición 0. En R los índices comienzan en 1.

**Comprueba:** ¿Qué número sigue después de 32? 64, porque 32 × 2 = 64.


<a id="NIV-02"></a>
## Lámina 07 · Vectores: creación, selección, modificación y llenado con for

**Identificador de enlace:** `NIV-02`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo reservamos un vector y modificamos solo algunas posiciones?

















**Consigna:** Crea un vector de largo 20, solo con valores 0, pero con un −1 en las posiciones impares.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-02

Ejecutar después de intentar la consigna.


```r
v <- numeric(20)
for (i in 1:20) {
  if (i %% 2 != 0) {
    v[i] <- -1
  }
}
print(v)
```


**Lectura del resultado:** El vector alterna −1, 0, −1, 0 hasta completar 20 posiciones. numeric(20) reserva un vector de veinte ceros. El ciclo recorre sus posiciones y la condición i %% 2 != 0 identifica los índices impares. Solo esas posiciones cambian a −1: quedan diez valores −1 y diez ceros.

**Error frecuente:** Confundir el valor guardado con su posición. La condición se aplica al índice i, no al contenido v[i].


### Comprueba lo aprendido · Lámina 07

Trabaja sobre el vector anterior: reemplaza cada 0 por el número de su posición y conserva los valores −1.

Intenta resolverlo antes de continuar a la solución.


### Solución del ejercicio de comprobación


```r
for (i in seq_along(v)) {
  if (v[i] == 0) {
    v[i] <- i
  }
}
print(v)
```


El resultado alterna −1, 2, −1, 4, −1, 6 y continúa hasta −1, 20. Las posiciones impares conservan −1; cada posición par contiene su propio índice.

<a id="NIV-07"></a>
## Lámina 08 · Matrices y ciclos anidados

**Identificador de enlace:** `NIV-07`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo guardamos resultados por filas y columnas?















**Antes de ejecutar:** Indica cuáles son las posiciones (2, 3) y (3, 2).

**Consigna:** Llena una matriz de 3 × 3 solo con valores 0; luego haz que su diagonal principal contenga únicamente valores 1.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-07

Ejecutar después de intentar la consigna.


```r
A <- matrix(0, nrow = 3, ncol = 3)
for (i in 1:3) {
  A[i, i] <- 1
}
print(A)
```


**Lectura del resultado:** Esta es la matriz identidad: cumple en la multiplicación de matrices un papel similar al 1 en los escalares. Tiene unos en la diagonal principal y ceros en las otras posiciones.

**Error frecuente:** Confundir la diagonal principal con una fila completa. En la diagonal principal coinciden el índice de fila y el de columna.

**Comprueba:** Si $A$ es una matriz de $2 \times 4$, ¿se cumple $A(2,3) = A^{\mathsf{T}}(3,2)$? $A^{\mathsf{T}}$ es la transpuesta de $A$ y en R se obtiene con `t(A)`.


### Comprueba lo aprendido · Lámina 08



Intenta resolverlo antes de continuar a la solución.


### Solución del ejercicio de comprobación


```r
A <- matrix(1:8, nrow = 2, ncol = 4)
print(A[2, 3])
print(t(A)[3, 2])
print(A[2, 3] == t(A)[3, 2])
```


Sí. La transposición intercambia filas y columnas: A[2,3] y t(A)[3,2] contienen el mismo elemento. En este ejemplo ambos valen 6 y la comparación devuelve TRUE.

<a id="NIV-08"></a>
## Lámina 09 · Actividad integradora: sucesiones y matrices

**Identificador de enlace:** `NIV-08`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Nivelación · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo organizamos una sucesión de números en una matriz?

















**Consigna:** Genera la sucesión 3, 9, 27, 81, 243 y 729, es decir, 3 elevado a 1, 2, 3, 4, 5 y 6. Con esos números crea una matriz de 3 × 2.

**Datos:** Objetos artificiales de programación.


### Solución · NIV-08

Ejecutar después de intentar la consigna.


```r
sucesion <- 3^(1:6)
A <- matrix(sucesion, nrow = 3, ncol = 2)
print(sucesion)
print(A)
```


**Lectura del resultado:** La sucesión contiene las seis primeras potencias de 3. matrix() distribuye estos valores por columnas: la primera contiene 3, 9 y 27; la segunda, 81, 243 y 729. Una matriz puede entenderse como varios vectores columna organizados juntos. En estadística siempre vemos matrices.

**Error frecuente:** Leer los valores por filas cuando matrix() los ha organizado por columnas de forma predeterminada.

**Comprueba:** ¿Cuáles son los valores de la segunda columna? 81, 243 y 729.


<a id="NIV-NOTEBOOK"></a>
## Lámina 10 · Vista general de un notebook

### Librerías → adecuación de datos → EDA → modelamiento → resultados

EDA significa análisis exploratorio de datos.


<a id="P1-01"></a>
## Lámina 01 · Introducción a la econometría y a los datos

**Identificador de enlace:** `P1-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 1 · **Modalidad:** Presencial.



datos/wage1.csv es una copia local de wage1, una base del paquete de R wooldridge, asociado al libro de Jeffrey M. Wooldridge. Contiene 526 observaciones de personas y 24 variables de la Current Population Survey (CPS) de Estados Unidos de 1976. Es una base de corte transversal: cada fila corresponde a una persona. En este taller utilizaremos seis variables.









- `wage`: Salario promedio por hora, en dólares estadounidenses de 1976.
- `educ`: Años de educación.
- `exper`: Años de experiencia laboral potencial.
- `tenure`: Años de antigüedad con el empleador actual.
- `female`: Indicador: 1 si la persona está registrada como mujer; 0 en caso contrario.
- `married`: Indicador: 1 si la persona está registrada como casada; 0 en caso contrario.

[Documentación de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html). El paquete se instala desde CRAN: `repos = "https://cloud.r-project.org/"`.



**Consigna:** Carga la base e identifica wage y educ en seis filas.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-01

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** wage1 es un corte transversal observacional de Estados Unidos en 1976. wage es remuneración por hora en dólares nominales de ese período; educ son años de educación. No son pesos chilenos actuales. La inspección no prueba efectos.

**Comprueba:** ¿Cuántas filas tiene el dataset? Tiene 526 filas: son observaciones de personas, no períodos de tiempo.


<a id="P1-02"></a>
## Lámina 02 · Exploración gráfica de los datos

**Identificador de enlace:** `P1-02`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 2 · **Modalidad:** Presencial.

**Pregunta:** Selecciona una variable para explorar su distribución.

















**Consigna:** En la web, pulsa wage, educ, exper, tenure, female o married. En R, cambia el nombre de variable y ejecuta la celda para reproducir el gráfico.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-02

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** Cada gráfico resume las mismas 526 personas. El histograma agrupa salarios en intervalos de 2 USD; las barras cuentan personas para cada cantidad de años; los gráficos circulares muestran proporciones de las categorías 0 y 1.


<a id="P1-04"></a>
## Lámina 03 · Correlación, causalidad y factores no observados

**Identificador de enlace:** `P1-04`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 4 · **Modalidad:** Presencial.

**Pregunta:** Relación lineal de dos variables

















**Consigna:** Observa el gráfico: cada punto representa a una persona. El eje horizontal muestra sus años de educación y el vertical, su salario por hora. El azul identifica a los hombres y el amarillo a las mujeres.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-04

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** La nube de puntos sugiere una asociación positiva: a más años de educación, los salarios tienden a ser mayores, aunque hay mucha dispersión. Las columnas de puntos aparecen porque varias personas tienen los mismos años de educación. A igual educación se observan salarios distintos y los colores permiten comparar ambos grupos. No se ha dibujado ni estimado una recta: el gráfico es una primera aproximación para estudiar una posible relación lineal. Esta asociación, por sí sola, no demuestra que estudiar cause un aumento salarial o que el género corresponda a una condición causal a las diferencias. Para llegar a esa conclusión se debe hacer un estudio más profundo.


<a id="P1-05"></a>
## Lámina 04 · Educación y salarios: alcances de la comparación

**Identificador de enlace:** `P1-05`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · láminas 5–6 · **Modalidad:** Presencial.

**Pregunta:** ¿Podemos llamar universitario a todo registro con educ >= 16?









### ¿Por qué educ ≥ 16 y no educ ≥ 18?

educ mide años de educación, no la edad. Usamos 16 como un umbral didáctico: la referencia habitual es 12 años escolares más unos 4 años de estudios universitarios en Estados Unidos. Esto no permite afirmar que cada persona tenga un título universitario. Exigir 18 años de educación seleccionaría una trayectoria educativa más larga y dejaría fuera a quienes registran 16 o 17 años. En esta base, educ ≥ 16 reúne 99 personas, mientras que educ ≥ 18 reúne solo 19. Para la comparación siguiente mantendremos dos grupos: menos de 16 años y 16 años o más. Es una decisión de agrupación para este ejercicio, no una frontera universal ni una prueba de causalidad.

[Referencia: duración habitual de estudios universitarios, NCES](https://nces.ed.gov/surveys/ctes/tables/glossary_college.asp). Los tamaños de grupo se calcularon con el CSV del taller.





**Antes de ejecutar:** ¿Los dos grupos serán idénticos en sus otras características?

**Consigna:** Crea una etiqueta de umbral educativo y examina filas, sin calcular todavía diferencias de medias.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-05

Ejecutar después de intentar la consigna.


```r
datos$educ16 <- datos$educ >= 16
print(head(datos[c("educ", "educ16", "wage", "exper")], 12))
```


**Lectura del resultado:** educ >= 16 es un umbral de años de educación, no una certificación de título. El ejemplo del 30% de Chile pertenece a cátedra; no se atribuye a esta base. La comparación de promedios se hará en su bloque.

**Error frecuente:** Repetir el 30% como si se hubiese calculado con wage1.

**Comprueba:** ¿Una diferencia entre grupos sería automáticamente efecto de estudiar? No.


<a id="P1-06"></a>
## Lámina 05 · Comparar salarios con boxplots

**Identificador de enlace:** `P1-06`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 7 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Cómo cambia la distribución salarial entre grupos?

















**Consigna:** Selecciona educ, female o married en la web. En R, cambia variable para comparar los salarios por educación (menos de 16 años y 16 años o más), sexo registrado o estado civil registrado.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-06

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** La línea dentro de la caja es la mediana; la caja resume la mitad central de los salarios. Los bigotes llegan hasta los valores más extremos dentro de 1,5 veces el rango intercuartílico desde los bordes de la caja. Los puntos exteriores son valores atípicos según esta regla, no necesariamente errores. Compara medianas y dispersión; las diferencias entre grupos no demuestran causalidad.


<a id="P1-07"></a>
## Lámina 06 · Tipos y estructura de los datos económicos

**Identificador de enlace:** `P1-07`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · láminas 8–11 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué representa cada punto y cómo se ordena?







[Video interactivo en la web](https://ivanrenatoc.github.io/UTFSM-econometria/#P1-07)

### Corte transversal

Los puntos se ordenan por unidad: A, B, C, D, E y F. Todos pertenecen a 2020. El eje vertical muestra el valor observado. Comparamos unidades en un mismo período; el orden horizontal no representa tiempo. wage1, la base del taller, es de corte transversal.

### Serie de tiempo

Los puntos de la unidad A se ordenan de 2020 a 2025. El eje horizontal ahora representa tiempo y el vertical, el valor observado en cada período. La línea ayuda a seguir el orden temporal: no es una recta de regresión. Estudiamos cómo cambia una unidad a través del tiempo.

### Datos de panel

Seguimos a A, B y C de 2020 a 2025. Cada color identifica siempre a la misma unidad. Los puntos se ordenan por período y forman tres trayectorias. Podemos comparar unidades y observar cambios dentro de cada una. Las líneas conectan observaciones de una misma unidad; no son regresiones estimadas.










**Consigna:** Observa el video silencioso de 45 segundos: corte transversal, serie de tiempo y datos de panel. Los puntos se ordenan por unidad, por período o por ambos. Los ejemplos son ficticios.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-07

Ejecutar después de intentar la consigna.


```r
# Ejemplos ficticios: los mismos puntos que aparecen en el video.
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
print(panel)
```


**Lectura del resultado:** En el corte transversal cada punto es una unidad distinta en 2020. En la serie de tiempo cada punto es un período de la unidad A. En el panel cada punto combina una de las unidades A, B o C con un período. Los colores conservan la identidad de la unidad y las líneas solo conectan observaciones; no son regresiones estimadas. wage1 es transversal.

**Comprueba:** Si seguimos a las mismas personas A, B y C en 2020, 2021 y 2022, tenemos datos de panel.


<a id="P1-09"></a>
## Lámina 07 · Razones para trabajar con muestras

**Identificador de enlace:** `P1-09`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 14 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Para qué trabajar con una parte de los datos?



### Presupuesto

Observar a toda la población puede exigir más dinero, tiempo y personal de los disponibles. Una muestra permite planificar la recolección y concentrar recursos en mediciones de calidad. Por ejemplo, con un presupuesto de 100 unidades y un costo de 5 por entrevista, podemos financiar 20 entrevistas. El tamaño y la selección deben responder al objetivo del estudio: ahorrar no garantiza representatividad ni precisión.

### Validaciones (train / test)

Para evaluar un modelo predictivo, dividimos los datos disponibles: train se utiliza para ajustar el modelo y test para medir su desempeño con observaciones que no participaron en el ajuste. Si evaluamos con los mismos datos de entrenamiento, podemos obtener una impresión demasiado optimista. El conjunto test se reserva para la evaluación final; la elección y el ajuste del modelo se realizan dentro de train, por ejemplo con validación cruzada. Esta partición evalúa predicción: no prueba causalidad ni corrige una muestra sesgada. En series de tiempo debemos respetar el orden temporal.

### Estudios en terreno

Visitar hogares, empresas o localidades requiere coordinar rutas, encuestadores, horarios y permisos. Una muestra hace viable ese trabajo y permite supervisar las entrevistas y revisar la calidad de las respuestas. Antes de salir se define a quién se quiere estudiar, el marco de selección y cómo se elegirán las unidades; luego se registran los rechazos y las ausencias. Entrevistar únicamente a quienes resulta más fácil contactar puede dejar fuera a grupos importantes y sesgar las conclusiones.


[Referencias: evaluación predictiva, tidymodels](https://www.tidymodels.org/start/recipes/) y [diseño de encuestas, Banco Mundial](https://www.worldbank.org/en/programs/lsms/publication/capturing-what-matters).











**Consigna:** Calcula cuántas entrevistas financia ese presupuesto.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-09

Ejecutar después de intentar la consigna.


```r
presupuesto <- 100
costo <- 5
capacidad <- floor(presupuesto/costo)
print(capacidad)
```


**Lectura del resultado:** Son 20 entrevistas bajo costos hipotéticos, un ejercicio de planificación con el marco real. Un presupuesto no define por sí solo un buen diseño.

**Error frecuente:** Confundir capacidad de entrevistar con representatividad.

**Comprueba:** ¿Una muestra barata garantiza precisión? No.


<a id="P1-08"></a>
## Lámina 08 · Población, muestra y unidad de observación

**Identificador de enlace:** `P1-08`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · láminas 12–13 · **Modalidad:** Presencial.

**Pregunta:** ¿De qué conjunto seleccionaremos personas?















**Antes de ejecutar:** ¿Una submuestra representa automáticamente a Estados Unidos?

**Consigna:** Define el marco de filas de datos y extrae 12 registros sin reemplazo.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-08

Ejecutar después de intentar la consigna.


```r
set.seed(16201)
N <- nrow(datos)
marco <- seq_len(N)
ids <- sample(marco, size = 12, replace = FALSE)
print(datos[ids, c("wage", "educ")])
```


**Lectura del resultado:** Tratamos la tabla completa como población finita didáctica. Su encuesta original tiene otra población y diseño; nuestro submuestreo no los reproduce.

**Error frecuente:** Llamar población real completa a las 526 observaciones.

**Comprueba:** ¿Cuál es nuestra unidad de observación? La persona registrada.


<a id="P1-10"></a>
## Lámina 09 · Variables, parámetros y estadísticos

**Identificador de enlace:** `P1-10`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 15 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Es lo mismo una variable que un parámetro?















**Antes de ejecutar:** ¿El salario de una persona es un promedio poblacional?

**Consigna:** Clasifica variable, parámetro objetivo y estadístico.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-10

Ejecutar después de intentar la consigna.


```r
print(data.frame(
  concepto = c("Variable", "Parámetro", "Estadístico"),
  ejemplo = c("Salario por hora individual",
              "Media salarial de la población objetivo",
              "Media salarial calculada en una muestra")))
```


**Lectura del resultado:** La variable se observa por persona; el parámetro resume una población; el estadístico depende de la muestra. Las fórmulas vienen después.

**Error frecuente:** Llamar parámetro a cualquier número de una fila.

**Comprueba:** ¿Un estadístico cambia al cambiar la muestra? Generalmente sí.


<a id="P1-11"></a>
## Lámina 10 · Métodos de muestreo probabilístico en R

**Identificador de enlace:** `P1-11`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · láminas 16–17 · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo cambia quién entra según el método?















**Antes de ejecutar:** ¿Estratificar garantiza que ambos grupos definidos tengan participantes?

**Consigna:** Selecciona por cuatro algoritmos y conserva sus índices.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-11

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** El sistemático usa inicio aleatorio; su tamaño puede variar aquí. Los grupos artificiales no sustentan una comparación real de eficiencia. La afijación igual por estrato requeriría ponderar al estimar una media global si difieren los tamaños; aquí solo seleccionamos.

**Error frecuente:** Comparar precisión de diseños con tamaños distintos o usar media estratificada no ponderada como estimador global.

**Comprueba:** ¿El sistemático deja de ser probabilístico porque solo se sortea el inicio? No.


<a id="P1-12"></a>
## Lámina 11 · Muestreo estratificado y por conglomerados

**Identificador de enlace:** `P1-12`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 18 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿En qué se diferencian estratos y conglomerados?















**Antes de ejecutar:** ¿En qué selección aparecen todos los estratos?

**Consigna:** Inspecciona los grupos incluidos por cada selección.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-12

Ejecutar después de intentar la consigna.


```r
print(table(datos$educ16[ids_estrato]))
print(table(grupo_artificial[ids_conglomerado]))
```


**Lectura del resultado:** Estratificar selecciona dentro de todos los estratos; conglomerados selecciona algunos grupos. Homogeneidad y heterogeneidad son criterios didácticos, no definiciones universales.

**Error frecuente:** Presentar grupos artificiales como geografía de la encuesta.

**Comprueba:** ¿Conglomerados puede tener una segunda etapa de muestreo? Sí.


<a id="P1-13"></a>
## Lámina 12 · Muestreo no probabilístico y selección

**Identificador de enlace:** `P1-13`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 19 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué sucede si solo invitamos a quienes tienen al menos 16 años de educación?















**Antes de ejecutar:** ¿Quién queda sin oportunidad de selección?

**Consigna:** Selecciona las primeras 12 filas que cumplen ese criterio.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-13

Ejecutar después de intentar la consigna.


```r
ids_conveniencia <- head(which(datos$educ16), 12)
print(datos[ids_conveniencia, c("wage", "educ")])
```


**Lectura del resultado:** Es una selección por criterio y orden disponible, no una muestra probabilística del conjunto. Una muestra grande no elimina sesgos de cobertura o respuesta, como ilustra Literary Digest en la web.

**Error frecuente:** Generalizar sin supuestos a quienes quedaron fuera.

**Comprueba:** ¿Conocer el criterio equivale a conocer probabilidades de selección aleatoria? No.


<a id="P1-14"></a>
## Lámina 13 · Estadística descriptiva e inferencial

**Identificador de enlace:** `P1-14`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 1 · lámina 20 · **Modalidad:** Presencial.

**Pregunta:** ¿Describimos la tabla o hablamos de una población?















**Antes de ejecutar:** ¿Decir “en estas filas” cambia el alcance?

**Consigna:** Redacta una frase descriptiva y otra inferencial, identificando qué supuesto falta.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P1-14

Ejecutar después de intentar la consigna.


```r
frases <- c("Describo los salarios de las filas observadas",
            "Quiero estimar un promedio de una población definida")
print(frases)
```


**Lectura del resultado:** La segunda frase exige definir población y mecanismo de muestreo. Continúa con la descripción antes de construir intervalos.

**Error frecuente:** Generalizar sin identificar el universo.

**Comprueba:** ¿La inferencia usa solo programación? No, también supuestos.


<a id="P2-01"></a>
## Lámina 01 · Ramas de la estadística

**Identificador de enlace:** `P2-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · lámina 1 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Qué puede decirnos una tabla antes de generalizar?















**Antes de ejecutar:** ¿Un resumen de esta muestra es ya una ley general?

**Consigna:** Selecciona la variable salarial y verifica su tamaño.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-01

Ejecutar después de intentar la consigna.


```r
x <- datos$wage
print(length(x))
```


**Lectura del resultado:** Descriptiva resume x; inferencia requiere un marco adicional. Los datos conservan sus unidades históricas.

**Error frecuente:** Cambiar de población sin avisar.

**Comprueba:** ¿Un histograma es descriptivo? Sí.


<a id="P2-02"></a>
## Lámina 02 · Estadísticos como funciones de los datos

**Identificador de enlace:** `P2-02`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · lámina 2 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué entra y qué sale de un estadístico?















**Antes de ejecutar:** ¿length devuelve un vector de 526 valores?

**Consigna:** Construye un pequeño resumen de tamaño y rango observado.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-02

Ejecutar después de intentar la consigna.


```r
resumen_inicial <- c(n = length(x), minimo = min(x), maximo = max(x))
print(resumen_inicial)
```


**Lectura del resultado:** Cada función transforma el vector en un resultado. Un estadístico es una función de la muestra.

**Error frecuente:** Confundir el vector de datos con su resumen.

**Comprueba:** ¿max(x) conserva todas las observaciones? No.


<a id="P2-03"></a>
## Lámina 03 · Medidas de localización central: media y mediana

**Identificador de enlace:** `P2-03`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · láminas 3–4 · **Modalidad:** Presencial.

**Pregunta:** ¿Media y mediana reaccionan igual a un salario extremo?















**Antes de ejecutar:** ¿Cuál cambiará más al añadir un valor enorme?

**Consigna:** Calcula ambas y compara con una copia que añade un dato artificial.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-03

Ejecutar después de intentar la consigna.


```r
centro <- function(z) c(media = mean(z), mediana = median(z))
print(centro(x))
x_modificado <- c(x, 10*max(x))
print(rbind(original = centro(x), copia_con_extremo = centro(x_modificado)))
ordenados <- sort(x)
n_x <- length(x)
mediana_manual <- if (n_x %% 2 == 1) ordenados[(n_x+1)/2] else
  (ordenados[n_x/2] + ordenados[n_x/2+1])/2
stopifnot(isTRUE(all.equal(mediana_manual, median(x))))
```


**Lectura del resultado:** La media es sensible a extremos. La mediana se obtiene de posiciones centrales; la copia modificada no es una nueva observación real.

**Error frecuente:** Guardar el dato artificial sobre la base original.

**Comprueba:** ¿La mediana exige ordenar conceptualmente los datos? Sí.


<a id="P2-04"></a>
## Lámina 04 · Percentiles y cuartiles

**Identificador de enlace:** `P2-04`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · lámina 5 · **Modalidad:** Presencial.

**Pregunta:** ¿Dónde comienza el cuarto superior?















**Antes de ejecutar:** ¿P50 coincide con la mediana?

**Consigna:** Obtén cuartiles y el percentil 90 con interpolación tipo 7.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-04

Ejecutar después de intentar la consigna.


```r
cuartiles <- quantile(x, probs = c(.25, .5, .75), type = 7)
print(cuartiles)
print(quantile(x, .9, type = 7))
```


**Lectura del resultado:** Los cuartiles delimitan posiciones de la distribución; type=7 especifica la interpolación. Empates y convenciones pueden alterar recuentos exactos.

**Error frecuente:** Interpretar P75 como el 75% del salario máximo.

**Comprueba:** ¿P50 es la mitad del máximo? No.


<a id="P2-05"></a>
## Lámina 05 · Medidas de dispersión: RIQ, varianza y desviación

**Identificador de enlace:** `P2-05`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · láminas 6–7 · **Modalidad:** Presencial.

**Pregunta:** ¿Dos muestras con la misma media pueden ser diferentes?















**Antes de ejecutar:** ¿Varianza y salario tienen las mismas unidades?

**Consigna:** Calcula RIQ, varianza muestral y desviación estándar; verifica manualmente.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-05

Ejecutar después de intentar la consigna.


```r
print(c(RIQ = IQR(x, type = 7), varianza = var(x), desviacion = sd(x)))
s2_manual <- sum((x-mean(x))^2)/(length(x)-1)
stopifnot(isTRUE(all.equal(s2_manual, var(x))))
```


**Lectura del resultado:** La varianza usa unidades al cuadrado y n-1; sd conserva USD por hora. RIQ mide la separación entre P75 y P25.

**Error frecuente:** Confundir desviación estándar con error estándar de la media.

**Comprueba:** ¿sd(x) disminuye necesariamente cuando aumenta n? No.


<a id="P2-06"></a>
## Lámina 06 · Histogramas y elección de intervalos

**Identificador de enlace:** `P2-06`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · lámina 8 · **Modalidad:** Presencial.

**Pregunta:** ¿Cambian los datos cuando cambiamos los intervalos?















**Antes de ejecutar:** ¿Esperas ver la misma apariencia con 5 y 20 cortes sugeridos?

**Consigna:** Dibuja dos histogramas y compara forma y frecuencias.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-06

Ejecutar después de intentar la consigna.


```r
op <- par(mfrow = c(1,2))
for (b in c(5,20)) hist(x, breaks = b, col = "#7DB4B5",
  main = paste("Cortes sugeridos:", b),
  xlab = "Salario por hora (USD de 1976)", ylab = "Frecuencia")
par(op)
```


**Lectura del resultado:** breaks numérico es una sugerencia a R, que elige límites convenientes. La forma visual cambia aunque la muestra sea idéntica.

**Error frecuente:** Confundir barras de frecuencia con la lista de valores individuales.

**Comprueba:** ¿Un histograma con otra anchura prueba otra población? No.


<a id="P2-07"></a>
## Lámina 07 · Gráfico de caja, bigotes y valores atípicos

**Identificador de enlace:** `P2-07`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 2 · láminas 9–10 · **Modalidad:** Presencial.

**Pregunta:** ¿Un punto fuera de los bigotes es un error?















**Antes de ejecutar:** ¿Cuántos posibles atípicos crees que aparecerán?

**Consigna:** Dibuja la caja, extrae sus límites y contrasta bisagras con cuartiles tipo 7.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-07

Ejecutar después de intentar la consigna.


```r
boxplot(x, horizontal = TRUE, col = "#7DB4B5",
  main = "Salarios: posición y dispersión", xlab = "USD por hora de 1976")
bp <- boxplot.stats(x)
print(bp$stats); print(bp$out)
print(quantile(x, c(.25,.5,.75), type = 7))
```


**Lectura del resultado:** R usa bisagras para la caja, que no siempre coinciden con quantile(type=7). Los bigotes terminan en observaciones dentro de 1,5 veces el rango entre bisagras; las cercas no son necesariamente datos. Un atípico requiere investigar, no borrar.

**Error frecuente:** Eliminar automáticamente puntos extremos.

**Comprueba:** ¿El bigote siempre termina justo en q3+1,5*RIQ? No.


<a id="P3-01"></a>
## Lámina 01 · Inferencia y población empírica de referencia

**Identificador de enlace:** `P3-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 1 · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo podemos evaluar un método si normalmente no conocemos la verdad?















**Antes de ejecutar:** ¿Qué cambia si tratamos toda la tabla como una distribución conocida?

**Consigna:** Define la distribución empírica de salarios y sus momentos poblacionales.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-01

Ejecutar después de intentar la consigna.


```r
poblacion <- datos$wage
mu <- mean(poblacion)
sigma2 <- mean((poblacion-mu)^2)
sigma <- sqrt(sigma2)
print(c(mu = mu, sigma = sigma, N = length(poblacion)))
```


**Lectura del resultado:** Cada fila tiene probabilidad 1/N en esta distribución didáctica. Usamos denominador N; no afirmamos conocer la varianza salarial de todo Estados Unidos.

**Error frecuente:** Llamar sigma a sd de la muestra sin justificar una población conocida.

**Comprueba:** ¿Esta media es un parámetro de nuestra distribución didáctica? Sí.


<a id="P3-02"></a>
## Lámina 02 · Intervalos de confianza e incertidumbre

**Identificador de enlace:** `P3-02`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 2 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué aporta un intervalo frente a un valor único?















**Antes de ejecutar:** ¿Un intervalo ya calculado tiene parámetro aleatorio?

**Consigna:** Escribe qué cambia al repetir el muestreo.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-02

Ejecutar después de intentar la consigna.


```r
print(c("El parámetro didáctico permanece fijo",
        "La muestra y sus límites cambian",
        "La confianza describe el procedimiento"))
```


**Lectura del resultado:** Como en los aros y la estaca de cátedra, mu permanece fijo y los intervalos cambian. La cobertura es una propiedad de repetición.

**Error frecuente:** Decir que el 95% de las observaciones está dentro del IC de la media.

**Comprueba:** ¿Un IC de media es un intervalo de salarios individuales? No.


<a id="P3-03"></a>
## Lámina 03 · Teorema central del límite: simulación en R

**Identificador de enlace:** `P3-03`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 3 · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo se distribuye el promedio al repetir muestras?















**Antes de ejecutar:** ¿Las medias de n=100 serán menos dispersas que las de n=5?

**Consigna:** Extrae 1.000 muestras por tamaño, independientes y con reemplazo.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-03

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** La comparación usa muestras de una población empírica conocida, no remuestreo de una muestra para estimar un parámetro desconocido. El TCL aproxima la forma de la distribución de medias.

**Error frecuente:** Confundir salarios individuales con medias muestrales.

**Comprueba:** ¿sigma/sqrt(n) es la desviación de salarios? No, de la media.


<a id="P3-04"></a>
## Lámina 04 · Supuestos del teorema central del límite

**Identificador de enlace:** `P3-04`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 4 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿n=30 garantiza normalidad en cualquier caso?















**Antes de ejecutar:** ¿La asimetría afecta la rapidez de aproximación?

**Consigna:** Comprueba que los datos utilizados son finitos y revisa el mecanismo de muestreo.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-04

Ejecutar después de intentar la consigna.


```r
stopifnot(all(is.finite(poblacion)), sigma2 > 0)
print(c(media_finita = is.finite(mu), varianza_finita = is.finite(sigma2)))
```


**Lectura del resultado:** Con reemplazo cada extracción tiene la misma distribución y es independiente. Los umbrales de tamaño son orientativos. Si la población fuera normal, su media muestral sería normal para cualquier n.

**Error frecuente:** Tratar 30, 50 o 100 como garantías universales.

**Comprueba:** ¿El ciclo por sí solo demuestra independencia en la encuesta original? No.


<a id="P3-05"></a>
## Lámina 05 · Intervalo para una media: ejemplo salarial

**Identificador de enlace:** `P3-05`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 5–7 · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo estimamos mu con una muestra de 36 salarios?















**Antes de ejecutar:** ¿El resultado quedará centrado en mu o en la media de la muestra?

**Consigna:** Extrae 36 observaciones y calcula el intervalo normal de 95% con sigma conocida didáctica.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-05

Ejecutar después de intentar la consigna.


```r
set.seed(16204)
n_ic <- 36L
muestra_ic <- sample(poblacion, n_ic, replace = TRUE)
xbarra <- mean(muestra_ic)
z95 <- qnorm(.975)
se <- sigma/sqrt(n_ic)
ic95 <- xbarra + c(-1,1)*z95*se
print(c(estimacion = xbarra, error_estandar = se,
        inferior = ic95[1], superior = ic95[2], mu_didactica = mu))
```


**Lectura del resultado:** Es un ejercicio propio con wage1, análogo al ejemplo de ventas; no reproduce su media 200 ni su sigma 60. La cobertura normal aquí es aproximada.

**Error frecuente:** Atribuir los números de ventas del sitio a la base salarial.

**Comprueba:** ¿Cuál es el centro del intervalo? xbarra.


<a id="P3-06"></a>
## Lámina 06 · Componentes del intervalo de confianza de 95%

**Identificador de enlace:** `P3-06`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 8 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Qué papel tiene cada pieza?















**Antes de ejecutar:** ¿Qué ocurre al duplicar sigma y conservar lo demás?

**Consigna:** Separa estimación, valor crítico, error estándar y margen.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-06

Ejecutar después de intentar la consigna.


```r
margen95 <- z95*se
print(c(estimacion = xbarra, z = z95, se = se, margen = margen95))
stopifnot(isTRUE(all.equal(diff(ic95), 2*margen95)))
```


**Lectura del resultado:** El margen es z por error estándar; la longitud total es el doble del margen.

**Error frecuente:** Usar el margen como si fuera longitud total.

**Comprueba:** ¿Duplicar sigma duplica el margen? Sí.


<a id="P3-07"></a>
## Lámina 07 · Intervalos con distintos niveles de confianza

**Identificador de enlace:** `P3-07`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 9–10 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué cambia al pasar a 99%?















**Antes de ejecutar:** ¿El centro debería moverse?

**Consigna:** Calcula 90%, 95% y 99% para la misma muestra.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-07

Ejecutar después de intentar la consigna.


```r
niveles <- c(.90,.95,.99)
z <- qnorm((1+niveles)/2)
limites <- cbind(inferior = xbarra-z*se, superior = xbarra+z*se)
rownames(limites) <- paste0(100*niveles, "%")
print(limites)
```


**Lectura del resultado:** Se utiliza el cuantil superior positivo; el centro se conserva. qnorm evita inconsistencias por redondeo de 2,57 o 2,58.

**Error frecuente:** Extraer otra muestra y atribuir todo cambio a la confianza.

**Comprueba:** ¿Qué intervalo es más ancho? El de 99%.


<a id="P3-08"></a>
## Lámina 08 · Comparación gráfica de intervalos de confianza

**Identificador de enlace:** `P3-08`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 11 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Podemos comparar los intervalos de un vistazo?















**Antes de ejecutar:** ¿Cuál abarcará a los otros?

**Consigna:** Representa los límites en una misma recta salarial.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-08

Ejecutar después de intentar la consigna.


```r
plot(range(limites), c(1,3), type = "n", yaxt = "n",
     xlab = "Media salarial (USD/h)", ylab = "Confianza",
     main = "La misma muestra, distinta confianza")
axis(2, at = 1:3, labels = rownames(limites))
segments(limites[,1], 1:3, limites[,2], 1:3, lwd = 3, col = "#35618A")
points(rep(xbarra,3), 1:3, pch = 19)
```


**Lectura del resultado:** El intervalo mayor ofrece más cobertura bajo el modelo a costa de anchura.

**Error frecuente:** Confundir intervalo más ancho con mejor precisión.

**Comprueba:** ¿El centro de los tres es idéntico? Sí.


<a id="P3-09"></a>
## Lámina 09 · Cobertura, confianza y precisión

**Identificador de enlace:** `P3-09`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 12–13 · **Modalidad:** Presencial.

**Pregunta:** ¿Cuántos intervalos capturan la media conocida?















**Antes de ejecutar:** ¿Se obtendrán exactamente 950 aciertos de 1.000?

**Consigna:** Repite 1.000 veces y visualiza los primeros 100 intervalos.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-09

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** La proporción observada fluctúa y la aproximación normal puede afectar cobertura. Cuadruplicar n reduce el margen a la mitad manteniendo confianza y sigma.

**Error frecuente:** Prometer exactamente 95 aciertos en cada 100 muestras.

**Comprueba:** ¿Un intervalo fallido demuestra que el código está mal? No.


<a id="P3-10"></a>
## Lámina 10 · Tamaño muestral para estimar una media

**Identificador de enlace:** `P3-10`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 14 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Cuántas observaciones para un margen de 0,5 USD/h?















**Antes de ejecutar:** ¿Reducir el margen a la mitad duplicará n?

**Consigna:** Despeja n y verifica el margen obtenido después de redondear.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-10

Ejecutar después de intentar la consigna.


```r
E_media <- .5
n_necesario <- ceiling((qnorm(.975)*sigma/E_media)^2)
print(c(n = n_necesario, margen = qnorm(.975)*sigma/sqrt(n_necesario)))
```


**Lectura del resultado:** n crece con el inverso del margen al cuadrado. El muestreo con reemplazo puede requerir más extracciones que filas únicas. No es un plan validado para una encuesta nacional.

**Error frecuente:** Redondear hacia abajo.

**Comprueba:** ¿Reducir E a la mitad multiplica n por cuatro antes del redondeo? Sí.


<a id="P3-11"></a>
## Lámina 11 · Intervalos de confianza para proporciones

**Identificador de enlace:** `P3-11`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 15–19 · **Modalidad:** Presencial.

**Pregunta:** ¿Qué fracción tiene al menos 16 años de educación?















**Antes de ejecutar:** ¿Puede una proporción ser mayor que 1?

**Consigna:** Define el indicador, extrae n=200 y calcula el IC normal aproximado si se cumplen las condiciones.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-11

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** El indicador es derivado, con definición explícita. Para aproximación poblacional se consideran np y n(1-p); los conteos observados sirven de diagnóstico práctico. Este intervalo de Wald puede funcionar mal cerca de 0 o 1; aquí no se amplían métodos.

**Error frecuente:** Confundir “éxito” estadístico con juicio de valor o título universitario.

**Comprueba:** ¿Un 1 representa exactamente qué? educ >= 16.


<a id="P3-12"></a>
## Lámina 12 · Proporciones: comparación con una referencia

**Identificador de enlace:** `P3-12`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 20–21 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿La proporción de referencia 0,20 queda en el intervalo?















**Antes de ejecutar:** Predice mirando los límites anteriores.

**Consigna:** Comprueba inclusión y escribe una conclusión bajo el modelo didáctico.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-12

Ejecutar después de intentar la consigna.


```r
referencia <- .20
compatible <- ic_p[1] <= referencia && referencia <= ic_p[2]
print(c(referencia = referencia, dentro_del_IC = compatible))
```


**Lectura del resultado:** Si queda fuera, hay evidencia de diferencia bajo los supuestos; si queda dentro, no se ha demostrado igualdad. La referencia es hipotética, no una afirmación publicada sobre Estados Unidos.

**Error frecuente:** Convertir ausencia de evidencia en prueba de igualdad.

**Comprueba:** ¿Que quede dentro prueba p=0,20? No.


<a id="P3-13"></a>
## Lámina 13 · Tamaño muestral para estimar una proporción

**Identificador de enlace:** `P3-13`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 22 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Qué pasa si no tenemos estimación previa?















**Antes de ejecutar:** ¿p=0,5 maximiza p(1-p)?

**Consigna:** Compara el plan con p piloto y el conservador para margen 0,03.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-13

Ejecutar después de intentar la consigna.


```r
E_p <- .03
print(c(con_piloto = ceiling(qnorm(.975)^2*p_hat*(1-p_hat)/E_p^2),
        conservador = ceiling(qnorm(.975)^2*.25/E_p^2)))
```


**Lectura del resultado:** Usar 0,5 maximiza la varianza Bernoulli. Una proporción piloto imprecisa puede producir un plan optimista.

**Error frecuente:** Usar p_hat=0 como garantía de tamaño cero suficiente.

**Comprueba:** ¿El plan conservador depende de observar éxitos en el piloto? No.


<a id="P3-14"></a>
## Lámina 14 · Aplicación: longitud y margen de error

**Identificador de enlace:** `P3-14`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 23–24 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Cuántas extracciones para longitud total máxima 0,05?















**Antes de ejecutar:** ¿El margen será 0,05 o 0,025?

**Consigna:** Usa una muestra piloto de 30 indicadores educativos y compara con el caso conservador.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-14

Ejecutar después de intentar la consigna.


```r
set.seed(16207)
piloto <- sample(indicador, 30, replace = TRUE)
p_estrella <- mean(piloto)
longitud_max <- .05
E_plan <- longitud_max/2
n_plan <- ceiling(qnorm(.975)^2*p_estrella*(1-p_estrella)/E_plan^2)
n_conservador <- ceiling(qnorm(.975)^2*.25/E_plan^2)
print(c(piloto = p_estrella, margen = E_plan, n_piloto = n_plan,
        n_conservador = n_conservador))
```


**Lectura del resultado:** Es un caso propio análogo a chips; el n del piloto es una planificación aproximada, no garantía de longitud real para toda muestra futura con varianza estimada.

**Error frecuente:** Afirmar que el resultado debe ser 711 porque ese es el ejemplo de chips.

**Comprueba:** ¿De dónde sale E=0,025? De dividir la longitud total por dos.


<a id="P3-15"></a>
## Lámina 15 · Comparación de medias entre dos poblaciones

**Identificador de enlace:** `P3-15`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · lámina 25 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Cómo cambia el salario medio entre umbrales educativos?















**Antes de ejecutar:** ¿Qué signo esperas para alta educación menos el resto?

**Consigna:** Define las dos poblaciones empíricas sin mezclarlas.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-15

Ejecutar después de intentar la consigna.


```r
pob_alta <- datos$wage[datos$educ >= 16]
pob_resto <- datos$wage[datos$educ < 16]
stopifnot(length(pob_alta) > 1, length(pob_resto) > 1)
print(c(N_alta = length(pob_alta), N_resto = length(pob_resto)))
```


**Lectura del resultado:** Los grupos son dos distribuciones empíricas para una comparación didáctica. No son carreras universitarias ni grupos aleatorizados.

**Error frecuente:** Cambiar la definición de los grupos a mitad del ejercicio.

**Comprueba:** ¿Los grupos se superponen? No.


<a id="P3-16"></a>
## Lámina 16 · Diferencia de medias: parámetro e interpretación

**Identificador de enlace:** `P3-16`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 26–27 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Qué significa que el intervalo incluya cero?















**Antes de ejecutar:** ¿Qué pasa con el signo si invertimos el orden?

**Consigna:** Define delta como media de alta educación menos media del resto.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-16

Ejecutar después de intentar la consigna.


```r
mu_alta <- mean(pob_alta); mu_resto <- mean(pob_resto)
delta <- mu_alta-mu_resto
print(c(delta_didactica = delta))
```


**Lectura del resultado:** Un intervalo que excluye cero aporta evidencia de diferencia bajo el procedimiento. Invertir el orden invierte el signo y los extremos correspondientes.

**Error frecuente:** Interpretar incluir cero como demostrar igualdad.

**Comprueba:** ¿Excluir cero prueba causalidad? No.


<a id="P3-17"></a>
## Lámina 17 · Diferencia de medias con varianzas conocidas

**Identificador de enlace:** `P3-17`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 28–31 · **Modalidad:** Ampliación autónoma.

**Pregunta:** ¿Cómo se combina la incertidumbre de muestras independientes?















**Antes de ejecutar:** ¿Se restan o se suman las varianzas?

**Consigna:** Extrae 144 y 121 salarios con reemplazo de cada grupo; calcula el error estándar de la diferencia.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-17

Ejecutar después de intentar la consigna.


```r
var_alta <- mean((pob_alta-mu_alta)^2)
var_resto <- mean((pob_resto-mu_resto)^2)
set.seed(16208)
n_a <- 144L; n_b <- 121L
m_a <- sample(pob_alta, n_a, replace = TRUE)
m_b <- sample(pob_resto, n_b, replace = TRUE)
diferencia <- mean(m_a)-mean(m_b)
se_diferencia <- sqrt(var_alta/n_a+var_resto/n_b)
print(c(estimacion = diferencia, error_estandar = se_diferencia))
```


**Lectura del resultado:** Las varianzas se suman por independencia aunque las medias se resten. Los momentos conocidos son de las distribuciones didácticas con denominador N de cada grupo.

**Error frecuente:** Usar var(m_a) y llamarla varianza poblacional conocida.

**Comprueba:** ¿Usar una sola muestra compartida garantizaría independencia? No.


<a id="P3-18"></a>
## Lámina 18 · Diferencia de medias: intervalo y conclusión

**Identificador de enlace:** `P3-18`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · láminas 32–34 · **Modalidad:** Presencial.

**Pregunta:** ¿La diferencia es compatible con cero?















**Antes de ejecutar:** ¿Tu conclusión cambia si hablas de causa?

**Consigna:** Calcula límites y escribe dos frases: resultado e interpretación limitada.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-18

Ejecutar después de intentar la consigna.


```r
ic_d <- diferencia+c(-1,1)*qnorm(.975)*se_diferencia
print(c(inferior = ic_d[1], superior = ic_d[2], delta_didactica = delta,
        contiene_cero = ic_d[1] <= 0 && ic_d[2] >= 0))
plot(range(c(ic_d,0)), c(0,1), type = "n", yaxt = "n", ylab = "",
     xlab = "Diferencia de medias (USD/h de 1976)", main = "Alta educación menos resto")
segments(ic_d[1],.5,ic_d[2],.5,lwd = 3,col = "#35618A")
points(diferencia,.5,pch = 19); abline(v = 0,lty = 2)
```


**Lectura del resultado:** Redacta según la salida efectiva: el IC incluye o excluye cero. El resultado compara medias de las poblaciones didácticas bajo muestreo independiente; no estima el efecto causal de educarse ni una brecha actual chilena.

**Error frecuente:** Copiar la conclusión sin mirar los límites obtenidos.

**Comprueba:** ¿Controlamos habilidad y contexto familiar? No.


## CIERRE · Autoevaluación

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


## Matriz de correspondencia

La guía y el notebook se generan desde el mismo contenido: todas las consignas, soluciones y celdas R de actividades coinciden. Los IDs son estables. Los enunciados son el código inicial de trabajo: cada pareja escribe su intento en una celda R nueva antes de consultar la celda de solución; no hay ejercicios deliberadamente rotos que impidan ejecutar el notebook completo.

| Actividad | Referencia web | Sección y celda de código del notebook | Modalidad |
|---|---|---|---|
| NIV-01 | Nivelación | `niv-01-consigna` / `niv-01-r` | Presencial |
| NIV-ASIG | Nivelación | `niv-asig-consigna` / `niv-asig-r` | Presencial |
| NIV-03 | Nivelación | `niv-03-consigna` / `niv-03-r` | Presencial |
| NIV-06 | Nivelación | `niv-06-consigna` / `niv-06-r` | Presencial |
| NIV-FOR | Nivelación | `niv-for-consigna` / `niv-for-r` | Presencial |
| NIV-05 | Nivelación | `niv-05-consigna` / `niv-05-r` | Presencial |
| NIV-02 | Nivelación | `niv-02-consigna` / `niv-02-r` | Presencial |
| NIV-07 | Nivelación | `niv-07-consigna` / `niv-07-r` | Presencial |
| NIV-08 | Nivelación | `niv-08-consigna` / `niv-08-r` | Presencial |
| NIV-NOTEBOOK | Nivelación | `niv-notebook-consigna` | Presencial |
| P1-01 | Parte 1 · lámina 1 | `p1-01-consigna` / `p1-01-r` | Presencial |
| P1-02 | Parte 1 · lámina 2 | `p1-02-consigna` / `p1-02-r` | Presencial |
| P1-04 | Parte 1 · lámina 4 | `p1-04-consigna` / `p1-04-r` | Presencial |
| P1-05 | Parte 1 · láminas 5–6 | `p1-05-consigna` / `p1-05-r` | Presencial |
| P1-06 | Parte 1 · lámina 7 | `p1-06-consigna` / `p1-06-r` | Ampliación autónoma |
| P1-07 | Parte 1 · láminas 8–11 | `p1-07-consigna` / `p1-07-r` | Presencial |
| P1-09 | Parte 1 · lámina 14 | `p1-09-consigna` / `p1-09-r` | Ampliación autónoma |
| P1-08 | Parte 1 · láminas 12–13 | `p1-08-consigna` / `p1-08-r` | Presencial |
| P1-10 | Parte 1 · lámina 15 | `p1-10-consigna` / `p1-10-r` | Ampliación autónoma |
| P1-11 | Parte 1 · láminas 16–17 | `p1-11-consigna` / `p1-11-r` | Presencial |
| P1-12 | Parte 1 · lámina 18 | `p1-12-consigna` / `p1-12-r` | Ampliación autónoma |
| P1-13 | Parte 1 · lámina 19 | `p1-13-consigna` / `p1-13-r` | Presencial |
| P1-14 | Parte 1 · lámina 20 | `p1-14-consigna` / `p1-14-r` | Presencial |
| P2-01 | Parte 2 · lámina 1 | `p2-01-consigna` / `p2-01-r` | Ampliación autónoma |
| P2-02 | Parte 2 · lámina 2 | `p2-02-consigna` / `p2-02-r` | Presencial |
| P2-03 | Parte 2 · láminas 3–4 | `p2-03-consigna` / `p2-03-r` | Presencial |
| P2-04 | Parte 2 · lámina 5 | `p2-04-consigna` / `p2-04-r` | Presencial |
| P2-05 | Parte 2 · láminas 6–7 | `p2-05-consigna` / `p2-05-r` | Presencial |
| P2-06 | Parte 2 · lámina 8 | `p2-06-consigna` / `p2-06-r` | Presencial |
| P2-07 | Parte 2 · láminas 9–10 | `p2-07-consigna` / `p2-07-r` | Presencial |
| P3-01 | Parte 3 · lámina 1 | `p3-01-consigna` / `p3-01-r` | Presencial |
| P3-02 | Parte 3 · lámina 2 | `p3-02-consigna` / `p3-02-r` | Presencial |
| P3-03 | Parte 3 · lámina 3 | `p3-03-consigna` / `p3-03-r` | Presencial |
| P3-04 | Parte 3 · lámina 4 | `p3-04-consigna` / `p3-04-r` | Ampliación autónoma |
| P3-05 | Parte 3 · láminas 5–7 | `p3-05-consigna` / `p3-05-r` | Presencial |
| P3-06 | Parte 3 · lámina 8 | `p3-06-consigna` / `p3-06-r` | Ampliación autónoma |
| P3-07 | Parte 3 · láminas 9–10 | `p3-07-consigna` / `p3-07-r` | Presencial |
| P3-08 | Parte 3 · lámina 11 | `p3-08-consigna` / `p3-08-r` | Ampliación autónoma |
| P3-09 | Parte 3 · láminas 12–13 | `p3-09-consigna` / `p3-09-r` | Presencial |
| P3-10 | Parte 3 · lámina 14 | `p3-10-consigna` / `p3-10-r` | Ampliación autónoma |
| P3-11 | Parte 3 · láminas 15–19 | `p3-11-consigna` / `p3-11-r` | Presencial |
| P3-12 | Parte 3 · láminas 20–21 | `p3-12-consigna` / `p3-12-r` | Ampliación autónoma |
| P3-13 | Parte 3 · lámina 22 | `p3-13-consigna` / `p3-13-r` | Ampliación autónoma |
| P3-14 | Parte 3 · láminas 23–24 | `p3-14-consigna` / `p3-14-r` | Ampliación autónoma |
| P3-15 | Parte 3 · lámina 25 | `p3-15-consigna` / `p3-15-r` | Ampliación autónoma |
| P3-16 | Parte 3 · láminas 26–27 | `p3-16-consigna` / `p3-16-r` | Ampliación autónoma |
| P3-17 | Parte 3 · láminas 28–31 | `p3-17-consigna` / `p3-17-r` | Ampliación autónoma |
| P3-18 | Parte 3 · láminas 32–34 | `p3-18-consigna` / `p3-18-r` | Presencial |

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

**Cobertura documental:** 48/48 láminas (10 de nivelación, 13 introductorias, 7 descriptivas y 18 inferenciales); 64/64 láminas de contenido del curso; 15/15 categorías de requisitos anteriores. Esto no equivale a una certificación de ejecución ni a 48 láminas resueltas en clase.
