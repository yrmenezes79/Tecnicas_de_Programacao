with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Primeira linha\nSegunda linha")
with open("exemplo.txt", "r") as arquivo:
    print(arquivo.read())
