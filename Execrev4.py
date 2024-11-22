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

try:
    # Abrindo o arquivo de entrada
    with open("idades.txt", "r") as arquivo_entrada:
        idades = arquivo_entrada.readlines()

    # Processando as idades e classificando
    with open("categorias.txt", "w") as arquivo_saida:
        for linha in idades:
            try:
                idade = int(linha.strip())  # Remove espaços extras e converte para inteiro
                categoria = categoria_por_idade(idade)
                arquivo_saida.write(f"{idade}: {categoria}\n")
            except ValueError:
                arquivo_saida.write(f"{linha.strip()}: Idade inválida\n")

    print("Classificações salvas no arquivo 'categorias.txt'.")

except FileNotFoundError:
    print("Erro: O arquivo 'idades.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
