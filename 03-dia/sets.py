sets = set((1, 3, 4, 5, 6, 7))
print(type(sets))
print(sets)

nuevo_set = {'werf', 'we', 'tr'}
print(type(nuevo_set))
print(nuevo_set)

print(2 in sets)
print(2 in nuevo_set)

set_final = sets.union(nuevo_set)
print(set_final)

sets.add(10)
print(sets)
sets.remove(3)
print(sets)
sets.discard(5)
print(sets)
sets.pop() # Elimina un elemento aleatorio
print(sets)