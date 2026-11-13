import os
os.system("cls")

def logo_senai():
    print("==========")
    print("   SENAI    ")
    print("==========")

def mostrar_dados(nome, idade):
    print(f" {nome} tem {idade} anos")

#FUNÇÃO SEM RETORNO E SEM PARAMETROS
print("Solicitando dados")
logo_senai()
nome = input("digite seu nome")
idade = int(input("digite sua idade"))




logo_senai()
print("exibindo dados")
logo_senai()
mostrar_dados(nome, idade)