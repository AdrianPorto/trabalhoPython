def verificarResultado(jogador1, jogador2):
    regras = {
        "tesoura-papel": "Tesoura corta papel",
        "papel-pedra": "Papel cobre pedra",
        "pedra-lagarto": "Pedra esmaga lagarto",
        "lagarto-spock": "Lagarto envenena Spock",
        "spock-tesoura": "Spock esmaga tesoura",
        "tesoura-lagarto": "Tesoura decapita lagarto",
        "lagarto-papel": "Lagarto come papel",
        "papel-spock": "Papel refuta Spock",
        "spock-pedra": "Spock vaporiza pedra",
        "pedra-tesoura": "Pedra amassa tesoura"
    }

    jogada1 = jogador1.lower()
    jogada2 = jogador2.lower()
    jogada = jogada1 + "-" + jogada2

    if jogada in regras:
        return f"Jogador 1 escolheu {jogador1}\nJogador 2 escolheu {jogador2}\n{regras[jogada]}\nJogador 1 venceu!"
    elif jogada2 + "-" + jogada1 in regras:
        return f"Jogador 1 escolheu {jogador1}\nJogador 2 escolheu {jogador2}\n{regras[jogada2 + '-' + jogada1]}\nJogador 2 venceu!"
    else:
        return f"Jogador 1 escolheu {jogador1}\nJogador 2 escolheu {jogador2}\nNenhum jogador venceu, é um empate!"


print("---------------------------------------------------------------------")
jogador1 = input("| Jogador 1, escolha entre pedra, papel, tesoura, lagarto ou Spock: ")
print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")
jogador2 = input("| Jogador 2, escolha entre pedra, papel, tesoura, lagarto ou Spock: ")
print("---------------------------------------------------------------------")

resultado = verificarResultado(jogador1, jogador2)

print("---------------------------------------------------------------------")
print(resultado)
print("---------------------------------------------------------------------")
