# Punto-de-Equilibrio
Funciones básicas de python aplicadas al cálculo del Punto de Equilibrio.

## Código clave:
### Markdown

Funciones matemáticas simples.

![math_function](https://user-images.githubusercontent.com/90414330/214788603-d2074444-0f2e-4816-9f2c-4c86b0e1d8f1.png)


### Tabla Margen de Ganancia

**Función $range$**. Usamos la función para poder generar una lista de unidades que vaya desde el 1 y hasta el 50, de 5 en 5.

**List Comprehension**. Para cada elemento de la lista unidades, calculamos el costo de producción o de ventas.

**Función $For-Loop$ / $map(lambda())$**. Hacemos operaciones aritméticas entre los elementos de dos listas (costos y ventas).

Librería **Pandas** para poder armar una tabla con las listas *unidades*, *costos*, *ventas* y *utilidades*. De esta forma visualizamos de mejor manera los datos.

![pe_df](https://user-images.githubusercontent.com/90414330/214788326-4fb9114c-03e8-468b-9846-f28d74e81f37.png)

### Plotly

Usamos la librería **$plotly.graph_{}objects$** para graficar *costos*, *ventas* y *utilidades* vs *unidades*, y el **punto de equilibrio** en un sólo gráfico.

![Grafico del Punto de Equilibrio](https://user-images.githubusercontent.com/90414330/214787998-8b2fd4df-dd30-4a38-a041-1bb83e7e5c39.png)
