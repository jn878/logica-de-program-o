import os

print("inserir numeros")
vetor_numeros = []

for i in range(3):
    vetor_numeros.append(5)
    numero = int(input("digite um numero"))


    print(" \nexibindo numeros do vetor ")
for index in range(3):
    print(f"primeira posição do vetor: {vetor_numeros[index]}")
