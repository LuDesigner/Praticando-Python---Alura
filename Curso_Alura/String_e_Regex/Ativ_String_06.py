import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Nathalia é uma escritora que está revisando um texto para publicação. 
    Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". 
    Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.

    Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. 
    O programa deve exibir o texto com as alterações aplicadas.

    Exemplo de Entrada:

    Digite o texto a ser revisado: O dia está bom, tudo está bom.`
    Qual palavra deseja substituir? bom
    Qual a nova palavra? ótimo

    Saída esperada: O dia está ótimo, tudo está ótimo.

    """
    )
    
    texto = input("Digite o texto a ser revisado: ").strip().lower()
    palavra_antiga = input("Qual palavra deseja substituir? ").strip().lower()
    palavra_nova = input("Qual a nova palavra? ").strip().lower()

    texto_revisado = texto.replace(palavra_antiga, palavra_nova)

    print("\nTexto Revisado.")
    print(texto_revisado)

    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
