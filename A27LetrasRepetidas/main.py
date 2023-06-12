def encontrarPrimeiraLetraNaoRepetida(texto):
    letras = {}

    texto = texto.lower()

    for letra in texto:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

    for letra in texto:
        if letras[letra] == 1:
            return letra

    return ""


print("--------------------")
texto = input("  Digite o texto:   ")
print("--------------------")

primeiraLetraNaoRepetida = encontrarPrimeiraLetraNaoRepetida(texto)

if primeiraLetraNaoRepetida != "":
    print("-------------------------------------------------------------")
    print(f"A primeira letra não repetida no texto é: {primeiraLetraNaoRepetida}")
    print("-------------------------------------------------------------")
else:
    print("-------------------------------------------------------------")
    print("| Não existem letras que não se repetem no texto informado. |")
    print("-------------------------------------------------------------")
