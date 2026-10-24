"""Gráficos SVG de frecuencias reales del CSV; sin dependencias de red."""
from pathlib import Path
from html import escape
from collections import Counter
import csv, math

PALETTE = ['#0160a0', '#e12523', '#f8c751', '#00875a']
LABELS = {'wage':'Salario por hora (USD de 1976)', 'educ':'Educación (años)', 'exper':'Experiencia potencial (años)', 'tenure':'Antigüedad con el empleador (años)', 'female':'Sexo registrado', 'married':'Estado civil registrado'}

def bars(variable, values):
    histogram = variable == 'wage'
    if histogram:
        counts = [sum(2*i <= v < 2*(i+1) for v in values) for i in range(13)]
        labels = [f'{2*i}–{2*(i+1)}' for i in range(13)]
    else:
        freq = Counter(int(v) for v in values)
        labels = list(range(min(freq), max(freq)+1))
        counts = [freq[k] for k in labels]
    maximum = math.ceil(max(counts)/20)*20
    left, top, width, height = 62, 28, 620, 260
    svg = [f'<svg class="wage-chart" viewBox="0 0 720 375" role="img" aria-labelledby="chart-title-{variable}"><title id="chart-title-{variable}">{"Histograma" if histogram else "Gráfico de barras"}: {LABELS[variable]}. Frecuencia de personas.</title>']
    for i in range(5):
        value = maximum*i/4; y = top+height-height*i/4
        svg.append(f'<line x1="{left}" y1="{y}" x2="{left+width}" y2="{y}" class="chart-grid"/><text x="{left-10}" y="{y+4}" text-anchor="end">{value:g}</text>')
    step = width/len(counts)
    for i, (label, count) in enumerate(zip(labels,counts)):
        h = height*count/maximum; x = left+i*step; y = top+height-h
        color = PALETTE[0] if histogram else PALETTE[{'educ':0,'exper':1,'tenure':3}[variable]]
        svg.append(f'<rect tabindex="0" x="{x:.2f}" y="{y:.2f}" width="{step if histogram else step*.76:.2f}" height="{h:.2f}" fill="{color}" stroke="white" stroke-width="1" aria-label="{escape(str(label))}: {count} personas"><title>{escape(str(label))}: {count} personas</title></rect>')
        if histogram or i%max(1, math.ceil(len(counts)/14)) == 0:
            svg.append(f'<text x="{x+step/2:.2f}" y="310" text-anchor="end" transform="rotate(-45 {x+step/2:.2f} 310)">{label}</text>')
    svg.append(f'<text x="{left+width/2}" y="365" text-anchor="middle">{LABELS[variable]}</text><text x="17" y="158" text-anchor="middle" transform="rotate(-90 17 158)">Frecuencia (personas)</text></svg>')
    return ''.join(svg), list(zip(labels,counts)), 'Histograma · intervalos de 2 USD por hora' if histogram else 'Barras · frecuencia para cada cantidad de años'

def pie(variable, values):
    counts = [values.count(0), values.count(1)]
    names = ['Hombre (0)', 'Mujer (1)'] if variable == 'female' else ['No casado/a (0)', 'Casado/a (1)']
    svg = [f'<svg class="wage-chart pie-chart" viewBox="0 0 520 330" role="img" aria-labelledby="chart-title-{variable}"><title id="chart-title-{variable}">Gráfico circular: {LABELS[variable]}.</title>']
    angle=-math.pi/2
    for i,count in enumerate(counts):
        end=angle+2*math.pi*count/len(values)
        x1,y1=260+125*math.cos(angle),155+125*math.sin(angle)
        x2,y2=260+125*math.cos(end),155+125*math.sin(end)
        color=PALETTE[0 if i==0 else 2]
        label=f'{names[i]}: {count} personas ({100*count/len(values):.1f} %)'
        svg.append(f'<path tabindex="0" d="M260 155 L{x1} {y1} A125 125 0 {int(end-angle>math.pi)} 1 {x2} {y2} Z" fill="{color}" stroke="white" stroke-width="3" aria-label="{label}"><title>{label}</title></path>')
        mid=(angle+end)/2; tx,ty=260+78*math.cos(mid),155+78*math.sin(mid)
        svg.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" class="pie-label" fill="{"white" if i==0 else "#10193b"}">{100*count/len(values):.1f} %</text>')
        angle=end
    svg.append('</svg>')
    legend=''.join(f'<span><i style="background:{PALETTE[0 if i==0 else 2]}"></i>{names[i]}: {counts[i]} personas</span>' for i in range(2))
    return ''.join(svg)+f'<div class="chart-legend">{legend}</div>',list(zip(names,counts)), 'Gráfico circular · proporción de cada categoría'

def explorer(root: Path):
    rows=list(csv.DictReader((root/'datos/wage1.csv').open()))
    controls=[]; panels=[]
    for variable in LABELS:
        values=[float(row[variable]) for row in rows]
        svg, frequencies, kind = pie(variable,values) if variable in ('female','married') else bars(variable,values)
        assert sum(count for _,count in frequencies)==526
        controls.append(f'<button type="button" class="chart-choice" data-variable="{variable}" aria-pressed="false" aria-controls="panel-{variable}">{variable}</button>')
        table=''.join(f'<tr><th scope="row">{escape(str(label))}</th><td>{count}</td><td>{100*count/526:.1f} %</td></tr>' for label,count in frequencies)
        panels.append(f'<section id="panel-{variable}" class="chart-panel" hidden aria-labelledby="heading-chart-{variable}"><h4 id="heading-chart-{variable}">{LABELS[variable]}</h4><p class="data-note">{kind} · 526 personas</p>{svg}<details class="check"><summary>Ver frecuencias del gráfico</summary><div class="chart-table-wrap"><table class="schedule"><thead><tr><th>{"Intervalo / categoría"}</th><th>Personas</th><th>Porcentaje</th></tr></thead><tbody>{table}</tbody></table></div></details></section>')
    return '<div class="wage-explorer"><p>Selecciona una variable para ver su distribución en las 526 personas de la base.</p><div class="chart-choices" role="group" aria-label="Variable del gráfico">'+''.join(controls)+'</div><p class="chart-status" role="status">Elige una de las seis variables.</p>'+''.join(panels)+'<p class="data-note">Fuente: datos/wage1.csv · wooldridge · CPS de Estados Unidos, 1976. Pasa el cursor o enfoca las barras y sectores para consultar sus frecuencias.</p></div>'


def scatter(root: Path):
    rows=list(csv.DictReader((root/'datos/wage1.csv').open()))
    svg=['<svg class="wage-chart scatter-chart" viewBox="0 0 720 430" role="img" aria-labelledby="scatter-title scatter-description"><title id="scatter-title">Educación y salario por género</title><desc id="scatter-description">526 personas: educación en el eje horizontal y salario por hora en el vertical. Azul para hombres y amarillo para mujeres. La nube tiende a subir, con dispersión y superposición entre los grupos.</desc>']
    for y in range(0,26,5):
        py=360-y/26*310
        svg.append(f'<line class="chart-grid" x1="65" y1="{py}" x2="690" y2="{py}"/><text x="53" y="{py+4}" text-anchor="end">{y}</text>')
    for x in range(0,21,2):
        px=65+x/20*625
        svg.append(f'<text x="{px}" y="385" text-anchor="middle">{x}</text>')
    for row in rows:
        educ,wage=float(row['educ']),float(row['wage']); female=int(row['female'])
        label=f'{"Mujer" if female else "Hombre"}: {educ:g} años de educación; {wage:.2f} USD por hora'
        svg.append(f'<circle cx="{65+educ/20*625:.2f}" cy="{360-wage/26*310:.2f}" r="4" fill="{PALETTE[0 if female == 0 else 2]}" fill-opacity="0.5"><title>{label}</title></circle>')
    svg.append('<text x="377" y="418" text-anchor="middle">Educación (años)</text><text x="18" y="205" text-anchor="middle" transform="rotate(-90 18 205)">Salario por hora (USD de 1976)</text></svg>')
    return '<h4>Educación y salario por género</h4>'+''.join(svg)+'<div class="chart-legend"><span><i style="background:#0160a0"></i>Hombre (female = 0)</span><span><i style="background:#f8c751"></i>Mujer (female = 1)</span></div><p class="data-note">526 personas · wage1 · CPS de Estados Unidos, 1976. Los puntos semitransparentes permiten apreciar su superposición.</p>'


def box_summary(values):
    """Mediana de mitades (bisagras de Tukey) y bigotes a 1,5 RIQ, como boxplot de R."""
    from statistics import median
    ordered=sorted(values); n=len(ordered)
    lower=median(ordered[:(n+1)//2]); upper=median(ordered[n//2:])
    spread=upper-lower
    inside=[v for v in ordered if lower-1.5*spread <= v <= upper+1.5*spread]
    return dict(n=n, lower=lower, median=median(ordered), upper=upper,
                minimum=min(inside), maximum=max(inside),
                outliers=[v for v in ordered if v < lower-1.5*spread or v > upper+1.5*spread])


def boxplots(root: Path):
    rows=list(csv.DictReader((root/'datos/wage1.csv').open()))
    definitions=[('educ','Educación: < 16 / ≥ 16', ['Menos de 16 años','16 años o más']),
                 ('female','Sexo registrado', ['Hombre (0)','Mujer (1)']),
                 ('married','Estado civil registrado', ['No casado/a (0)','Casado/a (1)'])]
    controls=[];panels=[]
    for variable,heading,names in definitions:
        groups=[[],[]]
        for row in rows:
            category=int(float(row['educ'])>=16) if variable=='educ' else int(row[variable])
            groups[category].append(float(row['wage']))
        summaries=[box_summary(v) for v in groups]
        assert sum(x['n'] for x in summaries)==526
        svg=[f'<svg class="wage-chart" viewBox="0 0 720 420" role="img" aria-labelledby="box-title-{variable}"><title id="box-title-{variable}">Salario por hora según {heading}. Comparación de medianas, dispersión y valores atípicos.</title>']
        py=lambda value:345-value/26*310
        for tick in range(0,26,5):
            y=py(tick)
            svg.append(f'<line class="chart-grid" x1="65" y1="{y}" x2="690" y2="{y}"/><text x="53" y="{y+4}" text-anchor="end">{tick}</text>')
        for i,summary in enumerate(summaries):
            x=240+270*i; color=PALETTE[0 if i==0 else 2]
            label=f'{names[i]}: n = {summary["n"]}; mediana = {summary["median"]:.2f} USD por hora'
            svg.append(f'<g tabindex="0" aria-label="{escape(label)}"><title>{escape(label)}</title><path d="M{x} {py(summary["minimum"])} V{py(summary["maximum"])} M{x-25} {py(summary["minimum"])} H{x+25} M{x-25} {py(summary["maximum"])} H{x+25}" stroke="#10193b" fill="none" stroke-width="2"/><rect x="{x-65}" y="{py(summary["upper"])}" width="130" height="{py(summary["lower"])-py(summary["upper"])}" fill="{color}" fill-opacity=".75" stroke="#10193b"/><path d="M{x-65} {py(summary["median"])} H{x+65}" stroke="#10193b" stroke-width="3"/></g>')
            for outlier in summary['outliers']:
                svg.append(f'<circle cx="{x}" cy="{py(outlier)}" r="3.5" fill="{color}" stroke="#10193b"><title>{names[i]}: {outlier:.2f} USD por hora, valor atípico según 1,5 RIQ</title></circle>')
            svg.append(f'<text x="{x}" y="372" text-anchor="middle">{escape(names[i])}</text><text x="{x}" y="393" text-anchor="middle">n = {summary["n"]} · mediana = {summary["median"]:.2f}</text>')
        svg.append('<text x="18" y="190" text-anchor="middle" transform="rotate(-90 18 190)">Salario por hora (USD de 1976)</text></svg>')
        table=''.join(f'<tr><th scope="row">{escape(names[i])}</th><td>{v["n"]}</td><td>{v["lower"]:.2f}</td><td>{v["median"]:.2f}</td><td>{v["upper"]:.2f}</td><td>{v["minimum"]:.2f}–{v["maximum"]:.2f}</td></tr>' for i,v in enumerate(summaries))
        controls.append(f'<button type="button" class="chart-choice" data-variable="{variable}" aria-pressed="false" aria-controls="box-panel-{variable}">{"educ ≥ 16" if variable=="educ" else variable}</button>')
        panels.append(f'<section id="box-panel-{variable}" class="chart-panel" hidden aria-labelledby="box-heading-{variable}"><h4 id="box-heading-{variable}">Salario según {heading.lower()}</h4>'+''.join(svg)+f'<details class="check"><summary>Ver resumen del boxplot</summary><div class="chart-table-wrap"><table class="schedule"><thead><tr><th>Grupo</th><th>n</th><th>Borde inferior</th><th>Mediana</th><th>Borde superior</th><th>Bigotes</th></tr></thead><tbody>{table}</tbody></table></div></details></section>')
    return '<div class="wage-explorer"><p>Elige una variable para comparar la distribución del salario entre sus dos grupos. Para educación mantenemos el corte justificado en la lámina anterior: menos de 16 años frente a 16 años o más.</p><div class="chart-choices" role="group" aria-label="Variable de agrupación del salario">'+''.join(controls)+'</div><p class="chart-status" role="status">Elige una variable de agrupación.</p>'+''.join(panels)+'<h4>Cómo leer los boxplots</h4><p>La línea dentro de la caja es la mediana salarial. La caja resume la mitad central de los salarios. Los bigotes llegan hasta los valores más extremos dentro de 1,5 veces el rango intercuartílico desde los bordes de la caja; los puntos exteriores son valores atípicos según esta regla y no necesariamente errores. Compara la altura de las medianas y la amplitud de las cajas. Las diferencias observadas entre grupos no demuestran causalidad.</p><p class="data-note">Fuente: datos/wage1.csv · 526 personas · CPS de Estados Unidos, 1976. Bisagras de Tukey y bigotes a 1,5 RIQ, siguiendo <a href="https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/boxplot.stats.html">boxplot.stats de R</a>. Salarios en USD por hora de 1976.</p></div>'
