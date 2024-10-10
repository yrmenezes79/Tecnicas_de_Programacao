def fibonacci(n):
    # Caso Base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso Recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testando a função
for i in range(10):
    print(fibonacci(i), end=" ")  # Saída: 0 1 1 2 3 5 8 13 21 34
