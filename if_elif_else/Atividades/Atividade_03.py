import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
    Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

    """
    )

    temperatura = int(input("Digite a quantidade de maças vendidas: "))

    if macas > bananas:
        print(f"\nAs maças tiveram venda {macas} a mais que as bananas {bananas}.")
        recursos.reinicializar()
    elif bananas > macas:
        print(f"\nAs bananas tiveram venda {bananas} a mais que as bananas {macas}.")
        recursos.reinicializar()
    else:
        print(f"\nHouve empate nas vendas de bananas ({bananas}) e maças ({macas}) .")
        recursos.reinicializar()


        recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
