import os

vetor_notas = []

for i in range(3):
    nota = float(input(f"digite a {i+1} nota" ))
    vetor_notas.append(nota)

for notas, nota in enumerate(vetor_notas, start=1):
    print(f"{notas} nota : {nota}")

