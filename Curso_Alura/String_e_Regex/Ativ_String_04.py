<<<<<<< HEAD
import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. 
    Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.

    Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?
    
    Exemplo de Entrada:

    Digite a URL para validação: https://monitorrenan.com

    Saída esperada: URL válida!

    """
    )
    
    url = input("Digite a URL: ").strip()

    if url.startswith("https://") and url.endswith(".com"):
        print("URL válida!")
    else:
        print("URL inválida!")
    
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
    Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. 
    Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.

    Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?
    
    Exemplo de Entrada:

    Digite a URL para validação: https://monitorrenan.com

    Saída esperada: URL válida!

    """
    )
    
    url = input("Digite a URL: ").strip()

    if url.startswith("https://") and url.endswith(".com"):
        print("URL válida!")
    else:
        print("URL inválida!")
    
    recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
>>>>>>> f25ae57e82f1c2746ed65adf1c7d3f7d140eaa72
