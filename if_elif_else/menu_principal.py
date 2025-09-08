import Atividades.Atividade_01 as Atividade_01
import Atividades.Atividade_02 as Atividade_02
import Atividades.Atividade_03 as Atividade_03
import Atividades.Atividade_04 as Atividade_04
import Atividades.Atividade_05 as Atividade_05
import Atividades.Atividade_06 as Atividade_06
import Atividades.Atividade_07 as Atividade_07
import Atividades.Atividade_08 as Atividade_08
import Atividades.Atividade_09 as Atividade_09
import Atividades.Atividade_10 as Atividade_10

import os
import sys


def texto():
    print(
        """
------------------------------------------------------
        Bem-vindo ao menu de atividades!
-----------------------------------------------------
          1 - Atividade 01
          2 - Atividade 02
          3 - Atividade 03
          4 - Atividade 04
          5 - Atividade 05
          6 - Atividade 06
          7 - Atividade 07
          8 - Atividade 08
          9 - Atividade 09
          10 - Atividade 10
          0 - Sair
    """
    )


def menu():
    texto()
    resposta_usuario = int(input("Digite a atividade que deseja: "))

    if resposta_usuario == 1:
        Atividade_01.main()
    elif resposta_usuario == 2:
        Atividade_02.main()
    elif resposta_usuario == 3:
        Atividade_03.main()
    elif resposta_usuario == 4:
        Atividade_04.main()
    elif resposta_usuario == 5:
        Atividade_05.main()
    elif resposta_usuario == 6:
        Atividade_06.main()
    elif resposta_usuario == 7:
        Atividade_07.main()
    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    menu()