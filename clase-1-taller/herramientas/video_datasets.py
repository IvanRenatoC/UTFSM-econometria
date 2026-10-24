"""Contenido compartido del video silencioso de tres estructuras de datos."""
CHAPTERS = [
 dict(id='transversal', title='Corte transversal', subtitle='Varias unidades · un mismo período',
      key='Cada punto es una unidad distinta observada en 2020.',
      explanation='Los puntos se ordenan por unidad: A, B, C, D, E y F. Todos pertenecen a 2020. El eje vertical muestra el valor observado. Comparamos unidades en un mismo período; el orden horizontal no representa tiempo. wage1, la base del taller, es de corte transversal.',
      cues=['Observamos varias unidades en un mismo período.', 'Los puntos se ordenan por unidad; todos corresponden a 2020.', 'Comparamos unidades entre sí. Este es el caso de wage1.']),
 dict(id='temporal', title='Serie de tiempo', subtitle='Una misma unidad · varios períodos',
      key='Cada punto es un período de la misma unidad A.',
      explanation='Los puntos de la unidad A se ordenan de 2020 a 2025. El eje horizontal ahora representa tiempo y el vertical, el valor observado en cada período. La línea ayuda a seguir el orden temporal: no es una recta de regresión. Estudiamos cómo cambia una unidad a través del tiempo.',
      cues=['Seguimos una misma unidad en distintos períodos.', 'Los puntos se ordenan de 2020 a 2025: el eje horizontal es tiempo.', 'La línea conecta observaciones en el tiempo; no es una regresión.']),
 dict(id='panel', title='Datos de panel', subtitle='Las mismas unidades · varios períodos',
      key='Cada punto combina una unidad y un período.',
      explanation='Seguimos a A, B y C de 2020 a 2025. Cada color identifica siempre a la misma unidad. Los puntos se ordenan por período y forman tres trayectorias. Podemos comparar unidades y observar cambios dentro de cada una. Las líneas conectan observaciones de una misma unidad; no son regresiones estimadas.',
      cues=['Seguimos a las mismas unidades A, B y C durante varios períodos.', 'Los puntos se ordenan por tiempo; cada color conserva la unidad.', 'Comparamos unidades y sus cambios en el tiempo. Esto es panel.'])
]


def interactive_video(root):
    import json,hashlib
    from html import escape as e
    def asset(name):
        digest=hashlib.sha256((root/'media'/name).read_bytes()).hexdigest()[:12]
        return f'media/{name}?v={digest}'
    timing=json.loads((root/'media/tipos-datasets-capitulos.json').read_text())
    buttons=''.join(f'<button type="button" class="dataset-chapter" data-start="{t["start"]}" aria-pressed="false">{i+1}. {e(c["title"])}</button>' for i,(c,t) in enumerate(zip(CHAPTERS,timing)))
    transcript=''.join(f'<h4>{i+1}. {e(c["title"])}</h4><p>{e(c["explanation"])}</p>' for i,c in enumerate(CHAPTERS))
    return f'''<div class="dataset-lesson"><p>Video sin audio · 45 segundos. Observa cómo se ordenan los puntos: por unidad, por tiempo o por ambos. Los valores son ficticios y sirven para reconocer la estructura de los datos.</p>
<video class="dataset-video" controls muted preload="metadata" playsinline poster="{asset('tipos-datasets-portada.png')}" aria-label="Video silencioso de 45 segundos: corte transversal, serie de tiempo y datos de panel"><source src="{asset('tipos-datasets.mp4')}" type="video/mp4"><track kind="subtitles" src="{asset('tipos-datasets-es.vtt')}" srclang="es" label="Explicación en español">Tu navegador no admite video. Lee la explicación que aparece más abajo.</video>
<div class="dataset-chapters" role="group" aria-label="Capítulos del video">{buttons}</div><p class="dataset-status" role="status">Tres capítulos de 15 segundos · Puedes pausar o elegir un tipo de dataset. Las explicaciones aparecen escritas en el video.</p>
<fieldset class="dataset-quiz"><legend>Comprueba la diferencia</legend><p>Observas a las mismas personas A, B y C en 2020, 2021 y 2022. ¿Qué estructura tiene la base?</p><div class="dataset-answers"><button type="button" data-answer="transversal">Corte transversal</button><button type="button" data-answer="temporal">Serie de tiempo</button><button type="button" data-answer="panel">Datos de panel</button></div><p class="dataset-feedback" role="status"></p></fieldset>
<details class="check"><summary>Leer la explicación de los tres casos</summary><div class="solution-body">{transcript}</div></details><p class="data-note">Las líneas conectan observaciones de una misma unidad, no regresiones estimadas. Referencias: <a href="https://www.stata.com/manuals/xt.pdf">datos transversales y panel</a> y <a href="https://otexts.com/fpp3/regression.html">regresión con series de tiempo</a>.</p></div>'''
