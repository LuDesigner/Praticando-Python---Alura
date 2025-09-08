import Atividade_01
import Atividade_02

import os
import sys

def texto():
    print(
        """
------------------------------------------------------
        Bem-vindo ao menu de atividades!
------------------------------------------------------

          1 - Atividade 01
          2 - Atividade 02

    """
    )

def menu():
    texto()
    resposta_usuario = int(input("Digite a atividade que deseja: "))
    print("""
          1 - Atividade 01
          2 - Atividade 02
          """)

    if resposta_usuario == 1:
        Atividade_01.main()
    elif resposta_usuario == 2:
        Atividade_02.main()
    else:
        pass
     

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    menu()