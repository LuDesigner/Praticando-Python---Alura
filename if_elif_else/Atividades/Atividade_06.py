import recursos.reinicializar as recursos
import os


def texto_inicial():
    print(
        """
    Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. 
    
    Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
    
    Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

    """
    )


def main():
    os.system("cls" if os.name == "nt" else "clear")
    texto_inicial()

    hora_str = input("Deja bem vindo, para acessar por favor, digite a hora atual: ")

    try:
        partes = hora_str.split(":")
        hora = int(partes[0])
        minuto = int(partes[1])

        minuto_total = hora * 60 + minuto

        if 480 <= minuto_total <= 1080:
            print("\nAcesso permitido. Bem-vindo ao escritório!")
            recursos.reinicializar()
        else:
            print("\nAcesso negado. O escritório está fechado no momento.")
            recursos.reinicializar()
    
    except (ValueError, IndexError):
        print("Erro: digite no formato correto HH:MM (ex: 09:30)." \
        "")
        input("Pressione Enter para reiniciar...")
        main()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
