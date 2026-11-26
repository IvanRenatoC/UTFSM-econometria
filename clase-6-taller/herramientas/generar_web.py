"""Genera la página, notebook R y script desde una fuente compartida."""
import hashlib
import html
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
C=json.loads((ROOT/'contenido-clase-6.json').read_text())
V=json.loads((ROOT/'datos/verificacion.json').read_text())
assert hashlib.sha256(json.dumps(C,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==V['codigo_sha256']
O=json.loads((ROOT/'datos/salidas-verificadas-r.json').read_text())
e=html.escape
cells=[]
script=['# Clase 6. Ejecutar en orden con R desde clase-6-taller/ o en Colab.']
def md(text,id):
 cells.append(dict(cell_type='markdown',id=id,metadata={},source=(text+'\n').splitlines(True)))
def code(text,id):
 cells.append(dict(cell_type='code',id=id,metadata={},source=(text+'\n').splitlines(True),execution_count=None,outputs=[]))
 script.append(text)
md('# '+C['titulo']+'\n\nTaller práctico de 110 minutos. Selecciona R como entorno de ejecución de Colab. Ejecuta las celdas en orden.\n\n[Clase teórica]('+C['fuente']+')','inicio')
elapsed=0
agenda=[]
for a in C['laminas']:
 agenda.append((f"{elapsed:03}–{elapsed+a['minutos']:03} min",a))
 elapsed+=a['minutos']
assert elapsed==110
md('## Agenda de 110 minutos\n\n| Tiempo transcurrido | Actividad |\n|---|---|\n'+'\n'.join('| '+t+' | '+a['titulo']+' |' for t,a in agenda),'agenda')
parts=[]
def block(c):
 return '<div class="code-head"><span>R</span><button class="copy" type="button">Copiar código</button></div><pre><code>'+e(c)+'</code></pre>'
def render_graph(kind):
 controls={
  'log':'<label>Educación <input type="range" min="6" max="18" value="12" step="1"></label>',
  'lognivel':'<label>Educación <input type="range" min="6" max="18" value="12" step="1"></label>',
  'loglog':'<label>Educación <input type="range" min="1" max="18" value="12" step="1"></label>',
  'cuad':'<label>Experiencia <input type="range" min="1" max="51" value="10" step="1"></label>',
  'int':'<label>Experiencia fija <select><option value="5">5 años</option><option value="20">20 años</option><option value="35">35 años</option></select></label>',
  'escala':'<label>Unidades <select><option value="usd">USD/h y años</option><option value="pesos">Pesos/h y años</option><option value="meses">USD/h y meses</option></select></label>',
  'repaso':'<select hidden aria-label="Modelo de repaso"><option value="lognivel">Log-nivel</option><option value="loglog">Log-log</option><option value="cuad">Cuadrática</option><option value="int">Interacción</option></select>'
 }[kind]
 buttons=''
 if kind=='repaso':
  buttons='<div class="review-buttons" role="group" aria-label="Elige un modelo">'+''.join('<button type="button" data-model="'+k+'" aria-pressed="'+str(k=='lognivel').lower()+'">'+t+'</button>' for k,t in [('lognivel','Log-nivel'),('loglog','Log-log'),('cuad','Cuadrática'),('int','Interacción')])+'</div><p class="review-explanation" aria-live="polite"></p>'
 captions={'lognivel':'Logaritmo del salario frente a educación','loglog':'Logaritmo del salario frente a logaritmo de educación','repaso':'Cuatro modelos, cuatro interpretaciones'}
 return '<figure class="demo" data-plot="'+kind+'"><figcaption>'+captions.get(kind,'Explora la curva estimada con R')+'</figcaption>'+buttons+'<div class="controls">'+controls+'<button type="button" class="animate">Dibujar curva</button><button type="button" class="reset">Restablecer</button></div><canvas width="900" height="460" role="img" aria-label="'+captions.get(kind,'Dispersión observada y curva estimada')+'"></canvas><output aria-live="polite"></output><details><summary>Ver los valores de la curva</summary><div class="curve-table"></div></details></figure>'

for a in C['laminas']:
 id=a['id'].lower()
 steps='\n\n'.join('**'+k+'**\n\n'+v for k,v in a['pasos'])
 md('## '+a['id']+' · '+a['titulo']+'\n\n'+a['texto']+'\n\n### Sentencias del ejemplo\n\n'+steps,id+'-intro')
 extra=''
 fields=''
 if a.get('campos'):
  fields='<table><thead><tr><th>Variable</th><th>Definición y unidad</th></tr></thead><tbody>'+''.join('<tr><td><code>'+e(k)+'</code></td><td>'+e(v)+'</td></tr>' for k,v in a['campos'])+'</tbody></table>'
 if a.get('instalacion'):
  extra='<h4>Preparar Colab</h4><p>Ejecuta esta instalación una vez al preparar el entorno. Después ejecuta el código de carga.</p>'+block(a['instalacion'])
  md('### Variables de la base\n\n'+fields+'\n\n### Preparar Colab\n\nEjecuta esta instalación una vez al preparar el entorno.','preparacion')
  code(a['instalacion'],'instalacion-r')
 code(a['codigo'],id+'-r')
 md('### Resultados del ejemplo\n\n<pre>'+e(O[a['id']]['ejemplo'])+'</pre>\n\n### Ejercicio\n\n'+a['ejercicio']+'\n\n### Solución comentada\n\n'+a['respuesta'],id+'-ejercicio')
 code(a['solucion'],id+'-solucion')
 md('<pre>'+e(O[a['id']]['solucion'])+'</pre>',id+'-resultado')
 graph=render_graph(a['grafico']) if a['grafico'] else ''
 initial_graphs=''.join(render_graph(k) for k in a.get('graficos_inicio',[]))
 final_graphs=''.join(render_graph(k) for k in a.get('graficos_final',[]))
 steps_html=''.join('<details class="explain"><summary><code>'+e(k)+'</code></summary><p>'+e(v)+'</p></details>' for k,v in a['pasos'])
 parts.append('<article class="slide" id="'+a['id']+'"><details><summary class="slide-head">'+e(a['titulo'])+'<span>LÁMINA '+a['id'][-2:]+' · '+str(a['minutos'])+' min</span></summary><div class="slide-body">'+initial_graphs+'<p>'+e(a['texto'])+'</p>'+fields+extra+graph+'<h4>En R · Ejemplo guiado</h4>'+block(a['codigo'])+'<h4>Haz clic en una sentencia para entenderla</h4>'+steps_html+'<details class="solution"><summary>Resultados del ejemplo</summary><pre>'+e(O[a['id']]['ejemplo'])+'</pre></details><h4>Comprueba lo aprendido</h4><p>'+e(a['ejercicio'])+'</p><details class="solution"><summary>Ver solución y explicación</summary><p>'+e(a['respuesta'])+'</p>'+block(a['solucion'])+'<pre>'+e(O[a['id']]['solucion'])+'</pre></details>'+final_graphs+'</div></details></article>')
nb=dict(cells=cells,metadata=dict(kernelspec=dict(display_name='R',language='R',name='ir'),language_info=dict(name='R',file_extension='.r',mimetype='text/x-r-source')),nbformat=4,nbformat_minor=5)
(ROOT/'clase-taller-6.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n')
(ROOT/'clase-taller-6.R').write_text('\n\n'.join(script)+'\n')
toc=''.join('<li><a href="#'+a['id']+'">'+t+' · '+e(a['titulo'])+'</a></li>' for t,a in agenda)
nav=''.join('<a href="../clase-'+str(i)+'-taller/">Clase '+str(i)+'</a>' for i in [1,2,3,4])
page='''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Clase 6 · Interpretación de modelos en R · UTFSM</title><link rel="stylesheet" href="../identidad-utfsm.css"><link rel="stylesheet" href="taller6.css">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet"></head><body>
<a class="skip" href="#inicio">Saltar al contenido</a><header class="topbar"><div class="header-inner"><a class="brand" href="../"><img src="../Logo_UTFSM.png" alt="Escudo UTFSM">Econometría ICS-294</a></div><nav class="header-tabs"><div><a href="../">Inicio</a>'''+nav+'''<a href="#inicio" aria-current="page">Clase 6</a></div></nav></header>
<div class="course-layout"><aside class="class-sidebar"><p class="sidebar-title">Clases del taller</p><nav><a href="../">Menú del curso</a><a href="../clase-1-taller/">Clase 1 · Computación estadística en R</a><a href="../clase-2-taller/">Clase 2 · Regresión lineal simple</a><a href="../clase-3-taller/">Clase 3 · Causalidad y variable omitida</a><a href="../clase-4-taller/">Clase 4 · Regresión lineal múltiple</a><a href="#inicio" aria-current="page">Clase 6 · Interpretación de modelos</a></nav></aside><main id="inicio"><div class="hero"><h1>Clase 6 · Interpretación de modelos en R</h1><div class="session-meta"><span>Taller presencial</span><span>110 minutos</span><span>Wooldridge · wage1</span></div>
<p>Escribe, ejecuta e interpreta. Trabajaremos con logaritmos, experiencia al cuadrado, interacciones y cambios de unidades, en el orden de la cátedra.</p>
<div class="downloads"><a href="clase-taller-6.ipynb" download>Descargar notebook R</a> <a href="clase-taller-6.R" download>Descargar código R</a> <a href="https://colab.research.google.com/github/IvanRenatoC/UTFSM-econometria/blob/main/clase-6-taller/clase-taller-6.ipynb">Abrir notebook en Colab</a></div>
<p>En Colab, elige R en Tipo de entorno de ejecución. La primera celda carga la base. Página y notebook comparten los mismos ejemplos, ejercicios y soluciones.</p>
<h2>Agenda e índice</h2><p>Los minutos se cuentan desde el comienzo del taller. Reserva el tiempo de cada bloque para escribir código y conversar sobre sus resultados.</p><ol class="agenda">'''+toc+'''</ol><p><a href="'''+C['fuente']+'''">Cátedra 6 de referencia</a> · <a href="https://justinmshea.github.io/wooldridge/reference/wage1.html">Documentación de wage1</a></p></div><div class="content">'''+''.join(parts)+'''<footer><p>Para practicar, cambia educ por tenure en los modelos logarítmicos y explica las unidades de cada pendiente.</p><p><a href="https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html">Ayuda oficial de lm()</a> · <a href="https://stat.ethz.ch/R-manual/R-devel/library/stats/html/predict.lm.html">Ayuda oficial de predict()</a> · <a href="../">Volver al menú</a></p></footer></div></main></div><script src="interactivos.js"></script></body></html>'''
(ROOT/'index.html').write_text('\n'.join(line.rstrip() for line in page.splitlines())+'\n')
