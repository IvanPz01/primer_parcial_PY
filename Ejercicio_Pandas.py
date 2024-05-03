import pandas as pd
import matplotlib.pyplot as plt


ventas_mensuales = [ 
{"mes": "Enero", "total_ventas": 15000, "año": 2023}, 
{"mes": "Febrero", "total_ventas": 18000, "año": 2023}, 
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},

{"mes": "Abril", "total_ventas": 19000, "año": 2023}, 
{"mes": "Mayo", "total_ventas": 25000, "año": 2023}, 
{"mes": "Junio", "total_ventas": 28000, "año": 2023}, 

{"mes": "Julio", "total_ventas": 32000, "año": 2023}, 
{"mes": "Agosto", "total_ventas": 30000, "año": 2023}, 
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023}, 

{"mes": "Octubre", "total_ventas": 31000, "año": 2023}, 
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023}, 
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023}, 

{"mes": "Enero 2", "total_ventas": 37000, "año": 2024}, 
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024}, 
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024}, 

{"mes": "Abril 2", "total_ventas": 39000, "año": 2024}, 
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},

{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024}, 
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},

{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
] 

ventas_mensuales_df = pd.DataFrame(ventas_mensuales)

Primer_Trimestre=[
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023}]
df_primer = pd.DataFrame(Primer_Trimestre)

Segundo_trimestre = [
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
]
df_segundo = pd.DataFrame(Segundo_trimestre)

tercer_trimestre = [
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023}
]
df_tercero = pd.DataFrame(tercer_trimestre)

cuarto_trimestre = [
    {"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023}
]
df_cuarto = pd.DataFrame(cuarto_trimestre)

quiento_trimestre = [
    {"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024}
]
df_quinto = pd.DataFrame(quiento_trimestre)

Sexto_trimestre= [
    {"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024}
]
df_sexto = pd.DataFrame(Sexto_trimestre)

septimo_trimestre = [
    {"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024}
]
df_septimo = pd.DataFrame(septimo_trimestre)

octavo_trimestre = [
    {"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]
df_octavo = pd.DataFrame(octavo_trimestre)


print('Primer timestre', df_primer['total_ventas'].sum())
print('Segundo timestre', df_segundo['total_ventas'].sum())
print('tercero timestre', df_tercero['total_ventas'].sum())
print('caurto timestre', df_cuarto['total_ventas'].sum())
print('quiento timestre', df_quinto['total_ventas'].sum())
print('sexto timestre', df_sexto['total_ventas'].sum())
print('septimo timestre', df_septimo['total_ventas'].sum())
print('octavo timestre', df_octavo['total_ventas'].sum())



ventas_mayores_200 = ventas_mensuales_df[ventas_mensuales_df['total_ventas'] > 2000]

print('ventas mayores a 2000',ventas_mayores_200)

mes_max = ventas_mensuales_df["total_ventas"].max

print('el maximo de ventas es: ', mes_max )

ventas_mensuales_df.drop('año', axis=1, inplace=True)



x = ventas_mensuales_df['mes']
y = ventas_mensuales_df["total_ventas"]


plt.plot(x,y)

plt.title('ventas mensuales')

plt.xlabel('meses')
plt.ylabel('Ventas')

plt.show()