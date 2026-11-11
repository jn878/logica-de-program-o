import os
os.system("cls")

print("solicitando dados")

def mostrar_saudacao(nome,idade):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    print("Exibindo dados")
    mostrar_saudacao(nome, idade)