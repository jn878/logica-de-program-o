import os

vetor_numeros = []
QUANTIDADE_NUMEROS = 5



for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"digite o {i+1} numero "))

if numeros < 0:
    numeros = 0

    vetor_numeros.append(numeros)


for posicao, numeros in  enumerate (vetor_numeros, start = 1):

    print(f"{posicao}) {numeros}")
