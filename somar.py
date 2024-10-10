def somar(a, b):
    return a + b

def realizar_soma(num1, num2):
    # Chamar somar de forma reentrante
    return somar(num1, num2)

# Funções sample para mostrar que cada chamada é independente
print(realizar_soma(10, 20))  # Saída: 30
print(realizar_soma(5, 7))    # Saída: 12
