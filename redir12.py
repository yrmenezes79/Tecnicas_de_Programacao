import json

# Função para ler um arquivo JSON
def ler_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados

# Chame a função
caminho_arquivo = 'dados.json'
dados_json = ler_json(caminho_arquivo)

# Exiba os dados
print(dados_json)
