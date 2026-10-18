"""Guion y contenido compartido del video de tipos de datasets."""
CHAPTERS = [
 dict(id='transversal', title='Corte transversal', subtitle='Muchas unidades · un período',
      headers=['Persona','Año','Educación','Salario'],
      rows=[['Ana','2020','12','4'],['Bruno','2020','16','8'],['Carla','2020','14','6'],['Diego','2020','10','3']],
      key='Cambia la persona; el período es el mismo.', formula='yᵢ = β0 + β1xᵢ + uᵢ',
      narration='Primero, los datos de corte transversal. Observamos varias unidades, como personas, empresas o países, en un mismo período. En esta tabla ficticia cada fila es una persona, y todas corresponden al año dos mil veinte. Podemos estudiar cómo se relacionan educación y salario entre personas. En la expresión del modelo, el subíndice i identifica a cada unidad. La base wage uno de nuestro taller tiene esta estructura: personas observadas en mil novecientos setenta y seis. El número de fila no representa el paso del tiempo.'),
 dict(id='temporal', title='Serie temporal', subtitle='Una unidad · varios períodos ordenados',
      headers=['Empresa','Año','Publicidad','Ventas'],
      rows=[['Empresa A','2020','10','42'],['Empresa A','2021','12','45'],['Empresa A','2022','11','44'],['Empresa A','2023','15','52']],
      key='La unidad es la misma; avanza el tiempo.', formula='yₜ = β0 + β1xₜ + uₜ',
      narration='Ahora, una serie temporal. Seguimos una misma unidad durante varios períodos ordenados. En este ejemplo ficticio, cada fila es un año de la misma empresa. Relacionamos sus ventas con su gasto en publicidad a lo largo del tiempo. El subíndice t identifica el período. Aquí importa conservar el orden temporal: los resultados de un año pueden estar relacionados con los del anterior. Por eso debemos revisar tendencias y dependencia temporal antes de aplicar e interpretar un modelo lineal. No son cuatro empresas diferentes: es una empresa observada cuatro veces.'),
 dict(id='repetidos', title='Cortes transversales repetidos', subtitle='Varias muestras · distintos períodos',
      headers=['Persona','Año','Educación','Salario'],
      rows=[['Ana','2020','12','4'],['Bruno','2020','16','8'],['Elena','2023','12','5'],['Felipe','2023','16','9']],
      key='Cambia el período y cambia la muestra de personas.', formula='y = β0 + β1x + δ·período + u',
      narration='También podemos reunir cortes transversales repetidos. Tomamos una muestra en un período y otra muestra en un período posterior. Observa los nombres: las personas de dos mil veinte no son las mismas que las de dos mil veintitrés. Podemos comparar distribuciones y asociaciones entre períodos, y un modelo lineal puede incluir un indicador del período. Pero no podemos calcular cuánto cambió el salario de Ana, porque no la volvimos a observar. Tener una columna con años no convierte por sí solo a la base en un panel.'),
 dict(id='panel', title='Datos de panel', subtitle='Las mismas unidades · varios períodos',
      headers=['Persona','Año','Educación','Salario'],
      rows=[['Ana','2020','12','4'],['Ana','2023','13','5'],['Bruno','2020','16','8'],['Bruno','2023','16','9']],
      key='Seguimos a las mismas personas a través del tiempo.', formula='yᵢₜ = β0 + β1xᵢₜ + uᵢₜ',
      narration='Por último, los datos de panel. Observamos a las mismas unidades en varios períodos. Ana aparece dos veces y Bruno también. Ahora cada fila es una combinación de persona y período. Los subíndices i y t identifican ambas dimensiones. Podemos comparar personas y estudiar cambios dentro de una misma persona. La expresión que ves solo ilustra los índices: analizar un panel requiere considerar la dependencia entre observaciones de la misma unidad y, según el modelo, diferencias persistentes entre personas. Recuerda la distinción: en cortes repetidos cambia la muestra; en panel seguimos a las mismas unidades. Ninguna de estas estructuras, por sí sola, demuestra causalidad.')
]


def interactive_video(root):
    import json
    from html import escape as e
    timing=json.loads((root/'media/tipos-datasets-capitulos.json').read_text())
    buttons=''.join(f'<button type="button" class="dataset-chapter" data-start="{t["start"]}" aria-pressed="false">{i+1}. {e(c["title"])}</button>' for i,(c,t) in enumerate(zip(CHAPTERS,timing)))
    transcript=''.join(f'<h4>{i+1}. {e(c["title"])}</h4><p>{e(c["narration"])}</p>' for i,c in enumerate(CHAPTERS))
    return f'''<div class="dataset-lesson"><p>Reproduce el video o elige un capítulo. Observa qué cambia en cada tabla: la unidad, el período o ambos. Los ejemplos son ficticios y sirven para reconocer la estructura de los datos.</p>
<video class="dataset-video" controls preload="metadata" playsinline poster="media/tipos-datasets-portada.png" aria-label="Video narrado: tipos de datasets en modelos lineales"><source src="media/tipos-datasets.mp4" type="video/mp4"><track kind="captions" src="media/tipos-datasets-es.vtt" srclang="es" label="Español" default>Tu navegador no admite video. Lee la transcripción que aparece más abajo.</video>
<div class="dataset-chapters" role="group" aria-label="Capítulos del video">{buttons}</div><p class="dataset-status" role="status">Narración en español · Puedes pausar, cambiar la velocidad o activar los subtítulos desde los controles del video.</p>
<fieldset class="dataset-quiz"><legend>Comprueba la diferencia</legend><p>Encuestas a Ana y Bruno en 2020, y a Elena y Felipe en 2023. ¿Qué estructura tiene la base?</p><div class="dataset-answers"><button type="button" data-answer="panel">Panel</button><button type="button" data-answer="repetidos">Cortes transversales repetidos</button><button type="button" data-answer="temporal">Serie temporal</button></div><p class="dataset-feedback" role="status"></p></fieldset>
<details class="check"><summary>Leer la transcripción completa</summary><div class="solution-body">{transcript}</div></details><p class="data-note">Las ecuaciones son esquemas para identificar las unidades y los períodos; el video no estima modelos. Referencias: <a href="https://www.stata.com/manuals/xt.pdf">datos transversales y panel</a> y <a href="https://otexts.com/fpp3/regression.html">regresión con series temporales</a>.</p></div>'''
