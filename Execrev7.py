from typing import List, Union

def calcular_media(numeros: List[Union[int, float]]) -> Union[float, None]:
    # Verifica se a lista está vazia
    if len(numeros) == 0:
        return None
    
    # Calcula a soma dos números e divide pelo número de elementos
    return sum(numeros) / len(numeros)

# Testes
print(calcular_media([10, 20, 30, 40, 50]))  # Esperado: 30.0
