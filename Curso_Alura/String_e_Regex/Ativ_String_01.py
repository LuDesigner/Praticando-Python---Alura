import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Victor trabalha em um sistema de e-commerce e precisa organizar os nomes dos produtos que estão sendo cadastrados pelos lojistas. 
    Esses nomes geralmente vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços desnecessários no início e no final.

    Ajude Victor a criar um programa que receba um nome de produto e o padronize, deixando todas as letras minúsculas e removendo os espaços extras.

    Exemplo de Entrada:

    Digite o nome do produto: ChocoLAte Branco

    Saída esperada: chocolate branco

    """
    )
    
    nome_produto = input("Digite o nome do produto: ").strip().lower()
    print(f"\nNome do produto formatado: {nome_produto}")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
