print([letra for letra in 'python'])
print([numero/2 for numero in range(10, 31)])
print([numero for numero in range(0, 21, 2) if numero * 2 > 10])
print([numero if numero * 2 > 10 else 'no' for numero in range(0, 21, 2)])

fts = [10,20,30,40,50]
mts = [p * 3.281 for p in fts]
print(mts)

