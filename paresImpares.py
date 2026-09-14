print("=== PARES E ÍMPARES ===")

while True:
    entrada = input(
        "Digite os números inteiros separados por espaço: "
    ).strip()

    if entrada == "":
        print("Você precisa digitar pelo menos um número.")
        continue

    valores = entrada.split()

    try:
        numeros = [int(valor) for valor in valores]
        break

    except ValueError:
        print("Entrada inválida! Digite somente números inteiros.")

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\n=== RESULTADO ===")
print(f"Lista completa: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")