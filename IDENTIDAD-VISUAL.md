# Identidad visual del taller

Referencia: [Clase 1 de Sebastián Azócar](https://hizocar.github.io/econometria-usm/clases/clase1/), estilos calculados del tema claro consultados el 17 de octubre de 2026.

| Elemento | Valor de referencia aplicado |
|---|---|
| Tipografía | Roboto, con alternativas del sistema |
| Título principal | 32 px, peso 300, color #1b2a5e, espaciado -0,01 em |
| Línea del título | 3 px, #e5b300 |
| Subtítulo de sección | 25 px, peso 300, borde izquierdo #005f96 |
| Título de lámina | 21 px, peso 700, #1b2a5e |
| Cabecera | linear-gradient(90deg, #10193b 0%, #1b2a5e 55%, #005f96 100%) |
| Banda de navegación | #10193b, línea superior amarilla |
| Etiquetas azules | #1b2a5e, texto blanco, peso 600, radio 6 px |
| Etiqueta de semana | #e5b300, texto #10193b |
| Aviso informativo | Borde #00b8d4, cabecera al 10% de opacidad, radio 4 px |
| Menús laterales | 14 px; título peso 700 y gris; clase actual amarilla |

El logo utilizado es el archivo `Logo_UTFSM.png` entregado por el profesor, sin alterar su imagen. La fuente se carga desde Google Fonts, como en la referencia; sin conexión se utiliza la alternativa del sistema.

El temario izquierdo contiene las clases 1 y 2 solicitadas. La clase 2 lleva al aviso de próxima clase, sin presentar contenido que todavía no se ha preparado. La columna derecha enlaza objetivos, agenda, los cuatro bloques y sus 46 actividades, autoevaluación y siguiente clase.

La fecha exacta del taller no fue especificada: la etiqueta muestra «Lunes · Taller presencial», manteniendo 18:50–21:25. No se reutiliza la fecha del viernes de cátedra.

## Regeneración

Ejecutar `python3 herramientas/generar_web.py`. Este generador conserva las actividades del notebook y aplica `herramientas/identidad_web.py`. Los estilos y la búsqueda están en `identidad-utfsm.css` y `navegacion-utfsm.js`.

## Verificación

Se comprobaron logo, 46 actividades, IDs y enlaces locales, estilos calculados, búsqueda por «matrices», navegación de presentación y apertura de soluciones. Se revisó el diseño de escritorio y en un ancho móvil de 390 px, sin desbordamiento horizontal. Este cambio de presentación no valida la ejecución de los ejercicios en R, que sigue pendiente según la guía.
