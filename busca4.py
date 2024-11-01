def buscar_produto(produtos, codigo):
    esquerda = 0
    direita = len(produtos) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if produtos[meio] == codigo:
            return meio  
        elif produtos[meio] < codigo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return "Produto não encontrado"  

produtos = [101, 205, 301, 405, 501, 603, 702]

print(buscar_produto(produtos, 301))  

