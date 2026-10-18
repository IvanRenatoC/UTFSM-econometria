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
