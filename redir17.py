from docx import Document

def ler_docx(arquivo):
    # Carregar o documento
    doc = Document(arquivo)
    
    # Ler e imprimir o conteúdo de cada parágrafo
    for parágrafo in doc.paragraphs:
        print(parágrafo.text)
        
caminho_arquivo = 'TESTE.docx'
ler_docx(caminho_arquivo)
