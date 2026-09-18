import os 
os.system("cls")

login = input("qual seu nome de usuario: ")
senha = (input("digite sua senha: "))

login_salvo = "andre"
senha_salva = "123"

login_esta_correto = login == login_salvo
senha_esta_correta = senha = senha_salva

if login_esta_correto and senha_esta_correta:
    print("bem vindo")
else:
    print("login ou senha invalidos")


