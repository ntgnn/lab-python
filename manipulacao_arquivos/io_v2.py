arquivo = open('pessoas.csv', encoding='utf-8')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
