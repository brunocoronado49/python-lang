def cero_seguido(*args):
    for num in args:
        if args[num - 1] == args[num]:
            return True
    return False

print(cero_seguido(5,6,1,0,0,9,3,5))
print(cero_seguido(6,0,5,1,0,3,0,1))

