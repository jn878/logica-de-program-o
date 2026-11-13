import os
os.system("cls")


def operacao1(numero1, numero2):
    soma = numero1 + numero2
    return soma


def operacao2(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao


def operacao3(numero1, numero2):
    if numero1  and numero2 == 0:
        return "Atenção! não e possivel dividir por 0"
    divisao = numero1 / numero2
    return divisao


def operacao4(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao

print("Solicitando dados")
numero1 = float(input("digite um numero "))
numero2 = float(input("digite um numero "))

soma = operacao1(numero1,numero2)
multiplicacao = operacao2(numero1,numero2)
divisao = operacao3(numero1,numero2)
subtracao= operacao4(numero1,numero2)


print("exibindo dados")
print(f"\nsoma: {numero1} + {numero2} = {soma}")
print(f"\nmultiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"\ndivisão: {numero1} / {numero2} = {divisao} ")
print(f"\nsubtração: {numero1} - {numero2} = {subtracao}")