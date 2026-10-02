import os
os.system("cls")

print("kabum  ssd= 1    rtx 5090 = 2    memoria ram 16gb = 3")






#while True:
    #numero = int(input("digite o numero do pedido: "))
    #if numero == 1:
        #print(f"{numero}  ssd = 10$")
    #elif numero == 2:
        #print(f"{numero}  rtx 5090 = 9$")
    #elif numero == 3:
        #print(f"{numero} memoria ram = 7$")
    #break
#else:
    #print("numero invalido")
    #numero = int(input("digite o numero do pedido: "))


numero = int(input("digite o numero do pedido: "))
while True:
    match numero:
        case "1":
            ssd = 10
            break
        case "2":
            rtx5090 = 9
            break
        case "3":
            memoria = 7
            break
        case _:
            numero = int(input("invalido digite novamente"))
