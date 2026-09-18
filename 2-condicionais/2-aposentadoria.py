import os
from datetime import date
os.system("cls")

matricula = (input("digite a matricula do empregado: "))
nascimento = int(input("digite a data de nascimento: "))
tempo = float(input("digite o tempo de trabalho: "))

resultado = date.today().year - nascimento

if tempo > 30 and nascimento > 65:
    print("requer aposentadoria")
else:
    print("nao requer aponsentadoria")



print(f"\nresultado  {resultado}")
print(f"\nmatricula  {matricula}")
print(f"\nnascimento  {nascimento}")
print(f"\ntempo  {tempo}")
print(f"data{date.today()}")