import random

opcoes = ["pedra", "papel", "tesoura"]

pontos_jogador = 0
pontos_computador = 0
empates = 0

print("=== JOKENPÔ ===")

while True:
    print("\nEscolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Encerrar")

    escolha = input("Digite sua escolha: ").strip()

    if escolha == "0":
        break

    if escolha not in ["1", "2", "3"]:
        print("Opção inválida! Escolha 1, 2, 3 ou 0.")
        continue

    jogador = opcoes[int(escolha) - 1]
    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
        empates += 1

    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu!")
        pontos_jogador += 1

    else:
        print("Computador venceu!")
        pontos_computador += 1

    print("\n--- Placar ---")
    print(f"Você: {pontos_jogador}")
    print(f"Computador: {pontos_computador}")
    print(f"Empates: {empates}")

print("\n=== JOGO ENCERRADO ===")
print(f"Pontuação final - Você: {pontos_jogador}")
print(f"Pontuação final - Computador: {pontos_computador}")
print(f"Empates: {empates}")