nome = 'Saulo Pedro'
print(nome)
print(nome[0])

print("marca d'agua")
print('marca d"agua')
print('marca d\'agua')

# No python o início é incluído, mas o final não é incluído
print(nome[2:])
print(nome[:2])

# Ordem reversa
print(nome[::-1])

# Operações de membro com string
print("Ped" in nome)

# É case-sensitive
print("sau" in nome.lower())
