from random import *

aleatorio = randint(20, 155)
print(f'El numero random es: {aleatorio}')

decimal_aleatorio = uniform(10, 50)
print(f'El numero con decimal random es: {decimal_aleatorio}')

numero_random = random()
print(f'El numero random es: {numero_random}')

colores = ['azul', 'rojo', 'negro', 'verde', 'naranja']
color_random = choice(colores)
print(f'El color random es: {color_random}')

numeros = list(range(5, 51, 5))
shuffle(numeros)
print(numeros)

