def main():
    print("Olá bem vindo ao programa Palindromo, entre com uma palavra e direi se é um Palindromo: ")
    palavra = input()
    palavraLower = palavra.lower()
    if palavraLower == palavraLower[::-1]:
        print(f"A Palavra {palavra} é um Palindromo!")
    else:
        print(f"A Palavra {palavra} não é um Palindromo!")

if __name__ == "__main__":
    main()