def main():
    print("Olá bem vindo ao programa de calcular área de uma circunferência "
          " ,entre com o valor do raio:")
    raio = float(input())
    pi = 3.14159265

    area = pi * (raio * raio)
    print(f"A Área de circunferência  é de : {area}")

if __name__ == "__main__":
    main()