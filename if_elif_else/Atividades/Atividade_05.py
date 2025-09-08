import recursos.reinicializar as recursos
import os


def texto_inicial():
    print(
        """
    Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
    Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
    
    O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

    """
    )

def main():
    os.system("cls" if os.name == "nt" else "clear")
    texto_inicial()

    orcamento_str = input("Digite quanto que Carlos gastou no mês atual: ")
    orcamento_str = orcamento_str.replace(",", ".")
    orcamento = float(orcamento_str)

    if orcamento < 0:
        print(f"\nO orçamento de carlos esse mês foi negativo: R$ {orcamento:.2f}.")
        recursos.reinicializar()
    elif 0 <= orcamento <= 2999.99:
        print(f"\nO orçamento de carlos esse mês foi abaixo do esperado: R$ {orcamento:.2f}.")
        recursos.reinicializar()
    else:
        print(f"\nO orçamento de carlos esse mês foi acima do esperado: R$ {orcamento:.2f}.")
        recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
