
# Exemplo de generator
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # 0^0 = saída 0
print(next(generator))  # 2^2 = saída 4
print(next(generator))  # 4^2 = saída 16
print(next(generator))  # 6^2 = saída 36
print(next(generator))  # 8^2 = saída 64
# print(next(generator))  # 10^2 = Erro! (10 não está no range)


# A diferença do generator para o list comprehension é que o generator
# não gera de imediato todos os elementos da lista, vai gerando sob demanda
# e com isso ocupa menos memória
