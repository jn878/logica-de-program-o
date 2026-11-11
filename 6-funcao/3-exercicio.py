import os
os.system("cls")

#faça um programa que solicite:
# NOME,EMAIL E TELEFONE
#O PROGRAMA DEVE MANTER NA TELA O LOGO
#    =============
#    SENAI - BAHIA
#    ==============
# O LOGO DE SER EXIBIDO USANDO FUNÇÃO:
# logo_senai()

# OS DADOS DEVERÃO SER APRESENTADOS POR MEIO
# DE UMA FUNÇÃO COM PARAMETROS CHAMADA:
# mostrar_dados(nome, email, telefone)

def logo_senai():
    os.system("cls")
    print("""   =============
                SENAI - BAHIA
                ==============""")

def mostrar_dados(nome,email,telefone):
    print(f"nome {nome} ")
    print(f"email {email} ")
    print(f"telefone {telefone} ")




print("solicitando dados")

nome = input("digite seu nome")
logo_senai()

email = input("digite seu email")
logo_senai()

telefone = input("digite seu telefone")
logo_senai()


logo_senai()
print("exibindo dados")
mostrar_dados(nome,email, telefone)

