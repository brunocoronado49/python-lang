'''
Analizador de texto:
Pedir al usuario que ingrese un texto.
Pedir al usuario ingresar 3 letras aleatorias.
Realizar 5 tipos de verificaciones:
1. Cuantas veces aparece cada letra en el texto
2. Modificar el texto y letras a minuscula
3. Cuantas palabras hay en el texto
4. Cual es la primer letra y la ultima
5. Palabras en orden inverso
6. Aparece la palabra "python"?
'''

# Inicialicion de variables
letras = []
texto = input("Ingresa un texto que quieras: ").lower()

# Agregar letras a un arreglo
for i in range(3):
    letra = input('Ingresa una letra: ').lower()
    letras.append(letra)

# Veces que sale cada letra en el texto
primera = letras[0]
segunda = letras[1]
tercera = letras[2]
contador1 = texto.count(primera)
contador2 = texto.count(segunda)
contador3 = texto.count(tercera)
print(f'Letras en texto: {primera} = {contador1}, {segunda} = {contador2}, {tercera} = {contador3}')

# Cuantas palabras hay en el texto
palabras_en_texto = texto.split(' ')
print(f'Palabras totales en el texto: {len(palabras_en_texto)}')

# Primera y ultima letra en texto
print(f'Primer letra: {texto[0]}, ultima letra: {texto[-1]}')

# Python en el texto
validar = 'python' in texto
print(f'La palabra "Python" esta en el texto? {validar}')

