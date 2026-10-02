import os
os.system("cls")


while True:
    nota = float(input("digite uma nota"))
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        print(f"nota {nota}")
    break