import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print(
        """
    Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
    Essa verificação será usada para definir ações diferentes dentro do jogo. 

    Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

    """
    )

    try:
        numero = int(input("Digite um número para Lucas: "))

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            recursos.reinicializar()
        else:
            print(f"O número {numero} é ÍMPAR.")
            recursos.reinicializar()
        
    except ValueError:
        print("\nValor inválido! Por favor, digite um número inteiro.")
        input("Pressione Enter para continuar...")
        main()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
