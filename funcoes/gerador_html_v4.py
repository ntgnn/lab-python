

def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    # Generator que percorre todos os elementos da tupla informada
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    # Também pode sert um list comprehension, exemplo:
    # lista = ''.join([f'<li>{item}</li>' for item in itens])
    return f'<ul>{lista}</ul>'


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
