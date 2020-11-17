
def protected(func):

    def wrapper(password):
        
        if password == 'platzi':
            return func()
        else:
            print('El password es incorrecto.')

    return wrapper


@protected
def protected_func():
    print('Tu password es correcto.')


if __name__ == '__main__':
    password = str(input('Ingresa tu password: '))

    protected_func(password)
