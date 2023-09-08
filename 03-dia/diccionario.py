diccionario = {
    'nombre': 'Sabine',
    'apellido': 'Wren',
    'edad': 25,
    'tipo': 'Mandaloriana',
    'amigos': {
        'nombre': 'Ahsoka'
    }
}

print(type(diccionario))
print(diccionario)
print(diccionario['nombre'])
print(diccionario['amigos']['nombre'])

mi_dict = {
    "c1": ["a", "b", "c"],
    "c2": ["d", "e", "f"]
}
print(mi_dict["c2"][1].upper())
print(mi_dict["c1"][0].upper())

otro_dic = {
    "c1": "a",
    "c2": "b"
}
print(otro_dic)
otro_dic["c3"] = "c"
print(otro_dic)

print(otro_dic.keys())
print(otro_dic.values())
print(otro_dic.items())
