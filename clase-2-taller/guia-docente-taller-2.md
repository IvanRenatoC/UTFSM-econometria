# Guía docente · Taller 2

Profesor: Iván Canales. Taller presencial para 8 a 10 estudiantes.
Horario: 18:50–21:25. Descanso: 20:00–20:15. La agenda detallada está en la página y el notebook.

Trabajar en parejas: predecir el signo antes de mostrar la recta, ejecutar el código, interpretar en unidades y contrastar con la nube. Las láminas y soluciones comienzan plegadas.

Se usa wage1 del libro de Wooldridge para wage ~ educ (positivo). La lámina 07 incorpora summary y ANOVA con sus resultados numéricos e interpretación desplegable. Para los otros casos se usa mtcars, base real incluida en R: qsec ~ hp (negativo) y qsec ~ drat (no significativo al 5 %). La respuesta es el tiempo en segundos para recorrer un cuarto de milla; hp es potencia bruta y drat, relación de transmisión del eje trasero. No hay una pendiente exactamente cero demostrada. La lámina 08 compara ambos casos y la 09 profundiza en el intervalo del no significativo. La inferencia clásica de lm requiere sus supuestos. Son asociaciones entre autos distintos, no efectos de una intervención.

Resultados verificados: qsec ~ hp tiene pendiente −0.018458, R² ≈ 0.5016 y p ≈ 5.77e−6. qsec ~ drat tiene pendiente 0.3048, R² ≈ 0.008318, p ≈ 0.6196 e intervalo del 95 % [−0.9361, 1.5458]. En la regresión salarial, la ANOVA da SSE ≈ 1179.732 y SSR ≈ 5980.682, con F ≈ 103.36.

La secuencia sigue los temas revisados en la cátedra: motivación, modelo y error, esperanza condicional, regresión poblacional, MCO, regresión muestral, descomposición y R². No se incorporan demostraciones de insesgamiento ni varianza de estimadores. La consulta del p-valor se limita a distinguir el tercer caso solicitado.

Notación de la cátedra: SST total, SSE explicada, SSR residual. En MCO con intercepto, SST = SSE + SSR. Evitar intercambiar las siglas con otras convenciones.

En Colab seleccionar kernel R y ejecutar de arriba abajo, sin rpy2 ni %%R. Si no hay CSV local, la primera celda instala/carga wooldridge. La instalación necesita conexión. Los gráficos de la web usan la copia CSV completa; se calculan los ajustes en el navegador. El notebook los reproduce con lm y gráficos R.

## Fuentes

- [Cátedra 2](https://hizocar.github.io/econometria-usm/clases/clase2/).
- [Documentación de mtcars](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html): Motor Trend 1974, 32 automóviles de modelos 1973–1974.
- [ANOVA de lm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/anova.lm.html).
- [summary de lm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.lm.html).
- [Documentación de wage1](https://justinmshea.github.io/wooldridge/reference/wage1.html): CPS 1976, 526 personas, 24 variables; advertencia sobre experiencia potencial.

## Mantenimiento

Editar contenido-clase-2.json y ejecutar `python3 herramientas/generar_web.py` desde esta carpeta. Genera web, notebook, script y guía de actividades. Las visualizaciones están en herramientas/interactivos.js. Verificar nuevamente R si cambia el contenido.
