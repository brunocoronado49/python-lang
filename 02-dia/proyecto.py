nombre = input('dime tu nombre: ')
ventas = float(input('cuales fueron tus ventas: '))
comision = round(ventas * 13 / 100, 2)

print(f'Hola {nombre} este mes ganaste {comision}')