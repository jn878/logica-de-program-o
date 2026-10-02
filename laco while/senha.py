import os
import time
os.system("cls")

print("""  cadastro
        crie seu login
        crie sua senha
""")
while True:
    criar_login = input("crie seu login: ")
    criar_senha = input("crie sua senha: ")
    input("pressione enter pra continuar")
    os.system("cls")
    break
while True:
        login = input("digite seu login salvo: ")
        senha = input("digite sua senha salva: ")

        if criar_login == login and criar_senha == senha:
                    print("logado com sucesso")
                    input("aperte enter para ir pra pagina inicial")
                    os.system("cls")
                    break
                    
        else:
                print("algo deu errado, reveja suas informações !")
                print("espere 3 segundos para digitar novamente")
                time.sleep(3)

