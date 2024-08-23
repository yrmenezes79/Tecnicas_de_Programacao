lista_a = [1, 2, 3]
lista_b = lista_a  # lista_b referência para o objeto que lista_a

lista_b.append(4)  # Adiciona 4 à lista referenciada por lista_b

print("lista_a:", lista_a)  # Saída: [1, 2, 3, 4]
print("lista_b:", lista_b)  # Saída: [1, 2, 3, 4]
