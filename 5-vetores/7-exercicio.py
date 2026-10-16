import os

vetor_numeros = []
QUANTIDADE_DE_NUMEROS = 5
soma_positivos = 0
quantidade_impares = 0


for i in range (QUANTIDADE_DE_NUMEROS):
    numero = int(input(f"digite o {i+1} numero "))
    vetor_numeros.append(numero)

soma = sum(vetor_numeros)

if numero > 0:
    soma_positivos += numero

if numero % 2 == 1:
    quantidade_impares += 1

print(f"soma = {soma_positivos}")
print(f"quantidade de numeros impares {quantidade_impares}")