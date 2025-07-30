mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))
print(mi_tuple)

nueva_tupla = (45, 2.3, 'hola', True)
print(nueva_tupla)
print(nueva_tupla[1])
print(nueva_tupla[-2])

x, y, z, u = nueva_tupla
print(x)
print(z)
print(nueva_tupla.count(45)) # cuantos 45 hay en la tuple
print(nueva_tupla.index(True)) # el indice del valor True en la tuple

mi_tuple2 = "perro", "gato", "pajaro"
print(type(mi_tuple2)) # <- tuple

tuple_anidado = (1, 2, 3, (3, 2, 1), 4)
print(tuple_anidado[3][1])

tuple_repetida = (1, 2, 3, 1)
print(len(tuple_repetida))
print(tuple_repetida.count(1))

