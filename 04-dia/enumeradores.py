lista = ['a','b','c']

for indice, item in enumerate(lista):
    print(indice, item)
    
lista_enums_tuple = list(enumerate(lista))
print(lista_enums_tuple)
    
for item in enumerate(range(10, 51, 5)):
    print(item)
    
nombres = enumerate(['bruno','francisco','jenni','lety'])
for indice, nombre in nombres:
    print(f'{nombre} tiene el indice: {indice}')

indices = list(enumerate('python'))
print(indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for i, nm in enumerate(lista_nombres):
    if nm[0] == 'M':
        print(i)

