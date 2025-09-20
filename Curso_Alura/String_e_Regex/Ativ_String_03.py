import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. 
    Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.

    Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

    Exemplo de Entrada:
    Digite a palavra-chave: Misterioso

    Saída esperada:
    Primeiras: Mis
    Últimas: oso

    """
    )
    
    palavra = input("Digite uma palavra-chave: ").strip()
    quant_palavras = int(input("Quantas letras você quer da palavra-chave? "))
    primeira_palavra = palavra[:quant_palavras]
    ultima_palavra = palavra[-quant_palavras:]
    print(f"\nOlá {palavra}! as 3 primeiras letras são {primeira_palavra} e as 3 últimas são {ultima_palavra}")
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
