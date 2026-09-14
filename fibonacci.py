print("=== SEQUÊNCIA DE FIBONACCI ===")

while True:
    entrada = input("Quantos termos você deseja ver? ").strip()

    try:
        quantidade = int(entrada)

        if quantidade <= 0:
            print("Digite um número maior que zero.")
            continue

        break

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

fibonacci = []

a = 0
b = 1

for i in range(quantidade):
    fibonacci.append(a)

    proximo = a + b
    a = b
    b = proximo

print("\n=== RESULTADO ===")
print(fibonacci)