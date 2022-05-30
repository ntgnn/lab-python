

class Potencia:
    # Calcula uma potência específica
    # Em Python/OO:
    # - o método __init__ é o construtor da classe
    # - o primeiro parâmetro dos métodos de uma classe ésempre a instância da classe
    def __init__(self, expoente):
        self.expoente = expoente

    # o método __call__ é usado para definir o comportamento do objeto
    # quando ele é chamdo como uma função
    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    # Instanciação da classe Potencia
    # perceba que nao existe a palavra reservada new
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3^2 => {quadrado(3)}')
        print(f'2^3 => {cubo(2)}')
        print(f'5^3 => {cubo(5)}')
        # Outra forma de chamar, diretamente
        print(f'2^4 => {Potencia(4)(2)}')
        # 3^2 => 9
        # 2^3 => 8
        # 5^3 => 125
        # 2^4 => 16

# MUITO IMPORTANTE!!
#
# Evitar usar objetos mutáveis como parâmetros de funções (ex.: listas),
# pois o python reutiliza os objetos nesse caso!!! Se for usar objetos como
# parâmetros, dar preferência a tuplas, que não são mutáveis.
# JS tbm passa por este problema!
#
# Alternativamente, podemos definir o valor padrão como None (nulo) + OU e verificar
# internamente, por exemplo:
#
# def fibonacci(sequencia=None)
#     sequencia = sequencia or [0, 1]
