'''
string(str): "hola", "1234", "%$%&/("
integer(int); 1,2,3,123,0,-1
floating(float): 1.4,2.3,3.4,1.23,0.5,-1.3
listas(list): [1, 2, "hola", True]
diccionarios(dic): {"nombre": "bruce", "edad": 25}
tuples(tup): (1, 2, 3, 4, 5)
sets(set): ("a", "b", "c")
booleanos(bool): True, False
'''

numero_uno = 23
numero_dos = 54
numero_tres = numero_uno + numero_dos
print(numero_tres)
print(type(numero_tres))

numero_decimal = 32.3
print(type(numero_decimal))

edad = int(input('dime tu edad: '))
edad += 1
print(f'{edad} - {type(edad)}')