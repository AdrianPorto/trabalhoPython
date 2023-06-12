print("----------------------------------")
print("| Informe o início do intervalo: |")
print("----------------------------------")
inicioIntervalo = int(input())

print("----------------------------------")
print("| Informe o fim do intervalo:    |")
print("----------------------------------")
fimIntervalo = int(input())

somaPares = 0

for i in range(inicioIntervalo, fimIntervalo+1):
    if i % 2 == 0:
        somaPares += i

print("------------------------------------------------------------------")
print(f" A soma dos números pares no intervalo [{inicioIntervalo} a {fimIntervalo}] é: {somaPares}")
print("------------------------------------------------------------------")
