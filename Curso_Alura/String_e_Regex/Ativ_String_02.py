<<<<<<< HEAD
import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes. 
    Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.

    Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

    Exemplo de Entrada:

    Digite o nome do cliente: Laura
    Digite a cidade do cliente: Rio de Janeiro

    Saída esperada: Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro.

    """
    )
    
    nome_do_cliente = input("Digite o nome do cliente: ").strip().lower().title()
    cidade_cliente = input("Digite a cidade do cliente: ").strip().lower().title()
    print(f"\nOlá {nome_do_cliente}! Bem-vinda ao sistema da cidade de {cidade_cliente}")
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
    Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes. 
    Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.

    Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

    Exemplo de Entrada:

    Digite o nome do cliente: Laura
    Digite a cidade do cliente: Rio de Janeiro

    Saída esperada: Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro.

    """
    )
    
    nome_do_cliente = input("Digite o nome do cliente: ").strip().lower().title()
    cidade_cliente = input("Digite a cidade do cliente: ").strip().lower().title()
    print(f"\nOlá {nome_do_cliente}! Bem-vinda ao sistema da cidade de {cidade_cliente}")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
>>>>>>> f25ae57e82f1c2746ed65adf1c7d3f7d140eaa72
