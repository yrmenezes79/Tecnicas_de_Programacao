# Passo 1: Criando a função soma_inteiros sem tipagem
def soma_inteiros(a, b):
    return a + b

# Passo 2: Modificando a função soma_inteiros com type hints
def soma_inteiros(a: int, b: int) -> int:
    return a + b

# Passo 3: Criando a função concatena_strings sem tipagem
def concatena_strings(s1, s2):
    return s1 + s2

# Passo 4: Modificando a função concatena_strings com type hints
def concatena_strings(s1: str, s2: str) -> str:
    return s1 + s2
