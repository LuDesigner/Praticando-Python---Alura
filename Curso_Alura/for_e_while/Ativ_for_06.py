import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado. 
    A lista de livros já cadastrados no sistema é a seguinte:

    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

    Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. 
    Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.

    """
    )

    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

    exibir_livros(livros)


def exibir_livros(livros):
    buscar_livros = input("Digite o nome do livro que deseja buscar: ")

    for livro in livros:
        if livro == buscar_livros:
            print(f"Livro encontrado: {livro}")
            break
    else:
        print(f"Livro não encontrado: {buscar_livros}")

    input("\nPressione Enter para continuar...")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()