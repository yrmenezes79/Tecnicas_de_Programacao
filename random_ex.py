from datetime import datetime, timedelta

# Data e hora atuais
data_atual = datetime.now()
print("Data e hora atuais:", data_atual)

# Data de um mês atrás (aproximadamente 30 dias)
um_mes_atras = data_atual - timedelta(days=30)
print("Data de um mês atrás:", um_mes_atras)

# Diferença entre duas datas
data_passada = datetime(2023, 1, 1)
diferenca = data_atual - data_passada
print(f"Dias entre {data_passada.date()} e {data_atual.date()}: {diferenca.days} dias")
