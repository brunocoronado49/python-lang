from random import choice

# Funcion que elije una palabra al azar
def choice_word(words_list):
    word_selected = choice(words_list).lower()
    return word_selected

# Funcion que cambia las letras por guiones
def hidden_word(word, guessed_letters = []):
    return ''.join(
        char if char in guessed_letters or char == ' ' else '-'
        for char in word)

# Ingreso de la letra del usuario
def user_letter():
    while True:
        letter = input('Ingresa una letra de la A a la Z: ').lower().strip()
        if len(letter) == 1 and letter.isalpha():
            return letter # Retorna la letra y sale del bucle infinito
        else:
            # muestra el error y repite el bucle
            print('Error, debe ser una letra de la A a la Z')

# comparacion de entrada de usuario con palabra elegida
def check_answer():
    lives = 7
    guessed_letters = []
    words = ['python', 'batman', 'caracoles', 'videojuegos', 'mariposas', 'agua']
    correct_word = choice_word(words)
    
    print('******* Juego del Ahorcado *******')
    print(f'Palabra a adivinar tiene {len(correct_word)} letras')
    
    while lives > 0:
        showed_word = hidden_word(correct_word, guessed_letters)
        print(f'Palabra: {showed_word}')
        print(f'Vidas: {lives}')
        print(f'Letras adivinadas: {', '.join(guessed_letters)}')
        
        if showed_word == correct_word:
            print(f'Felicidades, la palabra era {correct_word}')
            return
        
        letter = user_letter()
        
        if letter in guessed_letters:
            print('Esa letra ya esta, prueba otra')
            continue
        
        guessed_letters.append(letter)
        
        if letter in correct_word:
            print(f'Muy bien, {letter} esta en la palabra')
        else:
            print(f'Mal, la letra "{letter}" no esta en la palabra.')
            lives -= 1
    print(f'Perdiste, la palabra era {correct_word}')
    
check_answer()

