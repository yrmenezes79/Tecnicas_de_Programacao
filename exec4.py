# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero >= 0:
    print(f"Números pares de 0 até {numero}:")
    # Loop para exibir os números pares
    for i in range(0, numero + 1):
        if i % 2 == 0:  # Verifica se o número é par
            print(i)
else:
    print("Por favor, insira um número inteiro positivo.")
