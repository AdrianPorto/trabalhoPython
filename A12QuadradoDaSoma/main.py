# Código para calcular o Quadrado da Soma de três valores:

def calcular_quadrado_soma(val1, val2, val3):
    soma = val1 + val2 + val3
    quadrado_soma = soma ** 2
    return quadrado_soma


# Entrada de valores para realizar o cálculo
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# Chamada de função com parâmetros, sendo eles os valores que definimos acima
resultado = calcular_quadrado_soma(valor1, valor2, valor3)

# Resultado do quadrado da soma
print("O quadrado da soma dos três valores é:", resultado)
