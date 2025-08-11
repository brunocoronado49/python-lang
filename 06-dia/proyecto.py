import os
from pathlib import Path
from os import system


my_route = Path(Path.home(), 'Documents', 'Dev', 'Languajes', 'python-total')

def count_recetas(route):
    counter = 0
    for txt in Path(route).glob('*.txt'):
        counter += 1
    
    return counter


def inicio():
    system('clear')
    print('*' * 50)
    print('bienvenido al administrador de recetas'.upper())
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en {my_route}')
    print(f'Total de recetas: {count_recetas(my_route)}')
    
    election_menu = 'x'
    while not election_menu.isnumeric() or int(election_menu) not in range(1,7):
        print('Elije una opcion:')
        print('''
        [1] Leer receta
        [2] Crear nueva receta
        [3] Crear nueva categoria
        [4] Eliminar receta
        [5] Eliminar categoria
        [6] Salir del programa
        ''')
        election_menu = input('Opcion: ')
        
    return (election_menu)


def show_caregories(route):
    print('Categorias:')
    categories_route = Path(route)
    list_categories = []
    counter = 1
    
    for folder in categories_route.iterdir():
        folder_str = str(folder.name)
        print(f'[{counter}] - {folder_str}')
        list_categories.append(folder)
        counter += 1
        
    return list_categories


def choose_categories(list_categories):
    choose_correct = 'x'
    
    while not choose_correct.isnumeric() or int(choose_correct) not in range(1, len(list_categories) + 1):
        choose_correct = input('\nElije una categoria: ')
    
    return list_categories[int(choose_correct) - 1]


def show_recipes(route):
    print('Recetas:')
    route_recipes = Path(route)
    recipes_list = []
    counter = 1
    
    for recipe in route_recipes.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f'[{counter}] - {recipe_str}')
        recipes_list.append(recipe)
        counter += 1
        
    return recipes_list


def choose_recipes(list_recipes):
    choose_recipe = 'x'
    
    while not choose_recipe.isnumeric() or int(choose_recipe) not in range(1, len(list_recipes) + 1):
        choose_recipe = input('\nElije una receta: ')
        
    return list_recipes[int(choose_recipe - 1)]


def redad_recipe(recipe):
    print(Path.read_text(recipe))
    

def create_recipe(route):
    exists = False
    
    while not exists:
        print('Receta nueva'.upper())
        recipe_name = input('Escribe el nombre de la receta nueva: ') + '.txt'
        recipe_content = input('Escribe el contenido de tu receta nueva: ')
        new_route = Path(route, recipe_name)
        
        if not os.path.exists(new_route):
            Path.write_text(new_route, recipe_content)
            print(f'Tu receta {recipe_name} ha sido creada!')
            exists = True
        else:
            print('Esa receta ya existe')
            

def create_category(route):
    exists = False
    
    while not exists:
        print('Categoria nueva'.upper())
        category_name = input('Escribe el nombre de la categoria nueva: ')
        new_route = Path(route, category_name)
        
        if not os.path.exists(new_route):
            Path.mkdir(new_route)
            print(f'Tu categoria {category_name} ha sido creada!')
            exists = True
        else:
            print('Esa categoria ya existe')


def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f'La receta {recipe.name} ha sido eliminada!')


def delete_category(category):
    Path(category).rmdir()
    print(f'La categoria {category.name} ha sido eliminada!')
    

def back_menu():
    election_back = 'x'
    
    while election_back.lower() != 'v':
        election_back = input('\nPresiona "v" para volver al inicio del menu: ').lower()


ending_program = False

while not ending_program:
    menu = inicio()

    if menu == 1:
        my_categories = show_caregories(my_route)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_route)
        my_recipe = choose_recipes(my_recipes)
        redad_recipe(my_recipe)
        back_menu()
        
    elif menu == 2:
        my_categories = show_caregories(my_route)
        my_category = choose_categories(my_categories)
        create_recipe(my_category)
        back_menu()
        
    elif menu == 3:
        create_category(my_route)
        back_menu()
        
    elif menu == 4:
        my_categories = show_caregories(my_route)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_route)
        my_recipe = choose_recipes(my_recipes)
        delete_recipe(my_recipe)
        back_menu()
        
    elif menu == 5:
        my_categories = show_caregories(my_route)
        my_category = choose_categories(my_categories)
        delete_category(my_category)
        back_menu()
        
    elif menu == 6:
        ending_program = True
        
