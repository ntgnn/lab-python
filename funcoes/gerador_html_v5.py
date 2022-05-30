
# Tuplas usadas para filtrar os atributos
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados: dict, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)

#  recebe bloco_accesskey='m', bloco_id='conteudo', ul_id='lista' e retorna
#  sem os prefixos accesskey='m', id='conteudo', id='lista'


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
    atrs = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atrs} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    # Generator que percorre todos os elementos da tupla informada
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    # Também pode sert um list comprehension, exemplo:
    # lista = ''.join([f'<li>{item}</li>' for item in itens])
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))

    # após a passagem de parâmetros com o packing, somente parâmetros nomeados
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', False)) # Erro
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=False))

    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='clor:red'))
