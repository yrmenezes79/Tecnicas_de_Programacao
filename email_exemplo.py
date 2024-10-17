from email.message import EmailMessage

# Criar uma mensagem de email
mensagem = EmailMessage()
mensagem['Subject'] = 'Olá!'
mensagem['From'] = 'meuemail@example.com'
mensagem['To'] = 'destinatario@example.com'
mensagem.set_content('Este é o corpo da mensagem.')

print(f"Mensagem de email:\n{mensagem}")
