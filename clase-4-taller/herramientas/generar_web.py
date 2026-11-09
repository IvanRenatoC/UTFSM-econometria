"""Genera web, notebook R, script y guía desde una fuente común verificada en R."""
import json, hashlib, html, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
C=json.loads((ROOT/'contenido-clase-4.json').read_text())
V=json.loads((ROOT/'datos/verificacion.json').read_text())
code='\n\n'.join(a['id']+'\n'+a['codigo'] for a in C['laminas'])
assert hashlib.sha256(code.encode()).hexdigest()==V['codigo_sha256'],'Ejecutar verificar_en_R.mjs antes de generar.'
O=json.loads((ROOT/'datos/salidas-verificadas-r.json').read_text())
e=html.escape
M={
'C4-05':'<mrow><mover><mi>wage</mi><mo>^</mo></mover><mo>=</mo><msub><mover><mi>β</mi><mo>^</mo></mover><mn>0</mn></msub><mo>+</mo><msub><mover><mi>β</mi><mo>^</mo></mover><mn>1</mn></msub><mi>educ</mi><mo>+</mo><msub><mover><mi>β</mi><mo>^</mo></mover><mn>2</mn></msub><mi>IQ</mi></mrow>',
'C4-08':'<mrow><mi>SSR</mi><mo>=</mo><munder><mo>∑</mo><mi>i</mi></munder><msup><mrow><mo>(</mo><msub><mi>y</mi><mi>i</mi></msub><mo>−</mo><msub><mover><mi>y</mi><mo>^</mo></mover><mi>i</mi></msub><mo>)</mo></mrow><mn>2</mn></msup></mrow>',
'C4-09':'<mrow><mi>y</mi><mo>=</mo><mi>Xβ</mi><mo>+</mo><mi>u</mi><mspace width="1em"/><mtext>X: n × (k + 1); β: (k + 1) × 1</mtext></mrow>',
'C4-10':'<mrow><msub><mrow><mo>(</mo><msup><mi>X</mi><mi>T</mi></msup><mi>X</mi><mo>)</mo></mrow><mn>23</mn></msub><mo>=</mo><munder><mo>∑</mo><mi>i</mi></munder><msub><mi>x</mi><mi>i1</mi></msub><msub><mi>x</mi><mi>i2</mi></msub></mrow>',
'C4-11':'<mrow><mover><mi>β</mi><mo>^</mo></mover><mo>=</mo><msup><mrow><mo>(</mo><msup><mi>X</mi><mi>T</mi></msup><mi>X</mi><mo>)</mo></mrow><mn>−1</mn></msup><msup><mi>X</mi><mi>T</mi></msup><mi>y</mi></mrow>',
'C4-12':'<mrow><msup><mi>X</mi><mi>T</mi></msup><mover><mi>u</mi><mo>^</mo></mover><mo>=</mo><mn>0</mn><mspace width="2em"/><mover><mi>y</mi><mo>¯</mo></mover><mo>=</mo><mover><mover><mi>y</mi><mo>^</mo></mover><mo>¯</mo></mover></mrow>',
'C4-14':'<mrow><msup><mi>R</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>−</mo><mfrac><mi>SSR</mi><mi>SST</mi></mfrac><mspace width="2em"/><mover><msup><mi>R</mi><mn>2</mn></msup><mo>¯</mo></mover><mo>=</mo><mn>1</mn><mo>−</mo><mfrac><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>−</mo><mi>k</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mfrac><mi>SSR</mi><mi>SST</mi></mfrac></mrow>',
'C4-18':'<mrow><msub><mi>C</mi><mi>ij</mi></msub><mo>=</mo><msup><mrow><mo>(</mo><mn>−1</mn><mo>)</mo></mrow><mrow><mi>i</mi><mo>+</mo><mi>j</mi></mrow></msup><mi>det</mi><mo>(</mo><msub><mi>A</mi><mrow><mo>−</mo><mi>i</mi><mo>,</mo><mo>−</mo><mi>j</mi></mrow></msub><mo>)</mo></mrow>',
'C4-19':'<mrow><msup><mi>A</mi><mn>−1</mn></msup><mo>=</mo><mfrac><msup><mi>C</mi><mi>T</mi></msup><mrow><mi>det</mi><mo>(</mo><mi>A</mi><mo>)</mo></mrow></mfrac></mrow>'}

M['C4-01']='<mtable><mtr><mtd><mover><mi>Y</mi><mo>^</mo></mover><mo>=</mo><mi>X</mi><mover><mi>β</mi><mo>^</mo></mover></mtd></mtr><mtr><mtd><msub><mover><mi>Y</mi><mo>^</mo></mover><mi>i</mi></msub><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>p</mi></munderover><msub><mover><mi>β</mi><mo>^</mo></mover><mi>j</mi></msub><msub><mi>X</mi><mi>ij</mi></msub></mtd></mtr></mtable>'
M['C4-04']='<mtable><mtr><mtd>' +M['C4-05']+'</mtd></mtr><mtr><mtd><mrow><mi>Y</mi><mo>=</mo><mi>Ŷ</mi><mo>+</mo><mi>û</mi><mspace width="2em"/><mi>Ŷ</mi><mo>=</mo><mi>X</mi><mi>β̂</mi></mrow></mtd></mtr></mtable>'

# Notebook, Markdown y script comparten el orden y el código exacto de las láminas.
cells=[]; guide=[]; script=['# Clase 4: ejecutar desde clase-4-taller/ o con kernel R en Colab.']
def md(text,id):
 cells.append(dict(cell_type='markdown',id=id,metadata={},source=(text+'\n').splitlines(True)));guide.append(text)
def rc(text,id,guardar_script=True):
 cells.append(dict(cell_type='code',id=id,metadata={},source=(text+'\n').splitlines(True),execution_count=None,outputs=[]))
 if guardar_script:script.append(text)
 guide.append('```r\n'+text+'\n```')
md('# '+C['titulo']+'\n\nEjecuta en orden con kernel R. En Google Colab selecciona R como tipo de entorno. No uses rpy2 ni %%R.\n\n[Clase teórica de referencia]('+C['fuente']+')','inicio')
md('## Agenda\n\n| Horario | Actividad |\n|---|---|\n'+'\n'.join('| '+h+' | '+t+' |' for h,t,_ in C['agenda']),'agenda')
for a in C['laminas']:
 id=a['id'].lower();md('## '+a['id'].split('-')[1]+' · '+a['titulo']+'\n\n'+a['texto'],id+'-intro')
 if a.get('solo_tabla'):
  rc(a['codigo'],id+'-r')
  md('```text\n'+O[a['id']]+'\n```',id+'-salida')
  continue
 if a['formula']:md('$$'+a['formula']+'$$',id+'-formula')
 if a.get('carga_ejercicio'):
  rc(a['carga_ejercicio'],id+'-carga',guardar_script=False)
  md(a['descripcion_base'],id+'-base')
 if a.get('campos'):
  md('| Campo | Significado |\n|---|---|\n'+'\n'.join('| `'+k+'` | '+v+' |' for k,v in a['campos'])+'\n\n[Documentación del conjunto de datos]('+a['fuente_campos']+')',id+'-campos')
 if a.get('codigo_primero'):rc(a['codigo'],id+'-r')
 if a.get('conceptos'):
  md('### Vectores y notación\n\n'+'\n'.join('- **'+k+'**. '+v for k,v in a['conceptos']),id+'-conceptos')
 if a['codigo'] and not a.get('codigo_primero'):md('### En R · Tu turno',id+'-turno')
 if a['pasos']:md('### El código, paso a paso\n\n'+'\n\n'.join('**`'+line+'`**\n\n'+desc for line,desc in a['pasos']),id+'-pasos')
 if a['codigo'] and not a.get('codigo_primero'):rc(a['codigo'],id+'-r')
 if a.get('consignas'):
  md('### Actividades\n\n'+'\n'.join(f'{i}. {t}' for i,t in enumerate(a['consignas'],1)),id+'-actividades')
 md(('### Mensaje final' if a.get('consignas') else '### Cómo leer el resultado')+'\n\n'+a['lectura'],id+'-lectura')
 if a['codigo']:md('<details><summary>Resultados de referencia ejecutados en R</summary>\n\n```text\n'+O[a['id']]+'\n```\n\n</details>',id+'-salida')
 if a['pregunta']:md('### Comprueba lo aprendido\n\n'+a['pregunta']+'\n\n<details><summary>Mostrar respuesta</summary>\n\n'+a['respuesta']+'\n\n</details>',id+'-pregunta')
nb=dict(cells=cells,metadata=dict(kernelspec=dict(display_name='R',language='R',name='ir'),language_info=dict(name='R',file_extension='.r',mimetype='text/x-r-source')),nbformat=4,nbformat_minor=5)
(ROOT/'clase-taller-4.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n')
(ROOT/'clase-taller-4.R').write_text('\n\n'.join(script)+'\n')
(ROOT/'guia-docente-taller-4.md').write_text('\n'.join(line.rstrip() for line in '\n\n'.join(guide).splitlines())+'\n')
# Mantiene el mismo diseño institucional y las mismas convenciones de navegación.
old=(ROOT.parent/'clase-3-taller/index.html').read_text()
style=old.split('<style>',1)[1].split('</style>',1)[0]
css=(ROOT/'herramientas/taller4.css').read_text()
head=old[old.index('<header class="topbar">'):old.index('<main id="contenido">')]
head=head.replace('href="#inicio" aria-current="page">Clase 3','href="../clase-3-taller/">Clase 3').replace('href="#inicio" class="current" aria-current="page">Clase 3','href="../clase-3-taller/">Clase 3')
head=head.replace('</div></nav></header>','<a href="#inicio" aria-current="page">Clase 4</a></div></nav></header>')
head=head.replace('</nav></aside>','<a href="#inicio" class="current" aria-current="page">Clase 4 · Regresión lineal múltiple en R</a></nav></aside>')
sections=[]
for tid,title,lo,hi in C['temas']:
 cards=[]
 for a in C['laminas'][lo-1:hi]:
  id=a['id'];steps=''.join('<details class="step"><summary><code>'+e(line)+'</code></summary><p>'+e(desc)+'</p></details>' for line,desc in a['pasos'])
  formula='<div class="formula"><math display="block">'+M[id]+'</math></div>' if id in M else ''
  widget='<section class="lab" data-kind="'+a['interactivo']+'" aria-label="Ejemplo interactivo: '+e(a['titulo'])+'"></section>' if a['interactivo'] else ''
  conceptos=''
  if a.get('conceptos'):
   conceptos='<h4>Vectores y notación</h4><dl>'+''.join('<dt><strong>'+e(k)+'</strong></dt><dd>'+e(v)+'</dd>' for k,v in a['conceptos'])+'</dl>'
  campos=''
  if a.get('campos'):
   campos='<div class="table-wrap"><table class="agenda"><thead><tr><th>Campo</th><th>Significado</th></tr></thead><tbody>'+''.join('<tr><th scope="row"><code>'+e(k)+'</code></th><td>'+e(v)+'</td></tr>' for k,v in a['campos'])+'</tbody></table></div><p><a href="'+e(a['fuente_campos'])+'">Documentación del conjunto de datos</a></p>'
  code_block='<div class="solution-body"><div class="code-head"><span>R · Ejecutar en orden</span><button class="copy" type="button">Copiar código</button></div><pre><code>'+e(a['codigo'])+'</code></pre></div>'
  exercise=''
  output=''
  if a['codigo']:
   output='<details class="solution"'+(' open' if a.get('mostrar_salida') else '')+'><summary>Ver resultados de referencia en R</summary><div class="solution-body"><pre><code>'+e(O[id])+'</code></pre></div></details>'
   instructions='<h4>El código, paso a paso</h4><div class="code-explorer">'+steps+'</div>'
   if a.get('codigo_primero'):
    exercise='<h4>Código completo en R</h4>'+code_block+instructions
   else:
    exercise='<h4>En R · Tu turno</h4><p>Ejecuta las instrucciones en el notebook y compara tu resultado con la salida de referencia.</p>'+instructions+'<details class="solution"><summary>Ver código completo en R</summary>'+code_block+'</details>'
  figura=''
  if a.get('figura'):
   ruta=e(a['figura'])
   figura='<figure><a href="'+ruta+'"><img src="'+ruta+'" alt="Matriz de dispersión de los 17 campos de wage2" style="width:100%;height:auto"></a><figcaption><a href="'+ruta+'">Abrir la matriz a tamaño completo</a></figcaption></figure>'
  lectura_titulo='Cómo leer el resultado'
  quiz=''
  if a['pregunta']:
   quiz='<details class="solution"><summary>Comprueba lo aprendido</summary><div class="solution-body"><p>'+e(a['pregunta'])+'</p><details><summary>Mostrar respuesta</summary><p>'+e(a['respuesta'])+'</p></details></div></details>'
  if a.get('carga_ejercicio'):
   carga=code_block.replace('<code></code>', '<code>'+e(a['carga_ejercicio'])+'</code>')
   campos=carga+'<h4>La base gpa2</h4><p>'+e(a['descripcion_base'])+'</p>'+campos
   exercise='<h4>Actividades</h4><ol>'+''.join('<li>'+e(t)+'</li>' for t in a['consignas'])+'</ol>'
   lectura_titulo='Mensaje final'
  if a.get('solo_tabla'):
   exercise=''
   output=''
  lectura='<div class="reading"><h4>'+e(lectura_titulo)+'</h4><p>'+e(a['lectura'])+'</p></div>' if a['lectura'] else ''
  introduccion='<p>'+e(a['texto'])+'</p>' if a['texto'] else ''
  cards.append(f'''<article class="slide" id="{id}" data-title="{e(a['titulo'])}"><header class="slide-head"><h3><button class="slide-toggle" type="button" aria-expanded="false" aria-controls="body-{id}"><span class="slide-chevron" aria-hidden="true">▶</span><span>{e(a['titulo'])}</span></button></h3><span class="number">LÁMINA {id[-2:]}</span></header><div class="slide-body" id="body-{id}" hidden><p class="data-note">Tema {C['temas'].index([tid,title,lo,hi])+1} · Cátedra 4 · Aplicación en R</p>{introduccion}{formula}{widget}{conceptos}{campos}{figura}{exercise}{lectura}{output}{quiz}<p class="data-note"><a href="#{id}">Enlace a esta lámina ↗</a></p></div></article>''')
 sections.append('<section id="'+tid+'"><div class="chapter-intro"><p class="eyebrow">Tema '+str(len(sections)+1)+'</p><h2>'+e(title)+'</h2></div>'+''.join(cards)+'</section>')
agenda='<section id="agenda"><h2>Agenda y tabla de contenidos</h2><table class="agenda"><thead><tr><th>Horario</th><th>Actividad</th></tr></thead><tbody>'+''.join('<tr><td>'+h+'</td><td>'+('<a href="#'+id+'">'+e(t)+'</a>' if id else e(t))+'</td></tr>' for h,t,id in C['agenda'])+'</tbody></table><p>140 minutos de trabajo y 15 minutos de descanso.</p></section>'
links='<a href="#agenda">Agenda</a><a href="#objetivos">Objetivos y preparación</a>'+''.join('<a href="#'+a['id']+'">'+a['id'][-2:]+' · '+e(a['titulo'])+'</a>' for a in C['laminas'])
data=(ROOT/'datos/resultados-interactivos.json').read_text()
js=(ROOT/'herramientas/interactivos.js').read_text()
base=(ROOT/'herramientas/presentacion-base.js').read_text()
page=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Taller 4: regresión múltiple, matrices, selección de variables y R² ajustado. Código R y notebook sincronizados."><title>{e(C['titulo'])} · UTFSM</title><style>{style}\n{css}</style><link rel="stylesheet" href="../identidad-utfsm.css"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet"></head><body><a class="skip" href="#contenido">Saltar al contenido</a>{head}<main id="contenido"><div class="hero" id="inicio"><h1>{e(C['titulo'])}</h1><div class="session-meta"><span>Taller presencial · Econometría ICS-294</span><span class="tag-gold">18:50–21:25 · Descanso 20:00–20:15</span></div><section class="official-info"><h2>Contenido del taller</h2><div><p>Aplicamos en R la regresión lineal múltiple de la <a href="{C['fuente']}">cátedra 4</a>. Comparamos modelos sobre una muestra común y practicamos cómo leer ANOVA, coeficientes, correlaciones y medidas de ajuste.</p><p>Trabajamos con wage2 y el ejemplo numérico de cinco personas. Cerramos con un ejercicio en Colab usando gpa2. Predice, escribe código y explica lo observado. Las soluciones están plegadas; la web y el notebook contienen el mismo código.</p></div></section><div class="downloads"><a href="clase-taller-4.ipynb" download>Descargar notebook R ↓</a><a href="clase-taller-4.R" download>Script R ↓</a><a href="guia-docente-taller-4.md">Guía de la clase ↗</a><a href="contenido-clase-4-taller.pdf" download>Clase en PDF ↓</a></div></div><div class="content">{agenda}<section id="objetivos" class="brief"><h2>Antes de comenzar</h2><p>Abre el notebook con kernel R en Google Colab; no uses %%R ni rpy2. Ejecuta en orden. Si trabajas localmente, abre la carpeta clase-4-taller para encontrar datos/wage2.csv. <a href="../clase-1-taller/#preparar-colab">Preparar Colab paso a paso</a>.</p><h3>Objetivos de la sesión</h3><ul><li>Estimar una regresión múltiple e interpretar sus pendientes manteniendo constantes los demás regresores.</li><li>Construir X y reconocer las operaciones matriciales del ajuste.</li><li>Comparar R² y R² ajustado sobre una muestra común.</li><li>Interpretar ANOVA y summary(), y justificar una selección de regresores.</li></ul></section>{''.join(sections)}<footer class="footer"><p>Fuentes: <a href="{C['fuente']}">Cátedra 4</a> · <a href="https://justinmshea.github.io/wooldridge/reference/wage2.html">Wooldridge · wage2</a> · <a href="https://stat.ethz.ch/R-manual/R-devel/library/stats/html/model.matrix.html">model.matrix()</a> · <a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/solve.html">solve()</a></p><p><a href="README.md">Guía del material</a> · <a href="../">Menú del curso</a></p></footer></div></main><aside class="contents-sidebar"><nav aria-label="Tabla de contenidos"><p class="sidebar-title">Tabla de contenidos</p>{links}</nav></aside></div><nav class="present-controls" aria-label="Navegación de láminas"><button id="prev" type="button">← Anterior</button><span class="counter" aria-live="polite"></span><button id="next" type="button">Siguiente →</button></nav><script>window.datosC4={data};</script><script>{js}</script><script>{base}</script><script src="../navegacion-utfsm.js"></script></body></html>'''
(ROOT/'index.html').write_text('\n'.join(line.rstrip() for line in page.splitlines())+'\n')
print('Generadas',len(C['laminas']),'láminas, notebook R, script y guía sincronizados.')
