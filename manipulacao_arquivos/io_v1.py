
arquivo = open('pessoas.csv', encoding='utf-8')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

