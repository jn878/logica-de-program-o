import os
os.system("cls")

soma = 1


for i in range(3):
    while True:
        nota = float(input(f"digite a {i+1} nota do aluno"))
        if nota <0 or nota >10:
            print("entre 0 e 10")

            print("calculos")
            print(f"\nnotas{i}")
            media = soma =+ i /3
            if media > 7:
                print("aprovado")
            elif media > 5 and media < 6.9:
                print("recuperação")
            elif media < 5:
                print("reprovado")

