import os
os.system("cls")


quantidade = int(input("escreva a quantidade maçãs: "))



if quantidade < 12:
    preco = 1.30
else:
    preco = 1.0

valor_total = quantidade * preco 


print(F"valor total: {valor_total}")

