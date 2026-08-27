numero_1 = int(input("escreva um numero: "))
numero_2 = int(input("escreva um numero :"))


soma = numero_1 + numero_2
media = soma / 2
produto = numero_1 * numero_2
if  numero_1 > numero_2:
    maior = numero_1
    menor = numero_2


else:
    maior = numero_2
    menor = numero_1



print(f"\nmedia {media}")
print(f"\nsoma {soma}")
print(f"\nproduto {produto}")
print(f"\nmaior numero: {maior}")
print(f"\nmenor numero: {menor}")
