def numeros_perfumeria():
    for numero in range(1, 20):
        yield f'P - {numero}'


def numeros_farmacia():
    for numero in range(1, 20):
        yield f'F - {numero}'


def numeros_cosmeticos():
    for numero in range(1, 20):
        yield f'C - {numero}'


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmeticos()


def decorador(rubro):
    print('\n' + '*' * 23)
    print('Su numero es:')
    
    if rubro == 'p':
        print(next(p))
    elif rubro == 'f':
        print(next(f))
    else:
        print(next(c))
    print('Espere y sera atendido...')
    print('*' * 23 + '\n')
