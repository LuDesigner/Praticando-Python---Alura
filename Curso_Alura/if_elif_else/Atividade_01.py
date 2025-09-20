import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
    Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
    Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

    Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
    Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

    """
    )

    macas = int(input("Digite a quantidade de maças vendidas: "))
    bananas = int(input("Digite a quantidade de bananas vendidas: "))

    if macas > bananas:
        print(f"\nAs maças tiveram venda {macas} a mais que as bananas {bananas}.")
        recursos.reinicializar()
    elif bananas > macas:
        print(f"\nAs bananas tiveram venda {bananas} a mais que as bananas {macas}.")
        recursos.reinicializar()
    else:
        print(f"\nHouve empate nas vendas de bananas ({bananas}) e maças ({macas}) .")
        recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
