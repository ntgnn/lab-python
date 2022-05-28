
with open('pessoas.csv', encoding='utf-8') as arquivo:
    with open('pessoas.txt', encoding='utf-8', mode='w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!')

if saida.closed:
    print('Arquivo de saída já foi fechado!')
