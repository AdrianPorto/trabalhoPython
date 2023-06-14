# Código de Média do ALuno - leitura das notas e status de aprovado/reprovado

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificação e exibição do resultado
if media >= 5:
    print("Aprovado!!!!")
else:
    print("Reprovado :'(")

print("Média:", media)
