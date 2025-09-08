import menu_principal
import os
import sys

def reinicializar():
    print(
        """
          \n
-----------------------------------------------------------
    Vamos reiniciar o programa para uma nova análise?
-----------------------------------------------------------
    """
    )
    reinicializar = input("Digite 's' para sim ou 'n' para não: ").lower()
    if reinicializar == "s":
        os.system("cls" if os.name == "nt" else "clear")
        menu_principal.menu()

    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()