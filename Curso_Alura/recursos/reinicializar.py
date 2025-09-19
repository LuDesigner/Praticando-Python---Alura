import menu_principal
import os
import sys


def reinicializar():
    print(
        """
          \n
-----------------------------------------------------------
            Vamos retornar ao menu principal!
-----------------------------------------------------------
    """
    )

    while True:
        resposta = input("Digite 's' para sim ou 'n' para não: ").lower()
        if resposta == "s":
            os.system("cls" if os.name == "nt" else "clear")
            menu_principal.menu_inicial()
            break

        elif resposta == "n":
            print("Programa encerrado. Até a próxima!")
            sys.exit()

        else:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")
