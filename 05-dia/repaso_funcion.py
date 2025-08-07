precios_cafe = [('Capuchino', 100), ('Expreso', 120), ('Moka', 93)]

def precio_mayor(lista_precios):
    precio_mayor = 0
    cafe_caro = ''
    
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
    
    return (cafe_caro, precio_mayor)

cafe, precio = precio_mayor(precios_cafe)
print(f'El cafe mas caro es el {cafe} y su precio es de ${precio}.00 MXN')

