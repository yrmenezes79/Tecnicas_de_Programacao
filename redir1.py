# Redirecionamento de saída
with open("exemplo.txt", "w") as arquivo:
    print("Texto de exemplo", file=arquivo)
