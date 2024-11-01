def buscar_aluno(lista, matricula):
    for i in range(len(lista)):
        if lista[i] == matricula:
            return i  
    return "Aluno não encontrado"  
# Lista de números de matrícula
matriculas = [123, 456, 789, 101, 112, 131]

# Testando a função
print(buscar_aluno(matriculas, 789))  

