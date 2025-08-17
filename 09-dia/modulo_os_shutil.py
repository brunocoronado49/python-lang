import os
import shutil


print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba')
archivo.close()

print(os.listdir())

shutil.move('curso.txt', '/home/bruce117/Desktop')

ruta = '/home/bruce117/Documents/Dev'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: {subcarpeta}')
    print(f'Y los archivos son: {archivo}')
    
