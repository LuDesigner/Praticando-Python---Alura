import if_elif_else.Atividade_01 as Atividade_01
import if_elif_else.Atividade_02 as Atividade_02
import if_elif_else.Atividade_03 as Atividade_03
import if_elif_else.Atividade_04 as Atividade_04
import if_elif_else.Atividade_05 as Atividade_05
import if_elif_else.Atividade_06 as Atividade_06
import if_elif_else.Atividade_07 as Atividade_07
import if_elif_else.Atividade_08 as Atividade_08
import if_elif_else.Atividade_09 as Atividade_09
import if_elif_else.Atividade_10 as Atividade_10

import for_e_while.Ativ_for_01 as Ativ_for_01
import for_e_while.Ativ_for_02 as Ativ_for_02

import os
import sys


def menu_inicial():
    print(
        """
------------------------------------------------------
        Bem-vindo ao menu das atividades Alura!
-----------------------------------------------------
          1 - Atividade - If, Elif e Else
          2 - Atividade - For e While

          0 - Sair
    """
    )

    resposta_usuario = int(input("Digite a atividade que deseja: "))

    if resposta_usuario == 1:
        texto()
        menu_if_elif_else()
    elif resposta_usuario == 2:
        texto()
        menu_for()
    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()


def texto():
    os.system("cls" if os.name == "nt" else "clear")
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


# Menu If, Elif e Else
def menu_if_elif_else():
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
    elif resposta_usuario == 8:
        Atividade_08.main()
    elif resposta_usuario == 9:
        Atividade_09.main()
    elif resposta_usuario == 10:
        Atividade_10.main()
    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()


# Menu For e While
def menu_for():
    texto()
    resposta_usuario = int(input("Digite a atividade que deseja: "))

    if resposta_usuario == 1:
        Ativ_for_01.main()
    elif resposta_usuario == 2:
        Ativ_for_02.main()
    elif resposta_usuario == 3:
        pass
    elif resposta_usuario == 4:
        pass
    elif resposta_usuario == 5:
        pass
    elif resposta_usuario == 6:
        pass
    elif resposta_usuario == 7:
        pass
    elif resposta_usuario == 8:
        pass
    elif resposta_usuario == 9:
        pass
    elif resposta_usuario == 10:
        pass
    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    menu_inicial()
