print("---------------------------------------------------------------")
print("| Informe a cotação do REAL para dólar:                       |")
print("---------------------------------------------------------------")
cotacaoReal = float(input())

print("---------------------------------------------------------------")
print("| Informe a quantia em dólar que deseja transformar em reais: |")
print("---------------------------------------------------------------")
quantidadeDolar = float(input())

valorCotado = quantidadeDolar * cotacaoReal

print("-----------------------------------------")
print(f"Valor cotado em reais: R$ {valorCotado:.2f}")
print("-----------------------------------------")
