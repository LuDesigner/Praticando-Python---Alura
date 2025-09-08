import recursos.reinicializar as recursos
import os


def main():
    os.system("cls" if os.name == "nt" else "clear")
        print(
        """
    Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
    No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

    Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
    Se algum valor for negativo, mostre uma mensagem informando o erro.

    """
    )
        
        atividade_a = int(input("Digite o tempo da atividade A: "))
        atividade_b = int(input("Digite o tempo da atividade B: "))
        atividade_c = int(input("Digite o tempo da atividade C: "))

        if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
            print(f"\n Os dias não podem ser negativos.")
            recursos.reinicializar()
        else:
            total_dias = atividade_a + atividade_b + atividade_c
            print(f"\nO tempo total do projeto é de {total_dias} dias.")

            atividades = [
                ("Atividade A", atividade_a),
                ("Atividade B", atividade_b),
                ("Atividade C", atividade_c),
            ]

            atividades.sort(key=lambda x: x[1], reverse=True)

            print("Atividades em ordem de dias:")
            for nome, dias in atividades:
                print(f"{nome} = {dias} dias")

            recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
