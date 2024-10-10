def soma_lista(lista):
    # Caso Base
    if len(lista) == 0:
        return 0
    # Caso Recursivo
    return lista[0] + soma_lista(lista[1:])

# Testando a função
numeros = [1, 2, 3, 4, 5]
print(soma_lista(numeros))  # Saída: 15
