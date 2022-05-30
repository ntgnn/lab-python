# Implementação do design pattern decorator em python
# log = decorator
# function = função que vai ser decorada
# resultado = resultado da função decorada


def log(function):
    def decorator(*args, **kwargs):
        # Como uma função é um objeto (callable) conseguimos acessar as
        # propriedades dela, como o nome, por exemplo
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


# Com o @ + nome da função decorator, o python faz todo o mapeamento
# necessário
@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
