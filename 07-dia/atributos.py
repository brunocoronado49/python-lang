class Dog:
    patas = True
    
    def __init__(self, d_name, type):
        self.d_name = d_name
        self.type = type


print(Dog.patas)
seven = Dog('Seven', 'Pastor Belga Malinois')
print(seven.d_name)
print(seven.type)

print(f'Mi perro se llama {seven.d_name} y es un {seven.type}')
