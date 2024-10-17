import datetime

# Data e hora atual
agora = datetime.datetime.now()
print("Data e hora atual:", agora)

# Extraindo partes da data e hora
print("Ano:", agora.year)
print("Mês:", agora.month)
print("Dia:", agora.day)
print("Hora:", agora.hour)
print("Minuto:", agora.minute)
print("Segundo:", agora.second)

# Criando uma data específica
data_especifica = datetime.datetime(2024, 10, 17, 15, 30)
print("\nData e hora específica:", data_especifica)

# Formatando a data para uma string
data_formatada = data_especifica.strftime("%d/%m/%Y %H:%M")
print("Data formatada:", data_formatada)

#
