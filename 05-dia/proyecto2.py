from random import choice


palabras = ['python', 'batman', 'caracoles', 'videojuegos', 'mariposas', 'agua']
letras_correctas = []
letras_incorrectas = []
intentos = 7
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    
    while not es_valida:
        letra_elegida = input('Ingresa una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('La letra no es valida')
    
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')
    
    print(' '.join(lista_oculta))
    

def revisar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        print(f'Letra {letra_elegida} es incorrecta')
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    
    return vidas, fin, coincidencias


def perder():
    print('Te has quedado sin vidas')
    print(f'Palabra correcta: {palabra}')
    
    return True


def ganar(palabra_descubierta):
    print('Felicidades, has ganado!')
    mostrar_nuevo_tablero(palabra_descubierta)
    
    return True


palabra,letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print(f'Letras incorrectas: {len(
        letras_incorrectas)} - ' + ', '.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    
    letra = pedir_letra()
    
    intentos, terminado, aciertos = revisar_letra(letra, palabra, intentos, aciertos)
    
    juego_terminado = terminado
