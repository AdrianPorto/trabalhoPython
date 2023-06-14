# Código para cálculos de percentuais de votos válidos - Eleição Sindical

# Para a realização dos percentuais, precisamos primeiro inputar as quantidades de votos por candidato.
# Leitura dos votos válidos, nulos e em branco, convertidos para inteiros:
votos_validos_A = int(input("Informe a quantidade de votos válidos do candidato A: "))
votos_validos_B = int(input("Informe a quantidade de votos válidos do candidato B: "))
votos_validos_C = int(input("Informe a quantidade de votos válidos do candidato C: "))
votos_nulos = int(input("Informe a quantidade de votos nulos: "))
votos_em_branco = int(input("Informe a quantidade de votos em branco: "))

# Cálculo do total de eleitores
total_eleitores = votos_validos_A + votos_validos_B + votos_validos_C + votos_nulos + votos_em_branco

# Cálculo dos percentuais para cada situação com round() para arredondar em 2 casas decimais:
percentual_validos_total = round((votos_validos_A + votos_validos_B + votos_validos_C) / total_eleitores * 100, 2)
percentual_validos_A = round(votos_validos_A / total_eleitores * 100, 2)
percentual_validos_B = round(votos_validos_B / total_eleitores * 100, 2)
percentual_validos_C = round(votos_validos_C / total_eleitores * 100, 2)
percentual_nulos = round(votos_nulos / total_eleitores * 100, 2)
percentual_em_branco = round(votos_em_branco / total_eleitores * 100, 2)

# Resultados:
print("Número total de eleitores:", total_eleitores)
print("Percentual de votos válidos em relação aos eleitores:", percentual_validos_total, "%")
print("Percentual de votos válidos do candidato A em relação aos eleitores:", percentual_validos_A, "%")
print("Percentual de votos válidos do candidato B em relação aos eleitores:", percentual_validos_B, "%")
print("Percentual de votos válidos do candidato C em relação aos eleitores:", percentual_validos_C, "%")
print("Percentual de votos nulos em relação aos eleitores:", percentual_nulos, "%")
print("Percentual de votos em branco em relação aos eleitores:", percentual_em_branco, "%")