import os
import sys

def atividade(): 
    print("""
    Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
    Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
    Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

    Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
    Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

    """)

def reinicializar():
    print("""
          \n
-----------------------------------------------------------
    Vamos reiniciar o programa para uma nova análise?
-----------------------------------------------------------
    """)
    reinicializar = input("Digite 's' para sim ou 'n' para não: ").lower()
    if reinicializar == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

    else:
        print("Programa encerrado. Até a próxima!")
        sys.exit()

def main():
    macas = int(input("Digite a quantidade de maças vendidas: "))
    bananas = int(input("Digite a quantidade de bananas vendidas: "))

    if macas > bananas:
        print(f"\nAs maças tiveram venda {macas} a mais que as bananas {bananas}.")
        reinicializar()
    elif bananas > macas:
        print(f"\nAs bananas tiveram venda {bananas} a mais que as bananas {macas}.")
        reinicializar()
    else:
        print(f"\nHouve empate nas vendas de bananas ({bananas}) e maças ({macas}) .")
        reinicializar()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    atividade()
    main()
