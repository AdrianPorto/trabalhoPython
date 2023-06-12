print("------------------------------------------------")
print("| Digite o valor da hora-aula:                 |")
print("------------------------------------------------")
valorHoraAula = float(input())

print("------------------------------------------------")
print("| Digite o número de horas trabalhadas no mês: |")
print("------------------------------------------------")
horasTrabalhadas = float(input())

print("------------------------------------------------")
print("| Digite o percentual de desconto do INSS:     |")
print("------------------------------------------------")
percentualDesconto = float(input())

salarioBruto = valorHoraAula * horasTrabalhadas
desconto = salarioBruto * (percentualDesconto / 100)
salarioLiquido = salarioBruto - desconto

print("------------------------------------------------")
print(f"Salário Bruto: R$ {salarioBruto:.2f}")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}")
print("------------------------------------------------")
