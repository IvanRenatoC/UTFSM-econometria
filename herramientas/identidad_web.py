"""Aplica la identidad visual del taller a la página generada, sin alterar actividades."""
from html import escape
import re
from pathlib import Path
from hashlib import sha256

def animacion_vector():
    cells = ''.join(f'<span class="vector-cell"><span class="vector-dot" aria-hidden="true"></span></span>' for i in range(1, 7))
    return f'''<figure class="vector-demo" aria-labelledby="vector-caption">
<figcaption id="vector-caption"><strong>Un vector, posición a posición</strong><span>Los puntos aparecen en orden: de izquierda a derecha y de arriba abajo.</span></figcaption>
<div class="vector-figures" role="img" aria-label="A es una fila de seis casillas. Su transpuesta A T es una columna de seis casillas. Ambas se llenan en el mismo orden con puntos azules.">
<div class="vector-equation vector-horizontal"><span class="vector-symbol">A =</span><div class="vector-grid">{cells}</div></div>
<div class="vector-equation vector-vertical"><span class="vector-symbol">A<sup>T</sup> =</span><div class="vector-grid">{cells}</div></div>
</div><div class="vector-controls"><button type="button" class="vector-pause" aria-pressed="false">Pausar animación</button><button type="button" class="vector-replay">Reiniciar</button></div>
<p class="vector-note">Cada casilla representa una posición. La transposición cambia la orientación y conserva el orden de los elementos. En R, un vector simple no tiene dimensión de fila o columna; aquí usamos ambas orientaciones como representación visual.</p></figure>'''

def animacion_matriz():
    def grid(rows, columns, transpose=False):
        cells = []
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                step = (j - 1) * 4 + i if transpose else (i - 1) * 4 + j
                cells.append(f'<span class="matrix-cell" title="Fila {i}, columna {j}"><span class="matrix-dot matrix-step-{step}" data-step="{step}" aria-hidden="true"></span></span>')
        return f'<div class="matrix-grid" style="--matrix-columns:{columns}">{"".join(cells)}</div>'
    return f'''<figure class="vector-demo matrix-demo" aria-labelledby="matrix-caption">
<figcaption id="matrix-caption"><strong>Una matriz y su transpuesta, posición a posición</strong><span>A tiene 6 filas y 4 columnas; A<sup>T</sup> tiene 4 filas y 6 columnas.</span></figcaption>
<div class="matrix-figures" role="img" aria-label="Matriz A de seis filas por cuatro columnas y su transpuesta de cuatro filas por seis columnas. Cada punto de A en la fila i, columna j aparece al mismo tiempo en la fila j, columna i de la transpuesta.">
<div class="matrix-equation"><span class="vector-symbol">A =</span><div>{grid(6, 4)}<p class="matrix-dim">6 × 4</p></div></div>
<div class="matrix-equation"><span class="vector-symbol">A<sup>T</sup> =</span><div>{grid(4, 6, True)}<p class="matrix-dim">4 × 6</p></div></div>
</div><div class="vector-controls"><button type="button" class="vector-pause" aria-pressed="false">Pausar animación</button><button type="button" class="vector-replay">Reiniciar</button></div>
<p class="vector-note">Llenamos A por filas, de izquierda a derecha. Cada posición A[i, j] se refleja en A<sup>T</sup>[j, i]: las filas se convierten en columnas. Ambas matrices contienen 24 posiciones. Este recorrido ilustra un llenado por filas con ciclos anidados; la función matrix() de R llena por columnas de forma predeterminada.</p></figure>'''

def animacion_escalera():
    return '''<figure class="vector-demo staircase-demo" aria-labelledby="stair-caption">
<figcaption id="stair-caption"><strong>Repetir el recorrido hasta encontrar la salida</strong><span>La persona baja dos veces: al terminar la primera vuelve arriba; al terminar la segunda aparece la salida.</span></figcaption>
<svg class="stair-scene" viewBox="0 0 560 370" role="img" aria-labelledby="stair-title stair-description">
<title id="stair-title">Dos descensos por una escalera</title><desc id="stair-description">Una persona baja seis escalones, desaparece al llegar abajo y reaparece arriba. Baja una segunda vez y se detiene junto a un letrero que dice salida.</desc>
<rect x="1" y="1" width="558" height="368" rx="12" fill="#f5f7fc"/>
<path d="M60 100 H130 V135 H175 V170 H220 V205 H265 V240 H310 V275 H355 V310 H510 V335 H60 Z" fill="#e7ecf5"/>
<path d="M60 100 H130 V135 H175 V170 H220 V205 H265 V240 H310 V275 H355 V310 H510" fill="none" stroke="#1b2a5e" stroke-width="3" stroke-linejoin="round"/>
<text x="24" y="35" class="stair-label-first stair-animated">Recorrido 1 de 2</text><text x="24" y="35" class="stair-label-second stair-animated">Recorrido 2 de 2</text>
<g class="stair-person stair-animated" aria-hidden="true">
<circle cx="0" cy="-56" r="11" fill="#e9b48c"/><path d="M-11 -58 Q-8 -75 4 -68 Q13 -67 11 -56 L5 -61 L-8 -58 Z" fill="#10193b"/>
<path d="M-7 -42 L8 -42 L12 -23 L-6 -23 Z" fill="#1b2a5e"/>
<path d="M-4 -38 L-13 -26 L-19 -22 M6 -38 L16 -29 L24 -29" fill="none" stroke="#e9b48c" stroke-width="6" stroke-linecap="round"/>
<path d="M-3 -23 L-8 -12 L-14 -1 M7 -23 L16 -13 L25 -8" fill="none" stroke="#005f96" stroke-width="7" stroke-linecap="round"/>
<path d="M-16 0 H-7 M23 -7 H31" stroke="#10193b" stroke-width="5" stroke-linecap="round"/>
</g>
<g class="stair-exit stair-animated"><rect x="416" y="242" width="112" height="45" rx="6" fill="#1b2a5e"/><text x="472" y="271" text-anchor="middle" fill="white" font-size="23" font-weight="700">salida</text><path d="M472 287 V310" stroke="#1b2a5e" stroke-width="4"/></g>
</svg><div class="vector-controls"><button type="button" class="vector-pause" aria-pressed="false">Pausar animación</button><button type="button" class="vector-replay">Reiniciar</button></div>
<p class="vector-note">Cada recorrido representa una repetición. Al finalizar el segundo se alcanza la condición de salida y la escena se detiene. Reinicia para observar los dos descensos otra vez.</p></figure>'''

def aplicar_identidad(html, activities):
    nav_left='''<aside class="class-sidebar" aria-label="Temario de talleres"><nav><p class="sidebar-title">Clases</p><a class="classes-home" href="#inicio">🏫 Clases</a><a class="current" href="#inicio" aria-current="page">Clase 1: Introducción a la computación estadística usando R</a><a href="#clase-2">Clase 2: Regresión lineal simple en R</a></nav></aside>'''
    toc=['<aside class="contents-sidebar" aria-label="Tabla de contenidos"><nav><p class="sidebar-title">Tabla de contenidos</p><a href="#objetivos">🎯 Objetivos de la sesión</a><a href="#agenda">🗓️ Agenda del taller (18:50–21:25)</a>']
    groups=[('NIV','Nivelación · Computación en R'),('P1','Parte 1 · Introducción a la econometría'),('P2','Ayudantía · Repaso de estadística descriptiva en R'),('P3','Parte 3 · Estadística inferencial')]
    for prefix,label in groups:
        toc.append(f'<a class="toc-group" href="#{prefix}">{label}</a><ul>')
        for a in activities:
            if a['id'].startswith(prefix+'-'):
                toc.append(f'<li><a href="#{a["id"]}">{escape(a["title"])}</a></li>')
        toc.append('</ul>')
    toc.append('<a href="#cierre">✅ Autoevaluación</a><a href="#clase-2">📚 Para la próxima clase</a></nav></aside>')
    header='''<header class="topbar"><div class="header-inner"><a class="brand" href="#inicio"><img src="Logo_UTFSM.png" width="36" height="36" alt="Escudo de la Universidad Técnica Federico Santa María"><span>Econometría ICS-294</span></a><div class="header-actions"><button id="theme-toggle" class="theme-toggle" type="button" aria-label="Cambiar a modo oscuro" aria-pressed="false">◐</button><div class="search-wrap"><label class="search-label" for="class-search"><span aria-hidden="true">⌕</span><input id="class-search" type="search" placeholder="Búsqueda" aria-label="Buscar en las láminas" aria-controls="search-results" autocomplete="off"></label><div id="search-results" role="region" aria-label="Resultados de búsqueda" hidden></div></div><button id="present" type="button" aria-pressed="false">Modo presentación</button></div></div><nav class="header-tabs" aria-label="Navegación principal"><div><a href="#inicio">Home</a><a href="https://hizocar.github.io/econometria-usm/programa/">Programa</a><a href="#agenda">Calendario</a><a href="#inicio" aria-current="page">Clases</a></div></nav></header>'''
    hero='''<div class="hero" id="inicio"><h1>Clase 1 · Introducción a la computación estadística usando R</h1><div class="session-meta"><span>📅 Lunes · Taller presencial</span><span>⏱️ 18:50 – 21:25</span><span class="tag-gold">Semana 1 · Computación en R y repaso de estadística</span></div><section class="official-info" aria-labelledby="contenido-semana"><h2 id="contenido-semana"><span class="info-icon" aria-hidden="true">i</span> Contenido del taller de la semana</h2><div><p>Acá se desarrolla el taller de la cátedra del día viernes 16, como apoyo al contenido visto por el profesor Sebastián. El taller está a mi cargo, Iván Canales y la idea es que vayamos desarrollando la clase en conjunto.</p><p>Antes de comenzar, una pregunta: ¿qué tan familiarizados están con la programación?</p><p>Primero es necesaria una nivelación en R con vectores, condicionales, ciclos, sucesiones y matrices. <strong>Después:</strong> introducción a la econometría y muestreo, estadística descriptiva e inferencia con datos transversales del libro Wooldridge. Las soluciones aparecen plegadas para que intentes resolver cada actividad primero; el <a href="clase-taller-1.ipynb" download>notebook de R</a> conserva la misma secuencia.</p></div></section><section id="objetivos" class="objectives"><h2>🎯 Objetivos de la sesión</h2><p><strong>Nivelación de computación en R</strong></p><ul><li>Usar sentencias clave como <code>if</code>, <code>else</code>, <code>while</code> y <code>for</code>, para hacer rutinas.</li><li>Crear y modificar <strong>vectores y matrices</strong>, utilizando índices y preasignación.</li></ul><p><strong>Aplicación de la materia de cátedra</strong></p><ul><li>Reconocer datos de <strong>corte transversal</strong> y practicar métodos de muestreo.</li><li>Calcular e interpretar medidas de localización y dispersión, histogramas y gráficos de caja.</li><li>Explorar el <strong>TCL</strong> e intervalos de confianza para medias, proporciones y diferencias de medias mediante simulaciones en R.</li><li>Distinguir una descripción o diferencia estadística de una conclusión <strong>causal</strong>.</li></ul></section><div class="downloads"><a href="clase-taller-1.ipynb" download>Descargar notebook R ↓</a><a href="clase-taller-1.R" download>Script para RStudio ↓</a><a href="guia-docente-taller-1.md">Guía docente ↗</a></div></div>'''
    html=re.sub(r'<header class="topbar">.*?</header>',header,html,count=1,flags=re.S)
    html=re.sub(r'<div class="hero" id="inicio">.*?<div class="content">',hero+'<div class="content">',html,count=1,flags=re.S)
    html=re.sub(r'<section class="brief"><h2>Cómo trabajar esta clase</h2>.*?</section>','',html,count=1,flags=re.S)
    html=html.replace('<details class="brief"><summary>Agenda · 140 minutos de trabajo</summary>','<section class="brief agenda" id="agenda"><h2>🗓️ Agenda del taller (18:50 – 21:25)</h2><p>140 minutos efectivos de trabajo y una pausa de 15 minutos.</p>')
    html=html.replace('</table></details>','</table></section>',1)
    html=html.replace('<main id="contenido">','<div class="page-layout">'+nav_left+'<main id="contenido">',1)
    html=html.replace('</main>','</main>'+''.join(toc)+'</div>',1)
    html=html.replace('<footer class="footer">','<section class="next-class" id="clase-2"><h2>📚 Para la próxima clase</h2><p><strong>Clase 2: Regresión lineal simple en R.</strong></p><p>Continúa con la lectura indicada por Sebastián: capítulo 1 y apéndice C de Wooldridge. El material del segundo taller se incorporará cuando esté preparado.</p></section><footer class="footer">',1)
    html=html.replace('<title>Taller 1 · Econometría en R · UTFSM</title>','<title>Clase 1 · Computación estadística en R · Econometría ICS-294</title>')
    html=html.replace('</head>','<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="identidad-utfsm.css"></head>')
    html=html.replace('</body>','<script src="navegacion-utfsm.js"></script></body>')
    html = re.sub(r'(<article class="slide" id="NIV-02".*?<p class="question">.*?</p>)', lambda match: match.group(1) + animacion_vector(), html, count=1, flags=re.S)
    html = re.sub(r'(<article class="slide" id="NIV-07".*?<p class="question">.*?</p>)', lambda match: match.group(1) + animacion_matriz(), html, count=1, flags=re.S)
    html = re.sub(r'(<article class="slide" id="NIV-06".*?<p class="question">.*?</p>)', lambda match: match.group(1) + animacion_escalera(), html, count=1, flags=re.S)
    if not any(a['id'] == 'NIV-04' for a in activities):
        html = html.replace('<article class="slide" id="NIV-02"', '<span id="NIV-04" aria-hidden="true"></span><article class="slide" id="NIV-02"', 1)
    # Cambia la URL cuando cambia el recurso para evitar estilos o controles antiguos en caché.
    root = Path(__file__).resolve().parent.parent
    for asset in ('identidad-utfsm.css', 'navegacion-utfsm.js'):
        version = sha256((root / asset).read_bytes()).hexdigest()[:12]
        html = html.replace(f'"{asset}"', f'"{asset}?v={version}"')
    return html
