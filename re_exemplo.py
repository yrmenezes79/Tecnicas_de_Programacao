import re

# Procurar uma correspondência em uma string
texto = "Meu número de telefone é 123-456-7890"
padrao = r'\d{3}-\d{3}-\d{4}'  # Expressão regular para um número de telefone

resultado = re.search(padrao, texto)
if resultado:
    print(f"Número encontrado: {resultado.group()}")
else:
    print("Nenhum número encontrado.")
