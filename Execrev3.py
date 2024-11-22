def categoria_por_idade(idade: int) -> str:
    """Determina a categoria de uma pessoa com base na idade."""
    if idade <= 12:
        return "Infantil"
    elif 13 <= idade <= 17:
        return "Juvenil"
    elif 18 <= idade <= 59:
        return "Adulto"
    else:
        return "Sênior"

# Entrada do usuário
try:
    idade = int(input("Digite a idade: "))
    categoria = categoria_por_idade(idade)
    print(f"A categoria é: {categoria}")
except ValueError:
    print("Por favor, insira um número válido.")
