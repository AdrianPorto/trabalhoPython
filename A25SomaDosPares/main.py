def calcularMedia(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media


numeros = []

continuar = True

while continuar:
    print("---------------------------------------")
    numero = float(input("| Digite um número:                   "))
    print("---------------------------------------")

    numeros.append(numero)

    print("---------------------------------------")
    opcao = input("  Deseja inserir mais números? (S/N): ")
    print("---------------------------------------")

    if opcao.lower() != "s":
        continuar = False

if len(numeros) > 0:
    media = calcularMedia(numeros)
    print("---------------------------------------")
    print(f"A média dos números informados é: {media:.2f}")
    print("---------------------------------------")
else:
    print("---------------------------------------")
    print("| Nenhum número foi informado.        |")
    print("---------------------------------------")
