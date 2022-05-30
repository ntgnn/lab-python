
# *args = parâmetros posicionais de número variado
# **kwargs = parâmetros nomeados de número variado
# para evitar conflitos, sempre os posicionais vem antes dos nomeados
def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    # args: ('a', 'b', 'c')
    # kwargs: {}
    todos_params(1, 2, 3, legal=True, valor=12.99)
    # args: (1, 2, 3)
    # kwargs: {'legal': True, 'valor': 12.99}
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # args: ('Ana', False, [1, 2, 3])
    # kwargs: {'tamanho': 'M', 'fragil': False}
    # todos_params(primeiro='João', 'Maria') # Erro, posicional depois
    todos_params('Maria', primeiro='João')
    # args: ('Maria',)
    # kwargs: {'primeiro': 'João'}
