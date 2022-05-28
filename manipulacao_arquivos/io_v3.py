arquivo = open('pessoas.csv', encoding='utf-8')

for registro in arquivo:
    print('Nome: {}\t | Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
