import os
os.system("cls")

media = float(input("informe a media: "))
falta = int(input("informe o numero de faltas: "))



if media > 7 and falta <40:
    print("\naprovado")
elif media < 7 and falta >40 :
    print("\nreprovado")




