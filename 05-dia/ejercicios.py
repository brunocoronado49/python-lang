from random import *

def lanzar_dados():
    valor_1 = randint(1, 7)
    valor_2 = randint(1, 7)
    return (valor_1, valor_2)

def evaluar_jornada(valor1, valor2):
    suma = valor1 + valor2
    if suma <= 6:
        return f'La suma total es de {suma}, muy mal'
    elif suma > 6 and suma < 10:
        return f'La suma total es {suma}, tienes chance'
    elif suma >= 10:
        return f'La suma es {suma}, excelente has ganado'
    
dado1, dado2 = lanzar_dados()
resultado = evaluar_jornada(dado1, dado2)
print(resultado)

def reducir_lista(lista):
    lista_nueva = []
    for numero in lista:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    num_mayor = max(lista_nueva)
    lista_nueva.remove(num_mayor)
    
    return lista_nueva

def promedio(lista):
    suma = 0
    for num in lista:
        suma += num
        promedio = suma / len(lista)
    return promedio

lista_numeros = [1,2,15,7,2,8,12,24,38,12,43,8]
print(lista_numeros)
nueva_lista = reducir_lista(lista_numeros)
print(nueva_lista)
resultado = promedio(nueva_lista)
print(resultado)

