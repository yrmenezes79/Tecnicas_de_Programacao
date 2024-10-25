import fitz  # PyMuPDF

# Função para ler um arquivo PDF
def ler_pdf(caminho_arquivo):
    # Abre o PDF
    with fitz.open(caminho_arquivo) as pdf:
        # Itera sobre cada página do PDF
        for pagina_num in range(pdf.page_count):
            pagina = pdf[pagina_num]
            conteudo = pagina.get_text()
            print(f"Conteúdo da página {pagina_num + 1}:\n{conteudo}\n")

# Chame a função
ler_pdf("exemplo-de-pdf.pdf")



