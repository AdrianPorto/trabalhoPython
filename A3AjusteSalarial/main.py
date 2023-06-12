def main():
    print("Olá bem vindo ao programa AjusteSalarial , entre com o seu salario:")
    salario = float(input())
    print("Agora entre com o seu porcentual para fazer um reajuste:")
    percentual = float(input())

    salarioNovo = salario + (salario * percentual / 100)

    print(f"O seu salário de {salario} vai para {salarioNovo}")

if __name__ == "__main__":
    main()