def calcular_media(numeros: list[float]) -> float:
    """
    Calcula a média de uma lista de números.

    Parâmetros:
        numeros (list[float]): Uma lista de números (inteiros ou decimais) para calcular a média.
    
    Retorna:
        float: A média dos números fornecidos. Se a lista estiver vazia, retorna 0.0.

    Exemplo:
        >>> calcular_media([10, 20, 30])
        20.0
        >>> calcular_media([])
        0.0
    """
    if not numeros:  # Verifica se a lista está vazia
        return 0.0
    return sum(numeros) / len(numeros)


# Teste
if __name__ == "__main__":
    # Exibindo a docstring da função
    help(calcular_media)
    
    # Testando a função
    print(calcular_media([10, 20, 30]))  # Saída esperada: 20.0
    print(calcular_media([]))           # Saída esperada: 0.0
