import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. 
    Ele quer garantir que a mensagem seja exibida 5 vezes.

    Ajude Marcos a escrever um programa que exiba a mensagem: 
    "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

    """
    )

    projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

    exibir_projetos(projetos)


def exibir_projetos(projetos):
    print("\nLista de projetos:")
    for projeto in projetos:
        if projeto is None:
            print("Projeto ausente")
        else:
            print(projeto)

    input("\nPressione Enter para continuar...")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()