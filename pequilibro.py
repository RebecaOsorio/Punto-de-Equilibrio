import pandas as pd
import plotly.graph_objects as go

print('Sea una marca que vende riñoneras a $2,000. El costo de producción de cada una es de $1,200 y, además, debe contemplar $28,000 de costos fijos.\n\n')
# Instanciación de Variables
cfijos = 28000
cvariables = 1200
ventatotal = 2000

print(f'Tendremos que: \n Costos Fijos = ${cfijos:,.2f} \n Costos Variables = ${cvariables:,.2f} \n Venta total = ${ventatotal:,.2f}\n\n')

# Punto de Equilibrio en Volumen
pe_volumen = cfijos / (ventatotal - cvariables)

# Punto de Equilibrio en Valor
pe_valor = cfijos / ( 1 - cvariables / ventatotal)

print(f'La empresa deberá vender {pe_volumen} productos o ${pe_valor:,.2f} para llegar al punto de equilibrio')

# Tabla Margen de Ganancia
unidades = list(range(0, 50+1, 5))
ventas = [x*ventatotal for x in unidades]
costos = [x*cvariables+cfijos for x in unidades]

utilidades = []
for i in range(len(unidades)):
    utilidades.append(ventas[i]-costos[i])

pe_df = pd.DataFrame(list(zip(unidades,ventas,costos,utilidades)),
                     columns =['unidades (x)','ventas','costos','utilidades'])
display(pe_df)


fig = go.Figure()
fig.add_trace(go.Scatter(x=unidades, y=ventas,
                         mode='lines',
                         name='ventas'))
fig.add_trace(go.Scatter(x=unidades, y=costos,
                         mode='lines',
                         name='costos'))
fig.add_trace(go.Scatter(x=unidades, y=utilidades,
                         mode='lines',
                         name='utilidades'))
fig.add_trace(go.Scatter(x=[pe_volumen],y=[pe_valor],
                         mode='markers',
                         name='Punto de Equilibrio',
                         marker=dict(color='DarkSlateBlue',size=9)))
fig.update_layout(title="Gráfico del Punto de Equilibrio",
                  xaxis_title="Unidades",
                  yaxis_title="$",)

fig.show()