import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    João está desenvolvendo um sistema de cadastro para um site de leitura. 
    Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. 
    As regras são as seguintes:

    - O nome de usuário deve ter pelo menos 5 caracteres.
    - A senha deve ter pelo menos 8 caracteres.
    - João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. 
    Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

    """
    )

    while True:
        usuario = input("Digite o nome de usuário (mínimo 5 caracteres): ")
        senha = input("Digite a senha (mínimo 8 caracteres): ")

        if len(usuario) < 5:
            print("O nome de usuário deve ter pelo menos 5 caracteres.\n")
            continue

        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.\n")
            continue
        
        print("\n✅ Cadastro realizado com sucesso!")

        input("\nPressione Enter para continuar...")
        recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()