def main():
    print("Bem-vindo ao programa de conversão de Algarismo Romano em número. Entre com um Algarismo Romano: ")
    algarismo = input()

    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    contador = 0

    while contador < len(algarismo):
        algarismoLetra = algarismo[contador]

        if algarismoLetra == 'I':
            if contador + 1 < len(algarismo):
                proximo_algarismo = algarismo[contador + 1]
                if proximo_algarismo == 'V':
                    total += 4
                    contador += 2
                elif proximo_algarismo == 'X':
                    total += 9
                    contador += 2
                else:
                    total += 1
                    contador += 1
            else:
                total += 1
                contador += 1

        elif algarismoLetra == 'X':
            if contador + 1 < len(algarismo):
                proximo_algarismo = algarismo[contador + 1]
                if proximo_algarismo == 'L':
                    total += 40
                    contador += 2
                elif proximo_algarismo == 'C':
                    total += 90
                    contador += 2
                else:
                    total += 10
                    contador += 1
            else:
                total += 10
                contador += 1

        elif algarismoLetra == 'C':
            if contador + 1 < len(algarismo):
                proximo_algarismo = algarismo[contador + 1]
                if proximo_algarismo == 'D':
                    total += 400
                    contador += 2
                elif proximo_algarismo == 'M':
                    total += 900
                    contador += 2
                else:
                    total += 100
                    contador += 1
            else:
                total += 100
                contador += 1

        else:
            total += valores[algarismoLetra]
            contador += 1

    print(f"O numeral romano {algarismo} corresponde ao número inteiro: {total}")

if __name__ == "__main__":
    main()
