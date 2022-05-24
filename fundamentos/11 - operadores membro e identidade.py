# Operador de membro
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Carla' in lista)
print(lista)

# Identidade com tipos primitivos, copiados por valor
x = 3
y = x
z = 3

print(x == z)  # True
print(x is y)  # True
print(x is z)  # True

# Identdade com tipos complexos, copiados por referência
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)  # True
print(lista_a is lista_c)  # False
