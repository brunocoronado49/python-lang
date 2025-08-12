class Dog:
    cute = True
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    
    def bark(self):
        print(f'Woof! Hola, soy {self.name}!')
        
    
    def walk(self, mts):
        print(f'El perro ha caminado {mts} metros')


melina = Dog('Melina', 'Putbull blue')
print(f'Mi mascota se llama {melina.name} y es una {melina.type}')
melina.bark()
melina.walk(10)
