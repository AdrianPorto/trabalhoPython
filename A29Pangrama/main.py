def ehPangrama(frase):
    frase = frase.lower()

    letras = set()

    for char in frase:
        if char.isalpha():
            letras.add(char)

    return len(letras) == 26

print("------------------------------")
frase = input("  Digite uma frase:           ")
print("------------------------------")

if ehPangrama(frase):
    print("------------------------------")
    print("| A frase é um pangrama!     |")
    print("------------------------------")
else:
    print("------------------------------")
    print("| A frase não é um pangrama. |")
    print("------------------------------")
