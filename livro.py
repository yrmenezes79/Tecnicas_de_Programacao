# arquivo: livro.py
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"
