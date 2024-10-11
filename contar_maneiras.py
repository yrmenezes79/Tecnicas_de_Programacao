def contar_maneiras(n):
    # Caso base: escada com 0 ou 1 degrau
    if n == 0 or n == 1:
        return 1
    
    # Chamada recursiva para escadas menores
    return contar_maneiras(n - 1) + contar_maneiras(n - 2)

# Testando a função
print(contar_maneiras(3))  # Saída esperada: 3
print(contar_maneiras(4))  # Saída esperada: 5
