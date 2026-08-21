import os

os.system("cls")

print("= solicitando dados =")
nome = input ("digite seu nome: ")
idade = int (input("digite sua idade: "))
primeira_nota = float (input("digite sua primeira nota: "))
segunda_nota = float(input("digite sua segunda nota; "))

media = print("primeira_nota + segunda_nota") / 2

print("\n= Exibindo dados =")
print("Nome: ", nome)
print("idade:", idade)
print("primeira nota: ",primeira_nota)
print("segunda nota: ",segunda_nota)
print("media: ", media)


# \N na execução esse comando pula uma linha