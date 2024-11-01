def encontrar_pares(lista, valor_soma):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == valor_soma:
                pares.append((lista[i], lista[j]))
    return pares

# Exemplo de uso
lista = [2, 4, 3, 6, 1, 7]
valor_soma = 7
resultado = encontrar_pares(lista, valor_soma)
print("Pares encontrados:", resultado)

