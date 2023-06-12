def main():
    print("Olá bem vindo ao programa FizzBuzz ,entre com um intervalo inicial:")
    intervaloInicial = int(input())
    print("Agora entre com um intervalo final:")
    intervaloFinal = int(input())

    if intervaloFinal <= intervaloInicial:
        print("O intervalo final deve ser maior que o intervalo inicial.")

    for numero in range(intervaloInicial, intervaloFinal + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)

if __name__ == "__main__":
    main()