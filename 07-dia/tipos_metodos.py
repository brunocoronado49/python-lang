class Dog:
    cute = True
    
    def __init__(self, name, type):
        '''Constructor'''
        self.name = name
        self.type = type
        
    
    def bark(self):
        '''Metodo de instancia'''
        print(f'Woof! Hola, soy {self.name}!')
        self.walk(20)
        
    
    def walk(self, mts):
        '''Metodo de instancia'''
        print(f'El perro ha caminado {mts} metros')
        
    
    def shower(self):
        '''Metodo de instancia'''
        self.type = 'Mestizo'
        print(f'Ahora {self.name} es {self.type} ')
        
    
    @classmethod
    def eat(cls, food):
        '''Metodo de clase'''
        print(f'Esta comiendo {food}')
        cls.cute = False
        print(cls.cute)
        
    
    @staticmethod
    def watch():
        '''Metodo estatico'''
        print('El perro ladra')


zeus = Dog('Zeus', 'Pastor')
print(f'Mi mascota se llama {zeus.name} y es una {zeus.type}')
zeus.bark()
zeus.shower()

Dog.eat('Croquetas')
Dog.watch()
