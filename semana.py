import os
os.system("cls")

dia = int (input("digite o dia da semana: "))






match dia:
    case 1:
        print("hoje e domingo (fim de semana)")
    case 2:
        print("hoje e segunda  (dia util)")
    case 3:
        print("hoje e terça feira (dia util)")
    case 4:
        print("hoje e quarta feira (dia util)")
    case 5:
        print("hoje e quinta feira (dia util)")
    case 6:
        print("hoje e sexta feira (dia util)")
    case 7:
        print("hoje e sabado (final de semana)")
    case _:
        print("dia invalido")