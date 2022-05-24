esta_chovendo = False

# Podemos usar colchetes nesse caso a ordem é (caso F, caso V)[valor]
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])

# Podemos usar o if/else inline, nesse caso a ordem é caso V if valor else caso F
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))
