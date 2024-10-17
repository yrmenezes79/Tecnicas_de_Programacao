import json

# Dicionário Python
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Converter para JSON
json_string = json.dumps(dados)
print(f"JSON: {json_string}")

# Converter de JSON para dicionário Python
dados_convertidos = json.loads(json_string)
print(f"Dicionário: {dados_convertidos}")