def insertion_sort(lista: list[int]) -> list[int]:
    """Ordena uma lista usando o algoritmo insertion sort."""
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Teste
print(insertion_sort([5, 2, 9, 1, 5, 6]))  # Saída: [1, 2, 5, 5, 6, 9]
