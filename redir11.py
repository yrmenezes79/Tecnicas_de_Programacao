from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Função para criar um PDF
def criar_pdf(nome_arquivo):
    # Cria um objeto canvas
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter

    # Adiciona texto ao PDF
    c.drawString(100, altura - 100, "Olá, este é um arquivo PDF criado com Python!")
    c.drawString(100, altura - 120, "Adicionando mais texto aqui.")

    # Finaliza o PDF
    c.save()

# Chame a função
criar_pdf("meu_arquivo.pdf")




