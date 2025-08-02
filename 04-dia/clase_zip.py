nombres = ['ana', 'hugo', 'valeria']
edades = [23, 43, 16]

combinados = list(zip(nombres, edades))
print(combinados)

ciudades = ['Mexico', 'Japon', 'Canada']

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f'{nombre} con la edad de {edad} vive en {ciudad}')

