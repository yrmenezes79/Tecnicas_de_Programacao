def calculadora(a, b, operacao):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
