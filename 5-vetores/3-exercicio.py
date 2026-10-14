import os

vetor_notas = []
quantidade_nota = 2

for i in range(quantidade_nota):
    nota = float(input(f"digite a {i+1} nota " ))
    vetor_notas.append(nota)
    
#"sum" somar tudo que esta no vetor
media = sum(vetor_notas) / quantidade_nota

for notas, nota in enumerate(vetor_notas, start=1):
    print(f"{notas} nota : {nota}")
    print(f"\nmedia: {media}")

