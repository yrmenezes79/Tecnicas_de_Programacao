# Criando uma lista com diferentes tipos de elementos
minha_lista = [10, "Impacta", 2.18, [1, 2, 3]]

# Exibindo a lista original
print("Lista Original:", minha_lista)

# Acessando elementos individuais
print("Primeiro Elemento:", minha_lista[0])  
print("Segundo Elemento:", minha_lista[1])   
print("Ultimo Elemento (uma lista):", minha_lista[3])  

minha_lista[1] = "Mundo"
print("Lista Apos Modificacao:", minha_lista)

# Adicionando um novo elemento à lista
minha_lista.append(42)
print("Lista Apos Adicionar Elemento:", minha_lista)

# Modificando um elemento dentro da sublista
minha_lista[3][0] = 99
print("Lista Apos Modificacao na Sublista:", minha_lista)
