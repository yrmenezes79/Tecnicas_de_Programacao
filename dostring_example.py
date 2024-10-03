def soma(a, b):
    """
    Soma dois números.

    Args:
        a (int or float): O primeiro número.
        b (int or float): O segundo número.

    Returns:
        int or float: A soma de `a` e `b`.
    """
    return a + b

def subtracao(a, b):
    """
    Subtrai dois números.

    Args:
        a (int or float): O número a ser subtraído.
        b (int or float): O número subtraído de `a`.

    Returns:
        int or float: O resultado da subtração de `a` por `b`.
    """
    return a - b

def divisao(a, b):
    """
    Divide dois números.

    Args:
        a (int or float): O numerador.
        b (int or float): O denominador.

    Returns:
        float or str: O resultado da divisão de `a` por `b` ou uma mensagem de erro se `b` for zero.
    """
    if b == 0:
        return "Erro: divisão por zero."
    return a / b
