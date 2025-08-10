# Permite manipular rutas del sistema de archivos
# en cualquier SO
from pathlib import Path, PureWindowsPath


folder = Path('/home/bruce117/Documents/Dev/Languajes/python-lang/06-dia/prueba1.txt')
folder_windows = PureWindowsPath(folder)

print(folder.read_text())
print(folder.name)
print(f'Ruta en Windows: {folder_windows}')

if not folder.exists():
    print('El archivo no existe')
else:
    print(f'El titulo es: {folder.stem} y es de formato {folder.suffix}')
    
