def soma_unicos(numeros: list[int]) -> int:
    """Retorna a soma dos números únicos de uma lista."""
    return sum(set(numeros))

# Teste
print(soma_unicos([1, 2, 2, 3, 3, 4]))  # Saída: 10
