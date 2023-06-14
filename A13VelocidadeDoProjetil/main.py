# Código para calcular a velocidade de um projétil

def calcular_velocidade(distancia, tempo):
    velocidade = (distancia * 1000) / (tempo * 60)
    return velocidade


# Armazenamento da informação de distancia e tempo para a função calcular_velocdade
# A utilização de float(input()) é para receber o valor e já converter para float
distancia = float(input("Digite a distância percorrida em quilômetros: "))
tempo = float(input("Digite o tempo decorrido em minutos: "))

resultado = calcular_velocidade(distancia, tempo)

# Arredondar o resultado e formatar com duas casas decimais
resultado_formatado = format(round(resultado, 2), ".2f")

print("A velocidade do projétil é de", resultado_formatado, "metros por segundo.")
