<<<<<<< HEAD
import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """
    Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. 
    Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas. 
    Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.

    Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

    Exemplo de Entrada:

    Digite o título dos livro: As Aventuras de Alice no País das Maravilhas 
    
    Digite a letra inicial para pesquisa: A

    Saída esperada: ["As", "Aventuras", "Alice"]

    """
    )

    
    titulo = input("Digite o título dos livros:  ").split()
    letra_inicial = input("Digite a letra inicial para pesquisa: ")

    resultado = [palavra for palavra in titulo if palavra.lower().startswith(letra_inicial.lower())]
    print(resultado)
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
    Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. 
    Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas. 
    Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.

    Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

    Exemplo de Entrada:

    Digite o título dos livro: As Aventuras de Alice no País das Maravilhas 
    
    Digite a letra inicial para pesquisa: A

    Saída esperada: ["As", "Aventuras", "Alice"]

    """
    )

    
    titulo = input("Digite o título dos livros:  ").split()
    letra_inicial = input("Digite a letra inicial para pesquisa: ")

    resultado = [palavra for palavra in titulo if palavra.lower().startswith(letra_inicial.lower())]
    print(resultado)
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
>>>>>>> f25ae57e82f1c2746ed65adf1c7d3f7d140eaa72
