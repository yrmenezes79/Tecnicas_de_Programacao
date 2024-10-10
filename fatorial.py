def fatorial(n):
    # Caso Base
    if n == 0 or n == 1:
        return 1
    # Caso Recursivo
    return n * fatorial(n - 1)

# Testando a função
print(fatorial(5))  # Saída: 120
