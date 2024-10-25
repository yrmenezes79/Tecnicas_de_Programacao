import json

# Dados que você quer salvar no arquivo JSON
dados = {
    "nome": "Yuri",
    "idade": 45,
    "cidade": "Santana de Parnaiba",
    "habilidades": ["Python", "SQL", "Elasticsearch"]
}

# Cria o arquivo JSON
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)  # 'indent' adiciona formatação ao arquivo JSON
