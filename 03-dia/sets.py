# Las listas no pueden ir dentro de un set, tampoco los diccionarios
# pero si admite tuples

sets = set((1, 3, 4, 5, 6, 7)) # set solo admite un elemento
print(type(sets))
print(sets)

nuevo_set = {'werf', 'we', 'tr'} # set sin la palabra set
print(type(nuevo_set))
print(nuevo_set)

print(2 in sets)
print(3 in sets)
print("hpa" in nuevo_set)
print("we" in nuevo_set)

set_final = sets.union(nuevo_set)
print(set_final)

sets.add(10)
print(sets)

# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
sets.remove(3) 
print(sets)

# Remove an element from a set if it is a member.
# Unlike set.remove(), the discard() method does not raise
# an exception when an element is missing from the set.
sets.discard(5)
print(sets)
sets.pop() # Elimina el primer elemento
print(sets)

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
s3 = s1.union(s2)
print(s3)
s3.clear()
print(s3)

