import zipfile
import shutil


mi_zip = zipfile.ZipFile('archivo_comprimido_dia_9.zip', 'w')
mi_zip.write('texto_a.txt')
mi_zip.write('texto_b.txt')
mi_zip.close()

carpeta_origen = '/home/bruce117/Documents/Resume'
archivo_destino = 'CV_COMPRIMIDO'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
