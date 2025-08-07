def contar_primos(numero):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    primos = []
    
    for i in range(0, numero + 1):
        if es_primo(i):
            primos.append(i)
            
    return primos

resultado = contar_primos(20)
print(f'La cantidad primos es de {len(resultado)}')

