import os
os.system("cls")



idade = int(input("informe sua idade: "))

if idade < 16:
    print("não pode votar: ")
elif idade < 18:
    print("o seu voto e opicional: ")
elif idade <= 64:
    print("voto obrigatorio")
else:
    print("não e obrigatorio votar")


    
    
