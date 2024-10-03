from calculadora import calculadora

def test_soma():
    assert calculadora(2, 3, "soma") == 5

def test_subtracao():
    assert calculadora(5, 2, "subtracao") == 3

def test_multiplicacao():
    assert calculadora(3, 4, "multiplicacao") == 12

def test_divisao():
    assert calculadora(10, 2, "divisao") == 5

def test_divisao_por_zero():
    assert calculadora(10, 0, "divisao") == "Erro: Divisão por zero"

def test_operacao_invalida():
    assert calculadora(5, 3, "potencia") == "Operação inválida"
