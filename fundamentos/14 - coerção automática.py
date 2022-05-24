
# A divsão de 2 inteiros é sempre um float
print(type(10/2))  # float


# Para o resultado inteiro ou float devemos usar o //
print(type(10//3))  # int
print(type(10//3.2))  # float
print(type(10//2.5))  # float

# Coerção automática de boolean True, vale 1
print(2 + True)  # 3

# Coerção automática de boolean False, vale 0
print(2 + False)  # 2
