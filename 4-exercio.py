import os
os.system("cls")

nota = float(input("digite sua nota: "))

if nota > 0 and nota <11:
    print(f"\n{nota}")
else:
    print("a nota deve ser entre 0 e 10")
