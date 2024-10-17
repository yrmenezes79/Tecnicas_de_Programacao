import random

# Gerando 10 números aleatórios entre 1 e 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("Números aleatórios:", numeros_aleatorios)

# Lista de nomes
nomes = ["Ana", "Carlos", "Bianca", "Pedro", "João", "Marina"]

# Escolhendo um nome aleatório
nome_escolhido = random.choice(nomes)
print("Nome escolhido:", nome_escolhido)
