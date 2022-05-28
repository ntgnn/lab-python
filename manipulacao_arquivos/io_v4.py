
try:
    arquivo = open('pessoas.csv', encoding='utf-8')

    for registro in arquivo:
        print('Nome: {}\t | Idade: {}'.format(*registro.strip().split(',')))

except IndexError:
    pass

finally:
    print('finally')
    arquivo.close()


if arquivo.closed:
    print('Arquivo já foi fechado!')
