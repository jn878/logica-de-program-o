import os
os.system("cls")

vetor_notas = []
quantidade_nota = 4

for i in range(quantidade_nota):
    nota = float(input(f"nota {i+1} " ))
    vetor_notas.append(nota)


#"sum" somar tudo que esta no vetor
media = sum(vetor_notas) / quantidade_nota
menor_nota = min(vetor_notas)
maior_nota = max(vetor_notas)



if media >= 7:
    print("! aprovado !")
elif media >= 5:
    print("recuperação")
else:
    print("reprovado")

for notas, nota in enumerate(vetor_notas, start=1):
    print(f"{notas} nota : {nota}")

print(f"\nmedia: {media}")
print(f"\nmenor nota: {menor_nota}")
print(f"\nmaior nota: {maior_nota}")
