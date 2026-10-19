"""Consignas comunes para la web, el notebook y la guía."""
from html import escape

WALL = '''Una persona quiere completar 100 wall balls, alternando bloques de repeticiones y descansos. Comienza con 16 repeticiones y reduce una repetición en cada bloque: 16, 15, 14, 13, 12, 11, 10 y 9. Descansa entre bloques; al completar 100 termina la rutina, sin un descanso adicional.

Escribe un programa en R que genere los bloques mediante un ciclo, sin escribir el vector completo a mano. Guarda las repeticiones de cada bloque y el total acumulado en dos vectores. Muestra un registro con el número de bloque, sus repeticiones y el acumulado. Comprueba con una condición que el total sea exactamente 100 y calcula cuántos bloques y descansos hay. ¿Qué condición permite terminar el ciclo? Resuélvelo primero con for y después con while.

Resultado de control: 8 bloques, 7 descansos y 100 repeticiones. El desafío es construir el procedimiento, no imprimir estos resultados directamente. Se trata de un ejercicio de programación, no de una prescripción de entrenamiento.'''
DATA = '''Trabaja con wage2, otra base de corte transversal del libro Wooldridge: 935 observaciones y 17 variables correspondientes a 1980. Cada fila representa a una persona. Aquí wage es el ingreso mensual; no es el salario por hora de wage1. No combines ambas escalas.

Usa wage (ingreso mensual), educ (años de educación), exper (años de experiencia), tenure (años con el empleador actual), age (edad), hours (horas semanales promedio) y married (1: casado; 0: no casado). El grupo no casado no equivale necesariamente a soltero. La documentación advierte inconsistencias entre tenure, exper y age: identifícalas y no las corrijas arbitrariamente.

Responde con código R, resultados e interpretación breve. En cada cálculo informa el número de casos utilizados y los faltantes excluidos. Los intervalos se plantean como aproximaciones de práctica, bajo independencia y representatividad; no prueban causalidad ni garantizan representar una población sin revisar el diseño muestral.'''
LOAD = '''# Ejecuta la instalación una vez, si aún no tienes el paquete:
# install.packages("wooldridge", repos = "https://cloud.r-project.org/")
library(wooldridge)
datos_ejercicio <- as.data.frame(wooldridge::wage2)
head(datos_ejercicio)
# Diccionario completo de las variables:
help("wage2", package = "wooldridge")'''
QUESTIONS = [
'Inspecciona la base: ¿cuántas filas y columnas contiene y qué tipo de datos son? Cuenta los faltantes de las siete variables seleccionadas. ¿Qué representa una fila y en qué unidad se mide wage?',
'Calcula la media, mediana, moda (incluye todas si hay empates) y percentiles 24, 50 y 75 de wage. ¿Qué revela la diferencia entre media y mediana?',
'Calcula varianza, desviación estándar, rango intercuartílico y coeficiente de variación de wage. Explica las unidades de cada medida y expresa el coeficiente de variación como porcentaje.',
'Dibuja un histograma y un boxplot de wage, con títulos y unidades. Describe la asimetría y los posibles valores atípicos; explica por qué un valor extremo no debe eliminarse automáticamente.',
'Compara el ingreso mensual de casados y no casados: muestra tamaños de grupo, medias, medianas y un boxplot por married. ¿En qué difieren sus distribuciones?',
'Calcula las correlaciones de Pearson entre wage, educ, exper y tenure usando los mismos casos completos. Dibuja wage frente a educ y describe la asociación, sin atribuirle causalidad.',
'Construye un intervalo aproximado de confianza del 95 % para el ingreso mensual medio: media ± qnorm(0.975) × sd(wage)/sqrt(n), con casos válidos. Justifica la aproximación de muestra grande e interpreta el intervalo como estimación de una media, no de salarios individuales.',
'Estima la proporción de personas casadas y su intervalo normal aproximado del 95 %: p ± qnorm(0.975) × sqrt(p*(1-p)/n). Comprueba n ≥ 30, éxitos > 5 y fracasos > 5 antes de usarlo. ¿Qué población podrías describir y bajo qué supuestos?',
'Estima la diferencia de medias de wage (casados menos no casados) y un intervalo aproximado del 95 %: diferencia ± qnorm(0.975) × sqrt(s1^2/n1 + s0^2/n0). Informa los tamaños de ambos grupos, revisa la aproximación de muestras grandes e indica si el intervalo contiene cero. ¿Por qué no demuestra un efecto causal del matrimonio?',
'Compara los intervalos del 90 %, 95 % y 99 % para la media total de wage en un gráfico con un punto central y una barra por intervalo. ¿Cómo cambia su amplitud al aumentar la confianza? Si cuadruplicaras n manteniendo la dispersión, ¿qué pasaría con el margen?'
]

def markdown():
 return ('## Ejercitación\n\n### Parte 1 · Programación en R: 100 wall balls\n\n'+WALL+'\n\n### Parte 2 · Análisis estadístico con wage2\n\n'+DATA+'\n\n[Diccionario de wage2](https://justinmshea.github.io/wooldridge/reference/wage2.html)\n\n```r\n'+LOAD+'\n```\n\n'+'\n\n'.join(f'{i}. {q}' for i,q in enumerate(QUESTIONS,1))+'\n\nEntrega un notebook con el programa de la primera parte y las diez respuestas de la segunda. Incluye gráficos rotulados y conclusiones apoyadas en los resultados.\n')

def render():
 paras=lambda s: ''.join('<p>'+escape(p)+'</p>' for p in s.split('\n\n'))
 return ('<section class="brief" id="ejercitacion"><h2>✍️ Ejercitación</h2><details class="check"><summary>Parte 1 · Programación en R: 100 wall balls</summary><div class="solution-body">'+paras(WALL)+'</div></details><details class="check"><summary>Parte 2 · Análisis estadístico con wage2</summary><div class="solution-body">'+paras(DATA)+'<p><a href="https://justinmshea.github.io/wooldridge/reference/wage2.html">Diccionario y fuente de wage2 ↗</a></p><h3>Descarga y carga de los datos</h3><pre><code>'+escape(LOAD)+'</code></pre><h3>Diez preguntas para resolver en R</h3><ol>'+''.join('<li><p>'+escape(q)+'</p></li>' for q in QUESTIONS)+'</ol></div></details><p>Entrega un notebook con el programa de la primera parte y las diez respuestas de la segunda. Incluye gráficos rotulados y conclusiones apoyadas en los resultados.</p><p><a href="clase-taller-1.ipynb" download>Descargar notebook con las consignas ↓</a></p></section>')
