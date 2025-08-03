smarthphone = 'Motorola G8 Plus'

match smarthphone:
    case 'Motorola G8 Plus':
        print('Es un motorola')
    case 'Samsung':
        print('Es un samsung')
    case 'Iphone':
        print('Es una porqueria')
    case _:
        print('No es ninguno')

cliente = {'nombre': 'Francisco',
       'edad': 27,
       'ocupacion': 'Programador'}

pelicula = {'titulo': 'Virus',
            'ficha_tecnica': {'protagonista': 'una morra asiatica guapa',
                              'director': 'no se jaja'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print('Es una pelicula')
            print(titulo)
            print(protagonista, director)
        case _:
            print('Ni puta idea manix')

