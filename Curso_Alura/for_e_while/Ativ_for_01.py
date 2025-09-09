import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
    Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

    clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

    Ajude Ana a decidir entre usar um laço for ou while. 
    Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.

    """
    )

    cliente = []

    nome = input("Digite o nome do cliente: ")
    cliente.append(nome)
    continuar_cadastro(cliente)


def continuar_cadastro(cliente):
    if len(cliente) < 5:
        resposta = input("Deseja cadastrar outro cliente? (s/n): ").lower()
        if resposta == "s":
            nome = input("Digite o nome do cliente: ")
            cliente.append(nome)
            continuar_cadastro(cliente)
        elif resposta == "n":
            print("Cadastro finalizado.")
            exibir_clientes(cliente)
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            continuar_cadastro(cliente)
    else:
        print("Número máximo de clientes cadastrados.")
        exibir_clientes(cliente)


def exibir_clientes(cliente):
    print("\nClientes cadastrados: ")
    print(cliente)

    input("\nPressione Enter para continuar...")
    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
