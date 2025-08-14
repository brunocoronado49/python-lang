def suma():
    try:
        num1 = int(input('Ingresa un numero: '))
        num2 = int(input('Ingresa otro numero: '))
        print(num1 + num2)
    except ValueError as e:
        print(f'Ocurrio un error: {e}')
    finally:
        print('Eso fue todo')


suma()

def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print('Fin')
    

pedir_numero()
