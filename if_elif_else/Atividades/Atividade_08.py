import recursos.reinicializar as recursos
import os

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print(
        """
    Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
    O valor do pedágio depende da distância percorrida:

        - Até 100 km: R$ 10,00
        - Entre 100 km e 200 km: R$ 20,00
        - Acima de 200 km: R$ 30,00

    Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

    """
    )

    km_str = input("Digite quantos kms foram percorridos por Fernanda: ")
    km_str = km_str.replace(",", ".")
    km = float(km_str)

    if km < 0:
        print(f"\nOs kms percorridos não podem ser negativos!")
        recursos.reinicializar()
    elif 0 <= km <= 100:
        print(f"\nOs kms percorridos estão em {km:.2f} - Preço do pedágio = R$ 10,00.")
        recursos.reinicializar()
    elif 100.99 <= km <= 200:
        print(f"\nOs kms percorridos estão em {km:.2f} - Preço do pedágio = R$ 20,00.")
        recursos.reinicializar()
    else:
        print(f"\nOs kms percorridos estão em {km:.2f} - Preço do pedágio = R$ 30,00.")
        recursos.reinicializar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
