import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes durante uma promoção especial da sua nova loja de livros. 
    O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".

    Crie um programa que utilize um laço for para exibir as seguintes mensagens:

    - Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
    - Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
    - Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

    """
    )

    while True:
        try:
            numero = int(input("Digite o número de livros: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Digite um número entre 1 e 10.")
        except ValueError:
            print("Digite apenas números inteiros.")

    for n in range(numero, 0, -1):
        if n % 2 == 0:
            print(f"\nFaltam apenas {n} segundos - Não perca essa oportunidade!")
        else:
            print(f"A contagem continua: {n} segundos restantes.")

    print("\nAproveite a promoção agora!")

    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
