

def main():
    print("Olá bem vindo ao programa TwoFer , entre com o seu nome:")
    nome = input()
    nome = nome.replace(" ", "")
    if nome == "":
        print("Um para você, um para mim.")
    else:
        print(f"Um para {nome}, um para mim.")


if __name__ == "__main__":
    main()
