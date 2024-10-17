import os

# Mostrando o diretório de trabalho atual
diretorio_atual = os.getcwd()
print("Diretório atual:", diretorio_atual)

# Listando arquivos e diretórios
conteudo = os.listdir(diretorio_atual)
print("Conteúdo do diretório:", conteudo)

# Criando um novo diretório
novo_diretorio = 'test_dir'
os.mkdir(novo_diretorio)
print(f"Diretório '{novo_diretorio}' criado.")

# Removendo o diretório criado
os.rmdir(novo_diretorio)
print(f"Diretório '{novo_diretorio}' removido.")
