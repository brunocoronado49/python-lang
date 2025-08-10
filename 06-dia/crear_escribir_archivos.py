url_file = '/home/bruce117/Documents/Dev/Languajes/python-lang/06-dia/prueba1.txt'
my_file = open(url_file, 'w') # Sobrescribe todo el archivo
my_file.write('I am the first line\n')
my_file.write('I am the last line until now\n')
my_file.writelines(['hola','mundo','buenas','tardes\n'])

lista = ['hola','mundo','buenas','tardes']

for l in lista:
    my_file.write(l+'\n')

my_file.close()
