lista_numeros = [34, 5645, 124, 4535, 67, 888, 1]

def checar_3_cifras(lista):
    lista_de_tres = []
    for numero in lista:
        if numero in range(100, 1000):
            lista_de_tres.append(numero)
        else:
            pass
    return lista_de_tres

resultado = checar_3_cifras(lista_numeros)
print(resultado)

def nums_positivos(lista):
    for num in lista:
        if num > 0:
            return True
    return False

lista_numeros = [2, 3, 4, 6, -5, -2, -4, 10]
print(nums_positivos(lista_numeros))

def suma_menores(lista):
    suma = 0
    for num in lista:
        if num > 0 and num < 100:
            suma += num  
    return suma

lista_numeros = [41, 268, 378, 45, 65, 634, 0, 1000, 200, 43]
print(suma_menores(lista_numeros))

