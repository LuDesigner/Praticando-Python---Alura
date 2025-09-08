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

    nota_1_str = input("Digite qual a nota da primeira prova: ")
    nota_1_str = nota_1_str.replace(",", ".")
    nota_1 = float(nota_1_str)

    nota_2_str = input("Digite qual a nota da segunda prova:")
    nota_2_str = nota_2_str.replace(",", ".")
    nota_2 = float(nota_2_str)

    nota_3_str = input("Digite qual a nota da terceira prova: ")
    nota_3_str = nota_3_str.replace(",", ".")
    nota_3 = float(nota_3_str)

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

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
