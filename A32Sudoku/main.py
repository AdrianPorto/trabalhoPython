def validar_sudoku(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if len(set(linha)) != 9:
            return False

    # Verificar colunas
    for coluna in zip(*tabuleiro):
        if len(set(coluna)) != 9:
            return False

    # Verificar regiões
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            regiao = []
            for k in range(3):
                for l in range(3):
                    regiao.append(tabuleiro[i + k][j + l])
            if len(set(regiao)) != 9:
                return False

    return True

def encontrar_campos_incorretos(tabuleiro):
    campos_incorretos = []
    # Verificar linhas
    for i, linha in enumerate(tabuleiro):
        if len(set(linha)) != 9:
            campos_incorretos.extend((i, j) for j, valor in enumerate(linha) if valor != 0 and linha.count(valor) > 1)

    # Verificar colunas
    for j, coluna in enumerate(zip(*tabuleiro)):
        if len(set(coluna)) != 9:
            campos_incorretos.extend((i, j) for i, valor in enumerate(coluna) if valor != 0 and coluna.count(valor) > 1)

    # Verificar regiões
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            regiao = []
            for k in range(3):
                for l in range(3):
                    regiao.append(tabuleiro[i + k][j + l])
            if len(set(regiao)) != 9:
                for k in range(3):
                    for l in range(3):
                        if tabuleiro[i + k][j + l] != 0 and regiao.count(tabuleiro[i + k][j + l]) > 1:
                            campos_incorretos.append((i + k, j + l))

    return campos_incorretos

# Solicitar entrada do tabuleiro de Sudoku
tabuleiro = []
for i in range(9):
    linha = input(f"Informe os valores da linha {i + 1} separados por espaço (0 para células vazias): ")
    numeros = linha.split()
    numeros = [int(num) for num in numeros]
    tabuleiro.append(numeros)

# Validar tabuleiro
if validar_sudoku(tabuleiro):
    print("O tabuleiro é válido.")
else:
    print("O tabuleiro contém valores incorretos.")
    campos_incorretos = encontrar_campos_incorretos(tabuleiro)
    print("Campos incorretos:")
    for i, j in campos_incorretos:
        print(f"({i + 1}, {j + 1})")