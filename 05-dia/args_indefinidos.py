def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(3, 5, 7, 6, 5, 4))

def suma_cuadrados(*args):
    total = 0
    for num in args:
        total += num * num
    return total

print(suma_cuadrados(4, 8, 12, 16))

