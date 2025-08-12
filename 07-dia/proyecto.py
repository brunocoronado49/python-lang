class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}\nCuenta {self.numero_cuenta}: ${self.balance}'
                    
    
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')
    
    
    def retirar(self, monto_retiro):
        if monto_retiro <= self.balance:
            self.balance -= monto_retiro
            print('Retiro realizado')
        else:
            print('No cuenta con fondos suficientes')


def crear_cliente():
    nombre_cliente = input('Ingrese su nombre: ')
    apellido_cliente = input('Ingrese su apellido: ')
    no_cuenta = input('Ingrese su numero de cuenta: ')
    
    cliente1 = Cliente(nombre_cliente, apellido_cliente, no_cuenta)
    
    return cliente1


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    
    opcion = 0
    
    while opcion != 's':
        print('Elije una opcion: Depositar [d], Retirar [r], Salir [s]')
        opcion = input('opcion: ').lower()
        
        if opcion == 'd':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'r':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
            
        print(mi_cliente)
        
print('Gracias por operar en BancoPy')

inicio()
