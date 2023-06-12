def main():
    print("Olá bem vindo ao programa Fatorial, entre com um número: ")
    numero = int(input())
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"Esse é o fatorial do número {numero} : {fatorial}")

if __name__ == "__main__":
    main()