from generadores_proyecto import *


def preguntar():
    print('Bienvenido a Farmacias Saladillo')
    
    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos\n')
        
        try:
            mi_rubro = input('Elije tu rubro: ').lower()
            ['p', 'f', 'c'].index(mi_rubro)
        except ValueError as e:
            print(f'No es opcion valida: {e}')
        else:
            break
    
    decorador(mi_rubro)
    

def inicio():
    while True:
        preguntar()
        
        try:
            otro_turno = input('Deseas sacar otro turno? [s][n]').lower()
            ['s', 'n'].index(otro_turno)
        except ValueError as e:
            print(f'No es opcion valida: {e}')
        else:
            if otro_turno == 'n':
                print('Gracias por su visita!')
                break


inicio()
