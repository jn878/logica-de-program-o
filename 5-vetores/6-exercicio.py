import os

vetor_pares_impares = []
QUANTIDADE_DE_NUMEROS = 6
pares = 0
impares = 0


for i in range (QUANTIDADE_DE_NUMEROS):
    numeros = int(input(f"digite {i+1} numero "))
    vetor_pares_impares.append(numeros)



if numeros % 2 == 0:
    pares += 1
else:
    impares += 1

for indice, numeros in enumerate(vetor_pares_impares):
    print(f"numeros {numeros}")

print(f"numeros pares = {pares}")
print(f"numeros impares = {impares}")