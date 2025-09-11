import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Você está desenvolvendo um sistema de controle de estoque para o Buscante. 
    Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. 
    Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.

    Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. 
    
    O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".

    """
    )

    while True:
        try:
            numero = int(input("Digiteo número de vendas: "))
            if numero <= 0:
                print("Digite um número positivo.")
            elif numero >= 11:
                print("Digite um número abaixo de 10.")
            else:
                if numero > 10:
                    numero = 10
                break
        except ValueError:
            print("Digite apenas números inteiros.")

    contador = 0

    while contador < numero:
        print(f"Estoque restante: { 5 - contador}")
        contador += 1
    
    print("Estoque esgotado")

    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
