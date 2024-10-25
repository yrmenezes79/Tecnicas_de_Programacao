with open("impacta.jpg", "rb") as arquivo:
    dados = arquivo.read()
    print(dados[:20])  # Exibe os primeiros 20 bytes
