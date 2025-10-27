import re


texto = 'Si necesitas ayuda llama a (492) las 24 horas al servicio de ayuda'

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

lista_busqueda = re.findall(patron, texto)
print(lista_busqueda)
print(len(lista_busqueda))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto = 'Llama al 555-456-2244 ya mismo'
patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron_cuantificado = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron, texto)
print(resultado.group())

resultado = re.search(patron_cuantificado, texto)
print(resultado.group())

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
print(resultado.group(2))
print(resultado.group(1))

clave = input('Clave: ')
patron = r'\D{1}\w{7}'

checar = re.search(patron, clave)
print(checar)

texto = 'Los lunes no se chambea por la tarde'
buscar = re.search(r'lunes|martes', texto)
print(buscar)

buscar = re.search(r'...bea....', texto)
print(buscar)

buscar = re.findall(r'[^\s]+', texto)
print(buscar)
