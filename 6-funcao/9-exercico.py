import os
os.system("cls")


def processamento(numero):
    if numero <= 0:
        resultado = "negativo"
    else:
        resultado = "positivo"
    return resultado

print("solicitando dados")
numero = int(input("digite um numero "))

resultado = processamento(numero)

print("exibindo dados")
print(f"o numero e {numero} e {resultado}")