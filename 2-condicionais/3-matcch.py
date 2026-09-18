import os
os.system("cls")

dia = input("digite o dia da semana")

match dia:
    case "segunda":
        print("hoje e segunda feira")
    case "terca":
        print("hoje e terça feira")
    case "quarta":
        print("hoje e quarta feira")
    case "quinta":
        print("hoje e quinta feira")
    case "sexta":
        print("hoje e sexta feira")
    case "sabado" | "domingo":
        print("hoje e fim de semana")
    case _:
        print("dia invalido")


print(dia)