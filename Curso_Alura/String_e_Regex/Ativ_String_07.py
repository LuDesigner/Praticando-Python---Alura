<<<<<<< HEAD
import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. 
    O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). 
    Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.

    Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

    Exemplo de Entrada:

    Digite o nome do cliente para validação: maria123

    Saída esperada: Nome inválido!

    """
    )
    
    nome_cliente = input("Digite o nome do cliente para validação: ").strip()

    if nome_cliente == nome_cliente.capitalize() and nome_cliente.isalpha():
        print("Nome válido!")
    else:
        print("Nome inválido!")

    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
=======
import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. 
    O padrão esperado é que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). 
    Para facilitar o trabalho, ela quer um programa que valide automaticamente os nomes fornecidos.

    Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.

    Exemplo de Entrada:

    Digite o nome do cliente para validação: maria123

    Saída esperada: Nome inválido!

    """
    )
    
    nome_cliente = input("Digite o nome do cliente para validação: ").strip()

    if nome_cliente == nome_cliente.capitalize() and nome_cliente.isalpha():
        print("Nome válido!")
    else:
        print("Nome inválido!")

    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
>>>>>>> f25ae57e82f1c2746ed65adf1c7d3f7d140eaa72
