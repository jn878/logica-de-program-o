import os
os.system("cls")

notas = []


def calculo(i):
    resultado = soma / 3
    return resultado




print("solicitando dados")
for i in range(3):
    nota = float(input(f"digite a nota {i+1}:   "))
    notas.append(nota)

soma = sum(notas)

media = calculo(i)

print("exibindo dados")
print(f"\nmedia total = {media}")