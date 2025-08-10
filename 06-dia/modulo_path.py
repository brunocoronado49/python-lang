from pathlib import Path


base = Path.home()
guia = Path(base, 'America', 'Mexico', 'Zacatecas.pdf')
guia2 = guia.with_name('El_Saladillo.pdf')
print(guia)
print(guia2)

print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)

guia = Path(base, 'Documents', 'Roadmaps')
for file in Path(guia).glob('*.pdf'):
    print(f'Documentos PDF: {file}')

