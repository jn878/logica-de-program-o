import os
os.system("cls")
pares = 0
impares = 0

for i in range(5):
    valores = int(input("digite um valor"))

if valores % 2 == 0:
    pares += 1
else:
    impares += 1

print(f"\npares {pares}")
print(f"\nimpares {impares}")
