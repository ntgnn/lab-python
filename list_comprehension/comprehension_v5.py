
# Exemplo de dict generator = chave : valor
# Nesse caso, as chaves serão os números do range de 0 a 9
# e os valores serão o seu dobro, SE o número do range for par
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)
# {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}

dicionario2 = {f'item_{i}': i * 2 for i in range(10) if i % 2 == 0}
print(dicionario2)
# {'item_0': 0, 'item_2': 4, 'item_4': 8, 'item_6': 12, 'item_8': 16}

# Percorrenr dicionário gerado
for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
