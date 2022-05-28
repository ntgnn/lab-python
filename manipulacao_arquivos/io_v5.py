
with open('pessoas.csv', encoding='utf-8') as arquivo:
    for registro in arquivo:
        print('Nome: {}\t | Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
