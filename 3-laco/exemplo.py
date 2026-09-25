import os
os.system("cls")

print("acumulando valores em uma variavel")
soma = 0

print(f"valor inicial da variavel soma: {soma}")
numero = int(input("digite um numero para somar: "))

for i in range (3):
    soma =soma + numero
    print (f"valor da variavel soma : {soma}")

print(f"valor final da variavel soma: {soma}")