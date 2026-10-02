import os
os.system("cls")

soma = 0
quantidade = 2

for i in range(quantidade):
    while True:
        nota = float(input("digite a {i+1} entre 0 e 10 : "))
        if nota <0 or nota > 10:
            print("invalido digite novamente ")
            input("pressione uma tecla pra continuar")
            os.system("cls")
        else:
            soma += nota
            break

media = soma / quantidade
print(f"media {media}")