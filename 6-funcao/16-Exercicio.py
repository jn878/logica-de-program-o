import os
os.system("cls")




def inflacionar_preco(preco):
    if preco >= 100:
        resultado = preco * 1.20
    else:
        resultado = preco * 1.10
        return resultado


print("SOLICITANDO DADOS")
preco = float(input("Digite o preço do produto "))


preco_inflacao = inflacionar_preco(preco)


print("EXIBINDO DADOS")
print(f"preço do produto = {preco}")
print(f"inflacionado = {preco_inflacao}")