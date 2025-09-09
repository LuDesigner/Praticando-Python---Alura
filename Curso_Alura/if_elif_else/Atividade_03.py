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

    temperatura = int(input("Digite qual a temperatura atual: "))
    calculo_de_temperatura = temperatura - 25

    if temperatura > 25:
        print(
            f"\nAlerta! Temperatura esta acima do limite, ultrapassou {calculo_de_temperatura}°C."
        )
        recursos.reinicializar()
    elif temperatura < 25:
        print(
            f"\nAlerta! Temperatura esta abaixo do limite, falta {calculo_de_temperatura}°C."
        )
        recursos.reinicializar()
    else:
        print(f"\nTemperatura dos servidores esta ideal em {temperatura}°C.")
        recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
