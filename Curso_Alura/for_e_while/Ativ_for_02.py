import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    André está testando um novo recurso no backend do Buscante que processa dados em um loop. 
    
    Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
    
    contador = 0
    while contador < 10:
    print("Processando dados...")

    """
    )

    while True:
        try:
            numero = int(input("Digite um número até 10: "))
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
        print("Processando dados...")
        contador += 1

    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
