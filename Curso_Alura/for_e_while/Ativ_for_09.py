import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Ana está implementando um sistema de filtragem de livros no Buscante. 
    A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. 
    No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.

    livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
    ]

    Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".

    """
    )

    livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
    ]

    exibir_livros(livros)

def exibir_livros(livros):

    buscar_livros = input("Deseja buscar os livros em estoque? (s/n): ")
    if buscar_livros.lower() != 's':
        print("Busca cancelada.")
        return
    else:
        print("Livros disponíveis em estoque:")
        for livro in livros:
            if livro["estoque"] > 0:  # só exibe se tiver estoque
                print(f"Livro disponível: {livro['nome']}")

    buscar_livros_02 = input("\nDeseja buscar os livros em estão faltnado em estoque? (s/n): ")
    if buscar_livros_02.lower() != 's':
        print("Busca cancelada.")
        return
    else:
        print("Livros e, falta no estoque:")
        for livro in livros:
            if livro["estoque"] == 0:  # só exibe se tiver estoque
                print(f"Livro disponível: {livro['nome']}")

    input("\nPressione Enter para continuar...")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()