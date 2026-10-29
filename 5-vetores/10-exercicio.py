import os

vetor_numero = []

for i in range(5):
    numero = float(input("digite um numero  "))
    vetor_numero.append(numero)

maior = max(vetor_numero)
menor = min(vetor_numero)


for number, numero in enumerate(vetor_numero, start =1):
    print(f"{number} numero : {numero}")

print(f"\nmaior {maior}")
print(f"\nmenor {menor}")
