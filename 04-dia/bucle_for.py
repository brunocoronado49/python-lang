lista_nombres = ['Francsico', 'Bruno', 'Jose', 'Kenshin', 'Leon']

for nombre in lista_nombres:
    if nombre.startswith('J'):
        print(f'Que onda {nombre}')
        continue
    
    print(f'Hola {nombre}')
    
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
    
print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra.upper())
    
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic.items():
    print(item)


