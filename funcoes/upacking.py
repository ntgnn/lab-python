
def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # Packing = empacotamento de vários valores em uma tupla e passando para
    # a função
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))

    # Unpacking = desempacotamento e espalhamento
    # O * faz o espalhamento dos valores da tupla nos parâmetros da função
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))

    # O * faz o espalhamento tambem de valores de uma lsita
    lista_nums = [1, 2, 3]
    print(soma_3(*lista_nums))
