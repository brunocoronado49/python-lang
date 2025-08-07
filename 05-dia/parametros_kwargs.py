def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        total += valor
        print(f'{clave} es igual a {valor}')
    print(f'El resultado de sumar los valores es {total}')

suma(x=3, r=5, y=8)

