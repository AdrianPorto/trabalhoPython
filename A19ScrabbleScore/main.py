def main():
    print("Olá bem vindo ao programa Scrabble Score, entre com uma palavra , e direi a pontuação dela: ")
    palavra = input()
    palavraLower = palavra.lower()
    pontuacao = 0

    for letra in palavraLower:
        if letra in ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']:
            pontuacao += 1
        elif letra in ['d', 'g']:
            pontuacao += 2
        elif letra in ['b', 'c', 'm', 'p']:
            pontuacao += 3
        elif letra in ['f', 'h', 'v', 'w', 'y']:
            pontuacao += 4
        elif letra == 'k':
            pontuacao += 5
        elif letra in ['j', 'x']:
            pontuacao += 8
        elif letra in ['q', 'z']:
            pontuacao += 10

    print(f"O score da palavra {palavra} é : {pontuacao}")


if __name__ == "__main__":
    main()