import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
    """
    Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. 
    
    As regras são:
        Média >= 7: Aprovado
        5 <= Média < 7: Recuperação
        Média < 5: Reprovado

    Escreva um programa que receba três notas como entrada e calcule a média final. 
    Com base na média, exiba a situação do aluno.

    """)


    nota_1 = ler_nota("\nDigite a nota da primeira prova: ")
    nota_2 = ler_nota("\nDigite a nota da segunda prova: ")
    nota_3 = ler_nota("\nDigite a nota da terceira prova: ")

    calculo_da_nota = (nota_1 + nota_2 + nota_3) /3

    if 5 <= calculo_da_nota < 7:
        print(f"\nO aluno esta de recuperação com {calculo_da_nota:.2f} da média.")
        recursos.reinicializar()

    elif calculo_da_nota < 5:
        print(f"\nO aluno esta reprovado com {calculo_da_nota:.2f} da média.")
        recursos.reinicializar()

    else:
        print(f"\nO aluno esta aprovado com {calculo_da_nota:.2f} da média.")
        recursos.reinicializar()

def ler_nota(mensagem):
    while True:
        nota_str = input(mensagem)
        nota_str = nota_str.replace(",", ".")  # permite vírgula como separador decimal
        try:
            nota = float(nota_str)
            if nota < 0 or nota > 10:
                print("\nErro: a nota deve estar entre 0 e 10.")
            else:
                return nota
        except ValueError:
            print("\nErro: digite apenas números válidos (exemplo: 7,5 ou 8.0).")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
