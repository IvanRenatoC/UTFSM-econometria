# Guía docente · Taller 2

Profesor: Iván Canales. Taller presencial para 8 a 10 estudiantes.
Horario: 18:50–21:25. Descanso: 20:00–20:15. La agenda detallada está en la página y el notebook.

Trabajar en parejas: predecir el signo antes de mostrar la recta, ejecutar el código, interpretar en unidades y contrastar con la nube. Las láminas y soluciones comienzan plegadas.

Se usa exclusivamente wage1 del libro de Wooldridge. Casos: wage ~ educ (positivo), educ ~ exper (negativo) y wage ~ numdep (no significativo al 5 %). El segundo cambia la variable respuesta y usa experiencia potencial; evitar atribuirle causalidad. El tercero no demuestra una pendiente poblacional cero. La inferencia clásica de lm requiere sus supuestos.

La secuencia sigue los temas revisados en la cátedra: motivación, modelo y error, esperanza condicional, regresión poblacional, MCO, regresión muestral, descomposición y R². No se incorporan demostraciones de insesgamiento ni varianza de estimadores. La consulta del p-valor se limita a distinguir el tercer caso solicitado.

Notación de la cátedra: SST total, SSE explicada, SSR residual. En MCO con intercepto, SST = SSE + SSR. Evitar intercambiar las siglas con otras convenciones.

En Colab seleccionar kernel R y ejecutar de arriba abajo, sin rpy2 ni %%R. Si no hay CSV local, la primera celda instala/carga wooldridge. La instalación necesita conexión. Los gráficos de la web usan la copia CSV completa; se calculan los ajustes en el navegador. El notebook los reproduce con lm y gráficos R.

## Fuentes

- [Cátedra 2](https://hizocar.github.io/econometria-usm/clases/clase2/).
- [Documentación de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html): CPS 1976, 526 personas, 24 variables; advertencia sobre experiencia potencial.

## Mantenimiento

Editar contenido-clase-2.json y ejecutar `python3 herramientas/generar_web.py` desde esta carpeta. Genera web, notebook, script y guía de actividades. Las visualizaciones están en herramientas/interactivos.js. Verificar nuevamente R si cambia el contenido.
