import math

def calcular_hipotenusa(cateto1: float, cateto2: float) -> float:
    """Calcula a hipotenusa de um triângulo retângulo utilizando o Teorema de Pitágoras."""
    return math.sqrt(cateto1**2 + cateto2**2)

# Exemplo de uso
cateto1 = 3
cateto2 = 4

hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f"A hipotenusa do triângulo com catetos {cateto1} e {cateto2} é: {hipotenusa}")
