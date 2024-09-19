# arquivo: main.py
from biblioteca import Biblioteca
from livro import Livro

def main():
    biblioteca = Biblioteca()

    # Adicionando livros
    biblioteca.adicionar_livro(Livro("Dom Quixote", "Miguel de Cervantes", "1234567890"))
    biblioteca.adicionar_livro(Livro("1984", "George Orwell", "0987654321"))
    biblioteca.adicionar_livro(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1122334455"))

    print("\nListando todos os livros:")
    biblioteca.listar_livros()

    print("\nEmprestando um livro:")
    biblioteca.emprestar_livro("1234567890")

    print("\nTentando emprestar o mesmo livro novamente:")
    biblioteca.emprestar_livro("1234567890")

    print("\nDevolvendo o livro:")
    biblioteca.devolver_livro("1234567890")

    print("\nListando todos os livros novamente:")
    biblioteca.listar_livros()

if __name__ == "__main__":
    main()