import os
os.system("cls")

nota = 0.0

for i in range(3):
    nota += float(input("digite as notas ")) / 3

print(f"media final {nota}")

if nota > 7:
    print("aprovado")
elif nota < 4:
    print("reprovado")
elif nota >= 4 and nota <7:
    print("recuperação")

