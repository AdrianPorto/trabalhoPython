# Código para Quebra de Linha - divisão de palavras em lista e delimitar limite de linhas

def quebrar_linhas(frase, colunas):
    palavras = frase.split()  # Dividir a frase em uma lista de palavras
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= colunas:
            # Se a palavra cabe na linha atual, adicionar à linha
            linha_atual += palavra + " "
        else:
            # Se a palavra não cabe na linha atual, adicionar a linha atual à lista de linhas e começar uma nova linha
            linhas.append(linha_atual.strip())
            linha_atual = palavra + " "

    # Adicionar a última linha à lista de linhas
    linhas.append(linha_atual.strip())

    return linhas

frase = input("Informe a frase: ")
colunas = int(input("Informe a quantidade de colunas: "))

# Quebrar linhas da frase e exibição
linhas_quebradas = quebrar_linhas(frase, colunas)


for linha in linhas_quebradas:
    print(linha)
