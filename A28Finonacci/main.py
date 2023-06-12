def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("---------------------------")
numero = int(input("  Digite um número:        "))
print("---------------------------")

print("---------------------------")
print("| Sequência de Fibonacci: |")
for i in range(numero + 1):
    print(fibonacci(i), end=" ")
print()
