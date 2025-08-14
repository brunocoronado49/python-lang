def return_number():
    return 4


def generate_number():
    yield 4


print(return_number())
print(generate_number())
g = generate_number()
print(next(g))


def generate_list_number():
    for num in range(1, 5):
        yield num * 10
        

g = generate_list_number()
print(next(g))
print(next(g))
print(next(g))
