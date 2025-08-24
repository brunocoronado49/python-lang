import zipfile


mi_zip = zipfile.ZipFile('archivo_comprimido_dia_9.zip', 'w')
mi_zip.write('texto_a.txt')
mi_zip.write('texto_b.txt')
mi_zip.close()
