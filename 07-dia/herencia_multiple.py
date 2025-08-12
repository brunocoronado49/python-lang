class Padre:
    def hablar(self):
        print('Hola')
        

class Madre:
    def reir(self):
        print('Jaja')
        
    
    def hablar(self):
        print('Que tal')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar() # Hereda de padre, ya que esta en orden y es el primero
mi_nieto.reir()

print(Nieto.__mro__) # Muestra el orden de resolucion de metodos
