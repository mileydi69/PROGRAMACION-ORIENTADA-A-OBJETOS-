def calcular_temperatura (frio_lluvia, calor_soleado):
    temperatura = (frio_lluvia - 5)
    temperatura = (calor_soleado + 23)
    return temperatura

temperatura=(5,23)
print( temperatura)
temperatura = calcular_temperatura

# ingreso de grados centigrados
grados_centigrados = float(input('ingrese los grados centigrados'))
frio_lluvia = float(input('ingrese calor, soleado'))

# llamada a funcion para la temperatura
temperatura = calcular_temperatura('frio_lluvia', 'calor_soleado')

# llamada a funcion para el calculo de la temperatura
# formula para calcular los grados centigrados de la temperatura
grados_centigrados_menos_temperatura = grados_centigrados-temperatura

print('temperatura frio lluvia: 5', 'menos_grados_centigrados')
print('temperatura calor soleado 23', 'mas_grados_centigrados')
print('temperatura total : 38', 'grados_centigrado_temperatura')