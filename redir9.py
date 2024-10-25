def copiar_arquivo():
    with open("meu_arquivo.txt", "r") as original:
        conteudo = original.read()
    with open("copia_meu_arquivo.txt", "w") as copia:
        copia.write(conteudo)

    # Confirme a cópia
    with open("copia_meu_arquivo.txt", "r") as copia:
        print("Conteúdo do arquivo copiado:")
        print(copia.read())

copiar_arquivo()



