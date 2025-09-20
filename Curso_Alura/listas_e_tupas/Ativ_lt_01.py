import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        """
    Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
    Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. 
    Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

    Exemplo de Entrada: Digite o item que você quer verificar: açúcar

    Saída esperada: O item açúcar precisa ser comprado.

    """
    )

    despensa = ["arroz", "feijão", "macarrão", "óleo", "sal", "açúcar", "café", "leite"]

    item = input("Digite o item que você quer verificar: ").lower()

    if item in despensa:
        print(f"O item {item} já está na despensa.")
    else:
        print(f"O item {item} precisa ser comprado.")



    recursos.reinicializar()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
