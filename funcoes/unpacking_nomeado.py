
def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'segundo': 'M. Verstappen',
              'terceiro': 'S. Vettel',
              'primeiro': 'L. Hamilton'}
    # com o ** é feito o desempacotamento do dicionário e é informado
    # como parâmetros os valores corretamente
    # observação: o dicionário não pode conter mais membros do que o numero de
    # argumentos da funcão
    resultado_f1(*podium)
    # saída
    # 1) L. Hamilton
    # 2) M. Verstappen
    # 3) S. Vettel
    # se passar com *, somente as chaves são enviadas, na ordem que aparecem
    # 1) segundo
    # 2) terceiro
    # 3) primeiro
