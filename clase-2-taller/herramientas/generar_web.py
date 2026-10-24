"""Construye la plantilla web de clase 2 y sincroniza el notebook y las guías."""
from pathlib import Path
import json, csv
from html import escape as e
from hashlib import sha256
from generar_taller import generar, ROOT
from preparacion_colab import render_preparacion

contenido = generar()
# Estructura gráfica copiada de la clase 1; recursos institucionales compartidos.
css = (ROOT / 'herramientas/estructura-base.css').read_text()
js = (ROOT / 'herramientas/presentacion-base.js').read_text()
shared = ROOT.parent
version_css = sha256((shared / 'identidad-utfsm.css').read_bytes()).hexdigest()[:12]
version_js = sha256((shared / 'navegacion-utfsm.js').read_bytes()).hexdigest()[:12]
interactive_js = (ROOT / 'herramientas/interactivos.js').read_text()
rows = list(csv.DictReader((ROOT / 'datos/wage1.csv').open()))
data_json = json.dumps([{k:float(r[k]) for k in ('wage','educ','exper','numdep')} for r in rows], separators=(',',':'))
agenda = '<section id="agenda"><h2>Agenda y tabla de contenidos</h2><table class="agenda"><thead><tr><th>Horario</th><th>Actividad</th></tr></thead><tbody>'+''.join('<tr><td>'+e(h)+'</td><td>'+('<a href="#'+e(i)+'">'+e(t)+'</a>' if i else e(t))+'</td></tr>' for h,t,i in contenido['agenda'])+'</tbody></table><p>140 minutos de trabajo y 15 minutos de descanso. Predice, ejecuta en R y explica con tus palabras.</p></section>'
sections = []
links = []
for bloque in contenido['bloques']:
    cards = []
    links.append('<a href="#'+e(bloque['id'])+'">'+e(bloque['etiqueta'])+' · '+e(bloque['titulo'])+'</a>')
    for a in bloque['laminas']:
        n = int(a['id'].split('-')[1])
        widget = '<div class="lab" data-kind="'+e(a['interactivo'])+'"></div>' if a.get('interactivo') else ''
        links.append('<a href="#'+e(a['id'])+'">'+str(n).zfill(2)+' · '+e(a['titulo'])+'</a>')
        cards.append(f'''<article class="slide" id="{e(a['id'])}" data-title="{e(a['titulo'])}"><header class="slide-head"><h3><button class="slide-toggle" type="button" aria-expanded="false" aria-controls="body-{e(a['id'])}"><span class="slide-chevron" aria-hidden="true">▶</span><span>{e(a['titulo'])}</span></button></h3><span class="number">LÁMINA {n:02d}</span></header><div class="slide-body" id="body-{e(a['id'])}" hidden><p>{e(a['texto'])}</p>{widget}<div class="reading"><h4>Cómo leer el resultado</h4><p>{e(a['lectura'])}</p></div><details class="solution"><summary>Ver código y solución en R</summary><div class="solution-body"><div class="code-head"><span>R</span><button type="button" class="copy">Copiar código</button></div><pre><code>{e(a['codigo'])}</code></pre><p>{e(a['lectura'])}</p></div></details></div></article>''')
    sections.append(f'''<section class="chapter" id="{e(bloque['id'])}"><div class="chapter-intro"><p class="eyebrow">{e(bloque['etiqueta'])}</p><h2>{e(bloque['titulo'])}</h2></div>{''.join(cards)}</section>''')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(contenido['titulo'])} · UTFSM</title><style>{css}
.lab {{border:1px solid #b8c8d8;border-radius:12px;padding:16px;margin:20px 0;background:var(--paper,transparent)}}
@keyframes trazar {{from {{stroke-dashoffset:1000}} to {{stroke-dashoffset:0}}}} .fitted-line {{stroke-dasharray:1000;animation:trazar 1.2s ease-out both}} @media (prefers-reduced-motion:reduce) {{.fitted-line {{animation:none}}}} .lab svg {{width:100%;height:auto;display:block}} .lab-controls {{display:flex;flex-wrap:wrap;gap:10px;align-items:center}} .lab-controls button {{padding:10px;border:1px solid #005e90;border-radius:6px;cursor:pointer;background:#1b2a5e;color:white}} .lab-controls button[aria-pressed="true"] {{background:#d6a600;color:#111}} .lab-controls label {{display:flex;gap:6px;align-items:center}} .lab-result {{font-variant-numeric:tabular-nums}} .agenda {{border-collapse:collapse;width:100%;margin:20px 0}} .agenda td,.agenda th {{text-align:left;padding:12px;border-bottom:1px solid #aab6c6}} .reading {{border-left:4px solid #d6a600;padding:4px 16px;margin:16px 0}}
</style><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="../identidad-utfsm.css?v={version_css}"></head><body><a class="skip" href="#contenido">Saltar al contenido</a>
<header class="topbar"><div class="header-inner"><a class="brand" href="#inicio"><img src="../Logo_UTFSM.png" width="36" height="36" alt="Escudo de la Universidad Técnica Federico Santa María"><span>Econometría ICS-294</span></a><div class="header-actions"><button id="theme-toggle" class="theme-toggle" type="button" aria-label="Cambiar a modo oscuro" aria-pressed="false">◐</button><div class="search-wrap"><label class="search-label" for="class-search"><input id="class-search" type="search" placeholder="Búsqueda" aria-label="Buscar en las láminas" aria-controls="search-results" autocomplete="off"></label><div id="search-results" role="region" aria-label="Resultados de búsqueda" hidden></div></div><button id="present" type="button" aria-pressed="false">Modo presentación</button></div></div><nav class="header-tabs" aria-label="Navegación principal"><div><a href="../">Home</a><a href="../#clases">Clases</a><a href="../clase-1-taller/">Clase 1</a><a href="#inicio" aria-current="page">Clase 2</a></div></nav></header>
<div class="page-layout"><aside class="class-sidebar"><nav aria-label="Clases"><p class="sidebar-title">Clases</p><a href="../clase-1-taller/">Clase 1 · Computación estadística en R</a><a href="#inicio" class="current" aria-current="page">Clase 2 · Regresión lineal simple en R</a></nav></aside><main id="contenido"><div class="hero" id="inicio"><h1>{e(contenido['titulo'])}</h1><div class="session-meta"><span>Taller presencial · {e(contenido['docente'])}</span><span class="tag-gold">18:50–21:25 · Descanso 20:00–20:15</span></div><section class="official-info"><h2>Contenido del taller</h2><div><p>{e(contenido['estado'])}</p><p>Anticipa la tendencia, ajusta la recta e interpreta sus resultados. Los gráficos interactivos usan las mismas 526 observaciones que el código R. Las animaciones ilustran el ajuste; los controles no modifican los datos.</p></div></section><div class="downloads"><a href="clase-taller-2.ipynb" download>Descargar notebook R ↓</a><a href="clase-taller-2.R" download>Script R ↓</a><a href="guia-docente-taller-2.md">Guía docente ↗</a></div></div><div class="content">{agenda}{render_preparacion(ROOT)}{''.join(sections)}<footer class="footer"><p>{e(contenido['docente'])} · Taller de Econometría ICS-294 · UTFSM</p><p>Fuentes: <a href="https://hizocar.github.io/econometria-usm/clases/clase2/">Cátedra 2</a> · <a href="https://justinmshea.github.io/wooldridge/reference/wage1.html">Wooldridge · wage1</a></p><p><a href="README.md">Guía del material</a> · <a href="instruccion-clase-taller-2.md">Instrucciones de desarrollo</a></p></footer></div></main><aside class="contents-sidebar"><nav aria-label="Tabla de contenidos"><p class="sidebar-title">Tabla de contenidos</p><a href="#preparar-colab">Preparación de Colab</a>{''.join(links)}</nav></aside></div>
<nav class="present-controls" aria-label="Navegación de láminas"><button id="prev" type="button">← Anterior</button><span class="counter" aria-live="polite"></span><button id="next" type="button">Siguiente →</button></nav><script>window.datosTaller={data_json};</script><script>{interactive_js}</script><script>{js}</script><script src="../navegacion-utfsm.js?v={version_js}"></script></body></html>'''
(ROOT / 'index.html').write_text(html)
print('Clase 2: web, notebook, script y guía sincronizados.')
