import os
os.system("cls")

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura * altura)


if imc < 18.5 :
    resultado = print("abaixo do peso")
elif imc <= 24.9:
    resultado = print("peso ideal, parabens")
elif imc <= 29.9:
    resultado = print("levemente acima do peso")
elif imc <= 34.9:
    resultado = print("obesidade grau 1")
elif imc <= 39.9:
     resultado = print("obesidade grau 2(severa)")
else:
    print("obesidade grau 3 (morbida)")

print("\nresultado{resultado}")