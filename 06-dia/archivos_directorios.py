import os
from pathlib import Path


# route = os.chdir('/home/...') <- Change directory
# route = os.makedirs('/home/...) <- Create directory

url_file = '/home/bruce117/Documents/Dev/Languajes/python-lang/06-dia/prueba1.txt'
element = os.path.basename(url_file)
directorio = os.path.dirname(url_file)
print(element)
print(directorio)

# Para romar la ruta completa en cualquier SO
folder = Path('/home/bruce117/Documents/Dev/Languajes/python-lang/06-dia')
my_file = folder / 'prueba.txt'
open_file = open(my_file)
print(open_file.readline())

route = os.getcwd()
print(route)
