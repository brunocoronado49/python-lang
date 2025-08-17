from collections import Counter, defaultdict, namedtuple


numeros = [8, 6, 5, 3, 7, 4, 3, 4, 6, 2]
print(Counter(numeros))
print(Counter('misisipi'))
print(Counter('Al pan pan y al vino vino'.split()))

serie = Counter([1,1,1,1,1,2,2,2,3,3,4,4,5,6,6,7,7,5,4,4])
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))


dic = defaultdict(lambda: 'nada')
dic['uno'] = 'verde'
print(dic)


Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.65, 68)
print(ariel.altura)
print(ariel[2])
