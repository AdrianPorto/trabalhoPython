def main():
    print("Olá! Bem-vindo ao programa de verificação de Número Primo. Entre com um número e irei dizer se"
          " ele é ou não é primo: ")

    numero = int(input())

    if numero < 2:
        print("Não é um número primo.")
        return

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print("Não é um número primo.")
            return

    print("É um número primo.")


if __name__ == "__main__":
    main()
