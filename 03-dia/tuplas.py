mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))
print(mi_tuple)

nueva_tupla = (45, 2.3, 'hola', True)
print(nueva_tupla)
print(nueva_tupla[1])

x, y, z, u = nueva_tupla
print(x)
print(z)
print(nueva_tupla.count(45))
print(nueva_tupla.index(True))