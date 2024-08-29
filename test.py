
print('Starts')
print('-'*20)
def the_one_decorator(func):
    print('the_one_decorator runs!')
    var = None
    def wrapper(*args, **kwargs):
        print('Wrapper starts')
        nonlocal var
        print(wrapper.deklarerad_variabel_utanför_funktionen)
        val = func(*args, **kwargs)
        print('Wrapper ends')
        return val
    
    wrapper.deklarerad_variabel_utanför_funktionen = 'Hejsan123'
    return wrapper

print('Something')
print('-'*20)

@the_one_decorator
def the_one_and_only_func(*args, **kwargs):
    print('The function runs')
    print(f'The arguments were {args} and {kwargs}')
    print('Function ends')

@the_one_decorator
def some_func():
    print('Hello world!')

print('-'*20)
print('         PROGRAM STARTS        ')
print('-'*20)
the_one_and_only_func(1,2,3,hello='hejsan', godbye='hejdå')
print('-'*20)
the_one_and_only_func()
print('-'*20)