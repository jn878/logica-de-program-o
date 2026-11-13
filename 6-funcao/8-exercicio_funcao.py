import os
os.system("cls")

def verificar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado



print(" solicitando dados")
numero = int(input("digite um numero    "))

resultado = verificar_par_impar(numero)



print("exibindo dados")
print(f"o numero e {numero} é {resultado}")

