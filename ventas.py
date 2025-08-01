precio_productos = []
subtotal = 0
pago = 0
cambio = 0
cantidad_productos = int(input('Ingresa la cantidad de productos: '))

for i in range(cantidad_productos):
    precio = float(input(f'Ingresa el precio del producto No. {i+1}: '))
    precio_productos.append(precio)

for i in precio_productos:
    subtotal += i

print(f'El subtotal es: {subtotal}')
pago = float(input('Ingresa la cantidad que vas a pagar: '))

if pago > subtotal:
    cambio = pago - subtotal

if cambio != 0:
    print(f'Su cambio es de {round(cambio)}')

print('Gracias por su compra. Y NO VUELVA!')

