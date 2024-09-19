# arquivo: biblioteca.py
from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro adicionado: {livro}")

    def emprestar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and livro.disponivel:
                livro.disponivel = False
                print(f"Livro emprestado: {livro}")
                return
        print("Livro não disponível ou não encontrado.")

    def devolver_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and not livro.disponivel:
                livro.disponivel = True
                print(f"Livro devolvido: {livro}")
                return
        print("Livro não encontrado ou já disponível.")

    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro} - Status: {status}")
