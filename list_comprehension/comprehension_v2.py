

# Trata-se de uma forma mais concisa de estruturar listas

# Exemplo de comprehension para criar uma lista de dobros, dos números de 0 a 9
dobros = [i * 2 for i in range(10)]
print('Dobros: ', dobros)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Código equivalente em versão normal
dobros = []
for i in range(10):
    dobros.append(i * 2)
print('Dobros: ', dobros)
# Dobros:  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Exemplo de comprehension para criar uma lista de dobros, dos números pares
# de 0 a 9 (com condicional)
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print('Dobros dos pares: ', dobros_dos_pares)
# Dobros dos pares:  [0, 4, 8, 12, 16]

# Código equivalente em versão normal
dobros_dos_pares = []
for i in range(10):
    if i % 2 == 0:
        dobros_dos_pares.append(i * 2)
print('Dobros dos pares: ', dobros_dos_pares)
# Dobros dos pares:  [0, 4, 8, 12, 16]
