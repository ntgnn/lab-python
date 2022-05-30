
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    # nesse caso, como o argumento da funcao tem **, os argumentos nomeados
    # serão transformados em um dicionário (pelo packing)automático
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
