import os
os.system("cls")
from datetime import date



def calculo(ano_de_nascimento):
    processamento = date.today().year - ano_de_nascimento
    return processamento


print("Solicitando dados")
ano_de_nascimento = float(input("digite seu ano de nascimento:  "))


idade = calculo(ano_de_nascimento)


print("Exibindo dados")
print(f"ano informado: {ano_de_nascimento}")
print(f"idade do usuario: {idade}")