import csv

with open('pessoas.csv', encoding='utf-8') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))

print('Última pessoa:')
print(pessoa)
