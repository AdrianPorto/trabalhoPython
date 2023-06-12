def main():
    print("Olá bem vindo ao programa Troca , entre com dois valores:")
    print("A:")
    A = input()
    print("B:")
    B = input()

    copyA = A
    A = B
    B = copyA

    print("Os valores ficaram:")
    print(f"A: {A}")
    print(f"B: {B}")

if __name__ == "__main__":
    main()