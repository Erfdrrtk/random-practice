# function stuff
def f(x):
    print(x ** 2 + 1)
f(2)

def buildings(owner, founder):
    print(f'the owner of apple of apple is {owner}. the founder of apple is {founder}')

buildings('dave', 'mom')


def f(a, add_three_to_a):
    a = a + add_three_to_a
    print(a ** 2 + 1)
f(5, 3)


def greet(language):
    if language == 'spanish':
        print('hola')
    elif language == 'french':
        print('Bonjour')
    else:
        print('Hello')

greet('spanish')
greet('french')


print("\U0001f600")