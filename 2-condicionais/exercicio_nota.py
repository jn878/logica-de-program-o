import os
os.system("cls")
nota_1 = float(input("digite sua nota do primeiro semestre : "))
nota_2 = float(input("digite sua nota do segundo semestre : "))
nota_3 = float(input("digite sua nota do terceiro semestre : "))
media = (nota_1 + nota_2 + nota_3)/3
if media > 7:
    print("aprovado")
else:
    print("reprovado")
print("media",media)