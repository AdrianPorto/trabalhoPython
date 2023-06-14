# Código para Ordenação de Inteiros - leitura dos elementos e exibição de ordem decrescente

elementos = []
for i in range(12):
    elemento = int(input("Digite o elemento {}: ".format(i+1)))
    elementos.append(elemento)

# Ordenação em ordem decrescente
elementos_ordenados = sorted(elementos, reverse=True)


print("Elementos em ordem decrescente:")
for elemento in elementos_ordenados:
    print(elemento)
