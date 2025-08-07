def orden_letras(palabra):
    letras_ordenadas = []
    for letra in palabra:
        if letra not in letras_ordenadas:
            letras_ordenadas.append(letra)
            
    letras_ordenadas.sort()
    return letras_ordenadas

print(orden_letras('entretenido'))

