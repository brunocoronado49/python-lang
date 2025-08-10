url_file = '/home/bruce117/Documents/Dev/Languajes/python-lang/06-dia/prueba.txt'
my_file = open(url_file)

# all_file = my_file.read()
# print(f'All the file:\n{all_file}')

one_line = my_file.readline()
print(one_line)

# for line in my_file:
#     print(f'***** {line}')

# all_lines_2 = my_file.readlines() <- retorna una lista
# print(all_lines_2)

my_file.close()
