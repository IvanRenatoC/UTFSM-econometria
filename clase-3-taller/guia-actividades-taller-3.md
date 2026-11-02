# Clase 3 · Causalidad y variable omitida en R

Taller práctico de la cátedra 3: de la comparación de promedios a la selección, la aleatorización y los controles.

Docente: Iván Canales

Ejecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.

## Agenda

- 18:50–19:00: Tema 1 · Asociación y contrafactual
- 19:00–19:20: Tema 2 · Resultados potenciales, ATE y ATT
- 19:20–19:40: Tema 3 · Selección y alarmas
- 19:40–20:00: Tema 4 · Aleatorización y repetición
- 20:00–20:15: Descanso
- 20:15–20:35: Tema 5 · Variable omitida y regresión auxiliar
- 20:35–20:45: Tema 6 · Signo del sesgo
- 20:45–21:00: Tema 7 · Controles: fumar y edad
- 21:00–21:10: Tema 8 · Variables irrelevantes
- 21:10–21:25: Práctica guiada con wage2 y cierre

## Parte 1 · Causalidad y selección · Comparar personas no es observar contrafactuales

### De la asociación al problema causal

Retomemos el taller 2: wage1 contiene 526 personas de Estados Unidos (CPS 1976). wage mide salario por hora en USD de 1976; educ, años de educación. ¿La pendiente positiva permite afirmar que estudiar causa ese aumento salarial? Primero describe la nube; luego distingue asociación y causalidad.

**Referencia en la cátedra:** Tema 1 · Esperanza condicional versus causalidad y contrafactual

```r
# Ejecuta primero esta celda en Colab con kernel R.
if (file.exists("datos/wage1.csv")) {
  salarios <- read.csv("datos/wage1.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  salarios <- wooldridge::wage1
}
head(salarios[, c("wage", "educ")])
modelo_asociacion <- lm(wage ~ educ, data = salarios)
print(coef(modelo_asociacion))
plot(wage ~ educ, data = salarios, pch = 19, col = "#005E9060",
     main = "Educación y salario: una asociación",
     xlab = "Educación (años)", ylab = "Salario por hora (USD de 1976)")
abline(modelo_asociacion, col = "#D6A600", lwd = 3)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)        educ
 -0.9048516   0.5413593
```

**El código, paso a paso**

**lm(wage ~ educ, data = salarios)**

Es el ajuste de la clase anterior. E[Y | X] resume diferencias entre personas observadas; no equivale automáticamente a comparar a una persona consigo misma en dos mundos.

**El contrafactual**

No es simplemente el salario pasado ni el promedio de otra persona. Es el resultado que esa misma persona habría obtenido bajo la alternativa que no ocurrió.

**Lectura del resultado:** La pendiente es aproximadamente 0.541 USD/h por año de educación. Describe una asociación promedio. No conocemos el salario que habría recibido la misma persona con otra educación: ese resultado alternativo es su contrafactual. Habilidad, oportunidades y recursos previos pueden relacionarse con ambas variables.

### Resultados potenciales: solo observamos un mundo

Cada fila corresponde a una persona. $Y^{NT}$ es su resultado potencial sin tratamiento y $Y^{T}$, con tratamiento. Observamos $Y^{T}$ si T = 1 y $Y^{NT}$ si T = 0. Para completar la tabla didáctica fijaremos efectos individuales de 25, 15, 20, 10 y 15 unidades. Son supuestos del ejemplo: no se estiman con los datos observados ni son efectos causales identificados.

**Tratamiento y grupo de control**

T = 1 indica que la persona recibe el tratamiento; T = 0 indica que no lo recibe y pertenece al grupo de control o no tratado. Cada persona tiene un solo resultado observado.

**Nomenclatura de la cátedra y nombres en R**

En las explicaciones usamos $Y^{NT}$ y $Y^{T}$. En el código escribimos `Y_NT` y `Y_T` como nombres de columnas para almacenar esos mismos resultados.

**La misma población artificial de cinco personas**

| Persona | T | Y observado | $Y^{NT}$ | $Y^{T}$ | Efecto supuesto |
| --- | --- | --- | --- | --- | --- |
| Sofía | 1 | 100 | 75 | 100 | 25 |
| Paula | 0 | 40 | 40 | 55 | 15 |
| Ezequiel | 1 | 80 | 60 | 80 | 20 |
| Juan | 0 | 20 | 20 | 30 | 10 |
| Caro | 1 | 60 | 45 | 60 | 15 |

**Para desarrollar en la pizarra**

**Cómo se completa el ejemplo**

$$Y^{T}=Y^{NT}+\text{efecto supuesto}$$

**Si T = 1: observamos el resultado con tratamiento**

Sofía: $Y^{T}$ = 100 y $Y^{NT}$ = 100 − 25 = 75. Ezequiel: $Y^{T}$ = 80 y $Y^{NT}$ = 80 − 20 = 60. Caro: $Y^{T}$ = 60 y $Y^{NT}$ = 60 − 15 = 45.

**Si T = 0: observamos el resultado sin tratamiento**

Paula: $Y^{NT}$ = 40 y $Y^{T}$ = 40 + 15 = 55. Juan: $Y^{NT}$ = 20 y $Y^{T}$ = 20 + 10 = 30.

**Qué significa el cálculo**

La resta o suma completa un mundo que nosotros construimos al fijar los efectos. Sin ese supuesto no podríamos conocer los valores faltantes. No debemos confundir completar esta tabla artificial con recuperar contrafactuales reales.

**Referencia en la cátedra:** Tema 2 · Marco de Rubin y resultados observados/no observados

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
    nombre T   Y Y_NT Y_T efecto
1    Sofía 1 100   75 100     25
2    Paula 0  40   40  55     15
3 Ezequiel 1  80   60  80     20
4     Juan 0  20   20  30     10
5     Caro 1  60   45  60     15
```

**El código, paso a paso**

**Crear la tabla y calcular sus dos columnas potenciales**

Ejecuta el bloque completo de esta viñeta. Para los tratados restamos el efecto supuesto al resultado observado; para los no tratados lo sumamos. Las columnas de R representan $Y^{NT}$ y $Y^{T}$.

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y", "Y_NT", "Y_T", "efecto")])
```

**Comprobar que recuperamos los resultados observados**

ifelse() elige el resultado que corresponde al tratamiento recibido. El vector obtenido debe coincidir con Y.

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
Y_recuperado <- ifelse(personas$T == 1, personas$Y_T, personas$Y_NT)
print(Y_recuperado)
print(all(Y_recuperado == personas$Y))
```

**Lectura del resultado:** Los valores completados son $Y^{NT}$ = (75, 40, 60, 20, 45) y $Y^{T}$ = (100, 55, 80, 30, 60). Al seleccionar el estado observado recuperamos (100, 40, 80, 20, 60). Los efectos supuestos permiten construir el ejemplo; los resultados observados, por sí solos, no permiten calcular esos contrafactuales.

### ATE y ATT: promediar efectos diferentes

Calculemos los dos promedios usando la tabla completa de esta misma lámina. La diferencia individual es $Y^{T}$ − $Y^{NT}$. ATE promedia a las cinco personas; ATT promedia solo a Sofía, Ezequiel y Caro, porque recibieron el tratamiento (T = 1).

**La misma población artificial de cinco personas**

| Persona | T | Y observado | $Y^{NT}$ | $Y^{T}$ | Efecto supuesto |
| --- | --- | --- | --- | --- | --- |
| Sofía | 1 | 100 | 75 | 100 | 25 |
| Paula | 0 | 40 | 40 | 55 | 15 |
| Ezequiel | 1 | 80 | 60 | 80 | 20 |
| Juan | 0 | 20 | 20 | 30 | 10 |
| Caro | 1 | 60 | 45 | 60 | 15 |

**Para desarrollar en la pizarra**

**Fórmula · ATE en una población de N personas**

$$ATE=\frac{1}{N}\sum_{i=1}^{N}(Y_i^{T}-Y_i^{NT})$$

**Fórmula · ATT entre las personas tratadas**

$$ATT=\frac{1}{N_T}\sum_{i:T_i=1}(Y_i^{T}-Y_i^{NT})$$

**ATE · Efecto promedio en las cinco personas**

$$ATE=\frac{1}{5}\sum_{i=1}^{5}(Y_i^{T}-Y_i^{NT})=\frac{25+15+20+10+15}{5}=\frac{85}{5}=17$$

**ATT · Efecto promedio entre los tres tratados**

$$ATT=\frac{1}{3}\sum_{i:T_i=1}(Y_i^{T}-Y_i^{NT})=\frac{25+20+15}{3}=\frac{60}{3}=20$$

**Primero: restar los dos resultados de cada fila**

Sofía: 100 − 75 = 25; Paula: 55 − 40 = 15; Ezequiel: 80 − 60 = 20; Juan: 30 − 20 = 10; Caro: 60 − 45 = 15.

**Después: elegir a quiénes promediamos**

ATE usa las cinco diferencias y divide por 5. ATT usa únicamente las diferencias de las filas con T = 1 y divide por 3. No se calcula restando el promedio observado de tratados y no tratados.

**Referencia en la cátedra:** Tema 2 · ATE y ATT

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
ATE <- mean(personas$efecto)
ATT <- mean(personas$efecto[personas$T == 1])
print(personas[, c("nombre", "T", "Y_NT", "Y_T", "efecto")])
print(c(ATE = ATE, ATT = ATT))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
    nombre T Y_NT Y_T efecto
1    Sofía 1   75 100     25
2    Paula 0   40  55     15
3 Ezequiel 1   60  80     20
4     Juan 0   20  30     10
5     Caro 1   45  60     15
ATE ATT
 17  20
```

**El código, paso a paso**

**Crear en R la tabla del ejemplo**

Este código es independiente de la lámina anterior: crea las cinco personas, calcula $Y^{NT}$ y $Y^{T}$ y muestra sus efectos individuales.

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
print(personas[, c("nombre", "T", "Y_NT", "Y_T", "efecto")])
```

**Calcular ATE = 17 y ATT = 20 en R**

Puedes ejecutar esta viñeta por sí sola: incluye la tabla completa. mean() sobre las cinco diferencias calcula ATE; el filtro T == 1 conserva las tres diferencias necesarias para ATT.

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
ATE <- mean(personas$efecto)
ATT <- mean(personas$efecto[personas$T == 1])
print(personas[, c("nombre", "T", "Y_NT", "Y_T", "efecto")])
print(c(ATE = ATE, ATT = ATT))
```

**Lectura del resultado:** ATE = 17 y ATT = 20 en esta población artificial. Son promedios de efectos individuales distintos: 85/5 frente a 60/3. El botón que modifica el resultado con tratamiento de Juan es un reto posterior: ATE pasa a 23 y ATT sigue en 20, porque Juan no es tratado. El código principal conserva la tabla original para obtener 17 y 20.

**Reto adicional: cambiar solo a Juan**

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
alternativa <- personas
alternativa$Y_T[alternativa$nombre == "Juan"] <- 60
alternativa$efecto <- alternativa$Y_T - alternativa$Y_NT
print(c(ATE = mean(alternativa$efecto),
        ATT = mean(alternativa$efecto[alternativa$T == 1])))
```

### Diferencia observada = ATT + selección

La media observada de los tratados es 80 y la del grupo no tratado es 30. ¿Las 50 unidades de diferencia son todas efecto del tratamiento? Usemos la tabla completa para separar el ATT de la diferencia que ya habría existido en ausencia del tratamiento.

**Definición · Grupo de control**

Es el grupo que no recibe el tratamiento (T = 0): Paula y Juan. Sirve como grupo de comparación, pero no constituye automáticamente un buen contrafactual del grupo tratado. Aquí control nombra un grupo de personas, no una variable añadida a la regresión.

**La misma población artificial de cinco personas**

| Persona | T | Y observado | $Y^{NT}$ | $Y^{T}$ | Efecto supuesto |
| --- | --- | --- | --- | --- | --- |
| Sofía | 1 | 100 | 75 | 100 | 25 |
| Paula | 0 | 40 | 40 | 55 | 15 |
| Ezequiel | 1 | 80 | 60 | 80 | 20 |
| Juan | 0 | 20 | 20 | 30 | 10 |
| Caro | 1 | 60 | 45 | 60 | 15 |

**Para desarrollar en la pizarra**

**Diferencia observada**

$$\bar Y_{T=1}-\bar Y_{T=0}=\frac{100+80+60}{3}-\frac{40+20}{2}=80-30=50$$

**Selección · Comparar el mundo sin tratamiento**

$$\frac{75+60+45}{3}-\frac{40+20}{2}=60-30=30$$

**Reconstruir la diferencia observada**

$$\text{Brecha}=ATT+\text{selección}=20+30=50$$

**Referencia en la cátedra:** Tema 3 · ATT y sesgo de selección

```r
personas <- data.frame(
  nombre = c("Sofía", "Paula", "Ezequiel", "Juan", "Caro"),
  T = c(1, 0, 1, 0, 1),
  Y = c(100, 40, 80, 20, 60),
  efecto_supuesto = c(25, 15, 20, 10, 15)
)
# Solo para completar este ejemplo artificial: fijamos los efectos.
personas$Y_NT <- ifelse(personas$T == 0, personas$Y,
                        personas$Y - personas$efecto_supuesto)
personas$Y_T <- ifelse(personas$T == 1, personas$Y,
                       personas$Y + personas$efecto_supuesto)
personas$efecto <- personas$Y_T - personas$Y_NT
tratados <- personas$T == 1
brecha <- mean(personas$Y[tratados]) - mean(personas$Y[!tratados])
ATT <- mean(personas$efecto[tratados])
seleccion <- mean(personas$Y_NT[tratados]) - mean(personas$Y_NT[!tratados])
print(c(brecha = brecha, ATT = ATT, seleccion = seleccion,
        suma = ATT + seleccion))
modelo_T <- lm(Y ~ T, data = personas)
print(coef(modelo_T))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
   brecha       ATT seleccion      suma
       50        20        30        50
(Intercept)           T
         30          50
```

**El código, paso a paso**

**Calcular la diferencia que observamos**

Estos son los resultados observados de los tratados y no tratados del ejemplo. La brecha no necesita conocer contrafactuales.

```r
media_tratados <- mean(c(100, 80, 60))
media_control <- mean(c(40, 20))
print(c(tratados = media_tratados, control = media_control,
        brecha = media_tratados - media_control))
```

**Calcular ATT y selección en el ejemplo construido**

El ATT usa los efectos de los tratados; la selección compara sus resultados sin tratamiento con los de Paula y Juan. Solo podemos hacer esta separación porque fijamos los contrafactuales del ejemplo.

```r
ATT <- mean(c(100 - 75, 80 - 60, 60 - 45))
seleccion <- mean(c(75, 60, 45)) - mean(c(40, 20))
print(c(ATT = ATT, seleccion = seleccion, suma = ATT + seleccion))
```

**Comprobar la pendiente de lm() sin buscar otra lámina**

Esta viñeta vuelve a crear los datos observados. El intercepto es 30 y la pendiente es 50: lm() entrega la diferencia de medias, no el ATT de 20.

```r
observado <- data.frame(T = c(1, 0, 1, 0, 1),
                        Y = c(100, 40, 80, 20, 60))
print(coef(lm(Y ~ T, data = observado)))
```

**Lectura del resultado:** La brecha observada es 50: ATT = 20 más selección = 30. Incluso sin tratamiento, los tratados tendrían un resultado medio 30 unidades mayor. El intercepto de lm(Y ~ T) es 30 y su pendiente es 50. Esa pendiente no es el efecto causal de 20.

### Alarmas: una comparación que puede engañar

Queremos mostrar por qué más robos observados en las casas con alarma no implica que la alarma cause robos. En este ejemplo hipotético, las casas que instalan alarma ya tenían mayor riesgo. $Y^{NT}$ es la tasa que tendría cada grupo sin alarma; $Y^{T}$, la que tendría con alarma. Todas las tasas son por cada 100 casas.

**Definición · Tratados y grupo de control en este ejemplo**

Las casas con alarma son el grupo tratado (T = 1); las casas sin alarma son el grupo de control o no tratado (T = 0). Los grupos pueden tener riesgos iniciales distintos. Cada fila de la tabla resume una tasa de un grupo, no una casa individual.

**Tasas hipotéticas por cada 100 casas**

| Grupo | T | $Y^{NT}$ | $Y^{T}$ | Y observado |
| --- | --- | --- | --- | --- |
| Con alarma | 1 | 12 | 7 | 7 |
| Sin alarma | 0 | 4 | 2 | 4 |

**Para desarrollar en la pizarra**

**La alarma protege en el grupo tratado**

$$ATT=Y^{T}-Y^{NT}=7-12=-5$$

**La comparación observada mezcla efecto y selección**

$$7-4=(-5)+(12-4)=-5+8=3$$

**Referencia en la cátedra:** Tema 3 · Ejemplo de las alarmas

```r
casas <- data.frame(
  grupo = c("Instalan alarma", "No instalan"),
  T = c(1, 0),
  Y_NT = c(12, 4),
  efecto_supuesto = c(-5, -2)
)
casas$Y_T <- casas$Y_NT + casas$efecto_supuesto
casas$Y <- ifelse(casas$T == 1, casas$Y_T, casas$Y_NT)
tratadas <- casas$T == 1
brecha_alarmas <- casas$Y[tratadas] - casas$Y[!tratadas]
ATT_alarmas <- casas$Y_T[tratadas] - casas$Y_NT[tratadas]
seleccion_alarmas <- casas$Y_NT[tratadas] - casas$Y_NT[!tratadas]
print(casas)
print(c(brecha = brecha_alarmas, ATT = ATT_alarmas,
        seleccion = seleccion_alarmas, suma = ATT_alarmas + seleccion_alarmas))
barplot(casas$Y, names.arg = casas$grupo,
        col = c("#005E90", "#D6A600"),
        ylab = "Robos por cada 100 casas (ejemplo hipotético)")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
            grupo T Y_NT efecto_supuesto Y_T Y
1 Instalan alarma 1   12              -5   7 7
2     No instalan 0    4              -2   2 4
   brecha       ATT seleccion      suma
        3        -5         8         3
```

**El código, paso a paso**

**Crear la tabla y sus resultados observados**

El efecto supuesto −5 reduce la tasa de las casas tratadas de 12 a 7. El valor 2 de las casas no tratadas es otro contrafactual supuesto; no se observa.

```r
casas <- data.frame(
  grupo = c("Instalan alarma", "No instalan"),
  T = c(1, 0),
  Y_NT = c(12, 4),
  efecto_supuesto = c(-5, -2)
)
casas$Y_T <- casas$Y_NT + casas$efecto_supuesto
casas$Y <- ifelse(casas$T == 1, casas$Y_T, casas$Y_NT)
print(casas)
```

**Calcular efecto, selección y brecha**

Cada operación usa los valores de la tabla de esta misma lámina. Un efecto negativo significa menos robos; la selección positiva refleja el mayor riesgo inicial.

```r
ATT_alarmas <- 7 - 12
seleccion_alarmas <- 12 - 4
brecha_alarmas <- 7 - 4
print(c(ATT = ATT_alarmas, seleccion = seleccion_alarmas,
        brecha = brecha_alarmas, suma = ATT_alarmas + seleccion_alarmas))
```

**Lectura del resultado:** Observamos 7 frente a 4 robos por 100 casas: brecha = +3. Sin alarma, las casas que la instalaron habrían tenido 12: selección = +8. El efecto en ellas es −5; por tanto, +3 = −5 + 8. Una brecha positiva no demuestra que la alarma aumente los robos.

### Autoselección frente a asignación aleatoria

Imagina un programa de capacitación que, por construcción de esta simulación, aumenta exactamente 10 puntos la productividad de cada persona. Comparamos dos formas de asignar el mismo programa a la misma población: participan quienes tienen mayor habilidad o se sortean 500 cupos entre 1000 personas. El efecto verdadero sigue siendo 10 en ambos escenarios; lo que cambia es quién participa.

**Propósito del ejemplo**

Qué queremos mostrar: una comparación puede sobreestimar mucho un efecto conocido si participan personas que ya eran distintas. Al sortear el tratamiento, esa diferencia de origen deja de ser sistemática.

**1. Fijar una respuesta conocida**

Para cada persona construimos $Y^{T}$ = $Y^{NT}$ + 10. Por eso conocemos el efecto verdadero antes de hacer cualquier regresión o comparación.

**2. Comparar dos reglas de asignación**

En la autoselección, los participantes tienen más habilidad y ya serían más productivos sin el programa. En el sorteo, recibirlo no depende de la habilidad.

**3. Interpretar lo que cambia**

La diferencia observada es aproximadamente 33.525 con autoselección y 10.965 con el sorteo ilustrado. El programa no se volvió mejor o peor: cambió la comparación entre grupos.

**Referencia en la cátedra:** Tema 4 · Aleatorización

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
# Escenario 1: participan las personas con habilidad mayor que cero.
T_auto <- as.numeric(habilidad > 0)
Y_auto <- ifelse(T_auto == 1, Y_T, Y_NT)
# Escenario 2: se sortean 500 cupos, sin cambiar los resultados potenciales.
T_azar <- sample(c(rep(1, n / 2), rep(0, n / 2)))
Y_azar <- ifelse(T_azar == 1, Y_T, Y_NT)
brecha_auto <- mean(Y_auto[T_auto == 1]) - mean(Y_auto[T_auto == 0])
brecha_azar <- mean(Y_azar[T_azar == 1]) - mean(Y_azar[T_azar == 0])
comparacion <- data.frame(
  asignacion = c("Autoselección", "Sorteo"),
  efecto_verdadero = c(10, 10),
  diferencia_observada = c(brecha_auto, brecha_azar)
)
print(comparacion)
print(aggregate(habilidad, list(T = T_auto), mean))
print(aggregate(habilidad, list(T = T_azar), mean))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
     asignacion efecto_verdadero diferencia_observada
1 Autoselección               10             33.52474
2        Sorteo               10             10.96493
  T          x
1 0 -0.7859066
2 1  0.7913583
  T           x
1 0 0.005629664
2 1 0.021903777
```

**El código, paso a paso**

**Construir los dos resultados potenciales**

rnorm() genera una población artificial. La línea Y_T <- Y_NT + 10 impone el efecto conocido de 10 puntos; no lo estima.

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
print(head(data.frame(Y_NT, Y_T, efecto = Y_T - Y_NT)))
```

**Autoselección: elegir según habilidad**

La regla habilidad > 0 favorece a personas que ya tendrían mayor productividad sin el programa. Ejecuta el ejemplo completo de esta viñeta.

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
T_auto <- as.numeric(habilidad > 0)
Y_auto <- ifelse(T_auto == 1, Y_T, Y_NT)
print(mean(Y_auto[T_auto == 1]) - mean(Y_auto[T_auto == 0]))
print(aggregate(habilidad, list(T = T_auto), mean))
```

**Sorteo: la asignación no depende de habilidad**

sample() mezcla 500 unos y 500 ceros. En una asignación concreta puede quedar un pequeño desequilibrio, aunque todos tengan la misma probabilidad de recibir el programa.

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
T_azar <- sample(c(rep(1, n / 2), rep(0, n / 2)))
Y_azar <- ifelse(T_azar == 1, Y_T, Y_NT)
print(mean(Y_azar[T_azar == 1]) - mean(Y_azar[T_azar == 0]))
print(aggregate(habilidad, list(T = T_azar), mean))
```

**Lectura del resultado:** La capacitación suma 10 puntos en ambos casos. Con autoselección, la brecha observada de 33.525 también recoge diferencias de habilidad previas. Con este sorteo, la brecha es 10.965: está cerca de 10, pero no es idéntica porque los grupos de una asignación finita pueden diferir por azar. La siguiente lámina comprobará qué ocurre al repetir el sorteo.

### Un sorteo no elimina el ruido muestral

Imagina que reiniciamos el mismo experimento 200 veces: son las mismas 1000 personas y el mismo efecto de 10 puntos, pero cada vez sorteamos de nuevo quién recibe la capacitación. Cada sorteo produce una diferencia de medias. El histograma no muestra personas ni sus productividades: muestra esas 200 estimaciones.

**Propósito del ejemplo**

Qué queremos mostrar: el resultado de un solo sorteo puede quedar por encima o por debajo de 10 sin que el método tenga sesgo sistemático. Repetir la asignación permite ver esa fluctuación y separarla del sesgo de selección.

**Cómo leer cada elemento del histograma**

Una estimación es la productividad media de tratados menos la de no tratados en un sorteo. Cada barra cuenta cuántas estimaciones cayeron en ese intervalo.

**Qué representa la línea dorada**

Marca 10: el efecto verdadero que fijamos. Esperamos que las diferencias fluctúen alrededor de esa referencia, no que las 200 sean exactamente iguales a ella.

**Qué conclusión buscamos**

El promedio de esta serie es aproximadamente 9.892 y la desviación entre sorteos, 1.050. Es variación muestral: otro conjunto de sorteos daría otras cifras. No revela el contrafactual individual ni asegura exactitud en cada asignación.

**Referencia en la cátedra:** Tema 4 · Aleatorización y variabilidad de muestras

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10

# Repetir la asignación sobre la población que acabamos de construir.
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))
print(c(promedio = mean(estimaciones), dispersion = sd(estimaciones)))
hist(estimaciones, col = "#005E90", border = "white",
     main = "200 sorteos sobre la misma población",
     xlab = "Efecto estimado: diferencia de productividades medias (puntos)")
abline(v = 10, col = "#D6A600", lwd = 3)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
[1] 10.588405  9.915662  9.362470 11.134671 10.007067 12.078062
  promedio dispersion
  9.892482   1.050358
```

**El código, paso a paso**

**Reservar un vector y guardar una estimación por sorteo**

Esta viñeta vuelve a construir la población y ejecuta todo el ciclo; no necesita objetos de otra lámina. numeric(200) reserva las posiciones y el for guarda una diferencia de medias en cada una.

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))
```

**Resumir y graficar las 200 estimaciones**

mean() resume las diferencias estimadas y sd() mide su dispersión entre sorteos. hist() cuenta estimaciones por intervalo y abline(v = 10) marca el efecto verdadero.

```r
set.seed(2026)
n <- 1000
habilidad <- rnorm(n)
Y_NT <- 100 + 15 * habilidad + rnorm(n, sd = 8)
Y_T <- Y_NT + 10

# Repetir la asignación sobre la población que acabamos de construir.
set.seed(2027)
estimaciones <- numeric(200)
for (b in seq_along(estimaciones)) {
  T_b <- sample(c(rep(1, n / 2), rep(0, n / 2)))
  Y_b <- ifelse(T_b == 1, Y_T, Y_NT)
  estimaciones[b] <- mean(Y_b[T_b == 1]) - mean(Y_b[T_b == 0])
}
print(head(estimaciones))
print(c(promedio = mean(estimaciones), dispersion = sd(estimaciones)))
hist(estimaciones, col = "#005E90", border = "white",
     main = "200 sorteos sobre la misma población",
     xlab = "Efecto estimado: diferencia de productividades medias (puntos)")
abline(v = 10, col = "#D6A600", lwd = 3)
```

**Lectura del resultado:** Los 200 sorteos producen estimaciones distintas, centradas aproximadamente en el efecto verdadero de 10 puntos. El promedio de esta serie es 9.892, no 10 exacto. La desviación 1.050 describe cuánto cambian las estimaciones entre sorteos; no es el efecto de la capacitación. La diferencia con la lámina 06 es que aquí observamos muchas asignaciones y no una sola.

## Parte 2 · Variable omitida · Entender qué captura una pendiente

### Variable omitida: construir un sesgo conocido

Piensa en x₁ como un índice estandarizado de formación y en x₂ como otra característica relacionada con ella. Son índices simulados, que pueden tomar valores negativos; no son años de educación ni salarios observados. Primero conoce las dos ecuaciones. Después observa la nube sin recta y dedica 2–3 minutos a discutir las preguntas antes de desplegar la respuesta.

**Propósito del ejemplo**

Queremos observar si una regresión atribuye a x₁ parte de lo que corresponde a x₂ cuando dejamos x₂ fuera del modelo. Conocemos el efecto directo verdadero de x₁ porque nosotros construimos estos datos: es 2.

**Para desarrollar en la pizarra**

**Ecuación que genera el resultado**

$$y=1+2x_1+3x_2+u$$

**Relación entre las variables explicativas**

$$x_2=0.5x_1+v$$

**Qué sabemos antes de ajustar**

En la primera ecuación, aumentar x₁ en una unidad, manteniendo x₂ fijo, aumenta y en 2. Además, x₂ influye en y y tiende a aumentar cuando x₁ aumenta. Los términos u y v agregan variación aleatoria independiente en esta simulación.

**Pausa de discusión: 2–3 minutos**

1. Si ajustamos y ~ x1 y ocultamos x₂, ¿la pendiente debería ser 2, mayor que 2 o menor que 2? ¿Por qué?
2. ¿Qué podría recoger la pendiente de x₁ además de su efecto directo?
3. Si x₂ dejara de relacionarse con x₁, ¿esperarían el mismo problema?

<details><summary>Mostrar respuesta</summary>

Al omitir x₂, el modelo no separa su contribución de la de x₁. Sustituir la segunda ecuación en la primera permite ver qué parte adicional recoge la pendiente. Esta respuesta se refiere al mecanismo que construimos; no es una regla para atribuir causalidad a cualquier regresión observacional.

**Sustituir y reunir los términos de x₁**

$$y=1+2x_1+3(0.5x_1+v)+u=1+3.5x_1+3v+u$$

**Pendiente poblacional al omitir x₂**

$$\widetilde{\beta}_1=2+3\times0.5=3.5$$

</details>

**Referencia en la cátedra:** Tema 5 · De la selección a la variable omitida

```r
set.seed(3)
n_ov <- 250
x1 <- rnorm(n_ov)
v <- rnorm(n_ov)
u <- rnorm(n_ov)
x2 <- 0.5 * x1 + v
y <- 1 + 2 * x1 + 3 * x2 + u
sim_ov <- data.frame(x1, x2, y)
corta <- lm(y ~ x1, data = sim_ov)
larga <- lm(y ~ x1 + x2, data = sim_ov)
print(coef(corta))
print(coef(larga))
plot(y ~ x1, data = sim_ov, pch = 19, col = "#005E9060",
     xlab = "x1 simulada", ylab = "y simulada")
abline(corta, col = "#D6A600", lwd = 3)
# Recta del modelo con control, manteniendo x2 = 0.
abline(a = coef(larga)["(Intercept)"], b = coef(larga)["x1"],
       col = "#005E90", lwd = 3, lty = 2)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
(Intercept)          x1
   1.089019    3.157912
(Intercept)          x1          x2
  0.8759587   1.9975200   2.9637812
```

**El código, paso a paso**

**rnorm(n, mean = 0, sd = 1)**

Función: genera valores normales simulados. `n` es cuántos valores se generan; `mean` es su media y `sd` su desviación estándar. En `rnorm(n_ov)` se usan media 0 y desviación 1. No descarga ni modifica una base real.

**lm(formula, data)**

Función: ajusta un modelo lineal. `formula` indica la respuesta a la izquierda de ~ y los predictores a la derecha; `data` es la tabla donde están las columnas. En `y ~ x1 + x2`, + agrega un predictor separado. El intercepto se incluye por defecto.

**abline(a, b, col, lwd, lty)**

Función: añade una recta a los ejes existentes. `a` es intercepto; `b`, pendiente; `col`, color; `lwd`, grosor; `lty = 2`, trazo discontinuo. La línea azul del ejemplo fija x₂ = 0 en el modelo con control: no es una segunda nube de personas.

**Lectura del resultado:** En esta muestra de 250 observaciones, la pendiente sin x₂ es aproximadamente 3.158 y con x₂ es 1.998. Los valores poblacionales del mecanismo son 3.5 y 2: una muestra contiene ruido. El cambio no significa que el efecto directo haya cambiado: cambia lo que recoge la regresión al omitir o incluir x₂. Usa los botones para quitar la relación entre x₁ y x₂ o hacer irrelevante a x₂.

### Comprobar la fórmula con tres regresiones

Ejecuta los tres ajustes sobre las mismas 250 filas: el modelo corto, el modelo con control y la regresión auxiliar x₂ ~ x₁. Luego extrae los coeficientes por su nombre y verifica la identidad numérica. El código completo de esta lámina incluye la simulación para ejecutarlo sin depender de otra celda.

**Propósito del ejemplo**

Comprobar de dónde sale el cambio de pendiente: necesitamos el coeficiente de x₂ en el modelo con control y la relación estimada entre x₂ y x₁.

**Qué representa cada número**

b1 es la pendiente de x₁ al incluir x₂. b2 es el coeficiente de x₂ en ese mismo ajuste. delta1 es la pendiente de x₂ ~ x₁. El producto b2 × delta1 reconstruye la diferencia entre la pendiente corta y b1; no es una cuarta regresión.

**Referencia en la cátedra:** Tema 5 · Regresión auxiliar y fórmula del sesgo

```r
set.seed(3)
n_ov <- 250
x1 <- rnorm(n_ov)
v <- rnorm(n_ov)
u <- rnorm(n_ov)
x2 <- 0.5 * x1 + v
y <- 1 + 2 * x1 + 3 * x2 + u
sim_ov <- data.frame(x1, x2, y)
corta <- lm(y ~ x1, data = sim_ov)
larga <- lm(y ~ x1 + x2, data = sim_ov)
auxiliar <- lm(x2 ~ x1, data = sim_ov)
b_corta <- unname(coef(corta)["x1"])
b1 <- unname(coef(larga)["x1"])
b2 <- unname(coef(larga)["x2"])
delta1 <- unname(coef(auxiliar)["x1"])
print(c(pendiente_corta = b_corta,
        b1_mas_b2_delta = b1 + b2 * delta1,
        cambio_por_omitir = b2 * delta1))
print(all.equal(b_corta, b1 + b2 * delta1))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  pendiente_corta   b1_mas_b2_delta cambio_por_omitir
         3.157912          3.157912          1.160392
[1] TRUE
```

**El código, paso a paso**

**lm(formula, data) · Regresión auxiliar**

`formula = x2 ~ x1` pone x₂ como respuesta y x₁ como predictor. `data = sim_ov` busca ambas columnas en esa tabla. Guardamos el ajuste en `auxiliar`; su pendiente mide cuánto varía x₂, en promedio, por unidad de x₁.

**coef(object, ...) · Extraer los coeficientes**

`object` es un modelo ya ajustado, por ejemplo `larga`. `coef(larga)` devuelve un vector con nombres: intercepto, x1 y x2. `coef(larga)["x2"]` selecciona la entrada llamada x2. Los corchetes seleccionan; no vuelven a estimar.

**unname(obj, force = FALSE) · Quitar etiquetas**

`obj` es el valor o vector al que quitamos su nombre; `force` se deja en FALSE. `unname(coef(larga)["x2"])` conserva el número y elimina su etiqueta x2. Esto evita que una comparación falle solo porque los números tienen nombres distintos.

**all.equal(target, current, tolerance, check.attributes)**

`target` es el valor de referencia; `current`, el valor que lo debería reproducir. `tolerance` permite pequeñas diferencias de redondeo (por defecto, aproximadamente 1.49e-8); `check.attributes` controla si se comparan también atributos como nombres. La función devuelve TRUE si coinciden dentro de la tolerancia o un texto que describe la diferencia. No comprueba supuestos causales.

**print(x, digits = 6) · Mostrar sin alterar los cálculos**

`x` es lo que se imprime. `digits` pide cifras significativas para mostrar: no cambia el valor almacenado ni fija necesariamente seis decimales. En el ejemplo imprimimos un vector nombrado con la pendiente corta, su reconstrucción y la diferencia por omitir x₂.

**Lectura del resultado:** Con intercepto y las mismas filas, b_corta = b1 + b2 × delta1, salvo redondeo de la computadora. El producto estimado mide la diferencia entre pendientes corta y larga. Llamarlo sesgo causal requiere que el modelo largo cumpla los supuestos necesarios; en la simulación conocemos el modelo generador.

### Predecir el signo: cuatro combinaciones

Hay dos relaciones distintas. delta1 (δ₁) indica cómo se relaciona x₂ con x₁; beta2 (β₂) indica cómo afecta x₂ a y dentro del mecanismo simulado. El signo del producto β₂ × δ₁ indica si la pendiente del modelo corto queda por encima o por debajo de 2 en la población. No es el signo de la pendiente completa.

**Propósito del ejemplo**

Aprender a anticipar la dirección del cambio antes de ejecutar R. La pendiente directa de x₁ sigue siendo 2 en todos los casos; cambia únicamente el componente que se le atribuye por omitir x₂.

**δ₁ · Relación de x₂ con x₁**

δ₁ > 0: al aumentar x₁, x₂ tiende a aumentar. δ₁ < 0: x₂ tiende a disminuir. δ₁ = 0: no hay esa relación lineal en el mecanismo poblacional.

**β₂ · Contribución de x₂ al resultado**

β₂ > 0: x₂ aumenta y, manteniendo x₁ fijo. β₂ < 0: x₂ disminuye y. β₂ = 0: x₂ no interviene en la ecuación del resultado.

**Para desarrollar en la pizarra**

**Dos ecuaciones, dos parámetros con funciones diferentes**

$$x_2=\delta_1x_1+v,\qquad y=1+2x_1+\beta_2x_2+u$$

**Paso 1 · Mira δ₁**

Pregunta si las personas con más x₁ tienden a tener más o menos x₂.

**Paso 2 · Mira β₂**

Pregunta si ese x₂ adicional empuja el resultado hacia arriba o hacia abajo.

**Paso 3 · Multiplica y suma**

Mismos signos: el producto es positivo; distintos signos: negativo. Después se suma a 2. Por ejemplo, un componente negativo puede reducir la pendiente sin hacerla necesariamente negativa. Elige un caso, predice y recién después muestra el resultado.

**Referencia en la cátedra:** Tema 6 · El signo del sesgo

```r
set.seed(3)
n_ov <- 250
x1 <- rnorm(n_ov)
v <- rnorm(n_ov)
u <- rnorm(n_ov)
x2 <- 0.5 * x1 + v
y <- 1 + 2 * x1 + 3 * x2 + u
sim_ov <- data.frame(x1, x2, y)
corta <- lm(y ~ x1, data = sim_ov)
larga <- lm(y ~ x1 + x2, data = sim_ov)

# Cambiar únicamente los dos parámetros de cada escenario.
casos <- data.frame(delta1 = c(0.8, -0.8, -0.8, 0.8, 0),
                    beta2 = c(2, -2, 2, -2, 2))
casos$sesgo_teorico <- casos$delta1 * casos$beta2
casos$pendiente_estimada <- numeric(nrow(casos))
for (j in seq_len(nrow(casos))) {
  x2_j <- casos$delta1[j] * x1 + v
  y_j <- 1 + 2 * x1 + casos$beta2[j] * x2_j + u
  casos$pendiente_estimada[j] <- coef(lm(y_j ~ x1))["x1"]
}
print(casos)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  delta1 beta2 sesgo_teorico pendiente_estimada
1    0.8     2           1.6          3.3663876
2   -0.8    -2           1.6          3.8002913
3   -0.8     2          -1.6          0.1663876
4    0.8    -2          -1.6          0.6002913
5    0.0     2           0.0          1.7663876
```

**El código, paso a paso**

**data.frame(...) y c(...) · Preparar los escenarios**

Cada vector creado con c() forma una columna: `delta1` y `beta2`. La fila j contiene los dos parámetros del escenario j; no son cinco personas ni cinco estimaciones de la misma muestra.

**numeric(length) · Reservar resultados**

`length` indica cuántos ceros tendrá el vector. `numeric(nrow(casos))` reserva una posición por escenario. Después el ciclo reemplaza cada cero con una pendiente estimada.

**nrow(x) y seq_len(length.out) · Contar e indexar**

`x` es la tabla casos. nrow(casos) cuenta sus filas; `seq_len(nrow(casos))` crea los índices del 1 al número de escenarios. Así el ciclo se adapta si añades otra fila.

**for (j in indices) · Repetir un procedimiento**

`j` es el índice actual. En cada vuelta se usan `delta1[j]` y `beta2[j]` para generar x₂ e y; se conservan las mismas x₁, v y u. Solo modificamos los parámetros que queremos comparar.

**lm(y_j ~ x1) y coef(modelo)["x1"]**

En esta llamada, `formula = y_j ~ x1` omite x₂. No pasamos data porque x1 e y_j son vectores del entorno actual. coef() extrae los coeficientes del ajuste y ["x1"] elige la pendiente que guardamos en la fila j.

**Lectura del resultado:** Dos signos iguales producen un sesgo poblacional positivo; signos distintos, uno negativo. Si beta2 o delta1 es cero, el sesgo poblacional por esta omisión es cero. Aun así, la estimación de una muestra puede diferir de 2 por variación muestral.

### Fumar y edad: una pendiente que cambia de signo

Los 100 registros son artificiales. edad se mide en años; fumar es una intensidad simulada y Y un índice artificial. Usa los botones para ver todas las personas o solo un grupo etario, inspeccionar sus filas y comparar sus promedios. Filtrar por grupos amplios sirve para explorar; no equivale a mantener la edad exactamente constante.

**Propósito del ejemplo**

Ver quiénes forman la nube agregada. Al separar edades, podremos observar que las personas mayores tienden a fumar menos y a tener un Y mayor en este ejemplo; mezclar ambos patrones puede producir una asociación engañosa.

**Qué observar antes de ajustar**

Compara dónde se ubica cada grupo en los ejes, su edad media, la intensidad media de fumar y el promedio de Y. Las edades son continuas: los grupos son 20 a menos de 40, 40 a menos de 60 y 60 a 80.

**Qué comparación hacemos**

La recta agregada usa a las 100 personas y mezcla sus edades. Los botones filtran puntos y filas; no cambian el mecanismo ni recalculan un efecto causal por grupo. La lámina siguiente mantendrá fija una edad dentro del modelo.

**Referencia en la cátedra:** Tema 7 · Controles: fumar y edad

```r
set.seed(2026)
fumar_datos <- data.frame(edad = runif(100, min = 20, max = 80))
fumar_datos$fumar <- 30 - 0.3 * fumar_datos$edad + rnorm(100, sd = 2.3)
fumar_datos$Y <- 13 + 0.94 * fumar_datos$fumar +
                0.98 * fumar_datos$edad + rnorm(100)
fumar_datos$persona <- seq_len(nrow(fumar_datos))
fumar_datos$grupo_edad <- cut(fumar_datos$edad,
  breaks = c(20, 40, 60, 80), right = FALSE, include.lowest = TRUE,
  labels = c("20 a <40", "40 a <60", "60 a 80"))
sin_edad <- lm(Y ~ fumar, data = fumar_datos)
con_edad <- lm(Y ~ fumar + edad, data = fumar_datos)
print(table(fumar_datos$grupo_edad))
print(aggregate(cbind(edad, fumar, Y) ~ grupo_edad,
                data = fumar_datos, FUN = mean))
# Cambia este texto por "20 a <40", "40 a <60" o "60 a 80".
grupo_elegido <- "Todos"
observados <- if (grupo_elegido == "Todos") fumar_datos else
  fumar_datos[fumar_datos$grupo_edad == grupo_elegido, ]
print(head(observados[, c("persona", "edad", "fumar", "Y", "grupo_edad")], 10))
colores_edad <- c("#005E90", "#D6A600", "#B83B45")
plot(Y ~ fumar, data = observados, pch = 19,
     col = colores_edad[as.integer(observados$grupo_edad)],
     xlim = range(fumar_datos$fumar), ylim = range(fumar_datos$Y),
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
abline(sin_edad, col = "#1B2A5E", lwd = 3)
print(coef(sin_edad))
print(coef(con_edad))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text

20 a <40 40 a <60  60 a 80
      33       37       30
  grupo_edad     edad     fumar        Y
1   20 a <40 29.21002 20.767396 61.45481
2   40 a <60 49.25415 15.333587 75.67854
3    60 a 80 70.59683  8.997309 90.67541
   persona     edad     fumar        Y grupo_edad
1        1 61.92041  8.733111 81.91545    60 a 80
2        2 53.39183 13.508191 78.35633   40 a <60
3        3 28.40840 19.337077 60.00649   20 a <40
4        4 37.14340 19.890595 68.59806   20 a <40
5        5 53.32214 12.520303 77.60169   40 a <60
6        6 21.50787 23.015367 56.85485   20 a <40
7        7 47.97383 12.764204 71.30526   40 a <60
8        8 71.66064  6.291610 88.52298    60 a 80
9        9 35.15007 19.763078 66.01605   20 a <40
10      10 54.84838 11.247665 77.66314   40 a <60
(Intercept)       fumar
 103.104478   -1.814066
(Intercept)       fumar        edad
 13.1460302   0.9465336   0.9772352
```

**El código, paso a paso**

**runif(n, min, max) y rnorm(n, mean, sd)**

runif() genera edades uniformes: `n = 100` registros y límites `min = 20`, `max = 80`. rnorm() agrega variación normal: usamos `sd = 2.3` en fumar. Una semilla fija permite volver a crear los mismos 100 registros.

**cut(x, breaks, labels, right, include.lowest)**

`x` es el vector de edades; `breaks` fija los límites 20, 40, 60 y 80; `labels` nombra los tres grupos. `right = FALSE` usa intervalos cerrados a la izquierda y abiertos a la derecha; `include.lowest = TRUE` incluye también el límite superior extremo en este caso. El resultado es una variable categórica o factor: una etiqueta de grupo por persona.

**table(x) · Contar personas por grupo**

`x = fumar_datos$grupo_edad` contiene las etiquetas. table() cuenta cuántas veces aparece cada una. No calcula promedios ni efectos. La suma de los tres conteos debe ser 100.

**aggregate(formula, data, FUN) y cbind(...)**

`formula = cbind(edad, fumar, Y) ~ grupo_edad` pide resumir tres columnas por grupo; cbind() las reúne para esta operación. `data` indica la tabla y `FUN = mean` la función aplicada a cada columna en cada grupo. No se escribe mean() porque aquí pasamos la función, no su resultado.

**tabla[condición, columnas] y head(x, n = 10)**

La condición `grupo_edad == "20 a <40"` elige filas; dejar vacío lo que está después de la coma conserva todas las columnas. `head(x, n = 10)` muestra las primeras diez filas del resultado; no toma una muestra aleatoria.

**as.integer(x) y col = colores_edad[...]**

`x` es el factor de grupos. as.integer() obtiene sus códigos 1, 2 y 3; se usan como posiciones del vector de colores. Esto conserva el mismo color para cada grupo aunque filtremos la tabla.

**Lectura del resultado:** La pendiente agregada es aproximadamente −1.814, mientras que el coeficiente de fumar al incluir edad es +0.947. No son efectos que cambiaron en la población: cambió la comparación. Separar los datos en tres intervalos etarios no garantiza eliminar la confusión por edad dentro de cada intervalo. Este ejemplo ilustra un mecanismo, no es evidencia sanitaria.

### Comparar manteniendo la edad fija

Explora otra vez las filas y los promedios de cada grupo etario. Luego activa las dos líneas de edad fija. Ambas provienen del ajuste Y ~ fumar + edad estimado sobre todas las personas; no son regresiones separadas de cada grupo. La línea continua fija edad = 30 y la discontinua edad = 60.

**Propósito del ejemplo**

Distinguir mirar un grupo de edades de comparar manteniendo la edad fija. Usamos los mismos 100 registros y el mismo modelo; los filtros muestran personas, mientras las líneas representan predicciones a los 30 y 60 años.

**Por qué las dos líneas tienen la misma pendiente**

En este modelo aditivo, fumar tiene un único coeficiente. Cambiar la edad fija modifica el nivel de la línea, no su pendiente. No hemos añadido una interacción entre fumar y edad.

**Qué no hace el filtro**

Mostrar solo a quienes tienen 60–80 años no vuelve a ajustar el modelo ni fija a todos en 60. Las líneas siguen usando el modelo de las 100 personas. Algunas combinaciones extremas de fumar y edad tienen poco apoyo en los datos: dibujarlas no crea observaciones.

**Referencia en la cátedra:** Tema 7 · Soluciones mediante controles

```r
set.seed(2026)
fumar_datos <- data.frame(edad = runif(100, min = 20, max = 80))
fumar_datos$fumar <- 30 - 0.3 * fumar_datos$edad + rnorm(100, sd = 2.3)
fumar_datos$Y <- 13 + 0.94 * fumar_datos$fumar +
                0.98 * fumar_datos$edad + rnorm(100)
fumar_datos$persona <- seq_len(nrow(fumar_datos))
fumar_datos$grupo_edad <- cut(fumar_datos$edad,
  breaks = c(20, 40, 60, 80), right = FALSE, include.lowest = TRUE,
  labels = c("20 a <40", "40 a <60", "60 a 80"))
sin_edad <- lm(Y ~ fumar, data = fumar_datos)
con_edad <- lm(Y ~ fumar + edad, data = fumar_datos)
# El filtro cambia los puntos mostrados, no la muestra que ajustó con_edad.
grupo_elegido <- "Todos"
observados <- if (grupo_elegido == "Todos") fumar_datos else
  fumar_datos[fumar_datos$grupo_edad == grupo_elegido, ]
print(head(observados[, c("persona", "edad", "fumar", "Y", "grupo_edad")], 10))
print(aggregate(cbind(edad, fumar, Y) ~ grupo_edad,
                data = fumar_datos, FUN = mean))
grid_fumar <- seq(min(fumar_datos$fumar), max(fumar_datos$fumar), length.out = 50)
a30 <- data.frame(fumar = grid_fumar, edad = 30)
a60 <- data.frame(fumar = grid_fumar, edad = 60)
colores_edad <- c("#005E90", "#D6A600", "#B83B45")
plot(Y ~ fumar, data = observados, pch = 19,
     col = colores_edad[as.integer(observados$grupo_edad)],
     xlim = range(fumar_datos$fumar), ylim = range(fumar_datos$Y),
     xlab = "Intensidad simulada de fumar", ylab = "Índice Y artificial")
lines(grid_fumar, predict(con_edad, newdata = a30), col = "#1B2A5E", lwd = 3)
lines(grid_fumar, predict(con_edad, newdata = a60), col = "#1B2A5E", lwd = 3, lty = 2)
legend("topright", c("Edad fija: 30", "Edad fija: 60"),
       col = "#1B2A5E", lwd = 3, lty = c(1, 2))
print(summary(con_edad))
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
   persona     edad     fumar        Y grupo_edad
1        1 61.92041  8.733111 81.91545    60 a 80
2        2 53.39183 13.508191 78.35633   40 a <60
3        3 28.40840 19.337077 60.00649   20 a <40
4        4 37.14340 19.890595 68.59806   20 a <40
5        5 53.32214 12.520303 77.60169   40 a <60
6        6 21.50787 23.015367 56.85485   20 a <40
7        7 47.97383 12.764204 71.30526   40 a <60
8        8 71.66064  6.291610 88.52298    60 a 80
9        9 35.15007 19.763078 66.01605   20 a <40
10      10 54.84838 11.247665 77.66314   40 a <60
  grupo_edad     edad     fumar        Y
1   20 a <40 29.21002 20.767396 61.45481
2   40 a <60 49.25415 15.333587 75.67854
3    60 a 80 70.59683  8.997309 90.67541

Call:
lm(formula = Y ~ fumar + edad, data = fumar_datos)

Residuals:
     Min       1Q   Median       3Q      Max
-2.70738 -0.60540  0.01779  0.56642  2.11791

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 13.14603    1.15783   11.35   <2e-16 ***
fumar        0.94653    0.03830   24.71   <2e-16 ***
edad         0.97724    0.01224   79.85   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.9187 on 97 degrees of freedom
Multiple R-squared:  0.9948,	Adjusted R-squared:  0.9947
F-statistic:  9250 on 2 and 97 DF,  p-value: < 2.2e-16

```

**El código, paso a paso**

**seq(from, to, length.out) · Preparar una rejilla**

`from` y `to` son el mínimo y máximo de fumar; `length.out = 50` pide 50 valores ordenados entre ellos. Esta rejilla sirve para trazar predicciones: no representa 50 personas nuevas.

**data.frame(fumar = grid_fumar, edad = 30)**

Crea la tabla de escenarios a predecir. La columna fumar varía en 50 posiciones y la edad 30 se repite en todas. La tabla a60 hace lo mismo con edad 60. Los nombres de columnas deben coincidir con los predictores del modelo.

**predict(object, newdata, interval = "none")**

`object = con_edad` es el ajuste ya estimado; `newdata = a30` entrega los valores de fumar y edad para los que queremos predecir. Con `interval = "none"` (por defecto) obtenemos predicciones puntuales; no bandas ni nuevos datos observados. El cálculo usa los coeficientes del modelo original, no lo vuelve a estimar.

**lines(x, y, col, lwd, lty)**

`x = grid_fumar` y `y = predict(...)` deben tener igual longitud. `col` fija el color, `lwd = 3` el grosor y `lty = 2` la línea discontinua. lines() añade segmentos al gráfico existente; plot() crea los ejes y la nube inicial.

**legend(x, legend, col, lwd, lty)**

`x = "topright"` ubica la leyenda; `legend` contiene los textos. Los vectores `lty = c(1, 2)` y los colores deben corresponder a las líneas dibujadas. Una etiqueta debe describir la predicción, no presentarla como una persona observada.

**Lectura del resultado:** Los puntos son personas simuladas; las líneas son resultados medios predichos al fijar una edad exacta. Su pendiente de fumar es aproximadamente +0.947 y la separación entre líneas refleja el coeficiente de edad. No debemos interpretar filtrar por un intervalo amplio como si fuera controlar exactamente por edad.

### ¿Más controles siempre es mejor?

Construimos un resultado con efecto verdadero 2 para la variable a. Creamos también x₃, muy relacionada con a, pero no la usamos para generar el resultado. Ajustamos el modelo sin x₃ y con x₃ en 200 muestras nuevas de 80 observaciones cada una. La pregunta es si el segundo ajuste queda más cerca de 2 de manera estable o si sus pendientes fluctúan más.

**Propósito del ejemplo**

Mostrar que añadir una variable que no explica y puede hacer menos precisa la pendiente que nos interesa, aunque no introduzca un sesgo sistemático. Compararemos la variación del estimador entre muchas muestras, no solo dos números de una muestra.

**Variable irrelevante en este ejercicio**

x₃ no aparece en la ecuación que genera y: su coeficiente poblacional es 0. Esto no significa que no esté correlacionada con a, ni que podamos identificar una variable irrelevante solo porque su p-valor sea alto en una muestra.

**Precisión del estimador**

Aquí se mide por cuánto varían las 200 pendientes estimadas. Menor dispersión entre muestras significa mayor precisión; no es lo mismo que una pendiente mayor, un R² mayor o un error estándar de las observaciones.

**Para desarrollar en la pizarra**

**Modelo generador y variable añadida**

$$y=1+2a+u,\qquad x_3=0.9a+v$$

**1. Mira una muestra**

Las dos pendientes pueden ser diferentes y cualquiera podría quedar más cerca de 2 en esa ocasión. Una sola muestra no permite observar el sesgo o la varianza del procedimiento.

**2. Mira las 200 muestras**

La media de las pendientes es aproximadamente 1.999 sin x₃ y 1.993 con x₃: ambas se aproximan al valor verdadero 2.

**3. Compara la dispersión**

La desviación entre estimaciones aumenta aproximadamente de 0.105 a 0.261 al añadir x₃. En este diseño, incluir una variable irrelevante que repite información de a hace más difícil separar sus contribuciones y reduce precisión. Un control relevante puede tener otro efecto; no concluimos que todos los controles perjudican.

**Referencia en la cátedra:** Tema 8 · Variables irrelevantes y conclusiones

```r
set.seed(10)
pendientes <- matrix(0, nrow = 200, ncol = 2)
colnames(pendientes) <- c("Sin x3", "Con x3")
for (b in seq_len(nrow(pendientes))) {
  a <- rnorm(80)
  x3 <- 0.9 * a + rnorm(80, sd = 0.45)
  resultado <- 1 + 2 * a + rnorm(80)
  pendientes[b, 1] <- coef(lm(resultado ~ a))["a"]
  pendientes[b, 2] <- coef(lm(resultado ~ a + x3))["a"]
}
print(pendientes[1, ])
barplot(pendientes[1, ], col = c("#005E90", "#D6A600"),
        ylab = "Pendiente estimada", main = "Una sola muestra")
abline(h = 2, lty = 2)
print(colMeans(pendientes))
print(apply(pendientes, 2, sd))
boxplot(pendientes, col = c("#005E90", "#D6A600"),
        ylab = "Pendiente estimada", main = "200 muestras simuladas")
abline(h = 2, lty = 2)
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
  Sin x3   Con x3
1.945225 2.005996
  Sin x3   Con x3
1.998904 1.993283
   Sin x3    Con x3
0.1047310 0.2606908
```

**El código, paso a paso**

**matrix(data = 0, nrow = 200, ncol = 2)**

`data = 0` llena inicialmente con ceros. `nrow = 200` reserva una fila por muestra simulada y `ncol = 2` una columna por modelo. `colnames(pendientes) <- ...` nombra esas dos columnas; no modifica sus valores.

**for (b in seq_len(nrow(pendientes)))**

En cada vuelta se generan 80 observaciones nuevas y se ajustan dos modelos a esa misma muestra. La fila b guarda las dos pendientes. A diferencia de la lámina 07, aquí cambia la muestra completa, no solo la asignación del tratamiento.

**colMeans(x, na.rm = FALSE) · Promedio por columna**

`x = pendientes` es una matriz numérica. colMeans() calcula una media de sus 200 valores en cada columna. `na.rm = FALSE` conserva el tratamiento predeterminado de faltantes; aquí no los hay. Estas medias describen dónde se centran los estimadores, no su dispersión.

**apply(X, MARGIN, FUN, ...) · Aplicar una función**

`X = pendientes` es la matriz; `MARGIN = 2` selecciona columnas (1 seleccionaría filas); `FUN = sd` es la función que aplicamos a cada columna. Se escribe sd sin paréntesis porque pasamos la función. Devuelve dos desviaciones entre estimaciones, una por modelo.

**sd(x, na.rm = FALSE) · Dispersión muestral**

`x` es un vector de pendientes. sd() calcula su desviación estándar con denominador n − 1. Aquí compara cuánto se alejan las estimaciones entre muestras; no es el efecto de a ni la desviación de las observaciones originales.

**boxplot(x, col, ylab, main) y abline(h, lty)**

`x = pendientes` produce una caja por columna. `col` asigna los dos colores; `ylab`, el nombre del eje vertical; `main`, el título. La caja resume cuartiles y mediana; los puntos extremos no son automáticamente errores. `abline(h = 2, lty = 2)` añade una referencia horizontal discontinua en la pendiente verdadera.

**Lectura del resultado:** La demostración busca separar dos conceptos: centrarse cerca de 2 en promedio y ser preciso en una muestra. Ambos ajustes se centran aproximadamente en 2, pero el que añade x₃ fluctúa más en este diseño. No estamos demostrando que una variable deba eliminarse solo por significancia ni que agregar controles siempre aumente la incertidumbre.

## Parte 3 · Práctica guiada · Aplicar controles a datos reales

### Ejercicio guiado: educación, salario e IQ

Ahora trabaja con wage2 de Wooldridge: 935 observaciones del año 1980. wage registra ingresos mensuales (dólares), educ años de educación e IQ una puntuación de test. No confundas este wage mensual con el salario por hora de wage1. IQ es una medida imperfecta; agregarla no garantiza identificar el efecto causal de la educación.

**Referencia en la cátedra:** Aplicación práctica de los temas 5–8 · Datos reales de Wooldridge

**Ejercicio guiado**

**1. Carga y describe los datos**

Ejecuta el bloque de carga; luego identifica cuántas filas quedan y las unidades de las tres variables.

**2. Antes de ajustar**

Dibuja salario frente a educación y calcula cor(trabajo). Predice qué podría ocurrir al añadir IQ sin suponer que observas la habilidad completa.

**complete.cases(...)**

Devuelve TRUE para filas sin valores faltantes en las columnas seleccionadas. Aplicamos el mismo filtro antes de estimar ambos modelos; no debemos comparar pendientes calculadas sobre muestras distintas.

**Preparar los datos: ejecuta sólo este bloque**

```r
# Carga independiente: puedes copiar esta celda directamente en Colab.
if (file.exists("datos/wage2.csv")) {
  trabajo <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  trabajo <- wooldridge::wage2
}
# Mantén las mismas filas al comparar los dos modelos.
trabajo <- trabajo[complete.cases(trabajo[, c("wage", "educ", "IQ")]),
                   c("wage", "educ", "IQ")]
head(trabajo)
print(c(filas = nrow(trabajo)))
```

La carga funciona desde esta carpeta con el CSV local y desde Colab instalando wooldridge. El filtro conserva las mismas filas en todos los ajustes.

```r
print(summary(trabajo))
print(cor(trabajo))
plot(wage ~ educ, data = trabajo, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Ingreso mensual (USD)")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
      wage             educ             IQ
 Min.   : 115.0   Min.   : 9.00   Min.   : 50.0
 1st Qu.: 669.0   1st Qu.:12.00   1st Qu.: 92.0
 Median : 905.0   Median :12.00   Median :102.0
 Mean   : 957.9   Mean   :13.47   Mean   :101.3
 3rd Qu.:1160.0   3rd Qu.:16.00   3rd Qu.:112.0
 Max.   :3078.0   Max.   :18.00   Max.   :145.0
          wage      educ        IQ
wage 1.0000000 0.3271087 0.3090878
educ 0.3271087 1.0000000 0.5156970
IQ   0.3090878 0.5156970 1.0000000
```

**Lectura del resultado:** Revisa primero unidades y filas comparables. Las correlaciones describen asociaciones lineales entre variables observadas. No vemos los salarios potenciales de una misma persona bajo diferentes niveles de educación y un test no recoge todos los factores omitidos.

### Ejercicio guiado: comparar e interpretar los modelos

Escribe primero el modelo simple y después el que incluye IQ. Obtén summary() y anova() de ambos. Compara la pendiente de educación y verifica la descomposición con IQ ~ educ. Explica qué cambia y qué conclusión causal sigue pendiente.

**Referencia en la cátedra:** Aplicación práctica · Controles y límites de una interpretación causal

**Ejercicio guiado**

**1. Dos ajustes sobre las mismas filas**

Estima wage ~ educ y wage ~ educ + IQ. En el segundo, interpreta educación manteniendo IQ constante dentro del modelo.

**2. summary() y anova()**

Lee signo, unidades y magnitud de la pendiente; distingue significancia estadística de identificación causal. En la ANOVA secuencial, la fila IQ evalúa su aporte tras educ.

**3. Regresión auxiliar**

Estima IQ ~ educ y extrae su pendiente. Multiplica por el coeficiente de IQ del modelo con control para reconstruir la diferencia entre pendientes.

```r
modelo_corto <- lm(wage ~ educ, data = trabajo)
modelo_control <- lm(wage ~ educ + IQ, data = trabajo)
print(summary(modelo_corto))
print(anova(modelo_corto))
print(summary(modelo_control))
print(anova(modelo_control))
aux_IQ <- lm(IQ ~ educ, data = trabajo)
b_educ <- unname(coef(modelo_control)["educ"])
b_IQ <- unname(coef(modelo_control)["IQ"])
delta_IQ <- unname(coef(aux_IQ)["educ"])
print(c(corta = unname(coef(modelo_corto)["educ"]),
        control = b_educ, diferencia = b_IQ * delta_IQ,
        reconstruida = b_educ + b_IQ * delta_IQ))
```

**ANOVA · Modelo simple · wage ~ educ · n = 935**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Educación | 16340645 | 1 | 16340645 | 111.79 | < 2.2e-16 |
| Residuos | 136375524 | 933 | 146169 | — | — |

**ANOVA secuencial · Con control · wage ~ educ + IQ · n = 935**

| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |
|---|---:|---:|---:|---:|---:|
| Educación primero | 16340645 | 1 | 16340645 | 115.135 | < 2.2e-16 |
| IQ después de educ | 4100932 | 1 | 4100932 | 28.895 | 9.66e-08 |
| Residuos | 132274591 | 932 | 141926 | — | — |

Sumas de cuadrados redondeadas de anova() en R. En el modelo con control, las contribuciones son secuenciales y dependen del orden de los predictores. SST = suma total; SSE = suma explicada; SSR = suma residual, como en el taller 2.

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text

Call:
lm(formula = wage ~ educ, data = trabajo)

Residuals:
    Min      1Q  Median      3Q     Max
-877.38 -268.63  -38.38  207.05 2148.26

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  146.952     77.715   1.891   0.0589 .
educ          60.214      5.695  10.573   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 382.3 on 933 degrees of freedom
Multiple R-squared:  0.107,	Adjusted R-squared:  0.106
F-statistic: 111.8 on 1 and 933 DF,  p-value: < 2.2e-16

Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
educ        1  16340645 16340645  111.79 < 2.2e-16 ***
Residuals 933 136375524   146169
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Call:
lm(formula = wage ~ educ + IQ, data = trabajo)

Residuals:
    Min      1Q  Median      3Q     Max
-860.29 -251.00  -35.31  203.98 2110.38

Coefficients:
             Estimate Std. Error t value Pr(>|t|)
(Intercept) -128.8899    92.1823  -1.398    0.162
educ          42.0576     6.5498   6.421 2.15e-10 ***
IQ             5.1380     0.9558   5.375 9.66e-08 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 376.7 on 932 degrees of freedom
Multiple R-squared:  0.1339,	Adjusted R-squared:  0.132
F-statistic: 72.02 on 2 and 932 DF,  p-value: < 2.2e-16

Analysis of Variance Table

Response: wage
           Df    Sum Sq  Mean Sq F value    Pr(>F)
educ        1  16340645 16340645 115.135 < 2.2e-16 ***
IQ          1   4100932  4100932  28.895  9.66e-08 ***
Residuals 932 132274591   141926
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
       corta      control   diferencia reconstruida
    60.21428     42.05762     18.15666     60.21428
```

**Lectura del resultado:** La pendiente simple de educación disminuye al incluir IQ en estos datos. Es una diferencia entre asociaciones estimadas; no hemos demostrado cuánto era el sesgo causal. summary() presenta coeficientes, errores estándar, pruebas t y R². anova(modelo_control) atribuye sumas de cuadrados secuencialmente: primero educ, luego IQ según la fórmula; su orden importa. Ningún p-valor comprueba ausencia de variables omitidas. En esta muestra: 60.214 USD mensuales por año de educación en el modelo simple frente a 42.058 con IQ; la diferencia es 18.157.

### Programa completo y cierre: ¿qué podemos afirmar?

Este bloque reúne toda la aplicación de wage2, desde la carga hasta la comparación. Puede ejecutarse solo en una sesión nueva de Colab con kernel R. Antes de mirar la solución, explica: ¿un cambio de pendiente prueba causalidad?, ¿una asignación aleatoria debe dar exactamente 10?, ¿más controles siempre ayuda?

**Referencia en la cátedra:** Tema 8 · Conclusiones y práctica integradora

```r
# Carga independiente: puedes copiar esta celda directamente en Colab.
if (file.exists("datos/wage2.csv")) {
  trabajo <- read.csv("datos/wage2.csv")
} else {
  if (!requireNamespace("wooldridge", quietly = TRUE)) {
    install.packages("wooldridge", repos = "https://cloud.r-project.org/")
  }
  trabajo <- wooldridge::wage2
}
# Mantén las mismas filas al comparar los dos modelos.
trabajo <- trabajo[complete.cases(trabajo[, c("wage", "educ", "IQ")]),
                   c("wage", "educ", "IQ")]
head(trabajo)
print(c(filas = nrow(trabajo)))
# 1. Explorar las variables y su relación.
summary(trabajo)
cor(trabajo)
plot(wage ~ educ, data = trabajo, pch = 19, col = "#005E9060",
     xlab = "Educación (años)", ylab = "Ingreso mensual (USD)")
# 2. Ajustar sin control y con control por IQ.
modelo_corto <- lm(wage ~ educ, data = trabajo)
modelo_control <- lm(wage ~ educ + IQ, data = trabajo)
# 3. Leer los resultados de cada ajuste.
summary(modelo_corto)
anova(modelo_corto)
summary(modelo_control)
anova(modelo_control)
# 4. Reconstruir la pendiente corta mediante la regresión auxiliar.
aux_IQ <- lm(IQ ~ educ, data = trabajo)
b1 <- unname(coef(modelo_control)["educ"])
b2 <- unname(coef(modelo_control)["IQ"])
delta1 <- unname(coef(aux_IQ)["educ"])
print(c(corta = unname(coef(modelo_corto)["educ"]),
        control = b1, componente = b2 * delta1,
        reconstruida = b1 + b2 * delta1))
# 5. Comparar pendientes; las dos NO son efectos causales demostrados.
barplot(c(Simple = coef(modelo_corto)["educ"],
          Con_IQ = coef(modelo_control)["educ"]),
        col = c("#005E90", "#D6A600"),
        ylab = "USD mensuales por año de educación")
```

**Resultados de referencia calculados en R**

**Salida del ejemplo ejecutado en R**

```text
filas
  935
       corta      control   componente reconstruida
    60.21428     42.05762     18.15666     60.21428
```

**El código, paso a paso**

**1. Carga reproducible**

Instala el paquete solo si hace falta, carga wage2 y selecciona las mismas columnas y filas para ambos ajustes.

**2. Explorar y ajustar**

Primero describe, luego estima y lee summary()/anova(). Una tabla de resultados no reemplaza la explicación económica.

**3. Identidad y conclusión**

Verifica la fórmula; distingue la identidad numérica de una afirmación sobre efectos causales.

**Lectura del resultado:** La regresión describe asociaciones; identificar un efecto causal exige un diseño o supuestos defendibles. Diferencia observada = ATT + selección. El signo de la omisión depende de beta2 × delta1. Los controles cambian la comparación y pueden reducir sesgo, pero no sustituyen los supuestos. Para continuar: sección 3.3 de Wooldridge y las indicaciones de la cátedra.

**Autoevaluación**

La pendiente cambia al añadir IQ. ¿Prueba que ya medimos el efecto causal?

1. Sí, porque mejora el R².
2. No: podrían quedar factores omitidos y errores de medición.
3. Sí, si el p-valor es pequeño.

Respuesta: No: podrían quedar factores omitidos y errores de medición. Correcto: controlar por una variable no asegura que el error sea independiente de educación.

¿Qué garantiza una asignación aleatoria bien implementada?

1. Un efecto estimado idéntico al verdadero en cada muestra.
2. Contrafactuales observados para todas las personas.
3. Comparabilidad en promedio sobre las asignaciones.

Respuesta: Comparabilidad en promedio sobre las asignaciones. Correcto: persiste variación muestral y cada persona sigue observada en un solo estado.
