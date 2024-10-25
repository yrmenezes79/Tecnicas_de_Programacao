def gravar_texto():
    with open("meu_arquivo.txt", "w") as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        arquivo.write("Linha 3\n")

def adicionar_texto():
    with open("meu_arquivo.txt", "a") as arquivo:
        arquivo.write("Linha 4 - Adicionada\n")
        arquivo.write("Linha 5 - Adicionada\n")

def ler_texto():
    with open("meu_arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

gravar_texto()
adicionar_texto()
ler_texto()


