import os
os.system("cls")


numero_1 = int(input("digite um numero 1: "))
numero_2 = int(input("digite um numero 2: "))

soma = numero_1 + numero_2
media = soma / 3
produto = numero_1 * numero_2


if numero_1 == numero_2:
    print(f"\nos numeros sao iguais ")
elif numero_1 > numero_2:
    print("o numero 1 e maior ")
else:
    print(f"\no numero 2 e maior  ")



print(f"\nsoma: {soma}")
print(f"\nmedia: {media}")
print(f"\nproduto: {produto}")
