from decimal import Decimal, getcontext

a = 5
b = 2.5
print(type(a / b))  # float
print(type(a + b))  # float
print(type(a * b))  # float

print(b.is_integer())
print(b.as_integer_ratio()[1])

# A função as integer analisa se o conteúdo possui ou não casas decimais
x = 4
y = 2.5
z = x * y
print(type(x))  # int
print(type(y))  # float
print(type(z))  # float
print(y)
print(y.is_integer())  # 2.5 é float e possui casa decimal
print(z)
print(z.is_integer())  # 10.0 é float, mas não possui casa decimal

res1 = 1.1 + 2.2
print(res1)  # 3.3000000000000003
print(res1 == 3.3)  # False, o mesmo problema ocorre com javascript

# Para evitar esse prblema, podemos usar o Decimal
res2 = Decimal('1.1') + Decimal('2.2')
print(res2)  # 3.3
print(res2 == 3.3)  # False
print(res2 == Decimal('3.3'))  # True
