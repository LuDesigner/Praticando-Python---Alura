import recursos.reinicializar as recursos
import os
import re

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando seus números de CPF no formato correto antes de registrar os dados no sistema.

    O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

    Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.

    Exemplo de Entrada:

    Digite o CPF no formato XXX.XXX.XXX-XX: 123.456.789-00

    Saída esperada: O CPF está no formato correto.

    """
    )
    
    cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX:  ")
    padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

    if re.match(padrao_cpf, cpf):
        print("O CPF está no formato correto.")
    else:
        print("O CPF está no formato incorreto.")

    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
