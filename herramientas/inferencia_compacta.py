"""Cinco láminas en el orden y con los ejemplos de la inferencia de Sebastián."""
from html import escape as e
from statistics import mean
import csv,random,json
SOURCE='https://hizocar.github.io/econometria-usm/clases/clase1/'
ZS=[round(random.Random(400+i).gauss(0,1),6) for i in range(20)]

def activity(id,title,kind,reference,description,code):
 return dict(id=id,title=title,inference_kind=kind,source_anchor=reference,
 slides='Parte 3 · '+reference,mode='Presencial',question=title,predict='',task=description,
 code=code.strip(),answer=description,error='',check='')

ACTIVITIES=[
 activity('P3-01','Inferir, TCL y supuestos','tcl','teorema-central-del-limite',
 'Inferir utiliza una muestra para estudiar una población y requiere supuestos. El TCL aproxima la distribución de las medias por una normal de media μ y varianza σ²/n. Aquí wage1 se trata como una población empírica didáctica conocida; no como toda la población de Estados Unidos. La figura es una curva normal de referencia, no una distribución de salarios individuales. Las observaciones deben ser independientes e idénticamente distribuidas, con media y varianza finitas; las reglas n=30/50/100 son orientativas, no garantías.',
 '''if (file.exists("datos/wage1.csv")) {
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
        error_estandar = sigma / sqrt(n)))'''),
 activity('P3-05','Intervalo de confianza para una media','media','ic-ejemplo1',
 'Ejemplo: ventas mensuales, x̄=200, σ=60 conocida y n=36. El intervalo es x̄ ± z × σ/√n. Para ilustrar su interpretación repetimos 20 medias de una población normal con μ=200: el parámetro permanece fijo y los intervalos cambian. La cobertura de estas 20 repeticiones puede diferir del nivel nominal. Un IC de la media no contiene necesariamente ese porcentaje de observaciones individuales.',
 '''xbarra <- 200
sigma <- 60
n <- 36
confianza <- 0.95
z <- qnorm((1 + confianza) / 2)
se <- sigma / sqrt(n)
ic <- xbarra + c(-1, 1) * z * se
print(c(estimacion = xbarra, margen = z * se, inferior = ic[1], superior = ic[2]))

# Ilustración normal con mu = 200 fijo; no es un parámetro estimado de wage1.
mu_demo <- 200
z_demo <- c('''+', '.join(map(str,ZS))+''')
medias_demo <- mu_demo + z_demo * se
inferior <- medias_demo - z * se
superior <- medias_demo + z * se
cubre <- inferior <= mu_demo & superior >= mu_demo
plot(range(c(inferior, superior, mu_demo)), c(1, 20), type = "n",
     xlab = "Media de ventas", ylab = "Repetición")
segments(inferior, 1:20, superior, 1:20,
         col = ifelse(cubre, "#0160A0", "#E12523"), lwd = 2)
abline(v = mu_demo, lty = 2)
print(mean(cubre))'''),
 activity('P3-07','Confianza, precisión y tamaño muestral','precision','intervalos-de-confianza-determinacion-del-tamano-muestral',
 'Para la misma media y muestra, aumentar la confianza ensancha el intervalo. Aumentar n reduce el error estándar; cuadruplicar n reduce el margen a la mitad. Para planificar, n = techo((z σ/E)²), con σ conocida y E como margen o semilongitud deseada, no longitud completa. Se conservan x̄=200 y σ=60 del ejemplo de Sebastián.',
 '''xbarra <- 200
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
print(c(margen_deseado = E, n_requerido = n_requerido))'''),
 activity('P3-11','Proporciones: intervalo y planificación','proporcion','ic-para-las-proporciones-ejemplo',
 'Ejemplo: 19 defectuosos entre 200 productos y afirmación del proveedor p=0,05. Usamos el IC normal p̂ ± z√(p̂(1−p̂)/n), con n≥30, éxitos>5 y fracasos>5. Para planificar, n = techo(z² p*(1−p*)/E²); p*=0,5 es el caso conservador cuando no hay una estimación preliminar. E es el margen, y el largo total es 2E.',
 '''exitos <- 19
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
print(c(n_requerido = n_requerido, largo_deseado = 2 * E))'''),
 activity('P3-15','Diferencia de dos medias independientes','diferencia','ejemplo_1',
 'Ejemplo: media de ingeniería industrial 800.000, arquitectura 680.000; nₓ=144, nᵧ=121; σₓ=60.000 y σᵧ=50.000 conocidas. Se usa (x̄−ȳ) ± z√(σₓ²/nₓ+σᵧ²/nᵧ), suponiendo independencia. Si el intervalo contiene cero, no se detecta una diferencia al nivel elegido. Si lo excluye, hay evidencia de diferencia, pero no de un efecto causal de estudiar una carrera. Estos montos son los del ejemplo de cátedra, no salarios de wage1.',
 '''xbarra <- 800000
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
abline(v = 0, lty = 2)''')
]

def render_inference(a,root):
 kind=a['inference_kind']
 def slider(key,label,value,lo,hi,step=1):
  return f'<label>{label}: <output>{value}</output><input type="range" class="inf-control" data-key="{key}" min="{lo}" max="{hi}" step="{step}" value="{value}"></label>'
 confidence='<label>Confianza: <select class="inf-control" data-key="confianza"><option value="0.90">90 %</option><option value="0.95" selected>95 %</option><option value="0.99">99 %</option></select></label>'
 attrs=''
 if kind=='tcl':
  rows=list(csv.DictReader((root/'datos/wage1.csv').open()));values=[float(r['wage']) for r in rows];mu=mean(values);sigma=(sum((x-mu)**2 for x in values)/len(values))**.5
  attrs=f' data-mu="{mu}" data-sigma="{sigma}"';controls=slider('n','Tamaño de cada muestra',50,5,200)
  formula='X̄ ≈ N(μ, σ²/n) · error estándar = σ/√n'
 elif kind=='media':
  attrs=' data-zs="'+e(json.dumps(ZS))+'"';controls=slider('n','Tamaño muestral',36,5,300)+confidence+'<button type="button" class="inf-repeat chart-choice">Repetir 20 muestras</button>';formula='IC = x̄ ± z × σ/√n'
 elif kind=='precision':controls=slider('n','Tamaño muestral',36,5,400)+confidence+slider('E','Margen deseado E',10,2,30,.5);formula='n requerido = techo((z × σ / E)²)'
 elif kind=='proporcion':controls=slider('n','Productos observados',200,50,1000)+slider('exitos','Productos defectuosos',19,1,199)+confidence+slider('p_previa','Proporción preliminar p*',.5,.05,.95,.01)+slider('E','Margen deseado E',.03,.01,.10,.005);formula='IC = p̂ ± z√(p̂(1−p̂)/n) · n = techo(z²p*(1−p*)/E²)'
 else:controls=slider('xbarra','Media de ingeniería',800000,600000,900000,10000)+slider('nx','n ingeniería',144,30,300)+slider('ny','n arquitectura',121,30,300)+confidence;formula='IC = (x̄−ȳ) ± z√(σₓ²/nₓ + σᵧ²/nᵧ)'
 return f'<div class="inference-demo" data-kind="{kind}"{attrs}><p>{e(a["task"])}</p><p class="inf-formula">{formula}</p><div class="inf-controls">{controls}</div><svg class="wage-chart inf-plot" viewBox="0 0 700 380" role="img" aria-label="Figura interactiva: {e(a["title"])}"></svg><p class="inf-reading" role="status"></p><p class="data-note">Referencia: <a href="{SOURCE}{"#"+a["source_anchor"]}">Cátedra 1</a>.</p><details class="solution"><summary>Código en R de esta lámina</summary><div class="solution-body"><div class="code-head"><span>R</span><button type="button" class="copy">Copiar código</button></div><pre><code class="inf-r-code">{e(a["code"])}</code></pre></div></details></div>'
