import os
os.system("cls")
contator = 0
valor = 0

while True:
        for i in range(5):
            valor = int(input(f"digite {i+1} valor positivo ")) / 3
        if valor > 0:
            print(f"valores positivos")
        else:
            print("valor negativo, reveja os valores")
            break

print(f"media{nota}")
