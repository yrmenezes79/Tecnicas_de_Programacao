import csv
nome_arquivo = 'exemplo.csv'

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 30, 'Nova York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escrever os dados
    writer.writerows(dados)

print(f'Arquivo {nome_arquivo} criado com sucesso!')



