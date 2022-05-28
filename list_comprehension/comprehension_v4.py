
# Exemplo de generator
generator = (i ** 2 for i in range(10) if i % 2 == 0)
for numero in generator:
    print(numero)

# 0
# 4
# 16
# 36
# 64

# Podemos usar o generator com o laço for, e a sinmtaxe fica muito mais siples
