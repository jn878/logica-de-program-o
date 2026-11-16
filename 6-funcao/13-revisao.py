import os
os.system("cls")
#Função sem retorno e sem parametros
def logo_senai():
    print("==========")
    print("   SENAI    ")
    print("==========")

#Função sem retorno e com parametros
def mostrar_dados(nome, idade):
    print(f" {nome} tem {idade} anos")

#FUNÇÃO SEM RETORNO E SEM PARAMETROS
print("Solicitando dados")
logo_senai()
nome = input("digite seu nome   ")
idade = int(input("digite sua idade "))




logo_senai()
print("exibindo dados")

#Função sem retorno e com parametros
mostrar_dados(nome, idade)