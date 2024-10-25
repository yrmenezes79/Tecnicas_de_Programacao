def gravar_texto():
    with open("meu_arquivo.txt", "w") as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        arquivo.write("Linha 3\n")

def ler_texto():
    with open("meu_arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# Chame as funções
gravar_texto()
ler_texto()


