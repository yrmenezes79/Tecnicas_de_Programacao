import copy

# Lista original (lista de listas)
lista_original = [[1, 2, 3], [4, 5, 6]]

# Cópia profunda (deep copy)
copia_profunda = copy.deepcopy(lista_original)

# Modificando a cópia profunda
copia_profunda[0][0] = 10
copia_profunda[1][1] = 20

# Exibindo as listas após a modificação
print("Lista Original:", lista_original)        # Saída: [[1, 2, 3], [4, 5, 6]]
print("Cópia Profunda:", copia_profunda)        # Saída: [[10, 2, 3], [4, 20, 6]]

