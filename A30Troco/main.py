# Código de Troco - é necessário identificar cédulas e moedas disponíveis

def calcular_troco(valor_total, valor_pago):
    troco = valor_pago - valor_total
    print("valor nominal do troco: ", round(troco, 2))

    # Lista das cédulas e moedas disponíveis, segundo o enunciado do exercício
    cedulas_moedas = [100, 50, 10, 5, 1, 0.5, 0.10, 0.05, 0.01]

    # Dicionário para armazenar o número de cédulas e moedas a serem fornecidas
    troco_em_cedulas_moedas = {}

    # Iterar sobre as cédulas e moedas disponíveis
    for cedula_moeda in cedulas_moedas:
        # Verificar se a cédula/moeda é menor ou igual ao troco
        if cedula_moeda <= troco:
            # Calcular o número de cédulas/moedas a serem fornecidas
            quantidade = int(troco // cedula_moeda) # operador '//' faz divisão e ignora o resto da divisão
            # Atualizar o troco restante
            troco -= quantidade * cedula_moeda
            # Armazenar a quantidade de cédulas/moedas no dicionário
            troco_em_cedulas_moedas[cedula_moeda] = quantidade

    return troco_em_cedulas_moedas


# Leitura do valor total a ser pago, valor efetivamente pago e calcular troco
valor_total = float(input("Digite o valor total a ser pago: "))
valor_pago = float(input("Digite o valor efetivamente pago: "))

troco_em_cedulas_moedas = calcular_troco(valor_total, valor_pago)

# Exibição das cédulas e moedas a serem fornecidas como troco
print("Troco em cédulas e moedas:")
for cedula_moeda, quantidade in troco_em_cedulas_moedas.items():
    print("{} - {}".format(quantidade, cedula_moeda))
