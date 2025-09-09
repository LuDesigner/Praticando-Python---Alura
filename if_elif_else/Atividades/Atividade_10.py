import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print(
        """
    Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

    O valor da renda mensal precisa ser maior que R$ 2.000,00.
    O valor da parcela não pode ultrapassar 30% da renda.

    Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
    O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

    """
    )

    try:
        renda = float(input("Informe o valor da renda mensal (R$): ").replace(",", "."))
        parcela = float(input("Informe o valor da parcela desejada (R$): ").replace(",", "."))
        limite_parcela = renda * 0.3


        if renda > 2000 and parcela <= limite_parcela:
            print(f"Empréstimo foi aprovado.")   
        else:
            print("\nEmpréstimo reprovado!")
            if renda <= 2000:
                print("Motivo: renda mensal abaixo de R$ 2.000,00.")
            if parcela > limite_parcela:
                print(f"Motivo: parcela acima de 30% da renda (máx: R$ {limite_parcela:.2f}).")
        
        recursos.reinicializar()
        
    except ValueError:
        print("\nValor inválido! Por favor, digite um número inteiro.")
        input("Pressione Enter para continuar...")
        main()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
