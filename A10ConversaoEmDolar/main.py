print("---------------------------------------------------------------")
print("| Informe a cotação do DÓLAR para real:                       |")
print("---------------------------------------------------------------")
cotacaoDolar = float(input())

print("---------------------------------------------------------------")
print("| Informe a quantia em reais que deseja transformar em dólar: |")
print("---------------------------------------------------------------")
quantidadeReais = float(input())

valorCotado = quantidadeReais / cotacaoDolar

print("-----------------------------------------")
print(f"Valor cotado em dólar: US$ {valorCotado:.2f}")
print("-----------------------------------------")
