import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
    """
    Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. 

    O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
    
    Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) 

    Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

    """)

    peso_str = input("Digite qual o peso em kg: ")
    peso_str = peso_str.replace(",", ".")
    peso = float(peso_str)

    altura_str = input("Digite qual a altura atual do paciente: ")
    altura_str = altura_str.replace(",", ".")
    altura = float(altura_str)

    calculo_de_IMC = peso / (altura ** 2)

    if peso <= 0 or altura <= 0:
        print("\nErro: peso e altura devem ser maiores que zero.")
        recursos.reinicializar()

    else:   
        if calculo_de_IMC <= 18.5:
            print(f"\nO paciente está abaixo do peso - {calculo_de_IMC:.2f}kg/m².")
            recursos.reinicializar()

        elif 18.5 <= calculo_de_IMC < 25:
            print(f"\nO paciente está com o peso normal - {calculo_de_IMC:.2f}kg/m².")
            recursos.reinicializar()

        elif calculo_de_IMC >= 25:
            print(f"\nO paciente está acima do peso - {calculo_de_IMC:.2f}kg/m².")
            recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
