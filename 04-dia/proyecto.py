from random import randint

'''
1. Preguntar el nombre al usuario
2. Mostrar que indique un numero del 1 al 100 con 8 intentos
3. El programa respondera con diferentes preguntas:
    - Si es un numero valido
    - Si el numero es menor al que penso el programa
    - Si el numero es mayor al que penso el programa
    - Si el numero es el que penso el programa y cuantos intentos tuvo
4. El programa pedira si quiere adivinar otro numero o salir
'''

nombre_usuario = input('Ingresa tu nombre: ')
print(f'Hola {nombre_usuario}, bienvenido a juego "Adivina el numero"...')
print('Tienes 8 intentos para adivinar un número entre 1 y 100.\n')

while True:
    numero_secreto = randint(1, 100)
    intentos = 0
    vidas = 8
    
    respuesta = input('Quieres adivinar el numero? (s/n) ').lower()
    if respuesta != 's':
        print('Gracias por jugar... Y NO VUELVA!')
        break
    
    while vidas > 0:
        try:
            numero_usuario = int(input(f'[{vidas} intentos] Ingresa un numero del 1 al 100: '))
        except ValueError:
            print('Error! Debes ingresar un numero entero')
            continue
        
        if numero_usuario < 1 or numero_usuario > 100:
            print('Numero invalido, debe ser entre 1 y 100')
            continue
        
        intentos += 1
        vidas -= 1
        
        if numero_usuario < numero_secreto:
            print(f'Tu numero es MENOR al secreto. Te quedan {vidas} intentos')
        elif numero_usuario > numero_secreto:
            print(f'Tu numero es MAYOR al secreto. Te quedan {vidas} intentos')
        else:
            print(f'Correcto, {numero_usuario}! Adivinaste en {intentos} intentos')
    
        if vidas == 0 and numero_usuario != numero_secreto:
            print(f'Se acabaron los intentos, el numero era: {numero_secreto}')
    
    