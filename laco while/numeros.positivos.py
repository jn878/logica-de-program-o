import os
os.system("cls")


soma = 0
quantidade = 0

while True:
    try:
        numero = int(input("Introduza um número inteiro positivo (ou um número negativo para encerrar): "))
    except ValueError:
        print("Por favor, introduza apenas números inteiros válidos.")
        continue

    if numero < 0:
        break

    soma += numero
    quantidade += 1


if quantidade > 0:
    media = soma / quantidade
    print(f"\nA media aritmética dos {quantidade} números introduzidos e: {media}")
else:
    print("\nNenhum número positivo foi introduzido.")