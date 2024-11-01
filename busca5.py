def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        # Procura pelo menor elemento nos elementos não ordenados
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

contagem = selection_sort([1,56,34,22,10])
print(contagem)