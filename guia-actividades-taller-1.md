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


<a id="P1-07"></a>
## Lámina 01 · Tipos y estructura de los datos económicos

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


<a id="P1-01"></a>
## Lámina 02 · Introducción a la econometría y a los datos

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
## Lámina 03 · Exploración gráfica de los datos

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
## Lámina 04 · Correlación, causalidad y factores no observados

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
## Lámina 05 · Educación y salarios: alcances de la comparación

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
## Lámina 06 · Comparar salarios con boxplots

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


<a id="P1-09"></a>
## Lámina 07 · Razones para trabajar con muestras

¿Para qué trabajar con una parte de los datos?

### Presupuesto

Observar a toda la población puede exigir más dinero, tiempo y personal de los disponibles. Una muestra permite planificar la recolección y concentrar recursos en mediciones de calidad. Por ejemplo, con un presupuesto de 100 unidades y un costo de 5 por entrevista, podemos financiar 20 entrevistas. El tamaño y la selección deben responder al objetivo del estudio: ahorrar no garantiza representatividad ni precisión.

### Validaciones (train / test)

Para evaluar un modelo predictivo, dividimos los datos disponibles: train se utiliza para ajustar el modelo y test para medir su desempeño con observaciones que no participaron en el ajuste. Si evaluamos con los mismos datos de entrenamiento, podemos obtener una impresión demasiado optimista. El conjunto test se reserva para la evaluación final; la elección y el ajuste del modelo se realizan dentro de train, por ejemplo con validación cruzada. Esta partición evalúa predicción: no prueba causalidad ni corrige una muestra sesgada. En series de tiempo debemos respetar el orden temporal.

### Estudios en terreno

Visitar hogares, empresas o localidades requiere coordinar rutas, encuestadores, horarios y permisos. Una muestra hace viable ese trabajo y permite supervisar las entrevistas y revisar la calidad de las respuestas. Antes de salir se define a quién se quiere estudiar, el marco de selección y cómo se elegirán las unidades; luego se registran los rechazos y las ausencias. Entrevistar únicamente a quienes resulta más fácil contactar puede dejar fuera a grupos importantes y sesgar las conclusiones.

Referencias: [tidymodels](https://www.tidymodels.org/start/recipes/) y [Banco Mundial](https://www.worldbank.org/en/programs/lsms/publication/capturing-what-matters).

**Comprueba:** ¿Una muestra barata garantiza precisión? No.


<a id="P1-08"></a>
## Lámina 08 · Cuatro técnicas de muestreo en R con wage1

Usamos wage1, incluida en el paquete wooldridge. Ejecuta la preparación una vez y después los cuatro ejemplos en orden. Las 526 personas de la base forman nuestro marco didáctico; estas selecciones no reproducen el diseño original de la CPS ni permiten afirmar representatividad nacional.

[Tipos de muestreo en la clase de Sebastián](https://hizocar.github.io/econometria-usm/clases/clase1/#muestreo-aleatorio).

### Preparación


```r
# Ejecuta esta preparación una vez antes de los cuatro ejemplos.
if (!requireNamespace("wooldridge", quietly = TRUE)) {
  install.packages("wooldridge", repos = "https://cloud.r-project.org/")
}
datos <- as.data.frame(wooldridge::wage1)
datos$educ16 <- datos$educ >= 16
N <- nrow(datos)
marco <- 1:N
set.seed(36)
```


### 1. Muestreo aleatorio simple

Sorteamos 24 personas sin reemplazo. Cada fila de la base tiene la misma probabilidad de ser incluida.


```r
ids_simple <- sample(marco, size = 24, replace = FALSE)
muestra_simple <- datos[ids_simple, ]
print(muestra_simple[c("wage", "educ", "female")])
```


Se obtienen 24 filas distintas. set.seed() permite repetir la selección cuando se ejecuta la preparación y luego los ejemplos en el mismo orden.


### 2. Muestreo aleatorio sistemático

Conservamos el orden de las filas, sorteamos el inicio entre 1 y 20 y elegimos después una de cada 20 personas.


```r
k <- 20
inicio <- sample(1:k, size = 1)
ids_sistema <- seq(inicio, N, by = k)
muestra_sistematica <- datos[ids_sistema, ]
print(muestra_sistematica[c("wage", "educ", "female")])
```


El tamaño será 26 o 27 personas. Con este inicio aleatorio, cada fila tiene probabilidad 1/20 de entrar antes de realizar el sorteo. Por eso es un diseño probabilístico, aunque no permite todas las combinaciones de una muestra aleatoria simple. Una vez fijado el inicio, las demás posiciones quedan determinadas. El orden de la lista y posibles patrones periódicos importan.


### 3. Muestreo aleatorio estratificado

Dividimos la base en dos estratos de educación: menos de 16 años y 16 años o más. Sorteamos 12 personas dentro de cada uno.


```r
estrato_menos16 <- which(!datos$educ16)
estrato_16omas <- which(datos$educ16)
ids_estrato <- c(sample(estrato_menos16, size = 12),
                 sample(estrato_16omas, size = 12))
muestra_estratificada <- datos[ids_estrato, ]
print(table(muestra_estratificada$educ16))
print(muestra_estratificada[c("wage", "educ")])
```


Participan ambos estratos: 12 personas de cada uno. Como sus tamaños en la base son distintos (427 y 99), seleccionar la misma cantidad no conserva sus proporciones. Para estimar una media global con este diseño habría que ponderar por el tamaño de cada estrato.


### 4. Muestreo por conglomerados (cluster)

Creamos 12 grupos artificiales y realizamos un muestreo de dos etapas: primero sorteamos dos grupos y luego sorteamos 12 personas dentro de cada grupo elegido. Los grupos son didácticos y no representan barrios o escuelas reales de la CPS.


```r
grupo_artificial <- rep(1:12, length.out = N)
elegidos <- sample(unique(grupo_artificial), size = 2)

# Segunda etapa: seleccionar personas dentro de los grupos elegidos.
personas_grupo1 <- which(grupo_artificial == elegidos[1])
personas_grupo2 <- which(grupo_artificial == elegidos[2])
ids_conglomerado <- c(sample(personas_grupo1, size = 12),
                     sample(personas_grupo2, size = 12))
muestra_conglomerados <- datos[ids_conglomerado, ]
print(elegidos)
print(table(grupo_artificial[ids_conglomerado]))
print(muestra_conglomerados[c("wage", "educ", "female")])
```


La muestra tiene 24 personas: 12 de cada uno de los dos grupos sorteados. En el estratificado entran personas de todos los estratos; aquí solo de los conglomerados elegidos. Si incluyéramos a todas las personas de esos grupos, sería un diseño de una etapa. Los grupos artificiales permiten ilustrar el algoritmo, no evaluar la eficiencia de un diseño geográfico real.


<a id="P2-01"></a>
## Lámina 01 · Salarios: promedio, mediana, moda y percentiles

**Identificador de enlace:** `P2-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Ayudantía · Localización central y percentiles de Sebastián · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo se distribuye el salario total y por estado civil?

















**Consigna:** Compara el total, no casados (married = 0) y casados (married = 1). Obtén promedio, mediana, moda y percentiles 24, 50 y 75. married = 0 no identifica exclusivamente a personas solteras.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-01

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** La mediana coincide con P50. La moda puede contener varios valores empatados. Los percentiles usan type = 7. Los salarios son USD por hora de 1976 y la comparación entre estados civiles es descriptiva, no causal.

**Comprueba:** ¿P50 coincide con la mediana? Sí. ¿married = 0 significa exclusivamente soltero? No.


<a id="P2-02"></a>
## Lámina 02 · Dispersión: de la nube compacta a la nube amplia

**Identificador de enlace:** `P2-02`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Ayudantía · Dispersión, histograma y boxplot de Sebastián · **Modalidad:** Presencial.

**Pregunta:** ¿Cómo cambia una nube cuando aumenta su varianza?

















**Consigna:** Compara varianza, desviación estándar, rango, RIQ y CV del salario total y por estado civil. Después usa la nube artificial para aumentar la dispersión sin mover la media.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P2-02

Ejecutar después de intentar la consigna.


```r
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
```


**Lectura del resultado:** Varianza = desviación estándar al cuadrado. La varianza usa n − 1 y unidades al cuadrado; la desviación mantiene las unidades originales. RIQ = P75 − P25. La altura de la nube solo separa puntos; la variación representada es horizontal.


<a id="P3-01"></a>
## Lámina 01 · Inferir, TCL y supuestos

**Identificador de enlace:** `P3-01`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · teorema-central-del-limite · **Modalidad:** Presencial.

**Pregunta:** Inferir, TCL y supuestos

















**Consigna:** Inferir utiliza una muestra para estudiar una población y requiere supuestos. El TCL aproxima la distribución de las medias por una normal de media μ y varianza σ²/n. Aquí wage1 se trata como una población empírica didáctica conocida; no como toda la población de Estados Unidos. La figura es una curva normal de referencia, no una distribución de salarios individuales. Las observaciones deben ser independientes e idénticamente distribuidas, con media y varianza finitas; las reglas n=30/50/100 son orientativas, no garantías.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-01

Ejecutar después de intentar la consigna.


```r
if (file.exists("datos/wage1.csv")) {
  base <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  base <- as.data.frame(wooldridge::wage1)
}
poblacion <- base$wage
mu <- mean(poblacion)
sigma <- sqrt(mean((poblacion - mu)^2))  # Momento poblacional: divisor N.
n <- 50
set.seed(40)
medias <- replicate(1000, mean(sample(poblacion, n, replace = TRUE)))
hist(medias, probability = TRUE, col = "#0160A0", border = "white",
     xlab = "Promedio salarial (USD/h de 1976)", main = paste("Medias con n =", n))
curve(dnorm(x, mean = mu, sd = sigma / sqrt(n)), add = TRUE,
      col = "#E12523", lwd = 2)
print(c(media_poblacional = mu, varianza_media = sigma^2 / n,
        error_estandar = sigma / sqrt(n)))
```


**Lectura del resultado:** Inferir utiliza una muestra para estudiar una población y requiere supuestos. El TCL aproxima la distribución de las medias por una normal de media μ y varianza σ²/n. Aquí wage1 se trata como una población empírica didáctica conocida; no como toda la población de Estados Unidos. La figura es una curva normal de referencia, no una distribución de salarios individuales. Las observaciones deben ser independientes e idénticamente distribuidas, con media y varianza finitas; las reglas n=30/50/100 son orientativas, no garantías.


<a id="P3-05"></a>
## Lámina 02 · Intervalo de confianza para una media

**Identificador de enlace:** `P3-05`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · ic-ejemplo1 · **Modalidad:** Presencial.

**Pregunta:** Intervalo de confianza para una media

















**Consigna:** Ejemplo: ventas mensuales, x̄=200, σ=60 conocida y n=36. El intervalo es x̄ ± z × σ/√n. Para ilustrar su interpretación repetimos 20 medias de una población normal con μ=200: el parámetro permanece fijo y los intervalos cambian. La cobertura de estas 20 repeticiones puede diferir del nivel nominal. Un IC de la media no contiene necesariamente ese porcentaje de observaciones individuales.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-05

Ejecutar después de intentar la consigna.


```r
xbarra <- 200
sigma <- 60
n <- 36
confianza <- 0.95
z <- qnorm((1 + confianza) / 2)
se <- sigma / sqrt(n)
ic <- xbarra + c(-1, 1) * z * se
print(c(estimacion = xbarra, margen = z * se, inferior = ic[1], superior = ic[2]))

# Ilustración normal con mu = 200 fijo; no es un parámetro estimado de wage1.
mu_demo <- 200
z_demo <- c(-0.271313, -1.056361, 0.197561, 0.002057, 0.870213, 2.519121, -0.91341, -0.254936, 0.322156, 0.578074, 1.506138, 0.186028, -0.36742, 0.614709, -0.81785, 0.118748, -0.002822, 1.631639, -0.215701, -1.137394)
medias_demo <- mu_demo + z_demo * se
inferior <- medias_demo - z * se
superior <- medias_demo + z * se
cubre <- inferior <= mu_demo & superior >= mu_demo
plot(range(c(inferior, superior, mu_demo)), c(1, 20), type = "n",
     xlab = "Media de ventas", ylab = "Repetición")
segments(inferior, 1:20, superior, 1:20,
         col = ifelse(cubre, "#0160A0", "#E12523"), lwd = 2)
abline(v = mu_demo, lty = 2)
print(mean(cubre))
```


**Lectura del resultado:** Ejemplo: ventas mensuales, x̄=200, σ=60 conocida y n=36. El intervalo es x̄ ± z × σ/√n. Para ilustrar su interpretación repetimos 20 medias de una población normal con μ=200: el parámetro permanece fijo y los intervalos cambian. La cobertura de estas 20 repeticiones puede diferir del nivel nominal. Un IC de la media no contiene necesariamente ese porcentaje de observaciones individuales.


<a id="P3-07"></a>
## Lámina 03 · Confianza, precisión y tamaño muestral

**Identificador de enlace:** `P3-07`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · intervalos-de-confianza-determinacion-del-tamano-muestral · **Modalidad:** Presencial.

**Pregunta:** Confianza, precisión y tamaño muestral

















**Consigna:** Para la misma media y muestra, aumentar la confianza ensancha el intervalo. Aumentar n reduce el error estándar; cuadruplicar n reduce el margen a la mitad. Para planificar, n = techo((z σ/E)²), con σ conocida y E como margen o semilongitud deseada, no longitud completa. Se conservan x̄=200 y σ=60 del ejemplo de Sebastián.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-07

Ejecutar después de intentar la consigna.


```r
xbarra <- 200
sigma <- 60
n <- 36
confianza <- 0.95
E <- 10
niveles <- c(0.90, 0.95, 0.99)
z_niveles <- qnorm((1 + niveles) / 2)
se <- sigma / sqrt(n)
limites <- cbind(inferior = xbarra - z_niveles * se,
                 superior = xbarra + z_niveles * se)
rownames(limites) <- paste0(100 * niveles, "%")
print(limites)
plot(range(limites), c(1, 3), type = "n", yaxt = "n",
     xlab = "Media de ventas", ylab = "Confianza")
axis(2, at = 1:3, labels = rownames(limites))
segments(limites[, 1], 1:3, limites[, 2], 1:3, lwd = 3, col = "#0160A0")
points(rep(xbarra, 3), 1:3, pch = 19)
n_requerido <- ceiling((qnorm((1 + confianza) / 2) * sigma / E)^2)
print(c(margen_deseado = E, n_requerido = n_requerido))
```


**Lectura del resultado:** Para la misma media y muestra, aumentar la confianza ensancha el intervalo. Aumentar n reduce el error estándar; cuadruplicar n reduce el margen a la mitad. Para planificar, n = techo((z σ/E)²), con σ conocida y E como margen o semilongitud deseada, no longitud completa. Se conservan x̄=200 y σ=60 del ejemplo de Sebastián.


<a id="P3-11"></a>
## Lámina 04 · Proporciones: intervalo y planificación

**Identificador de enlace:** `P3-11`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · ic-para-las-proporciones-ejemplo · **Modalidad:** Presencial.

**Pregunta:** Proporciones: intervalo y planificación

















**Consigna:** Ejemplo: 19 defectuosos entre 200 productos y afirmación del proveedor p=0,05. Usamos el IC normal p̂ ± z√(p̂(1−p̂)/n), con n≥30, éxitos>5 y fracasos>5. Para planificar, n = techo(z² p*(1−p*)/E²); p*=0,5 es el caso conservador cuando no hay una estimación preliminar. E es el margen, y el largo total es 2E.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-11

Ejecutar después de intentar la consigna.


```r
exitos <- 19
n <- 200
confianza <- 0.95
p_previa <- 0.5
E <- 0.03
p_hat <- exitos / n
z <- qnorm((1 + confianza) / 2)
if (n >= 30 && exitos > 5 && n - exitos > 5) {
  se <- sqrt(p_hat * (1 - p_hat) / n)
  ic <- p_hat + c(-1, 1) * z * se
  print(c(proporcion = p_hat, inferior = ic[1], superior = ic[2],
          contiene_0_05 = ic[1] <= 0.05 && ic[2] >= 0.05))
  plot(range(c(ic, 0.05)), c(0, 1), type = "n", yaxt = "n",
       xlab = "Proporción de defectuosos", ylab = "")
  segments(ic[1], 0.5, ic[2], 0.5, lwd = 3, col = "#0160A0")
  points(p_hat, 0.5, pch = 19)
  abline(v = 0.05, lty = 2)
} else {
  message("No se cumplen las condiciones de la aproximación normal.")
}
n_requerido <- ceiling(z^2 * p_previa * (1 - p_previa) / E^2)
print(c(n_requerido = n_requerido, largo_deseado = 2 * E))
```


**Lectura del resultado:** Ejemplo: 19 defectuosos entre 200 productos y afirmación del proveedor p=0,05. Usamos el IC normal p̂ ± z√(p̂(1−p̂)/n), con n≥30, éxitos>5 y fracasos>5. Para planificar, n = techo(z² p*(1−p*)/E²); p*=0,5 es el caso conservador cuando no hay una estimación preliminar. E es el margen, y el largo total es 2E.


<a id="P3-15"></a>
## Lámina 05 · Diferencia de dos medias independientes

**Identificador de enlace:** `P3-15`. La numeración se reinicia por bloque, como en la web.

**Referencia:** Parte 3 · ejemplo_1 · **Modalidad:** Presencial.

**Pregunta:** Diferencia de dos medias independientes

















**Consigna:** Ejemplo: media de ingeniería industrial 800.000, arquitectura 680.000; nₓ=144, nᵧ=121; σₓ=60.000 y σᵧ=50.000 conocidas. Se usa (x̄−ȳ) ± z√(σₓ²/nₓ+σᵧ²/nᵧ), suponiendo independencia. Si el intervalo contiene cero, no se detecta una diferencia al nivel elegido. Si lo excluye, hay evidencia de diferencia, pero no de un efecto causal de estudiar una carrera. Estos montos son los del ejemplo de cátedra, no salarios de wage1.

**Datos:** wage1: CPS de Estados Unidos, 1976; ver diccionario y limitaciones al inicio.


### Solución · P3-15

Ejecutar después de intentar la consigna.


```r
xbarra <- 800000
ybarra <- 680000
sigma_x <- 60000
sigma_y <- 50000
nx <- 144
ny <- 121
confianza <- 0.95
diferencia <- xbarra - ybarra
se <- sqrt(sigma_x^2 / nx + sigma_y^2 / ny)
z <- qnorm((1 + confianza) / 2)
ic <- diferencia + c(-1, 1) * z * se
print(c(diferencia = diferencia, inferior = ic[1], superior = ic[2],
        contiene_cero = ic[1] <= 0 && ic[2] >= 0))
plot(range(c(ic, 0)), c(0, 1), type = "n", yaxt = "n",
     xlab = "Diferencia de medias (pesos del ejemplo de cátedra)", ylab = "")
segments(ic[1], 0.5, ic[2], 0.5, lwd = 3, col = "#0160A0")
points(diferencia, 0.5, pch = 19)
abline(v = 0, lty = 2)
```


**Lectura del resultado:** Ejemplo: media de ingeniería industrial 800.000, arquitectura 680.000; nₓ=144, nᵧ=121; σₓ=60.000 y σᵧ=50.000 conocidas. Se usa (x̄−ȳ) ± z√(σₓ²/nₓ+σᵧ²/nᵧ), suponiendo independencia. Si el intervalo contiene cero, no se detecta una diferencia al nivel elegido. Si lo excluye, hay evidencia de diferencia, pero no de un efecto causal de estudiar una carrera. Estos montos son los del ejemplo de cátedra, no salarios de wage1.


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


## Ejercitación

### Parte 1 · Programación en R: 100 wall balls

Una persona quiere completar 100 wall balls, alternando bloques de repeticiones y descansos. Comienza con 16 repeticiones y reduce una repetición en cada bloque: 16, 15, 14, 13, 12, 11, 10 y 9. Descansa entre bloques; al completar 100 termina la rutina, sin un descanso adicional.

Escribe un programa en R que genere los bloques mediante un ciclo, sin escribir el vector completo a mano. Guarda las repeticiones de cada bloque y el total acumulado en dos vectores. Muestra un registro con el número de bloque, sus repeticiones y el acumulado. Comprueba con una condición que el total sea exactamente 100 y calcula cuántos bloques y descansos hay. ¿Qué condición permite terminar el ciclo? Resuélvelo primero con for y después con while.

Resultado de control: 8 bloques, 7 descansos y 100 repeticiones. El desafío es construir el procedimiento, no imprimir estos resultados directamente. Se trata de un ejercicio de programación, no de una prescripción de entrenamiento.

### Parte 2 · Análisis estadístico con wage2

Trabaja con wage2, otra base de corte transversal del libro Wooldridge: 935 observaciones y 17 variables correspondientes a 1980. Cada fila representa a una persona. Aquí wage es el ingreso mensual; no es el salario por hora de wage1. No combines ambas escalas.

Usa wage (ingreso mensual), educ (años de educación), exper (años de experiencia), tenure (años con el empleador actual), age (edad), hours (horas semanales promedio) y married (1: casado; 0: no casado). El grupo no casado no equivale necesariamente a soltero. La documentación advierte inconsistencias entre tenure, exper y age: identifícalas y no las corrijas arbitrariamente.

Responde con código R, resultados e interpretación breve. En cada cálculo informa el número de casos utilizados y los faltantes excluidos. Los intervalos se plantean como aproximaciones de práctica, bajo independencia y representatividad; no prueban causalidad ni garantizan representar una población sin revisar el diseño muestral.

[Diccionario de wage2](https://justinmshea.github.io/wooldridge/reference/wage2.html)

```r
# Ejecuta la instalación una vez, si aún no tienes el paquete:
# install.packages("wooldridge", repos = "https://cloud.r-project.org/")
library(wooldridge)
datos_ejercicio <- as.data.frame(wooldridge::wage2)
head(datos_ejercicio)
# Diccionario completo de las variables:
help("wage2", package = "wooldridge")
```

1. Inspecciona la base: ¿cuántas filas y columnas contiene y qué tipo de datos son? Cuenta los faltantes de las siete variables seleccionadas. ¿Qué representa una fila y en qué unidad se mide wage?

2. Calcula la media, mediana, moda (incluye todas si hay empates) y percentiles 24, 50 y 75 de wage. ¿Qué revela la diferencia entre media y mediana?

3. Calcula varianza, desviación estándar, rango intercuartílico y coeficiente de variación de wage. Explica las unidades de cada medida y expresa el coeficiente de variación como porcentaje.

4. Dibuja un histograma y un boxplot de wage, con títulos y unidades. Describe la asimetría y los posibles valores atípicos; explica por qué un valor extremo no debe eliminarse automáticamente.

5. Compara el ingreso mensual de casados y no casados: muestra tamaños de grupo, medias, medianas y un boxplot por married. ¿En qué difieren sus distribuciones?

6. Calcula las correlaciones de Pearson entre wage, educ, exper y tenure usando los mismos casos completos. Dibuja wage frente a educ y describe la asociación, sin atribuirle causalidad.

7. Construye un intervalo aproximado de confianza del 95 % para el ingreso mensual medio: media ± qnorm(0.975) × sd(wage)/sqrt(n), con casos válidos. Justifica la aproximación de muestra grande e interpreta el intervalo como estimación de una media, no de salarios individuales.

8. Estima la proporción de personas casadas y su intervalo normal aproximado del 95 %: p ± qnorm(0.975) × sqrt(p*(1-p)/n). Comprueba n ≥ 30, éxitos > 5 y fracasos > 5 antes de usarlo. ¿Qué población podrías describir y bajo qué supuestos?

9. Estima la diferencia de medias de wage (casados menos no casados) y un intervalo aproximado del 95 %: diferencia ± qnorm(0.975) × sqrt(s1^2/n1 + s0^2/n0). Informa los tamaños de ambos grupos, revisa la aproximación de muestras grandes e indica si el intervalo contiene cero. ¿Por qué no demuestra un efecto causal del matrimonio?

10. Compara los intervalos del 90 %, 95 % y 99 % para la media total de wage en un gráfico con un punto central y una barra por intervalo. ¿Cómo cambia su amplitud al aumentar la confianza? Si cuadruplicaras n manteniendo la dispersión, ¿qué pasaría con el margen?

Entrega un notebook con el programa de la primera parte y las diez respuestas de la segunda. Incluye gráficos rotulados y conclusiones apoyadas en los resultados.


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
| P1-07 | Parte 1 · láminas 8–11 | `p1-07-consigna` / `p1-07-r` | Presencial |
| P1-01 | Parte 1 · lámina 1 | `p1-01-consigna` / `p1-01-r` | Presencial |
| P1-02 | Parte 1 · lámina 2 | `p1-02-consigna` / `p1-02-r` | Presencial |
| P1-04 | Parte 1 · lámina 4 | `p1-04-consigna` / `p1-04-r` | Presencial |
| P1-05 | Parte 1 · láminas 5–6 | `p1-05-consigna` / `p1-05-r` | Presencial |
| P1-06 | Parte 1 · lámina 7 | `p1-06-consigna` / `p1-06-r` | Ampliación autónoma |
| P1-09 | Parte 1 · lámina 14 | `p1-09-consigna` | Ampliación autónoma |
| P1-08 | Parte 1 · láminas 12–13 | `p1-08-consigna` / `p1-08-r` | Presencial |
| P2-01 | Ayudantía · Localización central y percentiles de Sebastián | `p2-01-consigna` / `p2-01-r` | Presencial |
| P2-02 | Ayudantía · Dispersión, histograma y boxplot de Sebastián | `p2-02-consigna` / `p2-02-r` | Presencial |
| P3-01 | Parte 3 · teorema-central-del-limite | `p3-01-consigna` / `p3-01-r` | Presencial |
| P3-05 | Parte 3 · ic-ejemplo1 | `p3-05-consigna` / `p3-05-r` | Presencial |
| P3-07 | Parte 3 · intervalos-de-confianza-determinacion-del-tamano-muestral | `p3-07-consigna` / `p3-07-r` | Presencial |
| P3-11 | Parte 3 · ic-para-las-proporciones-ejemplo | `p3-11-consigna` / `p3-11-r` | Presencial |
| P3-15 | Parte 3 · ejemplo_1 | `p3-15-consigna` / `p3-15-r` | Presencial |

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
