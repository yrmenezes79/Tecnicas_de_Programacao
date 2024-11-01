def busca_binaria(arr, valor):
    inicio, fim = 0, len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == valor:
            return meio
        elif arr[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
conteudo = busca_binaria([1,2,3,4,5,6,7],7)
print(conteudo)