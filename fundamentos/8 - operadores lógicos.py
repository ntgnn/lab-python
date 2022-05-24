# Operador OU
print(True or False)

# Operador E
print(7 != 3 and 2 > 3)

# Operador XOU (não existe operador específico, então usa o != ou a função xor())
print(True != True)

# Operador NÃO
print(not True)
print(not False)
print(not 0)
print(not 1)

# Outras formas de booleano é com 0 ou 1
print('Outra forma de booleano')
print(not 0)

# Cuidado!
# Operadores bit a bit têm comportamentos diferentes, exceto quanto aos booleanos

# Operador E bit a bit
print(True & True)

# Operador OU bit a bit
print(True | False)

# Operador XOR bit a bit
print(False ^ False)

# Exemplo com os operadores E, OU e XOU, bit a bit com inteiro
# 3 == 0b11
# 2 == 0b10

# 3 & 2 == 2 (ou 0b10)
print(3 & 2)

# 3 | 2 == 3 (ou 0b11)
print(3 | 2)

# 3 ^ 2 == 1 (ou 0b01)
print(3 ^ 2)

# Exemplo
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas

# Desafio
trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saudavel = not sorvete

# Print com format
print("Tv50={} Tv32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))

# Print com interpolation
print(f"Tv50={tv_50} Tv32={tv_32} Sorvete={sorvete} Saudável={mais_saudavel}")
