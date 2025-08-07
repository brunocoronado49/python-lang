from random import shuffle

# Lista inicial de palitos
palitos = ['--', '----', '-----', '------', '----', '-']

# Mezclar palitos (volverlos aleatorios en la lista)
def mezclar(lista):
    shuffle(lista)
    return lista

# Entrada del usuario
def probar_suerte():
    intento = ''
    
    while intento not in ['1', '2', '3', '4', '5', '6']:
        intento = input('Ingresa un numero del 1 al 6: ')
        
    return int(intento)

# Comprobar resultado
def revisar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('Lavas los platos!')
    else:
        print('Te salvaste de lavar los platos!')
    
    print(f'Te toco el {lista[intento - 1]}')
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
revisar_intento(palitos_mezclados, seleccion)

