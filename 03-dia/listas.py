lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista)
print(type(lista))
lista.append(10)
print(lista)
lista.append('g') # agrega el elemento al final de la lista
print(lista)
lista[1] = 'aaa'
lista.pop()
print(lista)
lista.pop(5) # elimina el indice que se le indica
print(lista)
print(lista[4])
print(lista[0:2])

lista_ordenada = ["h", "d", "t", "b", "g", "a"]
print(lista_ordenada)
lista_ordenada.sort()
print(lista_ordenada)
lista_ordenada.reverse()
print(lista_ordenada)

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
result = mi_lista[0:]
print(result)
print(mi_lista)
print(mi_lista2)
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)
mi_lista3[0] = '%'
print(mi_lista3)

transportes = ['avion', 'carro', 'bici']
transportes.append('moto')
print(transportes)

frutas = ['manzana', 'platano', 'mango', 'sandia']
frutas.pop(3)
print(frutas)

