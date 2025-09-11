import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. 
    Ele quer garantir que a mensagem seja exibida 5 vezes.

    Ajude Marcos a escrever um programa que exiba a mensagem: 
    "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

    """
    )

    while True:
        try:
            numero = int(input("Digite quantas vezes quer que seja exibida a mensagem: "))
            if numero <= 0:
                print("Digite um número positivo.")
            elif numero >= 6:
                print("Digite um número abaixo de 6.")
            else:
                if numero > 5:
                    numero = 5
                break
        except ValueError:
            print("Digite apenas números inteiros.")

    contador = 0

    while contador < numero:
        print("Bem-vindo ao Buscante!")
        contador += 1

    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
