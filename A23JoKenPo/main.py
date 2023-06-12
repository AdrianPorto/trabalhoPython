def main():
    print("Olá bem vindo ao jogo JoKenPo, faça a sua jogada: ")
    print("Jogador 1 Escolha sua jogada:")
    print("1. Pedra")
    print("2. Papel ")
    print("3. Tesoura")
    jogadorUm = int(input())
    if(jogadorUm > 0 and jogadorUm < 4):
        pass
    else:
         print("Opção inserida inválida!")
         exit()

    print("Jogador 2 Escolha sua jogada:")
    print("1. Pedra")
    print("2. Papel ")
    print("3. Tesoura")
    jogadorDois = int(input())
    if(jogadorDois > 0 and jogadorDois < 4):
        pass
    else:
        print("Opção inserida inválida!")
        exit()
    if jogadorUm == 1:
        if jogadorDois == 3:
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
    elif jogadorUm == 3:
        if jogadorDois == 2:
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
    elif jogadorUm == 2:
        if jogadorDois == 1:
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
    else:
        print("Opção inserida inválida!")



if __name__ == "__main__":
    main()