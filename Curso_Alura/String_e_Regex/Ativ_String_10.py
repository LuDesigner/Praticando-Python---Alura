import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. 
    Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". 
    Por exemplo, “Monalisa Silva - 1994”.

    Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.
    Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.

    Exemplo de Entrada:
    Digite o nome completo e o ano de nascimento do paciente: Ana Silva - 1990
    
    Saída esperada:
    Primeiro Nome: Ana
    Sobrenome: Silva
    Ano de Nascimento: 1990

    """
    )
    
    entrada = input("Digite o nome completo e o ano de nascimento do paciente:  ")
    nome_completo, ano_nascimento = entrada.split(" - ")
    primeiro_nome, sobrenome = nome_completo.split()

    print(f"\nPrimeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")    
    print(f"Ano de Nascimento: {ano_nascimento}")

    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
