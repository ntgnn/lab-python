
# Simulando switch com o tuplas e generator
def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        # Alternativa = (2, 3, 4, 5, 6): 'Dia de semana'
        tuple(range(2, 7)): 'Dia de semana'
    }
    # generator que percorre o dicionário e retorna o tipo (fim de semana / dia de semana)
    # caso o dia seja encontrado em uma das chaves
    dia_escolhido = (valor for chave, valor in dias.items() if dia in chave)
    # chamamos o generator com o next
    return next(dia_escolhido, '** dia inválido **')


for dia in range(9):
    print(f'{dia} : {get_tipo_dia(dia)}')

# 0 : ** dia inválido **
# 1 : Fim de semana
# 2 : Dia de semana
# 3 : Dia de semana
# 4 : Dia de semana
# 5 : Dia de semana
# 6 : Dia de semana
# 7 : Fim de semana
# 8 : ** dia inválido **
