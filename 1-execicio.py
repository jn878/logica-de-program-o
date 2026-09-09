import os
os.systen("cls")

idade = int(input("escreva sua idade"))
sexo = input("escreva seu sexo")

if idade >= 18 and sexo == "masculino":
    resultado = print("deve se apresentar")
else:
    resultado = print("não deve se apresentar")

print(f"resultado:{resultado}")