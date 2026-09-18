peso = float(input("digite seu peso: "))
caracter = input("digite o caracter: ")
altura = float(input("digite sua altura: "))



M = (72.7 * altura) - 58
F = (62.1 *  altura) - 44.7

match caracter:
    case "M":
        print(f"PESO IDEAL  {M}")
    case "F":
        print("PESO IDEAL {F}")
    case _:
        print("algo deu errado")
