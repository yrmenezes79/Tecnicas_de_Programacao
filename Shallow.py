import copy

lista_e = [1, 2, [3, 4]]
lista_f = copy.copy(lista_e)  # Cópia superficial de lista_e

lista_f[2].append(5)  # Modifica a sublista dentro de lista_f

print("lista_e:", lista_e)  # Saída: [1, 2, [3, 4, 5]]
print("lista_f:", lista_f)  # Saída: [1, 2, [3, 4, 5]]
