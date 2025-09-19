import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.

    valores = [10, 20, 30, 40, 50]

    Crie um programa para implementar a soma.

    """
    )

    valores = []
    
    try:
        numero = float(input("Digite um valor: "))
        valores.append(numero)
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        main()
        return

    continuar_cadastro(valores)


def continuar_cadastro(valores):
    if len(valores) < 5:
        resposta = input("Deseja cadastrar outro número? (s/n): ")
        if resposta.lower() == "s":
            try:
                numero = float(input("Digite outro valor: "))
                valores.append(numero)
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
            continuar_cadastro(valores)
        elif resposta.lower() == "n":
            print("Cadastro finalizado.")
            exibir_clientes(valores)
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            continuar_cadastro(valores)
    else:
        print("Número máximo alcançado.")
        exibir_clientes(valores)


def exibir_clientes(valores):
    print("\nValores cadastrados: ")
    print(valores)

    soma = sum(valores)
    print(f"\nSoma total dos produtos: R$ {soma:.2f}")

    input("\nPressione Enter para continuar...")
    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
