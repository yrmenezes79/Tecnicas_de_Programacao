# Definindo a função recursiva para resolver o problema da Torre de Hanói
def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    # Mover n-1 discos da origem para a auxiliar
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    # Mover o disco restante da origem para o destino
    print(f"Mova o disco {n} de {origem} para {destino}")
    # Mover os n-1 discos da auxiliar para o destino
    torre_de_hanoi(n-1, auxiliar, destino, origem)

# Testando com 3 discos
torre_de_hanoi(3, 'A', 'C', 'B')
